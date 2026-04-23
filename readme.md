# Key Remapper — NVDA add-on

An NVDA add-on that lets you remap any keyboard key (or key combination) to
any other key. Useful for compact laptops missing function keys, arrow
keys, `Insert`, `Applications`, numpad, or media keys — map a key you *do*
have to produce the key you *don't*.

End-user documentation lives in [`doc/en/readme.md`](doc/en/readme.md) and
is bundled with the add-on when it is built.

## Status

* Version: 1.0.0
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

