# Production-System Findings

Distilled from `deep-research/2026-05-19/reply02.md` — the *production-system / procurement* research pass. Where reply01 verified model capabilities (specs, grammar, the compositional-skeleton open question), reply02 argues for the **workspace layer above the image engine** and supplies the economics, handoff requirements, and QA framework that pass missed.

Scope note: reply02 does **not** revisit reply01's startup landscape (LTX, Drawstory, MITO, Firefly Boards, Higgsfield, Runway), and says nothing about camera-angle / compositional-skeleton transfer — still the biggest unresolved empirical risk. This doc captures only what reply02 adds.

---

## 1. The two-layer stack

An "AI storyboard system" is two things, not one:

- **Layer 1 — production workspace:** board structure, review, timing, editorial interchange, downstream handoff. The *system of record*.
- **Layer 2 — image engine:** panel generation, edits, style/character exploration. A *tool the workspace calls*.

Evidence: Toon Boom positions Storyboard Pro as end-to-end preproduction (thumbnails → boards → animatics → handoff); OpenAI/Google/Midjourney position their products as image generation/editing, **not** storyboard management. reply02's framing: the system should look like a **preproduction control plane with image-generation tools attached**, not a prompt-only image sandbox.

**Implication for this project:** the image model is a commodity input; the workspace (bibles, state ledger, prompt lineage, review gates, handoff) is the moat. This validates the brief's architecture as the load-bearing, defensible layer.

---

## 2. Handoff-format requirements

reply02 uses Toon Boom Storyboard Pro as the benchmark for what a mature workspace's handoff surface looks like. A serious system has to **separate creative-review formats from editorial-interchange formats** — they are different artifact classes.

| Handoff goal | Artifact | What it's for |
|---|---|---|
| Creative review | PDF storyboard packet | writer / director / agency / client review |
| Pacing approval | movie / MP4 animatic + temp audio | approve rhythm *before* shoot / editorial commitment |
| Editorial interchange | **EDL / AAF / XML** | land animatics/boards in NLE timelines |
| Animation downstream | **Harmony scenes, layout images** | boards become structured scene packages |
| Remote review / history | shared links, comments, version control | shortens review cycles, preserves approval history |

Best-practice rules reply02 draws out (anchored in DGA director-development guidance — boards useful *early*, *shared widely*, *frame-specific*; real preproduction also uses shot guides, script notes, floor plans, trackers, checklists):

- keep **script + shot intent** as a first-class object
- use AI panels at **thumbnail / alternate / revision** stages, not as the sole system of record
- maintain a **timed animatic** before production commitment
- **separate creative-review formats from editorial-interchange formats**
- preserve a **versioned audit trail** of changes and sign-offs

**Decision fork:** EDL/AAF/XML/Harmony export is a hard requirement for studio animation pipelines that *no image model provides*. If the target user is a studio, either integrate with Storyboard Pro or rebuild editorial interchange. Boords (cloud-first) exports PDF / MP4 / images / shot lists with strong collaboration, but **no AAF/XML or animation-scene export** — so it does not cover the studio-pipeline case.

---

## 3. Production economics

The missing labor anchor reply01 lacked:

- **Animation Guild: 10–20 minutes per TV storyboard panel**, before revision, timing, or dialogue-track work.

Per-scenario model assuming **4 generated candidates per approved panel** (output cost only — excludes prompt tokens, seats, human review):

| Scenario | Panels | Manual baseline | GPT Image 2 low | GPT Image 2 medium | Gemini 2.5 Flash | Gemini 3 Pro 1K/2K |
|---|--:|--:|--:|--:|--:|--:|
| Pitch board | 60 | 10–20 artist-hrs | $1.44 | $12.72 | $9.36 | $32.16 |
| Episode board | 300 | 50–100 artist-hrs | $7.20 | $63.60 | $46.80 | $160.80 |
| Feature block | 800 | 133–267 artist-hrs | $19.20 | $169.60 | $124.80 | $428.80 |

