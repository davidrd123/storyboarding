# Deep Research Queries — Storyboard System

Derived from `STORYBOARD_SYSTEM_BRIEF.md` and the underlying chat. Goal: verify load-bearing claims, fill in known unknowns, and surface prior art before committing architecture.

Most queries here target claims in the brief that are sourced to "the prompting guides" or "the search" without named citations — those are the verification points. The genuinely open empirical questions (compositional skeleton transfer, vision-model continuity checking, bible-scale economics) are flagged.

---

## A. Model capability verification (cite-or-die)

1. **GPT Image 2 (gpt-image-1 / "Thinking" / April 2026 launch) — current published spec.**
   Confirm: max reference images per call (brief says 16), max resolution (brief says 2K), supported aspect ratios, latency at high quality, edit endpoint with masks, identity-preservation claims in OpenAI's own docs vs third-party benchmarks, current per-image pricing tiers. Pull the OpenAI cookbook + fal.ai's GPT Image 2 guide verbatim.

2. **Nano Banana Pro (Gemini 3 Pro Image) — controllability features.**
   Confirm: 14-ref cap and ~6 sweet spot, Google's *exact* recommendation language about composite character sheets ("complete 3D understanding"), supported reference roles, max output resolution, character-consistency claims and limits, and whether there's a documented storyboard workflow guide. Also: is there a separate "Nano Banana 2" / Gemini 3.1 Flash Image with different specs?

3. **Midjourney V7 — Omni Reference vs --cref vs --sref.**
   What does each actually do as of May 2026? Stylize/weight knobs, character reference fidelity benchmarks, moodboard feature, draft mode, and the *current* status of the API situation (brief says no public API — verify, check for partner/sanctioned access). Disney/Universal/WB lawsuit status and any settlements or rulings since the brief was written.

4. **Image Arena Elo current rankings.**
   Verify the GPT Image 2 ~1512 vs MJ V7 ~1270 numbers, get the full leaderboard, and note who else is climbing (Flux, Recraft, Ideogram, Reve, anything newer). This is the empirical claim that opens the closed-model-only path — worth double-checking.

---

## B. Controllability techniques — the real production patterns

5. **The "Preserve / Borrow / Do NOT borrow" grammar — actual examples in the wild.**
   Pull 10+ documented prompts that use this structure from professional users (not OpenAI marketing). Look for: how aggressive the do-not-borrow has to be, what leakage looks like when it fails, whether ordering of constraints matters, and whether the syntax is the same for GPT Image 2 vs Nano Banana Pro vs others.

