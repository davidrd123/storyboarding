# Storyboard System Brief

Synthesized from a long Claude chat (`2026-05-19_13-48-27_Claude_Chat_AI-generated_storyboard_system_design.md`). Final design only — corrections from the conversation are flagged inline where they justify the position.

---

## 1. Premise

A pipeline for generating pitch-quality storyboard books in a chosen art style, with character and location continuity, driven by a director's choices. Closed image-gen models + structured references are the rendering engine. The DSL, character/world bibles, and a script-aligned state ledger are the structured inputs that make output controllable.

Primary user: **the director.** Assume technical comfort and willingness to specify granular detail. The system's job is *fast, granular execution of the director's choices* — not creative proposal generation.

Commercial buyer: **production companies commissioning first-pass storyboards.** That matters because this is not trying to be a generic screenwriter storyboard toy or a marketer-friendly AI board canvas. The delivery shape is service-grade, director-controlled first-pass boards, with the system as the production engine.

### Origin and stated goal

This project started as a Discord ask: train a storyboard LoRA on a chosen artist's work (Rodolfo Damaggio as the test case), with film-term captioning, so pitch books could be generated in a consistent "house style." The strategic framing from the director was **"FairTrade, but way less heartbreak"** — find one artist willing to collaborate, train on their work *with consent*, ship pitch books that look like *their* hand.

The closed-model + reference pivot in this brief is a **pragmatic bootstrap, not a strategic preference.** A LoRA needs 40–80 captioned images that match the target style — basically a storyboard's worth of finished art — which the project doesn't have on day one. Closed-model + reference workflows are what's possible *today*. The collaborator-trained LoRA path remains the closer-to-stated-goal destination.

The director also already named most of the structural concepts in this brief — "character sheets in the style of our artist," "caption the dataset to respect film terms," "find an artist who has each variation of shot in their work." The brief below isn't proposing new ideas so much as formalizing instincts already on the table.

### Two tracks

- **Track A (the bootstrap):** closed-model + reference-image workflow. Available today. Style ~70%, controllability ~90%. Uses an artist's publicly-visible work as in-context references, not as training data. Ships pitches in weeks.
- **Track B (the destination):** open-model LoRA trained on Track A's output corpus + a recruited collaborator's hero refs. Style ~90%, full ownership, structurally consent-respecting. The path that realizes the original strategic intent — and (per the human-in-loop note below) also the substrate for human-supervised volume at scale.

The real product isn't the model — it's the DSL + bible flow + panel assembly pipeline. Durable across the Track A → Track B transition, and across projects after that.

### Competitive position

AI storyboard products already exist: Boords, LTX Studio, Adobe Firefly Boards, Higgsfield Popcorn, Drawstory, MITO, Runway, Storyboarder, and Showrunner all occupy parts of the space. The differentiator cannot be "AI storyboards exist."

The product position is sharper:

> A director-controlled pitch-storyboard system that externalizes a film's visual world into bibles, maps directorial intent to script position, assembles role-labeled references automatically, preserves prompt lineage, and flags continuity drift.

Boords / LTX / Firefly / Drawstory are credible products and need hands-on teardown before UI commitments. The initial customer segment here is narrower: production companies paying for first-pass boards, where continuity memory, bible invalidation, candidate history, and a human art-direction loop are more valuable than broad creator onboarding.

### Human-in-loop is structural, not optional

A meeting takeaway worth surfacing in the premise, because it changes how to read everything below: **pure mechanization doesn't work.** Ben's sniper-shot metaphor (small initial deviation → wildly off later), his dead-end clip story (a human can pivot when stuck; an autonomous pipeline cannot), Patrick's lessons-in-the-loop discipline, and David's own intuition all converge: the product isn't "AI generates storyboards" — it's "AI generates storyboards with the creative person catching drift early and recalibrating."

Implications:

- The eventual proposals-with-approval interaction mode (see Open Questions §4) isn't fire-and-forget. It means *the system proposes; the human approves/corrects at recalibration touchpoints baked into the workflow.*
- The $200/board unit economics need to budget human-touch time, not just generation cost.
- Phase A lab work (see `PHASE_A_GOALS.md`) is explicitly tasked with surfacing where the touchpoints have to be and what state needs to be tracked between them. These are mechanisms the rest of this brief implicitly assumes but doesn't yet specify.

### Two phases of work

This brief describes the destination architecture. Two distinct phases produce it:

- **Phase A — controllability lab (now, David driving).** Hands-on, struggle-tolerant, lessons-into-markdowns. Patrick's discipline as the substrate. Test beds (compositing class project; `phase-0/` Damaggio work; bespoke micro-scenarios) probe specific joints. Deliverable = knowledge in markdowns + working artifacts as side effects. Goals in `PHASE_A_GOALS.md`.
- **Phase B — Ben's directorial tool (later, derived from Phase A).** Low-friction, proposals-with-approval, fitted to a director's complexity tolerance. The MVP target (establishing shots across the script — see `MEETING_BREAKDOWN.md`) lives here. Built *on top of* Phase A lessons, not as a transition from them — the lessons keep accumulating.

