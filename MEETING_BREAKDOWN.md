# Meeting Breakdown — 2026-05-19

Source: raw notes in `Talk.md`. This is the structured digest, ordered by what changes the architecture in `STORYBOARD_SYSTEM_BRIEF.md`.

> **Post-discussion update:** the work splits into **Phase A** (David's controllability lab, now) and **Phase B** (Ben's directorial tool, later). Most of this doc describes Phase B; Phase A goals live in `PHASE_A_GOALS.md`. Patrick's lessons-in-markdowns discipline is the substrate for both, not a phase to leave behind. Several items below have been reframed — search "[reframed]" to find them.

---

## TL;DR

The brief got the architecture right. Ben confirmed director-as-primary-user, validated the state-ledger / bible / vault-as-memory pattern, and added several things the brief didn't have. **But the MVP target has moved.** Ben's "bare minimum" is **the establishing shot of every scene** — locations first, panels later. That's a smaller, sharper Phase 1 than the brief proposed.

The business is also concrete now: **first-pass storyboards for film companies at ~$200/board.** Research update: raw API cost is probably not the binding constraint; human art-direction time and iteration throughput are.

---

## Validated by Ben (the brief got these right)

These are things in the brief Ben endorsed without modification:

- **Director as primary user, granular technical specification welcome.** "Don't want to micromanage too many details early on" but "a creative person oversees it." Ben drives every decision.
- **Vault-as-memory / lessons across sessions.** "Would be great if it could learn — storing the lessons locally — markdowns per session — lessons per project." Patrick's vault discipline maps directly.
- **In-place re-roll buttons.** "An image of what the board presently is… regenerate buttons next to each." Matches the brief's candidate-carousel UI.
- **Sub-location handling → world discovery through storyboarding.** [reframed] "Walk & talk along a hallway… want to give this hallway-north-end?" Not just sub-location keying — it's *world state being discovered during the making.* Storyboarding reveals that what was named one location is actually several. Mechanism: bubble up the discovery, register the new location, consistency-check existing material. Connects to a possible background consistency-checker / rubric layer using vision language models — touched on with Patrick's rubric pattern. Mechanism unclear; a real Phase A discovery question (see `PHASE_A_GOALS.md`).
- **The closed-model + reference workflow is the right path now.** Ben's experience with Flux 2 Dev + LLMs: "can get consistent faces but then terrible with the styles." Same prior the brief argues against the open-model-first path.

---

## Redirected by Ben (things to update in the brief)

### 1. **MVP target → establishing shots of every scene, not panels**

> "Draw the establishing shot of every location… every scene that David & Ben are in."
> "FIRST — not even per-beat. What's the opening shot of every scene."
> "Establishing shot of every scene."

This is a smaller scope than the brief's mini-sequence test. **The first deliverable isn't a coverage-complete scene — it's one wide per scene, across the whole script.**

Implications:
- Phase 1 (bible build-out) and Phase 2 (mini-sequence test) collapse for the MVP. The first real run produces a *book of establishing shots*, not panels.
- Locations move ahead of characters as the load-bearing asset. The world bible matters first; character bible matters second.
- The brief's "scene-coverage protocol" doesn't apply yet — coverage is Phase 2 work.

### 2. **Character casting via actor reference, not invented from scratch**

> "I think this character is kind of a Hans Solo character → Harrison Ford."
> "Harrison Ford photograph → commit to storyboard style."
> "Screenwriters… write a description. Do your best to describe what the character looks like — upload an image / generate an image — take upload and draw it in cowboy."

The bible-creation workflow shifts. Instead of "Ben describes a character from scratch and the model invents them," it's:
1. Director / screenwriter picks an actor reference ("this character is Harrison Ford energy")
2. Photo of that actor + chosen art style → render in the storyboard style
3. That rendered output becomes the character bible's hero ref

Two implications:
- The bible-creation flow needs **actor-photo → in-style character render** as a first-class operation. The brief's lookbook idea covers this, but the *actor → casting* framing is sharper than "face energy."
- The screenwriter / writer-room can produce their own character refs by picking actors. The director doesn't have to do all character creation work.

### 3. **Tone seed comes BEFORE script breakdown, not after**

> "First to review the script. But if it doesn't know the tone…"
> "Start with an opening series… tone, comps, genre (high level stuff). So as it goes through to break it down it has more guidance."
> "Big Homerian Odyssey. No singles, want multiple people in shot. Millennium Falcon."

