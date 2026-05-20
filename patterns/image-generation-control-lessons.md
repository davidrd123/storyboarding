# Image Generation Control Lessons

Source: `/Users/daviddickinson/Projects/Lora/ComfyPromptByAPI-patrick/WorkingSpace/patrick/vault_gml`

Purpose: Extract the control surfaces from Patrick's GML image-generation workflow and translate them into reusable storyboarding patterns.

## Core Thesis

The durable product is not a single prompt. It is a controlled production memory:

- Canonical visual assets
- A shot/coverage vocabulary
- A world and style grammar
- Prompt records with lineage
- Approved keyframes
- Iteration notes that preserve what worked

The model can drift on identity, style, geography, scale, and story intent. The workflow controls drift by making every generation reference a small set of explicit authorities.

## Control Surfaces

### 1. Asset Control

Lock principal subjects before scene generation.

- Character sheets first, then scene shots.
- A useful character sheet is a multi-angle turntable, not just a hero pose.
- Key props, vehicles, and branded objects need model sheets too.
- The approved sheet becomes the identity anchor for every shot where that subject appears.
- Text-only character descriptions are treated as insufficient for continuity.

Storyboarding translation: before panel generation, build a `bible/` layer:

- `characters/[name]-turnaround`
- `characters/[name]-expressions`
- `characters/[name]-action-poses`
- `locations/[location]-wide`
- `props/[prop]-model-sheet`

Composite sheets are fine as canonical references. Atomized crops still help prompt assembly when a specific expression, pose, or prop detail matters.

### 2. Style Control

Separate evergreen style grammar from per-shot prompt text.

Patrick's vault uses:

- `look-overarching.md` for global visual grammar
- scene-specific `look-scene-XX-*.md` files for local style
- optional job addenda for one-off constraints or known failure modes

Storyboarding translation:

```
system = global_style + project_style + scene_style + optional_job_addendum
prompt = shot-specific instruction
references = identity/style/location/prop anchors with explicit roles
```

The style block should be stable. The shot prompt should change.

### 3. Reference Role Control

Every image input needs an assigned job.

Use explicit roles:

- Image 1 is the character identity reference.
- Image 2 is the style reference.
- Image 3 is the location/world reference.
- Image 4 is the prop/model reference.

Then specify preservation and borrowing:

- Preserve face, build, costume from Image 1.
- Borrow linework, palette, rendering texture from Image 2.
- Use environment grammar and lighting from Image 3.
- Match prop design from Image 4.

Key caution from Patrick's logs: image inputs carry spatial composition. A second image can fight the base image's framing. One strong anchor often beats two conflicting anchors.

### 4. World Geometry Control

Do not ask for new camera angles by camera command alone.

The scene coverage protocol introduces a `world inventory` before prompts:

- spatial landmarks
- foreground/midground/background positions
- off-frame implications
- lighting direction
- camera position
- style/register

For each new shot, spatially remap the world:

```
If the camera moves here, what should be foreground now?
What recedes?
What enters frame from off-screen?
Which landmarks prove this is the same place?
```

Storyboarding translation: make `WORLD` a first-class DSL block. Otherwise each panel invents a new location.

### 5. Coverage Control

Generate like a director, not like a mood-boarder.

The strong order is:

1. Asset sheets
2. Wide shot for each beat
3. Mediums derived from approved wides
4. Close-ups derived from approved wides/mediums
5. Inserts last

The wide is not just another image. Once approved, it is the ground truth for geography, lighting, and style.

Coverage must vary:

- wide / medium / close-up / insert
- front / profile / OTS / rear / low / high / dutch
- static and kinetic frames
- face shots and non-face shots

Storyboard test: lay approved panels in story order. If the scene reads and the geography stays clear, the kit is working.

### 6. Storyboard-First Control

For multiple related panels, consider generating a labeled storyboard page first.

Lesson from the coverage protocol: frame-by-frame generation causes drift because each frame starts fresh. A multi-panel storyboard page lets the model establish the location, characters, lighting, and beats in one shared context.

Rules:

- Use this when generating two or more related angles.
- Keep to 3-4 panels per run.
- Pass the approved wide/style anchor as Image 1.
- Label panels with short names: `PANEL A: WIDE LANDING`.
- Approve the page for geography and beat coverage, not final polish.
- Expand panels individually afterward.

Expansion prompt pattern:

