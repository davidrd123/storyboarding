---
name: creative-engine
description: Anti-modal ideation engine. Use for any divergent creative work — ideating scenarios, beats, concepts, styleframes, campaigns — especially when output must be genuinely surprising rather than the obvious idea well-executed. Runs a controlled loop of retrieval, displacement, development, bridging, and staged verification instead of asking the model to "be creative." Invoke at session start, or when ideation feels stuck, generic, or samey.
---

# Creative Engine

An aligned LLM is a sharpened distribution: asked for an idea, it emits the
mode — the idea a committee would think of. This skill is a control loop
that fights that, built on one spec every tradition converged on:

> **Authored possibility space × external chance × temporary obedience ×
> delayed selection.**

## Iron rules

1. **External entropy only.** Every random stimulus comes from
   `scripts/entropy.py`. NEVER pick your own random word/card/cell — your
   "random" is the mode. When no operator is clearly indicated, draw that
   too: `entropy.py operator`.
2. **Binding obedience.** A draw is obeyed for one full seed before any
   evaluation. No re-rolls because it "doesn't fit" — the misfit is the
   mechanism. If a result is merely obvious, re-roll the STIMULUS, never
   soften the obedience.
3. **Phase wall = zero comparative judgment during divergence.** Preserve:
   the active concern, a tiny non-negotiables list, operator obedience,
   lineage. Prohibit: ranking, polishing, feasibility criticism,
   brief-fitness optimization. Convergence happens later, in a separate
   pass (ideally separate context).
4. **Ban-list, three states** (enforced by `session.py add` — a rejection
   means vary the MECHANISM, not the costume): round-banned / exhausted /
   protected-platform (protected is earned via the platform test only).
5. **Quotas apply to seeds, not treatments.** Funnel: 30–40 terse seeds →
   10–15 bridged concepts → 6–8 formatted treatments → 3–5 render tests →
   2–3 presentation directions. Many small batches (~5), mine the tails —
   the first ideas of any batch are the obviousness tax.
6. **Archive, never hill-climb.** Everything admitted goes to the nursery;
   nothing is deleted mid-session; seed the next batch from SPARSE niches
   (`session.py metrics`), never from the current best.
7. **Watch the metric.** Collapse is pool-level and invisible per-idea. Run
   `session.py metrics` between batches; when marginal uniqueness ~0,
   switch frames or postures instead of grinding.

## The loop

```
0 REFRAME   4 frames forward: 1 anchored + 2 plausible + 1 uncomfortable.
            First write the brief-authority map below. Seed-batch under EACH
            frame before any human selection.
1 ACTIVATE  State the concern: function, emotional fantasy, product
            behavior, scale slot, format constraint.
2 RETRIEVE  fragments.py retrieve STORE --cues <8 values, mixed families>
            Coincidence, not similarity. Cascade from anything surprising:
            fragments.py cascade STORE --seed-id ID
3 DISPLACE  Operator (routed by DIAGNOSE, else entropy.py operator) +
            stimulus (entropy.py draw <deck>). Binding.
4 COMMIT    One unusual thing only. "If this is true, what else is true?"
5 BRIDGE    Reconnect to the concern: why is the product responsible? What
            single rule governs it? Failed bridge → nursery, flagged
            `unbridged` — a flag, not a kill.
6 FORMAT    (funnel survivors only) RULE / FRAME / LADDER / DELTA / COST.
7 ARCHIVE   session.py add ... → Gate 0 → nursery. New entropy → step 2;
            frame exhausted → step 0.
```

## Brief-authority map

Before reframing, separate five kinds of input. Do not allow a vivid existing
execution to acquire contractual authority merely because it has been rendered
or repeated often.

```
FIXED:        contractual facts explicitly named as set
OPEN:         areas explicitly invited for invention
PROVISIONAL:  existing treatments, examples, and starting trunks
INTERPRETED:  later assumptions added by collaborators or prior agents
ROUND-BANNED: dominant mechanisms temporarily excluded to reopen the space
```