The brief had Loop 1 (script → scene breakdown) at the top. Ben says there's an even higher layer: **tone/comps/genre seed** before scene breakdown begins. This frames how the LLM interprets scenes downstream.

Without it: "you get really huge character inconsistency" (his words) and the model defaults badly.

New top of the loop:
```
Loop 0: Tone / comparable films / genre / style — manually seeded
Loop 1: Script → scene breakdown (informed by Loop 0)
Loop 2: Scene → beats (later)
…
```

### 4. **Director-named shot-type packages, not generic DSL** [reframed]

> "Spielberg close-up, Barry Jenkins close-up."
> "Whatever you choose… goes into your shot types — wide, extra wide."

The brief's DSL had a flat shot-scale axis (ECU/CU/MCU/MS/etc). Ben wants curated, *director-attributed* shot vocabularies. "Give me a Spielberg close-up" is a real operation in his head — it pulls a specific framing, lens choice, lighting register, and proxemic stance, not just a scale.

**Two readings of this artifact:**

- **Phase A controllability probe:** words are underspecified. The Damaggio "Spielberg close-up" experiment is a real lab test — can image refs disambiguate what prose alone can't? For DSL slots the model handles weakly with prose (camera angle, coverage geometry, specific shot flavor), do labeled reference frames help?
- **Phase B design pattern:** if yes, that's *also* how directors naturally specify. The curated shot pack becomes the project's vocabulary.

Same artifact, two readings. The Phase A probe answers a controllability question and simultaneously validates a Phase B input format.

Implication: the DSL's shot vocabulary should be extensible per project. Each project has a base set + a director's chosen "shot type package" (Spielberg / Jenkins / whoever). Curated up front to "avoid getting overwhelmed by bad filmmakers."

### 5. **The default rule for crowd scenes**

> "Raiders of the Lost Ark — Beats — Overall… 200 people in the movie. Put in 5, guess the others. Commit to those decisions. Generate… guard #2 etc."
> "You want the system to do as much as possible."

For ensemble / extras: the director specifies a handful of named principals, the system generates plausible-but-controllable defaults for everyone else ("guard #2"), and those defaults get committed (named, indexed) so they reappear consistently. This is the **bible's principal/extras tier extension** — already loosely in the brief but Ben made it concrete.

### 6. **Friction is the real enemy at the start**

> "Too much friction at the beginning and you…"
> "Atomic Habits."
> "If you're having a hard time getting starting…"

The brief plans Phase 0 as a careful grammar-validation exercise. Ben's instinct: **the first interaction with the tool needs to feel like the start of a creative session, not setup.** This argues for:
- A pre-baked starter "shot type package" + style seed + tone seed so a director can begin a new project in minutes, not days
- Templates, not blank-canvas onboarding

The Phase 0 work we just did (`phase-0/`) is the *engineering* validation. The *director-facing* Phase 0 needs to be a low-friction starter pack.

*Tension worth flagging:* upfront bible/world-building effort clashes with this friction-sensitivity. David's read for the lab is opposite — for someone starting from zero (himself, knows nothing), upfront effort builds the foundation needed before anything else works. Possibly resolved by noting these are different roles (director vs. look-dev vs. storyboard-artist-in-conversation-with-director), but currently unresolved. Phase A goes upfront-heavy by necessity; Phase B's friction profile is still open.

### 7. **"Orders" → workflow primitive + bubble-up loop, not config layer** [reframed]

> "For each particular storyboard, it would have the various ingredients to it… text descriptions, character refs, vehicle ref, particular shot ref."
> "This doesn't quite work, and I actually want to change… the trench coat of the character… needs to be transparent and then that needs to kind of like change the underlying state that we're tracking or even maybe like needs to bubble back up to creating the ref images."

The original "orders" reading (global config / standing-preferences / invalidation graph) was wrong. The actual concept is **per-frame ingredient assembly with bubble-up to source-of-truth:**

- Per frame, assemble: text description + character refs + vehicle refs + shot refs + location plate
- View the result
- Discover a constraint that's wrong ("trench coat must be transparent, not black")
- Push the change *back* — to the state ledger, possibly all the way back to the character bible's ref images

