# Changelog

All notable changes to this project are documented here.
Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] — initial release

### Added
- Core `done-gate` skill: plain-language result summary → checklist verification →
  diagnose-and-fix loop. Only user-checked items pass; the round won't wrap up until
  everything is checked.
- Anti-self-pass guardrail (Principle 0): Claude may never self-declare done.
- Arguments: `log:` (acceptance log on/off), `as:` (audience: user/elder/pm/client),
  `lang:` (output language: en/zh/both, default en).
- Commands: `/done-gate` (alias `/dg`), `/done-gate-status`, `/done-gate-log`,
  `/done-gate-config`, `/done-gate-handoff`, `/done-gate-explain`.
- On/off toggle via `/done-gate-config off|on` (persisted as `enabled` in `.done-gate.json`);
  respected by the skill and the standing CLAUDE.md rule.
- References: plain-language guide (with per-domain jargon tables), checklist-writing guide,
  screenshot-flow guide, full conversation examples.
- Acceptance log `ACCEPTANCE.md` (auto-appended per round) + sample.
- Bilingual docs (`README.md` / `README.zh.md`), LICENSE (MIT), CONTRIBUTING.
- Packaged as a Claude Code plugin (`.claude-plugin/plugin.json`).