6. **Compositional skeleton / camera-angle transfer across different subjects.** *(Brief's biggest open question.)*
   Search: "low angle reference" workflows, ControlNet-depth-as-camera-angle, pose-transfer products applied to camera framing (Viggle? Animate Anyone? Runway Act-One?), and any documented "borrow framing but not subject" examples. If anyone has solved this even partially, it's worth knowing exactly how.

7. **Role-labeled multi-reference prompts at scale.**
   What's the documented ceiling on how many roles a model can keep distinct in one prompt? "Image 1 is character, Image 2 is style, Image 3 is location, Image 4 is composition" — does this degrade gracefully or fall off a cliff? Production users on r/StableDiffusion, fal.ai blogs, Replicate examples.

8. **Negative-constraint phrasings that actually work.**
   "Do not borrow X" vs "ignore X from Image N" vs "preserve only [list]." Empirical comparisons if they exist.

---

## C. Character consistency — the load-bearing case

9. **Multi-angle character sheet → consistent panel generation: documented workflows.**
   Specifically the pattern Google recommends. Find 3–5 working examples (not marketing) showing the same character across 6+ panels with varied poses/expressions, and what the failure rate looks like.

10. **Specialized character-consistency tools beyond base models.**
    Krea's character feature, Higgsfield, Pika character, fal's character workflows, OpenArt Character Consistency, scenario.gg. What's the state of the art for "lock this face across N images" outside MJ Omni Reference?

11. **Expression sheet generation — the diagnostic.**
    Has anyone published a "I generated 16 expressions for one character in style X using model Y" walkthrough with results? This is the brief's identified diagnostic for whether the whole pipeline works — find prior art.

---

## D. Storyboard tools that already exist (competitive landscape)

12. **Existing AI storyboard products as of May 2026.**
    Storyboarder, Boords (and any AI features added), Krea storyboard, LTX Studio, Showrunner, Sora storyboard mode, Runway storyboard, Invideo, plus any new entrants. What does each automate, what's the controllability gap, and which one's closest to what the brief describes?

13. **Director-facing AI tools used in real pre-production.**
    Not consumer tools — what are working commercial directors and DPs actually using in 2026? Look for trade press (Variety, IndieWire, NoFilmSchool), case studies, and DGA/ASC commentary.

14. **Pitch-book examples and conventions.**
    What does a studio pitch storyboard actually look like? Format, panel count, level of finish, ratio of panels to script pages. This sets the *target spec* the system has to hit.

---

## E. Production economics

15. **Per-image cost and latency at scale.**
    Real numbers for GPT Image 2 high-quality + multi-ref calls, Nano Banana Pro equivalent, and MJ V7. What does it cost to generate ~25 bible assets × 4 principals + ~60 panels × 3 candidates with realistic re-roll rates? Throughput limits per API key.

16. **Re-roll rates from production users.**
    Brief assumes 20–30% — is that documented anywhere for reference-heavy workflows? Look for blog posts from teams who've shipped real volume.

---

## F. Track B (LoRA) — viability and timeline

17. **Character LoRA training in 2026: minimum viable dataset.**
    Flux LoRA, SDXL LoRA, any newer open base models. How many captioned images for a workable character LoRA? How many for a *style* LoRA? Has the "50 image LoRA" prior moved with newer base models?

18. **The "closed-model output → LoRA training" pipeline.**
    Has anyone published this exact workflow — use closed model to generate 200+ panels, then train LoRA on those? IP/licensing implications of training on GPT Image 2 outputs specifically (OpenAI's terms).

19. **Best open-source base model for an illustrated/comics style as of mid-2026.**
    Flux Dev, Flux Pro, SDXL Lightning, any newer release. Which one most rewards a small style LoRA without losing prompt adherence?

---

## G. The continuity checker (Phase 5)

20. **Vision-model continuity checking in production.**
    Has anyone built "compare panel image to state-ledger description and flag mismatches"? GPT-4V / Claude Vision / Gemini for this task — accuracy on costume/prop/wound continuity. False-positive rates that would make it useful vs noisy.

21. **Multi-image consistency evaluation models.**
    Tools or papers that score "is this the same character across N images" with quantitative output.

---

## H. Adjacent — beat-to-DSL and lookbook capture

22. **Script breakdown LLM tools used in production.**
    Largo.ai, Filmustage, ScriptHop, Saturation, anything specifically for breaking script → beats → coverage. What do they get right, where do they fail, and is any of them a real component to integrate rather than rebuild?

23. **Director lookbook → AI input — current standard practice.**
    How are directors who *do* use AI assembling lookbooks today? File formats, organization conventions, any tooling that's emerged for the role-labeled-folder pattern the brief describes.

24. **Animatic / motion as the downstream of storyboard.**
    Sora 2, Veo 3, Kling 2, Runway Gen-4 — can any of them take a finished storyboard panel as a keyframe and animate the beat? This is the *next* product question after pitch books work, but worth scoping now.

---

## Suggested prioritization

**Before Tuesday meeting with Ben (highest leverage):**
- #1–4 (verify model specs underpinning the whole pipeline)
- #5–6 (the grammar and the open compositional-transfer question)
- #9 (does the bible workflow actually hold?)
- #12 (what already exists that we should compare against)
- #15 (per-character/per-pitch economics)

**Post-meeting deep dive:**
- #7–8, #10–11 (refinement on controllability technique)
- #13–14 (industry context)
- #16–19 (Track B planning)
- #20–21 (continuity checker feasibility)
- #22–24 (adjacent components and downstream)
