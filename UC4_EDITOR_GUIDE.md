# UC4 Mom guide

A browser editor for the Faderfox UC4. Everything runs in your browser. Use Chrome or Edge to talk to the UC4 over USB.

## How the UC4 is organised

```
UC4
└── 18 setups
    ├── Encoders & Enc.Buttons      8 groups   (Shift + press an encoder)
    │     8 encoders, each with its own Enc.Button (the encoder push)
    └── Faders & Green Buttons      8 groups   (Shift + press a green button)
          8 faders, Fader 9, 8 green buttons
```

- The two halves switch groups **independently**: you can have encoder group 3 and fader group 1 active together.
- One setup holds 8 x 33 = 264 controls.
- Each group has a 4-character **name** that the UC4 stores (GrP1 ...). Everything else you type here is a **label**.

## Label, description, name

The project name is above the view buttons (click it to rename, the pencil opens the description). The setup label and description are in the setup strip. In Focused, the pencil in a group header opens the 4-character UC4 name, the label and the description of that group. Label edits are part of Undo.


| | Where it lives | Limit |
|---|---|---|
| **Name** of a group | on the UC4 | 4 characters |
| **Label** of a setup, group or control | your project file and this browser, never on the UC4 | 24 (setup) / 60 characters |
| **Description** | your project file | 1000 characters |

The setup label is the same one in the setup list, Setup Manager and the tree.

## Three views

Switch them with the buttons next to **View:** at the top.

**Controller** - a tree on the left (the setups, each with its two halves and their 8 groups), a drawing of the UC4 in the middle, an inspector on the right.
Click a group in the tree to switch to it. Click a control to edit it. Type a label right under a control. Click a tree node to write its label and description.

**Focused** - the same two halves as two blocks. Every parameter is a row: checkbox, value, minus and plus. Pick the group in the tree on the left. The **Tree** button above the blocks hides the tree when you need the room. Collapse a block with the arrow.

**Overview** - one table per kind of control (rows are controls, columns are groups). It works like a spreadsheet. The panel on the right edits what you click:

- one cell: all its parameters
- several cells of one kind: what you change is applied to all of them
- cells of different kinds: only the parameters they share (Chan and CC)

| Do | Result |
|---|---|
| Click | select one cell |
| Shift + click | select a rectangle |
| Ctrl/Cmd + click | add or remove a cell |
| Drag | select a rectangle |
| Click a row or column header | select the whole row or column |
| Ctrl/Cmd + A | select the whole table |
| Ctrl/Cmd + C, Ctrl/Cmd + V | copy, paste |
| Delete, Backspace | put the factory values back into the selected cells |
| Esc | clear the selection |
| Double-click, Enter | open that control in Controller |

Pasting: one copied cell fills every selected cell (set "each next" to add a step to Chan or CC for each cell). A copied block lands with its top-left corner on the top-left selected cell. A paste is one Undo step.

**Reading a cell:** `ch1 CC 8` is MIDI channel 1, controller number 8. `N` is a note, `PC` a program change, `PB` pitch bend, `AT` aftertouch, `rel1` and `rel2` relative encoder modes. `mom` and `tgl` are momentary and toggle buttons. Every view uses the same notation.

## Colours: factory, saved, changed

Everything that can differ is coloured the same way in all views and in the tree:

- **factory** - quiet grey. The value is the same as in the UC4 factory setup. Putting a value back to factory makes it grey again, whatever it was before.
- **saved** - clear colour. The value differs from the factory but is what you loaded or saved last.
- **changed** - bluish. You changed it since the last load, download or save.

## Defaults

An empty or invalid number field gets the factory value back. Every list starts with **Default: ...**, the factory choice. In Overview, **Delete** puts the factory values into the selected cells. Undo brings your values back.

## Editing fast

