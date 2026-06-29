---
description: Generate a plain-language handoff/delivery document from the verified features, for a client or for onboarding.
allowed-tools: Read, Write
---

Produce a clean **handoff document** describing the delivered features in plain language —
suitable to hand to a client or a new user. Pulls from `ACCEPTANCE.md` (and the current round if any).

Output: write `HANDOFF.md` in the project root (overwrite). For each **verified (✅)** feature, include:
- **What it does** — plain language, no jargon (same rules as done-gate Flow A).
- **Where it is** — user-visible location.
- **How to use it** — numbered steps.

Structure:
```markdown
# Handoff

## <Feature name>
- What it does: …
- Where it is: …
- How to use it: 1) … 2) … 3) …
```

Rules:
- Include only features the user has **verified** (✅); skip pending ones (mention them in a short
  "Not yet delivered" note at the end if any exist).
- Default audience is `client`; honor `as:` in `$ARGUMENTS` to retune tone (e.g. `as:elder`).
- Zero technical terms, file names, or code — this document is for non-technical readers.
