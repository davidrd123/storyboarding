---
name: look-search-line-expressionism
description: "Visual look spec + system instruction for the 'search-line expressionism' style anchored on the Hephaestus MidJourney frame (job 054e808b). The style block image-gen models load to reproduce this hand."
title: "Look — Search-Line Expressionism (Hephaestus anchor)"
type: production_doc
tags: [visual_ref, style_probe, search_line]
tier: reference
status: exploratory
system_directive: "Load when generating any image in the search-line expressionism style. This is the base look — its System Instruction is the style block; layer the per-prompt scene + borrow-style-only fence on top (see Stack Order)."
related:
  - "prompts-greek-hybrid-active.md"
  - "../MidJourney/2026-05-21/G1-search-line-expressionism/"
---

# Look — Search-Line Expressionism (Hephaestus anchor)

> **Status: EXPLORATORY.** We are testing whether NB2 / GPT-Image-2 can *reproduce* this look on new subjects. Not yet a locked production style.

## Source anchor

`MidJourney/2026-05-21/G1-search-line-expressionism/ddickinson_Hephaestus_the_glassblower_the_forge_is_a_roaring__054e808b-…_2.png` — job `054e808b`. One frame from one MidJourney job (the only guaranteed same-style unit). Family G1; illustrator associations from Gemini calibration: **Alberto Mielgo / Ronald Searle / Ralph Steadman** (associations, not certainties — use as prompt seeds).

## The five discriminating axes (calibrated against Gemini 3.5 Flash comparative analysis)

- **Line discipline:** loose, scratchy, multi-stroke "search lines" — overlapping construction strokes, varying weight, visible jitter. NOT clean continuous contour.
- **Color-to-line registration:** flat opaque gouache blocks that *deliberately misregister* — bleed past or fall short of the linework, leaving dry-brush edges and exposed off-white paper.
- **Texture / finish:** grainy, toothy, matte; dry-brush drag; paper tooth. No smooth gradients.
- **Palette logic:** restricted high-contrast — cobalt blue, cadmium orange, glowing yellow, ochre, lavender, deep black, on off-white paper.
- **Value structure:** high-contrast, bold dark accents; energetic rather than tonal.

## System Instruction (the style block — constant across prompts)

> A loose, energetic search-line illustration. Forms built from scratchy, multi-stroke black ink/charcoal contour lines with visible overlapping construction strokes and varying weight. Flat, opaque gouache color in bold blocks that deliberately misregister — bleeding past or falling short of the linework, leaving dry-brush edges and exposed off-white paper. Restricted high-contrast palette: cobalt blue, cadmium orange, glowing yellow, ochre, lavender, deep black on off-white paper. Grainy, toothy, matte texture; dry-brush drag. Neo-expressionist editorial illustration — gestural, hand-made. No smooth gradients, no photorealism, no clean vector lines.

## Reference grammar (the borrow-style-only fence — prepend to every scene prompt)

> Use the attached reference image for STYLE ONLY — borrow its line quality, palette, texture, and rendering technique. Do NOT borrow its subject, its composition, or any scene element from it.

This is the `phase-0/FINDINGS.md`-validated fence. The nano-banana-pro skill warns a style ref tends to drag its composition along (over-anchoring); the fence + a strong text style block is the first mitigation. If the source frame's subject/composition still leaks, fall back to **text-only** style (drop the image, lean on the System Instruction).

## Stack Order

**System Instruction (this look) → per-prompt: borrow-style-only fence + new scene description.**
