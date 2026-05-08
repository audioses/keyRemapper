# Key Remapper — NVDA add-on

An NVDA add-on that lets you remap any keyboard key (or key combination) to
any other key. Useful for compact laptops missing function keys, arrow
keys, `Insert`, `Applications`, numpad, or media keys — map a key you *do*
have to produce the key you *don't*.

End-user documentation lives in [`doc/en/readme.md`](doc/en/readme.md) and
is bundled with the add-on when it is built.

## Status

* Version: 1.1.0
* Minimum NVDA: 2023.1
* Last tested NVDA: 2025.2
* Source: https://github.com/audioses/keyRemapper

## Quick feature summary

* `NVDA+Shift+X` — create a mapping (press source key then target key).
  Double press to pick the target from a searchable dialog.
* `NVDA+X` — execute a mapping (press source key, the mapped target is
  sent). Double press to open a dialog and send any known key directly.
* Mappings persist across NVDA restarts (stored in NVDA's config).
* Categorized, filterable key selection dialog covering navigation,
  function, numpad, media, browser, launch, and `Alt` / `Control` /
  `Windows` chord keys.
* All user-visible strings are translatable through NVDA's standard gettext
  workflow.

## Changelog

See [`changelog.md`](changelog.md) for the full version history.

### 1.1.0 — Bugfix

NVDA modifier keys are now captured and used properly.

### 1.0.0 — Initial release

* Create key mappings with `NVDA+Shift+X` (single press: source then target;
  double press: pick target from a searchable categorized dialog).
* Execute mappings with `NVDA+X` (single press: send mapped target; double
  press: pick any known key from the dialog and send it directly).
* Mappings persist across NVDA restarts.
* Filterable key selection dialog covering Navigation, System, Function,
  Numpad, Media, Browser, Launch, and Alt / Control / Windows chord groups.