### Research correction absorbed

The model layer is good enough to test now. The unsolved product problem is not whether an image model can make nice panels; it is whether the system can maintain **controllable production memory**: bibles, state ledger, role-labeled refs, prompt lineage, candidate history, and continuity checks.

Current research updates folded into this brief:

- Current OpenAI production image model ID is `gpt-image-2`; old `gpt-image-1` references are stale for new code/docs.
- `gpt-image-2` supports up to 16 GPT image-model edit inputs. 2K is reliable; 4K-class sizes are possible but still experimental enough to reserve for selected final panels.
- Gemini / Nano Banana reference limits are role-specific, not just "14 refs." The 14-ref cap is real, but object and character caps determine practical assembly.
- Raw model output cost is unlikely to be the bottleneck. The first pitch-scale test is tens of dollars in API cost, while art-direction time, re-roll review, bible iteration, and layout/polish are the real constraints.

---

## 2. The DSL

Storyboards are a constrained vocabulary; treating them as a domain-specific language is the unlock that makes panel generation programmatic.

### Six controllable axes

| Axis | Values |
|---|---|
| **Shot scale** | ECU, CU, MCU, MS, MLS, FS, LS, WS, ELS, insert, two-shot, three-shot |
| **Camera angle** | eye level, high, low, bird's eye, worm's eye, Dutch, OTS, POV, profile |
| **Camera move** | static, pan, tilt, dolly in/out, truck, crane, tracking, push-in, rack focus, whip |
| **Coverage role** | establishing, master, OTS reverse, reaction, insert, cutaway, transition |
| **Composition** | rule of thirds, leading lines, fg occlusion, frame-within-frame, headroom, negative space |
| **Continuity** | screen direction, eyeline match, 180° line, match-on-action |

The shot-scale axis is the **base layer**; per-project **director-curated "shot type packages"** (e.g., a canonical "Spielberg close-up" reference frame) extend it at the project level. See `MEETING_BREAKDOWN.md` §4 and `PHASE_A_GOALS.md` §3 — the question of whether image references can lock shot-flavor that prose alone leaves underspecified is an active Phase A probe (`TEST_BEDS.md` Bed 1).

### Panel skeleton

```
SHOT:        [scale] [angle] [movement if any]
SUBJECT:     [character name — refs Image 1]
STATE:       [expression + physical condition + wardrobe variations +
              held objects + eyeline + body tension]
ACTION:      [verb of this beat]
SETTING:     [location + time of day + weather + state of place]
MOOD:        [lighting direction + quality + atmosphere + tone]
COMPOSITION: [fg/mg/bg staging + framing + negative space + leading lines]
CONTINUITY:  [link to prior/next panel, screen direction]
```

### The Identity / State / Action distinction

The load-bearing structural insight. Three things that look similar but want different treatment:

- **Identity** — face, build, hair, signature wardrobe. Locked by reference image. Doesn't change panel to panel. Handled by the bible.
- **State** — expression, physical condition, eyeline, body tension, costume variations from baseline, held objects, attention focus. Specified in prose *and* (where helpful) reinforced with an atomized expression/pose reference.
- **Action** — the verb. What they're doing in this beat.

State carries the emotional content of the panel. Panels with locked identity and described action but no explicit state slot tend to render as "visually correct but emotionally flat."

> **Correction worth keeping:** the original DSL draft (`[shot scale] [angle] of [character] [action], [setting], [mood/lighting]`) had no `STATE` slot. That was the structural gap.

### Example filled in

```
SHOT: MCU, low angle, slight push-in
SUBJECT: Cowboy [ref: cowboy_bible_3q.png + cowboy_expr_cold-rage.png]
STATE: Jaw set, dust on his face, sweat at the hairline, eyes narrowed
       and locked off-frame right. Scarf loosened. Hand resting on
       holster grip but not closed around it. Wound tight but still.
ACTION: Holds his ground, watching.
SETTING: Beside the brick well, late afternoon, long shadows.
MOOD: Tense, anticipatory. Warm directional light from frame left,
      deep shadow on his off side. Dust haze in the air.
COMPOSITION: Cowboy occupies right two-thirds; eyeline pulls composition
             to empty left third. Negative space signals what he's
             watching without showing it.
CONTINUITY: Picks up from prior panel where officer pointed off-right.
```

---

## 3. The Bibles

The bibles are the externalized vision of a specific story's visual world. Generate once, reference everywhere. Co-evolves with storyboarding — first version informed by script + reference; later versions informed by what works at panel-generation time.

The core idea — *character sheets in the style of the artist, plus a recognition system for retrieving the right one per panel* — was the director's framing from the project's start. The structure below is the formalization, not the proposal.

### 3.1 Character Bible

Per principal character (~20–25 image assets):

