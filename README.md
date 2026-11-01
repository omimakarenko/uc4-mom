# UC4 SysEx Editor

A web-based configuration editor for the **Faderfox UC4** MIDI controller. Edit all 18 setups, 8 groups, and every parameter without navigating the hardware menus.

**[→ Open Editor](index.html)** · **[→ Usage Guide](UC4_EDITOR_GUIDE.html)**

---

## Features

### Core Editing
- **18 Setups × 8 Groups** — Full access to all 4,752 controls
- **Focused View** — Detailed parameter cards with contextual tooltips
- **Overview Mode** — See all 64 controls per type in an 8×8 grid
- **All View** — See all control types stacked in one scrollable view

### Workflow
- **Import/Export SysEx** — Load from and save to your UC4
- **Import/Export JSON** — Human-readable backups (great for git)
- **Single Setup Export** — Export/import individual setups as JSON
- **Undo/Redo** — Full edit history with coalescing
- **Session Persistence** — Auto-saves to browser storage

### Power Features
- **Setup Manager** — Copy, swap, clear, and label entire setups
- **Quick Copy/Paste** — Rapid cell/row/column operations with Q key
- **Conflict Detection** — Find duplicate MIDI assignments automatically
- **Context Menu Copy/Paste** — Single controls, rows, or columns
- **Paste Special** — Channel offset, CC offset, auto-increment
- **Reset to Factory** — Restore individual setups to factory defaults
- **Contextual Tooltips** — Hover over any parameter for explanations
- **Keyboard Navigation** — Arrow keys, Enter, Tab in Overview mode
- **Link Groups** — Sync encoder and fader group selectors

---

## Quick Start

```
1. Open index.html in your browser
2. Factory defaults load automatically
3. Edit in Focused view or navigate with Overview
4. Export SysEx → send to UC4 via MIDI
```

No installation required. Works entirely in the browser.

---

## Screenshots

### Focused View
Edit individual control parameters with full detail:

```
┌─ FADERS ───────────────────────────────────── GrP1 ─┐
│                                                       │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │
│  │ Fader 1     │  │ Fader 2     │  │ Fader 3     │   │
│  │ Chan [1 ▾]  │  │ Chan [1 ▾]  │  │ Chan [1 ▾]  │   │
│  │ CC   [ 1  ] │  │ CC   [ 2  ] │  │ CC   [ 3  ] │   │
│  │ Type [CCAb] │  │ Type [CCAb] │  │ Type [CCAb] │   │
│  │ Min  [ 0  ] │  │ Min  [ 0  ] │  │ Min  [ 0  ] │   │
│  │ Max  [127 ] │  │ Max  [127 ] │  │ Max  [127 ] │   │
│  └─────────────┘  └─────────────┘  └─────────────┘   │
└───────────────────────────────────────────────────────┘
```

### Overview Mode
See all controls at once, spot conflicts instantly:

```
┌─────────────────────────────────────────────────────────┐
│ [All] [Encoders] [Push] [Green] [Faders]               │
│                                                         │
│ [✓ Concurrent (3)] [Mutually-Exclusive (12)]           │
├─────────────────────────────────────────────────────────┤
│         │ GrP1    │ GrP2    │ GrP3    │ GrP4    │ ...  │
│ Enc 1   │ 1:CC 1  │ 1:CC 1  │ 1:CC 1  │⚠ 1:CC 1 │      │
│ Enc 2   │ 1:CC 2  │ 1:CC 2  │ 1:CC 2  │ 1:CC 2  │      │
│ ...     │         │         │         │         │      │
└─────────────────────────────────────────────────────────┘
```

### Setup Manager
Manage entire setups with labels, copy, swap, and reset:

```
┌─────────────────────────────────────────────────────────┐
│ Setup Manager                                    [×]   │
├─────────────────────────────────────────────────────────┤
│  1: Synth      2: Drums     3: (factory)  4: FX       │
│  5            6: Keys       7            8             │
│  9            10           11           12             │
│  13           14           15           16             │
│  17: Ableton  18: Ableton                              │
├─────────────────────────────────────────────────────────┤
│ [Label] [Clear] [Copy] [Swap] [Reset] [Export] [Import]│
└─────────────────────────────────────────────────────────┘
```

---

## File Formats

### SysEx (.syx)
- **Size:** 100,640 bytes (full dump of all 18 setups)
- **Use:** Transfer to/from UC4 hardware via MIDI

### JSON (Full)
- **Use:** Human-readable backup of all 18 setups
- **Structure:** All setups, groups, and control parameters

