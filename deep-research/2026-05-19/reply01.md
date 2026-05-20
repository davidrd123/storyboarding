# Storyboard research memo — priority pass

I treated the vault brief and research questions as hypotheses to verify, not as authoritative facts. The priority items I covered first are #1–4, #5–6, #9, #12, and #15 from the research list. 

## Top-line corrections

The overall architecture still looks plausible: **director-led DSL + character/world bibles + role-labeled references + prompt assembly + candidate history + continuity checking** is a good direction. But several claims in the brief need tightening:

1. **“GPT Image 2 / gpt-image-1” should be corrected to current model naming.** OpenAI’s current image docs identify `gpt-image-2` as the latest GPT Image model; `gpt-image-1`, `gpt-image-1.5`, and `gpt-image-1-mini` are separate older/lower models. `gpt-image-2` supports generation and editing workflows, and GPT image-model edits can accept **up to 16 images**. ([OpenAI Developers][1])

2. **The “max 2K” claim is too conservative.** OpenAI’s docs list popular `gpt-image-2` sizes including 2048×2048, 2048×1152, and 3840×2160, with constraints around max edge length, pixel count, and aspect ratio; OpenAI labels 2K+ as experimental and says 2560×1440 is the recommended upper reliability boundary. ([OpenAI Developers][1])

3. **The Nano Banana Pro “14 refs” claim is official, but the “~6 sweet spot / complete 3D understanding” language is not official Google language in the sources I found.** Google documents Gemini 3 Pro Image / Nano Banana Pro as supporting up to 14 reference images, with specific role caps for object and character references. The “6-image sweet spot” and “complete 3D understanding” phrasing came from a third-party prompt guide, not Google’s docs. ([Google AI for Developers][2])

4. **Image Arena still supports the closed-model path, but the quoted Elo numbers are stale.** Arena.ai’s May 12, 2026 leaderboard has `gpt-image-2 (medium)` ranked #1 in text-to-image at 1393±7, followed by Gemini/Nano Banana image models; the image-edit leaderboard also has `gpt-image-2` #1 at 1467±5. The brief’s “~1512 vs ~1270” looks like an earlier snapshot, not the current leaderboard. ([arena.ai][3])

5. **The “preserve / borrow / do-not-borrow” grammar is directionally grounded, but it is a house grammar, not a magic official syntax.** OpenAI and fal.ai both strongly support the underlying pattern: label each input image by role, separate what changes from what must be preserved, and repeat preserve constraints explicitly. ([OpenAI Developers][4])

6. **Camera-angle transfer remains the biggest empirical unknown.** There is support for preserving framing, layout, perspective, and camera angle in edits or sketch-to-render workflows, but I found no solid public evidence for “borrow only the camera angle from Image 3 into a fresh scene with a different subject” as a reliable production pattern. A 2025 camera-control paper explicitly says precise camera control is still missing in current text-to-image models, which reinforces that this should be tested rather than assumed. ([Fal.ai][5])

---

## 1. GPT Image 2 / OpenAI image model verification

**Finding:** OpenAI’s current production image model is `gpt-image-2`. It supports image generation and image editing. The edits endpoint supports one or more source images, optional masks, and up to 16 input images for GPT Image models. OpenAI also notes that organization verification may be required for GPT image models. ([OpenAI Developers][1])

**Capabilities relevant to storyboards:**

| Claim                            | Current finding                                                                                                                                               | Evidence quality | Implication                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------: | -------------------------------------------------------------------------------------------------------- |
| 16 reference images              | Verified for GPT image-model edit inputs                                                                                                                      |             High | The proposed per-panel ref budget of character + expression + location + style is comfortably under cap. |
| 2K output                        | Partly wrong; 2K is supported, but docs also list 4K-like sizes under constraints; 2K+ is experimental                                                        |             High | Use 1536×1024 or 2048×1152 for reliable pitch boards; reserve 4K for selected final panels.              |
| High-fidelity input preservation | `gpt-image-2` automatically processes image inputs at high fidelity; input fidelity is not user-settable on `gpt-image-2`                                     |             High | Good for reference-heavy workflows; fewer knobs, but less control over fidelity/cost tradeoff.           |
| Latency                          | OpenAI warns complex prompts can take up to 2 minutes                                                                                                         |             High | Candidate generation should be batched/asynchronous in the UI; don’t design around instant output.       |
| Character consistency            | OpenAI claims robust identity preservation for edits/character-consistency workflows, but also warns recurring character/brand consistency can still struggle |             High | Bible workflow is justified, but a continuity checker and re-roll loop are not optional.                 |

