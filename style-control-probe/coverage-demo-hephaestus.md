---
name: coverage-demo-hephaestus
description: "End-to-end demo of patterns/coverage-discovery-schema.md: a hand-authored brief + bible for the Hephaestus forge scene, the manifest the schema DERIVES from them, and the rendered coverage."
type: demo
tags: [coverage, storyboard, schema, demo]
related:
  - "../patterns/coverage-discovery-schema.md"
  - "prompts-coverage-active.md"
---

# Coverage-Discovery Demo — Hephaestus forge-line

Demonstrates `patterns/coverage-discovery-schema.md` end-to-end. **§1–2 are the INPUTS** (authored by hand — the brief + bible we didn't have). **§3 is the schema's OUTPUT** (derived by the engine, not hand-picked). **§4 is the render.**

---

## 1. Asset & Character Bible  *(INPUT — grounded in the MJ source `…Hephaestuss_automata…3c793ade…_0.png`)*

**Character — HEPHAESTUS:** middle-aged smith; fair/blond shoulder-length hair, full beard; pale cream toga/work-robe off one shoulder; broad, stooped. Sole identity anchor.

**Key assets:**
- **GOLD AUTOMATA** — classical-featured humanoid figures in burnished gold, serene blank faces, visible seams/joints; *many identical* on the line.
- **WELDER ARMS** — overhead articulated robotic arms with sparking tool-heads.
- **THE LINE** — a long conveyor/assembly rail receding deep into the workshop.

**Environment:** cavernous industrial forge, cool blue-violet shadow, volumetric haze, a tall red furnace column.

**Style direction:** painterly cinematic concept-art (cool blue/violet + warm gold + orange spark-light); not photoreal, not litho.

## 2. Scene Brief  *(INPUT)*

- **Beat / action:** Hephaestus **lifts** a just-finished automaton off the line and **inspects its face.** *(Verb = lifts/handles/looks.)*
- **Purpose:** reveal the maker's relationship to what he builds.
- **Emotional register:** weary tenderness, edged with unease.
- **Subtext:** a craftsman and his creation — but he's made an *army of identical others*; does the thing look back?
- **Obligations:** none.

---

## 3. Derived Manifest  *(OUTPUT — the engine walking §2's nouns/verbs against §1)*

| # | Shot | Derived by rule | Why | Tier |
|---|------|-----------------|-----|------|
| A | Wide — the line receding into the workshop | 1 establishing | scale + automata *en masse* | **1** |
| B | Medium — Hephaestus lifting the automaton off the line | 2 character | the action beat | **1** |
| C | CU — Hephaestus's face | 2 face | the maker's regard (subtext) | **1** |
| D | **Insert — his hands cradling the automaton's gold face/shoulder** | **2 hands (verb "lifts")** | tactile authorship — *not in the brief; the engine surfaced it* | **1** |
| E | CU — the automaton's serene blank face | 3 asset-face | the created gaze; eyeline-pairs with C ("does it look back?") | **1** |
| F | OTS behind the automaton → the receding army of identical others | 4 exchange + 5 subtext | "he made an army" — carries the subtext | **1** |
| G | POV — what Hephaestus sees: the endless line | 2 POV | his vantage; the scale of the task | 2 |
| H | Insert — welder spark on a gold seam | 3 asset + kinetic | the act of making (punctuation) | 2 |

**Contrast gate:** wide (A) ↔ tight (D,E) ✓ · face (C,E) ↔ back/OTS (F) ✓ · static ↔ kinetic (H) ✓.
**Engine's discoveries (beyond the obvious wide/medium/CU):** D (hands), E (automaton-face eyeline pair), F (the army/subtext), G (POV). These fell out of the *verb* + the *asset* + the *subtext* — exactly the "coverage you didn't know to ask for."

## 4. Render

One-shot storyboard page of the **Tier-1** set (A–F) per the generation doctrine (one-shot the page; style from the source). Output: `outputs/2026-05-24/gemini-31-flash-image-preview/01_hephaestus-derived-coverage_ea50d0f5/…_0{1,2}.png`.

**Result — SUCCESS.** Coherent 6-panel page, same Hephaestus + automata + concept-art palette throughout; labels A–F correct. The engine's **discovered** shots all landed: **D** (hands cradling the gold face — tactile authorship), **E** (automaton's gaze to camera — eyeline-pairs with C: *does it look back?*), **F** (the receding army — subtext visible). Proof point: vs. the earlier ad-hoc `hp-sp01` page (generic "down-the-line" / "low-angle-arms" filler), the **derived** page produced story-driven coverage (hands insert, C↔E eyeline pair, army-OTS) that a naive shot list misses. End-to-end chain validated: authored brief+bible → engine-derived manifest → one-shot render.

### Hero render — GPT-Image-2 + 180° rule + rich subtext (2026-05-24)

Re-rendered the derived A–F on **GPT-Image-2** with the action axis enforced (Hephaestus screen-left facing right; automaton screen-right facing left) and the full subtext loaded. Output: `gpt-image-2/01_hephaestus-coverage-gpt-180_71494586/`. **Result — the strongest board of the session.** (1) **180 held:** C (Hephaestus looks right) + E (automaton looks left) = a true eyeline match across the cut — fixes the B→C flip the NB2 page had. (2) **Far richer:** painterly finished-concept-art quality; C reads as grief, D intimate, E's automaton gaze genuinely uncanny — the "does it look back" subtext is in the image. GPT's over-rendering is an asset for an expressive narrative board (vs. a liability for raw litho facture). Confirms: enforce the axis in-prompt + subtext-rich → GPT-Image-2 (hero); NB2 for fast coverage volume.

---

## Beat 7 — The Reckoning  *(schema run on a 2nd beat, 2026-05-24)*

**Brief:** the patron Kronos/Saturn has come; the line is halted; Hephaestus has hidden the one automaton that looked back, and faces the consequence — he loses his place but keeps the one. **Subtext:** needed-back > needed; the cost of conscience; the patron's faceless devouring authority. **Axis:** Hephaestus screen-left facing right; the patron's dark mass screen-right.

Derived 6-panel Tier-1: (1) WIDE forge stilled, shadow across ranks; (2) LOW-ANGLE the faceless towering patron (R); (3) MEDIUM Hephaestus before the shadow (L, facing R); (4) INSERT his hand hiding the one; (5) CU the hidden automaton's open eyes toward him; (6) FINAL alone with the one, ranks dark. Engine's discoveries: the patron's looming-presence shot (new asset), the concealing-hand insert (hands+subtext), the protected-automaton CU, the bittersweet keep (subtext select). Render: GPT-Image-2 → `gpt-image-2/01_hephaestus-beat7-reckoning_*`.
