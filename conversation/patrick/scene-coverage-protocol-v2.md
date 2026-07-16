\---

name: scene-coverage-protocol
description: "Agnostic workflow for generating full editorial coverage of a scene from an anchor image — phases, gates, shot manifest, and review loop."
type: protocol
tags: \[production\_workflow, image\_generation, coverage, editorial]
status: draft
---

# Scene Coverage Protocol

A repeatable workflow for generating the full suite of shots an editor needs to cut a scene. Works from either an anchor image or a written scene brief. Agnostic — works across any style, project, or generation tool.

\---

## The Director's Lens

This protocol is modeled on how directors approach coverage in live-action and animation production. Think of the output not as a collection of images, but as a **storyboard** — a set of panels that tell the story of each beat with enough visual coverage that an editor could cut the scene from them alone.

**How a director thinks:**

1. **Assets and characters first.** Before any scene coverage begins, a director locks the character designs and key asset model sheets. This is the animation pipeline principle: establish what everything looks like in the medium *before* putting it into any scene. In generative terms, this means character sheets and asset model sheets must be approved and available as image inputs before the first scene shot is fired. Skip this and every shot drifts independently.
2. **Wide shots of each key beat before going tighter.** Directors shoot the wide establishing shot of each story beat first — it locks the geography, the lighting grammar, and the style for everything that follows. Tighter shots are then composed *within* that established world. In generative terms: fire the wide shot of each beat, approve it, and use that output as the image input anchor for the medium shots and close-ups of the same beat. The approved wide is the ground truth.
3. **Beat structure drives manifest order.** The shot manifest is not a flat list — it is ordered by beat, and within each beat by scale (wide → medium → close-up → insert). Each wider shot output can chain into tighter shots as an image input. This chaining is what gives the kit its geographic and stylistic coherence — shots feel like they're in the same world because they are generated from the same world.
4. **Fill out with an editor's eye.** Once hero shots (the key beat wides and the character moments) are locked, ask: what does the editor need to cut this scene? Wide to cut from, medium for dialogue and action, close-up for emotion, insert for product/detail punctuation. The editor's question is: "can I cut this scene from these frames?" If any shot type is missing, the kit has a gap.

**The storyboard test:** Lay all approved shots in story order. Can you read the scene? Do you understand each beat and where the camera is at all times? If yes, the coverage kit is complete.

\---

## How It Works

**Input:** An anchor image OR a written scene brief / creative direction document. Both are valid starting points.
**Output:** A coverage kit — a set of generated shots at different angles, focal lengths, and scales that are geographically coherent with each other and with the source material. The kit functions as a production storyboard.

**The core constraint:** Every shot in the kit must be grounded in the same world — spatially, semantically, and stylistically. Whether that world comes from an image or a written description, once the geography is established in Phase 2 it is fixed. This is not a collection of independently generated images; it is a set of views into the same world.

**Image-input mode:** The anchor image is the primary spatial reference. Phase 2 reverse-engineers the geography from what the camera can see.

**Text-only mode:** The scene brief, beat file, or creative direction document replaces the anchor image as the world source. Phase 2 constructs the geography from descriptive language — inferring spatial positions, landmarks, and relationships from the written text. When the brief doesn't specify a spatial detail, a deliberate decision is made and documented in Phase 2. That decision becomes canonical for the session. All coverage prompts must then reference the same landmarks at the same positions, consistently across every shot.

\---

## Storyboard-First Path (Alternative)

When generating coverage frame-by-frame, each shot starts fresh — the model has no memory of other shots, so geographic drift compounds across the batch. The storyboard-first path inverts this: instead of generating individual frames, generate a **multi-beat storyboard panel** first. The whole location, multiple characters, and multiple beats are generated simultaneously in a single context — the model establishes the entire world at once.

This is the same principle as generating all five Seans together in SC08: doing it in one go keeps things in memory rather than splitting. The storyboard page becomes the location-coherent world document from which individual frames are extracted and finished via img2img / style transfer.

**The workflow:**

