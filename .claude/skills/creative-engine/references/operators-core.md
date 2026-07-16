# Core Operators (v0 — the eight)

A large router is itself a taste surface. These eight are the whole v0 set;
the researched long tail lives in [operators-annex.md](operators-annex.md),
promotable only when session traces reveal a pathology these can't address.

**Universal rules** (apply to every operator):
- Stimuli come from `scripts/entropy.py` — never model-picked. No re-rolls:
  re-rolling because the draw "doesn't fit" reinstalls the taste filter.
- The draw is **binding for one full seed** before any evaluation (Eno:
  "absolutely drop everything"; Cage: "if you don't accept the chance
  operations you have no right to use them").
- Every seed records provenance: operator, stimulus, parent, mechanism.
- A good output is *prospectively improbable but retrospectively logical*.
  If a seed is merely obvious, re-roll the STIMULUS, not the prompt.

---

## 1. reframe (Trott / Sullivan / Gorilla)

**When:** session start (loop step 0), or when a whole frame is exhausted.
**Protocol:**
1. State the truest/awkwardest thing about the product — usually the thing
   the client would minimize (Sullivan).
2. Generate 5 restatements of what the work must accomplish, each locating
   the problem in a different place: the product / the buyer / the moment of
   use / the category / the culture (Trott upstream move).
3. List what the brief forbids or is embarrassed by; write one restatement
   that celebrates a forbidden thing (Guinness flip-the-fence).
4. Keep 4 frames forward: 1 anchored reading of the actual brief + 2
   plausible reframes + 1 deliberately uncomfortable one. Seed-batch under
   each BEFORE any human selection. Contractual constraints survive verbatim.
**Entropy:** optional — `entropy.py pick product buyer moment category culture`.
**Forbids:** picking the winning frame before seeds exist under all four.
**Example:** "make a spot about the gummy" → "make peeling something in
public a flex."

## 2. random-entry (de Bono)

**When:** blank page; repeating; DIAGNOSE says "stuck at the mode."
**Protocol:**
1. `entropy.py word` → one concrete noun. It may not be swapped.
2. List 5–6 attributes/associations of the word — of the WORD, not the brief.
3. Bridge EACH attribute to the live concern; every bridge must yield one
   concrete seed. "N/A" is an invalid completion.
**Entropy:** `entropy.py word` (nouns deck) or `entropy.py dictword`.
**Forbids:** choosing or re-rolling the word; skipping hard bridges.
**Example:** LIGHTHOUSE → "rotating beam" → the peeled gummy's exposed center
sweeps the dark cafeteria like a beacon; whoever the light touches levitates
until it passes.

## 3. oblique-interruption (Eno/Schmidt; McLuhan variant)

**When:** live deadlock mid-development; a seed that's close but dead.
**Protocol:**
1. `entropy.py draw oblique` → ONE card.
2. Obey it for one full draft even when its relevance is unclear — the
   irrelevant-seeming card is the mechanism working.
3. State in one line how the card was honored.
**Entropy:** `entropy.py draw oblique`.
**Forbids:** drawing more than one card; interpreting so loosely nothing
changes; evaluating before the obedient draft exists.
**Example:** "Cut a vital connection" → the peel keeps going: gummy, wrapper,
kitchen wall — the cut connection is between the candy and the room it's
eaten in.

## 4. synectic-analogy (Gordon/Prince)

**When:** the concern is well-defined but every seed feels like the category.
**Protocol (4-analogy ladder, in order, 2 outputs each):**
1. PERSONAL — *be* the product: first-person sensory monologue of being
   peeled and eaten (a genuinely different sampling region; discomfort is
   the signal it's working).
2. DIRECT — `entropy.py draw far-domains` → how does that domain "peel /
   reveal / transform"? Extract 3 mechanisms. Product mention BANNED during
   this excursion.
3. SYMBOLIC — compress the beat into a 2-word paradox ("delicate armor").
4. FANTASY — how would it happen in a dream, physics be damned?
5. FORCE FIT — every excursion output must be connected back into a
   shootable beat, however awkwardly. Evaluate goods-before-flaws.
**Entropy:** far-domains deck for step 2.
**Forbids:** skipping personal analogy; mentioning the product mid-excursion;
discarding an excursion output instead of force-fitting it.
**Example:** BE the gummy: "being peeled feels like taking off a jacket in
summer" → everyone on the bus involuntarily sighs in relief as she peels.

## 5. morphological-collision (Zwicky / Webb Young / Cage)

**When:** need coverage of a space, not one idea; suspicion that all seeds
sit on the modal diagonal.
**Protocol:**
1. Parameterize the beat (5–7 axes: where the change starts / what changes /
   physics violated / who reacts / sensory register / camera / who pays).
2. Enumerate 4–6 values per axis. Each axis MUST span registers: banal,
   formal, grotesque, sentimental, abstract — including options you'd never
   pick (that is the point of exhaustive charts).
3. Write the box as JSON; `entropy.py zwicky box.json --draws 5`.
4. Compose ALL drawn configurations as seeds before judging any (Cage's
   acceptance rule). The obvious idea is one cell in thousands.
   *Webb Young 2-pile variant:* 20 specific product facts × 20 unrelated
   things the audience knows; force-pair across the piles.
**Entropy:** `entropy.py zwicky`; the model builds the chart, the RNG casts.
**Forbids:** casting before the chart is complete (back-fitting); vetoing a
cast; padding a chart with 6 flavors of the same modal idea.
**Example:** draw = {peel starts at the horizon / sound becomes visible / a
dog reacts / camera upside-down} → the dusk sky peels back in sync with the
gummy, releasing visible strawberry-scented sound only the dog notices.

## 6. explicit-mutation (Mueller/DAYDREAMER)

**When:** ordinary development of a promising seed has stalled — last-resort
search expansion. Operates on an EXISTING seed, never from nothing.
**Protocol:**
1. Identify the seed's action elements (who does what to what, with what).
2. `entropy.py pick permute generalize retype` → apply the drawn operator:
   - PERMUTE: swap which object plays which role (the gummy peels the teen).
   - GENERALIZE: one object becomes a typed variable constrained NOT to be
     the original (not the gummy — something else peelable: the day itself).
   - RETYPE: change the action type, keep participants (not peel — unlock,
     unmoor, translate, defrost).
3. Record: parent seed, exact property changed, operator.
4. The mutation is NOT accepted directly — it goes to BRIDGE (loop step 5)
   and earns admission only if a path back to the concern verifies.
**Entropy:** `entropy.py pick` for the mutation operator.
**Forbids:** "a creative alternative" without naming what was mutated and
how; accepting mutations that never bridged.
**Example:** PERMUTE on "teen peels gummy" → "gummy peels teen": her outline
peels off like a sticker, revealing a more saturated, flavor-colored self.

## 7. constraint-transformation (Oulipo / Dogme / Obstructions)

**When:** output too generic; too comfortable; "prematurely polished."
**Protocol (three modes — pick by situation, or `entropy.py pick`):**
- CAGE: `entropy.py draw constraints` BEFORE ideating → generate 5 seeds
  inside the cage; then a validator pass discards quiet violations.
  One declared clinamen (rule-break) allowed per session, stated aloud.
- VOW: draw 3 constraints as a named rule-set for a whole batch ("signed").
  Rules ban techniques, never subjects.
- OBSTRUCT: after a strong seed, name its most habitual quality and issue a
  rule banning exactly that; regenerate; keep both versions. (Never issue
  "total freedom" — documented as the weakest obstruction.)
- N+7 mode for a stale premise: `entropy.py nplus7 "<the obvious sentence>"`
  → treat the mutated sentence as a literal brief.
**Entropy:** constraints deck; nplus7.
**Forbids:** choosing constraints the idea already satisfies; relaxing the
cage in revision; patching a violating idea instead of disqualifying it.
**Example:** "The product is never shown whole" → the beat lives in extreme
close-up on the peel curling; the impossible thing is seen only as colored
light on the teen's face.

## 8. consequence-heightening (UCB game / Skittles rulebook / two dials)

**When:** a seed passed Gate 0 and needs development into a treatment; the
DEVELOP operator. This is where ideas become the deliverable's shape.
**Protocol:**
1. BASE REALITY — 2 mundane sentences. Boring is load-bearing.
2. ONE impossible rule (the seed's mechanism). Budget: one.
3. FRAME it — one sentence where the world visibly registers the rule.
4. EXPLORE — 4 answers to "if this is true, what else is true?" derived
   from the rule's internal physics.
5. HEIGHTEN — 3 escalations of the SAME rule, each conceptually new (never
   merely bigger), each citing which explore answer licenses it; the
   protagonist's reaction escalates on its own track.
6. TWO DIALS — score event-magnitude and reaction-magnitude 1–10
   separately; require |event − reaction| ≥ 5 (both mismatch directions are
   valid genres: farce vs deadpan).
7. COST — someone quietly pays a price for the magic; everyone underreacts
   (the Skittles tragedy beat — whimsy without cost evaporates).
8. BUTTON — reincorporate a detail from the base reality, transformed.
**Validator (reject if):** a second impossible thing appeared; an escalation
can't cite its license; a rung is reachable by pure size increase; dials
match.
**Entropy:** none — this operator is pure logic applied to displaced input.
**Forbids:** heightening a rule that never got framed; crazy town (escalation
without logic); gaming out too fast (burning the top rung in move two).
**Example:** Rule: whatever the peel touches, peels. Frame: it brushes the
bench — the paint peels off in one clean coil. Heighten: sidewalk →
candy-glass; bus → a brighter bus; gray sky → ripe orange. Cost: her
transfer ticket peels too — blank. She shrugs. Button: the trash can peels
to reveal a slightly cooler trash can.
