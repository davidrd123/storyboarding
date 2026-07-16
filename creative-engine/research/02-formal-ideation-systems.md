# Formal / Systematic Ideation Methodologies — Mechanics for a Creative Engine

Research for the "creative engine" skill: making LLM ideation genuinely divergent instead of modal.
Focus: the actual **mechanics** of each system, and how each translates into an executable prompt move.

**Test case used throughout:** *"a candy commercial beat where a teenager eats a peelable gummy and one impossible thing happens."*

**Framing note.** The LLM failure mode is sampling the highest-probability continuation — the "first idea a committee would think of." Every system below was designed to defeat the human analog of exactly that failure (de Bono calls it pattern-following, TRIZ calls it *psychological inertia*, Synectics calls it the tyranny of the familiar). The load-bearing mechanisms recur across all seven systems: **(a) inject an input the problem didn't supply** (random word, analogy domain, contradiction pair, provocation), **(b) defer judgment structurally**, not as an attitude, **(c) impose quotas / systematic enumeration** so the modal answer is only 1 of N and cannot end the search, **(d) require an explicit bridging step** ("movement," "force fit," "cross-consistency") so the weird input must be metabolized rather than discarded.

---

## 1. Edward de Bono — Lateral Thinking

### 1.1 The theory: brain as self-organizing patterning system

