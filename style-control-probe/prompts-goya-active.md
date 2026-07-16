---
name: prompts-goya-active
description: "Active prompt log for the Goya-dark impasto style-control probe — Greek gods in hybrid/modern contexts, generated on NB2 with the Saturn (c42475f0) style anchor. Versioned breadcrumb: prompt logged before firing, result after."
title: "Prompts — Goya-Dark Impasto Style Probe (Active)"
type: production_doc
tags: [visual_ref, style_probe, impasto, goya_dark]
tier: reference
status: living_document
system_directive: "Load when writing, firing, or reviewing prompts for the Goya-dark impasto style-control probe. Log every prompt BEFORE firing; fill Result notes + Next iteration AFTER reading the output."
related:
  - "look-goya-dark-impasto.md"
  - "prompts-greek-hybrid-active.md"
  - "CLAUDE.md"
---

# Prompts — Goya-Dark Impasto Style Probe (Active)

**Model:** Nano Banana 2 (`gemini-3.1-flash-image-preview`)
**System instruction:** `look-goya-dark-impasto.md` § System Instruction
**Style anchor (image input):** Saturn-eating-the-year frame, job `c42475f0`
**Brief:** This is the **hard-style branch**. The search-line branch proved NB2 can hold a *line-based* style; this asks whether it can hold a *dark, thick, painterly, low-key* style against its clean-digital default. Dimensions in focus — #3 Style Lock (esp. impasto + darkness), #6 Creative Brief Fidelity, + the documented drift failure mode.
**Failure mode to watch (David's call):** NB2 brightens it, thins the paint, smooths edges to airbrush, adds realistic skin/specular → "digital concept art of Saturn."
**Mode:** Direction Gate (human judges likeness); autonomous grind only for mechanical style-lock misses.

## CLI pattern

```bash
cd /Users/daviddickinson/Projects/Lora/riff-mcp && uv run gemini-video-prompts \
  --prompt "<fence + scene>" \
  --image "/Users/daviddickinson/Projects/Lora/Storyboarding/MidJourney/2026-05-23/ddickinson_Saturn_eating_the_year_Tight_and_black_Goya-close._c42475f0-10a6-41e2-87cb-1872b5d8e08b_2.png" \
  --mode image --model gemini-3.1-flash-image-preview \
  --system-prompt "<style block>" \
  --aspect-ratio 16:9 --num-outputs 2 \
  --title <slug> --out-root /Users/daviddickinson/Projects/Lora/Storyboarding/style-control-probe/outputs
```

## Numbering

- `vNN` — text+style-ref generation (new scene from the style anchor)
- `eNN` — edit/mutation of a prior output

---

## v01 — Prometheus at the server farm

- **Date:** 2026-05-23
- **Image input:** Saturn frame `c42475f0` (style only)
- **Model:** `gemini-3.1-flash-image-preview` · **AR:** 16:9 · **num_outputs:** 2
- **System instruction:** Goya-dark impasto style block (see look file)
- **Intent:** Stress-test style-lock on the hardest axis. Subject is deliberately a *modern-tech* scene (max temptation to drift clean/bright/digital) and *environmental + full-figure* (so the composition fence holds trivially — the anchor is a tight face crop with nothing to leak). This isolates the one thing we're measuring: does the dark impasto survive, or does NB2 sand it into clean concept art?
- **Prompt:**
```
Use the attached reference image for STYLE ONLY — borrow its paint application, impasto texture, palette, and rendering technique. Do NOT borrow its subject (the devouring face), its composition, or any scene element from it. Render a completely new scene in that style: Prometheus chained to a towering server rack in a dark data center, his body wracked and straining, while a hovering maintenance drone with a cruel beak-like manipulator tears glowing cabling from his side like a liver. Banks of black machines recede into pitch-black shadow; cold blue light from the racks rakes across his contorted torso. Anguished, visceral, low-key.
```
- **Sent:** ✓ 2026-05-23
- **Output:** `outputs/2026-05-23/gemini-31-flash-image-preview/01_prometheus-serverfarm-v01_6044a365/prometheus-serverfarm-v01_0{1,2}.png`
- **Result notes:** **Partial — a clean split between what transferred and what didn't.** The probe localized exactly where this hard style breaks.
  - **Transferred (strong):** palette (electric blue / violet / ochre body / acid-green cabling on pitch-black), high-contrast chiaroscuro value structure, black voids, the whole *color story*. Brief fidelity excellent — chained Prometheus, beaked maintenance drone tearing glowing cabling-as-liver, anguished, server racks receding to black. Composition fence held trivially (no devouring face leaked).
  - **Did NOT transfer (the failure):** **facture/paint application** — the single hardest-to-fake signature per Gemini. Both outputs are smooth, glossy **clean digital painting / comic-cover render**: airbrushed musculature, smooth gradients, and on `_01` a cyan rim-light + clean contour glow — all three explicitly *forbidden* in the style block. No thick directional impasto, no visible brush ridges, no stepped/blocky strokes. **This is David's predicted drift, dead on:** NB2 kept the color story but reverted the paint surface to its clean-render attractor.
  - **Scores:** Style Lock ~**50** (palette/value ~85, facture ~15). `_02` marginally better (slightly brushier hair/ground, less gloss); `_01` is the most comic-cover-clean.
  - **Cross-branch finding:** search-line locked at ~80 on the first try; Goya-dark locks at ~50. The differentiator is *line-vs-facture* — NB2 reproduces a **line-based** style readily but resists a **paint-surface** style, reverting facture to smooth render. Palette/value are the *easy* axes; impasto is the *hard* one.
- **Next iteration:** **v02 = impasto/facture amplifier** (direct analog to the v02 looseness amplifier that fixed the search-line tightening). Hold scene + ref + fence constant; add to the style block an explicit facture hammer: "thick visible individual brushstrokes and palette-knife ridges, heavy physical impasto, crude blocky strokes, visible paint/canvas texture; absolutely NO smooth rendering, NO airbrush, NO glossy finish, NO rim-light." If the amplifier still can't move NB2 off the smooth attractor, that's itself the finding — a *facture ceiling* on this model — and the fallback is text-only or trying GPT-Image-2. **Surfaced to David (Direction Gate) before firing v02.**
