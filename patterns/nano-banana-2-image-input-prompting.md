# Nano Banana 2 Image-Input Prompting

Date: 2026-05-23

Model target: Nano Banana 2, also published as `gemini-3.1-flash-image-preview` / Gemini 3.1 Flash Image.

Purpose: Condense the current public guidance, model constraints, and this repo's storyboarding control lessons into one practical document for constructing prompts from image inputs.

## Core Thesis

For Nano Banana 2, the prompt is not just a description of the desired image. It is a contract that assigns authority to each image input.

The model can use text, images, search grounding, and multi-turn context. That makes it powerful, but also easy to confuse. The prompt has to answer four questions explicitly:

- What is each input image allowed to control?
- What must be preserved exactly?
- What should be borrowed loosely?
- What must not leak from the references into the output?

The best prompt is usually not the longest prompt. It is the prompt with the cleanest division of responsibility.

## Ten Rules

Use this section first, then reach for the detailed patterns below.

1. Give every input image exactly one primary role.
2. Name important characters and objects, then use those names consistently.
3. Separate "preserve," "borrow," and "do not borrow" instructions.
4. Preserve concrete visible features, not generic identity claims.
5. Use fewer high-signal references before trying the full reference budget.
6. Build bible assets before storyboard panels.
7. Describe shots in camera, staging, and foreground/midground/background terms.
8. Repeat state facts every time they must persist.
9. Use higher thinking and search grounding only when the task actually benefits from them.
10. Mutate local failures; rebuild when identity, geography, or reference separation fails.

## Verified Model Facts

Use these as the operating assumptions for current API work.

- Model id: `gemini-3.1-flash-image-preview`.
- Official positioning: Nano Banana 2 is Gemini 3.1 Flash Image, combining Pro-level image generation/editing capabilities with Flash-level speed.
- Inputs: text strings and images. The model card describes a token context window up to 1M.
- Outputs: image plus optional text response.
- Image editing mode: send one or more image inputs plus a text instruction.
- Multi-turn editing is recommended for iterative visual work.
- Search grounding can be used for factual or real-world visual subjects.
- Resolutions: `512`, `1K`, `2K`, `4K`.
- Aspect ratios for 3.1 Flash Image Preview: `1:1`, `1:4`, `1:8`, `2:3`, `3:2`, `3:4`, `4:1`, `4:3`, `4:5`, `5:4`, `8:1`, `9:16`, `16:9`, `21:9`.
- Reference images: the API docs describe up to 14 reference images. For Gemini 3.1 Flash Image Preview, they break this down as up to 10 object images and up to 4 character images. Google's launch blog also describes subject consistency for up to five characters and up to 14 objects in a single workflow. Treat four character reference images as the safe API budget unless the actual surface you are using proves otherwise.
- Thinking controls: Google's developer launch post describes Minimal as the default and High/Dynamic as higher-reasoning modes for complex prompts before rendering.
- Limitations called out in the model card: hallucinations, occasional slowness/timeouts, small or long text problems, imperfect character consistency, partial masked/doodle editing instruction following, infrequent copying/pasting from input images, spatial localization confusion, and limited advanced factuality/3D reasoning.
- Rights and provenance: only upload source images you have the right to use. The API docs say generated images include a SynthID watermark.

## Prompt Construction Stack

Build image-input prompts in this order.

### 1. Reference Manifest

Name every image and assign one job.

```text
Image 1 is the character identity reference for MARA.
Image 2 is the expression reference for MARA.
Image 3 is the location plate for the ruined observatory.
Image 4 is the style reference.
Image 5 is the prop reference for the brass astrolabe.
```

Do not assume the model will infer why an image was attached. If an input has no explicit role, it becomes ambient influence.

### 2. Preserve Contract

State what must stay fixed from identity and object references.

```text
Preserve from Image 1: MARA's face structure, nose shape, eye spacing, hair silhouette, coat cut, scarf color, height, and build.
Preserve from Image 5: the astrolabe's circular frame, brass material, etched zodiac ring, hinge shape, and central pointer.
```

Concrete features beat generic phrases like "same character" or "same object."

### 3. Borrow Contract

State what may be borrowed from style, lighting, mood, location, or composition references.

