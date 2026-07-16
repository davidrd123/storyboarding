---
name: vault-migration-proposal
description: "Proposal (for review, NOT yet executed) to adopt Patrick's vault structure — nested CLAUDE.md routers + three root meta-files (CLAUDE.md / vault-guide.md / open-items.md) + vault-as-memory discipline — adapted to this repo's dual lab+production nature. Captured 2026-05-28 to think on further."
type: workflow
title: "Vault Migration Proposal"
tags: []
tier: production-tools
status: draft
system_directive: "A decision document to mull over, not a record of work done. Nothing here has been executed. Decisions D1–D5 are my recommended defaults (the user did not pick when asked); revise them, then we execute Step A first. Reference model: /Users/daviddickinson/Projects/Lora/ComfyPromptByAPI-patrick/WorkingSpace/patrick/vault_graffito."
related:
  - "STORYBOARD_SYSTEM_BRIEF.md"
  - "style-control-probe/CLAUDE.md"
  - "style-control-probe/LOG.md"
  - "story/hephaestus-forge/BIBLE.md"
---

# Vault Migration Proposal

> **Status: proposal for review — NOT executed.** No files have been moved, created, or modified as a result of this document (other than this file itself). This captures the plan so it can be considered before any reorganization happens. The decisions below (D1–D5) are *my recommended defaults* — when asked to pick the vault shape, consolidation aggressiveness, and first move, the answer was deferred, so I chose lowest-regret options and flagged them all as reversible. **Change any of them, then we start with Step A.**

## Context — why consider this

Patrick's `vault_graffito` (`/Users/daviddickinson/Projects/Lora/ComfyPromptByAPI-patrick/WorkingSpace/patrick/vault_graffito`) is a **production vault**:
- **Nested `CLAUDE.md` routing tables** — root → domain → subfolder. Each `CLAUDE.md` holds *no content*; it's a pure index/router with a trigger table whose descriptions are written as retrieval anchors (the literal test: *"if this vault had 200 files, would this line still route an agent to the right one?"*).
- **Three root meta-files:** `CLAUDE.md` (router + operating manual), `vault-guide.md` (a deterministic filing procedure — triage → folder → name → frontmatter → update the `CLAUDE.md` chain, with the trick *"find the analogous file first"*), and `open-items.md` (the live queue: TODO / OPEN / Resolved, each item linking its source file).
- **Uniform frontmatter schema** on every file (`type / tier / status / system_directive / related`) for human, agent, and RAG navigation.
- **Governing philosophy — vault-as-memory:** *"Source files are truth, conversations are intake."* The **fresh-agent test:** could someone reading only the vault make a good next decision? If not, something must be written before closing out.

This is worth adopting because this session's failures were all **organization** failures, not generation failures: the active repair target (which kit?) got lost; outputs live in scattered gitignored dated dumps; state is split across `LOG.md` / the handoff doc / `prompts-*-active` / agent-memory with **no single entry point**; and there is **no repo-root `CLAUDE.md`** at all.

We've already half-reinvented Patrick's pieces, ad hoc:
- `style-control-probe/CLAUDE.md` ≈ a domain router
- `LOG.md` ≈ a lab log
- `prompts-*-active.md` ≈ the fire-before / result-after breadcrumb discipline
- `style-control-probe/sessions/2026-05-24-handoff.md` ≈ the fresh-agent test, written from scratch each session
- `story/hephaestus-forge/BIBLE.md` ≈ a `world/`-domain bible

The one adaptation Patrick doesn't need: **we are dual-natured — an active R&D lab *and* the Hephaestus production.** Patrick is production-only, so he has no `research/` domain. We do.

**The three files the user named — root `CLAUDE.md`, `vault-guide.md`, `open-items.md` — are exactly Patrick's routing/meta overlay.** That overlay is ~80% of the value and carries near-zero breakage risk. So it's the primary deliverable; physical folder reshuffling is secondary and optional.

## Decisions (recommended defaults — reversible)

