# Agent Instructions

## Scroggins / Manson Image Generation

For this vault, any user request to run an image-generation prompt under `_trace/scroggins-manson/pages/` is an explicit request to delegate image generation to fresh-context subagents.

Always use one fresh-context subagent per requested variant, including a single variant.

When spawning image-generation subagents:
- set `fork_context: false`
- create exactly one subagent per requested variant
- determine and assign exact output filenames before spawning subagents
- pass each subagent its exact assigned output filename
- do not let subagents independently choose the next available variant filename
- do not reuse generation context between variants
- do not pass prior generated variants, inline previews, or critique from one variant subagent to another unless the user explicitly asks for an iterative correction pass

The purpose of this standing instruction is to prevent image-generation context pollution from the primary conversation and from other variants.
