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

| | Where it lives | Limit |
|---|---|---|
| **Name** of a group | on the UC4 | 4 characters |
| **Label** of a setup, group or control | your project file and this browser, never on the UC4 | 24 (setup) / 60 characters |
| **Description** | your project file | 1000 characters |

The setup label is the same one in the setup list, Setup Manager and the tree.

## Three views

**Controller** - a tree on the left (Project, setups, the two halves with their 8 groups), a drawing of the UC4 in the middle, an inspector on the right.
Click a group in the tree to switch to it. Click a control to edit it. Type a label right under a control. Click a tree node to write its label and description.

**Focused** - the same two halves as two blocks with group tabs. Every parameter is a row: checkbox, value, minus and plus. Collapse a block with the arrow.

**Overview** - one table per kind of control (rows are controls, columns are groups). It works like a spreadsheet:

| Do | Result |
|---|---|
| Click | select one cell |
| Shift + click | select a rectangle |
| Ctrl/Cmd + click | add or remove a cell |
| Drag | select a rectangle |
| Click a row or column header | select the whole row or column |
| Ctrl/Cmd + A | select the whole table |
| Ctrl/Cmd + C, Ctrl/Cmd + V | copy, paste |
| Esc | clear the selection |
| Double-click, Enter | open that control in Controller |

Pasting: one copied cell fills every selected cell (set "each next" to add a step to Chan or CC for each cell). A copied block lands with its top-left corner on the top-left selected cell. A paste is one Undo step.

## Editing fast

- **- and +** next to a value change it by 1 (hold Shift for 10). For lists they move to the previous or next option.
- **Hover a name** (Chan, Type, Mode ...) to read what it does.
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

## Project menu

| Item | What it does |
|---|---|
| New | start again from the factory setups |
| Open, Save | a **project**: the exact UC4 data plus your labels and descriptions |
| Save this setup | a project with just the current setup |
| Import SysEx, Export SysEx | plain UC4 dump files: all 18 setups or one setup |
| Import JSON, Export JSON | readable text of all parameters, for sharing or editing by hand (no descriptions) |
| New setup from Library | ready-made setups, see below |

Use **Save** for your own work. Use SysEx for other tools (SysEx Librarian ...). Use JSON for sharing.

## Library

Project > **New setup from Library**. Pick a config, then pick where it goes in one list:

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
