# Identity Reference Probe — composite vs atomized

Maps to `PHASE_A_GOALS.md` §3 (which refs disambiguate prose) and the deep-research recommendation (`deep-research/2026-05-19/reply01.md` §2): run composite-vs-single character references head-to-head and measure identity preservation across varied panels.

**Question:** does a multi-angle composite character sheet preserve identity *better* than a single hero reference, across panels — especially panels showing angles the single ref never depicted?

---

## Gating step (DONE) — character sheet generation

Generated `refs/cowboy_turnaround_sheet.png` from the single Damaggio hero ref (`cowboy_single_hero.jpg`) + style ref, in one shot with Nano Banana Pro. Four angles (front / three-quarter / profile / back), consistent costume, neutral cream ground, flat lighting.

**Result:** clean and usable on first successful fire. This is a positive result for the brief's "hardest step" (§3.7 — bible creation). NB Pro produced a coherent multi-angle turnaround from a single front-ish hero ref. (Took 3 API retries due to a Google-side 502/503 wobble on 2026-05-21, unrelated to the prompt.)

---

## Head-to-head design

Three test panels, each fired twice — once with the composite sheet as identity ref (Variant A), once with the single hero ref (Variant B). Same prompt, same style ref, only the identity ref differs.

| Panel | Shot | What it stresses | Hypothesis |
|---|---|---|---|
| P1 | CU three-quarter front, tense reaction | Face under close scrutiny | Roughly even — single ref already shows this angle |
| P2 | FS action, drawing revolver, mid-stride | Build, costume, silhouette in motion | Composite slightly ahead (body/costume from multiple angles) |
| P3 | MS from behind, walking away toward a ridge | A rear angle the single hero ref NEVER showed | **Composite should win clearly** — this is the cleanest test of multi-angle value |

**Refs:**
- `refs/cowboy_turnaround_sheet.png` — composite (Variant A identity ref)
- `refs/cowboy_single_hero.jpg` — single hero (Variant B identity ref)
- `refs/style_anchor.jpg` — style ref (both variants)

**Scoring:** each output scored by `gemini-3.5-flash` against the original canonical identity (`cowboy_single_hero.jpg` as the ground-truth identity ref for *both* variants — the fair comparison). Primary metric: preservation_fidelity (identity carry-through). Watch P3 especially.

**Decision rule:** if composite wins materially on P3 (the unseen angle) and ties elsewhere, the bible needs a turnaround sheet, not just a hero shot. If single ref holds even on P3, a hero shot may be enough to start — cheaper bible.

---

## Outputs

Filenames: `idp-[panel]-[variant]_NN.png` where variant = `comp` (composite) or `solo` (single).
Land in `outputs/YYYY-MM-DD/`.
