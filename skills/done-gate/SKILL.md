---
name: done-gate
description: Use at the end of every coding/editing round in Claude Code, before declaring the work done or ending the session. Explain in plain (non-technical) language what was built, where it is, and how to use it, then walk the user through a checklist to verify each feature/module — only items the user checks off pass; unchecked items loop back for fixes until everything is checked. Invoke manually with /done-gate; supports log:/as:/lang: arguments.
user-invocable: true
---

# done-gate — acceptance-gated wrap-up

This skill governs how Claude Code **wraps up** each round of coding/editing work. Core rule:
before declaring done or ending, explain the result in plain language and have the user verify
each item via a checkmark. **Do not wrap up until the user has checked off everything.**

## Enabled toggle (check first)

If `.done-gate.json` in the project root has `"enabled": false`, **do not run the acceptance gate**
on wrap-up. If invoked explicitly while disabled, state that done-gate is off and how to re-enable
(`/done-gate-config on`). The user may also ask to skip the gate for a single conversation in chat —
honor that without changing any config. When enabled (default), proceed with the flow below.

## Principle 0: anti-self-pass guardrail (highest priority, overrides everything)

- **Never** self-declare "done / finished / should be fine" while the user has not checked items off.
- **Never** check items on the user's behalf, or treat "I tested it" as a pass.
- The **only** source of "pass" is the user personally checking the item in the checklist.
- Any unchecked item counts as "not passed" — keep fixing, do not end the round.
- If unsure whether an item is done, default to "not passed".

## Arguments (read from $ARGUMENTS; defaults apply when absent)

| Arg | Values | Default | Effect |
|------|----|------|------|
| `log:` | `on` / `off` | `on` | Whether to append this round's acceptance to `ACCEPTANCE.md` |
| `as:`  | `user` / `elder` / `pm` / `client` | `user` | Audience and tone of the plain-language summary |
| `lang:`| `en` / `zh` / `both` | `en` | Output language of the plain-language summary |

Example: `/done-gate log:off as:elder lang:both`

## Flow A — plain-language result summary

For **each feature/module** delivered this round, write one short block with **only three things**:

1. **What it does** — in everyday terms, as if explaining to a non-technical family member what problem it solves.
2. **Where it is** — from the user's point of view: which screen area, which button, which menu path. **Not a file path.**
3. **How to use it** — step-by-step, so following along actually reaches the feature.

### Strictly forbidden content
File names, folder paths, function/variable names, framework/library names, APIs, databases,
code snippets, any technical jargon. If a sentence needs a technical term to make sense, rephrase
it as an analogy or as the result the user sees.

### Audience tone (per `as:`)
- `user`: a general user, clear and conversational.
- `elder`: for an older relative — slower, more concrete, no loanwords, lots of analogies.
- `pm`: for a product manager — focus on what the user can now do and the value it brings.
- `client`: for a client — focus on the delivered outcome and verifiable value, formal tone.

> When struggling to write plain language or to translate jargon into human terms, read
> [references/plain-language-guide.md](references/plain-language-guide.md) (jargon→plain tables, per-audience templates).

### Good / bad example (follow the "good" format)

✅ Good:
> **Export report**
> - What it does: lets you save the data on screen to a file in one click, to email or keep.
> - Where it is: the top-right button row, the one labeled "Export".
> - How to use: 1) pick the month you want → 2) click "Export" top-right → 3) choose where to save.

❌ Bad (jargon, uses a file path for "where"):
> Added `ExportService.exportCSV()`, wired to `ReportPage.tsx` onClick, calling backend `/api/export`…

More full conversation examples: [references/examples.md](references/examples.md).

## Flow B — checklist verification

**Hard prerequisite: before asking the user to check anything, you MUST first present the full
Flow A plain-language summary (what changed, where, how to use). Never jump straight to the checklist.**
Throwing a checklist with no plain-language summary is a violation.

Use `AskUserQuestion` (`multiSelect: true`) with each feature as one option, and ask the user to
**check the items they have confirmed done**. Each option's label = feature name, description = a
one-line plain-language way to verify it.

