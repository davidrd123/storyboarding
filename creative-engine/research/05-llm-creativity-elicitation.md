# 05 — Eliciting Creativity from LLMs: Research & Practitioner Knowledge

**Purpose:** the meta-layer for the creative-engine skill — what the literature says about why LLM ideation collapses to the predictable, which interventions demonstrably widen it, and how to measure whether the engine works.

**Evidence key:** [PR] peer-reviewed · [PP] preprint · [AN] anecdote/practitioner lore

---

## 1. The homogenization problem — what exactly collapses

### 1.1 LLM-assisted ideation homogenizes *across users* [PR]

- **Anderson, Shah & Kreminski, "Homogenization Effects of LLMs on Human Creative Ideation" (C&C 2024)** — 36-participant comparative study. Users of ChatGPT-as-creativity-support-tool produced **less semantically distinct ideas across different users** than users of a non-LLM tool. Individually they generated *more and more detailed* ideas — and felt less ownership of them. The collapse is invisible at the individual level; it only shows up when you compare users to each other. https://arxiv.org/abs/2402.01536
- **Doshi & Hauser, "Generative AI enhances individual creativity but reduces the collective diversity of novel content" (Science Advances, 2024)** — ~300 writers, short stories with/without GPT-4 idea access. AI access made individual stories rated more creative/better written (biggest gains for the least creative writers), but **AI-enabled stories were significantly more similar to each other** than human-only stories. Framed as a social dilemma: individually better off, collectively narrower. https://www.science.org/doi/10.1126/sciadv.adn5290 · https://arxiv.org/abs/2312.00506
- **"ChatGPT decreases idea diversity in brainstorming" (Nature Human Behaviour, 2025)** — same direction in group brainstorming. https://www.nature.com/articles/s41562-025-02173-x

**What collapses:** *between-sample / between-user semantic diversity* — the spread of the idea pool — not per-idea fluency, detail, or rated quality. This is exactly the failure mode a single-shot "give me ideas" skill invocation reproduces.

### 1.2 Alignment (RLHF/DPO) is a primary cause: mode collapse & typicality bias [PP, strong]

- **Kirk et al., "Understanding the Effects of RLHF on LLM Generalisation and Diversity" (2023)** — RLHF models show markedly lower across-input output diversity than SFT models; classic mode collapse toward a stylistic "mode." https://arxiv.org/abs/2310.06452
- **Zhang et al., "Verbalized Sampling" (2025)** — locates the cause in **typicality bias in preference data**: human annotators systematically prefer familiar/fluent/predictable text, which sharpens the aligned model's distribution (formalized as sharpening factor γ = 1 + α/β). Measured diversity: base model 45.4% → SFT 20.8% → DPO 10.8%. Direct prompting of an aligned model retains only **~24% of base-model diversity**. https://arxiv.org/html/2510.01171v2
- **Lu et al., "AI as Humanity's Salieri" (ICLR 2025) — the Creativity Index** — measures how much of a text can be reconstructed from existing web snippets (DJ Search). Professional human writers score on average **66.2% higher** than LLMs; **RLHF cuts the Creativity Index by a further ~30.1%**, mostly at the verbatim level — aligned models converge on a preferred linguistic style. https://arxiv.org/abs/2410.04265
- **Gwern, "Generative AI mode collapse" [AN, well-documented]** — practical symptoms: ChatGPTese, refusal to write non-rhyming poetry, inability to be random, and **flattened logits that make temperature nearly inert** — the distribution is already collapsed, so cranking temperature can't recover the lost modes. https://gwern.net/doc/reinforcement-learning/preference-learning/mode-collapse/abstract

### 1.3 The duplication / exhaustion problem when you sample at scale [PR/PP]

- **Si, Yang & Hashimoto, "Can LLMs Generate Novel Research Ideas?" (2024)** — LLM-generated research ideas were rated *more novel* than human experts' — but when they over-generated seed ideas, **only ~5% survived embedding-based deduplication (cosine 0.8 threshold)**. The model keeps re-emitting near-duplicates. https://arxiv.org/abs/2409.04109
- **Meincke, Mollick & Terwiesch, "Prompting Diverse Ideas" (2024)** — GPT-4 idea pools exhaust: diversity-boosting prompts hold an advantage **until ~750 ideas**, after which strategies converge as the reachable idea space depletes (~4,700 unique ideas for the best prompt vs ~3,700 baseline in their domain). https://arxiv.org/abs/2402.01727