1. **Turnaround sheet** — 6 angles, neutral pose, locked costume. Identity anchor. The costume reference.
2. **Action/pose sheet** — 4–6 signature poses (walking, running, idle, turning, looking back). Body language and silhouette.
3. **Expression sheet** — 14–18 emotional states (tiered, see below). Highest-leverage asset for reaction beats and CUs.
4. **Costume/state variants** — only if script requires (bloodied, soaked, formal, disguise).
5. **Bio block** — not an image; a metadata box (age, era, traits) that feeds prompt prose every panel.

Side characters: turnaround + 6 Tier-1 expressions. No action sheet.

### 3.2 Expression sheet, tiered

The hardest asset to do well, and the diagnostic for whether the whole pipeline works (asks the model to hold style + identity while varying emotion, which is the load-bearing case for current image models).

**Tier 1 — universal (8, every principal):** neutral, surprised/startled, determined/focused, angry/hostile, worried/concerned, amused/smirking, sad/grieving, confused/questioning.

**Tier 2 — genre-fitted (4–6, e.g. for western/adventure):** cold rage (suppressed), tactical/calculating, defiant, pained but pushing through, world-weary/resigned, suspicious/wary.

**Tier 3 — character signatures (2–4):** the looks unique to *this person*. For a cowboy character: "the dry sideways look," "the moment-before-the-draw stillness." For an officer: "the formal mask cracking."

### 3.3 Asset format conventions

- **Angle:** 3/4 front, eye-level. Most expressive, most flexible as reference.
- **Crop:** tight headshot — top of head to mid-chest.
- **Lighting:** flat, even, neutral. *Mood belongs in panels, not in references.* Moody backlighting on a reference is noise the model will preserve.
- **Background:** solid neutral.
- **Style:** matched to the chosen art style.
- **Profile variants:** for 2–3 highest-traffic expressions (neutral, determined, surprised) — for shot/reverse-shot coverage where 3/4 doesn't retarget cleanly.

### 3.4 Metadata schema

Atomized asset filename + JSON sidecar:

```yaml
filename:  cowboy_expr_cold-rage.png
character: cowboy
type:      expression
label:     cold-rage
intensity: 2/3
synonyms:  [suppressed-anger, slow-burn, contained-fury]
visual:    flat affect, eyes hard and unmoving, jaw set, no movement
use-for:   [confrontation hold, moment-before-violence, dressing-down]
opposite:  amused
related:   [determined, tactical]
```

`synonyms` matters more than it looks — when an LLM prompt assembler is mapping a beat description ("seethes at the order") to a bible asset, generous tagging is what makes the lookup land.

### 3.5 Composite vs atomized references

> **Research correction:** initial guidance was "atomize all references — clean isolated images work best." That was too narrow. Composite sheets remain a strong working pattern, but don't over-attribute the claim: the "complete 3D understanding" language came from third-party Nano Banana Pro guidance, not verified Google docs. Official docs support multiple role-labeled references with object/character caps; the composite-vs-atomized choice is still an empirical Phase A question.

Keep both forms:
- **Composite sheet** as the canonical "character canon" asset, especially for human approval / artist briefs and for testing Nano Banana Pro's multi-view behavior.
- **Atomized extracts** for prompt-assembly logic (programmatically picking "the running pose"), reference budgeting (when other refs crowd the budget), and targeted edits (changing one jacket color across the project).

### 3.6 World Bible

Same discipline, different subjects:

- **Location plates** — each recurring location, 2–4 angles capturing geography. Same-place continuity across panels.
- **Signature object/prop sheets** — recurring props that need consistency (specific revolver, pressure gauge, cavalry sword). Clean reference image each.
- **Vehicle sheets** — recurring vehicles that need consistency (specific make/model, damage state, weathering). Treat as their own category rather than lumping with props; vehicles are often hero objects in genre work, get featured at multiple scales, and accrue continuity state (dents, mud, missing panels) that needs tracking the way costume state does for characters.

### 3.7 Lookbook (the upstream input to bible creation)

The director's lookbook is *exactly* the structured input bible creation needs. It's how directors already communicate vision to crews — film stills for cinematography, photography for mood, concept art for visual style, period wardrobe, casting refs ("he has the energy of [actor in film]").

Atomized by role:
```
lookbook/
  style/                damaggio_panel_01.jpg, …
  characters/
    cowboy/             face_energy_01.jpg, costume_reference.jpg, silhouette_ref.jpg
    officer/            …
  locations/            well_reference_01.jpg, …
  mood/                 lighting_reference_01.jpg, …
```

Bible creation then becomes structured synthesis, not invention from scratch:

> "Image 1: face energy. Image 2: costume reference. Image 3: art style. Generate a turnaround sheet for this character — borrow face presence and bone structure from Image 1, costume vocabulary from Image 2, rendered in the style of Image 3. Do not borrow specific identity from Image 1; do not borrow subject from Image 3."

