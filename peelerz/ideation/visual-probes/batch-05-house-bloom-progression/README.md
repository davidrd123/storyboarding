# House-bloom progression

Four reference-guided frames testing a causal visual progression:

1. one house shows a nearly missable first symptom;
2. Tina notices the opening rule advancing toward her;
3. the same rule reaches the car, which begins to bloom open;
4. the car becomes an open viewing platform inside the fully revealed neighborhood.

The central thought is that the car is another enclosure around Tina—effectively a moving little
house. The environment's behavior can therefore reach the car without introducing a second,
unrelated magical mechanism.

## Run settings

- Model: `gemini-3.1-flash-lite-image`
- Output: one 1K, 16:9 image per beat
- Jobs: 4
- Batch source: [prompts.yaml](prompts.yaml)
- Selected four-frame sequence: [progression-strip.png](progression-strip.png)
- Reading and next questions: [RESULTS.md](RESULTS.md)

Two targeted retry prompts are preserved separately:

- [prompt-01-retry.yaml](prompt-01-retry.yaml) reduces the opening beat to one nearly invisible anomaly.
- [prompt-03-retry.yaml](prompt-03-retry.yaml) interpolates the missing bridge from successful frames
  2 and 4.
