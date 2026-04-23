# Key Selection Dialog for Key Remapper Addon

import wx
import addonHandler

addonHandler.initTranslation()


# Categories of keys the user can pick from. Grouped for discoverability.
# Names use NVDA's KeyboardInputGesture.fromName() vocabulary.
# Category titles are wrapped in _() at display time, see _build_items().
_KEY_CATEGORIES = [
	# Translators: Category of keys in the key selection dialog.
	(_("Navigation"), [
		"tab", "escape", "backspace", "enter", "space", "applications",
		"upArrow", "downArrow", "leftArrow", "rightArrow",
		"home", "end", "pageUp", "pageDown", "insert", "delete",
	]),
	# Translators: Category of keys in the key selection dialog.
	(_("System"), [
		"pause", "scrollLock", "printScreen", "numLock", "capsLock",
	]),
	# Translators: Category of keys in the key selection dialog.
	(_("Function keys"), [
		"f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8",
		"f9", "f10", "f11", "f12", "f13", "f14", "f15", "f16",
		"f17", "f18", "f19", "f20", "f21", "f22", "f23", "f24",
	]),
	# Translators: Category of keys in the key selection dialog.
	(_("Numpad"), [
		"numpad0", "numpad1", "numpad2", "numpad3", "numpad4",
		"numpad5", "numpad6", "numpad7", "numpad8", "numpad9",
		"numpadPlus", "numpadMinus", "numpadMultiply", "numpadDivide",
		"numpadDecimal", "numpadEnter",
	]),
	# Translators: Category of keys in the key selection dialog.
	(_("Media"), [
		"volumeUp", "volumeDown", "volumeMute",
		"mediaNextTrack", "mediaPrevTrack", "mediaStop", "mediaPlayPause",
	]),
	# Translators: Category of keys in the key selection dialog.
	(_("Browser"), [
		"browserBack", "browserForward", "browserRefresh", "browserStop",
		"browserSearch", "browserFavorites", "browserHome",
	]),
	# Translators: Category of keys in the key selection dialog.
	(_("Launch"), [
		"launchMail", "launchMediaSelect", "launchApp1", "launchApp2",
	]),
	# Translators: Category of keys in the key selection dialog.
	(_("Alt chords"), [
		"alt+f4", "alt+tab", "alt+shift+tab", "alt+space",
		"alt+enter", "alt+home", "alt+leftArrow", "alt+rightArrow",
		"alt+printScreen",
	]),
	# Translators: Category of keys in the key selection dialog.
	(_("Control chords"), [
		"control+c", "control+v", "control+x", "control+z", "control+y",
		"control+a", "control+s", "control+f", "control+n", "control+o",
		"control+w", "control+t", "control+shift+t", "control+tab",
		"control+shift+tab", "control+shift+escape", "control+alt+delete",
		"control+home", "control+end", "control+leftArrow", "control+rightArrow",
		"control+upArrow", "control+downArrow", "control+backspace",
	]),
	# Translators: Category of keys in the key selection dialog.
	(_("Windows chords"), [
		"windows+d", "windows+e", "windows+l", "windows+r", "windows+v",
		"windows+i", "windows+x", "windows+a", "windows+s", "windows+tab",
		"windows+leftArrow", "windows+rightArrow", "windows+upArrow", "windows+downArrow",
		"windows+shift+s", "windows+shift+leftArrow", "windows+shift+rightArrow",
		"windows+control+d", "windows+control+leftArrow", "windows+control+rightArrow",
		"windows+alt+r",
	]),
]


# ----------------------------------------------------------------------
# HOW TO ADD KEYS:
#   Append to one of the lists above. Any string accepted by
#   keyboardHandler.KeyboardInputGesture.fromName() works — e.g.:
#       "f13"                        single key
#       "alt+shift+t"                chord
#       "control+alt+windows+home"   long chord
#   Use "+" to separate. Modifier names: shift, control, alt, windows, NVDA.
# ----------------------------------------------------------------------


def _build_items():
	"""Flatten categories into [(label, key_or_None_for_header), ...]."""
	items = []
	for name, keys in _KEY_CATEGORIES:
		items.append((f"— {name} —", None))
		for k in keys:
			items.append((k, k))
	return items


class KeySelectionDialog(wx.Dialog):
	"""Dialog for selecting a key (or chord) to execute or map to."""

	def __init__(self, parent, title=None):
		super().__init__(
			parent,
			title=title or _("Select Key to Execute"),
			style=wx.DEFAULT_DIALOG_STYLE | wx.STAY_ON_TOP | wx.RESIZE_BORDER,
		)

		main_sizer = wx.BoxSizer(wx.VERTICAL)

		# Filter box for quick search — proper StaticText label so NVDA reads it.
		filter_label = wx.StaticText(self, label=_("&Filter:"))
		main_sizer.Add(filter_label, flag=wx.LEFT | wx.TOP, border=10)
		self._filter = wx.TextCtrl(self)
		self._filter.SetName(_("Filter"))
		main_sizer.Add(self._filter, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
		self._filter.Bind(wx.EVT_TEXT, self._on_filter)
		self._filter.Bind(wx.EVT_KEY_DOWN, self._on_filter_key)

		# Labelled list as well.
		list_label = wx.StaticText(self, label=_("&Keys:"))
		main_sizer.Add(list_label, flag=wx.LEFT, border=10)
		self._items = _build_items()
		self._key_list = wx.ListBox(self, style=wx.LB_SINGLE)
		self._key_list.SetName(_("Keys"))
		self._populate("")
		main_sizer.Add(self._key_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
		self._key_list.Bind(wx.EVT_LISTBOX_DCLICK, self._on_execute)

		button_sizer = wx.BoxSizer(wx.HORIZONTAL)
		ok_button = wx.Button(self, wx.ID_OK, _("Select"))
		button_sizer.Add(ok_button)
		cancel_button = wx.Button(self, wx.ID_CANCEL, _("Cancel"))
		button_sizer.Add(cancel_button, flag=wx.LEFT, border=10)
		main_sizer.Add(button_sizer, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)

		ok_button.Bind(wx.EVT_BUTTON, self._on_execute)
		ok_button.SetDefault()

		self.SetSizer(main_sizer)
		self.SetMinSize((380, 520))
		self.Centre()
		self._filter.SetFocus()

	def _populate(self, needle):
		needle = needle.strip().lower()
		self._visible = []
		self._key_list.Clear()
		for label, key in self._items:
			if key is None:
				if not needle:
					self._key_list.Append(label)
					self._visible.append((label, None))
				continue
			if not needle or needle in key.lower():
				self._key_list.Append(label)
				self._visible.append((label, key))
		# Auto-select first selectable row.
		for i, (_lbl, k) in enumerate(self._visible):
			if k is not None:
				self._key_list.SetSelection(i)
				break

	def _on_filter(self, event):
		self._populate(self._filter.GetValue())

	def _on_filter_key(self, event):
		# Down arrow in filter field → jump to list for easy keyboard navigation.
		if event.GetKeyCode() == wx.WXK_DOWN:
			self._key_list.SetFocus()
			return
		event.Skip()

	def _on_execute(self, event):
		if self.get_selected_key():
			self.EndModal(wx.ID_OK)

	def get_selected_key(self):
		sel = self._key_list.GetSelection()
		if sel == wx.NOT_FOUND:
			return None
		_label, key = self._visible[sel]
		return key
