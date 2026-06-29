# Screenshot annotation flow (web, optional)

When this round's change is a browser-visible web UI and a playwright MCP tool is available,
use screenshots to make "where it is" obvious.

## Preconditions
1. Did this round produce visible web UI? No → skip.
2. Is a playwright MCP tool available (`mcp__playwright__*`)? No → skip and tell the user
   "screenshots not enabled in this environment, skipped".
3. Is the app running and openable? You need a local URL; if you can't get one, ask or skip.

## Steps
1. `browser_navigate` to the relevant page.
2. If needed, `browser_snapshot` to get the element structure and locate where the feature lives.
3. `browser_take_screenshot`; save to the scratchpad (not the user's project directory).
4. In the "where it is" sentence of the plain-language summary, reference that screenshot.
5. Screenshots are an aid only; they **do not replace** the user's own verification and checkmark.

## Annotation tips
- Capture "the whole area", not a single pixel, so the user can orient.
- One screenshot per feature; name the file after the feature (e.g. `export-button.png`).
- When unsure of the location, leave it unmarked rather than mark it wrong.

## Do not
- Don't install a browser, add dependencies, or change project config just to screenshot.
- Don't dump screenshots into the user's repo; use the scratchpad.
- If there's no playwright, skip honestly — don't pretend there's an image.