```
Expand PANEL A: WIDE LANDING from the reference storyboard to a standalone full 16:9 frame.
Use the style and environment from the reference image.
No text, no labels, no captions - clean image only.
16:9 aspect ratio.
```

### 7. Prompt Log Control

Prompts are production records.

Patrick's pattern:

- Pre-log planned prompts before firing.
- Append new versions; do not overwrite.
- Keep active prompt files focused on current/approved shots.
- Archive older branches when active files get large.
- Mark approved keyframes immediately.
- Store output paths with searchable filenames.
- Log result notes and next iteration.

Storyboarding translation: each scene needs a prompt log, not just generated images.

Suggested entry:

```md
### p03b - Officer CU: expression fix

Date:
Mode: genesis | mutation | panel expansion
Shot:
Beat:
References:
System:
Job addendum:
Prompt:
Sent:
Output:
Result notes:
Score:
Next iteration:
Successful phrases:
```

### 8. Iteration Control

The main iteration method is surgical: take what worked and change only what failed.

Useful rules:

- If a result is 80% correct, edit/mutate the state instead of re-rolling.
- For a single wrong element, describe only the delta.
- Silence preserves; mentioning an element makes it mutable.
- Re-roll only when composition or geometry is fundamentally broken.
- If the same geometry failure happens twice, stop forcing it by mutation.
- When directionally correct but not quite right, try seed variants before changing prompt language.
- Save successful phrases verbatim. They are reusable assets.

For storyboards, this argues for a failure taxonomy attached to every panel:

- identity drift
- style drift
- geography drift
- wrong shot scale
- wrong expression/state
- wrong action
- wrong story beat
- preservation failure
- composition conflict from references

### 9. Evaluation Control

Patrick's review loop evaluates every output before moving on.

Core dimensions:

- Prompt Fidelity: did it do what was asked?
- Preservation Fidelity: did unchanged things stay unchanged?
- Style Lock: does it match the established look?
- Scene Hierarchy: is the right thing the hero?
- Story Service: does it tell the correct beat?
- Creative Brief Fidelity: does it satisfy project constraints?

Storyboard-specific additions:

- Continuity: does it connect to adjacent panels?
- Editorial utility: could this panel be cut into the sequence?
- Character state: does expression/body tension/eyeline match the beat?
- Readability: does the intended subject read at the chosen shot scale?

### 10. State Control

Character identity and character state should not be conflated.

- Identity is locked by reference: face, body, hair, costume baseline.
- State is panel-specific: expression, eyeline, body tension, dirt, injury, wardrobe variation, held object, emotional condition.
- Action is the beat verb.

Storyboarding prompt block:

```md
SHOT:
SUBJECT:
IDENTITY REFS:
STATE:
ACTION:
WORLD:
COMPOSITION:
LIGHTING:
CONTINUITY:
REFERENCE ROLES:
PRESERVE:
CHANGE:
AVOID:
```

## Practical File Structure For This Vault

```text
storyboard/
  project-brief.md
  style-guide.md
  characters/
    character-bible.md
  locations/
    location-bible.md
  scenes/
    scene-01/
      scene-01-beats.md
      scene-01-world-inventory.md
      scene-01-shot-manifest.md
      scene-01-prompts.md
      scene-01-approved-keyframes.md
```

## Short Version

The key transferable lesson is to make every image job answer four questions before it fires:

1. What is the identity anchor?
2. What is the style/world anchor?
3. What exact shot and character state are we asking for?
4. How will this result be evaluated, logged, and reused?

Without those four controls, storyboard generation becomes a sequence of attractive one-offs. With them, it becomes an iterative production system.

---

## Additional Patterns from Deeper Vault Read

The first pass captured the structural control surfaces. These are the named protocols and operational rules that live in `vault_gml/CLAUDE.md` and `visual/production-review-loop.md` and didn't fully transfer.

### 11. Genesis vs Mutation as load-bearing distinction

Patrick treats every image job as one of two modes, and they want different prompt structures, different reference strategies, and different evaluation criteria:

- **Genesis (text-to-image, no base plate):** building a new frame from scratch. Style must be carried by text + style refs. Identity must be carried by character sheet refs. The risk is *invention drift* — model fills gaps with whatever's plausible.
- **Mutation (img2img, base plate provided):** transforming an existing approved frame. Style and composition are already baked into the base. The risk is *preservation failure* — the model "improves" things that should not change.