Per-image reference points (official sources): GPT Image 2 ≈ $0.006 low / $0.053 medium per 1024² · Gemini 2.5 Flash ≈ $0.039 · Gemini 3 Pro ≈ $0.134 (1K/2K) / $0.24 (4K). Midjourney is subscription + GPU-time ($10–$120/mo), not a clean per-image production API.

**Takeaway:** even expensive image-model usage is cheaper than a modest amount of human revision time. ROI is *not* driven by inference fees — it's driven by whether the system reduces **roughing, alternate exploration, asset search, and revision churn.** (This conclusion matches reply01's independent estimate from a different methodology — treat it as settled.)

ROI is strongest in: pitch/concept boards, look-dev / tone-locking, continuity-preserving *localized* edits (vs. full redraws), and client/director sign-off cycles. Staffing effect is **role shift, not deletion** — reduced: rough thumbnails, alternate exploration, ref hunting, pitch assembly; durable: writer/director alignment, board-lead judgment, continuity supervision, animatic editorial, pipeline/export QA.

---

## 4. Operational QA framework

reply02 proposes an instrument for continuity (explicitly "a proposed operational framework, not an industry standard"). These double as gate criteria for Phase 0/1 validation.

| Metric | Threshold | Why |
|---|---|---|
| Identity pass rate (hero chars) | **95%+** | below this, director/editorial time goes to redraws |
| Wardrobe & prop continuity | **98%+** | mid-sequence slips cause expensive downstream confusion |
| Shot-intent fidelity (angle / staging / type) | **95%+** | missing shot language = not production-safe |
| Text / annotation accuracy | **99%** (100% after human proof) | models strong here but not perfect |
| Revision churn (panels reopened post-sign-off) | **under 10%** | high churn = weak prompt locking / weak gates |
| Editorial handoff integrity | **100%** | broken handoffs erase any generation-speed gain |

**Automated checks:** metadata linting (aspect ratio, scene ID, panel order, character ID, prompt-template version) · reference-set validation (every hero panel points to a current approved packet) · text/label checks · **panel-diff alerts on identity-critical attributes when an approved character drifts.**

**Human review:** board lead (visual continuity) · director (shot intent / storytelling) · editorial (timing / transition logic) · **pre-handoff review of export packages, not just images.**

Key principle: **continuity cannot be measured by image similarity alone** — it includes story state, performance intent, staging, and handoff integrity. This is the argument for why a naive embedding-similarity checker is insufficient and the state ledger is required.

Supporting method — **canonical packet + controlled edits:** build a character packet first (front, profile, expression sheet, wardrobe anchors, hero props, color notes); enforce a reference role hierarchy (canonical character → location → costume → pose); prefer editing approved panels over fresh generations when continuity matters; keep a per-scene **continuity ledger** (emotional state, costume state, prop state, damage state, staging side).

---

## 5. Smaller new facts

- **Midjourney V8.1** — released 2026-04-30, "fastest model so far," native 2K HD, ~4–5× faster standard jobs; still routes some editing through **V6.1-era tooling**; Omni Reference remains V7-only / one-image with incompatible edit modes. Warner Bros. suit (Sept 2025) **consolidated** with the Disney/Universal litigation.
- **Data-use posture (procurement-relevant)** — OpenAI: business/API data not used for training by default, customer owns output. Google: **paid tier excluded** from product-improvement; **unpaid services may be used to improve products and may be human-reviewed.** Midjourney: users own outputs but ToS forbids automation/reverse-engineering, provided "as is."
- **Boords pricing** — Free / Pro $75 / Team $125 / Agency $250.
- **Leaderboard (Arena, 2026-05-12)** — gpt-image-2 medium 1393±7 · `gemini-3.1-flash-image` 1268±5 · `gemini-3-pro-image-preview-2k` 1242±4. Note: the *Pro* model scores *below* the *Flash* model on the arena — quality-first ≠ leaderboard-first.
