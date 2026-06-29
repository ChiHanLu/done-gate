---
description: List the current round's per-feature verification status (passed / pending), without ending the round.
allowed-tools: Read
---

List the current status of every feature delivered **this round** as a table:

| Feature | Status |
|---------|--------|
| <feature> | ✅ Verified / ❌ Pending (what's missing) |

Rules:
- "Verified" applies only to items the **user has personally checked off**; everything else is ❌ Pending.
- Do not declare the round complete or wrap up here — this is just a progress snapshot.
- If no verification has happened yet, prompt the user to run `/done-gate` to start.
