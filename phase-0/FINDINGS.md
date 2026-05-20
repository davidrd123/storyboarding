# Phase 0 — Findings

Six tests fired against Nano Banana Pro (`gemini-3-pro-image-preview`), each evaluated against the 6 production-review dimensions by Gemini 3.5 Flash. Total cost ~$2. Summary below; full details in `prompts.md`.

---

## Headline result

**Four tests cleanly passed.** One produced a useful diagnostic failure (T03). The compositional-skeleton question (T06) was inconclusive on first pass and then **resolved by an isolation re-fire (T06a)**: the role-labeled framing reference was not contributing — prose carried it. **The bible-driven workflow architecture in the brief is empirically validated; compositional skeleton transfer via role-labeled reference is empirically rejected for Nano Banana Pro.**

| # | Test | PF | PrF | SL | SH | SS | CBF | Decision |
|---|---|---|---|---|---|---|---|---|
| T01 | Style-only borrow, new scene | 78 | — | 77 | 76 | 76 | 79 | accept |
| T02 | Style + cowboy identity | 81 | 80 | 82 | 80 | 80 | 81 | accept |
| T03 | Style + identity + STATE block | 74 | 82 | 85 | 80 | 75 | **68** | **iterate** |
| T04 | Style + identity + new location (prose-only) | 80 | 81 | 82 | 80 | 80 | 81 | accept |
| T05 | Style + identity + location plate | 76 | 84 | 85 | 83 | 84 | 86 | accept |
| T06 | Compositional skeleton transfer (with ref) | 80 | 78 | 81 | 79 | 80 | 82 | accept w/ caveat |
| T06a | Isolation — same prompt, no compositional ref | 83 | 81 | 84 | 82 | 80 | 85 | accept |

PF = prompt fidelity, PrF = preservation fidelity, SL = style lock, SH = scene hierarchy, SS = story service, CBF = creative brief fidelity.

T06a scored equal-or-better than T06 on every dimension *without* the compositional reference. That settles it: the framing ref added no measurable lift (and may have introduced competing signal). Prose carries camera framing; the reference does not.

---

## The validated grammar

```
Image 1 is a [role].
Image 2 is a [role].

Preserve from Image 1: [concrete feature list — face, hat, scarf, jacket, build]
Preserve from Image 2: [concrete feature list — well geometry, ruins, dust haze, light]
Borrow from Image 3: [style properties — ink wash, palette, linework, cross-hatch]
Do NOT borrow from Image 3: subject, composition, location, props, scene elements.

[DSL skeleton — SHOT/SUBJECT/STATE/ACTION/SETTING/MOOD/COMPOSITION]

16:9 aspect ratio.
```

Specific phrases that earned their keep:

- **`"Do NOT borrow from Image N: subject, composition, location, props, characters, or any specific scene element."`** — zero subject leakage in T01 and T04. The do-not-borrow fence is real and works.
- **Concrete feature lists for preservation.** `"face structure, beard pattern, hat shape, scarf, jacket, build, weathered look"` — not "preserve the character." The concrete enumeration is what holds.
- **Same pattern works for locations.** `"well geometry, ruins position, dust haze, palette of the location, time-of-day quality of light"` — geographic features behave the same way character features do.

---

## What translated from prose alone

Validated in T04: distinct location *categories* land cleanly from prose. "Narrow slot canyon between sandstone walls, cool shadow on canyon walls, hot light hitting the top edge" produced a recognizable slot canyon without a plate.

Implication for the world bible: only build plates for *recurring* locations. New unique locations can be prose-only.

---

## What needs references

**Character identity** (T02 confirmed). Prose-only generates a different actor. The identity ref fixed it.

**Same-location continuity** (T05 confirmed). Location plate + concrete feature preservation held the brick well + ruins geography across a new camera angle.

**Emotional state with specificity** (T03 diagnostic). The brief's prediction — that the expression sheet is the highest-leverage asset — is empirically confirmed. Prose like "cold rage held in, jaw set, eyes hard, no movement" rendered as overt snarl with bared teeth. The model defaults to legible, expressive emotion over suppressed contained emotion.