OpenAI’s official prompting guide is very aligned with the storyboard architecture. It recommends structured prompts, constraints/invariants, and explicitly referencing multi-image inputs by index and role. For style transfer, OpenAI advises stating what should stay and what should change, with hard constraints to prevent drift. ([OpenAI Developers][4])

**Cost:** For `gpt-image-2`, OpenAI lists example output prices such as 1024×1536 / 1536×1024 at **$0.041 medium** and **$0.165 high**, and 1024×1024 at **$0.053 medium** and **$0.211 high**. ([OpenAI Developers][1])

**Correction to brief:** Replace “GPT Image 2 / gpt-image-1” with a model matrix:

* `gpt-image-2`: production candidate for highest controllability.
* `gpt-image-1.5`: possible lower-cost / fallback test model.
* `gpt-image-1-mini`: likely not the right quality bar for pitch books.

---

## 2. Nano Banana Pro / Gemini image verification

**Finding:** Google’s docs identify two current Gemini image models: **Gemini 3.1 Flash Image / Nano Banana 2** and **Gemini 3 Pro Image / Nano Banana Pro**. Google positions Flash for speed/high-volume workflows and Pro for professional asset production. Both support high-resolution outputs up to 4K, thinking-mode behavior, and up to 14 reference images. ([Google AI for Developers][2])

**Reference limits are more nuanced than just “14 images.”** Google’s docs say Gemini 3.1 Flash Image supports up to **10 high-fidelity object images** and **4 character images**, while Gemini 3 Pro Image supports up to **6 high-fidelity object images** and **5 character images**. That is highly relevant to multi-character scenes. ([Google AI for Developers][2])

**Storyboard relevance:** Google’s Nano Banana Pro announcement includes an official storyboard example prompt asking for a black-and-white storyboard sketch with establishing, medium, close-up, and POV panels. That supports “storyboard as a native use case,” but it does not prove long-sequence character consistency. ([blog.google][6])

**Cost:** Google lists Gemini 3 Pro Image Preview at **$0.134 per 1K/2K output image** and **$0.24 per 4K output image**, with Batch/Flex rates at half price. Image input is listed as **$0.0011 per image**. ([Google AI for Developers][7])

**Correction to brief:** Keep “Nano Banana Pro is a strong candidate for bible generation and panel rendering,” but soften these claims:

* “14 max refs” = verified.
* “~6 sweet spot” = plausible and supported by third-party testing, but not official in the sources I found.
* “Composite character sheets are explicitly recommended by Google” = not verified in this pass. A third-party guide recommends a multi-angle character reference sheet and uses the “complete 3D understanding” phrase. ([prompting.systems][8])

**Recommended test:** For Phase 0, run composite-vs-atomized references head-to-head on the same character: one multi-angle sheet, one tight headshot, one turnaround crop set, and one expression crop. Measure which preserves identity best across 8–12 panels.

---

## 3. Midjourney V7 / Omni Reference / API / legal status

**Finding:** Midjourney’s **Omni Reference** is the current V7 mechanism for reusing a specific character, object, vehicle, or creature across images. It replaces older Character Reference behavior in V7, uses one image, can be weighted with `--ow`, and costs 2× GPU time. Midjourney’s docs warn that fine details may not perfectly match and that high stylization can compete with Omni influence. ([Midjourney][9])

**Reference modes:**

| Mode                       | What it does                                       | Notes                                                                                         |
| -------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Image prompt               | Influences content, composition, style, and colors | Broad influence; useful but can leak too much. ([Midjourney][10])                             |
| Omni Reference / `--oref`  | Reuses a specific character/object/vehicle/etc.    | V7-specific; one image; weighted with `--ow`; replaces Character Reference. ([Midjourney][9]) |
| Style Reference / `--sref` | Captures look/feel/style, not objects or people    | Weighted with `--sw`; can use multiple style refs. ([Midjourney][11])                         |
| Moodboards                 | Broader personalization/style system               | Useful for aesthetic exploration, not a deterministic pipeline primitive. ([Midjourney][12])  |

**API status:** The brief’s “no public API” claim remains correct. Midjourney’s own Community Guidelines say that, with rare explicitly granted exceptions, Midjourney does not provide an API or third-party app/script access, and automation is prohibited. ([Midjourney][13])