**Summary of what collapses:** (a) cross-sample semantic diversity, (b) the novelty *tail* (rare/atypical completions get pruned by alignment), (c) verbatim linguistic originality, (d) the effective size of the reachable idea space (heavy duplication). Per-idea *quality* generally does not collapse — which is why the problem goes unnoticed.

**AS A SKILL DESIGN RULE:** The engine's enemy is not bad ideas but *the same good idea over and over*. Every architectural choice must be judged on pool-level diversity metrics, never on how good any single idea looks. Never single-shot; always treat one invocation = one *distribution*, not one answer.

---

## 2. Interventions, ranked by evidence

### 2.1 Temperature / sampling parameters — WEAK LEVER [PR/PP]

- **Peeperkorn et al., "Is Temperature the Creativity Parameter of LLMs?" (ICCC 2024)** — narrative generation across temperatures: temperature is **weakly correlated with novelty**, moderately correlated with *incoherence*, no relation to cohesion/typicality. "Far more nuanced and weak than the 'creativity parameter' claim." https://arxiv.org/abs/2405.00492
- **"Measuring LLM Novelty as the Frontier of Original and High-Quality Output" (2025)** — U-shaped: novelty rises with temperature (more rare, less memorized n-grams) then falls as quality craters. https://arxiv.org/pdf/2504.09389
- Gwern [AN]: on heavily aligned models temperature barely matters because logits are already flattened/collapsed.

**AS A SKILL DESIGN RULE:** Do not build the engine around sampling parameters. Treat temperature as a minor tuning knob (mild raise for divergent phases if the API exposes it), never the mechanism. Prompt-level structure beats decoding-level noise.

### 2.2 Distribution-level prompting / Verbalized Sampling — STRONG [PP, extensive experiments]

Ask the model to **verbalize a probability distribution**: "Generate 5 responses to X, each with its estimated probability" — optionally "only include responses whose probability is below 0.10" to force the tail. Instance-level prompts collapse to the mode; distribution-level prompts approximately recover the base model's distribution. Results: **1.6–2.1× diversity over direct prompting** in poems/stories/jokes, ~67% of base-model diversity recovered (vs 24% direct), quality maintained (VS-CoT pushes the Pareto front), works on closed models without logit access, and **larger models gain 1.5–2× more** than small ones. https://arxiv.org/html/2510.01171v2

**AS A SKILL DESIGN RULE:** The engine's core sampling primitive should be "emit k candidates *with verbalized probabilities*, then deliberately harvest the low-probability tail" — not "give me an idea" k times. Tune the probability threshold as the divergence dial instead of temperature.

### 2.3 Persona / role diversity — WORKS, BUT ONLY THE RIGHT KIND [PP + PR, convergent]

