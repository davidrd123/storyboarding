---
name: prompts-litho-active
description: "Active prompt log for the Die Brücke litho-crayon duotone style-control probe — Greek gods in hybrid/modern contexts, generated on NB2 with the Cerberus (8f5831c8) style anchor. Versioned breadcrumb: prompt logged before firing, result after."
title: "Prompts — Litho-Crayon Duotone Style Probe (Active)"
type: production_doc
tags: [visual_ref, style_probe, lithograph, die_bruecke, duotone]
tier: reference
status: living_document
system_directive: "Load when writing, firing, or reviewing prompts for the litho-crayon duotone style-control probe. Log every prompt BEFORE firing; fill Result notes + Next iteration AFTER reading the output."
related:
  - "look-litho-crayon-duotone.md"
  - "prompts-greek-hybrid-active.md"
  - "CLAUDE.md"
---

# Prompts — Litho-Crayon Duotone Style Probe (Active)

**Model:** Nano Banana 2 (`gemini-3.1-flash-image-preview`)
**System instruction:** `look-litho-crayon-duotone.md` § System Instruction
**Style anchor (image input):** Cerberus-turnstiles frame, job `8f5831c8`
**Brief:** A **print-process branch**. Can NB2 fake a printmaking substrate — litho-crayon line + tri-tone + paper-grain/ink-starvation — instead of reverting to a clean digital surface? Dimensions in focus — #3 Style Lock (esp. palette restraint + ink grain), #6 Creative Brief Fidelity, + the clean-digital drift failure mode.
**Failure mode to watch:** smooth anti-aliased lines, gradients/glow, full-saturation color, sterile white background instead of warm cream.
**Mode:** Direction Gate (human judges likeness); autonomous grind only for mechanical style-lock misses.

## CLI pattern

```bash
cd /Users/daviddickinson/Projects/Lora/riff-mcp && uv run gemini-video-prompts \
  --prompt "<fence + scene>" \
  --image "/Users/daviddickinson/Projects/Lora/Storyboarding/MidJourney/2026-05-23/ddickinson_Cerberus_turnstiles_-_the_three_heads_as_security__8f5831c8-5e20-4490-bd11-b6e29596a6c4_0.png" \
  --mode image --model gemini-3.1-flash-image-preview \
  --system-prompt "<style block>" \
  --aspect-ratio 16:9 --num-outputs 2 \
  --title <slug> --out-root /Users/daviddickinson/Projects/Lora/Storyboarding/style-control-probe/outputs
```

## Numbering

- `vNN` — text+style-ref generation (new scene from the style anchor)
- `eNN` — edit/mutation of a prior output
- `xNN` — cross-model comparison run (same prompt+ref, different model)

---

## v01 — Sisyphus on the frozen escalator