**Pricing/throughput:** Midjourney plans range from $10 to $120/month. Fast GPU time ranges from 3.3 hours/month on Basic to 60 hours/month on Mega; extra Fast GPU time is $4/hour. A normal prompt set of 4 images usually costs about 1 GPU minute, while an Omni Reference prompt costs about 2 GPU minutes. ([Midjourney][14])

**Legal/commercial posture:** Disney and Universal sued Midjourney in June 2025, and Warner Bros. filed a separate suit in September 2025 that was later consolidated with the Disney/Universal litigation. The docket source I found still shows the Disney case active with filings into May 2026. ([Reuters][15])

**Implication:** Midjourney is still useful for **lookbook / hero-image exploration**, but it is a bad fit as the automated backend for a production storyboard system. The stronger architecture is: use Midjourney only where Ben is manually exploring taste, then use OpenAI/Google APIs for systematic bible and panel production.

---

## 4. Image Arena / benchmark verification

**Finding:** The overall “closed-model path is viable” claim is supported, but the exact scores in the brief are stale. Arena.ai’s May 12, 2026 text-to-image leaderboard ranks `gpt-image-2 (medium)` first at **1393±7**, followed by Gemini 3.1 Flash Image / Nano Banana 2 and Gemini 3 Pro Image / Nano Banana Pro. Arena’s image-edit leaderboard ranks `gpt-image-2 (medium)` first at **1467±5**, ahead of ChatGPT high-fidelity and Nano Banana Pro variants. ([arena.ai][3])

Artificial Analysis also ranks **GPT Image 2 high** first among text-to-image models in its leaderboard, with GPT Image 1.5, Nano Banana 2, Nano Banana Pro, and MAI-Image-2 among the top models. ([Artificial Analysis][16])

**Implication:** The brief should not lean on “GPT Image 2 1512 vs Midjourney V7 1270” as a current factual claim. The better statement is:

> Current public image leaderboards support testing an all-OpenAI/Google closed-model production path. Midjourney may remain aesthetically strong for exploration, but the leaderboard case for GPT/Gemini production work is now credible.

---

## 5. Preserve / borrow / do-not-borrow prompting

**Finding:** The proposed grammar is well grounded, but I would present it as a **workflow convention** rather than a model-specific magic phrase.

OpenAI’s guide says to state constraints and invariants explicitly; for edits, it recommends “change only X” and “keep everything else the same,” and it says multi-image inputs should be referenced by index/description. fal.ai’s GPT Image guide gives very similar guidance and provides templates that separate **Change**, **Preserve**, and **Constraints** blocks, including preserving face, identity, pose, lighting, framing, background, geometry, text, and layout. ([OpenAI Developers][4])

**Recommended house grammar:**

```text
Image 1 — character identity reference
Preserve: face structure, hair, build, signature wardrobe.
Do NOT borrow: pose, lighting, background, camera angle.

Image 2 — expression/state reference
Borrow: eye intensity, mouth tension, brow shape.
Do NOT borrow: crop, lighting, background.

Image 3 — location plate
Preserve: well geometry, ruins position, horizon, dust haze.
Do NOT borrow: characters, props not named in the shot.

Image 4 — style reference
Borrow: line quality, ink wash, palette, paper texture.
Do NOT borrow: subject, composition, scene elements.
```

**Implication:** This should become a formal prompt-assembly layer, not ad hoc prompt text. The system should generate these blocks from metadata attached to each reference asset.

---

## 6. Compositional skeleton / camera-angle transfer

**Finding:** This is still the riskiest claim in the brief.

What is documented: reference-guided edits can preserve layout, horizon line, perspective, camera angle, object placement, lighting direction, and composition. fal.ai shows prompt patterns like preserving exact layout, river path, mountain placement, horizon line, and perspective in sketch-to-render workflows. ([Fal.ai][5])

What I did **not** find: a documented, reliable workflow for fresh generation that says “use Image 3 only for camera angle / composition, but do not borrow subject, style, lighting, or environment.”

The research literature reinforces caution: PreciseCam’s abstract says precise camera/lens control is missing in current text-to-image models and proposes explicit camera-parameter conditioning to beat prompt engineering. ([arXiv][17])

**Implication:** Treat this as an empirical test track, not an architecture guarantee. Test “composition reference” with concrete geometric language:

```text
Image 3 is a compositional skeleton only.
Borrow: camera height, horizon placement, subject scale in frame,
foreground/midground/background depth stack, vanishing direction.
Do NOT borrow: subject, costume, location, props, lighting, palette, line style.
```

A successful result means the cinematography reference pack is viable. A failed result means shot grammar must rely more on explicit DSL prose and perhaps later ControlNet/3D/previs methods.

---

## 7. Character bible / expression sheet / multi-panel consistency

**Finding:** The bible idea is supported, but long-sequence consistency remains only partially proven in public sources.

OpenAI’s official cookbook includes a character-anchor workflow where a generated character is reused through the edit endpoint to continue a children’s book scene, with explicit identity constraints like keeping the same facial features and not redesigning the character. That supports the basic “character anchor → new scene” pattern, but it is not a 60-panel proof. ([OpenAI Developers][4])

Third-party evidence is mixed but useful. A Weavy.ai + Nano Banana Pro experiment reported that simple Gemini/Nano Banana chat-based storyboarding degraded rapidly across panels, while a structured node-based workflow improved consistency to roughly 80–90% after tuning, with occasional fine-detail drift. ([shawnkelshaw.com][18])

A Google AI Developers Forum thread is especially relevant: a user trying to generate 20–30 sequential pages with Gemini 3 Pro Image hit the 14-image attachment limit when keeping prior images in history. A Google-affiliated responder recommended File API / `file_uri` usage and sliding-window approaches; another responder said AI Studio was not using “magic” beyond the raw API. ([Google AI Developers Forum][19])

Recent research also supports the direction of the architecture. CANVAS frames long-form visual storytelling as a continuity problem involving character, background, and prop consistency, and reports improvements by explicitly planning continuity. StoryBlender proposes a continuity memory graph and canonical asset materialization to decouple global assets from shot-specific variables. DreamShot uses multi-reference role conditioning for identity alignment across storyboard shots. ([arXiv][20])

**Implication:** The character/world bible and state ledger are not overengineering; they match both product pain and current research direction. But the expression sheet should be treated as a **diagnostic validation artifact**, not an assumed solved step.

**Recommended validation artifact:** one principal character, in target style:

* 1 turnaround sheet.
* 1 action/pose sheet.
* 12-expression sheet.
* 8-panel micro-sequence using those refs.
* Failure log: identity drift, expression drift, pose drift, wardrobe drift, lighting/style leakage.

---

## 8. Existing AI storyboard tools / competitive landscape

This area is now crowded. The proposed system should not be positioned as “AI storyboards exist or don’t exist.” They exist. The question is whether any tool gives Ben the **director-controlled, bible-led, state-ledger, pitch-book-grade workflow** he wants.

| Tool                           | Current capability                                                                                                                                                                | Gap vs proposed system                                                                                                                                                                                       |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Boords**                     | AI storyboard generator, script/brief to structured storyboard, consistent characters, animatics, comments, approvals, exports. Strong client-review layer. ([boords.com][21])    | Great sign-off layer; less evidence of deep director-controlled DSL/state ledger/bible invalidation.                                                                                                         |
| **LTX Studio**                 | Script-to-video and AI storyboard generator; extracts characters/objects as reusable Elements; FLUX/Nano Banana model choice; shot-by-shot visuals. ([LTX Studio][22])            | Closest “AI production suite” competitor; needs hands-on test for granular shot control and bible-level consistency.                                                                                         |
| **Adobe Firefly Boards**       | Text/image/script to storyboard; consistent lighting, character style, background elements; collaboration/export; commercial-safe positioning for Adobe models. ([adobe.com][23]) | Strong mainstream tool; may be less specialized for director-authored beat/state ledger and custom model routing.                                                                                            |
| **Higgsfield Popcorn**         | Visually consistent scenes, reference characters/items, multi-angle shots, up to 8 images in a sequence, export to Sora 2 claim. ([Higgsfield][24])                               | Interesting for camera/keyframe workflows; Sora-dependent messaging is questionable because OpenAI says Sora web/app was discontinued April 26, 2026 and API ends Sept. 24, 2026. ([OpenAI Help Center][25]) |
| **Drawstory**                  | Script-to-storyboard, upload characters, character consistency, locations/cast/previs, pitch deck positioning; plans from free to production. ([drawstory.ai][26])                | Very directly aimed at directors; needs product teardown before building similar UI.                                                                                                                         |
| **MITO**                       | Infinite collaborative canvas, narrative/storyboard, moodboards, collaboration, continuity, regeneration while preserving cast/brand identity, model integrations. ([MITO][27])   | Potentially very close at workflow level; should be watched carefully.                                                                                                                                       |
| **Runway**                     | Has a Storyboard Creator featured workflow and related workflows for consistent sequences and characters. ([Runway Academy][28])                                                  | More video-model/workflow oriented; less clear as a pitch-book storyboard system.                                                                                                                            |
| **Storyboarder / Wonder Unit** | Free/open-source manual storyboarding app with drawing, metadata, shot type, export, Photoshop integration, and a shot generator. ([Wonder Unit][29])                             | Useful reference for UX and export conventions; not a modern bible/LLM continuity system.                                                                                                                    |
| **Showrunner / Fable**         | User-directed AI animated-show creation via simulation/community model. ([Showrunner][30])                                                                                        | More AI-TV/simulation than pitch-book storyboarding.                                                                                                                                                         |