- **- and +** next to a value change it by 1 (hold Shift for 10). Hold the button to repeat. For lists they move to the previous or next option.
- **Hover a name** (Chan, Type, Mode, Disp ...) to read what it does. For example bPoL shows the value as -63 to +63 around the centre.
- **Batch edit:** tick the checkbox of a parameter on several controls, or use the small buttons above a row ("Chan", "CC" ...) to tick it on all 8. A bar opens at the bottom: **Set** gives every ticked value the same number, **- / +** add a step, **Fill** counts up from a start value (50, 51, 52 ...). "All Chan" ticks the channel of a whole group.
- **Undo** and **Redo** cover everything, including batch edits and pastes.

## Download from the UC4 and Upload to it

**Download** (UC4 to editor)

1. Click **Download**, then **Connect MIDI** and allow access with SysEx.
2. On the UC4: hold Shift and press Edit twice (setup mode), then hold **encoder 4** for the selected setup or **encoder 8** for all 18.
3. The UC4 display counts while it sends. The result appears in the window and in the status line when it is complete. Chrome only shows the result at the end, so there is no progress bar.
4. **Load into editor** for all 18, or **Put into a setup** for one.

**Upload** (editor to UC4)

1. Click **Upload**, **Connect MIDI**.
2. On the UC4: setup mode, choose the target setup with **encoder 1**, then **keep holding encoder 7** until the display shows `rC00`. A short press only shows `rEc` and the data is ignored.
3. Tick "I have a backup", then **Upload Setup N** or **Upload all 18**.
4. Success: the display shows the setup number (for example `SE06`). If it stays on `rC00`, nothing was stored.

A single-setup dump is stored in whichever setup is selected on the UC4. Take a full backup first (Download, all 18, then Project > Export SysEx).

If nothing happens: use Chrome or Edge, close Ableton, SysEx Librarian and other programs that hold the UC4 port, and reconnect the USB cable.

## Project menu and files

| Item | What it does |
|---|---|
| New | start again from the factory setups |
| Open, Save | a **project**: the exact UC4 data plus your labels and descriptions |
| Save this setup | a project with just the current setup |
| Import SysEx, Export SysEx | plain UC4 dump files: all 18 setups or one setup |
| Import JSON, Export JSON (legacy) | the file format of the original UC4 SysEx Editor |
| Import Setup from Library | ready-made setups, see below |

**Cheat sheet** is the button right of Upload: printable pages with the device drawing and your labels, what each control sends, and the descriptions. One screen, one setup or all setups; print to PDF or download HTML.

Use **Save** for your own work. Use SysEx for other tools (SysEx Librarian ...).

**JSON, legacy:** the JSON files are the same format as in the original UC4 SysEx Editor by thegdyne, so you can move a configuration between this program and the original in both directions. JSON holds the parameters and the setup names only: no project name, no descriptions, no control labels. A project file (`.uc4proj.json`) is different: it keeps everything and only opens here.

**Same message** (Overview) shows controls that send the same channel and number. This is often on purpose, for example in different groups, so the filters are off until you switch them on.

## Library

Project > **Import Setup from Library**. Pick a config, then pick where it goes in one list:

- a setup number for a one-setup config (`8`),
- a run for configs that need several setups, for example the Elektron Digitakt II needs two (`8-9`, `9-10` ...).

Setups 17 and 18 are the factory Ableton setups. They are marked "(Ableton)" and you get a warning, but you can still replace them. Undo brings them back.

## Keys

| Keys | Action |
|---|---|
| Ctrl/Cmd + Z | undo |
| Ctrl/Cmd + Shift + Z, Ctrl/Cmd + Y | redo |
| Ctrl/Cmd + C, V, A | copy, paste, select all (Overview) |
| Arrows, Shift + arrows | move or extend the selection (Overview) |
| Enter | open the selected cell in Controller (Overview) |
| Esc | clear the selection |

## Good to know

- The light and dark switch is at the top right.
- Your work is kept in the browser while you edit; **Save** a project to keep it for good.
- A label never reaches the UC4. If you wipe the browser data, labels go with it unless you saved a project.
- The upload progress bar is an estimate. The UC4 does not report progress to the browser.
- The dump format is not documented by Faderfox. It was worked out by the community (see uc4-tool by vehka). UC4 Mom is an independent fork of UC4 SysEx Editor by thegdyne.