- **Date:** 2026-05-23
- **Image input:** Cerberus frame `8f5831c8` (style only)
- **Model:** `gemini-3.1-flash-image-preview` · **AR:** 16:9 · **num_outputs:** 2
- **System instruction:** litho-crayon duotone style block (see look file)
- **Intent:** Test style-lock on a compositionally fresh subject. The anchor is a duotone crowd/poster scene; this is a **lone melancholy figure** (Munch register) in a modern collision — different composition, so the fence holds easily and we isolate the print-process axes (tri-tone restraint, crayon line, paper grain). A somber lone subject also plays to the palette's mood.
- **Prompt:**
```
Use the attached reference image for STYLE ONLY — borrow its litho-crayon line quality, its tri-tone palette, its paper grain and ink-starvation texture, and its flat printmaking technique. Do NOT borrow its subject (the watching figure, the crowd, the dog-head poster), its composition, or any scene element from it. Render a completely new scene in that style: Sisyphus as a stooped commuter shoving a heavy stalled shopping cart up a long broken-down escalator in a derelict transit hall, head bowed, coat heavy on his shoulders. The escalator climbs into shadow above him. Lonely, weary, monumental.
```
- **Sent:** ✓ 2026-05-23
- **Output:** `outputs/2026-05-23/gemini-31-flash-image-preview/01_sisyphus-escalator-v01_b619761f/sisyphus-escalator-v01_0{1,2}.png`
- **Result notes:** **Strong — far better than the Goya-dark branch (~50). Style Lock ~68 (`_01`) / ~80 (`_02`).**
  - **`_02` is the keeper.** It locked the tri-tone palette *exactly* (cream / dusty rose-pink / Prussian blue, no saturation creep) and — notably — reproduced the **print object**, not just the image: cream plate-margins, a pencil edition number bottom-left, and an "EK" monogram bottom-right (Kirchner's E.K.). NB2 recognized the anchor as a *print artifact category* and reached for the whole apparatus.
  - **`_01`** holds palette + mood but drifts toward clean ink-and-wash *illustration*; **`_02`** drifts slightly toward flat woodcut/linocut rather than litho-crayon.
  - **Residual gap (both):** the **micro-grain** — the speckled ink-starvation / crumbling crayon drag Gemini named as the single hardest-to-fake signature — is not nailed. `_01` too clean, `_02` too flat-graphic. The *category* transferred; the *surface texture* is the remaining 20%.
  - Composition fence held (lone figure + cart + escalator; no crowd / dog-head poster leak). Brief fidelity excellent.
  - **Cross-branch finding (refines `nb2-facture-ceiling`):** the predictor isn't "hard vs. easy" — it's **category-anchored vs. facture-anchored**. Styles that map to a recognizable print/illustration category lock well (search-line ~80, litho ~80); a paint-*facture* style NB2 reads as "a painting" gets flattened to clean render (~50).
- **Next iteration:** **v02 = grain/crayon-drag amplifier on the `_02` direction.** Keep the print-object framing that worked; add a texture hammer to close the last 20%: "heavy litho-crayon grain, speckled ink-starvation breaking through every dark area, crumbling dragged greasy crayon edges, coarse visible paper tooth — NOT flat woodcut fills, NOT clean ink." **Surfaced to David (Direction Gate) — `_02` is the candidate; confirm direction before firing v02.**

---

## v02 — Sisyphus on the frozen escalator (deep-recipe block)

- **Date:** 2026-05-23
- **Image input:** Cerberus frame `8f5831c8` (style only) — held constant from v01
- **Model:** `gemini-3.1-flash-image-preview` · **AR:** 16:9 · **num_outputs:** 2
- **System instruction:** the **upgraded** look block (post Gemini deep-read) — bakes in the three named v01 misses: grain-from-heavy-crayon-pressure (not flat fills), hand-drawn/non-ruler-straight perspective, loose-registration print order. **Only changed variable.**
- **Intent:** Isolated test — same scene, same ref, same fence as v01; does the richer recipe close the Gemini 78 toward the named misses (line texture, dark-fill grain, perspective wobble)? Grade with the same Gemini compare call for an apples-to-apples delta.
- **Prompt:** _(identical to v01)_
- **Sent:** ✓ 2026-05-23
- **Output:** `outputs/2026-05-23/gemini-31-flash-image-preview/01_sisyphus-escalator-v02-recipe_13a85585/sisyphus-escalator-v02-recipe_0{1,2}.png`
- **Result notes:** **Negative result — the deep-recipe amplifier did NOT close the facture gap.** Gemini compare-grade of `_02`: **75/100**, vs. v01 `_02`'s **78** — flat, within noise. Gemini's complaints are nearly identical to v01: "lines too smooth/fluid/digital," "hatching too uniform/neat," "flat digital fills," and the diagnostic line — **"the simulated paper texture sits passively behind the artwork rather than actively breaking up the ink."**
  - **Improved (iconography, not facture):** v02 *did* pick up recipe details — the single terracotta-red spot (top-right), the corner plate-date, looser arches. But these are category/print-object cues, not the scored facture. The red spot even rendered as a *perfect geometric circle* vs. the anchor's irregular hand-stamped one.
  - **Did not move (the facture):** dry crumbly broken crayon line, grain-breaks-the-ink darks, ink-starvation. NB2 paints clean marks and overlays a passive paper texture, rather than building marks *out of* the grain. An explicit physical recipe (pressure / tusche / grain) could not invert that.
  - **Conclusion:** consistent with a **facture ceiling** — even on a category-anchored style where palette/layout/print-object lock richly (~75–80), micro-facture is structurally out of reach via prompt. Two escalating attempts (v01 amplifier-light → v02 full recipe) hit the identical wall.
- **Next iteration:** **Stop amplifying the prompt — it's a model ceiling, not a prompt miss.** Three real options, Direction Gate to David: (1) **Accept ~78** for storyboard purposes — it reads convincingly as a litho print; facture isn't load-bearing at thumbnail scale. (2) **Post-process** — generate clean, then composite a *real* litho-grain / ink-starvation texture pass so the grain actively breaks the ink (does in post what NB2 won't do natively). (3) **Try GPT-Image-2** on the same anchor+fence to test whether a different model reaches the facture NB2 can't. → **David chose (3); see x01.**

---

## v03 — Sisyphus escalator, multi-ref crops (show-don't-tell) on NB2

- **Date:** 2026-05-23
- **Model:** `gemini-3.1-flash-image-preview` (NB2) · **AR:** 16:9 · **num_outputs:** 2
- **Image inputs (3):** full Cerberus `8f5831c8` + `outputs/.../refs/cerberus_crop_line.png` (line character) + `cerberus_crop_mass.png` (heavy ink mass + grain). Passed via `--images`.
- **Style block:** v02 deep-recipe block, **byte-identical** (only the fence changed, to treat all 3 images as style/mark exemplars not subjects).
- **Intent:** Test the GPT-on-the-web suggestion *for NB2*: **show-don't-tell.** Post-process proved the facture gap is in the *line* (NB2 draws thin etched hatching, no heavy ink masses for grain to break through). Words ("thick blunt crayon, no fine detail") were already in the v02 block and didn't move it. Does *showing* NB2 crops of the actual mass-based crayon marks redirect the line where describing couldn't? **Single variable = the crops.**
- **Prompt (fence adjusted for multi-image + scene):**
```
You are given three STYLE reference images of the SAME lithograph. The first is the full print; the other two are close-up crops provided ONLY to show the mark-making to imitate — thick, greasy, mass-based litho-crayon strokes and cream paper grain breaking through heavy ink. Borrow line quality, mark-making, grain, texture, and the tri-tone palette from them. Do NOT borrow any subject, figure, animal, or composition from any of them — not the dog/wolf head, not the standing figure. Render a completely new scene in that style: Sisyphus as a stooped commuter shoving a heavy stalled shopping cart up a long broken-down escalator in a derelict transit hall, head bowed, coat heavy on his shoulders. The escalator climbs into shadow above him. Lonely, weary, monumental.
```
- **Sent:** ✓ 2026-05-23
- **Output:** `outputs/2026-05-23/gemini-31-flash-image-preview/01_sisyphus-escalator-v03-crops_408f3f38/sisyphus-escalator-v03-crops_0{1,2}.png`
- **Result notes:** **Show-don't-tell helped modestly — Gemini 78 (`_02`), +3 over v02's 75, tied with v01, beats post (75).** The crops moved the line *heavier/mass-based* (the coat reads as a crayon-dragged dark mass, not thin outline) — the thing the v02 word-recipe couldn't do. But NB2 still hit the two recurring walls: "lines too straight/clean/digitally drafted" (perspective, cart grid) and "uniform repetitive digital hatching" in the dark fills instead of greasy organic crayon; edges too sharp, no ink bleed. So crops *nudged*, didn't *convert*.
  - **Caveat — mild composition convergence:** Gemini noted a "large dark back-facing figure in the left foreground … matches the layout of Image 1" — possible slight leak from the mass crop (the anchor's foreground figure). Scene is otherwise clearly distinct (escalator/cart/transit hall). Watch on future multi-ref runs.
  - **NB2 leverboard (this style):** v01 78 · v02 75 · v02+post 75 · **v03 crops 78** · GPT-Image-2 82. Every NB2 lever lands 75–78 → **NB2 facture ceiling ≈ 78**; GPT-Image-2 ≈ 82. The ~4pt gap is plausibly within freehand-grade noise.
- **Next iteration:** The speed reframe (78 @ 20s vs 82 @ ~100s) makes "NB2 good enough" a legitimate call. Remaining untried NB2 levers (single-variable): **positive-framing block** (drop negation wall), **artist-list trim**. Owe a **calibrated `compare_images` re-grade** before trusting the 78-vs-82 gap. Direction Gate to David.

---

## x01 — Sisyphus escalator on GPT-Image-2 (cross-model)

- **Date:** 2026-05-23
- **Model:** `gpt-image-2` (OpenAI `images.edit` endpoint, via `../scripts/gen_openai.py`) · **size:** 1536×864 (16:9) · **quality:** high · **num_outputs:** 1 (endpoint returns one)
- **Image input:** Cerberus frame `8f5831c8` (style only) — held constant
- **Style block:** the **v02 deep-recipe block, verbatim** (OpenAI has no system slot, so it's prepended to the prompt)
- **Prompt:** _(identical to v01/v02 — fence + Sisyphus scene)_
- **Intent:** **Cross-model probe.** Hold prompt + ref + scene constant; swap NB2 → GPT-Image-2 so the *model* is the only variable. Question: does GPT-Image-2 reach the **litho-crayon facture + expressive linework** that NB2 structurally couldn't (NB2 ceiling = Gemini 75–78, "smooth/neat, passive texture overlay")? Directly tests David's note that *linework & expressiveness need work*.
- **Sent:** ✓ 2026-05-23
- **Output:** `outputs/2026-05-23/gpt-image-2/01_sisyphus-escalator-x01-gpt_d34b35c8/sisyphus-escalator-x01-gpt_01.png`
- **Result notes:** **GPT-Image-2 cleared NB2's facture wall. Gemini grade 82/100 vs NB2's 75 — and the failure mode flipped.**
  - **Facture transferred (the key result):** Gemini — "the simulated paper grain and the toothy crayon texture of the blue ink are highly accurate to the lithographic feel." This is exactly what NB2 *couldn't* do (NB2's texture "sits passively behind the artwork"). **So the facture ceiling is NB2-specific, not universal.**
  - **Palette nearly flawless:** cream base, dusty rose block, Prussian blue, *and the single terracotta-red accent circle* (on the "Ausgang" sign). German signage ("Ausgang", "Gleis 11") fits the Die Brücke lineage.
  - **New residual (opposite of NB2):** GPT-Image-2 is **too tight / detailed / illustrative** — fine-line hatching, legible signage, individual cart wires & escalator steps — "mimics a detailed charcoal drawing rather than a raw, spontaneous print." NB2 was *under*-marked (too smooth); GPT is *over*-rendered (not crude/gestural enough).
  - **Gemini's single fix:** "Simplify the linework — remove fine details, replace with thick, blunt, highly gestural strokes." **This is a promptable miss** (push crudeness/simplification), unlike NB2's structural wall. Addresses David's *linework & expressiveness* note directly.
- **Next iteration:** **x02 = crude-gesture push on GPT-Image-2.** Keep the win (palette + facture); add a simplification hammer to the block: "CRUDE, BLUNT, PRIMITIVE hand-drawn strokes; NO fine detail, NO legible text, NO fine hatching, NO precise mechanical lines — reduce everything to a few thick gestural crayon marks; raw and spontaneous, not a finished illustration." Grade vs anchor again. **GPT-Image-2 is now the lead model for this litho style.**

---

> **Human ground-truth (David, 2026-05-23):** v03 crops "definitely better" — confirms the show-don't-tell win by eye (stronger than Gemini's +3). **Crops = keeper baseline.** v05/v06 below build on the v03 crop config, changing one variable each. v04 is the text-only isolation.

## v04 — Sisyphus escalator, TEXT-ONLY (no input images) on NB2

- **Date:** 2026-05-23 · **Model:** NB2 · **AR:** 16:9 · **num_outputs:** 2 · **Images:** NONE
- **Style block:** v02/v03 deep-recipe block (with artists), verbatim. **Fence dropped** (no ref to borrow from).
- **Intent:** Isolation test (David's ask). How much is the image ref contributing vs. the text block alone? If text-only ≈ v03, the block carries the style and refs are optional; if much worse, the image is load-bearing.
- **Prompt:** `A lithograph scene in the established style (per system instruction): Sisyphus as a stooped commuter shoving a heavy stalled shopping cart up a long broken-down escalator in a derelict transit hall, head bowed, coat heavy on his shoulders. The escalator climbs into shadow above him. Lonely, weary, monumental.`
- **Sent:** ✓ · **Output:** `01_sisyphus-escalator-v04-textonly_950365ce/…_0{1,2}.png` · **Result:** **55 — falls apart.** Without refs NB2 drifts in execution (`_01` flat woodcut, `_02` fine pen-and-ink illustration); Gemini "resembling a modern digital comic book rather than a raw mid-century print." **The image refs (esp. crops) are load-bearing for this style** — text block alone is not enough.

## v05 — positive-framed block + crops on NB2

- **Date:** 2026-05-23 · **Model:** NB2 · **AR:** 16:9 · **num_outputs:** 2 · **Images:** full + 2 crops (= v03)
- **Variable:** style block rewritten **positive-framed** (negation wall removed, strong verbs), artists kept. Crops + scene = v03.
- **Intent:** Test GPT-web's "positive framing over negation" suggestion as a single variable on the crop baseline.
- **Sent:** ✓ · **Output:** `01_sisyphus-escalator-v05-positive_b4a3d0ba/…_0{1,2}.png` · **Result:** **75 (`_01`), −3 vs v03.** Print-object cues landed (title "LE CHAISE DE SISYPHE / STATION ABANDONNÉE"), heavy crayon masses present, but Gemini still flags thin/clean hatching. **Positive framing didn't help — slightly hurt.** The negation wall wasn't the problem; keep it.

## v06 — artist-list trimmed + crops on NB2

- **Date:** 2026-05-23 · **Model:** NB2 · **AR:** 16:9 · **num_outputs:** 2 · **Images:** full + 2 crops (= v03)
- **Variable:** v03 block with the artist names (Munch/Kirchner/Nolde/Nabis/Lautrec) **removed**; everything else identical.
- **Intent:** Test GPT-web's "trim artist list" suggestion (consistent with our calibration memory that illustrator names are unstable). Single variable.
- **Sent:** ✓ · **Output:** `01_sisyphus-escalator-v06-notrist_d6f4ad20/…_0{1,2}.png` · **Result:** **82 (`_01`) — NB2's best, ties GPT-Image-2 x01, at 5× the speed.** Gemini: "the dry-crayon texture on the man's coat closely mirrors the grainy lithographic texture" of the anchor. **Dropping the artist names was the active ingredient** (+4 vs v03's 78); the names were widening the basin (confirms `feedback_style-classification-via-gemini` + GPT-web's hunch). Residual still the fine hatching, but clearly the strongest NB2 result.
- **WINNING NB2 RECIPE:** deep-recipe block *with* negations + **artists removed** + full frame + 2 crops = **82**. (positive framing off; text-only off.)

## x02 — GPT-Image-2 + crops (cross-model, show-don't-tell)

- **Date:** 2026-05-23 · **Model:** `gpt-image-2` (`images.edit`) · **size:** 1536×864 · **Images:** full + 2 crops (= v03) · block = v02 deep-recipe (with artists)
- **Result:** **85/100 — highest of the whole probe.** Crops lifted GPT too (x01 82 → x02 85). Gemini: "overall grainy, speckled paper texture and the lithographic print feel are highly accurate." Residual identical to NB2 v06: lines still a touch thin/precise, perspective too structured vs. the anchor's flat graphic abstraction.

---

## Litho branch — SUMMARY (2026-05-23)

**Crops (show-don't-tell) were the universal unlock — lifted both models.** Final: **NB2 v06 (crops + artists trimmed) = 82 @ 20s** (production recipe); **GPT-Image-2 x02 (crops) = 85 @ ~100s** (hero-frame ceiling). 3-pt gap, within freehand-grade noise, for 5× speed → **NB2 is viable for this facture style**, revising the mid-session "NB2 facture ceiling ~78, structural" call. Negation wall: keep (positive framing −3). Text-only: not viable (55; refs load-bearing). Post-process: abandoned (can't fix line character). **Still owed:** calibrated `compare_images` re-grade of the freehand numbers.
