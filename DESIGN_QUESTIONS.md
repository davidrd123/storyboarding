# Design Questions

Conversation prep for walking the director through `STORYBOARD_SYSTEM_BRIEF.md`. Focused on **design** decisions only — strategic/business questions (artist recruitment, Track A/B timing, FairTrade operationalization) are deferred.

Filter applied: *if a different answer changes the architecture, lead with it; if it only changes a parameter, save it for later.*

---

## Five framework questions that matter most

Each can invalidate large parts of the brief if answered unexpectedly. Get these before anything else.

### 1. Does the panel skeleton match how you'd articulate a shot?

The brief proposes: `SHOT / SUBJECT / STATE / ACTION / SETTING / MOOD / COMPOSITION / CONTINUITY`. The interesting question is whether **STATE** as its own slot — distinct from identity and action — matches how you direct.

The argument: "what they're doing" (action) and "how they are in this moment" (state — held tension, eyeline, costume variation, attention focus) are different, and the second is where most emotional content lives.

**If you'd collapse those:** the bible's expression sheet and most of the prompt grammar get rethought.

### 2. Is "beat" the right unit of decomposition?

The brief treats a beat as the atomic unit — a beat may get zero, one, or several panels.

Alternatives:
- **Shots-first** — decompose into coverage geometry first, then assign beats to shots
- **Scene-first** — work at scene granularity and let panels emerge ad hoc

The choice determines what the state ledger looks like, what the UI scrolls through, and how the LLM structures your input.

### 3. Should the state ledger exist as a separate artifact at all?

The brief proposes that "what's true at any script position" is its own queryable object, independent of whether panels exist. That's an opinionated architectural call.

**Alternative:** keep state inside the panel itself — no upstream ledger.

**Trade-off:** separate ledger enables continuity checking and propagation when scripts change, but it's a real artifact to maintain. Do you actually want to maintain it, or is it overhead?

### 4. Direct manipulation vs. proposals-with-approval — primary mode?

This shapes the entire UI.

- **Direct:** you specify each DSL slot, system renders. Fast for high-confidence direction, heavy for hundreds of panels.
- **Proposals:** you give intent in prose, system fills DSL slots and shows you, you correct. Faster volume, less direct control.

The FairTrade context suggests direct (you've shown willingness to spec). But pitch volume might pull toward proposals. The actual answer might be "direct for first pass, proposals for variations" — worth confirming.

### 5. Recipe — is Midjourney actually wanted in the loop?

The brief proposes "Recipe 2 with Stage A prepended" — MJ for hero-image exploration, `gpt-image-2` for systematic build-out.

**Closed-only alternative** is cleaner commercially and operationally.

Do you actually want to spend exploration time in MJ, or would you rather start with `gpt-image-2` generating hero-image candidates with lookbook refs and skip the model switch? (Style is worse; pipeline is simpler.)

---

## DSL refinement

Lower-stakes detail, but worth a pass.

- **CAMERA MOVE slot** — does it earn its place for pitch storyboards, or is move-notation just artist's-note text? Pitch books usually don't animate.
- **COMPOSITION as its own slot** — useful, or does it collapse into MOOD/SETTING in practice?
- **Shot scale vocabulary** (ECU/CU/MCU/MS/MLS/FS/LS/WS/ELS) — is that the right cut? Do you actually use MLS vs FS as distinct, or is the practical vocabulary smaller?
- **Coverage role** (establishing/master/OTS A/OTS B/reaction/insert/cutaway) — does this match how you think coverage, or is it borrowed-from-feature-film and not quite right for pitch density?

---

## Bible refinement

- **~20–25 assets per principal** — does that match your intuition for testing, or does it feel high/low? (3× difference in build effort.)
- **Tier-2 expressions chosen for "western/adventure":** cold rage, tactical, defiant, pained-pushing-through, world-weary, suspicious. Do you have a different working emotional vocabulary you'd substitute or augment?
- **Profile-variant expressions for shot/reverse-shot work** — needed for the test project, or premature?
- **Vehicles** (added to the world bible after the Discord re-read) — does the test project actually have vehicles that matter, or hypothetical?
- **Costume/state variants** (bloodied, soaked, etc.) — generated up front per character, or derived per-panel as needed? Trade-off: pre-generated is more consistent; on-demand is less work for stuff you might not use.

---

## Workflow / interaction

- **What does "directing the system" feel like?** Typing? Voice? Bracketed annotations on a script? You drove FairTrade — what worked there?
- **Granularity per panel:** specifying every DSL slot, or saying "tight on him, low, slow creep" and letting the system fill the rest?
- **Iteration unit:** when something's wrong, do you typically re-roll the panel, edit the DSL, edit the prompt directly, or back out to the beat?
- **Across the script, how do you actually move?** Linear (Act 1 → 2 → 3)? Strongest-beats-first? Coverage clusters? Determines whether the UI should be script-spine, beat-grid, or scene-index.

---

## UI shape

- **Four nested loops** (script → scenes → beats → panels). Match your mental workflow? Or do you cross scales constantly (e.g., "I want this panel to echo Panel 3 from Scene 1.4 — I'm not thinking about Scene 4.2 right now")?
- **State always visible at cursor position** — useful, or visual noise once you've internalized the script?
- **3–4 candidates per panel slot** — right number? Some workflows want 1-and-reroll; some want 8.
- **Non-destructive history at every level** — every rejected candidate preserved, every state edit preserved. Necessary, or is "only the current selection matters" closer to your real workflow?
- **Continuity checker** — would automated flags ("this panel's wound state doesn't match Beat 2.4") earn their cost, or would they be noise?

---

## Empirical (not opinion — these need generations to answer)

These are open questions the **brief can't resolve** but worth naming so you know what's deferred to testing:

- Does **compositional skeleton transfer** (camera-angle-as-pose-transfer) actually work, or does it leak subject/composition?
- **Identity preservation across 60 panels** — what's the real drift rate when the bible reference holds constant?
- **Style leakage from references** — how much explicit do-not-borrow fencing is needed in practice?
- **Re-roll rate at production volume** — the 20–30% prior is borrowed; needs measurement. Raw API cost is probably small compared with human review time, so measure both re-roll count and review cadence.
- **Bible synthesis** — can the model hold style + identity + variation simultaneously well enough that the expression sheet for a single principal renders cleanly? *(This is the diagnostic for whether Track A's pipeline works at all.)*

---

## How to use this in conversation

- **Lead with the five framework questions.** Disagreement here changes the architecture; agreement validates the brief's foundation.
- **DSL/bible/UI refinement questions are mid-priority** — they tune the brief but don't restructure it. Save these for after framework questions are settled.
- **The empirical questions aren't really questions for the director** — they're a list of what can't be answered in a meeting and need to be validated by running the first generations. Worth surfacing so the conversation doesn't get stuck trying to argue them.
