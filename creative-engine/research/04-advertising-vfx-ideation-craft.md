# How Top Advertising / Commercial / VFX Creatives Actually Generate Ideas

Research for the creative engine skill. Test case used throughout: **"a teenager eats a peelable gummy and one impossible thing happens."**

Every framework ends with **AS A PROMPT MOVE** — the instruction pattern an LLM could execute, plus a 1-line application to the test case.

---

## 1. Named craft frameworks (the generative procedures)

### 1.1 James Webb Young — the 5-step combinatorial method (1939)

The oldest documented ad-ideation procedure, still the skeleton under everything else. Core axiom: *"An idea is a new combination of old elements, and the capacity to bring old elements into new combinations depends largely on the ability to see relationships."*

The five steps ([James Clear summary](https://jamesclear.com/book-summaries/a-technique-for-producing-ideas), [Farnam Street](https://fs.blog/a-technique-for-producing-ideas/), [The Marginalian](https://www.themarginalian.org/2012/05/04/a-technique-for-producing-ideas-young/)):

1. **Gather raw material** — *specific* (the product, the audience) and *general* (everything else you're curious about). The specific/general split matters: ideas come from crossing the two piles.
2. **Masticate** — work the facts over from different angles, try fitting pairs together, write partial ideas on cards even when they seem crazy.
3. **Drop it** — deliberately stop; do something stimulating and unrelated.
4. **The flash** — the idea arrives unbidden (Young: "out of nowhere, while shaving").
5. **Cold grey dawn of the morning after** — expose the idea to criticism, expand and adapt it to practical use.

The LLM-relevant insight: steps 1–2 are fully mechanizable. What Young calls "seeing relationships" is a forced-pairing operation between the specific pile and the general pile.

**AS A PROMPT MOVE:** *Build two lists first — 20 specific facts about the product (material, physics, ritual of eating, package, name) and 20 unrelated things the target audience knows deeply (memes, physics class, sports, skincare, video games). Then force-pair across the lists and describe the collision before judging it.*
Example: "peelable" (specific) × "screen protector peel videos" (general) → the teen peels the gummy and the whole visible world turns out to have a peelable protective film.

### 1.2 Luke Sullivan — *Hey Whipple, Squeeze This*: the working toolkit

Sullivan's book is the closest thing to a documented concepting procedure used inside agencies ([book](https://www.amazon.com/Hey-Whipple-Squeeze-This-Advertising/dp/1119819695), lesson digests: [Book Blabber](https://bookblabber.co.in/advertising-lessons/), [Copywriter Club interview](https://thecopywriterclub.com/creating-ads-luke-sullivan/), [Shortform](https://www.shortform.com/summary/hey-whipple-squeeze-this-summary-luke-sullivan)). The concrete moves:

- **Start with the truest thing you can say about the brand.** Sullivan: *"I don't care what the research says or what the client says or what the brief says, don't put pen to paper until you figure out the truest thing you can say about a brand. Usually the truth is something the client wants to cover up or minimize."* The flaw/awkward truth is generative, not the polished benefit.
- **Pose the problem as a question.** "A problem well-stated is a problem half-solved."
- **Inverse problem solving.** Study what the product *doesn't* do, who *doesn't* need it, when it's a waste of money — then reframe.
- **Cliché elimination as an explicit first pass.** Map the overused iconography of the category and get it out of your system by writing the clichés down *first*, deliberately, then banning them.
- **Do something "perfectly wrong."** Break a sacred category rule — "the more sacred the rule, the better" — but execute the violation with precision.
- **Visual manipulation exercise.** Physically coax visuals out of the product: rotate it, stretch it, morph it, collide it with other icons.
- **Volume before judgment.** Write 100 taglines fast; cluster them on a wall; look for patterns; edit ruthlessly *later*. "Until an idea grows, don't look for what's wrong. Look for what's right."
- **Precise strategies liberate.** "Vague strategies inhibit. Precise strategies liberate." A tight fence produces wilder ideas than an open field.

**AS A PROMPT MOVE:** *Before ideating: (1) state the truest/awkwardest thing about the product, (2) list 10 category clichés and ban them, (3) name the most sacred rule of the category and generate 3 ideas that break exactly that rule, precisely.*
Example: truest thing about a peelable gummy — "you play with your food before eating it; the peel is the point, the eating is an afterthought" → the impossible thing happens during the *peel*, not the bite (breaking the sacred candy rule that magic happens on tasting).

### 1.3 Dave Trott — *Predatory Thinking*: upstream reframing

Trott's move is not idea generation but **problem substitution**: when you hit a problem you can't solve, "get upstream of it" — change the context until it becomes a problem you *can* solve ([Trott's book page](https://davetrott.co.uk/book/predatory-thinking-a-masterclass-in-outwitting-the-competition/), [ProCopywriters review](https://www.procopywriters.co.uk/2013/08/predatory-thinking-by-dave-trott/), [LSE lecture](https://www.lse.ac.uk/lse-player/predatory-thinking)). Question the brief before answering it; go upstream to the business problem before touching the advertising problem. His canonical examples reframe *whose behavior* the problem lives in (Sweden's prostitution law: stop targeting supply, target demand).

**AS A PROMPT MOVE:** *Before generating executions, generate 5 alternative statements of what the ad actually has to accomplish, each locating the problem in a different place (the product, the buyer, the moment of use, the category, the culture). Ideate from the most surprising restatement.*
Example: restate "make a spot about the gummy" upstream as "make peeling something in public a flex" → the impossible thing is a *social* event: when she peels it, everyone in the food court involuntarily stands up like it's an anthem.

### 1.4 George Lois — the Big Idea discipline

Lois's *Damn Good Advice* rules ([Alex Murrell summary](https://www.alexmurrell.co.uk/summaries/george-lois-damn-good-advice), [Fast Company](https://www.fastcompany.com/1680316/7-pieces-of-damn-good-creative-advice-from-60s-ad-man-george-lois), [Agency Review interview](https://the-agency-review.com/lois/)):

- **Words first, visuals second.** "Start with the word. A big campaign can only be expressed in words that lend themselves to visual excitement." Write the idea as a line *before* trawling for images.
- **The stun test.** "Any great creative idea should stun momentarily — it should seem to be outrageous."
- **The three-sentence limit.** "After three sentences of explanation, people's eyes glaze over." If the idea needs more, it isn't one.
- **Steal from the client's own mouth.** Listen hard when they describe the business; the line is often said out loud by someone who doesn't know it's the line.
- **1–3 minds, not committees.** "Collective thinking usually leads to stalemate or worse."

**AS A PROMPT MOVE:** *Generate the idea as a ≤12-word verbal line FIRST (a line that "lends itself to visual excitement"), then derive the image from the line. Reject any candidate that needs more than 3 sentences to explain, or that doesn't momentarily stun.*
Example: line first — "The peel remembers being a snake." — then visualize: the discarded spiral peel slithers off the table and the teen and the peel regard each other.

### 1.5 John Hegarty — zag, juxtaposition, and the poster test

Hegarty (BBH) built a career on **structural opposition**: "When the world zigs, zag" — the black sheep against the white flock, made for Levi's black denim ([Destination Innovation](https://www.destination-innovation.com/world-zigs-zag/), [Uncensored CMO episode](https://uncensoredcmo.com/episode/48), [Hegarty on Advertising](https://www.thamesandhudson.com/products/hegarty-on-advertising)). Attendant principles: "An obstacle is an opportunity for creativity"; ideas must be reducible to a poster — one frame, instantly legible; juxtaposition as the basic engine of visual interest ([Hegarty on LinkedIn](https://www.linkedin.com/posts/sir-john-hegarty-a1310a92_juxtaposition-advertising-art-activity-7163577658717515777-fTEh)).

**AS A PROMPT MOVE:** *First write down what every competitor's ad in this category looks and sounds like (the "zig"); then require each idea to invert at least one structural axis (tone, palette, tempo, who's happy, what the product does). Kill any idea that can't be drawn as a single poster frame.*
Example: candy ads zig = loud, saturated, ecstatic → zag: a near-silent, muted, Bergman-grey kitchen where one quiet impossible thing happens when the gummy peels — the only color in frame is the fruit flesh inside.

### 1.6 Product truth → exaggeration, and visual metaphor construction

The standard agency operator chain, documented across craft guides ([EDUCBA advertising techniques](https://www.educba.com/advertising-techniques/), [Penji visual metaphor examples](https://penji.co/visual-metaphor/), [thebrief.ai](https://www.thebrief.ai/blog/visual-metaphors/), [LinkedIn: power of exaggeration](https://www.linkedin.com/pulse/power-exaggeration-advertising-kazi-mofrad-muntasir)):

1. Pick ONE product truth (benefit, problem it solves, physical attribute, ritual of use).
2. Choose an axis: exaggerate the **benefit** (Red Bull literally gives you wings), the **problem** (life without the product as apocalypse), or the **physical attribute** (giant sunscreen tube as a literal shield).
3. Push "beyond reality and reason" — the craft term of art is taking it to its *extreme conclusion*, not just making it bigger.
4. Or run the metaphor operator: find the thing in the world that already *is* what the product does, and fuse them in one image (metaphor must read in one frame — "tell a compelling story within a single frame").

Confirmed live at Skittles: group CD Brian Culp on the Gummies campaign — *"We take an insight about Skittles Gummies being softer than other gummies to an extreme conclusion at 'an uncomfortably soft level'"* ([Marketing Dive](https://www.marketingdive.com/news/campaign-trail-skittles-stays-surreal-for-uncomfortably-soft-gummies/820683/)). Note the phrase **extreme conclusion**: not "softer," but "so soft it's uncomfortable" — exaggeration pushed past pleasant into a new emotional register.

**AS A PROMPT MOVE:** *Enumerate the product's literal physical truths one per line. For each, ask: "what is the extreme conclusion of this?" — and keep pushing past the pleasant version until the exaggeration changes emotional register (delight → unease → awe).*
Example: truth "it peels like a fruit" → extreme conclusion: everything the teen owns is revealed to be peelable — phone, skateboard, best friend — and the gummy is the only thing that's *supposed* to be.

### 1.7 The disproportionate-response scale (escalation ↔ understatement)

Two mirrored comedy operators, both category workhorses:

- **Law of Disproportionate Response** ([TV Tropes](https://tvtropes.org/pmwiki/pmwiki.php/Main/LawOfDisproportionateResponse)): tiny trigger → enormous reaction. The humor is the *gap*, not the size.
- **The inverse — deadpan understatement** — is the actual signature of the best transformation spots: enormous event → tiny reaction. Skittles codified it: *"add a little bit of magic to a pretty mundane world, and everyone treats that magic like it's pretty normal"* (Culp, [Marketing Dive](https://www.marketingdive.com/news/campaign-trail-skittles-stays-surreal-for-uncomfortably-soft-gummies/820683/)).

The generative dial: pick the size of the impossible event, then *independently* pick the size of the reaction. Matching sizes = boring. The two mismatch directions produce two different genres (farce vs. deadpan surrealism).

**AS A PROMPT MOVE:** *For each scenario, specify event-magnitude and reaction-magnitude as separate 1–10 numbers and require |event − reaction| ≥ 5. Generate both mismatch directions.*
Example: event 9 / reaction 1 — the peeled gummy opens a portal to a citrus dimension in the cafeteria; the teen's friend says "you gonna eat the peel?" Event 1 / reaction 9 — the gummy peels slightly crooked; the school holds a candlelight vigil.

### 1.8 Comedic heightening — "the game" and the ladder

Sketch/improv craft that commercial writers use explicitly (Old Spice, Skittles writers came from this tradition). From Alex Baia's heightening breakdown ([Comedy Bizarre](https://comedybizarre.substack.com/p/how-to-make-your-humor-heighten)):

- Heightening = "expanding your premise in new and surprising ways that still connect coherently" to what came before. One rule, escalated — never a second rule.
- Failure modes are diagnostic: predictability (same-size beats), incoherence (new rules midstream), weak premise ("no legs").
- **Laddered escalation**: don't jump to maximum absurdity; establish incremental believable steps so the final absurd beat feels *earned*.
- Track **character emotional reaction** as its own escalating line — "the response to escalation matters as much as the escalation itself."

**AS A PROMPT MOVE:** *State the ONE rule of the spot in a sentence. Then write a 4-beat ladder where each beat applies the same rule to a bigger/stranger domain, with the protagonist's reaction escalating on its own track. Reject ladders that introduce a second rule.*
Example: rule "whatever the peel touches becomes peelable" → beat 1: the table gets a peel-tab; beat 2: the cafeteria wall; beat 3: the sky peels back one corner like a sticker; beat 4: the teen finds the tab on the back of their own neck — and shrugs, eats the gummy.

### 1.9 "The ad behind the ad" — concept vs. execution discipline

Creative-direction practice: the pitched script is never the unit of evaluation; the CD asks what the *underlying* reusable idea is. Formalized in concepting guides: "the concept isn't the ad itself — it's the reason the ad exists," one ownable idea "simple enough to express in one sentence yet flexible enough to adapt across formats" ([B2W concepting guide](https://www.b2w.tv/blog/concepting-in-advertising), [Big Idea, Wikipedia](https://en.wikipedia.org/wiki/Big_Idea_(marketing))). The practical test: **can the idea generate ten more executions?** Skittles' universe, Haribo's voice-swap, and Snickers' possession-by-hunger each spawned dozens of spots because the *platform* was the idea, not the script.

**AS A PROMPT MOVE:** *For every scenario generated, force-extract the one-sentence platform beneath it ("the ad behind the ad") and test: write 3 more different executions from that platform in one line each. If you can't, it's an execution, not an idea — mine it for its platform and regenerate.*
Example: scenario "the peel slithers away" → platform: "the peel has its own life after the candy is eaten" → 3 more: peels form a tiny civilization under the bed; a peel gets a job; peels migrate south in autumn.

---

## 2. The transformation-spot genre: case mechanisms (how each idea was findable)

### 2.1 Cadbury "Gorilla" (Fallon, 2007) — reframe the brief, then trust an off-topic collision

- **The reframe was the engine.** After the salmonella scare, marketer Phil Rumbol asked for an ad "as enjoyable to consume as a bar of Cadbury's chocolate" — Fallon formalized it: "all communications should be as effortlessly enjoyable as eating the bar itself" ([Wikipedia](https://en.wikipedia.org/wiki/Gorilla_(advertisement)), [Marketing Week](https://www.marketingweek.com/cadbury-gorilla/)). This moves the ad's job from *describing* joy to *being* joy — the product becomes the sponsor of the feeling, not the subject.
- **The image came from an off-topic argument.** Juan Cabral was arguing about the best drum solo of all time, said Phil Collins was "animalistic, he's like a gorilla drumming" — and the image stuck; he went home "with a burning desire" to write it ([AdWeek AgencySpy](https://www.adweek.com/agencyspy/juan-cabral-and-his-inspiration-to-the-cadbury-gorilla/), [Marketing Week](https://www.marketingweek.com/cadbury-gorilla/)). The idea pre-existed the brief; the reframed brief made it *admissible*.
- **The wrapper legitimized it**: "Glass and a Half Full Productions" framed the spot as entertainment content, so "no chocolate on screen" was a feature ([D&AD case study](https://www.dandad.org/insights/awards/cadbury-gorilla-case-study-insights)).
- Mechanism label: **feeling-transfer** — identify the emotion the product delivers, make 60 seconds of that emotion at maximum purity, attach logo.

**AS A PROMPT MOVE:** *Name the exact feeling of consuming the product (not the flavor — the feeling). Generate scenes that ARE that feeling at maximum purity with the product absent until the endframe.*
Example: peeling feeling = illicit tiny satisfaction → a spot that is 30 pure seconds of the world's most satisfying impossible peel (a lake peels off its reflection), gummy only at the end.

### 2.2 Sony Bravia "Balls" (Fallon, 2005) — the claim becomes a test; the image comes from childhood

- CD Richard Flintham wanted to dramatize "Colour like no other"; the creatives' stated logic: *"if Bravia has the best colour then we need to create a test to prove that"* — 250,000 bouncy balls down a San Francisco hill was the most beautiful possible test ([D&AD case study](https://www.dandad.org/insights/awards/sony-balls-case-study-insights), [esloganmagazine](https://en.esloganmagazine.com/bouncing-balls-by-sony/)).
- Cabral: "it was one of those ideas where you didn't need to write a script — there was no real narrative... The idea is something that's in every child's mind — to throw things down those steep streets and see what happens" ([Campaign](https://www.campaignlive.co.uk/article/close-up-live-issue-fuglsig-lets-balls-fly-sony-braviatv-ad/526360)).
- Shot 100% in-camera by Nicolai Fuglsig, six cameras, riot gear, 32 damaged cars — the *realness* is the persuasion ([esloganmagazine](https://en.esloganmagazine.com/bouncing-balls-by-sony/)).
- Mechanism labels: **claim → staged proof-event** ("design the world's most beautiful test of the claim") and **childhood-impulse mining** (ideas every kid already had, executed at adult scale).

**AS A PROMPT MOVE:** *Turn the product claim into a physical test a child would invent ("what would a 9-year-old do to prove this?"), then stage that test at absurd scale with documentary realness.*
Example: claim "it really peels" → a kid-logic test at scale: a stadium of teens synchronized-peeling one city-block-sized gummy, news-helicopter coverage.

### 2.3 Skittles "Taste the Rainbow" (TBWA\Chiat\Day, 2004–present) — a rulebook, not a gag file

The most explicitly documented surrealism *system* in the category ([Creative Review oral history](https://www.creativereview.co.uk/an-oral-history-of-skittles-taste-the-rainbow/), [Boston Waves case study](https://www.bostonwaves.com/post/skittles-taste-the-rainbow-campaign-a-case-study-in-surreal-marketing), [Marketing Dive](https://www.marketingdive.com/news/campaign-trail-skittles-stays-surreal-for-uncomfortably-soft-gummies/820683/)). The rules writers Scott Vitrone and Ian Reichenthal (and successors) work inside:

1. **Parallel universe, mundane register**: magic events (Skittles rain indoors, a man's touch turns everything to Skittles, a Skittles tree grows from a boy's stomach) are treated as unremarkable by everyone on screen.
2. **A slight bit of tragedy**: "there's always a slight bit of tragedy where maybe the magic didn't end up panning out like someone in the spot would have hoped" — the Midas-touch man can't hold his newborn. The tragedy is the memorability engine; pure whimsy evaporates.
3. **Product attribute → extreme conclusion** (see §1.6): softness → "uncomfortably soft" → a balloon-animal dog scraping itself on carpet.
4. **Brand voice over audience trend**: "Gen Z is not the idea: they're the target... Skittles is the brand and Skittles is the voice" (CD Katie Bero).
5. **Practical over CGI**: puppets with digitally-removed puppeteers, because slightly-wrong physical texture *is* the unsettling tone.

Mechanism label: **one-attribute literalization + deadpan world + a cost.** Every classic Skittles spot is (product attribute made physically literal) + (nobody impressed) + (someone quietly pays a price).

**AS A PROMPT MOVE:** *Generate: attribute → literal physical rule → who benefits → who quietly pays a price for the magic → everyone underreacts. Require the tragedy beat.*
Example: "peelable" literalized → a teen who can peel anything open, beloved at parties for peeling pistachios and stuck jars — but he can never wear a jacket again; zippers weep at his approach. Nobody finds this strange.

### 2.4 Old Spice "The Man Your Man Could Smell Like" (W+K, 2010) — audience paradox + monologue escalation

- **The strategic paradox generated the premise**: 60% of body-wash purchases are made by women → address the woman about the man, in one continuous seduction-parody ([D&AD case study](https://www.dandad.org/insights/awards/old-spice-case-study-insights), [Wikipedia](https://en.wikipedia.org/wiki/The_Man_Your_Man_Could_Smell_Like)).
- **Radio-first writing**: Craig Allen and Eric Kallman wrote it as pure dialogue before any visual — "The first words Craig typed were 'Hello ladies'... It was almost like a radio script" ([Muse by Clios oral history](https://musebyclios.com/advertising/behind-the-towel-an-oral-history-of-the-legendary-old-spice-ad/)).
- **Escalation as location/reality shifts under a constant register**: bathroom → boat → horse; tickets → diamonds; the voice never changes while reality mutates behind him. Textbook one-rule ladder (§1.8).
- **The ending was transplanted from a rejected script**: "I'm on a horse" was scavenged from a dead idea and stapled on ([Muse by Clios](https://musebyclios.com/advertising/behind-the-towel-an-oral-history-of-the-legendary-old-spice-ad/)) — dead ideas are an inventory, not waste.
- **Seamlessness sells impossibility**: Tom Kuntz shot it as one apparent take, "fairly anti-CGI when it doesn't have to be used" — the continuous shot makes the impossible transitions feel like sleight of hand rather than VFX.

**AS A PROMPT MOVE:** *Find the paradox in who buys vs. who uses, address the buyer; keep one element rigidly constant (voice, gaze, deadpan) while swapping the world behind it in 3 escalating jumps; harvest endings from your rejected ideas pile.*
Example: mom buys the gummies, teen eats them → the teen addresses the camera ("Hello, moms") deadpan while each peel teleports him somewhere a mom would approve of: library, piano recital, the 1950s.

### 2.5 Guinness "Surfer" (AMV BBDO, 1999) — constraint-flip + collision of two truths + image scavenging

Walter Campbell's own account ([Campaign: making of 'Surfer'](https://www.campaignlive.co.uk/article/campaign-making-guinness-surfer/1718803), [creative.salon 25-year piece](https://creative.salon/articles/features/guinness-surfer-learnings-qotw)):

- **The brief forbade the idea's raw material**: "the extended pour time shouldn't be mentioned... a potential barrier" — Campbell went straight at the forbidden thing.
- **Two old elements collided** (pure Webb Young): the heritage line "Guinness is good for you" × the pour-time problem → "Good things come to those who wait." The waiting *is* the reward.
- **The image was scavenged, not invented**: researching Neptune for a different spot, Campbell hit Walter Crane's painting of white horses in surf and "immediately knew" — the surfer-with-horses image was a found collision between an art-history image and the waiting theme.
- **Craft volume**: ~2,000 music tracks auditioned before Leftfield's "Phat Planet" ("it sounded underwater").

Mechanism labels: **flip the fence** (the constraint IS the idea), **collision of two brand truths**, **image scavenging from adjacent research**.

**AS A PROMPT MOVE:** *List everything the brief forbids or the client is embarrassed by; generate one idea that celebrates each forbidden thing. Separately, collide the brand's oldest line/asset with its newest problem.*
Example: forbidden truth "peeling is slow, you play with your food" → celebrate the wait: the impossible thing (the room filling with orbiting fruit-moons) only happens for teens patient enough to peel it in one unbroken spiral.

### 2.6 Michel Gondry (Levi's "Drugstore," Smirnoff "Smarienberg") — dream capture + technique-first ideation

- Gondry's documented sources: systematic **dream journaling** ("remembering my dreams is a big part of my life... some of my dreams are really cool stories"), including lucid-dream "experiments" that became scenes ([IndieWire masterclass](https://www.indiewire.com/2016/07/michel-gondry-directing-masterclass-microbe-and-gasoline-science-of-sleep-1201702442/), [No Film School](https://nofilmschool.com/2016/07/michel-gondry-masterclass)).
- **Technique-first ideation**: "I always wanted to be an inventor... when I bought my first camera, I realised I could be both of those things combined" — he invents an in-camera trick (graphic match-cuts through a vodka bottle in "Smarienberg," proto-bullet-time in 1996), then finds the story the trick makes possible ([Bold Content: 8 Gondry ads](https://boldcontentvideo.com/2015/06/11/8-great-tv-ads-directed-by-michel-gondry/), [AdForum](https://www.adforum.com/talent/4713-michel-gondry/work/5291)).
- **Commit in-camera**: "if there's something to be discovered, you want it discovered when the camera is running... you have to commit while shooting it" — constraint of physical execution disciplines the fantasy.

Mechanism label: **the trick precedes the story.** A named impossible *technique* ("the camera passes through the product," "time runs at two speeds in one frame") is itself a generative seed.

**AS A PROMPT MOVE:** *Generate 10 impossible camera/edit/physics TECHNIQUES first (no story), then for each ask what story only this technique could tell.*
Example: technique "match-cut through the inside of things" → the camera dives through the gummy's peel and emerges out of the peel of every other object in the teen's life — locker, moon, Tuesday.

### 2.7 Snickers "You're Not You When You're Hungry" (BBDO, 2010) — universal human truth → identity mechanic

BBDO's global focus groups surfaced the universal truth that hunger changes personality ("hangry"); the leap was making it an **identity-swap mechanic**: hungry you is literally a different person (Betty White tackled in the mud), fixed by the product ([The Drum](https://www.thedrum.com/news/2010-bbdo-new-york-creates-youre-not-you-when-youre-hungry-campaign-snickers-with), [B&T Cannes account](https://www.bandt.com.au/cannes-lions-heres-how-bbdo-and-snickers-figured-out-youre-not-you-when-youre-hungry/), [System1 retrospective](https://system1group.com/ad-of-the-week/flashback-fifteen-years-of-snickers-modern-classic)). The platform is a *casting engine*: infinite executions by choosing who "hungry you" is. Note this is the candy category's biggest transformation trope — the engine should know it both as a model and as a cliché (§4).

**AS A PROMPT MOVE:** *Find a universal human truth about the consumption moment, then convert it into a mechanic with a slot ("you become ___ until you eat it") that can be recast infinitely.*
Example: truth "peeling demands total focus" → while peeling, the teen becomes the most careful person on Earth — bomb squads recruit him mid-peel.

### 2.8 Sour Patch Kids "Sour Then Sweet" — product structure = narrative structure

The candy's literal taste sequence (sour coating, sweet interior) became a two-beat character arc: the Kid commits mischief (sour), then makes amends (sweet) ([Shorty Awards case](https://shortyawards.com/7th/sour-then-sweet-hijinks), [Wikipedia](https://en.wikipedia.org/wiki/Sour_Patch_Kids)). Decades of executions from one isomorphism. Mechanism label: **temporal structure of eating → plot structure of spot.** This is directly applicable to a *peelable* gummy: the product has a built-in two-act structure (outside/inside, before/after the peel) begging for narrative mapping.

**AS A PROMPT MOVE:** *Write the physical timeline of consuming the product as numbered stages; map each stage to a story beat; the impossible thing must respect the product's own sequence.*
Example: stages grip → peel → reveal → eat map to: ordinary world → the world's skin loosens → the true world beneath → the teen swallows the secret.

### 2.9 Haribo "Kids' Voices" — single incongruity, infinite re-execution

Adults in maximally adult settings (boardroom, locker room) speak about gummies in dubbed children's voices ([MediaPost](https://www.mediapost.com/publications/article/296495/new-adults-with-kid-voices-haribos-version-of-b.html), [Haribo 10-year retrospective](https://www.haribo.com/en-us/news/haribo-celebrates-10-year-anniversary-of-iconic-kids-voices), ~50 executions worldwide). Mechanism label: **one swapped channel.** Everything is realistic except exactly one swapped attribute (the voice). The discipline is the *only-one* rule — swap two things and it's noise.

**AS A PROMPT MOVE:** *List the channels of a scene (voice, physics, scale, texture, lighting, social norms, time). Swap EXACTLY ONE and keep all others documentary-real.*
Example: swap only physics-of-surfaces: an utterly naturalistic teen documentary except everything peels — one channel wrong, everything else Sundance-real.

### 2.10 Japanese CM surrealism — format pressure as generator

Japanese commercials' weirdness is partly structural: dominant 15-second slots force "impression over message" — one indelible image/gag, no time for setup-payoff, plus a cultural preference for soft-sell mood and absurdist humor ([Geinokai](https://geinokai.jp/blog/2024/11/25/why-japanese-commercials-are-so-quirky/), [ClickInsights](https://www.clickinsights.asia/post/the-wacky-world-of-japanese-commercials)). Nissin/Cup Noodle institutionalized weirdness as brand property ([Automaton](https://automaton-media.com/en/news/20230725-20270/)). Mechanism label: **compression forces surrealism** — at 15s the only options are cliché or dream-logic.

**AS A PROMPT MOVE:** *Impose a 15-second / one-scene / no-dialogue-setup constraint on a subset of generations: the impossible thing must be fully legible mid-happening, with no explanation before or after.*
Example: 15s — we open mid-event: the gummy is already half-peeled and the peel is already conducting the marching band; cut to pack shot.

---

## 3. How directors build treatments/styleframes for VFX-heavy spots

### 3.1 The treatment as a bounded-idea document

A director's treatment is a prose + visual pitch document produced after agency shortlisting; its job is to make the reader *see the finished film*, and to prove the director's take solves the client's specific problem within the money ([Assemble guide](https://www.onassemble.com/blog/how-to-write-a-winning-directors-treatment), [No Film School](https://nofilmschool.com/commercial-treatment), [Robin Piree](https://robinpiree.com/blog/how-to-write-a-directors-treatment-for-a-tv-commercial)). VFX-heavy treatments must show *where the money goes* — the ideation is explicitly bounded by executability, which is why strong treatments concentrate spectacle into **one repeatable mechanism** rather than many bespoke effects ([The Moon Unit](https://themoonunit.medium.com/how-to-write-outstanding-tv-commercial-treatments-f4ad7aa2ce20)).

### 3.2 Styleframes: the one-frame discipline

A styleframe is "a still image aiming to represent with accuracy the look and feel... as if it were a screenshot of the final video" ([Adrien de La Celle](https://medium.com/@adrien.delacelle/the-power-of-styleframes-d1b0ed1c8790), [Boords](https://boords.com/blog/what-are-style-frames-definition-and-examples), [Milanote guide](https://milanote.com/guide/motion-design-style-frames)). The practical consequence for ideation: **an idea that cannot be sold in one polished frame doesn't get bought.** This is Hegarty's poster test operationalized in the pipeline — the single frame must carry subject, transformation, tone, and product-relevance simultaneously.

### 3.3 One rule, escalated + worldbuilding-on-a-budget

Synthesis across the cases above and the heightening craft (§1.8): the VFX-spot discipline is —

- **One rule**: a single impossible mechanism, stated in a sentence (balls bounce down a hill; the world treats magic as normal; everything is peelable). One rule = one VFX methodology = one budget line = one legible poster.
- **Escalated**: the rule reapplied at growing scale/strangeness across 3–4 beats (Old Spice's bathroom→boat→horse), never a second rule.
- **Worldbuilding on a budget**: change one thing about the real world and shoot the rest documentary (Skittles' suburbia, Haribo's boardroom). The real world is free; the delta is the cost. Practical-effect texture is repeatedly chosen over CGI because slightly-wrong physicality reads as tone (Kuntz "fairly anti-CGI"; Skittles' puppets; Bravia all-in-camera).
- **Must read in one frame**: the transformation should be capturable mid-event in a single still that a stranger could caption correctly.

**AS A PROMPT MOVE:** *Output each idea in treatment-shape: (1) THE RULE in one sentence; (2) THE FRAME — describe the single styleframe that sells it, and what a stranger would caption it; (3) THE LADDER — 3 escalations of the same rule; (4) THE DELTA — what one thing is changed from documentary reality (= the budget).*
Example: RULE: gravity applies to the peel, not the fruit. FRAME: teen holds a spiraling peel that hangs down normally while the naked gummy floats above her open mouth; caption: "the candy that's already ascending." LADDER: gummy floats → all peeled fruit in the bodega floats → the peeled Earth. DELTA: one floating object per shot, everything else handheld real.

---

## 4. Candy/snack category grammar — and the cliché blacklist

### 4.1 The established surrealism grammar of candy ads

Candy is a zero-rational-benefit category — nobody needs it — so it went surreal earlier and harder than any other category; the sell is pure feeling/attention ([creative.salon: a century of surreal ads](https://creative.salon/articles/features/strange-fascination-a-century-of-surreal-ads), [True Treats: iconic 70s–80s candy ads](https://truetreatscandy.com/blogs/article/the-most-iconic-candy-ads-of-the-70s-and-80s), [Candies & Sweets: evolution of candy advertising](https://candiesandsweets.com/the-evolution-of-candy-advertising-2/)). The recurring grammar:

- **Attribute literalization**: one product property becomes a physical law (Skittles).
- **Consumption transformation**: eating changes who/what you are (Snickers).
- **Taste sequence as plot** (Sour Patch).
- **Innocence transposition**: candy re-childs adults (Haribo, Werther's).
- **Sensory hyperbole**: the flavor event rendered as weather/cosmos (Starburst, Fruit Gushers heads turning into fruit).
- The craft warning that governs all of it — Mother's Martin Rose: *"There is no surrealism for surrealism's sake"*; imagery must be rooted in brand detail or it's "visual randomness"/AI slop ([creative.salon](https://creative.salon/articles/features/strange-fascination-a-century-of-surreal-ads)).

### 4.2 The cliché blacklist (most-used candy-ad tropes)

For the engine: these are legal *raw materials* but banned as *final answers*. Each entry: trope → canonical user.

1. **Rainbow / color-explosion / slow-mo flavor burst** (macro juice splash, colors streaming) — Skittles' own default, every fruit candy since ([HistoryOasis on Skittles slogans](https://www.historyoasis.com/post/skittles-slogans-ads)).
2. **Bite transports you to a flavor world** ("Flavor Country," tropical waterfall, candy landscape) — the single most-used candy mechanic.
3. **Anthropomorphic candy afraid of being eaten** — M&M's spokescandies and descendants.
4. **You become someone else when you eat / until you eat** — Snickers; now category-generic transformation shorthand ([Media Shower Snickers case](https://www.mediashower.com/blog/snickers-hunger-campaign/)).
5. **Sour-face reaction shot** — every sour candy ad ever; Warheads to Toxic Waste.
6. **Adults act like kids / kid voices** — Haribo's ownership makes it radioactive for anyone else ([Haribo](https://www.haribo.com/en-us/news/haribo-celebrates-10-year-anniversary-of-iconic-kids-voices)).
7. **The sharing dilemma / possessive hoarding** — Twix left/right, "get your own," gollum-with-the-bag.
8. **Candy falls from the sky / grows on trees / rains indoors** — Skittles used it first and with tragedy; imitations keep only the rain.
9. **Midas touch — everything you touch becomes the candy** — Skittles "Touch" ([Selfstorming breakdown](https://www.selfstorming.com/tools/libraries/campaigns/skittles-touch-the-rainbow)).
10. **ASMR unwrap/peel macro with breathy sound design** — the modern gummy-category default; for a *peelable* product this is cliché #1 to fear.
11. **Craving possession** — can't think/work/talk until the candy is consumed; zombie-walk to the vending machine.
12. **"Random" Gen-Z weirdness with no cost and no rule** — weirdness as wallpaper; the documented failure mode ("imitation for imitation," AI-slop surrealism — [creative.salon](https://creative.salon/articles/features/strange-fascination-a-century-of-surreal-ads)).
13. **Mascot does extreme sports / is inexplicably cool** — 90s residue (Cheetos' Chester lineage).
14. **Forbidden/sensual indulgence** — slow-motion ecstasy eating (Cadbury Flake tradition; reads dated on a teen product).

**AS A PROMPT MOVE (blacklist usage):** *Generate 5 ideas freely, tag any that match blacklist entries, then for each tagged idea apply one of: (a) INVERT the trope (the flavor world visits YOU and is disappointed), (b) keep the trope but add the Skittles cost/tragedy beat, (c) swap which channel carries it (§2.9). Never ship a blacklist item straight.*
Example: trope #2 straight = "peel it and you're in gummy paradise" — inverted: the teen peels the gummy and a tiny confused tourist from the flavor world climbs OUT, photographs the cafeteria, and calls it paradise.

---

## 5. Engine-ready synthesis: the operator set

The whole corpus reduces to a small set of orthogonal generative operators. Divergence = varying the operator choice, not just the surface content:

| # | Operator | Source |
|---|----------|--------|
| 1 | Two-pile forced collision (specific product facts × unrelated audience knowledge) | Webb Young §1.1; Guinness §2.5 |
| 2 | Truest/awkwardest thing first; the flaw is generative | Sullivan §1.2 |
| 3 | Upstream re-statement of what the ad must accomplish | Trott §1.3 |
| 4 | Words-first: a ≤12-word stunning line, image derived from it | Lois §1.4 |
| 5 | Category zig-list → structural inversion; poster/one-frame test | Hegarty §1.5, styleframes §3.2 |
| 6 | Attribute → extreme conclusion (push past pleasant into a new register) | §1.6, Skittles §2.3 |
| 7 | Event-size vs reaction-size mismatch dial (both directions) | §1.7 |
| 8 | ONE rule + 4-beat ladder + separate reaction track | §1.8, Old Spice §2.4 |
| 9 | Platform extraction test ("the ad behind the ad": 3 more executions or it's not an idea) | §1.9 |
| 10 | Feeling-transfer: be the feeling, product absent till endframe | Gorilla §2.1 |
| 11 | Claim → child-logic proof-event at absurd scale, shot real | Bravia §2.2 |
| 12 | Deadpan world + someone quietly pays a price (tragedy beat) | Skittles §2.3 |
| 13 | Flip the fence: the forbidden/embarrassing constraint IS the idea | Guinness §2.5 |
| 14 | Technique-first: invent the impossible camera trick, then its story | Gondry §2.6 |
| 15 | Consumption timeline → plot structure | Sour Patch §2.8 |
| 16 | Swap exactly one channel, keep the rest documentary | Haribo §2.9 |
| 17 | 15-second compression: legible mid-event, no setup | Japanese CM §2.10 |
| 18 | Cliché blacklist: tag → invert / add cost / re-channel | §4.2 |
| 19 | Treatment-shape output: RULE / FRAME / LADDER / DELTA | §3.3 |
| 20 | Dead-idea inventory: harvest endings and images from rejected generations | Old Spice §2.4, Guinness §2.5 |

Two meta-findings for the engine's architecture:

1. **The famous ideas were findable because the *search space* was reframed first** (Gorilla's brief, Guinness's forbidden pour time, Old Spice's buyer/user paradox) — the engine should spend explicit turns mutating the problem statement before generating answers.
2. **Every durable surreal spot has a governing rule + a cost + an underreaction.** Random impossibility is the documented failure mode ("no surrealism for surrealism's sake"). The engine's novelty should come from *which* rule and *which* collision — the discipline (one rule, escalated, deadpan, priced) stays constant.
