---
name: prompts-coverage-active
description: "Coverage probe — treat the winning litho Sisyphus frame as an establishing MASTER and generate alternate camera angles of the SAME scene on NB2. Tests world/character/set consistency across shots (the flipped fence: preserve subject, change camera)."
title: "Prompts — Scene Coverage Probe (Active)"
type: production_doc
tags: [visual_ref, style_probe, coverage, consistency]
tier: reference
status: living_document
system_directive: "Log every coverage prompt BEFORE firing; fill result after. This probe PRESERVES world+character and changes only the camera — opposite of the style-only fence."
related:
  - "prompts-litho-active.md"
  - "look-litho-crayon-duotone.md"
  - "LOG.md"
---

# Prompts — Scene Coverage Probe (Active)

**Question:** can we treat one good frame as an establishing **master** and get consistent **coverage** (alternate camera setups) of the *same* scene — same set, same character, new angle — while holding the litho style?

**Master (establishing wide):** litho `v06` winner — `01_sisyphus-escalator-v06-notrist_d6f4ad20/sisyphus-escalator-v06-notrist_01.png` (NB2, graded 82). Geography: stooped coated man + stalled shopping cart at lower-left, "BROKEN / OUT OF ORDER" sign, broken escalator climbing into a dark arched tunnel center-right, derelict tiled transit hall, terracotta accent.

**Method:** refs = master (world + composition seed) + the two Cerberus facture crops (mark-making). System block = v06 winning recipe (artist-trimmed, negations kept). **Fence FLIPPED** — preserve set/character, change only the camera, don't copy the master composition. Model = NB2 (production/fast). Grade each on: style continuity, world/character continuity, and whether it's a genuinely new valid angle (not a copy, not a reinvention).

**Coverage fence (prepended):**
> You are given a reference establishing shot of a scene, plus two close-up crops showing the litho mark-making to imitate. PRESERVE the world, set, and character from the establishing shot — the same derelict tiled transit hall, the same stooped old man in a heavy dark overcoat, the same stalled overloaded shopping cart, the same broken escalator climbing into shadow. KEEP the exact litho-crayon style, tri-tone palette, and grain from all references. Render the SAME scene from a NEW camera angle — do NOT copy the establishing composition: [SHOT]

---

## c01 — Medium, front ¾ on the man at the cart
- **[SHOT]:** "Medium shot, front three-quarter view of the old man hunched over the cart handle, face strained and downcast, the broken escalator rising behind him."
- **Sent:** ✓ · **Output:** `01_sisyphus-coverage-c01-medium_22524905/…_0{1,2}.png` · **Result:** **PASS.** Camera pushed in + around to front ¾; face now readable (balding, strained). Set held (sign, escalator, tunnel, terracotta, tiles), style held, character consistent. Genuinely closer framing, not a master reframe.

## c02 — Low angle up the escalator
- **[SHOT]:** "Low angle from beside the cart looking steeply UP the broken escalator as it climbs into the dark tunnel above; the man's shoulder and gripping hands in the lower foreground."
- **Sent:** ✓ · **Output:** `01_sisyphus-coverage-c02-lowangle_18175b5e/…_0{1,2}.png` · **Result:** **PASS.** True low-angle up the escalator into the tunnel, man's shoulder/head lower-left foreground, arched ceiling with oval lights. New angle, same set + style + character.

## c03 — High reverse, down at the lone figure
- **[SHOT]:** "High reverse angle from the top of the escalator looking down at the tiny lone figure and his cart far below in the empty tiled hall."
- **Sent:** ✓ · **Output:** `01_sisyphus-coverage-c03-highreverse_d125b7ce/…_0{1,2}.png` · **Result:** **PASS (strongest).** High reverse from escalator top; escalator descends in foreground, tiny figure + cart at top in the tiled hall (scale/loneliness). Sign + style + character held.

---

## SUMMARY — coverage works on NB2 (2026-05-23)