This is **the workflow primitive of the Phase B system**, not a side feature. Every panel is an assembly act, and every result is a candidate revision of upstream state. Implies a coding-agent-readable log of what was tried + what changed + what bubbled — intersects with the DSL (which holds the ingredient slots), with Patrick's pattern (lessons accumulating in markdowns), and with the consistency-rubric layer hinted at in §8 below and the sub-location discovery point. Mechanism for the log is itself a Phase A discovery (see `PHASE_A_GOALS.md` §4).

---

## New from Ben (things the brief didn't cover)

### 8. **The business model: ~$200/storyboard, first-pass for film companies**

> "Business in doing first pass storyboards for film companies."
> "$200 for a storyboard."

This is the actual product. Not a tool sold to directors — a *service* selling first-pass storyboards to film companies, with this system as the production engine. Implications for the brief's strategic section:
- The customer isn't (immediately) the director. It's the production company commissioning the storyboard.
- "Pitch quality" is one tier; "first-pass production storyboard" is the actual delivery shape.
- Unit economics matter, but the constraint is not just per-panel model spend. The research memo's first pitch-scale estimate is ~$14–83 for ~345 raw output images, depending on model/quality. Re-rolls and bible iteration can multiply that floor, but Ben's `$200/board` target is still more constrained by art-direction time, continuity review, and layout/polish than by compute.

### 9. **Captioning is the long-term LoRA-training feed**

> "Upload the storyboard images… don't have any captioning."
> "Looking forward to captioning them with film terms & emotional states."
> "So that the model is trained better for film & television."

The DSL + state-ledger metadata isn't just for prompt assembly. It's also **the captioning that trains future film-specific image models.** The brief's Track B (LoRA, later) gets a richer framing: not just a style LoRA, but a *film-vocabulary* LoRA trained on captioned storyboards across many projects.

### 10. **Productization (deployment) is in scope**

> "Vibe code…"
> "Hiring people to make it live online."
> "All the ins and outs of deployment."

Ben's already thinking about this as a real online tool, not a local workflow. Adds engineering scope the brief didn't price in.

### 11. **Style-fight problem with mixed world elements**

> "Tend to put world elements up that are in a completely different style."

A known failure mode: when generating a scene that combines characters + world elements + props, the world elements often render in a *different* style than the characters. Per-element style leakage. This is a real production issue that needs naming in the failure-mode taxonomy.

### 12. **Post-production tools (downstream context)**