**Competitive conclusion:** The differentiator cannot just be “AI storyboard generator.” It has to be:

> A director-controlled pitch-storyboard system that externalizes a film’s visual world into bibles, maps directorial intent to script position, assembles role-labeled references automatically, preserves prompt lineage, and flags continuity drift.

That is more specific and defensible than a generic script-to-board tool.

---

## 9. Production economics

Using the brief’s rough workload:

* 4 principals × 25 bible assets = **100 images**
* 60 panels × 3 candidates = **180 images**
* 25% panel re-roll allowance = **45 images**
* 20% bible rework allowance = **20 images**
* Total: about **345 output images**, before extra location/prop plates.

Output-only cost estimates:

| Stack                                       |                                                   Approx output cost for 345 images | Notes                                                                                          |
| ------------------------------------------- | ----------------------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------- |
| OpenAI `gpt-image-2`, 1536×1024 medium      |                                                                                ~$14 | Based on $0.041/image. ([OpenAI Developers][1])                                                |
| OpenAI `gpt-image-2`, 1536×1024 high        |                                                                                ~$57 | Based on $0.165/image. ([OpenAI Developers][1])                                                |
| Google Gemini 3 Pro Image, 1K/2K            |                                                                                ~$46 | Based on $0.134/image standard pricing. ([Google AI for Developers][7])                        |
| Google Gemini 3 Pro Image, 1K/2K Batch/Flex |                                                                                ~$23 | Based on $0.067/image. ([Google AI for Developers][7])                                         |
| Google Gemini 3 Pro Image, 4K               |                                                                                ~$83 | Based on $0.24/image. ([Google AI for Developers][7])                                          |
| Midjourney                                  | Harder to map per image; likely cheap in subscription GPU terms but not automatable | Omni Reference prompt ≈2 GPU minutes; Pro plan has 30 Fast GPU hours/month. ([Midjourney][14]) |

**Important:** the cost bottleneck is not raw image generation. Even at high quality, model output cost for a first pitch-scale test is probably **tens of dollars, not thousands**, excluding human time and any subscription seats. The real costs are Ben’s art-direction time, prompt iteration, failed bible assets, continuity review, and layout/polish.

**Re-roll rate:** I did not find a strong public source validating the brief’s 20–30% re-roll assumption for reference-heavy storyboard workflows. Treat that as a planning prior and measure it in Phase 0/1.

---

## Recommended meeting stance with Ben

The strongest updated framing is:

> “The model layer is good enough to test now. The unsolved product problem is not whether an image model can make nice panels; it is whether we can build a controllable production memory: bibles, state ledger, role-labeled refs, prompt lineage, candidate history, and continuity checks.”

For the next experiment, I would not try to build a full product. I would run a **one-character / one-location / eight-panel validation**:

1. Choose one visual style anchor.
2. Generate one principal character bible: turnaround, 8–12 expressions, 4 poses.
3. Generate one location plate and one prop sheet.
4. Render an 8-panel micro-sequence with 3 candidates per panel.
5. Log every failure by type: identity, expression, pose, wardrobe, geography, composition, style leakage, reference leakage.
6. Compare OpenAI vs Nano Banana Pro on the same prompt/ref package.
7. Optional: run Midjourney only for hero-image exploration, not panel production.

That test directly validates the load-bearing claims: bible creation, expression consistency, role-labeled prompt assembly, compositional transfer, and real re-roll rates.

## Open items not fully resolved in this pass