Why this matters for storyboards: a panel that's the first look at a new beat is a genesis job. A reaction shot that follows an approved establishing shot is a mutation. The DSL skeleton is the same, but the reference budget, the preserve/borrow grammar, and the failure modes are different. The system should track and label which mode each panel is in.

### 12. System prompt architecture — locked stack + optional job addendum

Patrick's system prompt for every generation is structured as:

```
system_prompt = global_style (V2, locked) 
              + scene_style (locked)
              + optional job_addendum (one-off)
```

The locked layers never change between jobs in the same scene. The job addendum is a short string appended at the bottom for *this job's* known failure mode or specific emphasis — e.g. "suppress proportional reinterpretation — mutation job, identity must hold" or "close-up scale: ink line quality and paper grain are the primary read."

The addendum is logged alongside the prompt; it's part of the production record, not loose chat context. This pattern lets the evergreen style grammar stay clean while still applying targeted nudges per shot.

Storyboarding translation: the `STYLE` block in the DSL should be the locked stack; per-panel adjustments go in a labelled `JOB ADDENDUM` slot that's preserved in the prompt log.

### 13. Named protocols worth lifting verbatim

These are the model-behavior protocols Patrick has crystallized into named tools. The names themselves earn their keep — they make iteration decisions discussable.

- **Occam Protocol:** *Mentioning a feature makes it mutable; silence preserves it.* For mutation tasks, describe only the delta — every other element should not be mentioned. The less you say, the more accurately the model preserves. Direct implication for storyboard prompts: do not re-describe the costume on every panel if the costume hasn't changed.
- **Parsimony Protocol:** the same idea generalized — the shortest correct prompt outperforms the most descriptive one. Pile-up of adjectives causes drift more than it causes precision.
- **Anti-Hero Protocol / Hero Syndrome:** the model defaults to making the named subject larger/more central than asked. Counter with explicit forbidden zones ("nothing in the bottom third") and semantic downscaling ("the machine reads as a distant landmark, figures in foreground are the hero"). Relevant any time a panel's hero is *not* the most photogenic element in frame.
- **Character Sheet Technique:** lock identity in isolation on a clean background *before* any scene composition. Already captured in section 1; the named term is useful when talking about it.

### 14. Camera-change protocol — when to use img2img vs token-deconstruct

The brief's "compositional skeleton transfer" open question has a precursor in Patrick's vault. His rule:

- **Light camera adjustment (track back, slight reframe, same axis):** clean plate the wide and use as img2img — the model extends the composition without geometry conflict.
- **Heavy camera change (new angle, new axis, new coverage):** do NOT use the wide as img2img. Instead: (1) clean plate the wide, (2) deconstruct into text tokens (lighting, atmosphere, palette, materials, spatial grammar), (3) write a genesis prompt from those tokens with the new framing.

The pre-prompt check before any genesis: *does a reference exist that shares this world?* If yes, read it and extract tokens before writing the prompt. The focal length and shot type of the ref are irrelevant — what's being borrowed is the world grammar, not the framing.

This is the operational answer to "can the model take camera angle from a reference?" — the honest answer is *partially*, and the workaround is to extract world-grammar tokens from the reference and write a new prompt rather than asking the model to abstract framing across subjects.

### 15. Style anchor as text vs image input — the framing-conflict rule

For mutation jobs, Patrick keeps style locked through **text** (the locked-stack system prompt + style anchor text block), not through a second image. Reason: a second image input carries spatial composition along with style, and that composition can fight the base plate's framing. One strong image anchor beats two conflicting anchors.

Pass a style anchor as a second image only when the base plate doesn't already carry the style — e.g. a fresh genesis. For everything else, describe style in text.

Storyboarding implication: the style reference image is not a default ingredient on every panel. It's a tool used in genesis. For mutations on approved plates, the style is already in the base — adding the style anchor as a second image risks the framing override problem.

### 16. Reference-frame bleed (green screen / clean plate first)

Related to the above. Any image input carries its own spatial information whether you want it or not. Two mitigations:

- **Green screen the asset before using as img2img reference:** before using a character render as a reference into a new scene, mutate it to a neutral background. The model then anchors to identity without picking up the spatial composition.
- **Clean plate the scene before adding a character:** if the environment is the thing being preserved, clean-plate the scene first (mutate out existing characters/props), then use that as the img2img base.

