# Artist, Writer & Performer Techniques: Constraint, Chance, and Play

Research for the **creative engine** skill — techniques from working artists that make ideation genuinely divergent instead of predictable. Every section ends with **AS A PROMPT MOVE**: the concrete instruction pattern an LLM could execute, the randomness/constraint source it needs, and a one-line application to the test case:

> **Test case:** *a candy commercial beat where a teenager eats a peelable gummy and one impossible thing happens.*

---

## 0. The Shared Engine (read this first)

Every technique below attacks the same enemy from a different angle: **the author's taste** — the pull toward the first-associated, most-rehearsed, most-defensible idea. For a human that's habit and ego; for an LLM it's literally the mode of the distribution. The techniques divide into three mechanisms:

1. **Constraint** (Oulipo, Dogme 95): a rule so arbitrary it can't be satisfied by any stock answer, forcing search into unvisited regions. Queneau: Oulipians are *"rats who construct the labyrinth from which they plan to escape"* ([Wikipedia: Oulipo](https://en.wikipedia.org/wiki/Oulipo)).
2. **Chance** (cut-ups, surrealist games): external entropy injected mid-process, producing juxtapositions no intention could have planned. Burroughs: *"You cannot will spontaneity. But you can introduce the unpredictable spontaneous factor with a pair of scissors"* ([The Cut-Up Method of Brion Gysin](https://www.writing.upenn.edu/~afilreis/88v/burroughs-cutup.html)).
3. **Play / logical commitment** (Johnstone, UCB game, comedy heightening): NOT randomness — instead, take one small deviation and treat it with absolute deadpan logic. The originality comes from *rigorous consequence-following*, not from the deviation being wild.

Critical LLM note: **an LLM cannot self-generate real randomness.** Asked to "pick a random word" it picks a clichéd one. Every chance-based move below therefore names an *external entropy source*: a shuffle script, dictionary index math, `random.org`, a seeded RNG in Bash, a word list file indexed by dice roll, or hidden-context handoffs between subagents (the fold of the exquisite-corpse paper). Constraint-based moves don't need entropy — the constraint itself does the work — but they need *verification* (a checker that rejects outputs violating the rule), or the LLM will quietly drift back to taste.

---

## 1. Oulipo — Constraint as Generator

**Ouvroir de littérature potentielle** ("workshop of potential literature"), founded 1960 by Raymond Queneau and François Le Lionnais — writers *and mathematicians* who treated constraints as idea-triggering machines, not ornament. Their term *littérature potentielle*: "the seeking of new structures and patterns which may be used by writers in any way they enjoy" ([Wikipedia: Oulipo](https://en.wikipedia.org/wiki/Oulipo), [Poem Analysis: Oulipo](https://poemanalysis.com/movement/oulipo/)).

### Why arbitrary constraint produces non-obvious output

The mechanism is subtractive: a hard formal rule makes the habitual answer *illegal*. Perec could not write any of the sentences he would naturally have written for a 300-page novel once "no letter e" was in force (*La Disparition* / *A Void*) — and the constraint became thematically load-bearing (the missing *e* / missing *eux* = "them", the disappeared). The constraint doesn't just filter output; it **changes what the author goes looking for**. Crucially, the constraint is *arbitrary* — chosen for its structure, not its meaning — which is exactly why it escapes taste: taste can't have pre-optimized for it. A text written under constraint escapes the author's aesthetic defaults because the search is redirected before aesthetics get a vote.

### Key techniques

- **Lipogram** — exclude a letter (or several). Prisoner's constraint: exclude all letters with ascenders/descenders. The harder the excluded element is to avoid, the further from habit the output lands.
- **N+7 (S+7)** — devised by Jean Lescure: replace every noun with the seventh noun following it in a chosen dictionary. Purely mechanical; the dictionary is the entropy source; the offset (7) is arbitrary. Different dictionaries give different poems from the same source ([Sophie Herxheimer on N+7](https://poetryteapot.wordpress.com/wp-content/uploads/2024/07/n7articleformslexia.pdf)).
- **Snowball** — each word one letter longer than the last.
- **Queneau's *Cent mille milliards de poèmes*** (1961) — 10 sonnets, each page cut into 14 strips (one per line); any line 1 combines with any line 2, etc. → 10^14 valid sonnets. **Combinatorics as authorship**: write interchangeable modules, let selection explode the space.
- **Queneau's *Exercises in Style*** — the same trivial anecdote (a man on a bus, an altercation, a button) retold 99 times in 99 registers (telegraphic, olfactory, mathematical, opera-libretto…). Proof that *variation lives in treatment, not premise*.
- **Mathews' Algorithm** — rule-driven permutation of elements across a set of texts.
- **The clinamen** — the sanctioned swerve: Oulipians may break their own rule *when the rule would force a bad result*, e.g. take the 8th dictionary noun if the 7th is dead on arrival. The constraint generates; taste gets one veto per emergency — in that order. ([Writing in Company: Writing with constraints](https://writingincompany.substack.com/p/writing-with-constraints), [Gilliam Writers Group on Oulipo](https://www.gilliamwritersgroup.com/blog/the-oulipos-legacy-using-literary-constraints-to-innovate-writing))

### AS A PROMPT MOVE

- **Instruction pattern (constraint):** "Before ideating, adopt this arbitrary formal rule: {rule drawn from a rule deck — e.g. 'no idea may involve the mouth', 'every beat must be describable in exactly 6 words', 'the impossible thing must be silent', 'the camera may never move'}. Generate 5 ideas that satisfy it. Then run a checker pass: discard any idea that quietly violates the rule." Needs: a **rule deck file** + a **verification pass** (constraints decay without enforcement). One clinamen allowed, declared explicitly.
- **Instruction pattern (N+7):** "Write the obvious version of the beat. Extract its nouns. Replace each with the 7th-next noun from {wordlist} via script. Treat the mutated sentence as a literal brief." Needs: dictionary/wordlist + index arithmetic done in code, not by the model.
- **Instruction pattern (Exercises in Style):** "Hold the beat fixed. Retell it 10 times in 10 registers drawn from a register deck (nature documentary, security-cam footage, opera, unboxing video, crime-scene report…)." Needs: register deck + shuffle.
- **Instruction pattern (Queneau combinatorics):** "Write 5 interchangeable options for each slot — WHERE / WHO ELSE / THE PEEL / THE IMPOSSIBLE THING / THE BUTTON ENDING — then assemble 3 beats by rolling one option per slot." Needs: seeded RNG for slot selection.
- **Example:** Constraint "the impossible thing must be silent and the teen must never react" → *the teen peels the gummy and the peel keeps going — sofa, wall, sky peel back in one continuous spiral — while she chews, unbothered, in the un-peeled patch of world.*

---

## 2. Cut-Up Technique — Burroughs / Gysin Lineage

### The discovery and the protocol

Brion Gysin rediscovered the method in 1959 while slicing through layered newspapers used as a cutting mat; the accidental cross-column juxtapositions read better than the columns. He and Burroughs formalized it (*Minutes to Go*, 1960; *The Third Mind*, 1977) ([Wikipedia: Cut-up technique](https://en.wikipedia.org/wiki/Cut-up_technique)).

Burroughs' exact instructions, from *The Cut-Up Method of Brion Gysin* ([full text](https://www.writing.upenn.edu/~afilreis/88v/burroughs-cutup.html)):

> "Take a page. Like this page. Now cut down the middle and cross the middle. You have four sections: 1 2 3 4… Now rearrange the sections placing section four with section one and section two with section three. And you have a new page."

- **Fold-in variant:** fold two pages of linear text vertically in half, marry the halves, read across the seam.
- **Why it works, per Burroughs:** "All writing is in fact cut ups. A collage of words read heard overheard" — the scissors just make the recombination *explicit and subject to extension and variation*. "Images shift sense under the scissors: smell images to sound, sight to sound, sound to kinesthetic." And the divination claim: *"When you cut into the present the future leaks out."*
- The key discipline: **you don't keep everything.** The cut generates; the artist curates. Chance proposes, taste disposes — but only *after* the chance operation, never instead of it.

### The musicians' variants

([Open Culture: How Bowie, Cobain & Yorke used cut-ups](https://www.openculture.com/2015/02/bowie-cut-up-technique.html), [Far Out: how they wrote lyrics](https://faroutmagazine.co.uk/david-bowie-thom-yorke-kurt-cobain-lyrics-method/))

- **David Bowie** (from ~1972): "You write down a paragraph or two describing different subjects, creating a kind of 'story ingredients' list… then cut the sentences into four or five-word sections, mix 'em up and reconnect them." He called it "a kind of Western Tarot" — an oracle you interrogate, not an autopilot. Note the detail: he *seeds the pool deliberately* (multiple subjects → guaranteed cross-domain collisions), then cuts. In 1995 he and Ty Roberts built the **Verbasizer**, a program that auto-recombined sentences he typed in — the first digitized cut-up engine.
- **Kurt Cobain:** "My lyrics are total cut-up. I take lines from different poems that I've written" — self-corpus only, so the collisions stay in-voice.
- **Thom Yorke, *Kid A* (2000):** hit lyric-writer's block, wrote single lines on slips, **put them in a hat, drew them at random** while the band played, and sang them in drawn order. The hat decides sequence; the song structure disciplines the result.

### AS A PROMPT MOVE

- **Instruction pattern:** "Write 2–3 short paragraphs on *deliberately different subjects* (the brief's subject + 1–2 unrelated domains from a domain deck). Split all sentences into 4–6-word fragments. **Shuffle with a script** (never 'mentally'). Read the shuffled stream and pull the 3 collisions that spark; treat each collision as a beat premise." Needs: external shuffle (Bash/`sort -R`/seeded Python), and a seeded pool with intentional cross-domain material (Bowie's move). Variant: Yorke's hat = generate 20 one-line images across sessions/agents, shuffle, take the top 5 *in drawn order* as the beat's shot list.
- **Example:** Fragment pool = gummy-commercial copy + a citrus-orchard field guide + an astronaut training manual; shuffle yields "peel back the pressure suit / segments of noon light" → *the teen peels the gummy and the peel comes off like an airlock seal — the kitchen silently depressurizes, homework and cereal drifting up in citrus-colored light.*

---

## 3. Surrealist Games — Systematized Access to the Irrational

The Surrealists built party-game *protocols* for switching off conscious intention ([Wikipedia: Surrealist techniques](https://en.wikipedia.org/wiki/Surrealist_techniques), [A Book of Surrealist Games, Brotchie & Gooding](https://archive.org/details/a-book-of-surrealist-games-alastair-brotchie-mel-gooding)).

### Exquisite corpse (cadavre exquis)

Players write (or draw) in turn on folded paper, **each seeing only a sliver of the previous contribution** (for drawings: just the connecting lines at the fold). Named for its first output: "The exquisite / corpse / shall drink / the new / wine." The engine is **partial information**: each contributor acts locally-coherently on a fragment, and the global result is something no single mind would produce — coherent at every joint, alien as a whole ([Artnet on exquisite corpse](https://news.artnet.com/art-world/art-bites-surrealists-exquisite-corpse-2672024), [Georgetown English](https://english.georgetown.edu/exquisite-corpse/)).

### Automatic writing / drawing

Breton & Soupault, *Les Champs magnétiques* (1919): write at speed, without pause, without revision, before "logic takes over and rephrases it." Purpose: "free imagination by producing a creative process free of conscious control." The operative parameters are **speed and no-backspace** — velocity outruns the censor.

### Question-and-answer games & "irrational enlargement"

- **Conditionals:** one player writes an "If/When…" clause, the other — *without seeing it* — writes a future-tense consequence; unfold and join.
- **Irrational enlargement:** given an existing object, film, or scene, answer *irrational questions about what lies outside its frame* as if the facts already existed. The canonical instance: "Data toward the Irrational Enlargement of a Film: *The Shanghai Gesture*" in *L'Âge du cinéma* — the group answered questions about von Sternberg's 1941 film that the film never poses (what's in an unseen room, what a character eats, what happens to props off-screen), treating the fiction as a world with hidden depth ([Grokipedia: Adonis Kyrou](https://grokipedia.com/page/adonis_a_kyrou), [cineCollage: Surrealist Cinema](http://cinecollage.net/surrealism.html)). Sibling game: "Certain Possibilities Relating to the Irrational Embellishment of a City" — for each landmark: *conserve, displace, modify, transform, or suppress?* ([A Book of Surrealist Games](https://dokumen.pub/a-book-of-surrealist-games-1570620849-9781570620843.html)).
- **One into another:** describe object A entirely in the vocabulary of unrelated object B until they fuse.

### Paranoiac-critical method (Dalí)

Dalí's contribution was *interpretive*, not generative: induce a "paranoid" state in which the mind **over-reads** — sees the double image, the face in the rock — then use critical faculties to *fix and render* the delusion precisely. Two-stroke engine: irrational perception → rigorous, photorealistic execution. The craft is in painting the hallucination *convincingly* ([Babou 691: Dalí's surreal methods](https://babou691.com/2020/11/27/surreal-methods-of-salvador-dali/), [surrealismart.org: writing techniques](https://www.surrealismart.org/history/writing-techniques.html)).

Also in the toolbox: **decalcomania** (press wet paint, lift, interpret the blot), **frottage** (rubbings; Ernst), **cubomania** (cut an image into squares, reassemble at random), **entopic graphomania** (dot the impurities on a page, connect them) — all "generate texture noise first, find the image in it second."

### AS A PROMPT MOVE

- **Exquisite corpse:** "Run 3 subagents in sequence. Each writes one segment of the beat (setup / impossible turn / aftermath) seeing **only the last line** of the previous segment, not the brief's genre." Needs: enforced context isolation (subagents with truncated handoffs) — the fold in the paper. A single context window cannot play this game against itself.
- **Automatic writing:** "60-second sprint: stream 200 words of uncensored image-association from the trigger word 'peel' — no complete sentences required, no revision, no evaluation. THEN, in a separate pass, mine it for the 3 strangest concrete images." Needs: hard separation of generate-fast and judge-later turns (never simultaneous).
- **Irrational enlargement:** "The commercial already exists. Answer irrationally but confidently: What is in the teen's left pocket? What does the gummy dream about? What is behind the kitchen wall? Who manufactured the peel and what do they know? What happens in this kitchen at 3 a.m.? Build the beat from the best answer." Needs: a fixed question deck; questions must probe *outside the frame*.
- **Paranoiac-critical:** "Over-read the product: stare at the description of a peelable gummy until it 'is' something else (a fruit, an organ, a planet, a secret). State the double-image. Render the beat so both readings stay simultaneously true." Needs: none (interpretive move) — but demands the double image survive into the final frame.
- **Example (irrational enlargement):** Q: "Who manufactured the peel?" A: "The peel is grown, not made" → *the teen peels the gummy and plants the peel in the sugar bowl; by the time she swallows, a gummy tree has burst through the table, dropping ripe, glowing gummies into her friends' laps.*

---

## 4. Improv Theory — The Craft Closest to the Deliverable

### 4a. Keith Johnstone, *Impro: Improvisation and the Theatre* (1979)

([James Clear's summary](https://jamesclear.com/book-summaries/impro), [fluidself notes](https://fluidself.org/books/art/impro), [Improv Archive](https://improvarchive.org/books/impro-improvisation-and-the-theatre))

- **The "be obvious" paradox:** "The improviser has to realise that the more obvious he is, the more original he appears." People hunting for an "original" idea produce strained, interchangeable cleverness; "an artist who is inspired is being obvious. He's not making any decisions, he's not weighing one idea against another. He's accepting his first thoughts." Your obvious is not my obvious — the *specific* first thought is the fingerprint. Originality-seeking is a convergent behavior; obviousness-accepting is divergent. **For an LLM this inverts:** the model's first thought is everyone's obvious (the mode). The transferable move is not "take the first sample" but "take the first thought *after the constraint/entropy has displaced the start point*" — Johnstone-honesty downstream of an Oulipo/cut-up upstream.
- **Blocking vs. accepting:** an "offer" is anything a partner does; killing it ("blocking") "is a form of aggression" rooted in fear of losing control. "Good improvisers seem telepathic; everything looks prearranged. This is because they accept all offers made." Dull answers "keep the future safe" — safety is the enemy signature. Rule for the engine: **the generated weirdness is an offer; never walk it back, only build on it.**
- **Status transactions:** every line and movement implies status; the see-saw (one rises, the other falls) generates drama from nothing. High-status players block because they must control. A cheap variation crank: replay any beat with statuses reversed.
- **Reincorporation:** audiences gasp when a forgotten early detail returns transformed. Endings are not invented; they are *reincorporated*. (This is the comedy "button" too.)
- **Routines:** stories start by *interrupting a routine*, not by inventing content. Establish the mundane procedure, then break it — which is exactly the UCB base-reality logic below.

### 4b. UCB "Game of the Scene" — EXTRA DEPTH

The most direct existing craft theory for **"ordinary setup + one impossible rule + logical heightening."** Lineage: Del Close's ImprovOlympic Harold and *Truth in Comedy* (Halpern/Close/Johnson, 1994) — agreement, "follow the unusual thing," group mind ([Truth in Comedy](https://www.amazon.com/Truth-Comedy-Improvisation-Charna-Halpern/dp/1566080037), [Improv Archive: The Harold](https://improvarchive.org/formats/harold)) — codified by Besser/Roberts/Walsh in the *UCB Comedy Improvisation Manual* (2013) ([IRC Improv Wiki](https://wiki.improvresourcecenter.com/index.php?title=The_Upright_Citizens_Brigade_Comedy_Improvisation_Manual), [UCB Improv 201](https://ucbcomedy.com/training-center/improv-201/)).

**The full loop** ([Hoopla quick guide](https://www.hooplaimpro.com/quick-guide-game-of-scene), [There It Is pod: Finding the Game](https://www.thereitispod.com/post/2016/10/14/finding-the-game-in-the-scene)):

1. **Base Reality** — establish a *normal, specific, grounded* who/what/where via Yes-And. The base reality is the measuring stick: nothing can register as unusual until normal is defined. UCB warns: if your base reality is already weird ("having pizza in a space rocket"), the unusual thing must out-weird it — so keep the base boring. **Ordinary is load-bearing.**
2. **First Unusual Thing** — the first element that breaks the expectations set by the base reality. One. Singular. It's *found*, not forced — often it's just the first genuinely surprising choice anyone makes.
3. **Frame & Agree** — the other player *names/notices* the anomaly ("You're… also drunk? At 10 a.m.? In our session?") so both players (and the audience) lock onto the same game. Unframed anomalies dissipate.
4. **Rest the Game** — don't pile on immediately; return briefly to base reality so the anomaly stays figure-against-ground. Restraint preserves contrast.
5. **Explore** — the manual's revised mantra, displacing pure Yes-And: **"If this is true, then what else is true?"** Ask *why* the unusual thing is happening and derive its logical consequences *within the world's rules*. Exploration supplies the justification that makes each next escalation feel earned rather than random.
6. **Heighten** — raise the stakes/scale/commitment of the *same* unusual thing. Explore and heighten alternate in a **staircase**: heighten (step up) → explore/justify (tread) → heighten → explore… ([Hoopla](https://www.hooplaimpro.com/quick-guide-game-of-scene)). Kevin Mullaney's therapist example ([worked example](https://kevinmullaney.com/2011/05/02/game-of-the-scene-an-example/)): therapist overshares to match patient — kid problems → bedroom problems → "actually I'm drunk right now." Same game, three rungs, each *worse for the same reason*. His advice: once the pattern exists, **respect the pattern**; find variations by asking what *this* character, with *this* established behavior, would also do.
7. **Named failure modes:** **Second Unusual Thing** (introducing a new anomaly instead of heightening the first — now it's noise, not game) and **Crazy Town** (escalating magnitude without logic until the world has no rules left and nothing can be surprising). Also *gaming out too fast* — burning the top rung of the ladder in move two.

**Mapping to "one impossible visual rule, escalated":** base reality = the ordinary commercial world (kitchen, teen, gummy); first unusual thing = the ONE impossible visual rule; framing = the beat's first clear read of the rule; explore = derive the rule's physics ("if peels work like X, then Y must also…"); heighten = 2–3 escalations of the *same* rule, each logically justified, each bigger; forbidden = a second impossible thing, or escalation that abandons the rule's logic. This is a complete spec for the deliverable's shape.

### AS A PROMPT MOVE

- **Instruction pattern (game engine):** "(1) State base reality in 2 mundane sentences. (2) Introduce exactly ONE impossible rule. (3) FRAME it: one sentence where the world visibly registers it. (4) EXPLORE: list 4 answers to 'if this is true, what else is true?' — consequences derived from the rule's internal physics. (5) HEIGHTEN: 3 escalations of the same rule, each justified by an explore answer, ascending in scale. (6) VALIDATOR: reject if any second impossible thing appeared, or if an escalation can't cite which explore answer licenses it. (7) BUTTON: reincorporate a detail from the base reality." Needs: no entropy — needs the *validator* and the enforced one-rule budget. (Pair with a Section 1–3 move to choose a non-obvious rule.)
- **Instruction pattern (Johnstone status flip):** "Replay the beat with status reversed — the gummy/impossible thing holds high status, the teen low (or vice versa)." Needs: nothing; it's a deterministic transform that reliably yields a second distinct beat.
- **Example:** Base: teen at a bus stop, bored, peels a gummy. Impossible rule: *whatever the peel touches, peels.* Frame: the peel brushes the bench — the bench's paint peels off in one clean gummy-like coil. Explore: if surfaces peel, the world has a layer under it; the under-layer is brighter; peeling is contagious only via the peel. Heighten: sidewalk peels to reveal candy-glass, the bus peels to a brighter bus, the gray sky peels back to a ripe orange one. Button: she drops the peel in the trash — the trash can peels to reveal a slightly cooler trash can. One rule, staircase logic, no crazy town.

---

## 5. Filmmakers' Constraint Systems

### Dogme 95 — the Vow of Chastity (von Trier & Vinterberg, 1995)

Ten rules to "purify" filmmaking by banning the tools that let taste and money simulate quality ([Wikipedia: Dogme 95](https://en.wikipedia.org/wiki/Dogme_95), [full manifesto text](https://designmanifestos.org/lars-von-trier-and-thomas-vinterberg-dogme-95/), [StudioBinder overview](https://www.studiobinder.com/blog/dogme-95-rules-manifesto-films/)): location shooting only, props found on location; diegetic sound only; hand-held camera; color, no special lighting; no optical work or filters; no superficial action (no murders/weapons); no temporal or geographic alienation (here and now); no genre movies; Academy 35mm; **director uncredited**. The kicker is the pledge:

> "Furthermore I swear as a director to refrain from personal taste! I am no longer an artist… My supreme goal is to force the truth out of my characters and settings… at the cost of any good taste and any aesthetic considerations."

Two engine-relevant mechanics: (a) the rules **ban solutions, not subjects** — you can tell any story, you just can't reach for the default tools, so invention gets pushed into blocking, performance, and found circumstance; (b) it's a **signed public vow** with named rules — enforceability and identity ("a Dogme film") make the constraint stick. Constraint sets, not single constraints, define a *style space*.

### *The Five Obstructions* (2003) — constraint as adversarial gift

Von Trier orders his mentor Jørgen Leth to remake Leth's short *The Perfect Human* five times ([Wikipedia: The Five Obstructions](https://en.wikipedia.org/wiki/The_Five_Obstructions)):

1. **12-frame rule** — no shot longer than 12 frames (half a second), shot in Cuba, no set. Designed to destroy Leth's elegant long takes; instead the machine-gun cutting *energizes* the film. Leth: the obstruction became "a gift."
2. **The worst place in the world, unshown** — Leth must play the lead himself, eating a gourmet meal in Mumbai's red-light district without showing the location. Leth half-breaks the rule (translucent screen with the street visible through it) — the *partial violation* is the film's most powerful image.
3. **Total freedom** — offered as *punishment* for the rule-break. Freedom is the cruelest obstruction: with nothing to push against, Leth struggles most. (The clearest single datum in this whole document: for a skilled maker, "do whatever you want" is the weakest brief.)
4. **Remake it as animation** — a form Leth and von Trier both despise; solved by hiring rotoscope artist Bob Sabiston (*Waking Life*), turning contempt into beauty.
5. **Von Trier makes it; Leth must sign it** and read a voice-over von Trier wrote — surrendering authorship itself.

Meta-lessons: obstructions work best when **targeted at the maker's signature strengths** (take away the thing they'd default to); a near-failure against a hard rule beats a success with a soft one; and the constraint-giver/constraint-taker *dialogue* (propose → attempt → judge → re-obstruct) is itself the engine — a loop an orchestrator and a generator agent can literally run.

### Michel Gondry — the in-camera solution

Gondry commits to achieving effects **physically, in-camera** (stop-motion, forced perspective, puppetry, choreographed loops — LEGO in "Fell in Love with a Girl," the Escher-video for "Around the World," cardboard dreams in *The Science of Sleep*, "sweding" in *Be Kind Rewind*). When you can *see how a thing was made*, "it strains his creativity positively" — visible craft is a feature, and the whole set gets designed around the trick rather than the trick added in post ([IndieWire: Gondry masterclass](https://www.indiewire.com/features/general/michel-gondry-directing-masterclass-microbe-and-gasoline-science-of-sleep-1201702442/), [No Film School on the White Stripes videos](https://nofilmschool.com/2017/05/watch-how-michel-gondry-pulled-off-all-those-insane-effects-white-stripes-videos)). He shares with Jack White an explicit belief in restriction and minimalism, and says of his hero Lynch: "the most unexpected element should come from the most mundane story" ([Dazed interview](https://www.dazeddigital.com/art-photography/article/37823/1/candid-conversation-ingenious-director-michel-gondry-home-movie-factory)). The transferable move: **specify the impossible thing as a practical trick** — the seams do the charming.

### David Lynch — catching ideas

From *Catching the Big Fish* (2006) ([Wikipedia](https://en.wikipedia.org/wiki/Catching_the_Big_Fish), [Goodreads quotes](https://www.goodreads.com/work/quotes/1120870-catching-the-big-fish-meditation-consciousness-and-creativity)): "Ideas are like fish. If you want to catch little fish, you can stay in the shallow water. But if you want to catch the big fish, you've got to go deeper." Mechanics, not mysticism: (a) **desire is the bait** — you hold a wish/question patiently rather than forcing an answer; (b) you never get the whole film, you catch a **fragment** — an image with a feeling attached — and "when you catch one fish that you love, that fish will draw in another fish": fragments accrete and self-organize (this is literally how *Mulholland Drive* was assembled); (c) his depth practice is Transcendental Meditation — state-change before ideation, lowering the noise floor so faint signals surface ([Austin Kleon on Lynch's ideas](https://austinkleon.com/2020/09/24/david-lynch-on-ideas/), [The Culturium](https://www.theculturium.com/david-lynch-catching-the-big-fish/)). Lynch also abstracts *feeling* from *story* — impose the emotion first; plot is optional scaffolding.

### AS A PROMPT MOVE

- **Dogme vow:** "Adopt a named 5-rule vow for this batch (e.g. CANDY-DOGME: one location; no cuts; practical light only; the impossible thing must be achievable as an in-camera trick; no reaction shots). Sign it. Any idea violating a rule is disqualified, not patched." Needs: rule-set deck + validator; rules ban *techniques*, never subjects.
- **Five Obstructions loop:** "Generate the beat. An OBSTRUCTOR agent identifies its strongest/most habitual quality and issues a rule that bans exactly that. Regenerate. Repeat 3×; keep all versions." Needs: two roles (maker/obstructor) with the obstructor reading the maker's output — adversarial, targeted, iterative. (Also: never issue 'total freedom.')
- **Gondry:** "Design the impossible thing as an in-camera practical trick a clever crew could shoot for $500 — describe the rig, let the seams show." Needs: nothing; the feasibility constraint itself forces specificity.
- **Lynch:** "Do not pitch beats. Catch 10 fragments — single images with a feeling attached, no plot (e.g. 'a peel spiraling upward, dread'). Then pick the fragment you love and let it 'draw in' 3 more that belong to the same world. Only then assemble a beat." Needs: enforced fragment-before-story ordering; feeling named per fragment.
- **Example (Gondry):** *the peel comes off as a tiny spiral staircase — practical trick: an oversized gummy prop with a machined ramp inside — and a thumb-sized version of the teen walks down it out of her own hand, waving up at her.*

---

## 6. Comedy Writing Mechanics

- **Benign Violation Theory** (Peter McGraw): humor lives where something is simultaneously *a violation* (wrong, threatening, norm-breaking) and *benign* (safe, playful, distant). Too benign = boring; too violating = upsetting. Psychological distance (fiction, candy-world physics, low stakes) converts violations to benign ones ([Comedy Philosopher](https://comedyphilosopher.com/benign-violation-theory-in-comedy-defines-the-laughter-sweet-spot/), [Roxanna Elden's applied course](https://roxannaelden.com/2015/08/how-the-benign-violation-theory-can-make-your-writing-funnier-humor-writing-mini-course-class-2/)). For an ad beat this is a *tuning dial*: an impossible thing with zero violation is wallpaper; a beat that eats the teen is off-brand. Aim mid-dial (mild body horror rendered cute, mundane rules broken politely).
- **"What if X but Y" premise engines:** professional sketch/humor writers isolate the *premise* first — one incongruous collision stated in a sentence — before any structure ([Creative Stand-Up: Mechanics of Comedy](https://creativestandup.com/comedic-conflict-the-mechanics-of-comedy/)).
- **Escalation ladders** (Alex Baia, citing Mike Lacher): heightening = "expanding your premise in new and surprising ways that still connect coherently to what you've set up… finding new territory without jumping so far ahead that it feels contrived." Failure modes: predictable rungs, weak individual rungs, incoherent jumps, or a premise without "legs." Reference escalations: Key & Peele's "Dueling Hats" (each hat absurd in a *conceptually new way*, reactions intensifying in parallel) and Portlandia's "Colin the Chicken" (question the chicken → visit the farm → join the cult) ([How to Make Your Humor Heighten](https://comedybizarre.substack.com/p/how-to-make-your-humor-heighten), [Heightening in humor writing](https://medium.com/jane-austens-wastebasket/heightening-in-your-humor-writing-340f2ef3248a)). Sequencing rule: relatable rung first; each rung surprising *and* license-able from the last; the ladder converges with UCB's explore/heighten staircase.

### AS A PROMPT MOVE

- **Instruction pattern:** "State the premise as WHAT IF {ordinary gummy ritual} BUT {one rule from entropy source}. Rate the violation 1–10; retune to 4–6 (benign-violation midband) by adjusting stakes, cuteness, or distance — not by removing the rule. Build a 3-rung ladder where each rung is a *conceptually new expression* of the same rule (not just 'bigger') and names what licenses it. Reject any rung reachable by pure size increase."
- **Needs:** entropy for the BUT-clause; a violation-score self-check; the "conceptually new, not merely bigger" test per rung.
- **Example:** What if eating a gummy BUT peeling is a social contract → rung 1: the gummy peels the teen's sticker off her water bottle in polite exchange; rung 2: it neatly peels the afternoon off the calendar so she gets a free hour; rung 3: at checkout it peels the price off the display and hands the digits to the cashier — violation level ~5, same rule, three different conceptual territories.

---

## 7. Synthesis — Operational Grammar for the Engine

**The master pipeline these traditions jointly imply:**

1. **DISPLACE the starting point** (Oulipo constraint / cut-up collision / surrealist question / obstruction) — never let ideation begin at the distribution's mode. This is where entropy or arbitrary rules are mandatory.
2. **CATCH honestly** (Johnstone/Lynch) — take the first *live* fragment the displaced search surfaces; do not shop for cleverness; name its feeling.
3. **COMMIT to ONE anomaly** (UCB) — ordinary base reality + a single impossible rule, framed clearly. Budget: one. Second anomalies are bugs.
4. **HEIGHTEN by logic** (UCB explore/heighten + escalation ladders) — "if this is true, what else is true?"; staircase of 3 rungs, each conceptually new, each licensed by the rule's internal physics; benign-violation dial at 4–6.
5. **CLOSE by reincorporation** (Johnstone) — the button is an early detail returning transformed, not new material.
6. **CURATE after, never during** (Burroughs/clinamen) — chance and constraint generate; taste gets one bounded veto at the end.

**Entropy/constraint sources an LLM implementation actually needs** (because the model cannot self-randomize): seeded shuffle scripts (`python -c "random.seed(...)..."` / `sort -R`), dictionary + offset arithmetic (N+7), curated decks as files (rules, registers, domains, irrational questions, BUT-clauses) indexed by external roll, subagent context-isolation for exquisite-corpse folds, and a maker/obstructor two-agent loop for Five-Obstructions adversarial constraint. Constraints additionally need a **validator pass** — an explicit check that rejects rule-violating output — or the model reverts to taste within one generation.

**The single most load-bearing finding:** UCB's game of the scene is a complete, field-tested spec for the deliverable's exact shape — *ordinary setup + one impossible rule + logical heightening* — including its failure taxonomy (second unusual thing, crazy town, gaming out too fast). Use the other five traditions to choose a **non-obvious rule**; use UCB to **execute** it.