Every frame states which `FIXED` items survive. `PROVISIONAL` material competes
as one trunk; it is never the invisible destination of all four frames. When
the human says the work is staying too close to their ideas, route back to this
map before drawing harder entropy—the problem is usually inherited authority,
not insufficient strangeness.

Session bookkeeping: `session.py init/add/ban/new-batch/mark-dup/metrics`.
Store setup: build per [references/fragment-schema.md](references/fragment-schema.md),
then `fragments.py validate` and `fragments.py probe --store` (pick the
threshold where median retrieval is 2–6).

## DIAGNOSE — routing failures to operators

| Symptom | Move |
|---|---|
| blank page | random-entry |
| repeating myself | ban-list check + new deck / new-batch |
| too coherent, too smooth | harder displacement (oblique, constraint) |
| arbitrarily weird, unmotivated | BRIDGE work (movement operators) |
| generic / category-shaped | cliché check (decks/cliche-blacklist.md) + reframe |
| product-disconnected | product-fact cues + explicit-mutation on a product action |
| good seed, stalled | explicit-mutation, then consequence-heightening |
| concept unseen, all words | REHEARSAL posture, then FRAME it |
| everything feels inevitable | REVERSAL posture |
| dead seeds with live parts | RECOVERY posture (dead-idea inventory) |

Operator protocols: [references/operators-core.md](references/operators-core.md)
(8 core; annex promotable only on demonstrated pathology). Controller
stances: [references/postures.md](references/postures.md) — routed by state,
never drawn.

## Human injection (SEED / WILD)

The human is an entropy source the model can't simulate and the taste that
decides what becomes work. SEED: human fragment joins the store with
privileged activation. WILD: bypasses retrieval, still gets lineage + a
bridge. Neither gets a fitness bonus. Human selection votes at DIAGNOSE
pauses and funnel points — delayed, never mid-divergence.

## Gates (full rubrics: [references/verification.md](references/verification.md))

- **Gate 0** admissibility → nursery (cheap, in-session; cliché tag+repair)
- **Gate 1** developmental potential → portfolio (end of session)
- **Gate 2** brief fitness (separate context, comparative; poster test,
  product causality, two dials, cost, platform test)
- **Gate 3** RENDER — empirical, per-model, via render adapters; honour thy
  error (one pass treating artifacts as intentions); verdicts tagged
  per-model, never absolute

A strange candidate only needs to earn continued availability during
divergence — not prove it's best. Only Gates 2–3 pick what's presented.

## Parallel patterns (expensive modes)

- **Secret Cards:** N subagents, same brief, each dealt a DIFFERENT hidden
  card (`entropy.py draw oblique -n N`, one per agent). Harvest seeds, not
  winners.
- **Exquisite corpse:** sequential subagents, each seeing only the previous
  segment's last line. The fold is context isolation — one context cannot
  play it.
- **Maker/Obstructor:** obstructor reads the maker's output, bans its most
  habitual quality by name, maker regenerates. Keep all versions. Never
  issue "total freedom."

## Focused visual-probe mode

Use [references/focused-visual-probe.md](references/focused-visual-probe.md)
when a project already has useful trunks, diagnosed visual gaps, and reference
images, but its exploration has collapsed into small mutations of those refs.
This mode keeps the engine's entropy and delayed judgment while binding every
seed to a gap, an explicit reference-inheritance contract, a distance ring,
and an eventual render test. Before rendering, its Gate 2.5 compiler strips
metaphor/source-domain attractors out of the image prompt and replaces them
with substrate, force, topology, state-change, and shot-proof instructions.
It is a focused harness, not a safer replacement for the main loop.

## When NOT to use this

Convergent work (the brief already names the idea; execution quality is the
job), or when one obvious-but-correct answer is wanted. The engine buys
divergence with time; don't pay for it when convergence is the deliverable.
