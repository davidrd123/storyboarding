# Results — batch 04 Lite

## Bottom line

`gemini-3.1-flash-lite-image` is useful here as a fast visual-probing model. Across all 18 jobs it
kept Tina, the back-seat setup, the gummy, and the pink Peelerz bag coherent enough that the changed
idea could be compared from frame to frame. This is much closer to useful reference-guided iteration
than a fresh text-to-image lottery.

It is not a precision editor. Each result re-renders the whole frame: Tina's gaze and expression
shift, hands and package details drift, small label text mutates, and lighting is reinterpreted. The
right mental model is controlled variation, not a locked plate with an isolated paint-out.

See the full batch in [contact-sheet.png](contact-sheet.png).

## Strongest directions

### 08 — houses bloom open

The clearest transformation of ordinary suburbia. It is immediately readable, strange without
becoming arbitrary, and contains multiple layers of life inside the opened houses. This feels like a
world premise rather than a decorative effect.

### 09 — giant goldfish rooftops

A very clean single rupture. Tina's changed gaze gives the event an emotional beat, and the fish
feels surprising rather than generically psychedelic. It would be easy to understand in motion.

### 11 — street is a miniature world

The best scale play. The giant fingers, tiny car, and tropical miniature make a story with only a few
elements. It also suggests a transition mechanism: the world outside is being physically handled.

### 13 — sky peels into fruit night

The most directly Peelerz-native mechanism in the batch. The sky has an outer skin and an inner
world, making the brand action part of the cosmology rather than merely placing fruit in the scene.
The current interior is overdecorated, but the core gesture is strong.

### 18 — tiny mango mural civilization

The richest background story. It rewards looking and treats the transformed world as something with
inhabitants, labor, ritual, and history. The mango imagery does not match the visible lychee package,
so this is a world-building lead rather than a flavor-correct execution.

## Useful mechanisms, even where the frame is not a winner

- **05 — reflections transform first:** an excellent onset rule, but the reflection spills over
  Tina's face and weakens spatial clarity.
- **06 — neighborhood stagehands:** literalizes transformation as an event being built in real time.
  It has human comedy and is less dependent on pure CG spectacle.
- **10 — giant hand approaching:** the third storyboard reference pushed the model to reinterpret the
  whole composition. The result has energy, but it is evidence that more references do not
  automatically mean tighter continuity.
- **12 — fruit orchard under pavement:** the peel-back mechanism is compelling, but the model moved
  the road flap into the car instead of respecting the window boundary.
- **16 — classical still-life landscape:** proves that the exterior can carry a distinct visual
  language while Tina remains live action. The art-history treatment itself feels more like a look
  exercise than this character's particular imaginative world.

## Weaker territory

- **01 and 07:** too restrained; they read as background art direction rather than a reality break.
- **02:** attractive and legible, but close to generic lush tropical advertising.
- **14 and 15:** broad psychedelic and stop-motion styling collapse toward familiar colorful whimsy.
  They are less specific, less mysterious, and less story-bearing than the single-rupture ideas.
- **17:** beautiful aquarium imagery, but it replaces the premise with an environmental wallpaper.

## What the batch says about the larger creative direction

The useful axis is not realistic versus surreal. It is **a discoverable rule versus generalized
fantasy decoration**. The frames become compelling when an ordinary thing behaves according to one
precise impossible law: a house blooms, a sky has a peel, a street is a miniature, or a giant fish
occupies suburban air.

That is also the most grounded way to use Tina's point of view. The gummy does not need to launch a
complete candy universe. It can let her notice one impossible property of the world, then follow the
consequences. The best next batch would therefore deepen a few rules rather than add more unrelated
looks.

## Recommended next experiment

Take directions 08, 09, 11, and 13 and make four-frame progressions for each:

1. ordinary world with the first nearly missable symptom;
2. Tina notices as the rule becomes legible;
3. full transformation with one surprising consequence;
4. a transition image that can hand off to another character or flavor.

Use the same two references and the same foreground language. Keep Lite for this sixteen-frame
story-development pass; reserve a higher-fidelity model for the few frames that survive as actual
sequence candidates.

## Technical observations

- 18 of 18 jobs completed successfully.
- Two reference images worked consistently for identity, product, and composition guidance.
- The one three-reference job showed more compositional drift than the two-reference jobs.
- Most exterior-only instructions were respected, with notable spatial spill in 05, 11, 12, and 13.
- Product branding is unusually legible for ideation, but not accurate enough for final packaging.
- Outputs are 1K, 16:9, one image per prompt.
