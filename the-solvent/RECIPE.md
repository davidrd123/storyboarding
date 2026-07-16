---
name: the-solvent-recipe
description: "The page-generation recipe for THE SOLVENT — ported and generalized from John's proven Topanga/Manson 6-page comic system (conversation/john/). Three layers: the reference stack (controllability), the prompt architecture (reusable page-prompt skeleton), and the variant-orchestration discipline. Plus the solvent's two-register specifics on GPT-Image-2."
type: prompting-guide
title: "The Solvent — Page-Generation Recipe"
tags: []
tier: production-tools
status: draft
system_directive: "Use this to build any comic PAGE for the-solvent. It is the controllability+variation system: assemble the reference stack, fill the prompt architecture, and spawn variants under the orchestration discipline. Engine = GPT-Image-2 (Codex-side, riff-mcp NOT used here). Source of truth for the method = John's files in ../conversation/john/ (schema.txt, message (6).txt, AGENTS.md); this generalizes them + adds the two-register application."
related:
  - "CONCEPT.md"
  - "LEADS.md"
  - "prompts/opening-tests.md"
  - "../conversation/john/schema.txt"
  - "../conversation/john/message (6).txt"
  - "../conversation/john/AGENTS.md"
---

# The Solvent — Page-Generation Recipe

> **Provenance.** This is **John's recipe**, proven on his Topanga/Manson 6-page short, ported here and generalized. The three source artifacts: `../conversation/john/schema.txt` (3-panel page), `message (6).txt` (4-panel page, richer), `AGENTS.md` (variant orchestration). Where our own findings converge with his, it's noted. **Engine: GPT-Image-2**, run Codex-side (free on the max plan); riff-mcp is *not* used for this project.

Three layers, in the order you apply them: **(1) the reference stack** (what controls the image), **(2) the prompt architecture** (how the page-prompt is written), **(3) the orchestration discipline** (how variants are spawned). Then **(4)** the solvent's two-register specifics.

---

## 1. The reference stack — *the controllability mechanism*

Controllability comes from **showing**, not just telling. Each page-gen is fed a stack of reference images, each with a **declared, narrow authority** (what to take from it — and what NOT to). This is John's "Reference Authority" section and it maps 1:1 onto our asset-lock discipline.

| Ref | Authority (borrow) | Do NOT borrow | Our analog |
|---|---|---|---|
| **Image A — layout template** | page architecture *literally*: page shape, outer border, panel borders, gutter positions, relative panel sizes, approximate staging, character positions, object counts, eyelines, beats | its flat shapes/silhouettes must NOT appear in the final art | locks composition; **= what the rigid CLARION grid needs** |
| **Character sheet(s)** (turnaround / identity) | face, hair, costume, build, line economy for that character | pose/framing (comes from the beat) | our model-sheet asset-lock |
| **Prior finished page** | series look: page finish, gutters, caption-box color & style, lettering, color grouping, print grain, overall integration | its specific content | continuity anchor across pages |
| **Expression/framing ref** (per-panel, optional) | expression quality, tone, framing for ONE named panel | clothing/setting | targeted fix for a hero beat |
| **Style panel(s)** (from the moodboard) | the deconstructed look — line weight, hatch type, ink behavior, palette, paper stock | content | `LEADS.md` references → prompts |

> Refs live in `the-solvent/refs/`. Name them so the authority is obvious (`layout-pXX.png`, `vane-sheet.png`, `witness-sheet.png`, `prior-page-pXX.png`, `style-clarion-ware.png`, `style-solvent-sienkiewicz.png`).

**Proven exemplars — look at these before writing (`../conversation/john/summer_with_charlie/`):**
- **`structure_lock.png`** = what an **Image A** actually is: *not* a wireframe of boxes but a **flat-color silhouette colorblock of the real composition** — correct staging, figure positions, object counts, color zones, panel sizes — with zero rendering. The gen replaces the flat shapes with finished art (which is why the prompt says "Image A's flat shapes must NOT appear in the final").
- **`mike_turnaround.png`** = the **character-sheet format**: a 6-angle turnaround (front · ¾-front · side-L · side-R · ¾-back · back) + a **MOVEMENT / ACTION POSES** row (walking, running, turning, idle, looking-over-shoulder) + a **bio callout box** (age, era, temperament). Build the Vane and Witness sheets to this spec.
- **`page1`–`page6`** = the **finished proof, and the canonical "prior finished page" continuity anchor.** They demonstrate the recipe holds at full scale: legible hand-lettered all-caps yellow captions, one character consistent across day/dusk/night/moonlight, one stable series look (warm muted printed-comic, clean contour, grouped blacks). Feed the latest finished page as the series-look ref for the next.

---

## 2. The prompt architecture — *the reusable page-prompt skeleton*

John's page-prompt is a fixed skeleton. Fill it per page. Order matters (references and style first, then global continuity, then panel-by-panel, then the negative list last so it sticks).