The exact Google-originated “composite sheet gives complete 3D understanding” quote was **not verified**; I found it in a third-party guide. The most important remaining research items are production user examples of 6–20+ panel consistency, real failure/re-roll rates from teams shipping pitch boards, hands-on product teardown of LTX / Drawstory / MITO / Boords / Firefly Boards, and a legal review of Midjourney/artist-style risk for commercial pitch books.

[1]: https://developers.openai.com/api/docs/guides/image-generation "Image generation | OpenAI API"
[2]: https://ai.google.dev/gemini-api/docs/image-generation "Gemini API  |  Google AI for Developers"
[3]: https://arena.ai/leaderboard/text-to-image "Text-to-Image Leaderboard - Best AI Image Generators"
[4]: https://developers.openai.com/cookbook/examples/multimodal/image-gen-models-prompting-guide "GPT Image Generation Models Prompting Guide"
[5]: https://fal.ai/learn/tools/prompting-gpt-image-2 "GPT Image 2 Prompting Guide and Examples | fal.ai"
[6]: https://blog.google/innovation-and-ai/products/nano-banana-pro/ "Nano Banana Pro: Gemini 3 Pro Image model from Google DeepMind"
[7]: https://ai.google.dev/gemini-api/docs/pricing "Gemini Developer API pricing  |  Gemini API  |  Google AI for Developers"
[8]: https://prompting.systems/blog/nano-banana-pro-character-consistency-guide "Ultimate Nano Banana Pro Character Consistency Guide"
[9]: https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference "Omni Reference – Midjourney"
[10]: https://docs.midjourney.com/hc/en-us/articles/33329261836941-Getting-Started-Guide "Getting Started Guide – Midjourney"
[11]: https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference "Style Reference – Midjourney"
[12]: https://docs.midjourney.com/hc/en-us/articles/39193335040013-Moodboards "Moodboards – Midjourney"
[13]: https://docs.midjourney.com/hc/en-us/articles/32013696484109-Community-Guidelines "Community Guidelines – Midjourney"
[14]: https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans "Comparing Midjourney Plans – Midjourney"
[15]: https://www.reuters.com/business/media-telecom/disney-universal-sue-image-creator-midjourney-copyright-infringement-2025-06-11/?utm_source=chatgpt.com "Disney, Universal sue image creator Midjourney for copyright infringement"
[16]: https://artificialanalysis.ai/image/leaderboard/text-to-image "Text to Image Leaderboard - Top AI Image Models"
[17]: https://arxiv.org/abs/2501.12910 "[2501.12910] PreciseCam: Precise Camera Control for Text-to-Image Generation"
[18]: https://shawnkelshaw.com/2025/12/ai-generated-storyboards/ "Using Weavy.ai + Google Nano Banana Pro to generate character consistent storyboards – Shawn Kelshaw"
[19]: https://discuss.ai.google.dev/t/how-to-achieve-ai-studio-like-multi-turn-image-consistency-with-gemini-3-pro-image-api-in-automation-workflows/110709 "How to achieve AI Studio-like multi-turn image consistency with Gemini 3 Pro Image API in automation workflows? - Gemini API - Google AI Developers Forum"
[20]: https://arxiv.org/abs/2604.13452 "[2604.13452] CANVAS: Continuity-Aware Narratives via Visual Agentic Storyboarding"
[21]: https://boords.com/ai-storyboard-generator "Free AI Storyboard Generator (Create Storyboards Online) | Boords"
[22]: https://ltx.studio/ "The Creative Studio for AI Video Production | LTX Studio"
[23]: https://www.adobe.com/products/firefly/features/storyboard.html "AI Storyboard Generator Online - Adobe Firefly"
[24]: https://higgsfield.ai/storyboard-generator "AI Storyboard Generator — Plan Videos Visually | Higgsfield"
[25]: https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation "What to know about the Sora discontinuation | OpenAI Help Center"
[26]: https://www.drawstory.ai/ "Script To Storyboard AI"
[27]: https://mito.ai/ "MITO — AI Video Creation Platform | Create Videos Free"
[28]: https://academy.runwayml.com/tutorial/storyboard-featured-workflow "How to Use Storyboard Featured Workflow | Runway Academy | Runway Academy"
[29]: https://wonderunit.com/storyboarder/ "Storyboarder - The best and easiest way to storyboard. | Wonder Unit"
[30]: https://www.showrunner.xyz/ "Showrunner | Create Animated Shows and Scenes"