### JSON (Single Setup)
- **Format:** `uc4-editor-setup`
- **Use:** Export/import individual setups between files

```json
{
  "format": "uc4-editor-setup",
  "version": "1.0",
  "exported": "2026-01-15T12:00:00Z",
  "sourceSetup": 0,
  "label": "Synth",
  "groups": [...]
}
```

---

## Conflict Detection

The editor automatically detects MIDI assignment conflicts:

| Type | Description | Severity |
|------|-------------|----------|
| **Concurrent** | Same message from controls active simultaneously | ⚠️ Fix these |
| **Mutually-Exclusive** | Same message in different groups | Usually OK |

Filter chips in Overview mode let you show/hide each type.

---

## Keyboard Shortcuts

| Action | Key |
|--------|-----|
| Undo | Ctrl+Z |
| Redo | Ctrl+Shift+Z / Ctrl+Y |
| Copy (Overview) | Ctrl+C |
| Paste (Overview) | Ctrl+V |
| Quick Paste Mode | Q |
| Navigate grid | Arrow keys |
| Jump to Focused | Enter |
| Clear selection | Escape |

### Quick Paste Shortcuts (when active)

| Key | Action |
|-----|--------|
| 1 | Cell scope |
| 2 | Column scope |
| 3 | Row scope |

---

## Browser Compatibility

Tested in:
- Chrome 90+
- Firefox 90+
- Safari 15+
- Edge 90+

Requires JavaScript enabled. No server needed — runs entirely client-side.

---

## Files

| File | Description |
|------|-------------|
| `index.html` | The editor application |
| `UC4_EDITOR_GUIDE.html` | Comprehensive usage guide |
| `UC4_EDITOR_GUIDE.md` | Guide in Markdown format |
| `factory_default.syx` | UC4 factory defaults (auto-loaded) |

---

## UC4 Domain Mapping

Understanding how the UC4 organizes controls:

```
ENCODER DOMAIN (Shift + Encoder 1-8 to switch groups)
├── 8 Encoders
└── 8 Push Buttons (under encoders)

FADER/BUTTON DOMAIN (Shift + Green 1-8 to switch groups)
├── 8 Faders
├── 8 Green Buttons
└── Fader 9 (expression)
```

The editor mirrors this with separate group selectors. Use **🔗 Link** to sync them.

---

## Documentation

- **[Usage Guide](UC4_EDITOR_GUIDE.html)** — Complete walkthrough with examples
- **[HOWTO](HOWTO.md)** — Practical workflows for common tasks
- **[UC4 SysEx Protocol](UC4_SYSEX_PROTOCOL_COMPLETE.md)** — Technical protocol details
- **[Editor Specification](SPECIFICATION.md)** — Technical specification

---

## Version History

See [CHANGELOG.md](CHANGELOG.md) for detailed release notes.

### Current Features (v2.1)
- ✅ Full SysEx editing (all 18 setups, 8 groups)
- ✅ JSON import/export (full and single-setup)
- ✅ Setup Manager with labels, copy, swap, reset
- ✅ Quick Copy/Paste system
- ✅ Contextual tooltips for all parameters
- ✅ Undo/Redo with coalescing
- ✅ Session persistence
- ✅ Overview mode with All view
- ✅ Conflict detection (concurrent + mutually-exclusive)
- ✅ Context menu copy/paste with transforms
- ✅ Keyboard navigation
- ✅ Link groups toggle
- ✅ Reset to factory defaults

---

## License

MIT

---

## Acknowledgments

Built for the Faderfox UC4. Not affiliated with Faderfox.

## Fork additions (uc4-mom)

- **Import > From UC4 (USB MIDI)**: receive a dump straight from the UC4 over Web MIDI (Chrome/Edge). On the UC4: setup mode (Shift + Edit twice), then hold encoder 4 (current setup) or encoder 8 (all setups). Progress shows in the dialog, on the Import button and in the status line at the bottom. A received dump is compared with the editor and with what was last sent.
- **Upload**: send the current setup or all 18 setups to the UC4. Put the UC4 into receive mode first (setup mode, hold encoder 7 until `rC00`). After a single-setup dump is stored the UC4 display shows the setup number (`SE06`).
- **Single-setup SysEx** (5072 bytes, the UC4's own "Sndc" dump) can be imported into any slot and exported.
- **Notes**: names and descriptions for the project, each setup, each encoder group, each fader/button group and each control. Notes are stored in the project, not on the UC4.
- **Project** menu: save/open a whole-device project or a single-setup project (`.uc4proj.json`: SysEx plus notes and labels).

The dump format comes from vehka/uc4-tool (`docs/sysex-format.md`).