For Ben's broader pipeline (beyond storyboards):
- **Compositing:** Corridor Keyer, Frischluft (DOF), Lens Care, Composite Wizard
- **Set extensions / matte painting:** Video Co-pilot tutorials, point-tracking workflow
- **Video generation:** Seedance 2.0 (works); Kling 3.0 (he says doesn't work); Seedream 2.0 ("amazing at reference video")
- **Workflow note:** "Adding AI to compositing — hardest part used to be the digital matte painting — matching lighting etc."

Out of scope for storyboard MVP but useful framing for what the tool integrates with downstream.

### 13. **Specific reference points Ben mentioned**

For visual references and creative anchors:
- Ben Affleck grey-box Netflix
- *Trailer for Hope* (Korean film Ben suggested watching — not a Ben project)
- 1980s anime aesthetic
- *Raiders of the Lost Ark* (crowd handling)
- *Blade Runner* / Deckard ("change Deckard's raincoat, based on the location he's in")
- *Neuromancer* (Ben asked David to re-read)
- Happy Horse — sound design

### 14. **Creative person in the loop is structural, not preference** [new, post-discussion]

> "Without a creative person in the loop, stuff goes off the rails."
> Ben's sniper-shot metaphor: small initial deviation → wildly off later.
> Ben's dead-end clip story: $5 + 40 minutes chasing one 5-sec clip, abandoned, changed surrounding context, kept going. An automated pipeline can't make that pivot.

The deepest takeaway from the meeting. **Pure mechanization doesn't work** — recalibration touchpoints are intrinsic to the workflow, visible in Patrick's discipline, confirmed by Ben's experience, matched by David's intuition that "it's almost impossible to get something decent in a purely mechanized way" with the current model generation.

Implications:

- **$200/board unit economics** must budget human-touch time, not just generation cost. The number probably re-prices once touchpoints are characterized.
- **Phase A's job** is to surface *where* the touchpoints have to be and *what* state needs to be tracked between them. These are mechanisms the Phase B system structurally requires.
- **Automation's hard ceiling** is the inability to back out of dead ends. A human can pivot ("fuck it, change what's around it"); an autonomous pipeline cannot. The right design question isn't "how much automation" but "where do the touchpoints need to be."

---

## Phase B MVP target: establishing shots across the script

The **destination** Ben described — what the eventual director-facing tool should produce first when a new project starts. **Not Phase A work.** Phase A is building the joints this MVP will rely on (controllability primitives, refs, state tracking, recalibration mechanics). Phase B assembles those joints into the workflow below.

```
Project setup
  ├── Tone / comps / genre seed   (Loop 0 — director-stated)
  ├── Style anchor                (e.g. Damaggio — already done in Phase 0)
  ├── Shot-type package           (director-named: "Spielberg close-up," etc.)
  └── Casting refs (per principal)
         └── Actor photo → in-style hero render

Script breakdown
  └── Scene list (Loop 1 — informed by Loop 0)

Phase-1 MVP deliverable
  └── ONE establishing shot per scene
       ├── Location plate derived from script + tone seed
       ├── Principals present (casting refs)
       └── Optional: defaults for ensemble ("guard #2")
```

That's the eventual Phase B first-shipment shape. Not a coverage-complete scene. Not a six-panel mini-sequence. **A book of opening shots, one per scene, across the whole script.**

Phase A work in `phase-0/` and downstream test beds is grammar validation for the joints this MVP will rely on. The MVP itself is Phase B — built once Phase A surfaces the mechanisms it depends on.

---

## Next concrete steps (for David)

Aligned with Ben's redirects:

1. **Update `STORYBOARD_SYSTEM_BRIEF.md`** — fold the seven redirects above into the brief. Especially: move MVP target to establishing shots, add Loop 0 tone seed, change character creation flow to actor-photo casting.

2. **Re-scope Phase 1 around the establishing-shots MVP.** Instead of "build the cowboy bible" first, the order is now:
   - Tone seed (manual, fast)
   - Style anchor (already validated via `phase-0/`)
   - Casting refs for the principals David & Ben are in
   - **One establishing shot per scene**, generated using the validated grammar

3. **Pick a real script.** Ben said "any stories want to play with… would love to stress test it." Neuromancer was mentioned (re-read). Real-script-with-real-Ben-feedback is the next test.

4. **Build the actor-photo → in-style render workflow** as a first-class operation. This is the casting refinement that wasn't in the brief.

5. **Carry forward the T03 finding** (expression sheet is load-bearing) into Phase 2, but Phase 2 is deferred — establishing shots don't need expression sheets.

6. **Run T06-iso** (still owed from Phase 0 — prose-only re-fire to isolate whether the framing reference contributed). Worth ~30 seconds before Tuesday's next round.

7. **Schedule competitive teardown** for Boords, LTX Studio, Drawstory, MITO, and Adobe Firefly Boards before Phase B UI commitments. The differentiator needs to be director-controlled production memory, not generic AI-storyboard generation.

---

## Open Ben-questions to surface

Things the meeting raised that weren't resolved:

- **Which script first?** Ben mentioned Neuromancer (re-read) and his own stories. Concrete pick needed.
- **Casting refs — uploads from screenwriter or generated by system?** Ben suggested both ("upload an image / generate an image"). Which is the default path?
- **Shot-type package — does Ben supply one already, or do we curate one for him?** "Spielberg close-up" is specific enough that someone built that package mentally already.
- **Deployment scope** — does productization start during or after MVP shipping?
- **Per-board cost target** — $200/board sets a ceiling mostly on human review and polish time, with model generation as the smaller cost line. What's the implied re-roll budget and review cadence?
- **What's a "scene" exactly?** For establishing-shot MVP, we need a script breakdown that's unambiguous about scene boundaries. Loop 0 + script-aware LLM pass.

---

## What didn't change

For closure: these brief items remain unchanged after the meeting.

- The DSL skeleton (SHOT/SUBJECT/STATE/ACTION/SETTING/MOOD/COMPOSITION/CONTINUITY) — still the right structure, just with a Loop 0 tone seed above it and director-named shot-type packages feeding the SHOT slot.
- The preserve/borrow/do-not-borrow grammar — empirically validated in Phase 0; Ben didn't push back.
- Patrick's vault-as-memory discipline — Ben explicitly endorsed it.
- The Genesis/Mutation distinction from Patrick's lessons — still load-bearing.
- The closed-model + reference workflow as Track A — confirmed.
