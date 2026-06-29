# Full conversation examples

Demonstrates done-gate's A→B→C→D flow for Claude to follow.

## Example 1: passes on the first try

```
You: Add a "Remember me" checkbox to the login page

Claude (Flow A, plain language first):
  Remember me
  - What it does: once checked, you won't have to log in again next time you open it.
  - Where it is: below the password field on the login screen — the new little checkbox.
  - How to use: check "Remember me" when logging in, then press Log in.

Claude (Flow B, checklist): Check the items you've confirmed done:
  ☐ Remember me

You: ✅ (checked)

Claude (Flow D, wrap-up):
  | Feature | Status |
  |---------|--------|
  | Remember me | ✅ Verified |
  Round complete, written to ACCEPTANCE.md.
```

## Example 2: not passed → diagnose → fix

```
Claude (Flow B): Check the items you've confirmed done:
  ☐ Remember me

You: (leave it unchecked)

Claude (Flow C-1, ask why): "Remember me" is unchecked. Why?
  ○ Has a bug  ○ Wants improvement  ○ Custom

You: Has a bug → still asks me to log in again after checking it

Claude (Flow C-2, fix then re-verify only this item):
  (plain-language summary of the fix) … Please confirm again:
  ☐ Remember me

You: ✅

Claude (Flow D, wrap-up): ✅ All passed, wrapping up and recording.
```

## Example 3: multiple features, some not passed

```
Claude (Flow B): Check the items you've confirmed done:
  ☐ Remember me   ☐ Forgot password   ☐ Social login

You: ✅ Remember me, ✅ Forgot password (Social login left unchecked)

Claude (Flow C-1, ask only about the unpassed item): "Social login" is unchecked. Why?
  ○ Has a bug  ○ Wants improvement  ○ Custom

…(fix and re-verify "Social login" only; the two passed items are not re-listed)…

Final wrap-up summary:
| Feature | Status |
|---------|--------|
| Remember me | ✅ |
| Forgot password | ✅ |
| Social login | ✅ |
```
