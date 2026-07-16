# Visual probes — batch 04 Lite

Large, reference-guided Tina exploration using `gemini-3.1-flash-lite-image`.

## Intent

This batch tests whether the low-cost Lite model is useful for broad edit-style exploration before
spending on higher-fidelity generations. It uses the treatment's Tina-in-car frame as the edit target
and the bite close-up as supporting identity/product reference. Most prompts change only the exterior
world visible through the passenger window.

These are discovery images, not finalists. The batch deliberately spans quiet transformation,
theatrical construction, scale rupture, mixed media, art-historical landscape, and wild world detail.

## Run settings

- Model: `gemini-3.1-flash-lite-image`
- Output: one 1K, 16:9 image per prompt
- Jobs: 18
- Batch source: [prompts.yaml](prompts.yaml)
- Batch overview: [contact-sheet.png](contact-sheet.png)
- Findings and shortlist: [RESULTS.md](RESULTS.md)

## Evaluation questions

- Does Lite preserve Tina and the rideshare well enough to support cheap exploration?
- Does the edit-target wording localize changes outside the window?
- Which visual worlds create genuine curiosity rather than generic fantasy polish?
- Which ideas deserve a fuller Flash or Pro pass?