1. Write a storyboard-format prompt — multiple panels, multiple beats, one page — rather than individual shot prompts
2. Pass the approved wide shot or style anchor as Image 1. Describe each new panel in text within the prompt. Do NOT generate text-only (no reference image) — text-only genesis gives camera freedom but produces an output that diverges from the approved visual grammar. Some composition influence from the reference is expected; iterate if the bleed is too strong
3. Generate the storyboard as a single image. This establishes location grammar, lighting, spatial relationships, and character positions all at once in one shared context
4. Approve the storyboard for location and beat coverage — not for final style or quality. This is a planning artifact, not a deliverable
5. Expand each panel to full 16:9 individually. For each panel: describe the shot explicitly in text + pass the storyboard as image input for style context. End the prompt with: "Use the style and environment from the reference image. 16:9 aspect ratio." **Do NOT** ask the model to "reproduce the left/right panel" — it returns a new storyboard instead of a single frame
6. The Phase 3–6 workflow still applies — it now governs the style-transfer / final polish layer

**Panel labeling (confirmed):** Label each panel in the storyboard prompt with a short name (e.g., "PANEL A: WIDE LANDING", "PANEL B: MEDIUM GOODBYE"). The model renders the labels as visible text in the storyboard output, creating named callout anchors. Expansion prompt template: "Expand PANEL A: WIDE LANDING from the reference storyboard to a standalone full 16:9 frame. Use the style and environment from the reference image. No text, no labels, no captions — clean image only. 16:9 aspect ratio." The label targets the correct panel without re-describing content. The "no text/labels/captions" clause is required — omitting it produces an output with the label text rendered into the frame.

**When to use it:**

* Two or more shots needed simultaneously — prior frame-by-frame runs drifted, or no anchor exists yet
* Multiple characters or beats must share the same world in one generation context

**When not to use it:**

* Only one shot is needed — a storyboard adds overhead without benefit
* A strong anchor image already exists and individual genesis + img2img is working cleanly

The phases below describe the standard path. For the storyboard-first path, Phase 2 (world inventory) is completed from the storyboard output rather than from an anchor image, and Phase 4 prompt generation operates against individual cropped panels.

\---

## Phase 0 — Asset Prep

> \\\\\\\*\\\\\\\*Gate: Must be complete before any scene coverage begins. This phase cannot be skipped.\\\\\\\*\\\\\\\*

Before any scene shot is generated, all principal characters and key visual assets (vehicles, props, branded environments) must have approved reference sheets available as image inputs. This is the animation pipeline principle applied to generative coverage.

**Character sheets:** For each principal character appearing in the scene, an approved full-body character sheet must exist — locked design, approved style, correct rendering quality. The character sheet is the sole identity anchor for all scene shots featuring that character. Without it, each shot will drift independently.

**Asset model sheets:** For key non-character assets (vehicles, branded booths, hero props), an approved model sheet must exist — showing the design from enough angles to reconstruct it in any scene context.

**Check:** List every principal character and key asset in this scene. For each one, confirm the approved reference path exists. If any is missing, generate it now before proceeding to Phase 1.

|Asset|Reference path|Approved?|
|-|-|-|
||||

**If a reference does not exist:** Generate the character sheet or model sheet first, get approval, file it in the project vault, then proceed. Never attempt scene coverage without approved references for all principal subjects.

\---

## Phase 1 — Scene Context Intake

> \\\\\\\*\\\\\\\*Gate: Human or LLM must complete this before any generation begins.\\\\\\\*\\\\\\\*

Everything downstream depends on knowing what the scene is *about*, not just what's in it. The world inventory tells you what's in the frame. Scene context tells you what *matters*.

**Before filling in the fields below — search the vault.**
If this image belongs to a project with a vault, look for any documentation that deepens the creative and story understanding of the input image before answering from observation alone. Relevant documents include: scene beat files, character rules, look development docs, brief or concept docs, any copy or VO tied to this scene. The vault often contains the *why* behind what the image is showing — the emotional brief, the product obligation, the subtext the director intended. Pull that context in first. If no vault exists, proceed from observation.

Fill in the following:

**Scene purpose:**
What is this scene doing in the larger story? What beat does it carry?

**Emotional register:**
What should the audience feel watching this scene?

**Subtext:**
What is happening beneath the surface — thematically, tonally, or narratively? What does the camera need to communicate that the dialogue or action doesn't say directly?

**Commercial or product obligations:**
Are there specific products, logos, or branded elements that must be visible and legible? At what scale?

**Character intent (if applicable):**
What does the character want in this moment? What detail in the frame reflects or contradicts that?

**Insert candidates:**
Based on the above — what in this scene needs to be seen at detail level to serve the story, the brand, or the subtext? These become required inserts.

