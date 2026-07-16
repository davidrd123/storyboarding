---
name: look-litho-crayon-duotone
description: "Visual look spec + system instruction for the 'Die Brücke litho-crayon duotone' style anchored on the Cerberus-turnstiles MidJourney frame (job 8f5831c8). Expressionist stone-lithograph print look: tri-tone, crumbling crayon line, ink-starvation grain. A print-process branch of the style-control probe."
title: "Look — Die Brücke Litho-Crayon Duotone (Cerberus anchor)"
type: production_doc
tags: [visual_ref, style_probe, lithograph, die_bruecke, duotone]
tier: reference
status: exploratory
system_directive: "Load when generating any image in the Die Brücke litho-crayon duotone style. This is the base look — its System Instruction is the style block; layer the per-prompt scene + borrow-style-only fence on top (see Stack Order)."
related:
  - "prompts-litho-active.md"
  - "look-search-line-expressionism.md"
  - "../MidJourney/2026-05-23/"
---

# Look — Die Brücke Litho-Crayon Duotone (Cerberus anchor)

> **Status: EXPLORATORY.** A *print-process* branch of the probe. The question is no longer "line vs. paint" but whether NB2 can fake a **printmaking substrate** — the texture of ink on stone-pressed paper — rather than reverting to a clean digital surface.

## Source anchor

`MidJourney/2026-05-23/ddickinson_Cerberus_turnstiles_-_the_three_heads_as_security__8f5831c8-…_0.png` — job `8f5831c8`. A duotone lithograph: a coated figure watching a crowd file past a dog-head poster in a station. Gemini reads it as **Die Brücke Expressionist / Symbolist printmaking — Munch, Kirchner, Nolde — multi-color stone lithography**. Prompt seeds, not certainties.

## The five discriminating axes (calibrated against Gemini 3.5 Flash, comparative vs. the G1 search-line anchor)

- **Line discipline:** Thick, blunt, **greasy crumbling litho-crayon** on textured stone — no fine detail, no sharp vector precision. The line drags and breaks up.
- **Color-to-line registration:** Flat, stencil-like color blocks printed *behind* a dark key-line layer; registration **slightly offset**, leaving unprinted warm-cream paper borders at the edges.
- **Texture / finish:** Coarse organic **paper tooth**; imperfect ink coverage. Dark areas show **"ink starvation"** — speckled paper grain breaking through the ink; backgrounds have a soft, dusty, hand-rolled ink texture.
- **Palette:** Restricted, low-saturation **tri-tone** — warm cream (paper substrate) + dusty rose-pink + deep Prussian blue, with a *single* muted terracotta-red accent. Nothing else.
- **Value structure:** Stark, flat, high-contrast **graphic shapes**. Form from flat silhouettes + heavy outlines. No gradients, no digital glow, no volumetric/ambient shading.

**Hardest-to-fake signature:** the **imperfect ink-to-paper transfer** — dark shapes are not solid fills; they carry microscopic organic white speckling where heavy ink failed to seat in the deep wells of textured paper. Per the Gemini deep-read (below), this is produced by **heavy dragging crayon pressure that lets the stone grain break the ink**, not by a fill.

## Gemini deep-read (open-ended reproduction recipe — supersedes the 5 axes where they conflict)

A second, *unstructured* Gemini pass (`describe`-style, no axis cage) characterized the anchor as a **3-color transfer lithograph on grained limestone**, lineage **Symbolist / Les Nabis / Toulouse-Lautrec** as well as Die Brücke. Levers the 5-axis read missed:

- **Tool + gesture:** a No. 2–3 **tusche litho-crayon**; mark-making is **pressure-differentiated** — heavy *dragging* pressure on foreground darks (grain breaks the ink into dense speckle, never a flat pool), rapid *light* gestural strokes midground, blocky/primitive strokes on the focal element. **Tone comes only from crayon pressure over grain** — no cross-hatching, no gradients.
- **Edges:** soft, slightly feathered, *greasy* — never sharp/incised/vector.
- **Print order + registration:** pink tint block → terracotta-red spot → blue-black key plate, printed in that order with **loose registration** so the pink underlay peeks past or short of the key lines.
- **Draftsmanship (a key NB2 tell):** perspective and architecture are **loose, organic, hand-drawn — NOT mathematically straight**. NB2's ruler-straight perspective lines read as "too digital."
- **Plate artifacts:** quick handwritten plate markings / a date in a corner, drawn with the same crayon.

Independent Gemini grade of v01 `_02`: **78/100** — palette + layering + print-presentation captured; lines too clean, dark fills flat (no grain/speckle), perspective too precise.

## System Instruction (the style block — constant across prompts)

> A late-19th / early-20th-century multi-color transfer lithograph on grained limestone, in the spirit of Munch, Kirchner, Nolde, the Nabis, and Toulouse-Lautrec. Forms drawn with a No. 2–3 tusche litho-crayon, its line greasy, blunt, dragging and crumbling on coarse stone — soft feathered edges, no fine detail, no clean vector edges, no anti-aliasing. Mark-making is pressure-differentiated: heavy dragging pressure on foreground darks so the stone grain breaks the ink into dense speckle (never a flat solid fill), light rapid gestural strokes elsewhere; all tone built from crayon pressure over grain, never from gradients or cross-hatching. Three flat stencil-like color blocks printed in order — dusty rose-pink tint, then a single muted terracotta-red spot, then the deep Prussian blue-black key plate — with loose registration so the pink underlay peeks past or short of the key lines, leaving unprinted warm-cream paper borders. Coarse organic paper tooth throughout; visible "ink starvation" — speckled cream paper grain breaking through every dark area. Perspective and architecture are loose, organic, and hand-drawn — never mathematically straight or ruler-precise. Restricted low-saturation tri-tone palette: warm cream paper, dusty rose-pink, deep Prussian blue, with at most one muted terracotta-red accent. Stark, flat, high-contrast graphic shapes; form from flat silhouettes and heavy outlines. Absolutely no gradients, no digital glow, no volumetric shading, no specular highlights, no photorealism, no flat opaque digital fills, and never a sterile pure-white background — the substrate is always warm fibrous aged-cream paper.

## Reference grammar (the borrow-style-only fence — prepend to every scene prompt)

> Use the attached reference image for STYLE ONLY — borrow its litho-crayon line quality, its tri-tone palette, its paper grain and ink-starvation texture, and its flat printmaking technique. Do NOT borrow its subject (the watching figure, the crowd, the dog-head poster), its composition, or any scene element from it.

**Failure mode to watch:** the clean-digital attractor again — smooth anti-aliased lines, soft gradients/glow, full-saturation color, added rendering detail, and a sterile white background instead of warm cream. If NB2 drifts clean, escalate a print-process amplifier (grain / ink-starvation / offset-registration hammer) before falling back to text-only or GPT-Image-2.

## Stack Order

**System Instruction (this look) → per-prompt: borrow-style-only fence + new scene description.**
