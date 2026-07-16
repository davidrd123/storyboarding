---
name: hephaestus-forge-bible
description: "Scene bible + asset-lock index for Hephaestus's forge (Beat 1 of 'Gods in the Machine'). Canonical character/asset specs, the locked reference sheets, the approved board, and the final-approved panel manifest. The single source of truth fed into every panel generation."
type: scene_bible
status: building
related:
  - "../hephaestus-gods-in-the-machine.md"
  - "../../patterns/coverage-discovery-schema.md"
  - "../../style-control-probe/prompts-hephaestus-kit-active.md"
  - "../../style-control-probe/LOG.md"
---

# Scene Bible — Hephaestus's Forge (Beat 1)

> **Why this exists.** The first kit drifted (6/9 panels failed cross-panel QC: the automaton head changed design per panel, Hephaestus's age/costume wandered) because the characters were specified in *words* and each panel reinvented them. This bible holds the **asset-lock**: canonical *reference images* of each asset, fed into every panel so the model copies the design instead of re-inventing it. (This is the Phase-0 step our own `coverage-discovery-schema.md` prescribes and the first kit skipped.)
>
> **Image posture.** Per repo policy (`.gitignore`: all images local-only), the actual `.png` files in `refs/`, `board/`, `panels-final/` are **not committed** — they live on disk locally. This markdown is the tracked index; it points to those local files by path.

## Source of truth
- **Original MidJourney frame (style anchor + asset source):** `../../MidJourney/2026-05-23/ddickinson_Hephaestuss_automata_assembly_line_a_long_industri_3c793ade-f764-4e6b-9097-f60fec91e3c1_0.png`
- **Story / full bible:** `../hephaestus-gods-in-the-machine.md` (canonical specs §"Character & Asset Bible", L64–70)

## Current production stance

**NB-Pro is not the required path.** It was the clean-surface route, but the kit kept creating enough identity/design drift that the next agent should not blindly continue NB-Pro regeneration.

**Current stable baseline:** `../../style-control-probe/outputs/2026-05-24/kit-gpt/panel-01..09.png` — the GPT-Image-2 kit held the strongest 9-panel consistency. Its known tradeoff is gritty/noisy surface, not cross-panel story or asset continuity.

**Decision before more generation:** review the GPT kit against this bible and choose whether to accept/fix its surface or deliberately re-enter NB-Pro for targeted panel repairs with the locked refs below. The NB-Pro panel table is route diagnostics, not a mandate.

## Canonical asset specs (locked)

### HEPHAESTUS — *identity anchor for every shot*
- Middle-aged smith (NOT an elder — the panel-03 "white-haired" redo was a drift).
- Broad, stooped build; **favors one leg (lamed)** — his defining trait, must read in full-body shots.
- Fair / blond shoulder-length hair; full beard.
- Pale cream work-robe off one shoulder.
- Expression: weary, tender, watchful.
- **Lameness** ("favors one leg") is canonical but NOT visible in any source frame (all coverage is upper-body) — left OFF the sheet and directed per-shot, so we don't invent a leg design that becomes accidental canon.
- **Sheet:** `refs/hephaestus-character-sheet.png` ✅ LOCKED — NB-Pro 2K, anchored on a clean crop of the GPT board's panel-3 (smith CU); spec authored by Gemini 3.5-flash reading the source. Gemini-certified clean (no GPT grit) + consistent across front/¾/back.

### THE GOLD AUTOMATON — *the army + the hero "woken unit" share one design*
*(Spec CORRECTED 2026-05-24 via Gemini reading the actual pixels — the earlier "smooth serene face + hand-wrought seams" text was a loose human read. Locked to the working-canonical GPT board's "Variant A".)*
- **Head:** cylindrical, helmet-like skullcap separated from the face by a distinct **horizontal forehead seam**; rigid blocky side panels frame the face.
- **Face:** stylized Greco-Roman mask — **hollow pupil-less almond eyes**, straight prominent nose, flat horizontal-line mouth, strong squared jaw. (NOT a featureless blank mannequin, NOT a faceless barrel/canister, NOT a C-3PO dome, NOT a crown/crest.)
- **Surface:** brass/burnished gold, **semi-polished brushed metal with painterly facets** (not mirror-chrome, not dead matte); warm-gold highlights, blue-teal reflected shadow.
- **Construction:** circular **ball-and-socket shoulder joints**; neck/collar seam. Broad blocky shoulders, thick cylindrical neck, tapered torso.
- Mass-produced, every figure identical. The hero "woken unit" is *indistinguishable from the army until its eyes open.*
- **Sheet:** `refs/automaton-model-sheet.png` ✅ LOCKED — NB-Pro 2K, anchored on a clean crop of the GPT board's panel-5 (automaton CU). Gemini-certified clean + consistent across front/¾/back.

### WORLD (constant across panels)
- Vast cavernous forge-hall, cool electric-blue/violet gloom, volumetric haze, a tall red furnace column.
- A long assembly line of identical gold automata receding to a vanishing point; beyond it, the dark of the maw.
- Overhead articulated welder-arms throwing orange sparks.

### STYLE
- Painterly cinematic concept-art (cool blue/violet + warm gold + orange spark-light). Not photoreal, not litho. Clean intentional surface (no draft grain/noise).

## Approved board
- `board/` — the clean controlled coverage board, once re-approved against the locked assets. _(pending)_

## NB-Pro candidate diagnostics (Beat 1, 9-up coverage)
| Panel | Shot | Source kit | Status |
|------:|------|-----------|--------|
| 01 | Wide establisher | kit-nbpro | NB-Pro flagged: Hephaestus duplicated |
| 02 | Medium, lifting an automaton | kit-nbpro | NB-Pro candidate: clean |
| 03 | CU Hephaestus | kit03-nbpro-redo | NB-Pro flagged: re-pin age (skewed too old) |
| 04 | Insert, hands on automaton face | kit-nbpro | NB-Pro flagged: anatomy / extra arm |
| 05 | CU automaton face | kit-nbpro | NB-Pro flagged: crest/headgear drift |
| 06 | Low angle, ranks | kit-nbpro | NB-Pro candidate: clean |
| 07 | Insert, welder spark | kit-nbpro | NB-Pro candidate: clean |
| 08 | OTS down the ranks | kit-nbpro | NB-Pro flagged: C-3PO dome drift |
| 09 | Final wide, alone among ranks | kit-nbpro | NB-Pro flagged: blank mannequins |

_Source kits live in `../../style-control-probe/outputs/2026-05-24/` (gitignored). This table records why the NB-Pro branch was parked; it is not the current default work plan._