\---

## Phase 2 — World Inventory

> \\\\\\\*\\\\\\\*Image-input:\\\\\\\*\\\\\\\* Anchor image.
> \\\\\\\*\\\\\\\*Text-only:\\\\\\\*\\\\\\\* Scene brief, beat file, or creative direction document.
> \\\\\\\*\\\\\\\*Output:\\\\\\\*\\\\\\\* A spatial grammar document that all subsequent shots draw from.

Parse the input systematically. This is a fill-once step — all coverage prompts pull from it as shared constraints.

**Text-only sourcing note:** When no anchor image exists, construct the world inventory from the written source. Infer spatial positions, depth relationships, and landmark locations from descriptive language in the brief. When the brief doesn't specify a spatial detail — where exactly a landmark sits, what's in the background — make a deliberate decision and document it explicitly in the table below. That decision is canonical for the session. Every coverage prompt must reference the same landmarks at the same positions you established here. Do not re-derive or re-infer geography per shot; it must be fixed in Phase 2 and reused consistently.

**Spatial landmarks:**
List every major identifiable element in the frame and where it sits (foreground / mid / background, left / center / right).

|Element|Depth|Position|Notes|
|-|-|-|-|
|||||

**Geographic relationships:**
Describe spatial relationships between landmarks. "The arch is in the foreground center; the ferris wheel rises behind it center-right; the Bay View building roof occupies the mid-ground spanning left to right."

**Implied off-frame space:**
What does the image suggest exists outside the frame? (A road leading off-left implies more of the scene in that direction; a crowd implies a stage behind camera, etc.)

**Lighting direction and time of day:**
Where is the light coming from? Hard or soft? What's the shadow grammar?

**Camera position and angle:**
What height is the camera at? What angle to the ground plane? What focal length does this feel like?

**Style and rendering register:**
What aesthetic world does this image live in? (This is the style lock for all derived shots.)

**Insert candidates (from Phase 1):**
Confirm which insert candidates are actually present and legible in the anchor image.

\---

## Phase 3 — Shot Manifest

> \\\\\\\*\\\\\\\*Input:\\\\\\\*\\\\\\\* World inventory + scene context.
> \\\\\\\*\\\\\\\*Output:\\\\\\\*\\\\\\\* A prioritized table of shots to generate, ordered for generation sequence.

**Manifest ordering principle — wide before tight, beat by beat:**
Order the manifest in generation sequence, not story sequence. Within each story beat: wide establishing shot first, then mediums, then close-ups and inserts. Fire and approve the wide for each beat before generating tighter shots of that beat. The approved wide output then becomes available as a chained image input for its medium and close-up descendants.

This mirrors how directors approach coverage: lock the geography and style at wide scale, then go tighter with confidence. Tighter shots generated from an approved wide are geographically anchored to that world — they cannot drift spatially because they were derived from it.

**Chaining column:** The manifest table includes a "Chain input" column. For each shot, note which earlier output (if any) should be used as the image input anchor — either the Phase 0 character/asset sheet or the approved wide shot of the same beat. Leave blank for shots that generate from the original anchor image or from text only.

**Editorial contrast and variety — required, not optional:**
Before locking the manifest, ask: does an editor have enough contrast to cut with? A coverage kit that is all the same focal length, all frontal, all at the same scale is not a kit — it is a collection of similar images. The manifest must deliver deliberate contrast across three axes:

* **Focal length range:** Extreme close-up, medium, and wide establishing must all be present. Do not stack shots at the same distance.
* **Camera angle variety:** Frontal, profile, OTS, rear 3/4, dutch, worm's-eye — shoot the back of the subject, not just the face. Rear-facing and non-face angles are often the most editorially subversive and the most valuable for cutting.
* **Motion register (if applicable):** Static and kinetic shots should both be present — a locked frame and a frame that implies movement cut differently and should both be in the kit.

Apply this check before any shot fires: lay the manifest on the table and ask — *wide vs. tight? Face vs. back? Static vs. kinetic?* If any axis is missing, add a shot before proceeding. Contrast and variety are as much a first-class requirement as geographic coherence.

### Tier 1 — Required Coverage

The minimum an editor needs to cut the scene. Do not drop these — if a required shot fails, find another approach, not another tier.

