# Key Remapper Addon - Main Global Plugin
# Provides key remapping functionality for NVDA

import json

import globalPluginHandler
import wx
import gui
import tones
import config
import ui
import inputCore
import scriptHandler
from scriptHandler import script
from keyboardHandler import KeyboardInputGesture
import addonHandler

from .keySelectionDialog import KeySelectionDialog

addonHandler.initTranslation()

CONFIG_SECTION = "keyRemapper"

# Register a config spec so config.conf[CONFIG_SECTION] is always available.
config.conf.spec[CONFIG_SECTION] = {
	"mappings": 'string(default="")',
}


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	"""Main global plugin for Key Remapper addon."""

	SCRIPT_CATEGORY = _("Key Remapper")

	def __init__(self):
		super().__init__()
		self._mapping_mode = False
		self._waiting_for_key = False
		self._capture_type = None  # "source", "target", or "execute"
		self._captured_source_key = None
		self._key_mappings = {}
		self._load_config()

	def terminate(self):
		self._cancel_capture()
		self._save_config()
		super().terminate()

	@script(
		description=_("Map a key. Single press: target by keypress. Double press: target from dialog."),
		category=SCRIPT_CATEGORY,
		gestures=["kb:NVDA+shift+x"],
	)
	def script_toggleMappingMode(self, gesture):
		count = scriptHandler.getLastScriptRepeatCount()
		# Single → key-by-key; double (or more) → dialog target.
		target_from_dialog = (count >= 1)
		self._begin_mapping(target_from_dialog=target_from_dialog)

	@script(
		description=_("Execute a mapped key. Single press: by keypress. Double press: pick from dialog."),
		category=SCRIPT_CATEGORY,
		gestures=["kb:NVDA+x"],
	)
	def script_executeMappedKey(self, gesture):
		count = scriptHandler.getLastScriptRepeatCount()
		if count == 0:
			# Single — press a key to execute its mapping.
			if self._mapping_mode:
				return
			self._cancel_capture()
			self._capture_type = "execute"
			self._start_capture()
			ui.message(_("Press the key to execute"))
		else:
			# Double — cancel the single-press capture and open the dialog.
			self._cancel_capture()
			self._mapping_mode = False
			self._capture_type = None
			self._captured_source_key = None
			wx.CallAfter(self._open_key_selection_menu)

	def _begin_mapping(self, target_from_dialog):
		"""Start (or restart) mapping mode with the requested target style."""
		# Swap capture type if a previous press of the same gesture already
		# initiated mapping within the multi-press window.
		self._cancel_capture()
		self._mapping_mode = True
		self._captured_source_key = None
		self._capture_type = "source_for_dialog" if target_from_dialog else "source"
		tones.beep(1000, 100)
		self._start_capture()
		if target_from_dialog:
			ui.message(_("Press the source key, then pick the target from the dialog."))
		else:
			ui.message(_("Press the source key, then press the target key."))

	def _start_capture(self):
		if not self._waiting_for_key:
			self._waiting_for_key = True
			inputCore.decide_executeGesture.register(self._filter_gesture)
		tones.beep(1000, 100)

	def _cancel_capture(self):
		if self._waiting_for_key:
			self._waiting_for_key = False
			try:
				inputCore.decide_executeGesture.unregister(self._filter_gesture)
			except Exception:
				pass

	_MODIFIER_NAMES = frozenset((
		"shift", "control", "alt", "windows", "NVDA",
		"leftShift", "rightShift", "leftControl", "rightControl",
		"leftAlt", "rightAlt", "leftWindows", "rightWindows",
	))

	# Gestures that must never be captured — the plugin's own toggles.
	_PROTECTED_IDENTIFIERS = frozenset((
		"kb:NVDA+shift+x",
		"kb:NVDA+x",
	))

	def _filter_gesture(self, gesture=None, **kwargs):
		if not self._waiting_for_key or not isinstance(gesture, KeyboardInputGesture):
			return True
		# Never swallow our own toggle/execute gestures.
		try:
			if any(i in self._PROTECTED_IDENTIFIERS for i in gesture.identifiers):
				return True
		except Exception:
			pass
		main = gesture.mainKeyName
		# Ignore pure modifier-only presses (wait for the real key).
		if not main or main in self._MODIFIER_NAMES:
			return True
		# Build the full key name including modifiers, e.g. "alt+f4".
		try:
			mods = list(gesture.modifierNames)
		except Exception:
			mods = []
		key_name = "+".join(mods + [main]) if mods else main
		self._cancel_capture()
		wx.CallAfter(self._handle_captured_key, key_name)
		return False

	def _handle_captured_key(self, key_name):
		if self._capture_type == "source":
			self._captured_source_key = key_name
			self._capture_type = "target"
			self._start_capture()
			ui.message(_("Source key captured: {}. Now press the target key.").format(key_name))

		elif self._capture_type == "source_for_dialog":
			self._captured_source_key = key_name
			self._capture_type = None
			ui.message(_("Source key captured: {}. Choose the target from the dialog.").format(key_name))
			wx.CallAfter(self._pick_target_from_dialog)

		elif self._capture_type == "target":
			self._key_mappings[self._captured_source_key] = key_name
			self._save_config()
			tones.beep(1500, 100)
			ui.message(_("Mapping created: {} -> {}").format(self._captured_source_key, key_name))
			self._mapping_mode = False
			self._capture_type = None
			self._captured_source_key = None

		elif self._capture_type == "execute":
			if key_name in self._key_mappings:
				target_key = self._key_mappings[key_name]
				if self._execute_key(target_key):
					tones.beep(1200, 50)
					ui.message(_("Executed mapped key: {} -> {}").format(key_name, target_key))
				else:
					tones.beep(300, 200)
					ui.message(_("Failed to execute mapped key"))
			else:
				tones.beep(300, 200)
				ui.message(_("No mapping found for key: {}").format(key_name))

	def _show_dialog(self, title):
		"""Show the KeySelectionDialog on top and return the chosen key or None."""
		gui.mainFrame.prePopup()
		try:
			dialog = KeySelectionDialog(gui.mainFrame, title=title)
			dialog.Raise()
			result = dialog.ShowModal()
			selected = dialog.get_selected_key() if result == wx.ID_OK else None
			dialog.Destroy()
		finally:
			gui.mainFrame.postPopup()
		return selected

	def _open_key_selection_menu(self):
		selected = self._show_dialog(_("Select Key to Execute"))
		if selected and self._execute_key(selected):
			ui.message(_("Executed key: {}").format(selected))

	def _pick_target_from_dialog(self):
		source = self._captured_source_key
		target = self._show_dialog(_("Select Target Key for {}").format(source or ""))
		if source and target:
			self._key_mappings[source] = target
			self._save_config()
			tones.beep(1500, 100)
			ui.message(_("Mapping created: {} -> {}").format(source, target))
		else:
			ui.message(_("Mapping cancelled."))
		self._mapping_mode = False
		self._capture_type = None
		self._captured_source_key = None

	def _load_config(self):
		self._key_mappings = {}
		try:
			mappings_str = config.conf[CONFIG_SECTION]["mappings"]
		except Exception:
			mappings_str = ""
		if mappings_str:
			try:
				loaded = json.loads(mappings_str)
				if isinstance(loaded, dict):
					self._key_mappings = loaded
			except Exception:
				pass

	def _save_config(self):
		try:
			config.conf[CONFIG_SECTION]["mappings"] = json.dumps(self._key_mappings)
		except Exception:
			pass

	def _execute_key(self, key_name):
		try:
			gesture = KeyboardInputGesture.fromName(key_name)
			if gesture:
				gesture.send()
				return True
		except Exception:
			pass
		return False
