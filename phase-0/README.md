# Phase 0 — Style Seed + Prompt Grammar Validation

Per the brief's Phase 0 protocol. Goal is **not** a finished panel — it's learning how the model responds to the preserve/borrow/do-not-borrow grammar and mapping which DSL slots actually translate from prose vs. need references.

Outputs an evidence base for Tuesday rather than a polished demo.

---

## Source material

Four Damaggio panels in `sample-image-in/`, role-tagged copies in `refs/`:

| Role | File | Source | What it locks |
|---|---|---|---|
| Style anchors | `refs/style/damaggio_01–04.jpg` | all four | Ink wash + duotone palette + linework |
| Cowboy identity | `refs/characters/cowboy_hero_ref.jpg` | Shot_Reverse_01 | Face, hat, scarf, build (best face read of the four) |
| Officer identity | `refs/characters/officer_hero_ref.jpg` | Shot_Reverse_02 | Face, uniform, build |
| Location plate | `refs/locations/well_ruins_plate.jpg` | Establish | Brick well + ruins + camel + dust haze geography |

Same source images appear in multiple role folders — that's intentional. An image's *role* is set by the prompt, not by the file. Copies are organized for easy reference assembly per test.

---

## What we're testing

Each test cell answers one open question from the brief. Order matters — early tests inform later ones.

| # | Test | Question it answers | Brief reference |
|---|---|---|---|
| T1 | Style-only borrow, new scene | Does "borrow style, do NOT borrow subject" actually hold? How aggressive does the do-not-borrow have to be? | §4 Reference Grammar |
| T2 | Style + cowboy identity | Does the character-bible-driven workflow hold identity across a new scene? | §3 Bibles, §C9 deep-research |
| T3 | Style + cowboy identity + state | Does prose `STATE` block + identity ref render emotionally specific results? | §2 DSL — Identity/State/Action |
| T4 | Style + identity + new location prose | Can the model generate the *same character* in a *described new location* without a location plate? | Maps the prose-only ceiling |
| T5 | Style + identity + location plate | Does an explicit location plate hold same-place continuity? | §3.6 World Bible |
| T6 | Compositional skeleton transfer | Can a low-angle reference of a *different subject* impose framing on a new generation? **The brief's biggest open question.** | §4 "compositional skeleton transfer", deep-research #6 |

T1–T5 build the bible-workflow proof. T6 is the wildcard — likely partial result, mapped against Patrick's clean-plate → token-deconstruct fallback (see `patterns/image-generation-control-lessons.md` §14).

---

## How to fire (model-agnostic)

The prompt log in `prompts.md` is written to be model-agnostic — each entry has a `Model:` field. Recommended first pass: **Nano Banana Pro (`gemini-3-pro-image-preview`)** since Patrick's vault has working production discipline against it.

For a comparison pass, run the same prompts against **GPT Image 2 (`gpt-image-2`)** with high-quality settings. The 2×2 (model × test) is the actual deliverable.

Outputs land in `outputs/YYYY-MM-DD/`. Filename convention (per Patrick):

```
p0-t[NN]-[short-test-name]_[seed-or-iteration].png
```

e.g. `p0-t02-cowboy-identity-newscene_01.png`.

---

## Evaluation — the 6 dimensions

Per `patterns/image-generation-control-lessons.md` §9 and Patrick's `production-review-loop.md`:

1. **Prompt Fidelity** — did it execute the instruction?
2. **Preservation Fidelity** — did preserve-from-Image-N elements hold?
3. **Style Lock** — Damaggio ink wash, duotone palette, linework?
4. **Scene Hierarchy** — is the right element reading as hero?
5. **Story Service** — does it tell the intended beat?
6. **Continuity** *(storyboard-specific addition)* — would this cut next to the source panels without breaking the world?

Score each dimension on the calibrated 0–100 scale used by the evaluator. Accept at roughly ≥80 on the relevant dimensions; treat 60–79 as iterate / diagnose; treat <60 as re-roll or escalate. Hard limit: **5 grind iterations** per test before escalating.

---

## What "done" looks like

Phase 0 ends with:

1. A validated grammar template — the exact preserve/borrow/do-not-borrow phrasing that produced reliable results.
2. A confidence map by DSL slot — which slots translate from prose, which need refs, which fail even with refs.
3. A T6 verdict — compositional skeleton transfer works / doesn't / works with caveats.
4. Successful phrases logged for re-use (per Patrick's "save phrases verbatim" rule).
5. A failure-mode taxonomy populated from real outputs (not speculation).

That bundle is what walks into the Tuesday meeting with Ben.

---

## Genesis vs Mutation flagging

Each test in `prompts.md` is marked **genesis** or **mutation**. They want different reference strategies — see `patterns/image-generation-control-lessons.md` §11. Phase 0 is mostly genesis (no approved base plates exist yet); T3 may become mutation if T2 produces a usable cowboy frame.
