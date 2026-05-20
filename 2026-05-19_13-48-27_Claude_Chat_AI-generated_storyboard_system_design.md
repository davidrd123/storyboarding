# AI-generated storyboard system design

Source: [Claude Chat](https://claude.ai/chat/1ee6f7d3-0ec8-4b65-bd32-5a9e40c1fa0e)
Extracted: 2026-05-19T20:48:27.310Z
🚀 Exported with [Save my Chatbot](https://save.hugocolin.com)!

---

## User

So just want to prepare thinking about this you should look up the capabilities of GPT image 2, I'm not that versed in film
But just thinking through what putting together a system that could do storyboards would require 
Obviously the weak part using Nano banana or openai's equivalent is style following but if we're willing to put that aside I mean in my mind the ideal thing would be if you already had artist renderings of characters and style and then conceivably were able to train a LoRA on a open source model and then use those generations as references but then it gets circular right because to train that Laura you probably need as many drawings of characters and scenes as you need for the storyboard in the first place But I mean if you had if you cared less about style and then you had some reference styles then you could do something like that
If you see in the Discord screenshots the artist's style there I dropped in those four images and had GPT image 2 create I guess name those characters and then create prompts and then some scenes based off them and you can see the style isn't exact but it's at least in the zone and we have high controllability 

So then it becomes maybe more like a markdown/workflow engineering task 

So just preparing for talking with Ben you know maybe even just a proto storyboard or if we can like decide on some you know I tried creating a couple scenes based on those characters but you know I guess understanding kind of like what the I guess maybe even listing out sort of the vocabulary you know essentially storyboards is a domain specific language like having that vocabulary set down and then understanding what we try to be controlling and then come up even with like a little test run

## Claude

Synthesizing GPT Image 2's storyboarding potential and capabilities

Synthesizing GPT Image 2's storyboarding potential and capabilities

Let me look up GPT Image 2's current capabilities first since you asked, then I'll work through the framework.

Architected storyboard workflow, DSL vocabulary, and circular dependency solution

Architected storyboard workflow, DSL vocabulary, and circular dependency solution

Good prep instinct — let me try to add value to each thread you raised.

### GPT Image 2 reality check (what's actually true now)

It launched April 21 with "thinking mode" — it reasons about structure before generating, which is exactly what helps for shot framing instructions. Key relevant capabilities for storyboarding:

- Multi-image reference input at high fidelity (preserves details automatically — no knob)

- Strong instruction following on long/structured prompts

- Face consistency across edits is "practical but not identity-locked" (so good for sketches across panels, not perfect for hero-shot continuity)

- 2K resolution, multiple aspect ratios including 3:2 / 2:3

- Editing endpoint with masks (inpaint/outpaint specific regions)

- ~$0.04–$0.35/image, ~30s–2min latency for complex prompts

The face-consistency-but-not-locked point matters: it means your "character sheet → use as reference" approach works, but you should expect 20–30% rejection rate per panel and plan for re-rolls.

### The storyboard DSL you'll want to enumerate with Ben

Storyboarding really is a constrained vocabulary. Roughly six axes a panel locks down:

**Shot scale** — ECU, CU, MCU, MS, MLS, FS, LS, WS, ELS, insert, two-shot/three-shot
**Camera angle** — eye level, high, low, bird's eye, worm's eye, Dutch, OTS, POV, profile
**Camera move (for animatic/notation)** — static, pan, tilt, dolly in/out, truck, crane, tracking, push-in, rack focus, whip
**Coverage role** — establishing, master, OTS reverse, reaction, insert, cutaway, transition
**Composition** — rule of thirds, leading lines, foreground occlusion, frame-within-frame, headroom/lookspace, negative space
**Continuity** — screen direction, eyeline match, 180° line, match-on-action

The reason I'd push for nailing this vocabulary first: it becomes the *interface* to your system. A shot prompt then has a deterministic skeleton: `[shot scale] [angle] of [character(s)] [action], [setting], [mood/lighting]` — and the workflow engineering becomes assembling that skeleton with the right reference images attached.

### On the circular dependency — I think you can break it

You're right that training a style LoRA needs 40–80 captioned images, which is basically a storyboard's worth of art. But the loop isn't actually closed if you do this:

**Don't train style. Borrow it.** Use a closed model + reference images to get style "in the zone" (as you saw). Pour the training-data energy into a different asset: a **character/world bible** in the chosen style — 6–10 images per principal character (turnarounds, expressions, signature poses), 3–5 images per recurring location, prop sheets for signature objects. That bible is maybe 30–50 images total, generated *with the closed model + the artist's hero refs*, then human-curated for "yes this is canon."

Then every panel prompt is: style refs + relevant character bible images + location plate + shot DSL + beat description. You're not asking the model to invent the character each time — you're showing it. That's how you get cross-panel consistency without training.

The LoRA becomes a *Phase 2* — after you've generated 200+ successful panels with the closed-model workflow, you have your training set basically for free, and you can train a real style LoRA that gives you 90% style fidelity and lets you move off the closed model. So the LoRA isn't the entry point, it's the graduation.

### Concrete test run to propose Tuesday

To make the conversation real, I'd come in with a 4–6 panel proof. Suggested structure:

1. Pick a tiny scene (one beat, one location, two characters) — Damaggio's style is great, you could even reuse those characters since you already have hero refs

2. Generate the bible: cowboy turnaround (3 shots), officer turnaround (3 shots), camel/well/ruins location plate (2 shots) — call this Phase 0

Write the scene as DSL: e.g.,

3. Panel 1: WS, low angle, two figures at well, ruins BG (establishing)

4. Panel 2: MS OTS over cowboy → officer (coverage A)

5. Panel 3: MS OTS reverse → cowboy (coverage B)

6. Panel 4: CU on officer, reacting (beat)

7. Panel 5: MS two-shot, cowboy grabs officer (action)

8. Panel 6: ECU on hands at the valve (insert)

9. Generate each, log which ones needed re-rolls and why

10. Bring the panels + the failure modes to the meeting

The failure log is honestly the most valuable artifact — it tells you exactly which controllability problems are real vs. solvable with prompt engineering.

### Strategic framing for Ben

I'd pitch it as two parallel tracks rather than a fork:

- **Track A (now)**: closed-model + reference-image workflow. Available today. Style ~70%, controllability ~90%. Ship pitches with this in weeks.

- **Track B (later)**: open-model LoRA trained on Track A's output corpus + the artist's hero refs. Style ~90%, full ownership, no per-image cost. Months out.

The real product isn't the model — it's the DSL, the bible-generation flow, and the panel-assembly pipeline. Those are durable regardless of which model you sit on top of.

Want me to draft an actual prompt template + a sample DSL spec for a panel? Or pull together the failure-mode taxonomy you'd want to log against? Either would be useful to walk in with.

## User

So when you say three shots for the cowboy turnaround how does the character Bible map onto something like this

## Claude

Reconciled abstract guidance with concrete character sheet example

Reconciled abstract guidance with concrete character sheet example

Honestly, looking at this Mike sheet — I undersold. "Three shots" was lazy. *This* is closer to the right density. Let me re-map:

### A complete bible entry per principal character

Probably three or four sheets, not three images:

1. **Turnaround sheet** — exactly the top row of Mike. 6 angles, neutral pose, locked costume. This is the identity anchor and the costume reference.

2. **Movement/action sheet** — exactly the bottom row of Mike. 4–6 signature poses (walking, running, idle, turning, looking back). Carries body language and silhouette.

3. **Expression sheet** — Mike is missing this and it's the one I'd add. 6–8 facial expressions tight on the head: neutral, surprised, angry, focused, scared, smirking, exhausted, determined. Critical for CUs and reaction beats — most panel failures will be here.

4. **Costume/state variants** (only if the script needs them) — bloodied, soaked, formal, disguise, etc.

5. **Bio block** — the yellow box on Mike's sheet. Not an image reference; it's prompt template fuel. Age, era, traits feed into the prose description on every panel prompt.

So a principal gets ~20–25 image assets total. A side character maybe just the turnaround + 3 expressions.

### Human-facing sheet vs AI-facing assets

Important distinction your Mike example surfaces: this sheet is great as a **review document** — labels, layout, all in one — but it's not the optimal shape for *feeding* to the image model. GPT Image 2 / Nano Banana Pro do best with clean, isolated reference images, not a composited grid with text labels on it.

So in practice you'd want both:

- **The composite sheet** (like Mike): for pitches, artist briefs, human approval, the "this is canon" sign-off

- **The atomized assets**: each pose cropped into its own unlabeled image, tagged with metadata in the filename — `mike_turnaround_3q_front.png`, `mike_action_running.png`, `mike_expression_surprised.png`

Then per panel, you don't dump the whole bible — you pick 2–4 relevant refs. CU reaction on Mike → pull `3q_front` + `expression_surprised`. Wide shot of Mike running from something → pull `action_running` + `full_back` for the silhouette. This keeps the reference signal focused and avoids confusing the model with irrelevant poses.

### What Mike actually proves

Worth flagging: if you generated Mike like this (looks closed-model-generated to me — consistent ink style, clean color), you've *already validated* the trickiest step. Producing a coherent character sheet in a chosen style is the hard part. The next test is whether slicing Mike up and using those slices as refs for a *new* panel (say, Mike crouching behind a car at night in Topanga) preserves the face and the jacket. That's the real proof-of-concept for the bible-driven workflow — and a great thing to demo to Ben.

Want me to sketch what an "atomized asset spec" looks like — naming conventions, metadata fields, what each asset needs to be useful at panel-generation time?

## User

Do you want to search to make sure that the image models actually do best with clean isolated reference versus a composite because things are always advancing so you might want to verify

## Claude

Reconsidered prior claims and corrected composite reference guidance

Reconsidered prior claims and corrected composite reference guidance

You were right to push back — I was wrong, or at least overstating it. Current guidance from both model camps:

**Nano Banana Pro actually recommends the composite sheet.** Google/Gemini's own guidance is to generate a single image containing multiple views (front, 3/4, side) and upload *that* as the reference — they call it giving the model "a complete 3D understanding of the character's head structure." Their storyboard workflow guide explicitly says: build the multi-angle sheet, then upload it as a reference for every frame. So the Mike sheet as-is is actually well-shaped for Nano Banana Pro. Cap is 14 reference images per call, practical sweet spot ~6.

**GPT Image 2 is more agnostic but emphasizes role labels.** It accepts up to 16 references. The repeated advice in OpenAI's and fal's prompting guides is to *label each input by role* in the instruction: "Image 1 is the character reference. Image 2 is the style reference. Image 3 is the location plate. Preserve face and jacket from Image 1. Borrow ink wash and palette from Image 2. Place in environment from Image 3." Whether the character ref is a composite sheet or a single hero shot matters less than naming what each input is for.

**So the revised picture:**

The Mike sheet works as a single reference upload, especially for Nano Banana Pro. You probably don't need to atomize it for the model's sake. Where atomization still helps:

- **Prompt assembly logic** — easier to programmatically pick "the running pose" if it's a tagged file, vs. asking the model to look at panel 7 of a labeled grid

- **Reference budgeting** — if you're already passing style + location + props, you may only have room for one character image, and a tight expression shot may serve a CU panel better than the full sheet

- **Specific edits** — if you want to change just the jacket color across the project, having an isolated jacket reference is cleaner

A practical hybrid for the Ben demo: keep the Mike-style composite as the canonical "character canon" upload, and also keep a small folder of atomized extracts for cases where a specific pose or expression matters more than the full sheet. Let the per-panel prompt assembler decide which to grab.

Also worth flagging from the search: both models reward **explicit "preserve" / "change" / "borrow" instructions** way more than I gave credit for. The pattern is `Preserve [face, jacket] from Image 1. Borrow [linework, palette] from Image 2. Generate [new scene description].` That's probably more leverage than tinkering with reference shape.

Good catch — would have walked into Tuesday with bad advice.

## User

So in your DSL you just had shot scale angle of character action setting and then mood / lighting where does the detailed description of character state happen

## Claude

Identified structural gap and repositioned character state as distinct DSL component

Identified structural gap and repositioned character state as distinct DSL component

Good catch — my skeleton was anemic on that exactly. Character state deserves its own slot, distinct from both identity (locked by reference) and action (the verb).

The cleanest division is:

- **Identity** = locked by reference image. Face, build, hair, signature wardrobe. Doesn't change panel to panel. Handled by the bible.

- **State** = specified in prose for this panel. Expression, physical condition, eyeline, body tension, costume variations from baseline (sleeves rolled, hat in hand, jacket open, blood on the cheek). What they're holding, where their attention is.

- **Action** = the verb. What they're doing in this beat.

State is the slot that turns a character standing on a reference sheet into a character *in this specific moment of this specific story*. It's also where most of the emotional content of a storyboard lives.

### Revised skeleton

```
SHOT: [scale] [angle] [movement if any]
SUBJECT: [character name — refs Image 1]
STATE: [expression + physical condition + wardrobe variations + 
 held objects + eyeline + body tension]
ACTION: [verb of this beat]
SETTING: [location + time of day + weather + state of place]
MOOD: [lighting direction + quality + atmosphere + tone]
COMPOSITION: [fg/mg/bg staging + framing + negative space + leading lines]
CONTINUITY: [link to prior/next panel, screen direction]
```

### What it looks like filled in (using your Damaggio cowboy)

```
SHOT: MCU, low angle, slight push-in
SUBJECT: Cowboy [ref: cowboy_bible.png]
STATE: Jaw set, dust on his face, sweat at the hairline, eyes
 narrowed and locked off-frame right. Scarf loosened.
 Hand resting on holster grip but not closed around it.
 Whole body wound tight but still.
ACTION: Holds his ground, watching.
SETTING: Beside the brick well, late afternoon, long shadows.
MOOD: Tense, anticipatory. Warm directional light from frame
 left, deep shadow on his off side. Dust haze in the air.
COMPOSITION: Cowboy occupies right two-thirds; his eyeline pulls
 composition to empty left third. Negative space on the
 left signals what he's watching without showing it.
CONTINUITY: Picks up from prior panel where officer pointed off-right.
```

### The bigger pattern this surfaces

State is also where your expression sheet and pose sheet earn their keep. When you write `STATE: jaw set, eyes narrowed, body wound tight` — that's a description. But you can *also* pass `expression_determined.png` and `pose_ready_stance.png` as supporting references with the role label "expression and posture reference." Now state is locked from two directions: prose describes it, atomized refs show it.

This is also why the expression sheet I mentioned earlier (the one Mike is missing) is actually the single highest-leverage asset in the bible. Identity is solved by the turnaround. Body language is solved by the pose sheet. But emotional beats — which are the actual *content* of most storyboards — live in the expression sheet plus the STATE block. Skimp on either and panels read as visually correct but emotionally flat.

Want me to take a swing at what a complete expression sheet spec looks like — the canonical set of emotions worth having on hand, and how to caption them so prompts can grab the right one?

## User

Yeah let's unpack what that might look like

## Claude

Architected tiered expression framework with metadata schema for storyboards

Architected tiered expression framework with metadata schema for storyboards

Here's how I'd think about it.

### What the expression sheet is solving

Two problems at once: (1) giving the model a tight head reference for CU and reaction beats where the turnaround is too zoomed out to be useful, and (2) capturing the *emotional vocabulary* of the character so a prompt can say "use expression_determined" and get a consistent look every time, not a new improvisation.

The unit isn't "an expression" — it's an entry in an emotional dictionary, captioned and tagged so it's retrievable.

### A canonical set, tiered

I'd structure it in three tiers. **Tier 1 is universal** — every principal needs all of these. **Tier 2 is genre-fitted** — pick 4–6 that match your storytelling palette. **Tier 3 is character-specific** — signature looks unique to this person.

**Tier 1 — universal (8):**

- Neutral / resting (the baseline, not a beat)

- Surprised / startled (sudden, eyes wide, mouth slightly open)

- Determined / focused (jaw set, eyes clear, locked)

- Angry / hostile (overt — flared, teeth showing or jaw clenched)

- Worried / concerned (brow furrowed, mouth tight)

- Amused / smirking (one corner of mouth up, eyes warm or sharp)

- Sad / grieving (eyes down or distant, mouth slack)

- Confused / questioning (brow asymmetric, head implied tilt)

**Tier 2 — for your western/adventure tone, I'd add (6):**

- Cold rage (suppressed — flat affect, eyes hard, micro-tension)

- Tactical / calculating (eyes scanning, no expression, present but assessing)

- Defiant (chin up, eyes locked, dare on the face)

- Pained but pushing through (jaw clenched against it, eyes narrowed)

- World-weary / resigned (heavy eyes, mouth slack, exhausted)

- Suspicious / wary (eyes narrowed but not angry — watching)

**Tier 3 — character signatures (2–4):**
For your cowboy this might be: *the dry sideways look*, *the moment-before-the-draw stillness*. For the officer: *the formal mask cracking*, *the parade-ground composure under fire*. These are the looks that make the character recognizable as *them*, not just any cowboy or any officer.

So ~16–18 expressions per principal. Side characters get Tier 1 only, maybe 6 of them.

### Naming and metadata

The asset is useless if the prompt assembler can't find it cleanly. Schema I'd use:

```
filename: cowboy_expr_cold-rage.png
character: cowboy
type: expression
label: cold-rage
intensity: 2/3
synonyms: suppressed-anger, slow-burn, contained-fury
visual: flat affect, eyes hard and unmoving, jaw set, no movement
use-for: confrontation hold, moment-before-violence, dressing-down
opposite: amused
related: determined, tactical
```

The `synonyms` field matters more than it looks — when an LLM is assembling the prompt from a beat description like "Davies seethes at the order," you want it to find `cold-rage` whether the scene description says "seething," "furious but controlled," or "barely holding it together." Tag generously.

`use-for` is the directorial hint — these are the storyboard beat patterns where this expression fits. Helps the assembler pick the right one without re-deriving it.

### Format conventions for the images themselves

- **Angle**: 3/4 front, eye-level. Most expressive and most flexible as reference. Eyes facing camera, neutral eyeline (model will retarget per panel).

- **Crop**: tight headshot — top of head to mid-chest. Enough neck/shoulder for context but no environmental noise.

- **Lighting**: flat, even, neutral. The bible is not where mood lives. Mood gets specified per panel; the bible needs to be a *clean signal* the model can read regardless of the target panel's lighting.

- **Background**: solid neutral (paper white or warm cream to match the style's substrate). No environment.

- **Style**: matched to the chosen art style (Damaggio-style ink wash for your case).

The key insight: the expression sheet should look like a *catalog page*, not a panel. The model needs to read the expression cleanly. If you bake in moody backlighting and atmospheric haze, you've made the reference noisy — the model will try to preserve all of that.

For 2–3 of the highest-traffic expressions (probably neutral, determined, surprised), I'd also generate a profile variant. Profile reactions are common in shot/reverse-shot coverage and the 3/4 ref doesn't always retarget cleanly.

### How it plugs into a panel prompt

Back to the STATE block from earlier — now it's doing two jobs:

```
SUBJECT: Cowboy [ref: cowboy_bible_3q.png + cowboy_expr_cold-rage.png]
STATE: Cold rage held in. Jaw set, eyes hard on the officer, no
 movement. Dust on his cheek. Hat shadowing the upper half
 of his face. Hand near holster but not on it.
```

The prose describes state. The reference *shows* state. Belt and suspenders — when they agree, the model locks. When the prose contradicts the reference (e.g. you pass `expr_smirking` but write "jaw set, furious"), the prose usually wins but you get drift. Worth knowing for debugging.

### One thing this surfaces strategically

Building the expression sheet *is itself* the hardest test of whether the closed-model + reference approach works for your style. You're asking the model to generate the same character 16 times with controlled emotional variation while preserving the linework and ink wash. If that works clean, your whole pipeline works. If expressions drift in style or identity, you've found the weak link before committing to a whole storyboard.

I'd actually suggest making *one principal character's expression sheet* the literal Tuesday demo. It's small, scoped, generates fast, and the result tells you whether to proceed with the workflow approach or whether you really do need a LoRA. More diagnostic than producing a few finished panels.

## User

I gave your filled in DSL text to GPT image 2 chat, it wasn't really continuity with the previous generation but this is what I got which is interesting for reference

## Claude

Assessed image quality while diagnosing character continuity drift problem

Assessed image quality while diagnosing character continuity drift problem

Honestly, this is a productive failure — and the failure is the diagnostic.

Standalone, the panel is really good. The style is dead-on Damaggio: the duotone wash, the cross-hatch on the brick, the loose linework on the desert haze, the way the ruins fall off into atmosphere. Composition is on the nose — frame-right placement, the negative space pulling left to signal what he's watching, the well anchoring foreground, ruins doing midground work. State reads cleanly: the set jaw, the hand at the gun without gripping it, eyeline locked off-frame right. The model translated the prose almost completely.

But your instinct is right — this is not your cowboy. Different face structure, different hair, a different actor playing the role. The model invented a new protagonist from scratch because nothing told it who the protagonist *was*. That's exactly the load-bearing case for the bible, surfaced for free.

A few smaller drifts worth noting: it reads more eye-level than low-angle (camera angle is one of the things prose alone doesn't lock reliably — it's a spatial thing the model interprets loosely without a reference for *what eye-level looks like in this composition*); "dust on his face" became "stubble and grit," close but not exact; the warm directional light is softer than called for. None of these are dealbreakers, but they show where prose is approximate and where references would tighten things up.

The genuinely interesting follow-up test, if you want one before Tuesday: run the same DSL prompt again with one of your earlier four-panel images attached as the character reference, role-labeled as "Image 1 is the character reference for the cowboy. Preserve face structure, hair, scarf, and silhouette from Image 1." See if continuity resolves. That tells you, cheaply, whether the bible workflow holds — or whether GPT Image 2's identity preservation hits a ceiling that demands the LoRA path.

Either result is good news for the meeting. If it works, you can show Ben "prose alone" vs "prose + reference" side by side — concrete evidence that the workflow is the unlock and the LoRA is Phase 2. If it doesn't work, you've found the actual limit and Tuesday becomes about scoping the LoRA properly with that constraint understood.

Also worth flagging: the fact that *style* held this cleanly without a style reference image attached is its own data point. The model has clearly internalized "European bande dessinée western ink wash" as a recognizable category. So the work the bible needs to do is mostly identity, less so style — which is the cheaper of the two problems to solve.

## User

So it makes sense to try to eventually just run through all the variations and see what it can do easily and what it has trouble with because then maybe even for things like camera angle we could try having clear examples of what that should look like and see if it could actually separate that out when we say borrow camera angle from image three etc? (Using GPT image 2)

## Claude

Validated systematic testing approach for DSL elements and visual reference abstraction

Validated systematic testing approach for DSL elements and visual reference abstraction

Yes, and I think this is actually the most valuable thing you could prep for Tuesday — turning the whole question into an empirical exercise rather than an argument about model capabilities.

The mental model I'd use: every DSL slot has a *translation reliability* from prose alone, and the experiment is mapping that landscape. My priors for GPT Image 2:

**Probably translates cleanly from prose** (no reference needed):

- Style category ("ink wash western," "European bande dessinée")

- Action verb ("walking," "drawing his pistol")

- Mood adjectives ("tense," "melancholy")

- Time of day, weather

- General setting class ("desert with ruins")

**Probably ambiguous from prose** (reference might help):

- Specific shot scale boundaries — the MS/MCU/MLS distinctions are genuinely fuzzy and the model defaults to "comfortable medium" a lot

- Camera angle — your panel landed at eye level when prose called for low. Geometry is relational and hard to specify

- Coverage geometry (OTS specifically — the over-shoulder framing is a precise spatial relationship)

- Foreground occlusion / frame-within-frame (compositional depth tricks)

- Specific lighting direction (which side, how harsh, what bounce)

- Eyeline precision (slightly off-camera vs. dead-on vs. far off-frame)

**Definitely needs reference** (the ones you've already identified):

- Character identity

- Specific location continuity (the *same* well across panels)

- Style fidelity to a specific artist's exact line quality

- Specific prop continuity

### On whether the model can actually isolate "camera angle" from a reference

This is the open question and I want to be honest about my uncertainty. The clearest evidence we have from the prompting guides is that GPT Image 2 handles *concrete* role-labeled transfers well — "preserve face from Image 1," "borrow palette from Image 2," "use jacket from Image 3." Those are object-level extractions.

Camera angle is more abstract — it's a *relational* property between viewer and subject, not a thing in the image. My honest guess is that it'll work better than pure prose but won't be perfectly clean. The model will probably also pull in some of the reference's subject placement, composition, or lighting along with the angle, even when told not to. So the role label has to fight harder.

The trick that I think makes it more likely to work: have your camera-angle references be *in the target style*, with subjects that are *different enough from your scene* that the model can't accidentally substitute them. A low-angle reference shot of a totally unrelated subject — say, a French legionnaire pointing at the sky in a Damaggio panel — is easier for the model to abstract from than a low-angle shot of another cowboy at a well, which is too similar to the target and will leak.

### What a cinematography reference pack would look like

If this works, you'd build a one-time asset:

- **Shot scales** (8 refs): ELS, LS, FS, MLS, MS, MCU, CU, ECU — one canonical image each, in target style, subjects deliberately varied so they don't bleed

- **Angles** (6 refs): eye level, low, high, Dutch, bird's eye, worm's eye

- **Coverage patterns** (4 refs): OTS A, OTS B (reverse), two-shot, profile-over-profile

- **Composition tricks** (4 refs): foreground occlusion, frame-within-frame, deep stack, silhouette

~20 references, built once, reused across every project. Per panel you pull the 1–3 that matter. A CU reaction panel might attach: `character_ref` + `expression_ref` + `CU_scale_ref` + `style_ref` = 4 refs, well under budget.

### The test design that earns its keep Tuesday

I'd structure it as a 2×2:

| | Prose only | Prose + reference |
| --- | --- | --- |
| **Character identity** | (baseline drift you already saw) | Same DSL + cowboy ref attached |
| **Camera angle** | (does prose alone hold the angle?) | Same DSL + low-angle ref attached |

Four generations. Maybe an hour of work. Each cell answers a real question:

- Top-left: how bad is drift without references? (You have this — bad)

- Top-right: does reference fix identity? (The likely-yes case, validates workflow)

- Bottom-left: how bad is angle drift without references? (You have hints — eye-level instead of low)

- Bottom-right: does reference fix angle? (The genuinely uncertain case, where you learn something new)

The bottom-right is the most interesting cell because nobody knows the answer with confidence. If it works, the cinematography pack idea is validated and the whole DSL approach gets dramatically more powerful. If it doesn't — if camera angle just won't reliably extract from a reference — then you know prose has to do that work and you adjust the DSL to lean harder on spatial description ("subject's chin level with the horizon line, sky filling top two-thirds of frame" instead of "low angle").

Either result is meeting-quality. The methodology itself is also valuable to show Ben — you're not guessing about model capabilities, you're measuring them. That posture is more credible than any single demo.

One small note on cost: GPT Image 2 high quality runs ~$0.20-$0.35/generation. A 2×2 plus a few re-rolls is well under $5 and you have a real evidence base.

## User

Do you want to search again and see if you can ground that speculation

## Claude

Reconsidered speculation and plotted evidence-gathering strategy

Reconsidered speculation and plotted evidence-gathering strategy

Fair push. Let me actually check.

Synthesized evidence supporting speculation with calibrated expectations

Synthesized evidence supporting speculation with calibrated expectations

Good — and the answer is mixed, in a useful way.

**What the evidence supports:**

- OpenAI's own prompting guide (via fal) explicitly lists framing/composition as preservable properties in edits: "Preserve: face, identity, pose, lighting, framing, background, geometry, text, layout." So the model has some internal handle on these as separable qualities.

- Style/palette/edge-treatment transfer between very different subjects is well-documented and reliable. "Borrow palette and material mood, do not borrow the objects" is a standard pattern.

- Pose transfer between subjects is a documented workflow that works well — multiple tools build entire products around it.

**What complicates my speculation:**

One quote from fal.ai's guide is the most directly relevant signal, and it slightly cuts against my pitch: *"Reference images like this work because the palette, edge treatment, and silhouette language are concrete instead of abstract."* The implication is that GPT Image 2's reference handling is stronger for concrete visual properties (color, line quality, texture) than for purely abstract relational ones.

PixVerse's guide is similarly suggestive: it treats "camera distance, angle, subject placement" as things you state *clearly in the prompt*, not as things you extract from references.

And here's the gap I couldn't fill: I found no documented example of the specific workflow "use Image 3 to lock camera angle, with a different subject, in fresh generation." Style transfer between different subjects? Documented. Pose transfer between different subjects? Documented (often with specialized tools). Framing preservation in *editing* the same image? Documented. The exact "borrow only the camera angle" pattern? Not in the public guides I found.

**What this means for the test plan:**

The 2×2 is still the right design, but I'd recalibrate expectations on the bottom-right cell. My honest revised prior: probably *some* lift from the reference but not as clean as identity preservation, and prone to subject/composition leakage that requires careful negative instructions ("do not borrow subject, location, or props from Image 3").

There's also a refined version of the test that might work better, based on what the evidence does support. Instead of asking the model to abstract "low angle" as a concept, frame it as compositional skeleton transfer — closer to how pose transfer works:

> "Image 3 is a compositional reference. Use the same camera position relative to subject, the same horizon line height in frame, and the same vertical proportions. Do not borrow the subject, costume, location, props, or style from Image 3 — only the spatial layout."

That's a more concrete framing of the same idea, and it leans on the pose-transfer paradigm rather than abstract-concept extraction. The model is better at "make a new image with the same spatial geometry" than "make a new image with the same abstract angle property."

**One more thing worth noting from the search:**

A consistent piece of advice across multiple sources is using "preserve" and "do not borrow" instructions much more aggressively than I'd been suggesting. The leakage problem is real and documented — when you give the model a reference, it tends to pull in more than you wanted. The mitigation isn't fewer references, it's more explicit negative constraints per reference. So the prompt structure becomes:

```
Image 3: compositional reference
 Borrow: camera position relative to subject, horizon height,
 vertical proportions, framing
 Do NOT borrow: subject, costume, location, props, style,
 palette, lighting, or any other visual element
```

Verbose, but the documentation is consistent that this kind of explicit fencing earns its keep.

So: speculation was directionally right but I overstated confidence on the specific abstraction. Test is still worth running, with calibrated expectations and the compositional-skeleton framing as the version most likely to work.

## User

So if we were to separate this into different stages that need to be validated it seems like the first thing well okay so we have like dsls and then we also need to essentially get our character Bible and the character Bible especially the expression sheet and then we need location plates and signature objects I guess, and then we have our DSL for the shot itself then there is the preserved borrow do not borrow part that is essential and refers to the associated images so they're actually needs to be labeling of the images and intelligent selection in front of that prompting

But to even have those images in the first place we need the starter seed of style and then like the real work is then in generating our Bible and to generate our Bible then we also need to be prompting as well right so I guess is that interactive and discovering how to do that but we probably need The preserve borrow do not borrow and then just in iterative playground to kind of discover how specifically to do this? Am I missing anything

## Claude

Validated phased pipeline architecture and identified missing operational layers

Validated phased pipeline architecture and identified missing operational layers

You've got the dependency structure mostly right. Let me reflect it back and flag what I think is missing.

### Your dependency chain, slightly reordered

The way I'd phase it:

**Phase 0 — Style seed + prompt grammar (the smallest fast loop)**
The first thing to validate isn't even "can we generate a panel," it's "can we reliably get *any* image in the target style with explicit preserve/borrow grammar working." One reference image (a Damaggio panel), one role-labeled prompt, generate a simple test image, iterate until the grammar is reliable. This should be a few hours, not weeks. The output isn't an asset — it's *knowing how the model responds* to your prompt structure. This is the playground discovery you described, but tightly scoped.
**Phase 1 — Bible generation**
Once you can reliably produce *something* in style, the bible becomes a methodical exercise. Generate turnaround → action sheet → expression sheet for each principal. The process itself surfaces failure modes (some expressions will be hard, some angles will drift) and refines the grammar further. You learn which preserve/borrow phrasings actually hold across many generations of the same character.
**Phase 2 — Mini-sequence test**
The 6-panel proof we discussed earlier. Bible exists, grammar works, now stress-test the whole pipeline on a real beat. This is where continuity across panels gets tested, where the DSL gets exercised, and where you discover whether the workflow actually composes or whether it falls apart at sequence-length.
**Phase 3 — Operational scale-up**
Real storyboard volume. This is where the things you haven't built yet start to bite — captioning systems, prompt assemblers, QA criteria, continuity tracking.

### What I think you're missing

A few things that are implicit in what you said but worth making explicit:

**1. The captioning layer for the bible itself.** Each generated bible asset needs metadata: character name, asset type (turnaround/expression/pose), specific tag (3q_front, cold-rage, idle-stance), notes on what it shows. Without this, "intelligent selection" has nothing to select against. This is just a filename convention + a small JSON or sidecar file per asset. Tiny work, but if you skip it the system can't scale.

**2. The beat-to-DSL translator.** Someone (or something) has to read a treatment or script and break it into panels with DSL slots filled in. This is the actual creative work of storyboarding — the storyboard artist's brain. For Phase 2 you'll do this by hand. For Phase 3 you might use an LLM to do a first pass that humans edit. It's a real step in the pipeline you haven't named.

**3. The prompt assembler.** This is what you called "intelligent selection." It's a function that takes a panel's DSL spec, looks up which bible assets are relevant (this character's expression sheet, this location's plate, etc.), and assembles the final prompt with reference attachments and preserve/borrow/do-not-borrow blocks. Could be a manual checklist for Phase 2, must be code for Phase 3.

**4. Continuity tracking across the sequence.** If Panel 5 has the officer's coat buttoned and Panel 12 has it open with no beat justifying it, that's a continuity error. Across 60 panels this gets unmanageable by eyeball. You eventually need a state ledger — "as of Panel N, character X is in state Y." Premature to build in Phase 0–1, but worth knowing it's coming.

**5. QA criteria and re-roll triggers.** With 20–30% expected re-roll rates, "good enough" needs definition. Is the character recognizable? Is the framing right? Is the style on-brand? You'll develop this implicitly while doing Phase 1 — pay attention to *why* you're rejecting outputs, because that becomes the QA rubric.

**6. The art-direction question upstream of style.** I'd lock this with Ben Tuesday: are you committing to a specific living artist's style (Damaggio), an "in the spirit of" style that's deliberately not anyone's, or per-project styles where each pitch has its own visual identity? The architecture works for all three, but the recruiting/legal/relationship work downstream is very different. The Discord screenshots showed Ben thinking "find an artist willing to join us" — that's a meaningful commitment that should be made consciously, not by drift.

### One nuance on your chicken-and-egg

You're right that grammar discovery and bible generation feel circular, but I'd argue they're sequential with a fast Phase 0 — *not* deeply entangled. The grammar discovery only needs to be good enough to produce one reliable image in style. Once that's working, you batch-produce the bible with that grammar. You'll refine the grammar *while* making the bible, but you don't need a complete final grammar before starting bible work.

The genuinely co-discovered thing is more about *which DSL slots benefit from which kinds of references*. That's what the 2×2 test from earlier was probing. That discovery happens during Phase 2 (mini-sequence), not Phase 0.

### The shape of Tuesday's conversation, given this

I'd frame it for Ben like:

> "Here's the pipeline architecture. Phase 0 we can do this week — call it a day of playground work to validate the grammar. Phase 1 is a 2–3 week effort to build the bible for one project. Phase 2 is a week of mini-sequence tests. Phase 3 — actually shipping pitch storyboards — is contingent on Phase 2 holding up.
> Three decisions we need from you: (1) which artist's style or whether we're going original, (2) how heavily to invest in Phase 0 tooling vs. just doing the work manually, (3) the scope of the first real test project that defines what 'good enough for pitches' means."

That gives him a real decision space rather than a vague "let's explore this." The phases also give a clean way to kill the project early if Phase 0 or Phase 1 reveal the model just can't carry the load — which is a feature, not a bug.

Want me to take a swing at a written-up version of any of these — the Phase 0 grammar discovery protocol, or the bible captioning schema, or a one-pager you could actually walk Ben through?

## User

Could the beat to DSL translator benefit from a user interface where there's iterative refinement? I mean presumably you can bracket areas in the script and then try to hone in on this 
I mean so we have kind of a state machine where I mean the state across the script could be assembled without knowing the storyboard right 
Continuity tracking across sequence could then be happening are having sort of a checker 
Right now I'm just looking at the beat to DSL, and feeling like that's potentially an iterative discovery process right cuz I'm seeing the script hierarch lead this you know decomposed into its various Acts into the scenes and I'm assuming that like storyboards will belong to a scene I'm trying to narrow down where the difficult work is and feeling like if that can happen actually through saying you know you try to maybe it isn't just a One-Shot thing right and maybe they should have a rough pass with a llm kind of guesses or proposes various scenes and or maybe you discuss piercing you're intuitions and then they're sort of a first pass and then you get candidate panels so I'm seeing a visual interface for this where we're keeping history and candidates and mapping on to the script help me think this through further

## Claude

Validated architectural insight separating state extraction from image generation

Validated architectural insight separating state extraction from image generation

The insight that script state can be extracted upstream of any imagery is genuinely important, and I think you might be undervaluing how big it is. Let me build on it.

### The architectural shift you're proposing

What you've actually identified is that the storyboard pipeline has two cleanly separable problems that have been getting tangled together:

1. **Story comprehension** — what's happening, to whom, where, when, in what state

2. **Story visualization** — rendering a moment of that story as an image

Until now everything we've been discussing tangled these together. The DSL had character state in it, location in it, action in it — all of which are *derived from the story*, not chosen freely. By making state extraction its own upstream artifact, you're admitting that the storyboard tool's first job is *to understand the script*, and the second job is *to draw it*. Those are different jobs.

This is a real architectural win because:

- The state ledger is queryable independently. "What was the cowboy wearing in Act 2, Scene 4?" becomes a database query, not a re-reading of the script.

- Continuity checking becomes mechanical. "Does the rendered Panel 47 match the state at Beat 31?" is a vision-model task.

- Multiple storyboard passes can share the same state ledger. If you re-storyboard a scene, you don't re-derive the state.

- Edits to the script propagate. Change a line in Act 1, the affected state cascades forward and the storyboard surfaces what needs re-doing.

### What the state ledger actually contains

I'd structure it as a hierarchical model:

```
Script
├── Act 1
│ ├── Scene 1.3 [Desert well, late afternoon]
│ │ ├── Persistent state at scene start:
│ │ │ Characters present: Cowboy, Officer
│ │ │ Location: brick well in ruins, dust haze
│ │ │ Time: late afternoon, low warm light
│ │ ├── Beat 1.3.1 — Cowboy points off-frame
│ │ │ Cowboy state: scanning, tense, hand near holster
│ │ │ Officer state: standing parade-rest, watching
│ │ │ Costume delta from previous beat: none
│ │ │ Visual emphasis: distant threat off-right
│ │ ├── Beat 1.3.2 — Officer asks "Are you certain?"
│ │ │ ...
```

Each beat has:

- A short description of what happens

- The state of each character (emotional + physical + costume deltas)

- Location/time state

- What's just changed since the last beat

- A "visualization candidate" flag (does this beat want a panel? maybe more than one?)

The beat *might or might not* have an associated panel. That's a separate creative decision. Some beats are exposition that don't need visualizing. Some get multiple panels. The state exists regardless.

### The iteration loop you're describing

The "rough pass, human refines, get candidates" flow you sketched is exactly right. I'd shape it as four nested loops:

**Loop 1 (slowest, most strategic):** Script → scene breakdown
The LLM proposes the act/scene boundaries and a synopsis of each. Human accepts, splits, merges. Tens of decisions per script.
**Loop 2:** Scene → beats with state
Within a scene, the LLM extracts beats and proposes the state at each. Human refines. *This is where most of the creative state-tracking happens.* Hundreds of decisions per script.
**Loop 3:** Beats → panel selection
For each beat, decide if it gets a panel, how many, and what each emphasizes. This is the storyboard artist's taste call. The LLM can suggest defaults ("this beat probably wants 2 panels — establishing and reaction") but the human is driving. Hundreds to thousands of decisions per script.
**Loop 4 (fastest, most iterative):** Panel → image candidates
Each panel slot gets multiple generated candidates. Human selects, re-rolls, edits the DSL. This is where image gen lives.

The loops compose. Editing a beat (Loop 2) can invalidate panel selections (Loop 3) which invalidates candidates (Loop 4). The system needs to handle this cleanly — probably with explicit "this state changed, here's what's affected downstream" warnings rather than auto-regenerating everything.

### What the UI actually looks like

A few principles, then a sketch:

**The script is the spine.** Everything else is derived from script position. Scroll the script, the rest of the view updates to that position.

**State is always visible at any script position.** A persistent panel showing "as of this line: who's here, where, what state, what just happened, what's about to happen." Click any state element to see how it was derived.

**Candidates are visual.** Each panel slot is a small carousel showing multiple generated options plus the currently-selected one. You can re-roll, edit DSL, or pick a different candidate per slot.

**History is non-destructive.** Every rejected candidate is preserved. Every state revision is preserved. You can roll back any decision without losing parallel work.

**Continuity issues are inline annotations.** When the checker finds something — "Panel 47 shows the cowboy's right arm uninjured, but Beat 31 established a shoulder wound" — it surfaces as a flag on that panel, not a separate report.

Sketch of layout:

```
┌─────────────────────────────────────────────────────────────────────┐
│ SCRIPT (scroll spine) │ STATE AT CURSOR │ PANEL SLOTS │
│ │ │ │
│ Act 1 │ Location: well │ ┌──┬──┬──┐ │
│ Scene 1.3 │ Time: late aft. │ │○ │◉ │○ │ │ ← carousel
│ Beat 1.3.1 ● │ Present: Cow, Off │ └──┴──┴──┘ │ for this
│ ▶ Beat 1.3.2 ●● │ Cowboy: cold rage │ DSL ⌄ │ beat
│ Beat 1.3.3 │ Officer: resigned │ Re-roll │
│ Beat 1.3.4 ● │ Costume: as 1.3.1 │ Continuity ⚠ │
│ │ Just happened: ... │ │
│ Scene 1.4 │ About to: ... │ │
└─────────────────────────────────────────────────────────────────────┘
```

The dots next to beats indicate "this beat has panels" (○ = empty slot, ● = has selected panel, ●● = has multiple panels in sequence).

### What's harder than it looks

Three honest difficulties I'd flag:

**State derivation is genuinely hard.** Scripts don't always make state explicit. "Mike enters the room" — is he angry? bleeding? dripping wet from rain? The LLM will infer from context and often guess wrong. The human review step in Loop 2 is doing real work, not just rubber-stamping. Plan for it.

**The "which beats want panels" call is taste-driven and hard to automate.** A good storyboard isn't every beat panelized — it's the *visually charged* beats. Reactions, decisions, reveals, action. An LLM can propose but the human is making real creative decisions. Don't try to automate this away.

**Iteration across scopes creates churn.** If you re-derive Scene 1.3's state after editing the script, every panel below it might need re-evaluation. You need an "invalidation graph" that marks downstream artifacts as stale rather than silently regenerating them. This is a real engineering problem if the tool gets serious.

### On whether to build this for Tuesday

Honestly — no, and I'd be careful about pitching too much tool to Ben. The risk is that the conversation becomes about *building the tool* rather than *validating the workflow*. The MVP for the meeting is still Phase 0 (style + grammar) and a small Phase 1 demo (one character's bible). Even Phase 2 (mini-sequence) doesn't need this tool — it can be done in a spreadsheet plus a folder of images.

But I'd absolutely sketch this architecture as the *destination*. The framing: "Here's where this naturally goes if it works. We can start with a spreadsheet, but the moment we have a second project we'll want this." That positions the tool as inevitable rather than speculative, and gives Ben a sense of the eventual product surface without committing engineering resources prematurely.

The thing I'd actually want to demonstrate Tuesday, given everything we've discussed, is the *state ledger as a deliverable*. Take one scene from a real script, hand-derive the state ledger for it, and show how cleanly the panels fall out of that. Even without a tool, the *separation of state from rendering* is the conceptual unlock — and you can demonstrate it on paper.

Want me to take a swing at what a hand-derived state ledger for one scene actually looks like, end-to-end, in enough detail to be usable as a demo artifact?

## User

So to what degree are there free choices made by the storyboard artist from the script 
Because you're saying the LLM will infer from context, presumably the storyboard artist is then just making something up? Who is telling them what it should look like is it just like making up things that look good and it's actually figured out downstream once they start making the movie? 
And I've lost track of the dependency of the character in world Bible and how that relates to this is there actually a circular dependency or iteration between the two as wellAnd just to note Ben is a successful commercial director who has good foundation to move into movies so if he is in the loop providing input we should really factor that in
I mean we should picture him as a either direct user of the system all the time or as providing key input whenever needed right cuz this is for him to pitch

## Claude

Reframed Ben as creative director, not passive user, reshaping system architecture

Reframed Ben as creative director, not passive user, reshaping system architecture

You're catching real sloppiness in how I framed this earlier. Let me correct it, because it changes the architecture.

### What the storyboard artist actually decides

In professional practice, the storyboard artist makes very few autonomous creative choices. The script tells you *what happens*. The director tells you *how it should be shot*. The artist is rendering the director's vision, not inventing one.

A working note from a director sounds like: "this scene is slow, his face fills the frame for a long time before he says anything, then a hard cut to the wide reveal." That single sentence contains shot scale, pacing, cutting rhythm, and emotional emphasis. The artist draws what the director said. There's craft in *how* to draw it well, but the creative direction is upstream.

For pitch storyboards — which is Ben's actual use case — the director isn't just describing what they see; the pitch storyboard *is the director showing the room what the movie looks like in their head*. The visual choices ARE Ben's choices, completely.

### So who is the LLM inferring from? — I was wrong

My earlier framing of "LLM extracts state from script" was the mistake. If a script says "Mike enters the room" and you ask an LLM what it should look like, the LLM doesn't know — it'll make up something plausible. That's content-generation defaulting, not directing.

What you actually want: when Ben hits that line, he says (or types) "Mike enters wary, low light, we see him from inside the room, silhouetted in the doorway." Now the LLM has actual directorial intent. The state ledger captures "Mike: wary, silhouetted in doorway, from inside POV." The DSL captures the shot. The image renders Ben's vision.

So the LLM's job isn't inferring intent from sparse script. It's **structuring Ben's directorial input efficiently and mapping it back to script position.** The script provides the spine (what happens, who's there, geography). Ben provides the directorial layer (mood, emphasis, framing intent, cutting rhythm). The system encodes both.

### The circular dependency with the bible is real and that's fine

Yes, real circularity, and it's the normal rhythm of pre-production:

- Pre-bible: Ben reads the script, forms a vision, gathers reference

- Bible v1: Ben + system externalize that vision — characters get faces, locations get looks

- First storyboard pass: scenes get rendered with bible v1. Some things work, some don't.

- Bible v1.5: refinements emerge from making panels. "Actually the officer should look more weathered."

- Storyboard pass 2: informed by tightened bible

- Bible expansion: as new scenes need new costumes, locations, props — bible grows

In film, the character/world bible is a living document. The first version is informed by script reading and reference; later versions are informed by trying to make panels. The circularity is a feature — the work of making the storyboard *is itself* the work of figuring out what the visual world is. Don't try to fully solve the bible before storyboarding starts; assume it co-evolves.

What the system needs to support: editing the bible without breaking everything downstream, and surfacing "panels affected by this bible change" when something updates. Versioning matters.

### Ben as the primary user changes the design substantially

This is the most important thing in your message and I want to give it the weight it deserves.

**The interface should be directorial, not technical.** Ben thinks in feel and emphasis ("more wound up, like he's about to break"), not in DSL slots ("STATE: cold-rage 3/3"). The system should accept directorial input and translate to DSL behind the scenes. He shouldn't be learning "MCU low-angle slight push-in" — he should be able to say "tight on him, low, slow creep in" and have the system know what that means.

**Speed beats precision.** Pitch work means hundreds of iterations in a week. The tool should optimize for "director throws ideas at it" not "engineer carefully constructs prompt." Latency budget per interaction: seconds to a minute, not five minutes.

**Conversational refinement is the real input mode.** Real director notes sound like "no, more like he's tired but doesn't want to show it." That should be a valid input. The system translates that into something like "expression: stoic mask over exhaustion, shoulders: slight micro-tension, eyes: brief glaze." The director shouldn't have to do that translation himself.

**The bible becomes Ben's aesthetic fingerprint over time.** Across projects, Ben accumulates a personal library — his way of doing villains, his way of lighting interrogation scenes, his recurring archetypes. The system stops being "a tool for this pitch" and becomes "Ben's directorial vocabulary, externalized and reusable." That's a fundamentally different scale of value than one project's storyboards.

**Polish matters because pitches are competitive.** The output isn't just "correct storyboards" — it's pitch-quality artifacts that make the room *feel the movie*. Style consistency, mood, atmosphere are not optional; they're the product.

### How this reframes Tuesday

Less "let's figure out the workflow," more "let's figure out what kind of creative collaborator this should be." A version of the question worth asking Ben directly:

> *How much do you want to direct the panel-by-panel choices yourself versus have the system make defaults you can override? Are you the director using a fast tool with AI underneath, or are you the director giving notes to an AI assistant who comes back with options?*

The architecture is different in each case:

- **Direct manipulation model:** like Photoshop + AI. Ben drives every decision, the system makes them fast and renders them. Best when Ben has strong opinions and wants control.

- **Junior storyboard artist model:** Ben gives high-level direction, system proposes options, Ben selects and corrects. Best for when Ben is moving fast across many scenes and wants leverage on his time.

Both are real products. Best version is probably a blend — direct manipulation when Ben wants it, AI-proposals-with-approval when he doesn't have time. But the *primary mode* matters for the design.

### One more thing worth flagging

If this is for Ben to pitch with, the *audience* matters too. Studio execs and producers reading pitch books have seen thousands of them. What makes a pitch storyboard stand out isn't accuracy to the script — it's *the unmistakable feel of a specific director's voice*. The tool's job, ultimately, is to amplify Ben's directorial fingerprint, not to neutralize it into "generic competent storyboards."

That's a real design constraint: every decision in the system should preserve or sharpen Ben's distinctiveness, not average it toward a generic style. The bible captures his choices. The state ledger captures his interpretations. The output should look like *Ben made this*, not like *an AI made this*.

That framing is also probably how to position the product if it ever becomes one. Not "AI storyboards" — "your directorial vision, externalized."

## User

Okay but you know Ben also was working on you know again the fair trade was his attempt to do sort of a text to image model training site for artists that artist didn't pick up on 
And I think he'd be willing to specify you know granular detail to the shots
What you said is more clear but I want to sort of return back to what we said initially with the character Bible world Bible and kind of run it forward from the beginning again

## Claude

Synthesized workflow phases integrating bibles, DSL, and Ben's technical direction

Synthesized workflow phases integrating bibles, DSL, and Ben's technical direction

Good context on FairTrade — that tells me Ben's been working in this space and is comfortable with detailed technical specification. So the direct-manipulation model is right. He's not waiting for AI to make creative proposals; he's directing every beat and willing to specify granular detail. The system's job is to make his specifications fast and the rendering reliable.

Let me run the whole picture forward, integrated.

### The premise

The product is a pipeline for generating pitch-quality storyboard books in a chosen art style, with character and location continuity, driven by Ben's directorial choices. The closed-model + reference workflow is the engine. The DSL, state ledger, and bibles are the structured inputs that make it controllable. Ben is the primary user and the source of all creative intent.

### Phase 0 — Style seed and prompt grammar (Day 1)

Start small and tight. Take 3–5 hero images from the chosen artist (or eventually a recruited collaborator) as the style anchor. Run a series of single-image generation experiments to validate the prompt grammar:

```
Image 1: art style reference
Borrow: line quality, ink wash treatment, palette, paper texture
Do NOT borrow: subject, composition, scene
Generate: a simple new scene description
```

The goal isn't to produce a finished panel — it's to learn whether "borrow style only" actually works, how much it leaks the source subject, and how aggressive the do-not-borrow language needs to be. A day of iteration tells you whether the grammar is reliable enough to commit to the whole approach.

Output: a validated grammar template and a confidence level on style preservation.

### Phase 1 — Character bible (Week 1–2)

Now build the cast. For each principal character, three sheets:

**Turnaround sheet** — 6 angles, neutral pose, locked costume. Identity anchor.
**Action/pose sheet** — 4–6 signature poses. Body language and silhouette.
**Expression sheet** — 14–18 emotional states (the tiered set we worked through). The highest-leverage asset for reaction beats.

Each sheet is generated with the style grammar from Phase 0, with Ben directing the character's look at every step. "His hair is longer, more matted." "Make the jacket more worn." "The expression for cold rage isn't right — less obvious anger, more flat affect." This is where Ben's character vision gets externalized.

Each asset gets atomized into individually labeled image files with metadata:

```
cowboy_turnaround_3q-front.png
cowboy_expression_cold-rage.png 
cowboy_pose_idle-stance.png
```

Plus a sidecar JSON describing what it shows, synonyms, recommended use cases. Naming discipline is critical — it's what makes downstream automation possible.

Side characters get a stripped-down version: turnaround + 6 expressions, no action sheet.

### Phase 2 — World bible (Week 1–2, parallel)

Same discipline, different subjects:

**Location plates** — each recurring location, 2–4 angles capturing the geography. The brick well, the ruins, the camp, the desert. These are establishing references for *the same place* across panels.

**Signature object/prop sheets** — recurring props that need consistency: the pressure gauge, the cowboy's specific revolver, the officer's cavalry sword. Each gets its own clean reference image.

By the end of Phases 1 and 2, you have a *library* — Ben's externalized vision of this specific story's visual world, captioned and queryable.

### Phase 3 — Script + state ledger (Week 2–3)

Now bring in the script. Ben works through it scene by scene with the system, dictating directorial intent. The LLM's job is to structure what Ben says into the state ledger format:

```
Scene 3.2 — Well, late afternoon
 Persistent state:
 Location: brick well + tent canopy + distant ruins
 Time: late afternoon, low warm directional light, dust haze
 Present: cowboy (since 3.1), officer (since 3.1)
 
 Beat 3.2.1 — Officer admits sabotage
 Cowboy state: shifting to cold rage. Wound healing on right
 shoulder since 2.4 — sleeve torn there.
 Officer state: resigned, parade-rest broken, eyes down.
 What just happened: officer's confession line.
 What's about to happen: cowboy moves on officer.
 Visual intent (Ben): "I want to feel the temperature change.
 Hold on the cowboy first, very still.
 Then a hard cut to the officer, smaller
 in the frame than he was a beat ago."
```

The state ledger captures both *what* (mechanical state) and *Ben's directorial intent* (how he wants the moment to feel). It's queryable: "show me everything that's true about the cowboy at Beat 3.2.1." It's editable: change a beat, downstream beats get flagged as potentially stale.

Crucially, the state ledger is *script-locked but rendering-independent*. It exists whether or not you ever generate a panel.

### Phase 4 — Beat selection (Week 3)

Ben walks through the state ledger and decides which beats deserve panels. Most beats don't — they're dialogue or transition. The visually charged beats — reactions, decisions, reveals, action moments — get one or more panel slots.

Output: an ordered list of panel slots, each tied to a specific beat in a specific scene, with Ben's directorial intent attached.

### Phase 5 — Panel rendering (Week 3–4)

For each panel slot, the system assembles the actual generation prompt by combining:

1. **State** from the ledger (who, where, condition, just-happened, about-to-happen)

2. **Ben's directorial intent** for this specific panel (shot scale, angle, emphasis, mood)

3. **Bible references** — the relevant character/location/prop assets, selected based on what's in the beat

4. **Style reference** — the locked style anchor

5. **Preserve/borrow/don't-borrow grammar** — explicit role labels and fencing for each reference

A rendered prompt looks roughly like:

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
 Reference Image 3: well_location_plate.png
 Preserve from Image 3: well geometry, ruins position, dust haze
MOOD: warm directional light from left, deep shadow on off-side of face,
 atmospheric tension
STYLE:
 Reference Image 4: damaggio_style_anchor.png
 Borrow from Image 4: line quality, ink wash, palette
 Do NOT borrow from Image 4: any subject, composition, or scene elements
COMPOSITION: cowboy frame right, eyeline pulls compositionally to empty
 left third, negative space signals what he's watching
CONTINUITY: picks up from Beat 3.1.4 where officer pointed off-right
```

Generate 3–4 candidates. Ben picks, re-rolls, or edits the prompt directly. The history is preserved — every candidate stays around in case the selected one needs to be revisited.

### Phase 6 — Continuity check and assembly

A vision-model checker runs across selected panels in sequence, validating against the state ledger. "Panel 47 should show torn right sleeve (wound from Beat 2.4) — actual image shows intact sleeve. Flag." Ben reviews flags, accepts or re-rolls.

Final pass: arrange panels in script order, lay out the book, polish.

### How the bibles and state ledger interact, exactly

This is the question you flagged about circular dependency, now resolved cleanly in the integrated picture:

- **Bibles are upstream of state ledger.** They establish what characters and locations *look like at baseline*.

- **State ledger is upstream of panels.** It establishes what's true at any given script position.

- **Panels reference both.** The bible provides the identity; the state ledger provides the moment.

- **Iterating on either propagates downstream.** Bible update → potentially affects panels referencing it. State ledger update → potentially affects panels at and after that beat.

The circularity that confused us earlier comes from working on multiple phases in parallel. If you treat them as sequential — bible first, state ledger second, panels third — and accept that *late discoveries flow back into earlier artifacts*, the system stays coherent.

### What Ben is actually doing, end to end

Step out of the architecture and look at his actual workflow:

1. Reads the script, forms a vision, gathers reference

2. Builds the bible with the system — directs character look, location feel, style anchor

3. Walks through the script with the system, dictating directorial intent per beat

4. Selects which beats become panels

5. Per panel: reviews proposed prompt, refines, generates candidates, picks

6. Reviews continuity flags

7. Final assembly into pitch book

Steps 2 and 3 are the bulk of the creative work. Step 5 is where the volume is. Steps 1, 4, 6, 7 are quick passes.

The system's job is to make Steps 2, 3, and 5 *fast and granular* — Ben dictates, system captures, system renders. Not "AI proposes, Ben approves" — "Ben directs, AI executes." That's the FairTrade learning applied: don't ask the creative party (Ben, or the artist) to relinquish control; build the tool around their actual workflow.

### What this means for the FairTrade angle separately

Worth flagging: this architecture is artist-respecting in a different way than FairTrade was. FairTrade asked artists to consent to training. This approach uses references from an artist's work *within a closed-model context window*, not for training. The eventual Phase 2 LoRA path would re-raise the consent question — and that's the point at which recruiting an artist collaborator (the "FairTrade with way less heartbreak" framing from your Discord) actually becomes structurally necessary. Until then, the workflow doesn't depend on artist participation, which is both a feature (no adoption blocker) and a constraint (no true style ownership).

That's a real strategic question for Ben to consider: is the goal to ship pitch books fast with closed-model rendering, or to eventually own a trained style with an artist collaborator? Both are viable, but they imply different commitments and timelines.

## User

Right so questions to ask the number two yeah directing character look location field style anchor I guess having a lookbook or visual references would help tremendously hear I guess? 
This is the biggest unknown currently I mean mid journey is much better for style yeah building the Bible with the system feels like the tough part

## Claude

Reconciling Midjourney's aesthetic edge with narrowing competitive gaps

Reconciling Midjourney's aesthetic edge with narrowing competitive gaps

The lookbook insight is important — that's actually how directors traditionally communicate vision to crews. Let me check current state on the Midjourney-vs-controllability tradeoff before responding to the rest, because that's the crux of the technical question.

Synthesized lookbook strategy with hybrid workflow approach

Synthesized lookbook strategy with hybrid workflow approach

The Midjourney assumption is worth updating — the gap has narrowed more than most people realize. Let me put the lookbook idea and the model question together because they're connected.

### On the Midjourney prior

As of right now (May 2026), the picture is more nuanced than "Midjourney wins on style":

- On Image Arena Elo, GPT Image 2 is currently rated higher than Midjourney V7 overall (~1512 vs ~1270). That's overall — Midjourney still wins specifically on cinematic lighting and "default aesthetic intelligence," but GPT Image 2 has closed a lot of ground.

- Midjourney V7's character reference (now "Omni Reference") is still the strongest pure character-consistency tool available, but GPT Image 2 with role-labeled refs is comparable when explicit preserve/borrow grammar is used.

- The widely-documented pattern among professionals now is the hybrid: **Midjourney for mood boards and aesthetic exploration, GPT Image 2 for production work where controllability matters.** That's basically your workflow exactly.

- One real caveat: Midjourney has no public API and ongoing IP lawsuits (Disney/Universal, Warner Bros). For commercial pitch use, this is meaningful risk to scope.

So the practical answer is: don't pick one model. The bible-creation phase has two stages, and they want different tools.

### The lookbook insight is the key unlock for bible creation

You're right that this is the biggest unknown, but I think you've already half-solved it by mentioning the lookbook. Let me develop it.

A director's lookbook is *exactly* the structured input that bible creation needs. Frames from films for cinematography reference. Photography for mood/light. Concept art and illustrations for visual style. Wardrobe from period films. Locations from documentaries. Casting references — "he has the energy of [actor in film]."

This is how directors already communicate vision to crew. Ben presumably already does this. What we're proposing is that the lookbook becomes the **structured input to a generation pipeline**, not just a deck shown to a DP.

Concretely, the lookbook gets atomized by role:

```
lookbook/
 style/
 damaggio_panel_01.jpg (the art style anchor)
 damaggio_panel_02.jpg
 characters/
 cowboy/
 face_energy_01.jpg (Mads in The Hunt — that intensity)
 costume_reference.jpg (period western wardrobe)
 silhouette_ref.jpg
 officer/
 ...
 locations/
 well_reference_01.jpg (the location's geographic feel)
 mood/
 lighting_reference_01.jpg (the warm desert dusk feeling)
```

Now bible creation isn't "Ben describes characters from scratch and the model invents them." It's:

> "Image 1: face energy. Image 2: costume reference. Image 3: art style. Generate a turnaround sheet for this character — borrow face presence and bone structure from Image 1, costume vocabulary from Image 2, rendered in the style of Image 3. Do not borrow specific identity from Image 1 (we want similar energy, not the same person); do not borrow subject from Image 3."

This is a much more tractable problem than "generate me a cowboy." It's *synthesis of structured references*, which is exactly what GPT Image 2's role-labeled grammar was built for.

### The two-stage workflow for the bible

Given the model comparison:

**Stage A: Style and character exploration (Midjourney's wheelhouse)**
Ben uses Midjourney with his lookbook references to explore "what could the cowboy look like in this style?" Mood-board pace, fast iteration, exploratory. Output: a chosen hero image of the character that captures the right energy and style.
**Stage B: Bible build-out (GPT Image 2's wheelhouse)**
Take the chosen hero image from Stage A as the canonical character reference. Use GPT Image 2 with role-labeled grammar to systematically generate:

- The 6-angle turnaround (preserve face, hair, costume from Stage A hero; vary angle)

- The pose sheet (preserve identity; vary action)

- The expression sheet (preserve identity; vary emotional state)

Stage B is methodical, controllable, reproducible. Stage A is creative, exploratory, taste-driven. They're different jobs and benefit from different tools.

The handoff between stages is the key: Stage A produces *the choice* (this is what the character looks like). Stage B produces *the library* (this character in all the configurations the bible needs).

### Why bible creation is genuinely the tough part

You're right that it is. Three reasons:

1. **Style + identity + variation, all at once.** Every bible asset has to be in the chosen style, recognizably the same character, and a specific variation (this angle, that expression, that pose). Holding all three constant while varying the fourth is the hardest case for current image models.

2. **It's a one-shot product.** A single bad turnaround pose isn't a panel you can re-roll — it's a foundational asset that propagates into every downstream panel. The quality bar is higher than for individual panels.

3. **The lookbook → bible synthesis is creative work, not just technical work.** Ben has to make real choices about how the lookbook references combine. The system supports him, but doesn't replace him.

So the bible-creation phase isn't a few days of grinding through generations. It's probably **the most creatively important phase of the whole project**, and worth treating as such. Ben should expect to spend real directorial time on it.

### A reframed Phase 1

Knowing what we know now:

**Phase 1a — Lookbook curation (Ben-led, days)**
Ben assembles the lookbook from his existing references plus new pulls. Organized by role: style refs, character refs (per character), location refs, mood refs. This is a familiar job for him.
**Phase 1b — Hero image exploration (Midjourney, days)**
For each principal: explore in Midjourney with character + style references from the lookbook. Iterate to a hero image that captures the character. This is fast, creative, aesthetic.
**Phase 1c — Systematic bible build-out (GPT Image 2, ~1 week per principal)**
For each character: take the hero image as canonical reference. Generate turnaround, action sheet, expression sheet using role-labeled grammar. This is the methodical work.
**Phase 1d — Location and prop plates (GPT Image 2, parallel with 1c)**
Same pattern: lookbook references → hero image → plate variants. Could probably be faster than character work since locations don't have expressions or poses to enumerate.

### One last thing on legality

For pitch storyboards specifically, the IP risk profile is friendlier than for consumer products — pitch books circulate internally in studio meetings, they're not distributed or sold. But it's worth Ben thinking about because:

- If a pitch sells, the storyboards may end up referenced in production materials

- Using Midjourney commercially under the current IP cloud has real, if small, downside

- Closed models like GPT Image 2 have clearer commercial terms

If risk-conscious, the entire pipeline can be GPT Image 2 + Nano Banana Pro, accepting somewhat lower default aesthetics in exchange for cleaner commercial posture. The lookbook approach works there too. It's worth raising as an explicit decision with Ben rather than letting it default.