Storyboarding implication: bible assets should be on neutral backgrounds. A character pose extracted from an approved panel still has that panel's lighting, depth cues, and environmental noise — using it as a bible asset will leak that context into every future panel that references it.

### 17. Seed dialing as a separate iteration axis

When a generation is directionally correct but not quite right, try seeds before changing prompt language. A locked seed + locked prompt = a repeatable shot. When a seed produces a strong result, log it alongside the prompt version it came from.

This is a distinct iteration tool from "edit the prompt" or "edit the state." For storyboards, it means the prompt log should carry seed alongside prompt + references — re-rolling and seed-dialing are different operations and should be tracked separately.

### 18. Mature-exit criteria — knowing when to stop iterating

These tools have hard ceilings. Patrick's stop conditions:

- The same geometric or structural failure has appeared across 2+ targeted attempts — the model cannot execute this class of transform via mutation. Move on or accept the imperfection.
- The original intent can be served by an earlier, simpler result — complexity creep can make earlier outputs look better in retrospect.
- The story service dimension is already satisfied — a technically imperfect image that tells the right story beats a technically perfect image that took 8 more iterations.
- Hard limit: **5 grind iterations** before escalating to a human direction call.

Always log *why* you moved on — it records a real tool constraint for future sessions.

For storyboards, this maps directly to the re-roll rate question. Don't budget for 100% panel success; budget for 80% acceptance with logged-exit notes on the rest.

### 19. Vault-as-memory — the architectural principle behind all the discipline

The single sentence that governs every habit in Patrick's vault: *the vault is the persistent context. Chat sessions end, token budgets fill, agents rotate — the vault doesn't.* A fresh agent with no prior chat history must be able to read the vault and pick up the project without being briefed.

**The fresh-agent test:** after any session, could someone reading only the vault files (no chat, no memory) make a good next decision? If yes, the session is done. If no, something needs to be written before closing out.

This is why the operational rules exist:

- **Pre-log queue with blank `Sent:` dates** — entries committed to the file before firing means a fresh agent can resume by finding blank-`Sent:` rows.
- **Approved keyframes table at the top of every prompts file** — canonical references for downstream iterations live in a known location.
- **Output filenames are the search index** — `sc[XX]-[shot-name]-[key-beat]_[nn].png`. A `find` by shot name returns the right candidates without opening any file.
- **Append, don't overwrite** — version history is part of the record.
- **Producer notes are intake, not truth** — every direction change must propagate into the relevant source files (look files, beat sheets, prompt logs) before the session ends.

Storyboarding implication: the architecture in the brief — state ledger, bible, prompt assembler, candidate history — is *exactly* a vault-as-memory system. Patrick's operational discipline is the ground truth for what makes such a system actually work in production, not just on paper.

### 20. Symbiotic collaboration — honest redirect, not silent compliance

Patrick's stated rule for working with Claude: *interpret the intent behind the suggestion, not just the surface instruction. The goal is the best generation, not the most obedient response.* If a different approach is more likely to achieve the brief, say so and propose it.

This is the same posture the storyboard system needs with its director-user. The system isn't a yes-machine; it's a collaborator that should surface "this prompt is going to hit known failure mode X, here's the fix" rather than firing the job and reporting the failure.

For Ben specifically, who's coming from FairTrade with strong intuitions about creative-tool design, this is probably the right collaboration register out of the gate.

---

## What This Means for the Storyboard Brief

Three concrete updates the storyboard brief should absorb:

1. **Add a Genesis-vs-Mutation flag to every panel slot.** It's not a stylistic distinction — it changes reference strategy, prompt grammar, and which failure modes to expect. The DSL should track it.

2. **The "compositional skeleton transfer" open question has a partial answer.** Patrick's clean-plate → token-deconstruct → genesis path is the working pattern when reference framing won't transfer cleanly. It's not the magic abstract-extraction the brief was hoping for, but it's a documented workaround that ships results.

3. **The vault-as-memory principle is the system's spine.** Pre-log queues, append-only logs, named approved keyframes, searchable filenames, propagation of intake into source files — these are not nice-to-haves. They're what makes the whole pipeline survive context exhaustion, agent rotation, and multi-session work. The storyboard system's UI sketch is essentially a vault-as-memory interface; Patrick's vault is the proof that the discipline is achievable.
