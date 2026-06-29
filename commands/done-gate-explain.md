---
description: Re-explain a specific delivered feature in plain language, with an optional audience switch.
allowed-tools: Read
---

Explain one delivered feature again, in plain language, on demand.

`$ARGUMENTS`: the feature name, optionally followed by `as:<user|elder|pm|client>`.
Example: `/done-gate-explain Export report as:elder`

Output the three plain-language parts (same rules as done-gate Flow A):
- **What it does**
- **Where it is**
- **How to use it**

Rules:
- Default audience is `user`; honor `as:` if given (see
  [references/plain-language-guide.md](../references/plain-language-guide.md) for per-audience tone).
- Zero jargon, file names, or code.
- If the named feature can't be found in `ACCEPTANCE.md` or the current round, ask the user which
  feature they mean instead of guessing.