The shot type is mandatory. The execution is not. Use the scene context and subtext from Phase 1 to direct *how* each required shot is framed — where the camera sits, what's emphasized, what's in the foreground. A wide shot is required; which wide shot tells the right story is a creative decision.

|#|Beat|Shot Type|Description (world-specific)|Chain input|Derivable?|Insert?|Status|
|-|-|-|-|-|-|-|-|
|1||Wide establishing||Anchor image / text|Yes / No / Partial||Pending|
|2||Medium||Wide output from same beat|Yes / No / Partial||Pending|
|3||Close-up||Wide or medium output|Yes / No / Partial||Pending|
|4||Insert: \[element]||—|Yes / No / Partial|Yes|Pending|

**Derivability flag key:**

* **Yes** — can be generated directly from the anchor image; the necessary geometry is present or inferable
* **Partial** — camera angle requires inferring off-frame geometry; generation may hallucinate new space
* **No** — requires a new source image from a different camera position; flag before generating

**When to chain a wide output as image input:**
Use the approved wide shot of a beat as the image input for its medium/close-up descendants when: (1) the tighter shot is spatially derived from the wide (same geography, closer in), and (2) the wide output carries the style and lighting you want to preserve. Do not chain blindly — if the wide output has a flaw (wrong character pose, misplaced landmark), generate the tighter shot from the original anchor instead and describe the geometry in text.

### Tier 2 — Creative Coverage

> \\\\\\\*\\\\\\\*Gate: Human reviews and approves this list before batch generation.\\\\\\\*\\\\\\\*

Shots beyond required coverage — cutaways, special angles, visually striking compositions suggested by the specific world in this anchor image. Also includes editorially useful supporting shots (reaction shots, transitional cuts, etc.).

For each entry, include a brief rationale: why does this shot serve the scene given the context from Phase 1?

|Shot Type|Description (world-specific)|Creative rationale|Derivable from anchor?|Status|
|-|-|-|-|-|
|||||Pending|

**Start with scene context — ask these first:**

* What is the scene trying to communicate at this moment — narratively, emotionally, commercially?
* What is the subtext, and which camera position best reveals or reinforces it?
* What does the audience need to feel here, and does this angle deliver that?
* What would be missing from the editorial kit if this shot weren't included?

**Then consider what the world geometry supports:**

* Reflections or surfaces that create natural mirrors or frames-within-frames
* Depth compression opportunities (telephoto that stacks distant landmarks)
* Silhouette angles (backlit geometry, characters against sky)
* POV shots implied by character position in the anchor image
* Rack focus candidates (clear foreground/background separation)
* Aerial or low-angle reads that the world geometry supports

\---

## Phase 4 — Per-Shot Prompt Generation

> \\\\\\\*\\\\\\\*Input:\\\\\\\*\\\\\\\* Shot manifest row + world inventory.
> \\\\\\\*\\\\\\\*One prompt per shot. Each prompt must reference world inventory constraints.\\\\\\\*\\\\\\\*

**The core mechanic — spatial remapping through the new lens:**
A Director Mode camera command ("pull back to wide," "drop to low angle") tells the model *where* to move the camera. It does not tell the model what it would *see* from there. That gap is what causes geographic drift and hallucination. The world inventory is the fix: use it to explicitly describe what the new angle would reveal — which landmarks move to foreground, which recede, what enters the frame from off-screen, what the depth relationship between elements becomes. Think of it as answering the question: *if the camera were here, what would we actually see?* That description, drawn directly from the world inventory, is what gives the model enough information to reconstruct the angle credibly rather than invent a new world.

In the absence of specific human shot requests, the per-shot prompts are the default shotlist — Phase 3's manifest defines what needs to be covered, and Phase 4 translates each row into a generation-ready prompt.

### Prompt template (per shot)

```
Title: \\\\\\\[scene-shottype-vXX]
Source image: \\\\\\\[anchor image path — omit for text-only coverage]

\\\\\\\[Director Mode camera command — where is the camera moving and how]

\\\\\\\[Spatial remapping — what would we see from this angle, drawn from world inventory:
  which landmarks are now foreground vs. background,
  what enters frame that was previously off-screen,
  what is the depth relationship between key elements]

\\\\\\\[Lighting and style lock — pulled from world inventory]

\\\\\\\[Any scene-context obligations — product legibility, character beat, subtext note]
```

