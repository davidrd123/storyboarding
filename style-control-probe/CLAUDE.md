---
name: style-control-probe
description: "Style-control probe: can closed image models (NB2, GPT-Image-2) reproduce a chosen MidJourney style on new subjects? Structured after Patrick's vault_gml visual layer (look + prompts-active + breadcrumb discipline)."
---

# Style-Control Probe

Phase-0 style-controllability work (see `../STORYBOARD_SYSTEM_BRIEF.md` §"Phase 0", `../PHASE_A_GOALS.md` §3). Question: how faithfully can a closed model capture a style-atom from the mood board (`../MidJourney/2026-05-21/`) and apply it to a fresh subject, using the borrow-style-only grammar?

Organized after `WorkingSpace/patrick/vault_gml/visual/`: a **look** file holds the style spec + System Instruction; a **prompts-*-active** file is the versioned breadcrumb; outputs land in `outputs/` (gitignored). Review discipline = the `generation-review-loop` skill (6 dimensions, mode declaration, log-before-fire).

| File | Contents & task triggers |
|------|--------------------------|
| [`look-search-line-expressionism.md`](look-search-line-expressionism.md) | **Branch 1 (line-based, EASY).** Style look + System Instruction + borrow-style-only fence + 5 axes. Anchor = Hephaestus frame, job `054e808b`. Locked ~80–88 on NB2. |
| [`prompts-greek-hybrid-active.md`](prompts-greek-hybrid-active.md) | Active breadcrumb for branch 1 — Greek-gods-in-hybrid scenes on NB2. `vNN` = style-ref gen, `eNN` = edit. Log before firing, result after. |
| [`look-goya-dark-impasto.md`](look-goya-dark-impasto.md) | **Branch 2 (paint-surface, HARD — PARKED).** Goya-dark / Kirchner-Nolde impasto. Anchor = Saturn frame, job `c42475f0`. v01 finding: palette/value transfer (~85) but **facture/impasto does not** (~15) — NB2 reverts to clean render. David: "looks terrible" → parked. |
| [`prompts-goya-active.md`](prompts-goya-active.md) | Active breadcrumb for branch 2 (parked at v01). |
| [`look-litho-crayon-duotone.md`](look-litho-crayon-duotone.md) | **Branch 3 (print-process).** Die Brücke litho-crayon duotone. Anchor = Cerberus frame, job `8f5831c8` (`../MidJourney/2026-05-23/`). v01: locks ~80 (`_02`) — tri-tone exact, reproduced the *print object* (margins/edition no./monogram). Residual = micro-grain. |
| [`prompts-litho-active.md`](prompts-litho-active.md) | Active breadcrumb for branch 3. Crops (show-don't-tell) + artist-trim → **NB2 82 @ 20s** (production recipe); GPT+crops 85 @ 100s (hero ceiling). Earlier "facture ceiling" was a prompting limit, not structural. |
| [`prompts-coverage-active.md`](prompts-coverage-active.md) | **Coverage probe.** Treats the v06 master as an establishing wide → alternate camera angles of the same scene (flipped fence: preserve world, change camera). c01–c03 pass on NB2 → scene coverage works; storyboard premise validated. |
| [`LOG.md`](LOG.md) | **Running lab log** — session decisions, cross-branch findings, rigor items, experiment queue. The meta-layer above the breadcrumbs. |
| `outputs/` | Generated frames + `job.json` sidecars (`outputs/YYYY-MM-DD/gemini-31-flash-image-preview/NN_<title>_<hash>/`). Gitignored. |

**Stack Order:** look System Instruction → per-prompt (fence + scene). **Model:** `gemini-3.1-flash-image-preview` (NB2). **GPT-Image-2** comparison runs via `../scripts/gen_openai.py` later.