This is the most creatively important phase of the project, not a few days of grinding. Holding style + identity + variation constant while varying the fourth dimension is the hardest case for current image models, and every bible asset is foundational — a bad turnaround propagates into every downstream panel.

---

## 4. Reference Grammar

The pattern: **`Preserve [X] from Image 1. Borrow [Y] from Image 2. Do NOT borrow [Z]. Generate [new scene].`** Explicit fencing per reference earns its keep — leakage is real and documented.

### What translates from prose alone (no reference needed)

- Style category ("ink wash western," "European bande dessinée")
- Action verb ("walking," "drawing his pistol")
- Mood adjectives ("tense," "melancholy")
- Time of day, weather
- General setting class ("desert with ruins")

### Ambiguous from prose (reference helps)

- Specific shot scale boundaries — MS/MCU/MLS distinctions blur; model defaults to "comfortable medium"
- Camera angle — geometry is relational; prose alone often lands at eye-level regardless
- Coverage geometry (OTS specifically — precise spatial relationship)
- Foreground occlusion / frame-within-frame
- Specific lighting direction (which side, how harsh, what bounce)
- Eyeline precision

### Definitely needs reference

- Character identity
- Specific location continuity (the *same* well across panels)
- Style fidelity to a specific artist's line quality
- Specific prop continuity

### What references actually transfer cleanly

Evidence-supported (from OpenAI/fal and Google prompting guides):
- Concrete visual properties: color, palette, line quality, edge treatment, texture
- Pose transfer between different subjects
- Style/palette transfer between different subjects
- Framing preservation *in edits* of the same image

> **Correction worth keeping:** initial speculation that abstract relational properties like "camera angle" would transfer cleanly across subjects via role labels was overstated. fal.ai's guide explicitly notes reference handling is stronger for *concrete* properties than purely abstract relational ones. PixVerse's guide treats camera distance/angle/placement as prompt-stated, not reference-extracted. No documented workflow for "use Image 3 to lock camera angle, with a different subject, in fresh generation."

**The workaround:** frame angle/composition transfer as **compositional skeleton transfer** (the pose-transfer paradigm), not abstract concept extraction. Concrete spatial geometry, with explicit fences:

```
Image 3: compositional reference
  Borrow: camera position relative to subject, horizon height,
          vertical proportions, framing
  Do NOT borrow: subject, costume, location, props, style,
                 palette, lighting, or any other visual element
```

### Reference budgets

- **`gpt-image-2`:** up to 16 GPT image-model edit inputs. Use 1536×1024 or 2048×1152 as reliable pitch-board sizes; treat 4K-class output as experimental / final-panel only.
- **Gemini 3 Pro Image / Nano Banana Pro (`gemini-3-pro-image-preview`):** up to 14 reference images overall. Role caps matter: 6 high-fidelity object refs + 5 character refs.
- **Gemini 3.1 Flash Image / Nano Banana 2:** up to 14 reference images overall. Role caps matter: 10 high-fidelity object refs + 4 character refs.

The old "~6 refs is the sweet spot" line is a house prior from third-party guidance, not an official cap. Keep it as a caution when quality degrades, not as a rule.

Typical per-panel: `character_ref + expression_ref + location_plate + style_ref` = 4 refs. Well under budget.

### Prose + reference is belt-and-suspenders

When prose describes state and an atomized expression ref shows it, the model locks. When they contradict (`expr_smirking` ref but prose says "jaw set, furious") the prose usually wins but you get drift. Useful for debugging.

### Empirical status from `phase-0/FINDINGS.md`

The reference grammar above is no longer speculative. Phase 0 ran six tests against Nano Banana Pro (~$2, 10 minutes) and produced concrete empirical markers worth carrying forward:

**Validated:**

- **Bible-driven workflow holds identity across scenes.** T02 → T05 chained the same cowboy across mesa, slot canyon, and well location — all in style, all recognizable. Single hero ref was sufficient to lock identity across 5 totally different scenes. This is the architectural claim the brief leans on most heavily; it's now confirmed.
- **The expression sheet is load-bearing (the diagnostic was a failure).** T03 fed prose like *"cold rage held in, jaw set, eyes hard, no movement"* and got back an overt snarl with bared teeth. The model defaults to *legible* emotion over *suppressed* emotion. The brief predicted the expression sheet would be the highest-leverage Phase 1 asset; T03 is the proof, not an artifact to fix.
- **Do-not-borrow fences work.** Zero subject leakage in T01 and T04 from style-only references. The grammar that the rest of the system rests on is real.
- **Distinct location categories transfer from prose alone.** T04 produced a recognizable slot canyon without a location plate. Implication: only build plates for *recurring* locations; new unique locations can be prose-only.

**Ambiguous:**

- **Compositional skeleton transfer (camera-angle-as-pose-transfer).** T06 produced a correct-looking low-angle output, but the prose said "looking down toward the camera" — which alone would already imply low angle. We can't separate which input carried the angle. A `T06-iso` run (same prompt, no framing reference) is the cheap definitive test and remains pending.