**Text-only prompt note:** Without an anchor image, the spatial remapping block carries more weight — it is the only geometry the model has to work from. Be more explicit than you would with an image input: name every landmark present in the shot, state its depth and position relative to other landmarks, and describe light direction and environment in full. The world inventory you built in Phase 2 is your sole source of truth for these descriptions — do not improvise new geometry per shot.

**Rules:**

* Every prompt must name at least two world inventory landmarks as spatial anchors
* The spatial remapping block is mandatory for any shot that changes camera position — it is what prevents geographic drift
* Insert prompts describe the detail, not the whole scene — "a close-up of \[element]", not re-describing the full environment
* For shots flagged Partial or No derivability: add an explicit note in the prompt about what off-frame geometry is being inferred or invented
* Style anchor block from the project's look file appended to every prompt

**Generation sequence — do not fire everything at once:**
Phase 4 prompts are written for all shots, but they are not all fired simultaneously. The correct sequence mirrors the director's approach:

1. **Fire all wide/establishing shots first** (one per beat). Wait for results, evaluate, approve the best wide for each beat.
2. **Update the manifest** — record the approved wide output path as the chain input for that beat's medium and close-up descendants.
3. **Fire mediums and close-ups** using the approved wide outputs as image inputs where the chain column specifies. Character sheets from Phase 0 are used for character identity alongside the wide output.
4. **Fire inserts last** — they are standalone and do not depend on tighter shot approval.

This sequence trades some speed for geographic and stylistic coherence. The approved wide is the only image that can anchor a tighter shot to the exact world that was established — not the original anchor image, which is a reference, not an approved output. The wide output IS the world.

\---

### Per-shot review checklist

After each result, evaluate against all six dimensions. Coverage-specific brief is consistent across the kit:

**Coverage brief (applies to every shot):**

* Geographic coherence — does this shot feel like it's in the same world as the anchor image?
* Camera/framing match — does the shot type and focal length match the manifest description?
* Continuity — does lighting, time of day, and style match the other shots in the kit?
* Editorial utility — is this shot actually cuttable? Enough static framing, right duration register?
* Hero legibility — does the intended subject read clearly at this focal length?
* Subtext fidelity — does this shot communicate what the scene context said it needs to communicate?

**Standard 6-dimension evaluation (from generation-review-loop skill):**
Prompt Fidelity / Preservation Fidelity / Style Lock / Scene Hierarchy / Story Service / Creative Brief Fidelity

### Per-shot outcomes

|Outcome|Action|
|-|-|
|Passes coverage brief + 6 dimensions at 80%+|**File it** — mark Approved in manifest, log output path|
|Single dimension failing, fix is clear|**Iterate** — delta prompt, fire again|
|Same dimension failing across 2+ targeted attempts|**Hold** — move on, return after rest of batch is reviewed|
|Held shot still failing after 2 more attempts|**Drop** — find an alternate angle that covers the same editorial need|
|Derivability was Partial/No and geometry hallucinated|**Assess** — does the hallucinated geometry serve the scene? If yes, file it. If no, drop and replace with a different angle.|

### Batch triage

After all shots are reviewed:

1. File approved shots immediately — log output path in manifest
2. Identify held shots — re-batch together
3. Identify dropped shots — propose replacement angles before re-batching
4. Tier 2 (creative) shots are first to be dropped; never drop Tier 1 without a replacement

\---

## Phase 6 — Coverage Completeness Check

> \\\\\\\*\\\\\\\*Gate: Human reviews before closing the coverage session.\\\\\\\*\\\\\\\*

The final editorial sanity pass. A technically approved individual shot doesn't guarantee a cuttable kit.

**Checklist:**

* \[ ] Wide / medium / close-up all present and approved
* \[ ] All identified inserts present and approved
* \[ ] Shot transitions are covered — can the editor move from wide to close without a jump cut?
* \[ ] Lighting and style are consistent across the full kit (compare all approved selects together)
* \[ ] All Phase 1 commercial/product obligations are met
* \[ ] Subtext shots (if any) are present — the detail shots that carry the scene's emotional undercurrent
* \[ ] Creative tier: are the surviving creative shots actually adding value, or are they redundant?

**If gaps exist:**
Identify which shot type is missing, write a targeted prompt, and fire a single additional generation. Do not re-batch the whole manifest.

\---

## Shot Type Vocabulary

> \\\\\\\*\\\\\\\*Placeholder — to be populated from shot deck reference captions.\\\\\\\*\\\\\\\*

