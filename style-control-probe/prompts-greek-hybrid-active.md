---
name: prompts-greek-hybrid-active
description: "Active prompt log for the search-line style-control probe — Greek gods in hybrid/modern contexts, generated on NB2 with the Hephaestus style anchor. Versioned breadcrumb: prompt logged before firing, result after."
title: "Prompts — Search-Line Style Probe (Active)"
type: production_doc
tags: [visual_ref, style_probe, search_line]
tier: reference
status: living_document
system_directive: "Load when writing, firing, or reviewing prompts for the search-line style-control probe. Log every prompt BEFORE firing; fill Result notes + Next iteration AFTER reading the output."
related:
  - "look-search-line-expressionism.md"
  - "CLAUDE.md"
---

# Prompts — Search-Line Style Probe (Active)

**Model:** Nano Banana 2 (`gemini-3.1-flash-image-preview`)
**System instruction:** `look-search-line-expressionism.md` § System Instruction
**Style anchor (image input):** Hephaestus frame, job `054e808b`
**Brief:** does NB2 reproduce the search-line *hand* on a NEW subject? Dimensions in focus — #3 Style Lock, #6 Creative Brief Fidelity, + subject-leakage check.
**Mode:** Direction Gate (human judges likeness); autonomous grind only for mechanical style-lock misses.

## CLI pattern

```bash
cd /Users/daviddickinson/Projects/Lora/riff-mcp && uv run gemini-video-prompts \
  --prompt "<fence + scene>" \
  --image "<abs path to Hephaestus frame>" \
  --mode image --model gemini-3.1-flash-image-preview \
  --system-prompt "<style block>" \
  --aspect-ratio 16:9 --num-outputs 2 \
  --title <slug> --out-root <repo>/style-control-probe/outputs
```

## Numbering

- `vNN` — text+style-ref generation (new scene from the style anchor)
- `eNN` — edit/mutation of a prior output

---

## v01 — Hermes the bike courier

- **Date:** 2026-05-23
- **Image input:** Hephaestus frame `054e808b` (style only)
- **Model:** `gemini-3.1-flash-image-preview` · **AR:** 16:9 · **num_outputs:** 2
- **System instruction:** search-line style block (see look file)
- **Intent:** Test image-based style transfer onto a subject compositionally unlike the forge. Style lands → transfer works; forge/figure bleeds → over-anchoring.
- **Prompt:**
```
Use the attached reference image for STYLE ONLY — borrow its line quality, palette, texture, and rendering technique. Do NOT borrow its subject (the bearded glassblower), its forge, its composition, or any scene element from it. Render a completely new scene in that style: Hermes as a modern bike courier mid-sprint, standing on the pedals, weaving his bicycle through gridlocked city traffic. Winged sneakers, a messenger bag spilling glowing parcels, scarf and limbs streaking with motion. Stalled cars and exhaust haze around him, chaotic energetic street. Dynamic diagonal composition, strong sense of speed.
```
- **Sent:** ✓ 2026-05-23
- **Output:** `outputs/2026-05-23/gemini-31-flash-image-preview/01_hermes-courier-v01_60e98caa/hermes-courier-v01_0{1,2}.png`
- **Result notes:** **PASS on the core question — NB2 reproduces the search-line hand on a new subject.** Both outputs are clearly in-family: scratchy multi-stroke ink contours, flat misregistered gouache, limited high-contrast palette, paper grain.
  - `_01` is the closer match to the anchor — cobalt/lavender/orange/yellow palette, more dry-brush misregistration and tooth, convincing Mielgo/Searle read. **Style Lock ~80.**
  - `_02` is warmer (yellow/orange/red) and a touch *tighter/cleaner* — drifts toward polished graphic-novel. **Style Lock ~72.** Diagnosis: **style drift** — the model tightens the loosest gestural register (matches `phase-0/FINDINGS.md` "linework trends tight"). This is the residual gap, as predicted for Family A/G1.
  - **Leakage check:** composition fence HELD — no forge, fresh composition in both. `_01` shows a bearded/long-haired figure — possible faint *archetype* echo of the bearded glassblower; `_02` is clean (helmeted, clean-shaven). No hard subject bleed.
  - **Prompt fidelity:** both hit Hermes / bike / courier / winged sneakers / glowing parcels / traffic / motion. `_02` reads "mid-sprint speed" best (ground motion-lines); `_01` strongest on palette.
- **Next iteration:** Direction Gate — surfaced to David to judge likeness. Candidate next move (v02): push the *looseness* harder to close the tightening gap — emphasize "raw, unfinished, heavy dry-brush, scribbled overlapping construction lines, exposed paper, frantic energy" — and/or A/B a text-only run (drop the image ref) to test whether the image is helping or capping the looseness.

---

## v02 — Hermes the bike courier (looseness pushed)

- **Date:** 2026-05-23
- **Image input:** Hephaestus frame `054e808b` (style only) — held constant from v01
- **Model:** `gemini-3.1-flash-image-preview` · **AR:** 16:9 · **num_outputs:** 2
- **System instruction:** v01 style block **+ looseness amplifier** (only changed variable): "Emphasize the RAW, UNFINISHED planning-sketch register: heavy dry-brush drag, scribbled overlapping search/construction lines left visible, color blocks crudely offset from the linework, large areas of exposed off-white paper, splatter and smudge, frantic gestural energy. A working sketch, not a polished plate."
- **Intent:** Close the v01 tightening gap (style drift toward polished). Isolate the looseness variable — same scene, same ref, same fence.
- **Prompt:** _(identical to v01)_
- **Sent:** ✓ 2026-05-23
- **Output:** `outputs/2026-05-23/gemini-31-flash-image-preview/01_hermes-courier-v02-loose_a9f44434/hermes-courier-v02-loose_0{1,2}.png`
- **Result notes:** **Looseness amplifier worked — the v01 tightening gap is largely closed.** Both v02 outputs are visibly rougher than v01: more visible scratchy search/construction strokes, exposed off-white paper, smudgy dry-brush smoke, crude offset color. Reads as reportage *working sketch* (Searle/Mielgo register) rather than polished plate. **Style Lock ~85–88** (v02_02 the most frantic/anchor-true yet). Palette holds (cobalt/purple/ochre/orange/cream). Leakage: none — fresh composition, no forge, no hard figure bleed. Prompt fidelity intact (courier/bike/bag/glowing parcels/traffic/motion).
- **Next iteration:** **Style capture is proven.** Two reusable findings: (1) NB2 reproduces the search-line hand on new subjects; (2) its default tightening is correctable with an explicit looseness amplifier — so the amplifier should be **promoted into the look's System Instruction** for this style (pending David's nod). Then move to v03+: fire selected myth × matter / structure collisions to test the style across varied subjects.
