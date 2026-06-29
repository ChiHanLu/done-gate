# How to write good checklist items (Flow B)

The checklist is the user's only "check it off" interface. If items are written poorly,
the user can't judge whether to check them.

## One item = one observable outcome

- ✅ "Export report: can save the on-screen data to a file"
- ❌ "Export + filter + style tweaks" (too bundled; the user can't check half)

One feature → one item. If an item really contains several independent outcomes, split it.

## Describe "what the user can do", not the implementation

- ✅ "Forgot password: reset it yourself via email, no support needed"
- ❌ "Wired up an SMTP email service"

## The description should say "how to verify it yourself"

An option's description is the user's **self-verification guide** — follow it and you know whether to check:

> Export report
> description: On the report page, click "Export" top-right; confirm a real, openable file downloads.

## Checkable vs hard-to-check

- Checkable: a result the user can see/do themselves (screen, behavior, output).
- Hard to check: pure background changes with no visible result → give an "observable proxy".
  e.g. "auto-email a daily report" → provide "trigger it once manually, confirm the email arrives".

## Keep the count manageable

- Aim for ≤ 7 items per round; split into batches if more.
- Don't re-list already-passed items next round (see Flow C-2).

## Anti-patterns
- ❌ One item packed with multiple features.
- ❌ Jargon as the item name (the user can't tell what to verify).
- ❌ A description that just restates the title without a way to verify.