- **D1 — One unified vault at the repo root** (not a separate `film/` vault). Single project; the lab feeds production and already references the story/world bibles, so splitting would duplicate them.
- **D2 — Preserve the load-bearing state docs** (`LOG.md`, `prompts-*-active`, agent-memory); add the routing layer + one `open-items.md` on top. Per `feedback_proceed-systematically` — don't tear up working machinery. Harder consolidation can come later.
- **D3 — Routing overlay first; physical folder moves are incremental and optional** — forced by the relative-path coupling (see Risk). Also matches what was asked for.
- **D4 — The vault is the markdown routing tree.** Gitignored binary pools (`MidJourney/`, `sample-image-in/`, every `outputs/`, the `refs/`/`board/`/`panels-final/` image dirs) **stay in place**, referenced by path. `scripts/` stays at repo root (it's code, and is referenced as `../scripts/...` from several docs).
- **D5 — Agent-memory stays the complementary layer** (durable cross-session *facts/lessons*); the vault holds *session/execution state* + *creative source*. The boundary gets documented in root `CLAUDE.md`.

## Target domain model (logical → physical)

| Domain | Holds | Current physical home |
|---|---|---|
| `charter/` | system design & strategy | root: `STORYBOARD_SYSTEM_BRIEF.md`, `PHASE_A_GOALS.md`, `MEETING_BREAKDOWN.md`, `PRODUCTION_SYSTEM_FINDINGS.md`, `DESIGN_QUESTIONS.md`, `TEST_BEDS.md` |
| `world/` | aesthetic + character/asset OS | `story/…` bible specs, `MidJourney/srefs.md`, `style-control-probe/look-*.md` |
| `story/` | narrative | `story/hephaestus-gods-in-the-machine.md`, `story/hephaestus-forge/` |
| `production/` | how to generate | `patterns/*`, `scripts/*` (pointer), a new `qc-protocol.md` placeholder |
| `research/` | the probes (active) | `style-control-probe/`, `phase-0/`, `identity-ref-probe/`, `deep-research/` |
| `intake/` | raw collaborator input & chat logs | `conversation/`, `chats/`, root raw-chat exports, `Talk.md`, `outside-material/` |
| `meta/` | templates & registry | new; borrow `template-scene-breakdown/defense` from Patrick |

## Key risk — relative-path coupling (why we don't big-bang)

`style-control-probe/` docs and the root strategy docs are linked via `../`-relative paths across the repo (e.g. `style-control-probe/CLAUDE.md` → `../STORYBOARD_SYSTEM_BRIEF.md`, `../scripts/…`, `../story/…`, `../patterns/…`, `../MidJourney/…`). Physically moving these dirs into domain folders changes their depth and **silently breaks every such link**. Therefore physical consolidation must be incremental — fixing references per move, least-coupled dir first, `style-control-probe/` **last**.

## Build sequence

### Step A — Routing + meta overlay (do first; zero file moves, zero breakage)
The three named files:
1. **`CLAUDE.md`** (repo root) — vault description; **Loading Protocol** (mandatory cold-start reads: the story doc, the active scene `BIBLE.md`, `open-items.md`); a **trigger table** mapping the 7 logical domains to their *current* physical locations; the generation entry points (riff-mcp `generate_image` / `scripts/gen_openai.py` / `scripts/gen_seedance.py`); the **vault-as-memory** statement + the **agent-memory-vs-vault boundary** (D5); pointers to the generation skills.
2. **`vault-guide.md`** — filing procedure adapted from Patrick's: triage → folder (domain decision table + "find the analogous file first") → kebab-case naming + our conventions (`prompts-*-active`, `look-*`, `-vN`, dated session files) → frontmatter schema (`name/description/type/tier/status/system_directive/related`) → update every `CLAUDE.md` in the chain.
3. **`open-items.md`** — one consolidated live queue: *TODO (unwritten)* / *OPEN (creative & methodology questions)* / *TODO (tools not built)* / *Resolved*. Seeded from the real open threads found in the audit:
   - calibrated `compare_images` re-grade of the litho freehand numbers (75/78/82/85 are unanchored `analyze_image` guesses);
   - the **Gemini-as-eyes protocol — UNSOLVED** (bias-prone, single-axis-blind, calibration unknown; needs its own focused investigation before trusting it downstream);
   - the **story recognition fork** (woken-one = stranger vs = *her*);
   - the **camera/cutting layer** (extend `coverage-discovery-schema.md` with per-shot Director-Mode camera commands + cut/duration);
   - the **Hephaestus kit baseline decision** — NB-Pro repair is parked, not mandatory; GPT kit is the current stable consistency baseline to review against the clean-surface NB-Pro attempts;
   - NB delivery-channel control (style block as system vs prepended-to-prompt).

   This **subsumes the ad-hoc handoff doc** going forward.

### Step B — Domain `CLAUDE.md` routers in place (new files in existing dirs; zero breakage)
Add a routing-table `CLAUDE.md` to each dir that lacks one and is already a sensible domain: `story/`, `story/hephaestus-forge/`, `patterns/`, `phase-0/`, `identity-ref-probe/`, `deep-research/`, `conversation/`, `MidJourney/`. (`style-control-probe/CLAUDE.md` already exists — leave it.) Each row: `| [file](file) | what it's FOR + retrieval-anchor keywords |`, passing the "200-file routing test."

### Step C — Physical consolidation (OPTIONAL, later, incremental — only if the clean folders are wanted)
Per-domain, least-coupled first: `charter/` (move 6 root docs, fix the handful of `../` refs that point at them) → fold `patterns/` + `scripts/` reference under `production/` → group the probes under `research/` (fixing `../`→`../../` refs) with `style-control-probe/` **last**. Each move: `git mv`, then grep-and-fix inbound/outbound relative links, then re-run the fresh-agent test before the next move.

## Files created / moved
- **New (Step A+B):** `CLAUDE.md`, `vault-guide.md`, `open-items.md` (root); domain `CLAUDE.md` routers; `production/qc-protocol.md` placeholder; optional `meta/template-*`.
- **Retired (folded into `open-items.md`):** the per-session handoff pattern (`style-control-probe/sessions/*-handoff.md` becomes a thin pointer to `open-items.md`).
- **Unchanged:** `LOG.md`, all `prompts-*-active.md`, agent-memory, all gitignored image pools, `scripts/`.

## Reuse (don't reinvent)
- Patrick's `vault-guide.md`, `open-items.md`, and `CLAUDE.md` as **templates** to adapt (paths under `…/vault_graffito/`).
- Our existing `style-control-probe/CLAUDE.md` as the model for domain router tables.
- Patrick's `meta/template-scene-breakdown.md` & `template-scene-defense.md` if we adopt `meta/`.

## Verification — the fresh-agent test
After Step A (and again after each Step C move): spawn an `Explore` agent told to read **only** `CLAUDE.md` + `open-items.md` (no chat history, no memory) and answer *"What is the next concrete action on the Hephaestus forge kit, and which file holds the locked automaton design?"* If it routes correctly to `open-items.md` → `story/hephaestus-forge/BIBLE.md` and names the current baseline decision — GPT kit as stable consistency baseline, NB-Pro repair parked unless deliberately re-entered — the overlay works. Also confirm zero broken links after any Step C move with a relative-link grep.

## Out of scope (would be tracked in `open-items.md`, not part of building the structure)
- The **Hephaestus kit repair / baseline decision** itself.
- The **Gemini-as-eyes** investigation.
Both are *content* work the new structure will *host*, not part of standing up the structure.

---

## Appendix — open content state at time of writing (for whoever picks this up)

The repair thread this proposal interrupted, so it isn't lost:
- **NB-Pro is not the required path.** It was an attempted clean-surface route, but it kept creating enough cross-panel drift that a future agent should not blindly continue it.
- **Current stable baseline:** the GPT-Image-2 kit (`style-control-probe/outputs/2026-05-24/kit-gpt/panel-01..09.png`) had the strongest 9-panel consistency. Its tradeoff is surface grit/noise, not story or asset continuity.
- **NB-Pro candidate state:** the NB-Pro kit had cleaner surface but the scene bible still flags multiple candidate-panel problems in that route (notably 1, 3, 4, 5, 8, 9). Treat those as NB-Pro-route diagnostics, not as a mandate to keep grinding NB-Pro.
- **Next concrete action:** review the GPT kit against the scene bible and decide whether to accept/fix its surface or deliberately re-enter NB-Pro for targeted panel repairs with locked refs. Do not assume the model-sheet repair branch is the active default.
- Canonical automaton design (Gemini read of the working GPT board): **cylindrical skullcap + horizontal forehead seam, Greco-Roman mask face with hollow almond eyes, brushed gold, ball-socket shoulders** — recorded in `story/hephaestus-forge/BIBLE.md`. (My eye mislabeled this twice; trust the file + the original frame.)
