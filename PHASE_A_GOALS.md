# Phase A Goals — Controllability Lab

What David's lab work needs to surface so that Phase B (Ben's directorial tool, described in `STORYBOARD_SYSTEM_BRIEF.md`) can be designed on top of *working* primitives rather than assumed ones. Each item below is a **mechanism to probe** — not a deliverable, but a real question the lab needs to answer through hands-on tests.

**Phase A method:** Patrick's discipline. Hands-on, struggle-tolerant, lessons-into-markdowns. The vault is the deliverable; working artifacts (a class storyboard, validated reference grammar) are the side effects.

**Test beds:** Not a single test project. Several:

- David's compositing class project (real downstream consumer, supplies a brief)
- `phase-0/` Damaggio work (existing controllability validation — see `phase-0/FINDINGS.md` for results: four clean passes, expression-sheet load-bearing confirmed via T03, compositional-skeleton-transfer ambiguous via T06)
- Bespoke micro-scenarios designed to maximally exercise one joint — see `TEST_BEDS.md` for the current set (8 beds covering all five probes below)

A full script is not required. Bespoke 3–4 scene scenarios that isolate one joint at a time are usually more diagnostic than real scenes that test five things at once.

---

## Five mechanisms to probe

### 1. Where the recalibration touchpoints have to be

Creative-person-in-loop is structural, not preference (see `MEETING_BREAKDOWN.md` §13). The question is *where* in the pipeline a human "yes/no/correct" has to land to catch drift before it compounds. Probes:

- At what step does style drift first become visible? Detectable by a check, or only by eye?
- At what step does character identity drift first become visible?
- At what step does location continuity break?
- What's the cheapest place to insert a human touchpoint without breaking flow?

Output: a map of touchpoints + their detection signals.

### 2. What state needs to be tracked between touchpoints

Touchpoints only work if there's state to recalibrate *against*. Candidate state:

- Character costume / wound / mood deltas (panel-to-panel)
- Location identity (including sub-locations discovered during making — see §5)
- Style anchor (per-project; per-scene if it shifts)
- Ingredient assembly history per frame (which refs were attached — needed to debug "why does this look wrong")
- Bubble-up edits (when a result reveals an upstream-state revision is needed — see §4)

Form: probably markdown with structured frontmatter, coding-agent-readable. Exact schema is itself a discovery.

### 3. What refs can disambiguate prose at each touchpoint

Words are underspecified. Image refs may close the gap. Probe: for each DSL slot the model handles weakly with prose alone, does adding a labeled reference disambiguate? Specifically:

- Shot scale / camera angle / coverage (the "Spielberg close-up" experiment from `MEETING_BREAKDOWN.md` §4)
- Sub-location identity ("same hallway, different end")
- Specific character state (cold-rage expression ref vs. prose description)
- Style fidelity (one ref vs. multiple; composite vs. atomized)
- Composite vs. atomized character control: same character, four ref formats (multi-angle composite sheet, tight headshot, turnaround crops, expression crops), then 8–12 panels measuring identity / expression / leakage.

This is the Phase A side of the artifact that becomes Phase B's director-curated shot-type package.

### 4. What the "orders" assembly + bubble-up loop looks like in practice

Per-frame ingredient assembly is the Phase B workflow primitive (`MEETING_BREAKDOWN.md` §7). Probes:

- What's the right form for the per-frame assembly log? Markdown per panel? Per scene? One file per session?
- When a result reveals an upstream constraint ("trench coat must be transparent"), how does the change propagate back — to the state ledger, to the bible's ref images?
- What gets locked vs. stays mutable? Bible refs typically locked; per-panel ingredients typically mutable.
- How does a coding agent read and update this log without losing human-curated context?
- How does the assembly scale past model reference caps? Probe canonical asset refs + File API / `file_uri` handles + a sliding window of recent panels, rather than dragging every prior image through the prompt history.

Look at Patrick's pattern as a starting point. Extend as needed. Intersects with §2 (state schema) and §5 (consistency rubrics).

**Iteration mode: intra-panel vs. across-panel.** Two distinct generation modes with opposite strengths; the iterate loop has to pick the right one per situation.