```text
Borrow from Image 4: ink wash treatment, limited olive/sepia palette, dry-brush texture, soft paper grain, and cross-hatched shadow language.
Borrow from Image 3: the observatory's broken dome silhouette, cracked floor geometry, doorway placement, and late-afternoon light direction.
```

Borrowing is looser than preservation. Use it when exact replication is not required.

### 4. Do-Not-Borrow Fence

Block the common leakage paths.

```text
Do NOT borrow from Image 4: subject, pose, character identity, location, props, or composition.
Do NOT borrow from Image 3: its camera angle, people, weather, or color palette.
```

This repo's Phase 0 tests show that "Borrow / Do NOT borrow" phrasing can isolate style from subject leakage when the prompt is explicit.

### 5. Target Shot

Describe the actual requested image using the official prompt guide's slots:

- Style or medium
- Subject
- Setting
- Action
- Composition

For storyboards, also include:

- Shot scale
- Camera height and angle
- Foreground/midground/background stack
- Eyelines
- State ledger facts that must persist

Example:

```text
Generate a 16:9 cinematic storyboard panel.

SHOT: MCU, slight low angle, MARA frame right, empty left third.
SUBJECT: MARA stands alone, one hand holding the brass astrolabe.
ACTION: She has just understood the map. Her lips are closed, eyes fixed off-frame left, body still.
SETTING: Inside the ruined observatory from Image 3, late afternoon light entering from frame left.
COMPOSITION: Foreground has cracked floor tiles. Midground has MARA and the astrolabe. Background shows the broken dome and a bright slice of sky.
MOOD: Quiet discovery, tense but not frightened.
```

### 6. Output Spec

Specify final-use format.

```text
Aspect ratio 16:9.
Resolution 2K.
No captions, no labels, no subtitles, no panel borders.
```

If text is desired inside the image, quote it exactly and specify the surface and typography:

```text
The brass plaque reads "NORTH GATE" in engraved small caps.
```

Avoid long paragraphs of in-image text. Use short, exact strings.

### 7. Reasoning And Grounding

Use higher thinking for prompts that combine many constraints: multiple refs, text rendering, infographics, historically accurate scenes, search-grounded subjects, or complex spatial edits.

Use search grounding when the target is a real place, product, organism, current event, diagram, weather, or factual visual. Do not use it for purely invented worlds unless you want real-world contamination.

```text
Use high thinking for composition and continuity.
Use image search only to verify the architecture of Bletchley Park Mansion before rendering.
```

## Default Prompt Shell

Use this as the baseline for image-input generations.

```text
Image 1 is [role].
Image 2 is [role].
Image 3 is [role].

Preserve from Image 1: [specific identity/object features].
Borrow from Image 2: [style/composition/location features].
Borrow from Image 3: [environment/lighting/prop features].

Do NOT borrow from Image 2: [subjects, setting, pose, composition, props].
Do NOT borrow from Image 3: [unwanted people, weather, palette, camera angle].

Generate: [one-sentence target image].

SHOT: [shot scale, camera height, lens/angle if useful].
SUBJECT: [who/what, named consistently].
ACTION: [visible action or state].
SETTING: [where, time, atmosphere].
COMPOSITION: [framing, foreground/midground/background, eyeline, negative space].
STYLE: [stable style grammar, if not fully handled by a style ref].
CONTINUITY: [state facts that must persist].

Aspect ratio [ratio].
Resolution [512|1K|2K|4K].
[No text / exact quoted text].
```

## Image-Input Packaging

### Character Identity

Good character inputs are clear, high-signal, and role-labeled.

Prefer:

- One clean hero image.
- A turntable or model sheet when available.
- Separate expression references when expression is load-bearing.
- Separate costume/state references when the costume has changed.

Avoid:

- Cropped faces with no costume if the outfit matters.
- Busy composites where the character is small.
- Attaching several inconsistent versions of the same person.
- Relying on prose alone for a character who must remain consistent.

Use a named identity:

```text
The character in Image 1 is MARA. Refer to her only as MARA throughout this prompt.
```

### Style

Style references should be isolated from subject matter.

```text
Image 4 is a style reference only.
Borrow: linework, palette, texture, rendering density, shadow language.
Do NOT borrow: character, scene, pose, props, composition, or story content.
```

If style is crucial across a project, keep a stable text style block and reuse it verbatim. The style block should not change every shot.