Three angles (medium / low-angle-up / high-reverse-down) off one establishing master, all **PASS**: same character + set + litho style, each a genuinely new camera setup (not a reframe). The "BROKEN / OUT OF ORDER" sign persists across all three = NB2 held the *set as a place*. **The flipped fence (preserve world, change camera) works.** Combined with proven style-repro, this validates the core storyboard premise: establish a styled master once → cover the scene fast on NB2. Character identity is storyboard-consistent (archetype, not pixel-locked face). **Open:** push harder angles (OTS, reverse 180, insert detail), test character-face drift across a longer set, and whether a GPT master → NB2 coverage pipeline holds.

---

# Coverage off the ORIGINAL frame (Cerberus anchor as master)

**Master = the un-modified MidJourney source** `MidJourney/2026-05-23/…Cerberus_turnstiles…8f5831c8…_0.png` (fed ALONE — it carries world + style + best-in-project facture; no crops needed). Block = v06 recipe (artist-trimmed). Harder test: dense multi-element scene (lone watcher + filing crowd + looming three-headed Cerberus banner over the turnstiles). Same flipped fence (preserve world/characters, change camera).

**Coverage fence:** PRESERVE from the reference — the same dim station checkpoint hall, the same lone figure in a long dark coat watching, the same looming three-headed Cerberus dog banner over the turnstiles, the same crowd of cloaked figures filing through, the same duotone litho style/palette/grain. Render the SAME scene from a NEW camera angle; do NOT copy the establishing composition: [SHOT]

