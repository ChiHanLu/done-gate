---
description: View or set this project's done-gate defaults (log / as / lang) so you don't pass them as arguments every time.
allowed-tools: Read, Write, Edit
---

Manage per-project done-gate defaults, stored in `.done-gate.json` in the project root.

Behavior by `$ARGUMENTS`:
- **(empty)** — read `.done-gate.json` and show the current defaults; if absent, show the built-in
  defaults (`log:on`, `as:user`, `lang:en`) and note no config file exists yet.
- **`key:value` pairs** (e.g. `as:client lang:zh log:off`) — create or update `.done-gate.json`
  with those keys, then echo the resulting config.
- **`reset`** — delete `.done-gate.json` (revert to built-in defaults).

Config file shape:
```json
{ "log": "on", "as": "user", "lang": "en" }
```

Rules:
- Only the keys `log`, `as`, `lang` are valid; reject unknown keys with a one-line note.
- When the `done-gate` skill runs, `.done-gate.json` (if present) overrides built-in defaults,
  and explicit `/done-gate` arguments override the file.