- **"Examining and Addressing Barriers to Diversity in LLM-Generated Ideas" (2026)** — two barriers identified: *fixation* (LLMs fixate within a session about as much as humans) and, more fundamentally, **missing knowledge partitioning** — an LLM is one aggregated distribution, whereas a human population occupies distinct knowledge regions. **Ordinary, randomly-varied personas** ("retired politician," "ink chemist") act as sampling cues that anchor generation in distinct semantic regions and *closed the human–LLM diversity gap* (210 unique combos vs humans' 206); famous "creative entrepreneur" personas (Steve Jobs types) did much worse (164) because they share the same "creative" cues. **Persona + CoT-revise-for-distinctiveness beat human groups by 26%.** https://arxiv.org/pdf/2602.20408
- **Meincke et al.** found a plain "Steve Jobs" persona mediocre (cosine sim 0.368 vs CoT's 0.255) — consistent: celebrity-creative personas are themselves a mode. https://arxiv.org/abs/2402.01727
- **Cambridge Design Science (2024/25)**: multi-professional personas applied **sequentially** beat parallel/collective persona prompting for design-concept diversity. https://www.cambridge.org/core/journals/design-science/article/enhancing-design-concept-diversity-multipersona-prompting-strategies-for-large-language-models/3B346E253508337A4EE899499BE49D9B
- Caveat [PP]: fine-grained persona synthetic data is still less lexically diverse than human text (https://arxiv.org/pdf/2505.17390) — personas narrow the gap, don't abolish it.

**AS A SKILL DESIGN RULE:** Simulate a *population*, not a genius. Randomly sample mundane, concrete, varied personas (occupation × background × obsession) from an external list as partitioning cues — never "be a visionary creative." Apply them sequentially, one region of idea-space at a time.

### 2.4 Chain-of-thought — TWO-SIDED; scaffold yes, reasoning-mode maybe no

- **For idea-pool diversity, structured CoT is the single best-tested prompt.** Meincke et al. tested 35 strategies; CoT won (cosine 0.255, nearly matching human groups' 0.243; ~4,700 unique ideas). The Barriers paper's CoT ("generate, then explicitly revise each idea to be more distinct from the others") reduced fixation in LLMs (not in humans). [PP, replicated across 2 groups]
- **But reasoning-trained deliberation may pull *against* divergence:** reasoning-distilled models align with *low*-creativity human neural geometry (https://arxiv.org/html/2604.03480 [PP]); surveyed reasoning strategies fail to improve divergent creativity (https://arxiv.org/pdf/2511.07448 [PP]); direct creative prompting causes **premature convergence** — the model tries to satisfy all constraints immediately — motivating **CreativeDC**, which explicitly decouples a free-exploration phase from a constraint-satisfaction phase (https://arxiv.org/html/2512.23601 [PP]).

**AS A SKILL DESIGN RULE:** Use CoT as a *diversification scaffold* (plan the axes of variation → generate → audit pairwise similarity → revise for distinctiveness), and keep constraint-checking OUT of the divergent phase. Two-phase always: explore unconstrained first, converge/repair second.

### 2.5 Forced dissimilarity / denial prompting — GOOD EVIDENCE [PR]

- **Lu et al., "Benchmarking Language Model Creativity: A Case Study on Code Generation" (NAACL 2025)** — **Denial Prompting**: after each solution, *deny* the techniques it used ("solve it again without X, Y"), forcing progressively rarer strategies; measured by NeoGauge (correct + constraint-adherent + novel vs human solution corpus). Systematically denying routine solutions accesses novel regions of the generative space. https://arxiv.org/abs/2407.09007
- Serial-forcing corollary [PP]: incrementally prompting the model "more forcefully" for original responses across turns raises novelty (see §3.1 serial-order work; also IDEAFix on defixation prompting, https://arxiv.org/pdf/2606.00875).

**AS A SKILL DESIGN RULE:** Make dissimilarity an *explicit, named constraint*: each new idea must differ from ALL previous ideas along a stated axis, and the engine should extract "the move idea N made" and add it to a growing ban-list ("no more ideas that rely on: miniaturization, role-reversal, …"). Denial is cheap and composable with everything else.

### 2.6 Random-stimulus injection / external entropy — GOOD EVIDENCE, KNOWN FAILURE MODE [PP + AN]

- **"Addressing LLM Diversity by Infusing Random Concepts" (2026)** — prepending random unrelated concepts/words to the prompt significantly increases unique-response counts and response entropy across Claude/Gemma/Mistral. Failure modes: coherence loss, off-topic drift — recommend a coherence filter after generation. https://arxiv.org/pdf/2601.18053
- Long-standing human technique (random word / Oblique Strategies) transfers [AN]; Karen Boyd's practitioner review recommends seeding with contrasting examples and cross-domain material. https://drkarenboyd.com/blog/llm-augmented-brainstorming-how-to-make-it-work
- Critically, the entropy must be **external**: LLMs cannot self-randomize (Gwern; the model asked for "a random word" is itself mode-collapsed).

**AS A SKILL DESIGN RULE:** The skill must carry its own entropy source — wordlists, corpus snippets, `random.choice` in a script, dice — sampled *outside* the model and injected per-idea as forced-connection material. Never ask the model to pick its own random stimulus. Pair with a downstream relevance/coherence gate.

### 2.7 Multi-agent discussion / diverse-agent ideation — MODERATE [PR]

- **Lu et al., "LLM Discussion" (COLM 2024)** — three-phase discussion framework (diverge → exchange → converge) with **distinct role assignments** to combat homogeneity; beats single-LLM and prior multi-agent baselines on Alternative Uses, Similarities, Instances, and Scientific Creativity tests (LLM-judge + human eval). https://arxiv.org/abs/2405.06373
- Multi-agent brainstorming with dynamic role-play also augments *human* group creativity (ACM Collective Intelligence 2025). https://dl.acm.org/doi/10.1145/3715928.3737479

**AS A SKILL DESIGN RULE:** Worth having as an expensive mode: N parallel subagent "voices" with genuinely different role cards (and ideally different context/material each), a structured exchange round, then convergence. Roles must be differentiated by *knowledge and incentive*, not just name — otherwise it's one distribution cosplaying as N.

### 2.8 Evolutionary / quality-diversity (QD) search — STRONG CONCEPT, COMPUTE-HEAVY [PR]

- **Bradley et al., "Quality-Diversity through AI Feedback" (QDAIF, ICLR 2024)** — MAP-Elites where the LLM is both mutation operator and judge of quality *and* of position along explicit diversity dimensions (e.g. genre, sentiment, ending type). Maintains an archive of elites per diversity cell; mutates from random cells. Beat baselines on opinion pieces, stories, poetry; AI feedback tracked human judgment. https://arxiv.org/abs/2310.13032 · https://qdaif.github.io/
- Related: **Nova** (iterative planning+search raises novelty/diversity of research ideas, https://arxiv.org/pdf/2410.14255 [PP]); prompt-embedding evolution for QD generation (https://arxiv.org/html/2605.09781 [PP]).

**AS A SKILL DESIGN RULE:** The engine's memory should be a **MAP-Elites-style archive**: user- or engine-declared diversity axes define a grid; every generated idea is binned; new generation mutates from *sparsely populated or random* cells, not from the best idea. "Best idea so far" as the seed is precisely how you re-collapse.

### 2.9 Generate-N-then-pick vs. iterative — BOTH, IN ORDER [PP + PR]

- Over-generate + dedup + rerank works (Si et al.: novel ideas exist but you must strip ~95% duplicates); expect saturation (~750 ideas in Meincke's domain).
- The **serial-order effect replicates in LLMs**: later responses in a list tend to be more novel than earlier ones, mirroring humans (see https://arxiv.org/pdf/2602.02048 and the human literature it builds on, e.g. https://www.researchgate.net/publication/249334803). So the tail of a long list is where the interesting material is — but human work also shows a fluency/elaboration trade-off late in lists (ideas get thinner). [PP for LLMs; PR for humans]
- Verbalized Sampling recommendation: k=5 per call × many calls (N≈30) beats one call for 30. [PP]

**AS A SKILL DESIGN RULE:** Quota high but batch small: many calls of ~5 (fresh or varied context each) rather than one call of 40; keep everything, dedup by embedding threshold (~0.8 cosine), and treat items 1–3 of any list as the "obviousness tax" — auto-flag them as probable modes, and mine the tail. Stop adding samples when the marginal-uniqueness curve flattens.

---

## 3. Practitioner lore — what holds up

1. **"Ask for 40 ideas, not 5."** Holds up, with a twist. More samples → better best-idea (variance is your friend: Girotra/Terwiesch "Ideas are Dimes a Dozen," https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2023/08/LLM-Ideas-Working-Paper.pdf [PP]), and the serial-order effect means later ideas are more novel. But duplication grows fast and the idea space exhausts; the fix is dedup + denial/dissimilarity constraints + context resets, not ever-bigger single lists. Mollick documents the "irreducible weirdness" of what actually moves outputs [AN]: https://www.oneusefulthing.org/p/captains-log-the-irreducible-weirdness
2. **Two-stage divergent-then-convergent.** Holds up across sources: CreativeDC (decouple exploration from constraint satisfaction), LLM Discussion's phased framework, Boyd's "prevent premature convergence — tell it not to evaluate yet." Convergence pressure during divergence is the canonical failure.
3. **LLM as recombiner of externally supplied material, not generator-from-nothing.** Holds up: random-concept infusion [PP], seeding with your own/contrasting examples [AN], and the knowledge-partitioning theory (§2.3) all say the model is a superb *combiner* whose defaults are modal — feed it non-modal inputs.
4. **Fresh chats / context resets to break fixation.** Plausible and theory-consistent (LLMs fixate within a session like humans do — Barriers paper), practitioner-endorsed [AN]. Cheap to implement via stateless subagent calls.
5. **"Avoid the obvious answer" / negative instructions alone.** Weakest of the lore — mild effect at best; works far better when operationalized as *concrete* denial ("do not use techniques X, Y, Z which appeared in ideas 1–4") than as a vibe ("be original"). Consistent with Denial Prompting's design.

---

## 4. Measurement — how we'd know the engine works

**Pool-level diversity (primary):**
- Mean pairwise cosine distance of idea embeddings (Meincke's headline metric; human-group benchmark ≈ 0.243 similarity in their domain).
- Unique-idea count after dedup at cosine ~0.8 (Si et al.), and the *exhaustion curve* — unique ideas vs. total sampled. The engine wins if its curve dominates direct prompting's.

**Novelty / originality (secondary):**
- **DAT / DSI** — semantic-divergence measures validated on 100k humans; LLMs already beat average humans on DAT but lose to creative humans on DSI in writing (Bellemare-Pepin et al., Scientific Reports 2026, https://www.nature.com/articles/s41598-025-25157-3 [PR]).
- **Ocsai** (Organisciak, Acar, Dumas, Berthiaume 2023) — fine-tuned-LLM scoring of divergent-thinking responses, r ≈ .78–.81 with human judges vs r ≈ .12–.26 for raw semantic distance. Raw embedding distance is a *diversity* metric, not an *originality* judge. https://openscoring.du.edu/ [PR]
- **Creativity Index / DJ Search** for linguistic novelty against existing text (Lu et al.). [PR]

**Cautions:** LLM-as-judge inherits the same typicality bias that caused the collapse — calibrate judges comparatively, in batches, against human spot checks (mirrors our own Gemini-as-eyes finding: comparative batches, never isolated absolute scores). Torrance-style fluency/flexibility/originality/elaboration maps cleanly: fluency = unique count, flexibility = category count (the Barriers paper's "27 categories" metric), originality = Ocsai/statistical rarity, elaboration = detail — score all four; the engine should raise flexibility/originality *without* just inflating fluency.

**AS A SKILL DESIGN RULE:** Ship the metric with the engine. The skill should optionally emit its own scorecard per run (pairwise embedding diversity, category count, dedup survival rate) so regressions in divergence are visible — because §1 shows they are invisible to eyeballing single outputs.

---

## 5. Synthesis — architecture of the creative engine

The convergent picture across ~20 sources:

> An aligned LLM is a sharpened distribution. Nothing you do at the decoding layer un-sharpens it much (temperature ≈ weak). What works is **prompt-level structure that changes which distribution you're sampling from**: ask for distributions not instances (VS), partition the knowledge space (ordinary personas, external random stimuli), forbid re-use of prior modes (denial/dissimilarity ban-lists), keep divergence and convergence in separate phases, and manage the pool with an explicit diversity archive (QD) plus embedding dedup — measuring pool diversity the whole way.

**The five load-bearing design rules:**
1. **Never single-shot; sample distributions.** Every ideation call = k candidates with verbalized probabilities; harvest the low-probability tail. (VS, §2.2)
2. **External entropy is mandatory.** Random concepts/personas/material sampled outside the model, injected per idea; the model must never be its own randomness source. (§2.3, §2.6)
3. **Grow a ban-list.** Extract each accepted idea's core move; subsequent generations must verifiably avoid all prior moves ("differ from all previous along axis X"). (Denial Prompting, §2.5)
4. **Two phases, hard wall.** Divergent phase: no constraint-checking, no evaluation, CoT used only to plan variation axes and audit distinctness. Convergent phase: repair, select, satisfy the brief. (§2.4, §3.2)
5. **Archive, don't hill-climb.** Bin ideas on declared diversity axes MAP-Elites-style; seed new generations from empty/sparse cells, never from the current best. Dedup at ~0.8 cosine; watch the exhaustion curve and stop or switch strategy when marginal uniqueness flattens. (§2.8, §2.9)