### Location

A location plate is not just atmosphere. It is spatial authority.

Preserve:

- Landmark positions
- Major silhouettes
- Door/window/opening placement
- Light direction
- Foreground/midground/background structure

Do not simply say "same location." Say what proves it is the same location.

```text
Preserve the broken circular dome in the rear center, the cracked tile path leading from lower left to center, and the tall arched doorway on frame right.
```

### Composition Reference

Composition refs are dangerous because they carry subject, costume, and scene leakage.

Use only when the shot geometry is worth the risk. Fence hard:

```text
Image 6 is a composition reference only.
Borrow only: camera height, subject scale in frame, horizon placement, diagonal movement direction, and foreground/midground/background depth.
Do NOT borrow: subject, clothing, location, lighting, color palette, props, or narrative situation.
```

When possible, describe the skeleton in text instead of attaching a composition image.

### Visual Spec Pages

The 2026 visual-to-visual research trend supports a pattern this repo already uses: when visual intent is hard to serialize, make a visual spec page.

A visual spec page can include:

- Character sheet crops
- Prop crops
- Color swatches
- Location plate
- Shot sketch
- Typography samples
- Labeled do/don't examples

Prompt it as a specification, not as an image to edit:

```text
Image 1 is a visual specification sheet. It is not the target scene.
Use it to understand MARA's identity, the observatory location, the astrolabe prop, and the ink-wash style.
Do not reproduce the sheet layout, labels, borders, or collage structure.
Generate a single clean 16:9 storyboard panel.
```

## Storyboarding Workflow

### 1. Build The Bible First

Generate or collect canonical assets before panels:

- Character identity sheet
- Expression sheet
- Costume/state sheet
- Key prop sheet
- Location plate
- Style anchor

The bible images are the source of truth. Text-only continuity is too weak for repeated panel work.

### 2. Establish The Wide

For each scene, approve a wide shot before close-ups.

The wide shot locks:

- Geography
- Light direction
- Scale
- Main landmarks
- Palette
- Environmental texture

Subsequent panels should cite the approved wide or location plate and name the specific landmarks that must remain recognizable.

### 3. Generate Coverage From Approved Anchors

Prompt like a director:

- Wide
- Medium
- Close-up
- Insert
- Reverse
- Over-the-shoulder
- High/low angle variants

Do not ask for "same scene, different angle" alone. Remap the world:

```text
Camera is now inside the arched doorway looking back toward the broken dome.
Foreground: chipped doorframe edges.
Midground: MARA in profile crossing left to right.
Background: the cracked tile path and broken dome from the approved wide.
```

### 4. Multi-Panel Storyboard Page

Use when a beat needs several related images.

```text
Create a four-panel storyboard page using MARA from Image 1 and the observatory from Image 2.
Keep MARA's identity, costume, and scale consistent.
Panel A: wide establishing shot.
Panel B: MCU as she notices the plaque.
Panel C: insert of the astrolabe aligned with the plaque.
Panel D: reverse angle as the dome opens.
No final polish required. Prioritize geography, continuity, and readable staging.
```

Then expand approved panels:

```text
Expand PANEL C from Image 1 into a standalone clean 16:9 frame.
Preserve the prop design, hand placement, lighting direction, and ink-wash style.
Remove panel labels, borders, captions, and page layout.
```

## Editing Workflow

### Genesis Prompt

Use for first creation. Include all roles, preserve/borrow/fence rules, shot details, and output spec.

### Mutation Prompt

Use when the image is mostly correct.

```text
Edit the current image only.
Change: MARA's mouth should be closed, with no teeth showing. Her expression is controlled and cold, not shouting.
Preserve unchanged: identity, costume, pose, camera angle, background, lighting, linework, color palette, and aspect ratio.
```

For surgical edits, do not re-describe the whole scene unless the model needs reminder context. Mentioning stable elements can make them mutable; preserve lists should be short and explicit.

### Rebuild Prompt

Use when geometry, staging, or reference separation fails.

If the camera angle or spatial logic is wrong twice, stop mutating. Return to the prompt shell and clarify world geometry.

## Common Failure Modes And Fixes

### Identity Drift

Symptoms:

- Face changes between panels.
- Costume silently shifts.
- Character looks like a sibling rather than the same actor.

Fix:

