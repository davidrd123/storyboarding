---
name: prompts-hephaestus-kit-active
description: "Externalized, house-grammar-assembled per-panel prompts for the Hephaestus forge kit (Beat 1 coverage). Patrick-style breadcrumb: prompt logged BEFORE firing. Grammar per deep-research reply01 §5-6; structure per patterns/coverage-discovery-schema.md Phase 4."
type: production_doc
tags: [prompts, kit, hephaestus]
---

# Prompts — Hephaestus Forge Kit (Active)

**Model:** GPT-Image-2 (`gpt-image-2`, size 1536x864, quality high) · **Refs:** Image1 = source style anchor (`MidJourney/2026-05-23/…3c793ade…_0.png`); Image2 = storyboard board (`…01_hephaestus-9up-coverage_c970632f…`). **Prompt = shared PREAMBLE (house grammar + story context + world) + per-panel SHOT.** Shared preamble stored once below; per-panel `.txt` in `outputs/2026-05-24/kit-prompts/`.

## Shared preamble
```
You are reconstructing ONE finished storyboard frame from a full written spec.

REFERENCES (house grammar — borrow / do NOT borrow):
- IMAGE 1 = STYLE REFERENCE (clean original). BORROW: its exact painterly concept-art style, palette, brushwork, finish. DO NOT BORROW: its specific composition or subject arrangement.
- IMAGE 2 = STORYBOARD PAGE of this scene (composition + world). BORROW: the staging/layout of this shot, the world, and cross-shot consistency of the character and the gold automata. DO NOT BORROW: its grid, panels, labels, or any draft grain/noise/texture (treat those as artifacts — render clean and intentional, NOT gritty).

STORY CONTEXT (reason over this): a cast-out smith, Hephaestus, builds golden beings for others — the only Olympian who ever worked, finally needed, taking quiet pride. Beneath the warmth, the first unease: the line never ends and the figures file away and don't return. OPENING register — warm and proud on its face, the dark only glimpsed.

WORLD (constant across all panels — match exactly for consistency): a vast cavernous forge-hall in cool electric-blue and violet gloom, volumetric haze, a tall red furnace column; a long assembly line of identical burnished-gold automata (classical serene blank faces, hand-wrought seams); overhead robotic welder-arms throwing orange sparks; Hephaestus is a bearded, fair-haired smith in a pale cream work-robe off one shoulder.

Render ONE finished full-frame cinematic image, 16:9 — no grid, no panels, no borders, no text, no labels.

THE SHOT — 
```

## v01 — panel 01
- **Shot:** WIDE ESTABLISHER: the whole hall; the line recedes to a distant vanishing point; Hephaestus small lower-left at his station working a fresh automaton; deep one-point perspective; monumental, lonely.
- **Prompt file:** `outputs/2026-05-24/kit-prompts/panel-01.txt`
- **Sent:** _pending_ · **Output:** _pending_ · **Result:** _pending_

## v01 — panel 02
- **Shot:** MEDIUM: Hephaestus at the line, screen-left facing right, lifting and steadying a finished gold automaton; warm pride; the ranks behind him.
- **Prompt file:** `outputs/2026-05-24/kit-prompts/panel-02.txt`
- **Sent:** _pending_ · **Output:** _pending_ · **Result:** _pending_

## v01 — panel 03
- **Shot:** CLOSE-UP (Hephaestus): his weary lined face in three-quarter, looking screen-right toward his work; tender, proud, a flicker of unease; gold automata and spark-glow soft behind.
- **Prompt file:** `outputs/2026-05-24/kit-prompts/panel-03.txt`
- **Sent:** _pending_ · **Output:** _pending_ · **Result:** _pending_

## v01 — panel 04
- **Shot:** INSERT (hands): his hands cradling and finishing a gold automaton's face and shoulder; tactile, intimate; faint tool marks.
- **Prompt file:** `outputs/2026-05-24/kit-prompts/panel-04.txt`
- **Sent:** _pending_ · **Output:** _pending_ · **Result:** _pending_

## v01 — panel 05
- **Shot:** CLOSE-UP (automaton): one gold automaton's serene blank face, three-quarter turned screen-left toward its maker; the first hairline hint of awakening; matte hammered gold, seams; ranks blurred behind so it reads singular.
- **Prompt file:** `outputs/2026-05-24/kit-prompts/panel-05.txt`
- **Sent:** _pending_ · **Output:** _pending_ · **Result:** _pending_

## v01 — panel 06
- **Shot:** LOW ANGLE: looking up at the gold automata looming on the line against the hazy ceiling and the welder-arms; their scale and number.
- **Prompt file:** `outputs/2026-05-24/kit-prompts/panel-06.txt`
- **Sent:** _pending_ · **Output:** _pending_ · **Result:** _pending_

## v01 — panel 07
- **Shot:** INSERT / DETAIL: extreme close-up of a welder-arm tip sparking on a gold seam; molten orange against cool blue; the act of making.
- **Prompt file:** `outputs/2026-05-24/kit-prompts/panel-07.txt`
- **Sent:** _pending_ · **Output:** _pending_ · **Result:** _pending_

## v01 — panel 08
- **Shot:** OVER-THE-SHOULDER: from behind one gold automaton in the foreground, looking past it down the receding ranks of identical others to tiny Hephaestus at his bench; the multitude against the one maker.
- **Prompt file:** `outputs/2026-05-24/kit-prompts/panel-08.txt`
- **Sent:** _pending_ · **Output:** _pending_ · **Result:** _pending_

## v01 — panel 09
- **Shot:** FINAL WIDE: Hephaestus alone among the silent finished gold ranks as a vast shadow begins to fall across them; the first real chill; he is small, the ranks vast.
- **Prompt file:** `outputs/2026-05-24/kit-prompts/panel-09.txt`
- **Sent:** _pending_ · **Output:** _pending_ · **Result:** _pending_

---

## Batch result — fired 2026-05-24 ✓

All 9 fired on **GPT-Image-2** (1536x864, high) from the externalized `panel-NN.txt` prompts; refs = Image1 source style anchor + Image2 storyboard board; 0 failures. Outputs: `outputs/2026-05-24/gpt-image-2/01_hephaestus-kitNN-gpt_*/` (collected in `outputs/2026-05-24/kit-gpt/panel-NN.png`).

**Result: best + most consistent kit of the session.** One world / character / palette / painterly finish across all 9; the 180 eyeline pair (03 looks right ↔ 05 looks left) holds; **grain gone** (the house-grammar `Do NOT borrow: grain/noise/surface` on the composition ref fixed the noise-as-feature bleed). Locked recipe: full-reconstruction prompt (assembled from grammar) + source style-anchor + board context, on GPT-Image-2.