```
[FORMAT]  One finished comic PAGE, <aspect> (the-solvent = 2:3 portrait), high resolution.
          <N> panels: <layout in words, mirroring Image A>.

[REFERENCE AUTHORITY]  per attached ref: what to borrow / what NOT to. (table §1)
          "Treat Image A as a literal page template, not inspiration. Copy its panel
           layout exactly. Do not rebalance, improve, or redesign the arrangement.
           Replace its flat blocking with finished comic art."

[SERIES STYLE]  the house look in lift-able vocab (line, shadow, rendering, finish).
          All captions: one lettering style, one size, one caption-box tone.
          Emphasis = heavier ink only, NEVER larger text.

[GLOBAL CONTINUITY]  setting + time-of-day arc + per-character bible lines +
          key recurring objects/light sources rendered as DESIGNED graphic shapes
          (e.g. headlight cones = hard-edged flat fills, not atmospheric glow).

[PANEL N]  (repeat per panel)
          Framing: <shot type / angle>
          Visual center: <the one thing the panel is about>
          Beat: <what happens>
          Contents: <FG / MG / BG, staged>
          Eyelines: <who looks where>
          Caption/bubble: "<EXACT TEXT>"  + position  + (subtle emphasis word)
          Panel constraints: <the 2-3 things that must hold>

[GLOBAL CONTINUITY RULES]  costume consistency, object counts that must match across
          panels, caption text reproduced EXACTLY + positions respected.

[DO NOT]  the negative list — reproduce Image A's flat shapes; add production-sheet
          elements/panel numbers/keys; redesign layout; add unnamed characters; add
          motion lines/sparkles/blur unless called for; paraphrase captions; leave
          edge whitespace; look like a storyboard/concept sheet.

[FINAL]  Output only the finished comic page, following Image A's layout exactly.
```

**Why each block earns its place:** Reference Authority + layout-lock = composition control; Series Style + prior-page = look continuity; Global Continuity = character/object consistency; per-panel beats = staging; the DO-NOT list = suppressing the model's defaults (production-sheet look, layout drift, caption paraphrase). Note John's caption discipline: **exact text, exact position, emphasis by ink-weight not size** — text rendering is load-bearing and GPT-Image-2 must reproduce it verbatim.

**Controllability tactic — declare a screen-direction convention** (from `../conversation/john/tests/one_hand_other_hand.txt`). For any page where left/right or mirroring matters, state it explicitly near the top: *"All left/right are screen directions from the viewer; screen-left = the left side of the finished image; do not use anatomical left/right unless stated."* John's two-panel "ON THE ONE HAND… / BUT ON THE OTHER HAND…" test uses this to force the **active hand to switch across the gutter** — precise mirrored composition. Directly load-bearing for the-solvent (§4).

---

## 3. The orchestration discipline — *the variation mechanism* (from John's `AGENTS.md`)

How to spawn gens so variants stay clean and consistency doesn't rot. This is exactly how Codex should run:

- **One fresh-context subagent per variant** — including a single variant. `fork_context: false`.
- **Pre-assign exact output filenames** before spawning; pass each subagent its filename. Do **not** let subagents pick "next available."
- **No context reuse between variants.** Don't pass prior variants, previews, or critique from one to another — *unless* the user explicitly asks for an iterative correction pass.
- **Why:** prevents image-gen context pollution from the main conversation and cross-variant bleed. (This is the disciplined form of our own hardest lesson — context contamination wrecking cross-panel consistency.)

---

## 4. Two-register application — *the solvent's specific demand*

The book's whole conceit is **two opposed drawing systems** (`CONCEPT.md`). Each register uses the recipe differently:

### CLARION register — control / gold monument
- **Layout-lock is your friend.** Feed a rigid equal-panel grid as **Image A** → the model can't wander the architecture, which *is* the "total control of the page" idea. Maximal controllability — the easy pole.
- Style panels: Chris Ware (flat planar, ruler-straight, ligne claire), Williams III (illuminated gold leaf), Geof Darrow (hyperdetail). See `LEADS.md` for lift-vocab.
- **Vane's face identical across panels** is load-bearing (it *is* the self-image) → character sheet + repetition in the beat.

### the solvent register — dissolution / white eating inward
- **The hard pole, and exactly our facture problem.** Our finding (`project_nb2-facture-ceiling`): facture transfers by **showing** (reference crops), not by description — and GPT-Image-2 does facture better than NB2. So the dissolution look (Sienkiewicz ink-wash bleed / McKean smear) must come from **style reference panels**, not adjectives alone. This is why the engine is GPT-Image-2.
- **The border-failing / white-flooding-gutter is a LAYOUT effect** → it can be driven by an Image A whose gutter is deliberately widened/broken, OR composited (see fallback below).
- **Host vs Witness = two drawing systems on one page** (the *Asterios Polyp* move): Vane in rigid hyperdetail, the Witness in a simpler/softer line. Feed *both* style refs and assign each to its figure; if the model blends them, composite. When Vane and the Witness **mirror across a gutter**, use the **screen-direction convention** (§2) to lock who's on which side — John's two-panel mirror test (`one_hand_other_hand.txt`) is the proof-of-method for exactly this gutter-mirroring control.

### Fallback (from `opening-tests.md`)
If a full page garbles (lettering density + character consistency + the gutter trick is a lot to ask in one shot): **build panels separately with controlled white space and composite** — which is also how a real comic page is assembled. The gutter-failure can be composited deliberately.

---

## The loop, end to end
1. Pick or build the **layout template** (Image A) for the page.
2. Assemble the **reference stack** (§1) into `refs/`, each with declared authority.
3. Fill the **prompt architecture** (§2) for the page.
4. Spawn under the **orchestration discipline** (§3) — Codex, GPT-Image-2, pre-named outputs.
5. **Review** against the two-register intent (§4) + the bible. Log result + output filename back to the prompt (breadcrumb discipline).
6. Reference panels you want to chase → drop in `refs/`, deconstruct via `LEADS.md` into lift-vocab.

> **Reusability note:** this recipe is project-agnostic (it's John's general comic system). It currently lives in `the-solvent/` because that's the active project; it's promotable to a shared `production/` recipe later if/when the vault structure is ported repo-wide (see `../VAULT_MIGRATION_PROPOSAL.md`).