- Attach the cleanest identity ref as Image 1.
- Name the character.
- List facial and costume features.
- Use an expression ref if emotion is important.
- Reduce conflicting refs.

### Style Leakage

Symptoms:

- Subject from the style ref appears.
- Scene from style ref contaminates output.
- Composition copies the style ref.

Fix:

- Mark the image as "style reference only."
- Use a borrow list and a do-not-borrow list.
- Move stable style into a text block.

### Composition Conflict

Symptoms:

- Output averages two camera angles.
- Location plate fights composition ref.
- Subject scale is wrong.

Fix:

- Keep one geometry authority.
- Convert the desired composition into text skeleton terms.
- Specify camera position relative to landmarks.

### State Loss

Symptoms:

- Wounds heal.
- Hat reappears.
- Dirt, damage, or costume changes vanish.

Fix:

- Keep a state ledger outside the prompt.
- Re-inject state facts every panel.
- Create a costume/state reference image after major changes.

### Expression Collapse

Symptoms:

- "Cold rage" becomes a snarl.
- Subtle grief becomes theatrical crying.
- Determination becomes generic smile/anger.

Fix:

- Use physical expression language: "lips closed," "no teeth," "jaw set," "eyes fixed."
- Add anti-expression fences: "not shouting," "not smiling," "not crying."
- Use an expression sheet reference.

### Text Problems

Symptoms:

- Wrong letters.
- Blurry small text.
- Extra unwanted signs.

Fix:

- Quote exact text.
- Keep strings short.
- Specify font and surface.
- Use higher resolution for final.
- For no-text images, state "no text, no labels, no captions, no signs."

### Left/Right Or Spatial Confusion

Symptoms:

- Eyeline points wrong way.
- Character appears on wrong side.
- Object is misplaced.

Fix:

- Anchor positions to frame edges and landmarks.
- Use foreground/midground/background.
- Use "frame left" and "frame right," not only "left" and "right."
- Attach a visual spec or rough sketch when the layout is critical.

### Input Copy/Paste

Symptoms:

- The model pastes part of the reference image into the output.
- The result looks collaged.

Fix:

- Say "reinterpret, do not paste or collage."
- Use a cleaner reference crop.
- Reduce the number of attached images.

## Prompt Recipes

### Identity-Preserving New Scene

```text
Image 1 is the character identity reference for MARA.
Image 2 is a style reference only.

Preserve from Image 1: MARA's face structure, hair silhouette, coat, scarf, height, and build.
Borrow from Image 2: ink wash linework, muted olive/sepia palette, paper texture, and cross-hatched shadows.
Do NOT borrow from Image 2: subject, location, pose, props, or composition.

Generate a 16:9 storyboard panel of MARA standing at the edge of a ruined observatory balcony at dusk.
SHOT: medium-wide, slight low angle, MARA frame right.
ACTION: She holds the brass astrolabe close to her chest and looks off-frame left.
SETTING: cracked stone balcony, broken dome behind her, wind moving dust through the opening.
COMPOSITION: foreground balcony edge, midground MARA, background dome silhouette and orange sky.

No text, no labels, no captions.
Resolution 2K.
```

### Style-Only Transfer

```text
Image 1 is a style reference only.

Borrow from Image 1: palette, linework, texture, shadow treatment, and rendering density.
Do NOT borrow from Image 1: subject, setting, props, characters, composition, or story content.

Generate a new scene: a steam tram crossing a wet city square at dawn, one conductor stepping down with a lantern.
Wide 16:9 composition, cinematic but illustrated.
No text.
Resolution 1K.
```

### Location Continuity Shot

```text
Image 1 is the approved wide shot of the ruined observatory.
Image 2 is MARA's character identity reference.

Preserve from Image 1: broken dome in rear center, arched doorway on frame right, cracked tile path from lower left to center, and light entering from frame left.
Preserve from Image 2: MARA's face, hair, coat, scarf, height, and build.

Generate a new camera angle from inside the arched doorway, looking back toward the broken dome.
Foreground: chipped doorway edges on both sides.
Midground: MARA in profile, crossing left to right.
Background: cracked tile path and broken dome remain recognizable.
No text.
Aspect ratio 16:9.
Resolution 2K.
```

### Surgical Edit

