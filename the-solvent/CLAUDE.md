---
name: the-solvent
description: "Router + operating manual for THE SOLVENT graphic-novel project. Entry point: what's here, who does what (Codex gens / Claude structures), and the session discipline. Read CONCEPT + RECIPE + STATUS to pick up cold."
---

# THE SOLVENT — project router

A graphic novel where a mogul-president's ego is rendered *as the comic page itself*, and a buried alter administers a dissolution drug from inside the gutters. Full premise → `CONCEPT.md`.

## Read first (cold-start / fresh-agent pickup)
1. **`CONCEPT.md`** — the story, the cast, the form-as-content conceit, the 6 opening pages.
2. **`RECIPE.md`** — how to generate a page (John's proven system, ported + the two-register application).
3. **`STATUS.md`** — current phase, what's been generated, verdicts, next actions.
4. **`LEADS.md`** — reading list + the two registers' deconstructable visual references, with prompt-vocab.

## File map
| Path | What it's for |
|------|---------------|
| `CONCEPT.md` | Story, premise, cast, two-register conceit, opening-6 beat-board, open *creative* questions |
| `RECIPE.md` | The page-generation recipe — reference stack, prompt architecture, variant orchestration, two-register application. **Use for any page.** |
| `LEADS.md` | Reading kin + visual references by register (CLARION control / the solvent dissolution), with lift-able prompt-vocab |
| `prompts/` | The actual page/test prompts — logged **before** firing, result + output filename **after** (breadcrumb) |
| `refs/` | Reference images: layout colorblocks (Image A), character sheets, prior finished pages, style panels |
| `STATUS.md` | Live dashboard — phase, gen log (pointer), next actions |

**Outputs convention:** gens land under `outputs/<batch>/<YYYY-MM-DD>-<label>/<file>.png` (gitignored). Current batches: `opening-tests/` and `style-tests/` (GPT-Image-2, breadcrumbed in `prompts/`), `style-probes/` (NB2 exploration, self-described in its own README). Going forward prefer a single `style/` batch with a per-run README over the `style-tests/` vs `style-probes/` split.

## Division of labor (Claude is the driver here)
- **Claude (here) — primary driver.** Owns concept, recipe, QC/review, structure — **and runs the page gens**, via **NB2 / riff-mcp (`mcp__gemini-prompts__generate_image`)**. The strongest work to date (the opening sequence, the page-5 dead-channel, the deep-dissolution splash) is Claude-driven NB2. This is our lane — assert it.
- **Engine policy:** **NB2 via riff-mcp is the working engine** — confirmed fine across registers, *including* the dissolution/facture look (the earlier "NB2 ceiling on dissolution" worry did **not** hold up; the loved dissolution pages are NB2). **Codex / GPT-Image-2 (free on Max) is an OPTIONAL finishing pass** — crisper lettering or denser ink-facture on the clean gold-control register — not the default, not required.
- **Codex:** runs a GPT-Image-2 finishing/lettering pass from `prompts/` when asked; owns nothing by default.
- Breadcrumb + fresh-agent discipline below applies to whoever fires the gen.

## How we work here — session discipline *(Patrick's habits, scoped)*
- **Log the prompt BEFORE firing; log the output filename the instant it lands**, under that prompt. The prompt→output link is the production record — without it a gen is unrecoverable.
- **Append, don't overwrite.** Version prompts down the file; the history is part of the record.
- **Take what's good.** A gen rarely fails entirely — extract the seed/phrase/panel/crop that worked, carry it forward, change only what didn't. Log a seed/phrase that behaved as a reusable asset.
- **One fresh-context subagent per variant** (including a single variant): `fork_context: false`, pre-assign each subagent its exact output filename, and pass no prior variants/previews/critique between them — *unless* you're explicitly running an iterative correction pass. This prevents cross-variant context pollution. (Full rationale: John's `../conversation/john/AGENTS.md`.)
- **Fresh-agent test:** a new agent reading `CONCEPT` + `RECIPE` + `STATUS` should be able to make the next gen with no chat history. If it couldn't, write what's missing into `STATUS` before closing out.

## Note
This applies Patrick's vault structure (`../VAULT_MIGRATION_PROPOSAL.md`) to the smallest, greenfield, least-coupled corner of the repo — **the-solvent is the structure pilot.**
