---
description: Summarize the delivery history in the project's ACCEPTANCE.md (what each round built, verification result).
allowed-tools: Read
---

Read `ACCEPTANCE.md` in the project root and summarize the delivery history in plain language:

- List by round: what features Round N built, and each feature's final verification status (✅/❌).
- Keep it plain and non-technical (same rules as done-gate Flow A).
- If `ACCEPTANCE.md` doesn't exist, tell the user there's no record yet (possibly `log:off`, or no round verified yet).

$ARGUMENTS (optional): pass a round number (e.g. `3`) to summarize only that round; pass `last` for the latest round only.
