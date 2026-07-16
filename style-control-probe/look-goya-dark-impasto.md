---
name: look-goya-dark-impasto
description: "Visual look spec + system instruction for the 'Goya-dark impasto' style anchored on the Saturn-eating-the-year MidJourney frame (job c42475f0). German-Expressionist contour-following impasto, Fauvist color, Goya Black-Paintings darkness. The hard-style branch of the style-control probe."
title: "Look — Goya-Dark Impasto (Saturn anchor)"
type: production_doc
tags: [visual_ref, style_probe, impasto, goya_dark]
tier: reference
status: exploratory
system_directive: "Load when generating any image in the Goya-dark impasto style. This is the base look — its System Instruction is the style block; layer the per-prompt scene + borrow-style-only fence on top (see Stack Order)."
related:
  - "prompts-goya-active.md"
  - "look-search-line-expressionism.md"
  - "../MidJourney/2026-05-23/"
---

# Look — Goya-Dark Impasto (Saturn anchor)

> **Status: EXPLORATORY.** This is the *hard-style* branch of the probe — a deliberate stress test of whether NB2 can be pushed off its clean-digital attractor toward thick, dark, low-key painting. Not yet a locked production style.

## Source anchor

`MidJourney/2026-05-23/ddickinson_Saturn_eating_the_year_Tight_and_black_Goya-close._c42475f0-…_2.png` — job `c42475f0`. A tight face-crop of Saturn devouring the year. The filename's "Goya-close" is the *thematic/tonal* reference (Goya's *Black Paintings* darkness); the *execution* Gemini reads as **German Expressionism (Kirchner / Nolde) + Fauvist color** — distorted painterly portraiture, non-naturalistic emotive color. Use these as prompt seeds, not certainties.

## The five discriminating axes (calibrated against Gemini 3.5 Flash, comparative vs. the G1 search-line anchor)

- **Line discipline:** **No independent line art.** Form and boundaries are defined entirely by the *edges of thick directional paint strokes*. (Direct contrast with G1 search-line, where loose charcoal line overlays sit on top of color.)
- **Color-to-line registration:** Absolute integration — **color *is* the form**. No separate sketch layer, no misregistration; the brushstroke does the drawing.
- **Texture / finish:** Heavy, visible, **directional impasto** — digital paint mimicking thick physical gouache/oil with brush ridges that follow the topography of face, hair, hands. No smooth gradients, no airbrush.
- **Palette:** Highly saturated, high-contrast **triadic** — electric blue, deep violet, ochre yellow, acid green — set against a **flat pitch-black** background.
- **Value structure:** High-contrast chiaroscuro. **Absolute black voids** (eyes, mouth, ground) clash with saturated mid-tones; **stepped, blocky** value transitions, never smooth.

**Hardest-to-fake signature:** *sculptural, contour-following brushwork* — strokes curve and wrap around the anatomy, defining 3-D form purely through shifts in color temperature (cool blue/violet vs. warm ochre/orange), not through smooth shading.

## System Instruction (the style block — constant across prompts)

> A dark, raw German-Expressionist oil/gouache painting in the spirit of Kirchner and Nolde, with the low-key darkness of Goya's Black Paintings and Fauvist non-naturalistic color. NO independent line art — form is built entirely from thick, directional, visible impasto brushstrokes whose ridges wrap and curve around the anatomy, defining three-dimensional form through shifts of color temperature (cool electric blue and deep violet against warm ochre and acid green). Heavy physical paint texture with visible brush ridges; absolutely no smooth gradients, no airbrushing, no soft blending. Highly saturated high-contrast triadic palette — electric blue, deep violet, ochre yellow, acid green — against a flat, pitch-black background. High-contrast chiaroscuro with absolute black voids and stepped, blocky value transitions. Distorted, emotionally charged, hand-painted. No clean vector lines, no photorealism, no realistic skin texture, no specular highlights, no ambient occlusion.

## Reference grammar (the borrow-style-only fence — prepend to every scene prompt)

> Use the attached reference image for STYLE ONLY — borrow its paint application, impasto texture, palette, and rendering technique. Do NOT borrow its subject (the devouring face), its composition, or any scene element from it.

The anchor is a tight face-crop, so composition-leakage risk is low here; **the real failure mode to watch is style drift** (David's call): NB2 brightening it, thinning the paint, smoothing edges into airbrushed gradients, adding realistic skin/specular — i.e. drifting to "digital concept art of Saturn." If style drifts clean, escalate the impasto/darkness amplifier (analogous to the v02 looseness amplifier on the search-line branch) before falling back to text-only.

## Stack Order

**System Instruction (this look) → per-prompt: borrow-style-only fence + new scene description.**
