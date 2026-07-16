---
name: the-solvent-status
description: "Live dashboard for THE SOLVENT — current phase, the gen log (pointer to prompts/ detail), and next actions. The single place to learn 'what's the state and what's next' without reading chat history."
type: workflow
title: "The Solvent — Status"
tags: []
tier: production-tools
status: living_document
system_directive: "Update whenever a gen lands or a decision is made. This is the dashboard; the authoritative per-gen breadcrumb (prompt + output filename + verdict) lives in the prompts/ files — keep this pointing to them, don't duplicate the detail."
related:
  - "CLAUDE.md"
  - "CONCEPT.md"
  - "RECIPE.md"
  - "prompts/opening-sequence-filth.md"
  - "prompts/reference-stack.md"
---

# THE SOLVENT — Status

> Live state + next actions. The authoritative per-gen breadcrumb (prompt + output filename + verdict) lives in the `prompts/` files and the `outputs/**/README.md` logs; this is the dashboard over them.

## Phase
**Quick-pass spine COMPLETE — circling back to the top for deeper setup.** A full **15-page draft spine** now exists end-to-end (6 opening + 7 descent + 2 endings), generated on **NB2 via riff-mcp, Claude-driven** (see `CLAUDE.md` → "Claude is the driver"). It proves the **register-as-layers** visual system — gold self-image / duotone CCTV reality / signal-corruption + psychedelic-melt dissolution — and carries the whole resisted-ego-death (dukkha-ñāṇa) arc. NB2 held Vane/Witness identity well across separate gens and was fine on the dissolution register (the earlier "NB2 facture ceiling" worry did NOT hold).

**Engine:** NB2 is the working driver-engine; GPT-Image-2 (codex) is an *optional* finishing pass (crisp lettering / fine control-register facture).

**Two tracks to reconcile:** (1) the NB2 **quick-pass spine** [arc proven, no deep setup]; (2) the codex/GPT-Image-2 **reference stack** [Vane + Witness character sheets, Image-A layout locks]. The serious pass merges them.

## Gen log — codex / GPT-Image-2 reference-stack track (detail in `prompts/`)
| Item | Prompt | Output | Verdict |
|------|--------|--------|---------|
| TEST 1 — CLARION page (control / gold grid) | `prompts/opening-tests.md` | `outputs/opening-tests/2026-05-31-register-probes/test-1-page-1-clarion-register.png` | Strong gold monument; grid controlled but not perfectly equal-panel. |
| TEST 2 — solvent page (dissolution / white eating in) | `prompts/opening-tests.md` | `outputs/opening-tests/.../test-2-solvent-register.png` | Strong central white gutter; Witness reads as a different hand. |
| TEST 3 — the war page | `prompts/opening-tests.md` | `outputs/opening-tests/.../test-3-war-page.png` | Strong register split; captions survived. |
| STYLE 1 — Filth issue 02 reference probe | `prompts/style-tests.md` | `outputs/style-tests/2026-05-31-filth-refs/filth-ref-solvent-breach-test-1.png` | Toxic pop-sci-fi register; orange gutters + white rupture read. |
| REF 1 — Vane character sheet | `prompts/reference-stack.md` | `refs/characters/vane-sheet-v1.png` | Strong identity anchor; labels survived. |
| REF 2 — Witness character sheet | `prompts/reference-stack.md` | `refs/characters/witness-sheet-v2.png` | Preferred sheet; clean soft-line Witness. |
| REF 3 — Page 5 Image A | `prompts/reference-stack.md` | `refs/layout/page-05-gutter-breach-image-a-v1.png` | Strong flat layout lock. |

## Gen log — NB2 quick-pass spine (Claude-driven, 2026-05-31 → 06-02)
| Batch | Where | Verdict |
|------|--------|---------|
| Style probes (Filth register discovery) | `outputs/style-probes/README.md` | ★ Found the house language: CCTV/screen grammar (control = wall of monitored self-images; dissolution = signal-decay + the one dead channel). |
| Opening sequence (6pp) | `prompts/opening-sequence-filth.md`, `outputs/opening-sequence/` + `contact-sheet-2026-05-31.png` | ★ register grammar SEQUENCES across pages; P3 re-cut to suspense layout (P3b). |
| Descent (7pp, dukkha-ñāṇas) | `outputs/dukkha-nanas/` + `contact-sheet-dukkha-nanas-2026-06-01.png` | ★ full dark-night arc — one grammar, seven emotional registers; the Loop page = ouroboros form-as-content. |
| Endings (2) | `outputs/endings/` (A white / B re-gilded) | ★ savior/assassin fork drafted; choice open. |
| FULL SPINE contact sheet | `outputs/the-solvent-quick-pass-spine-2026-06-02.png` | 15pp (5×3) at a glance. |

## Next actions
- [x] Quick-pass full spine on NB2 — opening + descent + endings drafted (15pp).
- [x] Lane asserted: Claude drives gens (NB2); GPT-Image-2 optional finals (`CLAUDE.md` + memory updated).
- [x] `.gitignore` added (`outputs/`, `refs/the-filth/`) — scans/outputs stay local-only.
- [ ] **CIRCLE BACK TO THE TOP — deeper setup before the serious pass:**
  - [ ] **Character bible** beyond the archetype — Vane's pre-brand self (= the Witness): who he was, what he buried; the antagonists who control the dropper. *(Build on existing `refs/characters/` sheets.)*
  - [ ] **Plot / structure** — the thriller outer layer + act breaks; map the dukkha stages to scenes; the dissociative-alter mechanic beats.
  - [ ] Name the Witness (or commit to unnamed); pick the title.
  - [ ] Decide the ending (A / B / hold-both) — drafts now exist to choose from.
  - [ ] Reconcile tracks: fold codex's character sheets + Image-A locks into the NB2 spine for the serious pass.
- [ ] (carried) CLARION Image A flat-colorblock grid lock; whole-page vs panels-then-composite decision (`RECIPE.md`).

## Open creative questions
Tracked in `CONCEPT.md` → "Open questions": title, name-the-Witness-or-not, **which ending** (A / B / hold-both — *drafts now exist to choose from*), how literal the geopolitics outer layer.
