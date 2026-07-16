# Creative Engine — Skill Design (v0.2, metabolized)

Status: APPROVED DIRECTION, pre-implementation. v0.1 was scrutinized by Codex (7 changes);
this version integrates the accepted changes with guards noted. Sources: 5 research reports
(`research/01–05`), Mueller/DAYDREAMER condensation (latent-dreamer), creativity-skills
(ComfyPromptByAPI), Codex review. Codex's 3 research reports still pending export —
cross-fleet comparison by MECHANISM, not shared terminology.

## The one-line theory

LLMs sample the modal idea; every tradition surveyed converges on the same counter-spec:

> **Authored possibility space × external chance × temporary obedience × delayed selection.**

Mueller supplies the control loop around the operators — when to perturb, what to perturb,
whether the weird thing earned the right to *remain available* (not: proved it's best).

## V0 design commitments (evidence-graded, deliberately falsifiable)

Grades: [A] peer-reviewed/replicated · [B] preprint/strong practitioner convergence ·
[C] case-study reconstruction/anecdote. Each commitment is testable; the engine is allowed
to discover that a research-backed mechanism is unhelpful here.

1. **External entropy only** [A + universal practitioner convergence — treat as fixed].
   All randomness from `scripts/` — stimulus draws AND, when DIAGNOSE doesn't clearly
   indicate one, operator selection itself. The model never picks its own random stimulus.
2. **Binding obedience** [B/C — Eno/Cage doctrine + alignment logic]. A drawn stimulus is
   obeyed for a full seed before evaluation; non-binding randomness gets re-filtered by taste.
3. **Phase wall = zero comparative judgment** [A for deferred judgment; reworded per review].
   During divergence, PRESERVE: active concern, a tiny non-negotiables list (talent anchors,
   product present), operator obedience, lineage. PROHIBIT: ranking, polishing, feasibility
   criticism, brief-fitness optimization. (Divergence is concern-ful, judgment-free.)
4. **Three-state ban-list** [A for denial prompting; states added to protect platforms].
   round-banned (no immediate repetition) / exhausted (done this session) /
   protected-platform (generative mechanism, depth encouraged). Platform status is EARNED
   only by passing the platform test — 3+ distinct one-line executions on demand — never
   self-declared. Clichés legal as raw material, banned as final answers.
5. **Quotas apply to seeds, not treatments** [A for serial-order/fluency]. Funnel:
   30–40 terse seeds → 10–15 bridge-admissible concepts → 6–8 formatted treatments →
   3–5 render tests → 2–3 presentation directions. Many small batches, mine the tails.
6. **Archive by niche, never hill-climb** [B — QDAIF/MAP-Elites]. Bin on explicit axes;
   seed next batch from sparse cells. Depth-within-niche (platforms) and coverage-across-
   niches are both tracked; the archive says which a cell needs.
7. **Ship the metric** [A for pool-level collapse being invisible]. v0 = mechanism-class
   count + niche occupancy + dedup survival + marginal uniqueness per batch (stop condition:
   curve flattens → switch frames). Falls out of ban-list machinery. Classify Track A and
   Track B pools together, blind. Embedding distance deferred — likely confuses linguistic
   difference with visual-mechanism difference.

## The session loop (v0)

```
0. REFRAME    generate: 1 anchored reading of the client brief + 2 plausible reframes +
              1 deliberately uncomfortable reframe. Small seed batch under EACH before
              any human selection (delayed, not deleted). Reframes alter problem
              representation; contractual constraints survive verbatim.
              [Case studies support reframing as a powerful recurring move — not a law.]
1. ACTIVATE   state the concern: script function, emotional fantasy, product behavior,
              scale slot, styleframe constraint. (Peelerz: from coverage schema + treatment.)
2. RETRIEVE   coincidence retrieval over the fragment store — surface material because
              multiple independent cues converge, NOT nearest-semantic-match.
              2–3 hop bounded cascade from anything surprising.
3. DISPLACE   draw operator (routed by DIAGNOSE, else drawn by script) + stimulus from
              scripts. Binding for the full seed.
4. COMMIT     one unusual thing only (UCB game). "If this is true, what else is true?"
              Heighten on a ladder — each rung conceptually new, never just bigger.
5. BRIDGE     mandatory reconnection: movement operators / bisociation ripeness / Mueller
              serendipity-verification. Why is the product responsible? What single rule
              governs it? A failed bridge sends the seed to the nursery unbridged, flagged.
6. FORMAT     (only for funnel survivors) RULE (≤1 sentence) / FRAME / LADDER (3 escalations)
              / DELTA (the one change from documentary reality).
7. ARCHIVE    Gate 0 admission → nursery. Update ban-list states + metrics. Fresh entropy,
              go to 2 (or 0 if DIAGNOSE says the frame is exhausted).
```

**FRAME is model-neutral but concretely depictable**: one stageable tableau with mandatory
fields — subject, action, spatial relation, governing impossibility, emotional read,
composition. Never conceptual prose (the field list IS the legibility discipline).
Model-specific prompts are produced by **RENDER ADAPTERS** only at Gate 3 (MJ / NB2 / new
models), so current prompt conventions can't shape ideation.

**DIAGNOSE** (from creativity-skills) routes failures → operators: blank→random-entry;
repeating→ban-list+new deck; too coherent→harder displacement; arbitrarily weird→bridge
work; generic→cliché blacklist check; product-disconnected→product-physics pile.

**Control postures** (adapted DAYDREAMER goal types — routed by session state, NEVER drawn
randomly; controller stance ≠ mutation operator):
- ROVING: associative exploration (cascade without a pressing concern)
- REVERSAL: negate/undo a premise; also Gate-1 stress posture ("imagine it failing")
- REPERCUSSIONS: follow consequences outward
- REHEARSAL: simulate the concept through shots/transitions
- RECOVERY: repair a failed-but-fertile candidate (dead-idea harvesting)

**Human injection points** (from creativity-skills, semantics per review):
- SEED: human-authored fragment enters normal retrieval with privileged initial activation.
- WILD: bypasses retrieval entirely but still requires lineage and a later bridge.
- Neither receives any automatic fitness bonus. Human taste votes at DIAGNOSE pauses and
  at funnel selection points — delayed, never mid-divergence.

## V0 operator set (8 core — a large router is itself a taste surface)

Reframe · Random entry · Oblique interruption · Synectic analogy · Morphological collision ·
Explicit mutation (Mueller: permute / generalize / retype, with provenance) · Constraint
transformation (Oulipo/Dogme vow sets) · Consequence heightening.

The remaining ~51 researched operators live in `references/operators-annex.md`, promotable
only when session traces reveal a pathology the core 8 can't address. Exquisite-corpse /
Secret Cards is a HARNESS pattern (parallel subagents, isolated contexts, different hidden
stimuli), not an operator.

## Staged gates

- **Gate 0 — admissibility (in-session, cheap):** relates to a concern? rule statable?
  differs from parent + round-ban list? → nursery.
- **Gate 1 — development (end of session):** elaboration yields consequences? FRAME +
  transition exist? sparse niche? emotional fantasy present? REVERSAL stress-pass. → portfolio.
- **Gate 2 — brief fitness (separate context, comparative judging):** 1-second legibility
  (poster test), product causality, youth-coded not infantile, correct escalation slot,
  appetite appeal, platform test.
- **Gate 3 — RENDER (empirical, per-model):** RENDER ADAPTER per model; generate; verdicts
  tagged per-model, never absolute. "Honour thy error": artifacts get one pass as hidden
  intentions (seed, not reject). generation-review-loop is the harness. Adapters are not a
  hospice: repeated cross-model failure kills the treatment slot (the idea stays archived).

Nursery/portfolio never deleted mid-session; lineage (parent, operator, stimulus,
what-changed) immutable.

## Fragment store (the representation problem — biggest open risk)

- 40–100 compact fragments from EXTERNAL material only: script beats, product physics,
  research-file examples, MJ mood board, reference films. Never free-generated by the
  retrieving model.
- Multi-indexed with a FIXED controlled vocabulary across orthogonal families (physical
  operation / material behavior / spatial relation / emotional fantasy / social
  configuration / temporal behavior / formal medium / transition affordance / product fact /
  productive contradiction).
- Tagging pass runs WITHOUT the brief in context.
- Threshold retrieval + serendipity = threshold−1 (Mueller). **UNTESTED RISK:** small stores
  may degenerate (threshold 2 matches everything, 3 matches nothing) — tune empirically
  before trusting; this is the first thing `fragments.py` should let us probe.
- Substrate stays usage-unbiased forever. Retrieval queue may use recency/concern-strength;
  portfolio may record preference; neither ever rewrites fragment indices.

## Skill layout (canonical home: THIS repo, `.claude/skills/creative-engine/`)

Not installed globally until it survives Peelerz + two unrelated forward tests; then thin
per-harness adapters pointing at one canonical source.

```
creative-engine/
├── SKILL.md                    # loop + gates + routing ONLY (~150 lines)
├── scripts/
│   ├── entropy.py              # all randomness: decks, wordlists, N+7, Zwicky, operator draw
│   ├── fragments.py            # store build/tag/threshold-retrieve/cascade (+ threshold probe)
│   └── session.py              # archive, 3-state ban-list, lineage, metrics
└── references/
    ├── operators-core.md       # the 8, with full protocols
    ├── operators-annex.md      # the researched long tail (promotable)
    ├── postures.md             # 5 control postures + routing conditions
    ├── decks/                  # oblique cards, irrational-enlargement Qs, TRIZ, wordlists,
    │                           #   candy-cliché blacklist (+ repair operators)
    ├── verification.md         # gates 0–3 rubrics, two-dial scoring, poster/platform tests
    └── fragment-schema.md      # index families + blind-tagging protocol
```

## Peelerz v0 scoping — two tracks (deliverable never hostage to the engine)

- **Track A (direct):** disciplined manual ideation on the 3 open sandboxes using the
  operator references by hand. Guarantees Ben gets boards.
- **Track B (engine):** fragment store + scripts + full loop on the same sandboxes.
- Same portfolio; blind comparative judging; metrics on both; Gate 3 renders survivors
  of either track.

## Resolved / open

- RESOLVED: local skill home · SEED/WILD in (semantics above) · postures routed not drawn ·
  metric = Option A (class count, niche occupancy, dedup survival, marginal uniqueness).
- OPEN: Codex 3-report export → mechanism-level cross-fleet comparison.
- OPEN: coincidence-retrieval behavior at small store size (empirical probe first).
- FALSIFIABLE BY SESSION TRACES: 30-seed quota size · binding-obedience benefit ·
  ban-list increases range vs. thins pool · verbalized-probability sampling on this task.