> How to split features into checkable items and write the "how to verify" description:
> [references/checklist-writing.md](references/checklist-writing.md).

- Items the user checks → passed.
- Unchecked items → not passed.

## Flow C — fix loop

When any item is unchecked (not passed):

**C-1 Diagnose: ask "why not checked" first**
For each unchecked item, use `AskUserQuestion` to offer reason options so the user picks a direction:
- **Has a bug** — ask the user to describe the problem / how to reproduce (may be left blank; Claude investigates).
- **Wants improvement** — ask the user for the improvement they expect.
- **Custom** — the user explains what is still missing.

(You may ask about several unchecked items at once; use option descriptions to prompt for detail.)

**C-2 Fix and re-verify**
- Treat unchecked items as new requirements per the chosen direction → fix.
- After fixing, **re-run A + B only for the affected items** (no need to re-list passed ones).
- Repeat C-1～C-2 until the user has checked off **everything**.

## Flow D — wrap-up condition

- Only after the user checks off all features may the round end.
- On wrap-up, emit the summary and record per the value-add features below.
- Until then, no matter how green the tests or how high your self-assessment, **do not** self-wrap-up (see Principle 0).

## Value-add features

### 1. Closing ✅/❌ summary table
On wrap-up, emit a table summarizing each item's status:

| Feature | Status |
|---------|--------|
| Export report | ✅ Verified |
| Filter | ✅ Verified |

(If items remain unpassed mid-loop, mark them ❌ and state what's still missing.)

### 2. Unpassed items → TODO
If the user stops early, or an item can't be finished for now, collect unpassed items into a
plain-text follow-up list for the next round, formatted: `- [ ] <feature> — what's still missing`.

### 3. Acceptance log ACCEPTANCE.md (when `log:on`)
After wrap-up, **append** this round's plain-language summary + checkmark results to
`ACCEPTANCE.md` in the project root. Create it if absent; otherwise append a new round block:

```markdown
## Acceptance — Round N

### Features this round
(Flow A plain-language summary, per feature)

### Verification result
| Feature | Status |
|---------|--------|
| ... | ✅/❌ |
```

> No date stamps (avoid guessing the time); the round number = existing block count + 1.
> When `log:off`, skip this step entirely. Template: [examples/ACCEPTANCE.sample.md](../../examples/ACCEPTANCE.sample.md).

### 4. Bilingual output (per `lang:`)
- `en`: English only.
- `zh`: Traditional Chinese only.
- `both`: each block in English first, then Chinese.

### 5. Screenshot annotation (web, optional)
If this round's change is a browser-visible web UI and a playwright MCP tool is available:
- Open the relevant page, screenshot the spot where the feature lives, as a visual aid for the summary.
- Save screenshots to the scratchpad, and reference them in the summary.

If there is no playwright MCP or it's not a web project: **skip automatically** and tell the user in
one line, "screenshots not enabled in this environment, skipped". Do not install a browser or add
dependencies just to screenshot. Detailed steps: [references/screenshot-flow.md](references/screenshot-flow.md).

## Companion commands
- `/done-gate-status` — list the current round's per-item status (passed / pending).
- `/done-gate-log` — summarize the delivery history in `ACCEPTANCE.md`.
- `/done-gate-config` — turn done-gate `on`/`off`, or view/set defaults (`log`/`as`/`lang`) in `.done-gate.json`.
- `/done-gate-handoff` — generate a plain-language handoff doc from verified features.
- `/done-gate-explain` — re-explain one delivered feature in plain language (optional audience).

> Defaults precedence: explicit `/done-gate` args > `.done-gate.json` (if present) > built-in defaults.

## Wrap-up self-check
- [ ] Plain-language summary has zero jargon, all three parts (what / where / how)
- [ ] Used a checklist to ask the user to verify
- [ ] Unchecked items were fixed; never self-declared done
- [ ] Round ended only after the user checked off everything
- [ ] Emitted the ✅/❌ summary table (and wrote ACCEPTANCE.md when `log:on`)