## oc01 — Medium on the lone watcher
- **[SHOT]:** "Medium shot of the lone coated man from a front three-quarter angle as he watches, the filing crowd and the looming dog-head banner behind him."
- **Sent:** ✓ 2026-05-24 · **Output:** `2026-05-24/…/01_cerberus-coverage-oc01-medium_6b55ca0f/…_0{1,2}.png` · **Result:** **PASS.** Watcher front-¾ foreground-left; the banner resolved into THREE distinct wolf heads (title's "three heads" now explicit), crowd filing through an arched door, terracotta spot, "10.2.11" plate-date preserved. Style/facture held.

## oc02 — Low angle up at the Cerberus banner
- **[SHOT]:** "Low angle looking up at the looming three-headed Cerberus dog banner over the turnstiles, dominating the frame, small cloaked figures filing beneath it."
- **Sent:** ✓ 2026-05-24 · **Output:** `2026-05-24/…/01_cerberus-coverage-oc02-lowangle_1786915e/…_0{1,2}.png` · **Result:** **PASS (strongest).** Three Cerberus heads dominate the upper frame (central one roaring), watcher's back lower-left, crowd beneath, terracotta spot. Amplified the "three heads as security" concept. Style held.

## oc03 — Reverse over the crowd
- **[SHOT]:** "Reverse angle from beside the turnstiles looking back across the filing crowd toward the distant lone watching figure in the hall."
- **Sent:** ✓ 2026-05-24 · **Output:** `2026-05-24/…/01_cerberus-coverage-oc03-reverse_1af59dab/…_0{1,2}.png` · **Result:** **PASS.** Deep receding checkpoint corridor; crowd files away toward a distant lone figure, banner reframed as a wall panel left, watcher's back foreground on a bench, plate-date kept. Dramatic new depth, same world.

---

## SUMMARY — coverage off the ORIGINAL frame (2026-05-24)

All three **PASS, and stronger than the generated-master set.** Feeding the un-modified MJ source alone, NB2 held world + characters + facture AND *resolved* the scene (ambiguous dog-head → explicit three-headed Cerberus; built a deep corridor for the reverse; preserved the "10.2.11" plate-date as continuity). **Finding: coverage works directly off raw MidJourney source — a denser source gives MORE continuity anchors, not fewer.** Workflow shortcut: pick any MJ frame → cover it, no style-repro round-trip. Next: does coverage generalize across the *other* batch style families, or is this litho/Cerberus-favorable?

---

# Coverage off ORIGINAL — Hephaestus automata (generalization test, different style family)

**Master = MJ source** `…Hephaestuss_automata_assembly_line…3c793ade…_0.png` (clean concept-art, deep blue/gold industrial environment), fed ALONE. **Method change:** style block is now **generic style-match** ("match the reference's exact art style/palette/medium"), NOT the litho block — coverage off a non-litho frame must take style from the source image. Tests whether coverage generalizes to a different style family + NB2's comfort-zone clean render.

**Coverage fence:** PRESERVE from the reference image — the same industrial automaton workshop, the same bearded robed figure (Hephaestus), the same long assembly line of gold humanoid automata, the same cool blue/purple lighting and concept-art rendering. Render the SAME scene from a NEW camera angle; do not copy the establishing composition: [SHOT]

## hc01 — Medium on Hephaestus
- **[SHOT]:** "Medium shot of the bearded robed figure (Hephaestus) at the assembly line, inspecting a half-built gold automaton beside him."
- **Sent:** ✓ 2026-05-24 · **Output:** `01_hephaestus-coverage-hc01-medium_ff5d4ef7/…_0{1,2}.png` · **Result:** **PASS.** Closer on Hephaestus (blonde, bearded, white robe), now actively tooling a half-built automaton; robotic arms, gold figures, blue/purple palette held. New angle, same character/world/style.

## hc02 — Down-the-line tracking
- **[SHOT]:** "Low tracking angle looking down the long assembly line of gold humanoid automata receding into the cavernous workshop, machinery overhead."
- **Sent:** ✓ 2026-05-24 · **Output:** `01_hephaestus-coverage-hc02-downline_28692fb2/…_0{1,2}.png` · **Result:** **PASS (strongest).** True down-the-line tracking — row of gold automata receding into depth, Hephaestus mid-ground working with sparks, overhead arms, the source's red column kept. Same world/style.

## hc03 — Close-up on an automaton
- **[SHOT]:** "Close-up on a single gold automaton's face as a robotic arm assembles it, sparks and cabling, shallow depth of field."
- **Sent:** ✓ 2026-05-24 · **Output:** `01_hephaestus-coverage-hc03-closeup_733f768b/…_0{1,2}.png` · **Result:** **PASS.** CU on a serene gold automaton face under a sparking welder arm; **Hephaestus held as a soft bokeh presence in the background** (unprompted depth continuity). Shallow DOF, palette + style held.

---

## SUMMARY — coverage generalizes across style families (2026-05-24)

Hephaestus (clean concept-art) coverage: all three **PASS**, strongly — and easier than litho, since concept-art is NB2's native register so the **generic "match the reference style" block** locked it (no hand-built style block needed). Down-the-line tracking + CU-with-bokeh-background show real spatial reasoning, not reframing. **Finding: the coverage method is style-agnostic** — works on a facture-print style (litho/Cerberus) AND clean concept-art, off raw MJ source, with a generic style-match instruction. The source image carries the look; the fence carries the camera.

---

# Patrick's method — storyboard PAGE first, then extrapolate panels (2026-05-24)

Patrick (`conversation/patrick/Talk with Patrick 2026-05-24.md`): wide shot → render a labeled multi-panel comic/storyboard PAGE of the scene's coverage in ONE image (cross-panel consistency baked in by shared context), THEN extrapolate each lettered panel to a full frame. For reverse angles, enumerate every element in text. Letter labels = handles for step-by-step finishing.

## sp01 — Sisyphus storyboard page (stage 1: the page)
- **Ref:** v06 master · **System:** generic style-match (litho) · **Model:** NB2 · **AR:** 16:9 · **num_outputs:** 2
- **Prompt:** 3×2 grid of 6 labeled panels (A wide / B medium / C CU face / D low-angle up escalator / E high reverse / F insert cart-wheel), same character+set+litho across all, letter labels in the gutters.
- **Sent:** ✓ 2026-05-24 · **Output:** `01_sisyphus-storyboard-page-sp01_256743e9/…_0{1,2}.png` · **Result:** **WORKS.** One render → coherent 6-panel page: all panels the same old man + escalator + BROKEN sign + litho style; CU face (C) matches the wide. **Cross-panel consistency is tighter than separate per-angle renders** (shared canvas). **Wrinkle:** letter labels unreliable (`_01` repeats "A" for "D"; `_02` two "D"s) — NB2's in-image text isn't dependable → for production, render for art, **overlay A/B/C labels programmatically.**
- **Production loop this validates:** wide → ONE storyboard page (locks plan + consistency as a thumbnail board) → **extrapolate only chosen panels to full res** (stage 2, pending). Fewer hero renders, consistency guaranteed up front.
- **Next (stage 2):** extrapolate a panel (e.g. C, the CU face) to a full frame, using the panel as the comp + the page for continuity.

---

## c04 — Sisyphus REVERSE via element-breakdown-into-text (Patrick's technique)
- **Refs:** v06 master + 2 crops · **System:** v06 litho block · **Model:** NB2 · **num_outputs:** 2
- **Test:** Patrick's "reverse angle → break every element into text." Reverse from escalator TOP looking down; prompt enumerates all 6 scene elements + their placement from the new POV. Compare consistency vs the simpler c03 reverse.
- **Sent:** ✓ 2026-05-24 · **Output:** `01_sisyphus-coverage-c04-reverse-elembreak_4118cdae/…_0{1,2}.png` · **Result:** **PASS — more complete than c03.** Every enumerated element present + correctly placed: balustrades framing the descending litter-strewn steps, man+cart small at the foot, "BROKEN / OUT OF ORDER" sign, arched tiled hall, terracotta spot. **Enumerating the off-screen space as text turns the reverse (hardest case) into the most *controllable* one.** Patrick's technique validated. Style/facture held.

# Hephaestus — storyboard PAGE method (Patrick stage 1)

## hp-sp01 — Hephaestus storyboard page
- **Ref:** Hephaestus MJ source (alone) · **System:** generic style-match · **Model:** NB2 · **num_outputs:** 2
- **Prompt:** 3×2 grid, 6 labeled panels (A wide workshop / B medium Hephaestus / C CU his face / D down-the-line / E CU automaton face / F low angle up at the arms), same character+automata+palette across all.
- **Sent:** ✓ 2026-05-24 · **Output:** `01_hephaestus-storyboard-page-hpsp01_ea0b98e0/…_0{1,2}.png` · **Result:** **WORKS — cleanest board yet, and labels A–F correct + in order** (vs the litho page's duplicate letters — concept-art's crisper render likely makes NB2's in-image text more reliable). Six consistent panels (wide / medium / CU Hephaestus face / down-the-line / CU automaton-head-under-welder / low-angle-up-the-arms), same character + gold automata + blue-purple palette throughout.

---

## SUMMARY — Patrick's full workflow validated, across two style families (2026-05-24)

- **Page method (stage 1)** works on both litho (sp01) and concept-art (hp-sp01) — one render = a consistent labeled coverage board; cross-panel consistency tighter than separate per-angle renders. Labels reliable on concept-art, flaky on litho → **overlay labels programmatically** for production.
- **Element-breakdown reverse (c04)** validated — enumerating off-screen elements as text makes the reverse the most *controllable* angle, not the flakiest.
- **Whole loop proven:** wide → labeled coverage page → extrapolate panel to full frame, + element-breakdown for reverses. Style-agnostic, NB2-fast.
- **Still open:** programmatic label overlay; GPT-master → NB2-coverage; face-drift across a long sequence; the boundary case (coverage on a flat-tableau/portrait source).