```text
Edit the current image only.

Change only this: close MARA's mouth so no teeth are visible. Her expression should be controlled, tense, and silent.
Preserve unchanged: identity, costume, pose, camera angle, background, lighting, color palette, and linework.
No new characters, no text.
```

### Text Localization

```text
Image 1 is the current sign image.

Edit the sign text only.
Replace the English phrase "Native Wildlife: Please Observe from a Distance" with the exact Hindi text: "[verified translated text]".
Preserve unchanged: sign material, illustration style, camera angle, lighting, background foliage, and sign shape.
Use legible hand-painted lettering that fits the sign.
```

### Visual Spec Page To Panel

```text
Image 1 is a visual specification sheet, not the target image.
It defines MARA, the brass astrolabe, the ruined observatory, and the ink-wash style.
Do not reproduce the sheet layout, labels, borders, arrows, or collage structure.

Generate one clean 16:9 storyboard panel.
MARA kneels in the observatory, aligning the astrolabe with moonlight on the cracked floor.
Preserve MARA's identity, the astrolabe design, and the observatory landmarks from the sheet.
Use the sheet's palette and linework.
No text, labels, borders, or captions.
Resolution 2K.
```

## Prompt Lint Checklist

Before sending, check:

- Does every image have exactly one primary role?
- Are preservation features concrete?
- Are style/location/composition borrowing rules separated?
- Are do-not-borrow fences present for style and composition refs?
- Is the target shot described in visual terms, not abstract intent only?
- Are state facts repeated if they must persist?
- Is the output aspect ratio and resolution specified?
- Is in-image text either explicitly quoted or explicitly forbidden?
- Are there fewer refs than the maximum unless the task truly needs more?
- Is the prompt asking for one image unless a multi-image output is intentional?

## Output Review Rubric

Score quickly after generation.

- Prompt following: Did it do the requested action and shot?
- Preserve fidelity: Did identity/object refs hold?
- Style lock: Did style match without subject leakage?
- Spatial continuity: Does the location remain the same place?
- Composition: Does the camera/framing serve the beat?
- State continuity: Did wounds, props, costume, and emotional state persist?
- Text accuracy: Is every quoted string correct and legible?
- Artifacts: Any collage seams, duplicated subjects, warped hands, or accidental labels?

Decision:

- Accept if the panel advances the storyboard and has no continuity-breaking defects.
- Mutate if one or two local elements are wrong.
- Rebuild if geography, identity, or reference separation failed.

## Practical Defaults

- Use 512 or 1K for exploration.
- Use 2K for serious storyboard panels.
- Use 4K for final assets, typography, product shots, or detail-critical frames.
- Use Minimal/default thinking for simple single-ref edits.
- Use High/Dynamic thinking for multi-ref prompts, text-heavy images, infographics, storyboards, and real-world grounded images.
- Prefer 3-6 high-quality references over filling the 14-image budget.
- For API storyboarding on Nano Banana 2, budget safely for 4 character refs and 10 object refs unless your client/surface documents a higher character cap.
- If a result is 80 percent correct, edit surgically.
- If the same spatial failure appears twice, rebuild from a clearer world-geometry prompt.

## Source Notes

- Google DeepMind, "Gemini 3.1 Flash Image - Nano Banana 2": https://deepmind.google/models/gemini-image/flash/
- Google Blog, "Nano Banana 2: Combining Pro capabilities with lightning-fast speed" (2026-02-26): https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/
- Google Blog, "Build with Nano Banana 2, our best image generation and editing model" (2026-02-26): https://blog.google/innovation-and-ai/technology/developers-tools/build-with-nano-banana-2/
- Google AI for Developers, "Nano Banana image generation": https://ai.google.dev/gemini-api/docs/image-generation
- Google DeepMind model card, "Gemini 3.1 Flash Image": https://deepmind.google/models/model-cards/gemini-3-1-flash-image/
- Google DeepMind prompt guide, "How to create effective image prompts with Gemini Image": https://deepmind.google/models/gemini-image/prompt-guide/
- Liu et al., "Beyond Text Prompts: Visual-to-Visual Generation as A Unified Paradigm" (arXiv:2605.12271): https://arxiv.org/abs/2605.12271
- Local repo synthesis: `patterns/image-generation-control-lessons.md`, `phase-0/prompts.md`, and `TEST_BEDS.md`.
