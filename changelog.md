# Changelog

## 1.0.0 — Initial release

* Create key mappings with `NVDA+Shift+X`
  * Single press: press source key, then press target key.
  * Double press: press source key, then pick the target from a searchable
    categorized dialog.
* Execute mappings with `NVDA+X`
  * Single press: press the source key to send its mapped target.
  * Double press: pick any known key from the dialog and send it directly.
* Mappings persist across NVDA restarts (stored under the `keyRemapper`
  section of NVDA's configuration as JSON).
* Filterable, categorized key selection dialog covering Navigation, System,
  Function keys, Numpad, Media, Browser, Launch, and Alt / Control / Windows
  chord groups.
* Own toggle gestures (`NVDA+Shift+X`, `NVDA+X`) are protected from capture
  to prevent accidental self-lockout.
* Pure-modifier presses are ignored during capture — a real non-modifier
  key must be pressed before a chord is captured.
* All user-visible strings wrapped with `_()` and ready for extraction via
  NVDA's standard gettext workflow.
