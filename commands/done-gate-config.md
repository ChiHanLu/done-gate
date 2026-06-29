---
description: Turn done-gate on/off for this project, or view/set its defaults (log / as / lang). State persists in .done-gate.json.
allowed-tools: Read, Write, Edit
---

Manage per-project done-gate settings, stored in `.done-gate.json` in the project root.

Behavior by `$ARGUMENTS`:
- **(empty)** — read `.done-gate.json` and show current settings; if absent, show built-in
  defaults (`enabled:on`, `log:on`, `as:user`, `lang:en`) and note no config file exists yet.
- **`off`** — set `enabled: false` (done-gate stops auto-running on wrap-up for this project).
- **`on`** — set `enabled: true`.
- **`key:value` pairs** (e.g. `as:client lang:zh log:off`) — create or update `.done-gate.json`
  with those keys, then echo the resulting config.
- **`reset`** — delete `.done-gate.json` (revert to built-in defaults).

Config file shape:
```json
{ "enabled": true, "log": "on", "as": "user", "lang": "en" }
```

Rules:
- Valid keys: `enabled`, `log`, `as`, `lang`. Reject unknown keys with a one-line note.
- When `enabled` is `false`, the `done-gate` skill must NOT run the acceptance gate automatically;
  if invoked explicitly while disabled, say it's off and how to re-enable (`/done-gate-config on`).
- Precedence when the skill runs: explicit `/done-gate` arguments > `.done-gate.json` > built-in defaults.
- To skip the gate for a single conversation only, the user can just say so in chat — no config change needed.
