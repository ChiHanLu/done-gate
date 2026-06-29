# Contributing

Thanks for helping improve **verify-done**.

## Project layout

```
.
├── .claude-plugin/plugin.json   # plugin manifest
├── skills/verify-done/SKILL.md  # the skill (core logic)
├── commands/                    # /verify-status, /verify-log
├── references/                  # deep-dive docs, loaded on demand
├── examples/                    # sample ACCEPTANCE.md
├── CLAUDE.md                    # standing rule that triggers the skill every round
└── README.md / README.zh.md
```

## Local testing in this repo

Option A — install as a plugin (recommended): add this repo as a plugin source in Claude Code,
then `/verify-done` and the companion commands are available everywhere.

Option B — project skill: copy `skills/verify-done/` into a project's `.claude/skills/`
and add the standing rule from `CLAUDE.md`. The skill then auto-loads when you open that project.

## Design principles (please keep)

- **Keep SKILL.md lean.** Core flow stays in `SKILL.md`; detailed material goes to `references/`
  and is linked, not inlined (progressive disclosure).
- **The user's checkmark is the only source of "done".** Never let Claude self-pass.
- **Plain language only** in user-facing output: no file names, function names, or jargon.

## Making changes

1. Edit the relevant file (logic → `SKILL.md`; reference material → `references/`).
2. If you add a command, register it in `.claude-plugin/plugin.json` under `commands`.
3. Bump `version` in `plugin.json` for releases.
4. Update both `README.md` (English) and `README.zh.md` (Chinese) when behavior changes.
