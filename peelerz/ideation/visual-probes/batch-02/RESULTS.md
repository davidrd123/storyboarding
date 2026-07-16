# Visual probes — batch 02

Generated July 11, 2026 with Nano Banana 2 (`gemini-3.1-flash-image-preview`),
1K, 16:9. These are reaction objects, not proposed final boards.

The batch deliberately pairs obvious answers to Ben's red-marked questions with
one-rule mutations. The point is to see whether mutation improves the underlying
idea or merely adds visual complication.

![Contact sheet](contact-sheet.png)

## Tina — what is outside the window / what happens to the car?

### 1. Giant hand peels the car — literal baseline

![Giant hand peels the car](outputs/2026-07-11/gemini-31-flash-image-preview/01_tina-giant-hand-peels-car-baseline_a5e739f4/tina-giant-hand-peels-car-baseline_01.png)

**Immediate read:** a giant hand opens or disassembles the car around Tina.

**What works:** Ben's scale gag is immediate; Tina and the product stay calm and
anchored inside ordinary suburbia.

**What does not yet work:** the metal reads as folded doors/body panels, not as one
peelable skin. This is a useful negative baseline: a hand plus deformation is not
enough. The seam, tension, and one continuous strip have to be staged much more
explicitly if the verb must be *peel*.

### 2. Gummy car skin becomes canopy — causal mutation

![Gummy car skin becomes canopy](outputs/2026-07-11/gemini-31-flash-image-preview/02_tina-gummy-skin-becomes-canopy-mutation_98597700/tina-gummy-skin-becomes-canopy-mutation_01.png)

**Immediate read:** Tina is lifted from a car by a gigantic translucent gummy
sheet.

**What works:** unlike the current rainbow parachute, the canopy and car share one
material. It gives the transition a Peelerz-shaped physical cause.

**What does not yet work:** it is fleshy, a little body-horror, and the continuous
car → peel → canopy path is not quite traceable. This may be an idea worth repairing,
but the image is evidence that “gummy material” needs a cleaner, brighter, more
confectionary visual language.

## Raul — what else can he transform into?

### 3. Multiple-flavor candy mecha — literal baseline

![Multiple-flavor candy mecha](outputs/2026-07-11/gemini-31-flash-image-preview/03_raul-multi-flavor-candy-mecha-baseline_44ce0155/raul-multi-flavor-candy-mecha-baseline_01.png)

**Immediate read:** multiple translucent candy flavors have assembled into armor
around Raul.

**What works:** the flavor modules and Raul-at-the-center construction are cleanly
legible; it directly answers Ben's “better Voltron made of multiple candies?” note.

**What does not yet work:** it is still generic power armor. “Different colors make
a robot” is organization, not yet a surprising concept. A useful next mutation
would change the social or behavioral rule—for example, each module comes from a
different kid's chosen flavor—rather than merely making the robot stranger.

### 4. Giant Raul eats normal Raul — literal baseline

![Giant Raul eats normal Raul](outputs/2026-07-11/gemini-31-flash-image-preview/04_giant-raul-eats-small-raul-baseline_5466f674/giant-raul-eats-small-raul-baseline_01.png)

**Immediate read:** an enormous duplicate of Raul is about to eat little Raul as if
he were the candy.

**What works:** this is the fastest and funniest single-frame read in the batch.
Meg's underreaction gives the absurdity a comic register rather than horror. It
also lands Ben's exact suggestion without needing explanatory transition frames.

**What does not yet work:** the giant is merely larger, not visibly a consequence
of mango Peelerz. That may be fine—the premise is already strong—but if product
causality matters, it should be added with one quiet clue rather than another large
effect.

## Liz and John — what worlds do they float through?

### 5. Anchored two-world handoff — formal baseline

![Anchored two-world handoff](outputs/2026-07-11/gemini-31-flash-image-preview/05_couple-anchored-two-world-handoff-baseline_e0cf7f10/couple-anchored-two-world-handoff-baseline_01.png)

**Immediate read:** the same couple straddles ordinary live-action campus and a
painted fruit world.

**What works:** it demonstrates the Doctor Strange reference grammar cleanly: keep
the people emotionally and spatially anchored while the medium changes around them.

**What does not yet work:** as a still, it reads as split screen or a mural more
than a world actively changing. This is a transition-design baseline, not yet a
Peelerz idea.

### 6. Gummy peel-film redraws the world — causal mutation

![Gummy peel-film redraws the world](outputs/2026-07-11/gemini-31-flash-image-preview/06_couple-gummy-film-redraws-world-mutation_7b44bbbe/couple-gummy-film-redraws-world-mutation_01.png)

**Immediate read:** a golden peel or film curls around the couple, with an animated
fruit world inside it and live campus outside it.

**What works:** this is the strongest baseline/mutation improvement. The world swap
now has a possible material cause, and the couple remains stable. It begins to answer
both Ben's open world-building space and the product's peel behavior.

**What does not yet work:** the arc reads somewhat like a generic portal or brand
swoosh, and its origin in the candy is not visually proven. The next test should
make the peel cross the foreground and physically redraw a recognizable campus
object as it passes, instead of merely enclosing a different background.

## What this batch contributes to the engine

1. **Generate the obvious answer first.** It gives us a legibility control. Giant
   Raul proves that a literal answer can outperform a more elaborately transformed
   one.
2. **Mutation earns its keep only if it changes causality.** The couple's peel-film
   improves the baseline because it supplies a mechanism. Tina's gummy canopy adds
   material novelty but currently damages tone and clarity.
3. **Evaluate the visible verb, not the prompt's verb.** The first image was
   prompted as peeling but rendered as opening/disassembly. A visual verifier must
   report what is actually on screen.
4. **Separate premise strength from product causality.** Giant Raul has a strong
   premise with weak causality; the couple has better causality with a weaker comic
   premise. Those should be scored independently rather than collapsed into one
   “creative” rating.

Exact generation instructions are preserved in [prompts.yaml](prompts.yaml).