- **Intra-panel refinement → multi-turn chat.** When a panel is *almost* right ("trench coat darker," "push in tighter"), stay in a conversational thread: Gemini 3 Pro Image conditions on its own prior output via Thought Signatures, and implicit caching makes the resent stable prefix cheap (~90% token discount). The model builds on the last render instead of regenerating from scratch — good for small, coherent tweaks. *Note: continuity here comes from the resent transcript + thought signature, not from the cache; the KV cache is purely a cost/latency layer and produces identical output.*
- **Across-panel generation → fresh stateless call anchored on the bible.** Each new panel starts clean from canonical bible refs + the borrow/do-not-borrow fences — *not* from the prior panel's conversation history. Letting panel N carry panels 1…N-1 in history accumulates drift and hits the 14-ref cap. Empirical basis: naive chat-based storyboarding degraded rapidly across panels in the Weavy/Nano Banana test (`deep-research/2026-05-19/reply01.md` [18]), while a structured per-panel workflow held 80–90%. This is the concrete reason behind the sliding-window bullet above.

**Known quirk — refinement can rut.** Multi-turn refinement sometimes gets stuck returning essentially the same image no matter how the instruction is reworded; the escape hatch is to abandon the thread and start a fresh generation from the bible refs. The iterate loop therefore needs an explicit "bail to fresh generation" affordance, not just a "keep refining" path — and a touchpoint signal (§1) for *when* a refinement thread has stopped making progress.

### 5. How sub-location discovery + consistency-checking gets registered

`MEETING_BREAKDOWN.md` §8: storyboarding reveals world state ("we moved far enough down the hallway — this is a new location now"). Probes:

- What surfaces the "wait, this is a new location" realization — eyeball, model output, vision-LM check?
- How does the new sub-location get registered without breaking existing references?
- Is a background consistency-rubric layer feasible? Vision-LM + Patrick's rubric pattern is the obvious starting point.
- What's the false-positive rate at which a consistency checker becomes noise rather than signal?

Research prior art supports this direction rather than settling it: CANVAS frames long-form visual storytelling as explicit continuity planning, StoryBlender uses a continuity memory graph / canonical asset materialization pattern, and DreamShot uses multi-reference role conditioning for storyboard identity alignment. Treat those as vocabulary and design pressure, not answers.

---

## Deferred (worth naming, not yet a probe)

- **Markdown organization for orders ∩ DSL ∩ log-of-tried.** The exact intersection of: the DSL's ingredient slots, the per-frame assembly log, and the agent-readable lessons accumulated session-to-session. Will probably crystallize once §4 and §2 have run a few rounds. Likely modeled on Patrick's vault.
- **Captioning schema for `phase-0/refs/`.** Captioning Damaggio reference images with film terms + emotional states is a real Phase A task (and prep for Track B training) but doesn't block the five probes above.
- **Tone preamble (Loop 0) for David's own work.** Ben's instinct is that tone/comps/genre seed before script breakdown. David doesn't have a director's intuition here yet — discovering his own equivalent is part of the lab work, interactive, not a spec to implement.
- **Scene boundary detection.** `MEETING_BREAKDOWN.md` open questions raised "what's a scene exactly?" as gating for the Phase B establishing-shots MVP. Not a Phase A probe: David's bespoke micro-scenarios in `TEST_BEDS.md` are 1–4 panels long and don't need scene breakdown; for downstream test projects (compositing class) David supplies the scenes himself; for Ben's projects, Ben supplies the breakdown (he already has his own system). Phase A may *opportunistically* surface lessons here, but the probe doesn't belong in the lab work itself.
- **Competitive teardown.** Boords, LTX Studio, Adobe Firefly Boards, Drawstory, MITO, and Higgsfield need hands-on product comparison before Phase B UI commitments. This is product research, not a controllability primitive, so it sits beside Phase A rather than inside the five probes.

---

## What this isn't

- A phase plan with milestones. The lab is exploratory; lessons emerge.
- A spec for Ben's tool. That's Phase B (`STORYBOARD_SYSTEM_BRIEF.md`).
- Comprehensive. New mechanisms will surface as the work proceeds — this file gets updated, not appended-only.

---

## Open expectations

- **Ben's review of `STORYBOARD_SYSTEM_BRIEF.md`** (in flight, reviewing with Claude on his side) may return directional changes. Phase A probes don't block on his return; bias toward running the cheap ones now and integrating his feedback when it arrives.
- **Phase A → Phase B handoff artifact** isn't decided yet. When Ben re-engages, what does he see — raw lessons vault? A revised brief? A working class-project demo? All three? Worth deciding before the lab work generates too much that doesn't have a destination.