De Bono's justification for the whole toolkit (from *The Mechanism of Mind* / *Serious Creativity*): the brain is an **active, self-organizing information surface**, not a passive store. "All information changes the surface which then receives future information differently" — like rain self-organizing into rivers. Incoming experience carves asymmetric patterns; thereafter perception flows down the main channel and the side tracks are invisible *prospectively*, though obvious *in hindsight* ("If — somehow — we get across to the side track, the route becomes obvious in hindsight. This is the basis of both humor and creativity"). Because the system's whole excellence is pattern-following, there is "an absolute and logical need for something like lateral thinking in order to cut across patterns" — provocation is not a party trick but a **logical necessity in an asymmetric patterning system**. ([debono.com — Serious Creativity article](https://www.debono.com/serious-creativity-article), [Wikipedia: Lateral thinking](https://en.wikipedia.org/wiki/Lateral_thinking))

This maps almost one-to-one onto an autoregressive LLM: high-probability tokens *are* the main channel; hindsight-obvious/prospectively-invisible *is* the definition of an idea the model won't sample unless forced sideways.

### 1.2 Provocation ("po")

"Po" = *provocative operation*: a prefix signaling "this statement is not offered for judgment; it is a stepping stone." A provocation is a **deliberately false, impossible, or absurd statement** about the situation, held open long enough to see where thinking lands after the jump. Canonical example: *"Po: the factory is downstream of itself"* → factories must take intake water below their own outflow → later actual legislation. ([Wikipedia: Po](https://en.wikipedia.org/wiki/Po_(lateral_thinking)), [Mycoted: Provocation](https://www.mycoted.com/Provocation))

**Five formal setup methods** (from *Serious Creativity*; examples from the [UCSD cheat sheet](https://cseweb.ucsd.edu/classes/fa11/cse118-a/creativity.pdf)):

| Method | Operation | Example |
|---|---|---|
| **Escape / negation** | Cancel a taken-for-granted assumption | "Po: houses have no roofs" |
| **Reversal** | Flip a relationship or direction | "Po: servers call clients" |
| **Exaggeration** | Push a quantity to an extreme (up or down) | "Po: programs are a single line of code" |
| **Distortion** | Scramble normal relations / temporal order | "Po: the program is written before the requirements" |
| **Wishful thinking** | Fantasy stated as fact ("wouldn't it be nice if…") | "Po: programs write programs" |

### 1.3 Movement — the half everyone skips

De Bono is emphatic: **provocation without movement is useless**. Movement is the trained alternative to judgment — instead of asking "is this true/good?", you ask "where does this take me?" Five formal movement techniques ([UCSD cheat sheet](https://cseweb.ucsd.edu/classes/fa11/cse118-a/creativity.pdf), [Shortform summary](https://www.shortform.com/blog/edward-de-bono-lateral-thinking/)):

1. **Extract a principle** — pull the underlying concept out of the provocation and re-implement it realistically.
2. **Focus on the difference** — what exactly differs between the provocation and current practice? The difference IS the idea seed.
3. **Moment-to-moment** — cinematically simulate the provocation happening, second by second; harvest whatever the simulation surfaces.
4. **Look for positives** — enumerate any benefits the provocation would have, then chase those benefits by sane means.
5. **Special circumstances** — find contexts in which the provocation would be literally sensible; those niches are markets/scenes.

### 1.4 Random entry (random word → forced bridge)

Pick a truly random noun (dictionary page + position, random table, timer) and **force a connection** to the focus. The rules that matter: the word must be genuinely random — *you may not choose it, and you may not swap it out when it feels hard* (choosing reintroduces the pattern you're trying to escape); list the word's attributes/associations first, then bridge each to the problem. De Bono's example: "photocopier + NOSE" → copier emits lavender smell when paper is low. Works because in a patterning system any two points can be connected, and the entry point determines which patterns get activated. ([Wikipedia: Lateral thinking](https://en.wikipedia.org/wiki/Lateral_thinking), [Mycoted](https://www.mycoted.com/Provocation))

### 1.5 Concept extraction / concept fan, and Challenge

- **Concept fan:** take any existing idea → pull back to the concept behind it → generate alternative ideas that serve the same concept → pull back again to a broader concept → fan out again. Turns one idea into a tree; systematically escapes "first implementation = only implementation." ([UCSD cheat sheet](https://cseweb.ucsd.edu/classes/fa11/cse118-a/creativity.pdf))
- **Challenge:** non-hostile "why is it done this way at all?" applied to something that isn't a problem. Cup handles exist because cups are hot → insulated wall, separate holder, drink cooler by design. Attacks the assumption *upstream* of the solution space. ([Wikipedia](https://en.wikipedia.org/wiki/Lateral_thinking))

### AS A PROMPT MOVE
- **Pattern:** `State the fence (list 5 assumptions everyone would make about X). For assumption k [externally chosen], produce a PO using [escape|reversal|exaggeration|distortion|wishful] [externally chosen]. Do NOT evaluate it. Apply each of the 5 movement operators to the PO; each must yield one concrete usable idea.`
- **Needs:** external random choice of assumption + provocation type (dice/RNG in the harness, not model choice); an explicit no-judgment zone; movement as a *mandatory* second stage so the provocation can't be quietly rounded back to sensible.
- **Random entry pattern:** `Random word (harness-supplied): "LIGHTHOUSE". List 6 attributes of a lighthouse. Bridge each attribute to the gummy beat. No skipping, no re-rolling.`
- **Test case:** "Po: the gummy peels the teenager" → *movement/extract principle: the peel transfers* → the teen peels the gummy and their own outline peels off like a sticker, revealing a more saturated, flavor-colored self underneath — one continuous peel gesture matched across both scales.

---

## 2. SCAMPER (Osborn → Eberle)

### Mechanics

Seven **transformation operators applied to an existing thing** — SCAMPER doesn't invent from zero; it mutates a defined subject. Published by Bob Eberle (1971) as a mnemonic packaging of Alex Osborn's 1953 idea-spurring checklist ("magnify? minify? rearrange? reverse?…"). ([The Decision Lab](https://thedecisionlab.com/reference-guide/philosophy/scamper), [Designorate](https://www.designorate.com/scamper-technique-examples-and-applications/))

| Op | Operation | Trigger questions |
|---|---|---|
| **S**ubstitute | Swap a component/material/person/rule | What else instead? Other ingredient, process, place, tone? |
| **C**ombine | Merge with another product/idea/purpose | What can be merged? What if two functions shared one body? |
| **A**dapt | Import a solution from another context | What else is like this? What could I copy from a different domain? |
| **M**odify (Magnify/Minify) | Change scale, frequency, attribute intensity | Exaggerate? Shrink? Change color, sound, duration, weight? |
| **P**ut to other uses | New user, new context, new function | Who else could use it? What else could it do as-is? |
| **E**liminate | Remove parts, simplify to the core | What's unnecessary? What if we halved it? What survives deletion? |
| **R**everse / Rearrange | Invert order, roles, orientation | Swap cause/effect, start/end, inside/outside, who-does-what? |

**How pros actually run it** ([SI Labs](https://www.si-labs.com/en/articles/scamper/), [Big Bang Partnership](https://bigbangpartnership.co.uk/scamper/)): (1) define the subject concretely in 3–5 sentences (a vague subject makes every operator vague); (2) timebox each operator (5–10 min) and **run operators you'd skip** — the uncomfortable ones (Eliminate, Reverse) produce the non-obvious output; (3) record everything without evaluation; cluster and select afterward. Key practitioner insight: the operators are *forced*, not browsed — you don't ask "which operator feels promising?", you take all seven in order, which is exactly the anti-modal discipline.

### AS A PROMPT MOVE
- **Pattern:** `Subject in 3 sentences: [the beat]. Apply ALL 7 operators in order. 3 ideas per operator, 21 total. No operator may be skipped or merged. Do not evaluate until all 21 exist.`
- **Needs:** a concrete decomposed subject (the beat has parts: teen, gummy, peel gesture, bite, reaction, setting, camera); per-operator quota; deferred judgment. Optionally randomize *which element* each operator hits (Substitute-the-setting vs Substitute-the-teen).
- **Test case:** *Reverse* — the impossible thing happens first and eating the gummy is what makes the world normal again: gravity is sideways in the hallway until the first bite snaps everything upright.

---

## 3. Synectics (Gordon & Prince)

### Mechanics

Developed at Arthur D. Little (1950s–60s) by W.J.J. Gordon and George Prince; the first system to treat the *irrational, metaphoric* phase of invention as trainable. Two complementary operations: **make the strange familiar** (analysis) and — the creative one — **make the familiar strange**: deliberately distort the everyday view of the problem so its assumptions become visible and movable. ([Jon Kolko's chapter summary of Gordon](https://www.jonkolko.com/phd/writing/25-04-22-papers-gordon-synectics-chapter-two), [ScienceDirect overview](https://www.sciencedirect.com/topics/psychology/synectics))

**Four analogy mechanisms** (Gordon, with his own examples):

1. **Personal analogy** — *become* the thing; empathetic identification with the object itself ("imagine yourself as the shaft in the motor," "be the molecule in the electrolyte"). Requires "loss of self"; the least comfortable and often the most productive.
2. **Direct analogy** — straight cross-domain comparison, "how is this like that?" Brunel got the caisson from watching a shipworm tunnel; Bell modeled telephone parts on the ear. Biology is the historically richest source domain.
3. **Symbolic analogy** — compressed conflict: capture the problem's essence as a two-word paradox or poetic image (oxymoron: "delicate armor," "safe attack"); Gordon's group solved a jack design via the "Indian rope trick" image. Fast, and "feels complete when properly selected."
4. **Fantasy analogy** — solve it as a dream/child/magic would, physics be damned ("how would trained insects close this space suit?"). Gordon recommends using fantasy **first** to *frame* the problem, then working back toward feasibility.

**Excursions and force fit** (Prince's session architecture): the problem owner states **goal wishes** ("I wish…"); the group generates **springboards** ("it would be nice if X, but we don't know how"); then takes an **excursion** — deliberately leaving the problem entirely to play in an unrelated domain via the analogies, random stimuli, drawing, "book title" paradoxes; then the crucial step, **force fit**: material harvested on the excursion *must* be connected back to the problem, however awkwardly, and embryonic ideas are developed rather than judged (itemized response: list what's good about it before what's wrong). ([Mycoted: Synectics](https://www.mycoted.com/Synectics), [Synecticsworld visual overview](https://synecticsworld.com/pdf/A_Visual_Overview_of_the_Synectics_Invention_Model.pdf))

### AS A PROMPT MOVE
- **Pattern (4-analogy ladder):` `Run all four in order, 2 outputs each: (1) BE the gummy — first-person sensory monologue of being peeled and eaten; (2) direct: how does anything in biology/geology peel? pick 3 mechanisms; (3) symbolic: compress the beat into a 2-word paradox; (4) fantasy: how would it happen in a dream with no physics? THEN force-fit each back into a shootable beat.`
- **Needs:** enforced order (personal analogy first-person is a genuinely different sampling region for an LLM); an explicit excursion phase where mentioning the product is *banned*; a mandatory force-fit step; itemized response (goods before flaws) as the evaluation gate.
- **Test case:** *personal analogy* — "I am the gummy; being peeled feels like taking off a jacket in summer" → force fit: as the teen peels the gummy, they and every stranger on the bus involuntarily sigh in relief, as if the whole bus just took its coat off.

---

## 4. Arthur Koestler — Bisociation (*The Act of Creation*, 1964)

### Mechanics

Koestler's claim: **every creative act — joke, discovery, artwork — is a bisociation**: the perceiving of a situation or idea "in two self-consistent but habitually incompatible frames of reference" (matrices) at once. Association moves *within* one matrix along its own rules and is therefore predictable; bisociation is the **collision/intersection of two matrices**, and the spark lives precisely at the intersection point. The same collision yields laughter (when discharged with self-assertive emotion — the punchline), science ("aha" — the two matrices fuse permanently: Gutenberg = wine press × coin seal; Darwin = Malthus × natural history), or art ("ah…" — the matrices are held in sustained juxtaposition). ([Wikipedia: The Act of Creation](https://en.wikipedia.org/wiki/The_Act_of_Creation), [The Marginalian](https://www.themarginalian.org/2013/05/20/arthur-koestler-creativity-bisociation/), [Solving for Pattern](https://www.solvingforpattern.org/2013/09/05/koestler-creativity-in-humour-science-art/))

Operationally important details:
- The two frames must EACH be **internally coherent** ("self-consistent") — a random mashup of nonsense isn't bisociation; each matrix comes with its own complete logic, vocabulary, and rules, and the creative object obeys *both simultaneously*.
- "**Habitually incompatible**" is the load-bearing phrase: the value comes from the *distance and tension* between the frames, not just their difference. Near frames give associations (puns, riffs); far frames give creation.
- Koestler stresses **ripeness**: in science the collision works when both matrices are independently well-developed. Translation: develop each frame fully *before* colliding them.

Bisociation is arguably the theoretical common denominator of everything else in this file: random entry, direct analogy, and forced connections are all *procedures for manufacturing matrix collisions on demand*. It has also been picked up in computational creativity research as an explicit anti-pattern-matching mechanism ([Grandomastery on bisociation vs. pattern-matching AI](https://www.grandomastery.com/post/bisociation-the-hidden-engine-of-original-thought-in-an-age-of-pattern-matching-ai)).

### AS A PROMPT MOVE
- **Pattern:** `Frame A = the beat's home frame (candy commercial: appetite, snap, color, teen cool). Frame B = [externally drawn from a curated far-domain list: e.g., submarine warfare, beekeeping, medieval bookbinding, air traffic control]. Step 1: write Frame B's internal logic in 5 rules, without mentioning candy. Step 2: produce 3 beats that obey BOTH rule sets simultaneously. A beat that merely decorates A with B's props fails; the impossible event must be *entailed* by B's logic operating inside A.`
- **Needs:** external random draw of the second frame (never let the model pick — it picks near frames); the "develop B independently first" ripening step; a both-logics test as the acceptance criterion.
- **Test case:** Frame B = air traffic control → the peeled gummy strip becomes a runway; the teen's bite must be "cleared for landing" — a tiny tower voice from the wrapper holds the bite in a holding pattern while lesser snacks are waved off.

---

## 5. TRIZ (Altshuller) — Contradiction Matrix + 40 Principles

### Mechanics

Derived by Genrich Altshuller from patterns across hundreds of thousands of patents. Core stance: invention = **resolving a contradiction without compromise**. Procedure: (1) state the **ideal final result** (IFR); (2) identify what blocks it as a contradiction — *improving parameter X worsens parameter Y* (39 standardized parameters: weight, speed, reliability, complexity…); (3) look up the X×Y cell of the **contradiction matrix**, which lists the 3–4 of the **40 inventive principles** that historically resolved that contradiction most often (Segmentation, Taking Out, Nesting, Asymmetry, Do It In Reverse, Blessing in Disguise, Self-Service, Cheap Disposables, Prior Action…); (4) instantiate those abstract principles in your domain. The matrix ranks principles by historical popularity, not fitness — practitioners advise starting with the suggested cells but sweeping **all 40** when stuck. ([TRIZ Journal: Contradiction Matrix and the 40 Principles](https://the-trizjournal.com/contradiction-matrix-and-the-40-principles-for-innovative-problem-solving/), [Resolving Contradictions with 40 Inventive Principles](https://the-trizjournal.com/innovation-tools-tactics/breakthroughdisruptive-innovation-tools/resolving-contradictions-40-inventive-principles/))

TRIZ's named enemy is **psychological inertia** — the domain expert's default channel — and its cure is the same as de Bono's: an *external, systematic* source of solution directions that the solver would not have sampled.

**Adaptation outside engineering — yes, and mature:** Darrell Mann et al. built a separate **business/management contradiction matrix** with re-glossed principles (Segmentation → franchising/customer segments; The Other Way Round → benchmark the worst performer; Blessing in Disguise → convert complaints into loyalty; Nested Doll → store-within-store), applied to service ops, education, finance, marketing/advertising. Working method in the business adaptation when no matrix cell fits: state the IFR, surface the contradiction, then **apply the 40 principles essentially at random** to generate solution families. ([TRIZ Journal: 40 Inventive Business Principles with Examples](https://the-trizjournal.com/40-inventive-business-principles-examples/), [xTRIZ: TRIZ for Business and Management overview](http://www.xtriz.com/TRIZforBusinessAndManagement.pdf), [TRIZ in digital marketing](https://blog.andemili.com/en/triz-method-applied-to-digital-marketing)) For creative/story use, the transferable core is: **name the craft contradiction explicitly, then resolve it with a principle rather than a trade-off.**

### AS A PROMPT MOVE
- **Pattern:** `State the beat's ideal final result. Name the contradiction as "improving X worsens Y" (e.g., "the more impossible the event, the less appetizing the candy"). Draw 3 principles at random from the 40 [harness supplies numbers, e.g., 13 The Other Way Round, 22 Blessing in Disguise, 25 Self-Service]. For each: resolve the contradiction — both X and Y improve — no compromise allowed.`
- **Needs:** the 40-principle list embedded as a lookup table; RNG for principle draw; the "no trade-off" acceptance rule (this is what kills the modal middle-ground answer).
- **Test case:** contradiction "more impossible = less appetizing"; principle 22 *Blessing in Disguise* → the impossible thing IS the appetite appeal: the peeled gummy floats away, the teen's annoyed jump to catch it becomes the hero bite in zero-g — the malfunction is the tastiest shot.

---

## 6. Morphological Analysis (Zwicky) / Forced Connections

### Mechanics

Fritz Zwicky (astrophysicist; dark matter, supernovae) formalized **General Morphological Analysis**: make the *entire* solution space explicit, then explore it exhaustively/combinatorially, so no region is skipped because it "didn't come to mind." Steps ([SI Labs: Morphological Box](https://www.si-labs.com/en/articles/morphological-box/), [Swedish Morphological Society — Ritchey, "Fritz Zwicky, Morphological Analysis and Futures Studies"](https://www.swemorph.com/pdf/gma.pdf), [Ness Labs: Zwicky box](https://nesslabs.com/zwicky-box)):

1. Formulate the problem as an open question.
2. Choose **independent parameters** (dimensions) — 5–7 recommended.
3. Enumerate 3–5 **values** per parameter (states, options).
4. Build the box; every path picking one value per parameter is a candidate solution (5 params × 5 values = 3,125 configurations).
5. **Cross-Consistency Assessment (CCA):** pairwise-check values and prune only genuinely contradictory pairs — this is judgment applied *structurally and late*, to pairs, never to whole ideas early.
6. Sample and develop surviving configurations — random draws are the standard creative sampling method ("randomly pick one value from each category"; "continue creating combinations even if you don't find anything valuable at first").

Zwicky's own first rule: *"be completely open-minded and consider even the most absurd-looking possibilities."* The box's power against the modal answer is arithmetic: the obvious idea occupies exactly one cell out of thousands, and the procedure forces you to visit others. "Forced connections" (Whiting/Crawford-style) is the degenerate 2-parameter case: attribute-list two arbitrary things and cross them.

### AS A PROMPT MOVE
- **Pattern:** `Parameterize the beat: WHERE the peel starts / WHAT peels besides the gummy / PHYSICS violated / WHO reacts / SENSORY register of the reveal / CAMERA behavior. 4-6 values each — values must span from mundane to absurd within each row. Harness rolls dice → pick value per row → write the configuration as a beat. Repeat for 5 random draws; develop all 5 before judging any.`
- **Needs:** LLM builds the box (it's good at enumeration); **RNG makes the draws** (if the model picks, it re-centers on the modal diagonal); a rule that each row's values must include at least one absurd entry; late-stage CCA-style pruning only after generation.
- **Test case:** draw = {peel starts at the horizon / the sky peels / sound becomes visible / a dog reacts / register: smell / camera is upside-down} → the teen peels the gummy and the dusk sky peels back in sync like a giant lid, releasing visible strawberry-scented sound waves only the dog notices.

---

## 7. Brainstorming — The Actual Research Record

### Osborn's rules and where they fail

Osborn (*Applied Imagination*, 1953): (1) **defer judgment**, (2) **go for quantity** ("quantity breeds quality"), (3) welcome wild/freewheeling ideas, (4) combine and improve on others' ideas — with the claim that groups so instructed would roughly double output. The rules themselves survive scrutiny; **the group format doesn't**. The Mullen, Johnson & Salas meta-analysis (1991; 20 studies, 800+ groups) found interacting brainstorming groups **significantly less productive than nominal groups** (same people ideating alone, output pooled) in both quantity and quality — and the deficit *grows* with group size. ([Wikipedia: Brainstorming](https://en.wikipedia.org/wiki/Brainstorming), [SI Labs: what research really shows](https://www.si-labs.com/en/articles/brainstorming/), [Crema: Beyond productivity loss in brainstorming groups](https://www.crema-research.ch/wp-content/uploads/2022/01/beyond-productivity-loss-in-brainstorming-groupsthe-evolution-of-a-question.pdf))

**Why groups underperform** (mechanisms, not vibes):
- **Production blocking** — only one person talks at a time; ideas are forgotten or self-censored while waiting; experimentally the dominant cause (Diehl & Stroebe 1987/1991). ([ResearchGate: Production Blocking and Idea Generation](https://www.researchgate.net/publication/222204736_Production_Blocking_and_Idea_Generation_Does_Blocking_Interfere_with_Cognitive_Processes))
- **Evaluation apprehension** — judgment is deferred officially but feared privately.
- **Social loafing / free riding** — pooled output diffuses responsibility.
- **Cognitive fixation / conformity** — hearing others' ideas narrows everyone onto the same categories (the group converges on ITS modal answer).

**What actually fixes it:**
- **Brainwriting** (e.g., 6-3-5: 6 people, 3 ideas, 5 minutes, rotate sheets): parallel silent generation removes blocking and apprehension while keeping stimulation from others' written ideas; reliably beats verbal groups. Electronic brainstorming (anonymous, simultaneous) scales this — large electronic groups can beat nominal groups. ([Leadership IQ: Brainstorming science](https://www.leadershipiq.com/blogs/leadershipiq/brainstorming-science-methods-and-best-practices), [SI Labs](https://www.si-labs.com/en/articles/brainstorming/))
- **Nominal-then-pool**: generate alone, converge together.
- **Quotas and persistence** — the anti-modal heavy artillery:
  - **Serial order effect**: within a session, originality of ideas rises with output position while fluency falls — one of the most replicated findings in divergent-thinking research; early ideas are the accessible/common ones, later ideas are drawn from remoter categories. ([PMC: serial order in divergent thinking](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5023093/))
  - **Creative cliff illusion** (Lucas & Nordgren, PNAS 2020, 8 studies): people *believe* their creativity declines across a session when it actually persists or improves; the misprediction causes them to quit early and perform worse. Fix: externally imposed persistence — quotas, timeboxes past the comfort point. ([PNAS: The creative cliff illusion](https://www.pnas.org/doi/10.1073/pnas.2005620117), [Lucas & Nordgren PDF](https://www.brianjlucas.com/uploads/1/8/5/6/18565392/lucas_nordgren_2020.pdf))
  - Practical rule of thumb derived from these: **the best idea is rarely in the first 10** — treat the first tranche as pattern-flushing, not as candidates.

**LLM translation is direct.** A single LLM completion behaves like a fixated group of one: first ideas = highest-probability = the shared modal categories. The proven fixes map cleanly: quotas well past comfort ("30 ideas; the first 10 don't count"), category-forcing ("no two ideas from the same mechanism class"), parallel independent generation with different seeds/frames then pooling (nominal-group structure across calls), and strict phase separation of generation and evaluation.

### AS A PROMPT MOVE
- **Pattern:** `Generate 30 beats. Rules: defer all judgment; ideas 1-10 are a flush pass (expected, allowed to be bad); ideas 11-30 may not reuse any mechanism from 1-10; tag each idea's mechanism class; wild ideas explicitly welcome. Only after all 30: pick the 3 least-expected that still land the appetite beat.`
- **Needs:** a hard numeric quota; an explicit "first-N-don't-count" clause; a no-repeat-category constraint (the LLM version of escaping fixation); optionally multiple independent runs pooled (nominal group).
- **Test case:** by idea #23 the obvious ones (gummy floats, teen levitates, colors explode) are spent, and you get: the peel doesn't come off the gummy — it comes off the *day*: the teen peels back the last five awkward minutes of class and eats them.

---

## Cross-System Synthesis — Anti-Modal Design Patterns for the Engine

The seven systems converge on **six reusable mechanisms**, each targeting the highest-probability-answer failure directly:

| # | Mechanism | Source systems | Engine implementation |
|---|---|---|---|
| 1 | **Exogenous randomness** — the stimulus must come from outside the generator and be non-refusable | de Bono random entry; morphological random draws; TRIZ random principle draw; Synectics excursion stimuli | Harness-side RNG picks words/frames/cells/principles; model is forbidden to re-roll or substitute |
| 2 | **Mandatory bridge / force fit** — the weird input must be metabolized, never discarded | de Bono movement (5 operators); Synectics force fit; Koestler both-logics test; Zwicky "develop the absurd cell" | Bridging is a required output field; "N/A" is an invalid completion |
| 3 | **Quotas past the comfort point** | Osborn quantity; serial order effect; creative cliff illusion; SCAMPER per-operator counts | Hard counts (e.g., 30) with "first 10 don't count" framing |
| 4 | **Systematic enumeration over selection** — visit ALL operators/cells, not the appealing ones | SCAMPER all-7 rule; Zwicky full box; TRIZ all-40 sweep | Iterate operator lists exhaustively; never ask the model which operator to use |
| 5 | **Structural judgment deferral** — separate phases, not attitudes | Osborn rule 1; PO's no-judgment zone; Synectics itemized response; Zwicky late CCA | Generation call and evaluation call are different prompts (or different turns); evaluation must list merits before flaws |
| 6 | **Frame distance control** — two self-consistent far frames, each developed before collision | Koestler bisociation ripeness; Synectics direct/fantasy analogy; de Bono escape from the fence | Curated far-domain lists; "write frame B's rules before touching the product"; near-frame outputs rejected |

**Diagnostic heuristic (de Bono/Koestler):** a good output is *prospectively improbable but retrospectively logical* — if the idea reads as obvious-in-hindsight AND you can name the pattern-jump that produced it, the mechanism worked. If it reads as obvious, period, the model stayed in the main channel; re-roll the exogenous stimulus, not the prompt wording.

---

### All sources

- https://www.debono.com/serious-creativity-article
- https://en.wikipedia.org/wiki/Lateral_thinking · https://en.wikipedia.org/wiki/Po_(lateral_thinking)
- https://www.mycoted.com/Provocation · https://www.mycoted.com/Synectics
- https://cseweb.ucsd.edu/classes/fa11/cse118-a/creativity.pdf (Serious Creativity cheat sheet)
- https://www.shortform.com/blog/edward-de-bono-lateral-thinking/
- https://thedecisionlab.com/reference-guide/philosophy/scamper · https://www.designorate.com/scamper-technique-examples-and-applications/ · https://www.si-labs.com/en/articles/scamper/ · https://bigbangpartnership.co.uk/scamper/
- https://www.jonkolko.com/phd/writing/25-04-22-papers-gordon-synectics-chapter-two · https://www.sciencedirect.com/topics/psychology/synectics · https://synecticsworld.com/pdf/A_Visual_Overview_of_the_Synectics_Invention_Model.pdf
- https://en.wikipedia.org/wiki/The_Act_of_Creation · https://www.themarginalian.org/2013/05/20/arthur-koestler-creativity-bisociation/ · https://www.solvingforpattern.org/2013/09/05/koestler-creativity-in-humour-science-art/ · https://www.grandomastery.com/post/bisociation-the-hidden-engine-of-original-thought-in-an-age-of-pattern-matching-ai
- https://the-trizjournal.com/contradiction-matrix-and-the-40-principles-for-innovative-problem-solving/ · https://the-trizjournal.com/40-inventive-business-principles-examples/ · https://the-trizjournal.com/innovation-tools-tactics/breakthroughdisruptive-innovation-tools/resolving-contradictions-40-inventive-principles/ · http://www.xtriz.com/TRIZforBusinessAndManagement.pdf · https://blog.andemili.com/en/triz-method-applied-to-digital-marketing
- https://www.si-labs.com/en/articles/morphological-box/ · https://www.swemorph.com/pdf/gma.pdf · https://nesslabs.com/zwicky-box
- https://en.wikipedia.org/wiki/Brainstorming · https://www.si-labs.com/en/articles/brainstorming/ · https://www.crema-research.ch/wp-content/uploads/2022/01/beyond-productivity-loss-in-brainstorming-groupsthe-evolution-of-a-question.pdf · https://www.researchgate.net/publication/222204736_Production_Blocking_and_Idea_Generation_Does_Blocking_Interfere_with_Cognitive_Processes · https://www.leadershipiq.com/blogs/leadershipiq/brainstorming-science-methods-and-best-practices
- https://www.pnas.org/doi/10.1073/pnas.2005620117 (Lucas & Nordgren, creative cliff illusion) · https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5023093/ (serial order effect)