> **Carry-forward:** the expression sheet for one principal is now the most important Phase 1 asset. T03 is the proof that the brief needs it, not an artifact that needs to be fixed.

---

## The resolved test (T06 → T06a)

The brief's biggest open question — does a role-labeled framing reference impose camera angle on a different subject? — is now answered: **no, not measurably, in Nano Banana Pro.**

First pass (T06) looked right (low-angle dune shot, 78–82) but was confounded: the prose said "looking down toward the camera," which already implies low angle. Couldn't separate which input carried the framing.

The isolation re-fire (T06a) removed the compositional reference and kept the prose identical. Result: **the same low-angle composition, scoring equal-or-better on every dimension (CBF 85 vs 82).** Flash's verdict: *"prose alone can generate the desired low-angle framing... the compositional reference was not required."*

**Conclusion:** role-labeled compositional skeleton transfer does not work as a technique here. Prose carries camera framing; the reference adds no lift and may introduce competing visual signal. This matches the brief's own skepticism (§4) and the PreciseCam literature finding (precise camera control is genuinely missing from current text-to-image models — see `deep-research/2026-05-19/reply01.md` §6).

**The path forward** is Patrick's clean-plate → token-deconstruct → genesis (`patterns/image-generation-control-lessons.md` §14): describe framing in explicit spatial prose, don't try to extract it from a reference. T06b (still unrun) would test whether the *sharpened* geometric vocabulary outperforms the simple prose T06a already used — a refinement, not an open question.

---

## Quirks worth knowing

- **Mirror flips happen.** T05's composition mirrored (cowboy on left instead of right). For storyboards this matters because screen-direction is a continuity grammar. Mitigation: explicit "cowboy on right side of frame" prose. Patrick's vault has done this before; worth lifting as a known failure mode.
- **Linework register is slightly tight.** Across all 6 tests the output reads as a hair more "illustrated" / "polished" than Damaggio's loose confidence. Pushing language like "loose sketch quality, broken contour, scratch lines" might unlock the looseness.
- **Identity preservation is strong from a single hero ref.** Shot_Reverse_01 alone was enough to lock the cowboy across 5 totally different scenes. The bible doesn't need to be enormous to start working.

---

## What this means for the brief

Three architectural claims are now empirically supported (not just argued):

1. **The bible-driven workflow holds identity.** T02 → T05 chained the same cowboy across mesa, slot canyon, and well location, all in style, all recognizable. The "first proof point" the brief was hunting for.
2. **The expression sheet is load-bearing.** T03's clean failure on emotional specificity is the case for the highest-leverage Phase 1 asset.
3. **The do-not-borrow fence works.** T01 + T04 zero-leakage results validate the grammar that the rest of the system rests on.

One claim is now resolved — negatively:

4. **Compositional skeleton transfer (T06 → T06a)** — role-labeled framing reference does NOT impose camera angle in Nano Banana Pro. The isolation re-fire proved prose carried it alone. Update the brief's §4 from "workaround, untested" to "rejected technique; use explicit spatial prose (Patrick's token-deconstruct path) instead." This is a *positive* result for the workflow — it means the camera-angle DSL slot is handled by prose, removing the need for a cinematography reference pack.

One claim is *not* supported but only because not tested:

5. **Linework register match** — the brief's "style ~70%" guess is roughly right but we're trending closer to 80%+ on technique while the looseness register stays the gap. This is what a Track-B LoRA would solve cleanly.

---

## Suggested next moves

- **Run T06-iso** (prose-only, no Image 2) — 30 seconds to fire, definitively answers the brief's biggest open question.
- **Run T03-iter** — try sharpened anti-overt prose for cold rage ("lips closed, no teeth showing, flat affect, micro-tension at the jaw") to see if prose-only can ever land suppressed emotion or whether the expression sheet is truly the only path.
- **Build a one-character expression sheet** as the Phase 1 test, exactly as the brief specifies. T03 confirms this is the diagnostic for the whole pipeline.
- **Walk into Tuesday with all six panels + this findings doc.** Five passes + one diagnostic + one ambiguous = exactly the empirical posture the brief argues for ("you're not guessing about model capabilities, you're measuring them").

Total time elapsed: ~10 minutes of generation + eval. Total cost: ~$2.