Standard shot types and their framing grammar, for use in Per-Shot Prompt Generation (Phase 4). Each entry will include: shot name, focal length range, typical subject scale in frame, and editorial purpose.

|Shot Type|Focal Length|Subject Scale|Editorial Purpose|Director Mode prompt (mutation / spatial command)|
|-|-|-|-|-|
|Extreme wide / establishing|14–24mm|Subject occupies <10% of frame; environment dominant|Orients the audience — establishes geography, scale, and world. Opens scenes or reorients after a location change.|"Pull back to extreme wide. Subject tiny in the landscape. Environment dominant."|
|Wide|24–35mm|Subject occupies \~20% of frame|Shows subject in full context of environment. Communicates isolation, grandeur, or spatial relationships.|"Pull back to wide. Full body visible, surroundings dominant."|
|Full shot|35mm|Subject head-to-toe, environment visible|Shows full body and immediate surroundings. Used for choreography, entrances, exits.|"Full body in frame, head to toe. Environment visible at edges."|
|Medium / cowboy|35–50mm|Waist or thigh to head|The workhorse cut. Conversational, neutral. Shows gesture and expression without losing environment entirely.|"Frame from waist up. Eye level, neutral."|
|Medium close-up|50–85mm|Chest to head|Emotional engagement begins here. Expression readable, environment falls away. Most common TV and interview framing.|"Push in to medium close-up. Chest to head. Background falls away."|
|Close-up|85–135mm|Face fills frame|Emotion, reaction, intensity. Forces the audience into the character's interiority.|"Push in to close-up. Face fills the frame."|
|Extreme close-up|135mm+|Single feature — eye, mouth, hand detail|Hyper-focus. Used for dramatic punctuation, revelation, or to isolate a detail that carries narrative weight.|"Extreme close-up. Isolate \[eye / mouth / hand]. Fill the entire frame with this detail only."|
|Insert|85–135mm (macro for objects)|Object or detail fills frame|Directs audience attention to a specific story-critical element — a product, a gesture, a piece of text, a branded detail. Non-character.|"Insert shot. \[Named object] fills the frame. No character, no environment — isolate the object only."|
|Cutaway|Any|Varies|A shot outside the main scene axis — a reaction, an environmental detail, a parallel action. Provides editorial breathing room and can carry subtext.|"Cut away to \[named element]. Hold on it. No primary subject in frame."|
|POV|24–50mm (wide feels more immersive)|First-person — what the character sees|Places the audience inside the character's perspective. High subjective intensity.|"POV shot. Show what \[character] sees from their eyeline. No character visible in frame."|
|Over-the-shoulder (OTS)|50–85mm|Subject B occupies \~30–40% of frame over subject A's shoulder|Establishes eyeline and spatial relationship between two subjects. Standard for dialogue.|"Over-the-shoulder. \[Subject A]'s shoulder in foreground. \[Subject B] facing camera in mid-ground."|
|Two-shot|35–50mm|Two subjects share the frame|Shows relationship and dynamic between subjects simultaneously.|"Two-shot. Both \[subject A] and \[subject B] in frame. Equal weight. Eye level."|
|Aerial / bird's-eye|14–35mm (drone / crane equivalent)|Scene layout from above; figures at NPC scale|Establishes geography from above. Communicates scale, pattern, or spectacle. Removes the audience from ground-level intimacy.|"Move camera directly overhead. Bird's-eye view. Full scene layout visible. Figures small."|
|Low angle|24–50mm|Subject looms; sky or ceiling dominant in background|Conveys power, threat, heroism, or monumentality. Environment reads as imposing.|"Drop camera to low angle. Point up. Subject looms against the sky."|
|High angle|35–85mm|Subject appears small or vulnerable; ground dominant|Conveys vulnerability, smallness, or surveillance. Audience looks down on subject.|"Move camera high. Point down at subject. Subject appears small, ground dominant."|
|Dutch angle|35–85mm|Varies|Camera tilted on its axis. Communicates unease, instability, or psychological distortion. Use sparingly.|"Tilt the camera. Horizon line diagonal. Feeling of instability."|
|Rack focus|50–135mm (shallow depth of field)|Two subjects at different depths; one sharp, one soft|Shifts audience attention from one focal plane to another within a single shot. Implies connection or revelation between two elements.|"Rack focus from \[subject A] to \[subject B]. Shallow depth of field. One sharp, one soft."|

