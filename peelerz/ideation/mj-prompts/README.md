# mj-prompts — naming convention

Files are named `YYYY-MM-DD-NN-desc.md`, where `NN` is a two-digit
per-day sequence number in creation order. This makes a plain
alphabetical sort equal to chronological order.

Next file today continues the counter (e.g. `2026-07-13-07-….md`);
a new day resets to `-01-`.

Two writers share this counter (Fable and Codex sessions). Always `ls`
the directory immediately before numbering a new file — a `-06`
collision on 2026-07-14 was resolved by renumbering the newer file
to `-07`.