**Known quirks worth designing around:**

- **Mirror flips happen.** T05's composition mirrored (cowboy on left instead of right). For storyboards screen-direction is continuity grammar, so this matters. Mitigation: explicit "cowboy on right side of frame" in prose.
- **Linework register trends slightly tight.** Output reads a hair more *illustrated* / *polished* than Damaggio's loose confidence. The brief's "style ~70%" estimate is closer to 80%+ on technique with the looseness register being the remaining gap. A Track-B LoRA is the cleanest path to closing it.

---

## 5. Pipeline

### Loop 0 — Tone, comparables, genre seed (hours, director-led)

Before any image work, the director seeds tone descriptors, comparable films, genre anchors, and named-director cinematography references (see `MEETING_BREAKDOWN.md` §3, §4). This conditions every downstream decision — scene breakdown, character casting, shot vocabulary. Without it, "you get really huge character inconsistency" (Ben's words) because the model defaults badly when high-level intent isn't established.

Output: a short tone document the script-breakdown, bible, and panel-assembly work all consult. Also, the curated shot-type package (Spielberg close-up, Jenkins close-up, etc.) that extends the base DSL shot-scale axis per project.

For David's Phase A lab work specifically, the equivalent of this seed is a discovery rather than a spec — `PHASE_A_GOALS.md` deferred items.

### Phase 0 — Style seed + prompt grammar (Day 1)

Take 3–5 hero images from the chosen artist as style anchor. Run single-image experiments to validate "borrow style only" grammar. Goal isn't a finished panel — it's *learning how the model responds to your prompt structure.* Output: a validated grammar template + a confidence level on style preservation.

> **Empirical status:** Phase 0 validated against Nano Banana Pro in `phase-0/FINDINGS.md`. Four tests passed cleanly, T03 produced the useful expression-sheet diagnostic failure, and T06 remains visually good but attribution-inconclusive. Grammar template captured in FINDINGS §"The validated grammar." Specifically the `Do NOT borrow from Image N: subject, composition, location, props, scene elements` fence works (zero subject leakage in T01/T04) and concrete-feature-list preservation (`"face structure, beard pattern, hat shape, scarf, jacket, build"` instead of `"preserve the character"`) is what actually holds.

### Phase 1a — Lookbook curation (days, director-led)

Director assembles references from existing collections + new pulls, organized by role (style / characters / locations / mood). Familiar job for any working director.

### Phase 1b — Hero image exploration (days, Midjourney)

For each principal: explore with character + style references from the lookbook. Mood-board pace, fast iteration, taste-driven. Output: a chosen hero image of the character that captures the right energy and style.

### Phase 1c — Character bible build-out (~1 week per principal, `gpt-image-2` / Gemini)

Take the Stage A hero image as canonical reference. Use role-labeled grammar to systematically generate turnaround, action sheet, expression sheet. Methodical, controllable, reproducible.

### Phase 1d — World bible (parallel with 1c)

Location plates + prop sheets. Same pattern: lookbook refs → hero image → plate variants. Faster than character work (no expressions or poses to enumerate).

### Phase 2 — Script + state ledger

Director walks through the script with the system, dictating directorial intent per beat. The LLM's job is to structure that input into the ledger — *not* infer it from sparse script.

```
Scene 3.2 — Well, late afternoon
  Persistent state:
    Location: brick well + tent canopy + distant ruins
    Time: late afternoon, low warm directional light, dust haze
    Present: cowboy (since 3.1), officer (since 3.1)

  Beat 3.2.1 — Officer admits sabotage
    Cowboy state:  shifting to cold rage. Wound healing on right
                   shoulder since 2.4 — sleeve torn there.
    Officer state: resigned, parade-rest broken, eyes down.
    What just happened: officer's confession line.
    What's about to happen: cowboy moves on officer.
    Visual intent (director): "I want to feel the temperature change.
                   Hold on the cowboy first, very still. Then a hard
                   cut to the officer, smaller in the frame than he
                   was a beat ago."
```

The state ledger is **script-locked but rendering-independent.** It exists whether or not panels are generated. It's queryable ("what was the cowboy wearing in 2.4?") and editable (change a beat → downstream beats flagged stale).

> **Correction worth keeping:** the initial framing had the LLM "extracting state from script." That was the wrong frame — the LLM doesn't know how the director wants Mike to enter the room. The director supplies intent; the LLM structures it.

### Phase 3 — Beat selection

Director walks the state ledger and decides which beats deserve panels. Most beats don't (dialogue, transition). Visually charged beats — reactions, decisions, reveals, action moments — get one or more panel slots. Taste call; don't try to automate.

### Phase 4 — Panel rendering

The prompt assembler combines: state from ledger + director's intent for this panel + relevant bible refs + style anchor + preserve/borrow grammar.

```
SHOT: MCU, low angle, slight push-in
SUBJECT: Cowboy
  References:
    Image 1: cowboy_turnaround_3q-front.png (character identity)
    Image 2: cowboy_expression_cold-rage.png (current state)
  Preserve from Image 1: face structure, hair, jacket, scarf, build
  Preserve from Image 2: facial expression, eye intensity
STATE: jaw set, dust on cheek, eyes locked on officer off-frame right,
       hand near holster grip, shoulder wound's torn sleeve visible
ACTION: holding ground in tense stillness before moving
SETTING:
  Image 3: well_location_plate.png
  Preserve from Image 3: well geometry, ruins position, dust haze
MOOD: warm directional light from left, deep shadow on off-side of face
STYLE:
  Image 4: damaggio_style_anchor.png
  Borrow from Image 4: line quality, ink wash, palette
  Do NOT borrow from Image 4: any subject, composition, or scene elements
COMPOSITION: cowboy frame right, eyeline pulls left, negative space
             signals what he's watching
CONTINUITY: picks up from Beat 3.1.4 where officer pointed off-right
```

3–4 candidates per panel. Director picks, re-rolls, or edits the prompt directly. History is preserved — every rejected candidate stays around in case the selected one needs to be revisited.

**Reference-window scaling:** long sequences should not keep every prior panel attached. The known pattern for >14-ref pressure is canonical asset refs + a sliding window of recent context, with File API / `file_uri` handles where the backend supports them. The state ledger decides what must be re-injected; prior images are evidence, not permanent prompt baggage.

### Phase 5 — Continuity check + assembly

A vision-model checker runs across selected panels in sequence, validating against the state ledger. "Panel 47 should show torn right sleeve (wound from Beat 2.4) — actual image shows intact sleeve. Flag." Inline annotations, not separate report. Director reviews flags, accepts or re-rolls. Final layout into pitch book.

### Recipe reconciliation

Two specific recipes were proposed by the director at the project start:

- **Recipe 1:** trained LoRA generates the base image → closed model (`gpt-image-2` / Nano Banana Pro) face-replaces and context-edits for consistency.
- **Recipe 2:** closed model "understands the style and fully runs with it" — no LoRA in the loop.

This brief's recipe is **closer to Recipe 2 with one refinement: Midjourney handles hero-image exploration (Stage A); `gpt-image-2` handles systematic bible build-out and panel rendering (Stage B and beyond).** Reasons for not running either original as-is:

- **Recipe 1 reinstates the cold-start problem we're trying to escape.** It needs the LoRA up front, which means 40–80 captioned images of the target style — i.e., the data we don't have. Recipe 1 *is* viable once a collaborator artist is recruited and Track B is live; until then it's not bootstrappable.
- **Recipe 2 underweights exploration cost.** `gpt-image-2` is strong on instruction-following and controllability but defaulty in exploratory aesthetics. Midjourney is meaningfully better at "what could this character look like?" *before* a hero image is locked. Spending Stage A in Midjourney costs a few days and saves weeks of style drift downstream.

Once a hero image exists from Stage A, the rest looks essentially like Recipe 2 — `gpt-image-2` systematically generating bible assets and panels with the hero image as reference anchor. So the brief's recipe is best understood as **"Recipe 2 with Stage A prepended,"** not a third path.

### Model choice

> **Research correction:** the prior that "Midjourney wins on style, full stop" is outdated, but the old Elo numbers were stale. Arena's May 12, 2026 snapshot had `gpt-image-2 (medium)` at **1393±7** for text-to-image and **1467±5** for image edits. Treat the numbers as a snapshot, not a durable truth. The directional point holds: the closed OpenAI / Google production path is credible enough to test now.

The professional pattern is hybrid:
- **Midjourney** — mood boards, aesthetic exploration, hero image hunting (Stage A).
- **`gpt-image-2`** — production work where role-labeled grammar, editing, and high reference counts matter.
- **Gemini 3 Pro Image / Nano Banana Pro** — production work where strong multi-reference character / object handling and fast iteration matter.
- **Gemini 3.1 Flash Image / Nano Banana 2** — speed / high-volume exploration when role caps are acceptable.
- **`gpt-image-1.5` / `gpt-image-1-mini`** — possible lower-cost comparison models, but not the current quality bar for pitch boards.

**IP caveat:** Midjourney has no public API and active IP lawsuits (Disney/Universal, WB). For commercial pitch use this is non-zero risk. A risk-conscious version of the pipeline is all closed-model (`gpt-image-2` + Nano Banana Pro), accepting somewhat lower default aesthetics for cleaner commercial posture.

### Production economics

A first pitch-scale test is not likely to be API-cost constrained. The research memo's 345-output-image estimate lands around **$14–83** in raw model output cost depending on stack and quality. That is the floor, not the typical: re-rolls, failed bible assets, and layout/polish can multiply it. But the strategic conclusion still changes: Ben's `$200/board` target is generous for compute and tight for human art-direction time. Measure re-roll rate, but design around human review throughput.

### Bible vs state ledger — how they relate

The circularity that seemed thorny resolves cleanly:

- **Bibles are upstream of state ledger.** They establish what characters and locations *look like at baseline.*
- **State ledger is upstream of panels.** It establishes what's true at any given script position.
- **Panels reference both.** Bible provides identity; ledger provides the moment.
- **Iterating on either propagates downstream.** Bible update → potentially affects panels referencing it. Ledger update → potentially affects panels at and after that beat.

The bible is a **living document** — first version informed by script + reference; later versions informed by trying to make panels. Don't try to fully solve the bible before storyboarding starts; assume it co-evolves. The system needs to support versioning + "panels affected by this change" surfacing.

---

## 6. UI Sketch

### Principles

- **Script is the spine.** Everything else is derived from script position. Scroll the script, the rest of the view updates.
- **State is always visible at any script position.** A persistent panel showing "as of this line: who's here, where, what state, what just happened, what's about to happen." Click any state element to see how it was derived.
- **Candidates are visual.** Each panel slot is a small carousel — multiple generated options + the currently-selected one. Re-roll, edit DSL, or pick a different candidate per slot.
- **History is non-destructive.** Every rejected candidate preserved. Every state revision preserved. Roll back any decision without losing parallel work.
- **Continuity issues are inline annotations.** Flag surfaces on the panel, not in a separate report.

### Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│ SCRIPT (scroll spine)  │ STATE AT CURSOR    │ PANEL SLOTS           │
│                        │                    │                       │
│ Act 1                  │ Location: well     │ ┌──┬──┬──┐            │
│  Scene 1.3             │ Time: late aft.    │ │○ │◉ │○ │  ← carousel│
│    Beat 1.3.1 ●        │ Present: Cow, Off  │ └──┴──┴──┘   for this │
│  ▶ Beat 1.3.2 ●●       │ Cowboy: cold rage  │ DSL ⌄         beat   │
│    Beat 1.3.3          │ Officer: resigned  │ Re-roll               │
│    Beat 1.3.4 ●        │ Costume: as 1.3.1  │ Continuity ⚠         │
│                        │ Just happened: ... │                       │
│  Scene 1.4             │ About to: ...      │                       │
└─────────────────────────────────────────────────────────────────────┘
```

Dot markers next to beats: `○` empty slot, `●` selected panel, `●●` multiple panels in sequence.

### Four nested loops

The system runs four loops at different cadences. Edits at slow loops invalidate fast ones; surface that with explicit "stale" warnings rather than silently regenerating.

| Loop | Job | Cadence | Decisions per script |
|---|---|---|---|
| 1 | Script → scene breakdown | Slowest, most strategic | Tens |
| 2 | Scene → beats with state | Most creative state-tracking | Hundreds |
| 3 | Beats → panel selection | Taste call per beat | Hundreds–thousands |
| 4 | Panel → image candidates | Fastest, most iterative | Where image gen lives |

### Hard parts to design around

- **State derivation is genuinely hard.** Scripts don't make state explicit ("Mike enters the room" — angry? bleeding? wet from rain?). The LLM will infer and often guess wrong. The human review in Loop 2 is doing real work. Plan for it.
- **"Which beats want panels" is taste-driven.** A good storyboard isn't every beat panelized — it's the *visually charged* beats. LLM can propose defaults; human is making real creative decisions. Don't automate away.
- **Iteration across scopes creates churn.** Re-derive a scene's state → every panel below may need re-evaluation. Need an **invalidation graph** that marks downstream artifacts as stale rather than silently regenerating. Real engineering problem at scale.

---

## 7. Open Questions / Decisions

### Strategic decisions

1. **Timing of the artist-collaborator transition.** Damaggio is locked as the *testing* style — chosen for clear, recognizable aesthetic and publicly-visible body of work. The real strategic question is **when** the project transitions from testing on Damaggio's publicly-visible work to recruiting the collaborator artist whose corpus becomes Track B. After Phase 1c (one principal's bible proven)? After Phase 2 (mini-sequence proven)? Before any commercial pitch ships externally? This decision is coupled to commercial use and outreach timeline, and it's the operational expression of the FairTrade-with-less-heartbreak goal.
2. **Track A polish vs. Track B speed.** Track A is a bootstrap, not the destination. Live question: how much effort to invest in Track A polish vs. moving as fast as possible to artist outreach for Track B? Polishing Track A produces nicer near-term output and a better training corpus for the eventual LoRA; rushing to Track B realizes the original strategic intent sooner. (Coupled to decision #1.)
3. **Closed-only vs hybrid model stack.** Hybrid (MJ + `gpt-image-2` / Gemini) for better default aesthetics but IP exposure. Closed-only for clean commercial posture but a step down in default style. Should be an explicit choice, not a default.
4. **Interaction mode — mostly resolved by meeting, refined open question remains.** Phase B = proposals-with-approval (Ben: "want more to happen behind the scenes," "the system to do as much as possible," "a creative person oversees it"). Phase A = direct/manual (David driving in lab mode, Patrick-style). The deeper constraint from the Premise (human-in-loop is structural) refines the question: proposals-with-approval doesn't mean fire-and-forget — it means the system proposes; the human approves/corrects at recalibration touchpoints. **Live question:** *where do those touchpoints need to be?* This is a Phase A discovery (`PHASE_A_GOALS.md` §1) rather than a brief-time decision.

### Technical / empirical questions

1. **Identity preservation at panel scale.** How much does the bible-driven reference workflow actually reduce drift across a 60-panel sequence? (Phase 2 mini-sequence test answers this.)
2. **Compositional skeleton transfer.** Can role-labeled references reliably abstract camera angle / composition across different subjects? Likely partial; needs empirical mapping per DSL slot.
3. **Re-roll rate at production volume.** 20–30% is only a planning prior; the real number determines per-panel cost, human review throughput, and pipeline cadence. Measure it in Phase A rather than budgeting from the prior.
4. **Bible synthesis under load.** Holding style + identity + variation simultaneously is the hardest case for current models. The expression sheet for one principal is the diagnostic — if that works clean, the whole pipeline works.

### Pipeline / engineering questions

1. **Captioning layer schema.** Filename convention + JSON sidecar per asset. Concrete schema needs to land before automation scales.
2. **Beat-to-DSL translator.** Interactive iterative refinement vs one-shot LLM pass? Probably interactive with candidate history.
3. **Continuity checker implementation.** Vision-model run per panel against state-ledger query? What's the false-positive rate that keeps it useful instead of noisy?
4. **QA criteria / re-roll triggers.** What defines "good enough"? Develops implicitly during Phase 1c — capture *why* you're rejecting outputs and that becomes the rubric.
5. **Bible versioning + invalidation graph.** Required before any project has its second pass.

### FairTrade / consent — load-bearing motivation, not appendix

This isn't a footnote on the system; it's the stated point of the project. The director's framing from day one was *"FairTrade, but way less heartbreak"* — meaning the destination is a tool built around **one consenting artist collaborator**, not a generic style-extraction pipeline that scrapes whoever's online.

- **Track A** uses an artist's publicly-visible work as *in-context references*, not as training data. That's the bootstrap consent posture — defensible for testing and internal R&D, weaker for sustained commercial use. Damaggio is the test subject precisely because the work is publicly available and the recipe is reproducible.
- **Track B** is where the original intent gets realized: a recruited collaborator's corpus becomes the LoRA training set, with consent, attribution, and (presumably) revenue share. The recruiting work is the real strategic dependency for sustained commercial use, not a downstream nice-to-have.
- **The live operational question (Open Questions §1):** when does the Damaggio-as-test phase transition to a recruited-collaborator phase? Before any commercial pitch ships externally? Before Phase 2? This is the decision that determines whether Track A is "the rest of the year" or "the next four weeks."

---

## Appendix: Conversation corrections at a glance

| Initial claim | Correction | Why it matters |
|---|---|---|
| Atomize all references for the model | Composite sheets are a strong working pattern, but the Google-originated "complete 3D understanding" claim was not verified; keep composite and atomized forms and test them head-to-head | Saves time during bible build-out without turning third-party guidance into canon |
| Nano Banana Pro is just "14 refs, sweet spot ~6" | 14 overall refs is real, but role caps matter: Pro = 6 high-fidelity object refs + 5 character refs; Flash = 10 object refs + 4 character refs. The "~6 sweet spot" is a house prior | Prevents overfilling multi-character / prop-heavy panels and makes reference assembly explicit |
| "Three shots" for a character turnaround | ~20–25 image assets per principal across turnaround / action / expression / variant sheets | Sets realistic bible scope |
| DSL skeleton: shot + character + action + setting + mood | Add `STATE` slot (expression + condition + wardrobe variation + held objects + eyeline + body tension) | Without it, panels render as visually correct but emotionally flat |
| Role-labeled refs will let the model isolate "camera angle" cleanly | Probably partial; abstract relational properties leak more than concrete visual ones. Frame as compositional skeleton transfer instead | Re-shapes the cinematography reference pack and prompt fencing strategy |
| LLM extracts state and directorial intent from script | LLM *structures* the director's stated intent; doesn't infer it | Reshapes the entire UI and architecture around direct manipulation |
| Midjourney wins decisively on style | Gap has narrowed; May 12, 2026 Arena snapshot puts `gpt-image-2 (medium)` at 1393±7 T2I and 1467±5 edits, while Midjourney remains useful for manual aesthetic exploration | Opens the closed-model-only path as a legitimate strategic option |
| Per-board compute cost is the bottleneck | A 345-image first-pitch test is roughly $14–83 in raw output cost depending on stack/quality; human art direction and review throughput dominate | Reframes the $200/board target around human time, not just generation count |
