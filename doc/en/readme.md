# Key Remapper

* Author: Ömer Yılmaz
* Version: 1.0.0
* Minimum NVDA version: 2023.1
* Last tested NVDA version: 2025.2
* License: GPL v2 or later
* Source: https://github.com/audioses/keyRemapper

## Overview

Key Remapper is an NVDA add-on that lets you remap any keyboard key (or key
combination) to any other key. It is especially useful when your physical
keyboard is missing keys — for example compact laptop layouts that lack
function keys, arrow keys, `Insert`, `Applications`, a numpad, or media
controls — because it lets you assign a key you *do* have to produce the
keystroke you *don't* have.

Mappings are saved to NVDA's configuration and are restored automatically on
the next start.

## Commands

The add-on exposes two commands. Both are available in NVDA's Input Gestures
dialog under the **Key Remapper** category, where you can reassign them to a
different shortcut if the defaults conflict with something on your system.

### Create a mapping — `NVDA+Shift+X`

Starts mapping mode. A short beep confirms that the add-on is waiting for
input.

* **Single press (`NVDA+Shift+X`)** — press the source key you want to
  remap, then press the target key you want it to produce. A higher beep and
  a spoken confirmation announce that the mapping was saved.
* **Double press (`NVDA+Shift+X` twice quickly)** — press the source key,
  then choose the target from a searchable dialog. Use this when the target
  key is not physically present on your keyboard (that is usually the whole
  point of remapping).

Source and target keys may include modifiers. For example you can map
`F13` → `Alt+F4`, or `Caps Lock` → `Insert`.

### Execute a mapping — `NVDA+X`

Triggers a previously created mapping.

* **Single press (`NVDA+X`)** — press the source key; the add-on sends the
  mapped target key to the active application.
* **Double press (`NVDA+X` twice quickly)** — opens a dialog listing all
  keys the add-on knows about so you can send a key directly, without going
  through a mapping.

If you press a key that has no mapping, a low error beep sounds and NVDA
announces "No mapping found".

## Using the key selection dialog

The dialog that appears on a double press (for either command) shows keys
grouped into categories — Navigation, System, Function keys, Numpad, Media,
Browser, Launch, and chord groups for `Alt`, `Control`, and `Windows`. The
category headings are not selectable; they are there purely to help you
browse.

* **Filter field** — type any part of a key name to narrow the list (for
  example typing `f1` shows `f1` through `f19`, typing `alt` shows all Alt
  chords). Press `Down Arrow` from the filter field to jump directly into
  the results list.
* **Keys list** — move with `Up`/`Down` Arrow, then press `Enter` or
  activate the **Select** button.
* **Cancel** — close the dialog without selecting anything.

## Typical workflows

### Compact laptop with no `F13`

1. Press `NVDA+Shift+X` twice quickly.
2. Press the physical key you want to sacrifice (for example `ScrollLock`).
3. In the dialog, filter for `f13`, select it, press Enter.
4. From now on, `NVDA+X` followed by `ScrollLock` will send `F13`.

### Laptop with no numpad

Map a row of normal keys (for example `1` through `9`) to `numpad1` through
`numpad9` using the single-press workflow — press `NVDA+Shift+X`, press the
source key, press the target key.

### Keyboard with no `Insert` or `Applications`

Use the dialog workflow (`NVDA+Shift+X` twice) to pick `insert` or
`applications` from the **Navigation** category as the target.

## Notes and limits

* `NVDA+Shift+X` and `NVDA+X` themselves cannot be captured as source keys
  — the add-on protects its own shortcuts so you cannot accidentally map
  them and lock yourself out.
* Pure modifier presses (`Shift` alone, `Control` alone, `Alt` alone) are
  ignored while the add-on waits for a key; it waits for a real non-modifier
  key. Press the modifier *together* with another key to capture a chord.
* The target key is sent as a simulated keystroke to the currently focused
  application. Mappings do not rewrite hardware-level key events; they only
  translate when triggered through `NVDA+X`.
* Mappings are global — they are the same across all applications.
* All messages and the key selection dialog are fully translatable through
  NVDA's standard gettext translation system.

## Storage

Mappings are stored as JSON inside NVDA's configuration file, under the
`keyRemapper` section, key `mappings`. Removing that entry (or resetting
NVDA's configuration) clears all mappings.

## Changelog

### 1.0

* Initial release.
* Map keys by keypress or by choosing from a dialog.
* Execute mappings by keypress or pick a key to send directly.
* Searchable, categorized key selection dialog.
* Full translation support.