\---

## Quick Reference — Phase Sequence

```
Phase 0 — Asset Prep               \\\\\\\[Human gate — character sheets + model sheets approved before anything fires]
Phase 1 — Scene Context Intake     \\\\\\\[Human gate]
Phase 2 — World Inventory          \\\\\\\[LLM or human — anchor image OR written scene brief]
Phase 3 — Shot Manifest            \\\\\\\[LLM drafts ordered by beat/scale; human approves Tier 2]
Phase 4 — Per-Shot Prompts         \\\\\\\[LLM writes all prompts; generation fires in sequence, not all at once]
Phase 5 — Batch Generation + Loop  \\\\\\\[Wide shots first → approve → chain into mediums/close-ups → inserts last]
Phase 6 — Coverage Completeness    \\\\\\\[Human gate — storyboard test: can you read the scene?]
```

\---

## Storyboard-First Coverage Path — V2 Doctrine

### Why This Works: Model Behavior, Not Aesthetics

This approach is not a preference for storyboard aesthetics. It is an optimization for how Nano Banana image models (Gemini Pro Image / Flash Image) handle geographic consistency. When asked to one-shot multiple beats into a storyboard, the model establishes the entire location in one shared context — walls, spatial relationships, character positions, lighting direction — all held simultaneously. Frame-by-frame generation loses this: each shot starts fresh and geographic drift compounds across the batch.

The editor's thinking still applies exactly as described in The Director's Lens: angle contrast, focal length variety, wide/tight/insert rhythm, beat structure. The difference is where that thinking lives. Coverage planning goes into **storyboard prompt design** — what panels does the editor need, what angle does each panel cover — rather than into a series of individual prompts. The storyboard IS the previz. Panel expansion and style transfer are the execution steps that follow from an approved storyboard page.

### Panel Count: 3–4 Max Per Run

Too many panels in a single storyboard causes identity and geography breakdown — the model's context spreads too thin. Hard limit: **3–4 panels per storyboard run.**

### Rolling Storyboard Chain

When more than 4 panels of coverage are needed, chain storyboard runs:

**Run 1:**

* Image 1: Approved wide/anchor ref (style + environment authority)
* Prompt: 3–4 labeled panels describing the first coverage beats
* Output: Approve for geography and beat coverage — not final quality

**Run 2:**

* Image 1: Approved wide/anchor ref (style authority — always stays as Image 1)
* Image 2: Run 1 approved storyboard page (geometry context)
* Prompt: Next 3–4 labeled panels
* The Run 1 panels in Image 2 give the model established geometry to build new angles from, without being locked to the wide shot's camera axis

Continue chaining as needed. The original wide ref stays as Image 1 in every run.

### Multiple Image Inputs: Semantic Anchoring Tradeoff

Adding image inputs dilutes the model's semantic anchoring to any single one. This is both a tool and a risk:

**Good (geometry freedom):** Including prior storyboard panels as Image 2 helps the model propose genuinely new camera angles — it has more geometry in context and can deviate from the wide shot's composition axis. Useful when exploring coverage that the wide shot doesn't suggest on its own.

**Bad (style dilution):** Each additional image input dilutes the primary style authority (Image 1). The more inputs, the weaker the style lock. Identity consistency and environment grammar both drift as input count increases.

**Rule of thumb:** Keep total image input count to 3 or fewer. Image 1 is always the style/environment authority. When style consistency is the priority — keep inputs minimal. When geometry freedom is the priority (new angle exploration, extending coverage beyond what the wide implies) — add the prior storyboard page as Image 2 and accept some style dilution.

### Panel Labeling

Label each panel in the storyboard prompt (e.g., "PANEL A: WIDE LANDING", "PANEL B: MEDIUM GOODBYE"). The model renders labels as visible text in the output, creating named callout anchors. Expansion prompt template:

```
Expand PANEL A: WIDE LANDING from the reference storyboard to a standalone full 16:9 frame. Use the style and environment from the reference image. No text, no labels, no captions — clean image only. 16:9 aspect ratio.
```

The label targets the correct panel without re-describing content. "No text, no labels, no captions" is required — omitting it produces an output with the label rendered into the frame.

**The director's order in one line:** Asset sheets → wide beats → mediums derived from wides → close-ups → inserts.

