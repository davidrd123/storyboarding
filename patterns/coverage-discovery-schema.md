---
name: coverage-discovery-schema
description: "A runnable schema that derives a shot/coverage manifest from a scene brief + asset/character bible — for when you DON'T already have a shot list. Synthesis of Patrick's coverage protocol, John's per-shot/layout rigor, and the style-control-probe's empirical generation findings."
type: pattern
tags: [coverage, storyboard, schema, production_workflow]
status: draft
related:
  - "../conversation/patrick/scene-coverage-protocol-v2.md"
  - "../conversation/john/schema.txt"
  - "../style-control-probe/prompts-coverage-active.md"
  - "../style-control-probe/LOG.md"
---

# Coverage-Discovery Schema

**Purpose.** Turn a *scene brief + asset/character bible* into a derived, contrast-checked, subtext-aware **coverage manifest** — including the shots you wouldn't think to ask for (the insert of his hands on the statue). Use it when you **don't yet have a shot list**: it surfaces the coverage the scene *implies*.

**What it is vs. its sources.** Patrick's protocol is the *reasoning frame* (bible + brief + contrast gate). John's schema is what *one filled manifest* looks like (layout-locked, captioned output spec). This is the **missing middle** — the derivation that turns the first into the second automatically.

**The design goal: it writes itself.** Point an LLM at the INPUTS; it executes §Derivation and emits §Manifest. No hand-authored shot list required. The richer the brief and bible, the more complete the derivation.

---

## Inputs

### 1. Asset & Character Bible  *(Patrick Phase 0 / John character bible)*
- **Characters** — locked design per principal: silhouette, wardrobe, distinguishing marks. (Identity anchor for every shot.)
- **Key assets** — named props / vehicles / hero objects, with enough description to reconstruct them. *(Assets are the seed list for inserts.)*
- **Environment** — the place, its landmarks, light grammar, time of day.
- **Style direction** — the look lock (medium, palette, cultural anchors).

### 2. Scene Brief  *(Patrick Phase 1)*
- **Beat / action** — one sentence. *Mind the verb* — it's what nominates the inserts ("lifts," "hands over," "watches").
- **Purpose** — what story beat this carries.
- **Emotional register** — what the audience should feel.
- **Subtext** — what the camera must say that the action doesn't.
- **Obligations** — products/logos that must be legible, and at what scale.

---

## Derivation Engine  *(the part that writes itself)*

Walk the brief's **nouns and verbs** against the bible. Each rule emits candidate shots:

1. **Establishing — always.** A wide that shows the environment + the key asset *en masse*. Locks geography, scale, style.
2. **Per CHARACTER present →** a **face CU** (their regard); **+ a hands/action insert** *if the verb has them touch/handle/carry anything*; **+ a POV** *if they're looking at something that matters*.
3. **Per ASSET acted-on or named →** an **insert/detail** of it; **+ a CU of its "face"/key feature** if it can carry a gaze, a brand, or meaning.
4. **Per EXCHANGE / relationship (A↔B, or character↔asset) →** a **shot/reverse pair** + an **OTS** (establishes eyeline + spatial relation).
5. **Per SUBTEXT line →** name the **single shot that carries it** — usually a non-obvious insert or a back/wide. Mark it required.
6. **Axis & eyeline — the 180° rule** *(John's schema does this; the derivation must too).* Once the shots exist, fix the **action axis** between the two key elements and assign **screen-left/right + facing** to each, held across every shot. For an A↔B exchange: A screen-left facing right, B screen-right facing left, camera never crosses the line — so the two CUs become a true **eyeline match** (A looks right, B looks left → they read as looking at each other) and the coverage actually *cuts*. Without this, gazes flip across cuts (the B→C break). Carry the assigned direction in each manifest row.
7. **Contrast gate** *(Patrick)* — confirm the set spans **wide↔tight, face↔back, static↔kinetic**. If an axis is missing, add a shot.
8. **Tier** — mark **Tier-1** (an editor must have it to cut the scene) vs **Tier-2** (creative/cutaway). Never drop Tier-1 without a replacement.

> The non-obvious shots come from rules **2 (hands), 3 (asset insert), 5 (subtext)** — they fall out of the brief's verb + the bible's assets, not from a pre-built list. That's the discovery.

---

## Output Manifest  *(John-style per-shot rows; ordered wide→tight, beat by beat)*

| # | Beat | Shot type | World-specific description | Why (story/subtext) | Chain input | Derivable? | Tier |
|---|------|-----------|----------------------------|---------------------|-------------|------------|------|

- **Derivable?** Yes (geometry present) / Partial (infers off-frame space → may hallucinate) / No (needs a new source frame).
- **Chain input** — which approved earlier output anchors this one (the approved wide *is* the world).

---

## Phase 4 — Per-Shot Prompt (formalized)

> **GPT-Image-2 is a reasoning-image hybrid — it *uses* story context and instructions, not just description.** Lead with the *why*; it makes framing/light/expression choices that serve the subtext, and it honors explicit invariants/directives (the 180, eyelines, what's fixed vs. changes) the way a reasoning model honors constraints. Each manifest row expands into four blocks:

**A — STORY CONTEXT** *(lead with it; the model reasons over it; inherited from the Scene Brief / story doc)*
- **Logline** — the spine, one line.
- **Beat purpose + emotional register.**
- **Subtext** — what the shot must say beneath the action (+ what is only *foreshadowed* here, not yet revealed).

**B — REFERENCES: the house grammar** *(NOT ad-hoc prose — assemble these blocks from per-asset metadata; grounded in `deep-research/2026-05-19/reply01.md` §5–6, which says this must be "a formal prompt-assembly layer, not ad hoc prompt text")*

Per reference image, a role + **Borrow / Preserve** (what to take) + **Do NOT borrow** (what to ignore) block:
```
Image 1 — STYLE reference (the clean source):
  Borrow: line quality, palette, brushwork, rendering, finish.
  Do NOT borrow: subject, composition, scene elements.
Image 2 — COMPOSITION SKELETON (the panel crop / storyboard):
  Borrow: layout, framing, staging, subject scale, depth stack, eyelines.
  Do NOT borrow: grain, noise, surface texture, rendering, palette, line style  ← fixes the noise-as-feature bleed.
Image 3 — STORYBOARD PAGE (optional, context):
  Borrow: world + cross-shot consistency. Do NOT borrow: the grid, panels, labels.
```
Plus the **180 axis + eyeline** ("X screen-left facing right; Y screen-right facing left; they must read as looking at each other") and an explicit **reasoning instruction** for the hybrid ("reconstruct this frame from the spec; reinterpret the composition skeleton in the style reference; render clean").

**C — SHOT SPEC** *(the frame)*
- Shot type / framing; **the MOMENT** (the instant); staging + screen direction; materiality; light; composition; negative constraints (no grid/labels/text).

**D — LOG METADATA** *(Patrick's discipline — externalize + log every run)*
- `vNN`/`eNN` · date · model · size/quality · refs · **output path** · result notes · score · next iteration.

### Worked example — panel E "the gaze" (the intuitive prompt, rationale now explicit)

- **A. Story context:** *logline* (the smith forging tomorrows for Time); *subtext* — "the instant a made thing becomes a someone; **does it look back?**"; *foreshadow only* (early beat — the first hairline crack, not the reveal).
- **B. Invariants/direction:** style = concept-art (ref); identity = one gold automaton; **180 = it faces/looks screen-LEFT** toward the unseen maker; *invariant* = the army behind stays identical, blurred; *instruction* = "reason about what an awakening looks like in a blank golden face — let the **eye** carry it."
- **C. Shot spec:** tight CU, ¾ profile; the MOMENT = eyes opening, inner light waking; seams + solder bead; cool key + warm welder rim; face right-of-center, gaze leading left into negative space; bokeh army; no grid/labels.
- **What the reasoning model *did* with it:** lit the eye and made the one face singular against the blurred multitude — choices it made *because the subtext told it the meaning*, not because I specified pixels.

---

## Generation Doctrine  *(empirical — from `style-control-probe/LOG.md`)*

How to actually *render* the derived manifest:

- **One-shot the page first** (Patrick V2; validated sp01/hp-sp01). Render the panels together in one context → cross-panel consistency is baked in. **3–6 panels per run** (we held 6 on single-subject scenes; drop toward 3–4 as character/identity count rises).
- **Layout-lock is optional** (John): to fix panel architecture, feed a flat blocking template and instruct *"copy this layout exactly."* *(Open question — our `phase-0/FINDINGS.md` was skeptical of compositional-skeleton-via-reference; test whether the model obeys a literal template.)*
- **Labels are planning-layer only.** Don't trust the model to render them (NB2 duplicated letters). **Overlay A/B/C programmatically;** strip from any final art (*"no text, no labels, no captions — clean image only"* — John + Patrick V2 agree).
- **Facture styles: show, don't tell.** Pass crop refs of the mark-making; describing it doesn't transfer. **Hero frames on GPT-Image-2** (reaches facture, ~100s); **coverage volume on NB2** (~82, ~20s).
- **Reverses / hard angles: element-breakdown.** Enumerate the off-screen elements as text — turns the reverse into the most controllable shot (validated c04).
- **References:** keep ≤3; Image 1 = style/world authority; **never text-only** for a facture style (collapses to clean digital — our v04 = 55).
- **Enforce the 180° axis in the prompt** (derivation rule 6): when one-shotting the page, *state the axis and each panel's screen-direction explicitly* ("Hephaestus screen-left facing right; the automaton screen-right facing left; camera never crosses the line"). The model holds direction across panels when it's all one render — so the eyeline match lands and the board cuts.
- **Subtext-rich prompts favor GPT-Image-2.** For a hero/expressive board, load the full subtext into the prompt and render on GPT-Image-2 — its higher fidelity + tendency to over-render detail is an asset for dense story prompts (vs. NB2 for fast coverage volume).
- **Two render scales (the board is a plan, the panel is the deliverable).** Render the *coverage board* cheap/fast to lock plan + consistency. Then render **each chosen panel as its own full hero frame** with a Phase-4 per-shot prompt — not a one-line caption. On GPT-Image-2 use **`size=2560x1440` (2K; 4K experimental), `quality=high`** for heroes. Demonstrated: a starved 512px grid cell becomes a true hero frame as its own render.
- **Panel expansion MUST carry a shared style anchor (learned the hard way).** Expanding each panel from its *crop alone* lets every panel's style drift independently — the set comes out *inconsistent* (observed: NB2 crop-only expansions). Always pass **two refs: the panel crop (composition) + the original source frame as the shared style anchor**, and render on **GPT-Image-2** (consistency + reasoning). Declare roles in the prompt ("image 1 = composition to finish; image 2 = style anchor, match exactly"). Same anchor across all panels ⇒ consistent kit by construction.
- **The noise-as-feature trap (David, 2026-05-24).** GPT-Image-2 outputs carry a fine painterly noise/grain; when one is fed back as a reference to expand/upscale, the *reasoning* model reads that noise as **intentional texture to preserve and amplify** — so a board→crop→expand chain *compounds* artifacts. Fixes: (a) **instruct explicitly** — "treat any grain, noise, or compression artifacts in the references as artifacts; do NOT preserve or amplify them — render clean, intentional brushwork"; (b) prefer the **clean original source** as the style anchor over noisy GPT-derived crops; (c) optionally denoise the crop before feeding. The hybrid honors the instruction *because* it reasons — so tell it what's signal vs. artifact.
- **Storyboard → video: you CAN sequence in one generation (Patrick-proven).** Feed the finished panels as **named ingredients** (omni_reference, `[Image1..N]`) and prompt them as **ordered BEATS the camera transitions through** — "begin on [Image1] … transition to [Image2] … then [Image3] …". This gives *both* the order you specify *and* Seedance's own pacing/timing (often better than uniform manual cuts). (My earlier "it just freelances the order" was a prompting limitation, not a model limit — corrected.) Notes: a single grainy storyboard *page* fed as one image freelances more; **named individual-panel ingredients sequence better**; keep to the 3–6 ingredient sweet spot. **Full edit control alternative:** animate each panel as its own img2vid clip (~5s floor, motion-only delta prompt) and cut in an editor — more mechanical timing, total control. Two external 9-panel coverage boards (`conversation/patrick/HG*.jpeg`) confirm the board→video approach yields good results.

---

## Worked example — Hephaestus forge-line  *(the engine executed)*

**Brief:** *"In the forge-line, Hephaestus lifts a finished gold automaton and inspects it."* **Subtext:** a maker and his creation; one of many identical. **Assets:** the automata (many), welder arms, the line/workshop. **Character:** Hephaestus.

| # | Shot | Derived by rule | Why |
|---|------|-----------------|-----|
| 1 | Wide — line receding | 1 establishing | scale + the asset *en masse* |
| 2 | Medium — Hephaestus + automaton | 2 character | the working relationship |
| 3 | CU — Hephaestus's face | 2 face | the maker's regard (subtext) |
| 4 | **Insert — his hands on the gold surface** | **2 hands (verb "lifts")** | tactile authorship — *the shot not in the brief* |
| 5 | CU — the automaton's face | 3 asset-face | the created gaze; eyeline-pairs with #3 |
| 6 | OTS / reverse behind the automaton | 4 exchange | the line of identical others → "he made an army" (subtext) |
| 7 | Insert — welder spark on metal | 3 asset + kinetic | the act of making (punctuation) |
| 8 | Low angle up the automata | 6 contrast (looming) | what has he built? |

Contrast gate: wide(#1)/tight(#4,5) ✓, face(#3)/back(#6) ✓, static/kinetic(#7) ✓. Subtext selects: #4, #6 → Tier-1.

---

## Phase 0 — ASSET-LOCK before kit generation *(hard-won, 2026-05-24 — the step we skipped)*

**Before rendering the per-panel kit, lock canonical reference images and feed them to EVERY panel:**
- a **character identity** ref per principal (the correct face/age/wardrobe — decide and fix it),
- a **canonical asset design** ref per key asset (e.g. the one true automaton head/body).

**Why:** each panel is a *separate* generation with no cross-call memory. Without a locked design ref, every panel *reinvents* the asset and drifts the character — even on strong models. Evidence: the NB-Pro kit (prompt+board only, no asset-lock) came back **6/9 QC-flagged** — automaton head drifted across panels (cylinder → top-hat → C-3PO dome → blank mannequin), Hephaestus duplicated/identity-drifted. The GPT kit (same approach) fared better (**1/9**) — GPT holds refs more faithfully — but *neither is safe without the lock*.

**QC discipline:** **pretty-per-panel ≠ consistent-across-panels.** Run a Gemini QC over the WHOLE set (`scripts/style_probe.py`, all N panels, the 5-point continuity question) — *and keep a human eye*: the auto-QC is a net, not complete (it caught "fused fingers" but missed a 3-arm glitch a human saw).

**Camera/cutting is a SEPARATE layer (open):** the manifest gives the *shots* (what); it does NOT specify *camera moves + cut points + durations* (how) — leave that out and the video model improvises. Add a per-shot Director-Mode camera command + between-shot cut/transition + duration (Patrick's `scene-coverage-protocol-v2.md` "Shot Type Vocabulary" table is the start).
