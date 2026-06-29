# Plain-language guide (deep dive)

Flow A must translate "what was done" into words a non-technical person understands.
This file is the reference for when the words won't come.

## The golden structure (three sentences per feature)

1. **What it does** — what problem it solves for the user, what result it brings. Starting with "You can…" is safest.
2. **Where it is** — the location the user can see (screen area / button label / menu path), **never** a file path.
3. **How to use it** — numbered steps; following them reaches the feature.

## Jargon → plain language

| Technical phrasing | Plain phrasing |
|--------------------|----------------|
| Added an API endpoint | Lets the screen fetch / send data |
| Refactored a function | Tidied up how it works behind the scenes; nothing changes for you |
| Fixed a null pointer / exception | Fixed a case that crashed or errored the screen |
| Added caching | Makes opening the same thing again faster |
| Added an index / optimized a query | Makes data load faster; the list won't lag |
| Added validation | Stops you from mistyping or leaving things out |
| Added unit tests | Added automatic checks, so future changes are less likely to break it |
| Integrated a third-party service | Connected an outside service (e.g. email, payment) |
| State management | Lets the screen remember your recent choices |
| Responsive / RWD | Looks good on both phone and computer |

> Principle: what matters is the **difference the user feels**; how it's done under the hood need not be said.

## Per-audience templates (the `as:` arg)

**user (general user)**
> You can now save the list to a file in one click. It's the "Export" button top-right — pick the range, click it, choose where to save.

**elder (older relative)**
> There's a new "save it" feature. It's like printing what's on screen onto a sheet of paper to keep.
> It's at the top-right of the screen — a button that says "Export". First pick which months you want,
> then press it; the computer will ask where to put it, choose the Desktop and you'll find it there.

**pm (product manager)**
> Users can now self-serve report exports without engineering help — one fewer manual step.
> Entry point is top-right of the report page, supports filter-then-export.

**client**
> This delivery: a "report export" feature. On the report page top-right, users can export the
> filtered data to a file in one click, for sending out or archiving. Three steps: pick range → export → choose location.

## Domain-specific jargon → plain language

### Frontend / Web
| Technical | Plain |
|-----------|-------|
| Loading spinner / skeleton | Shows a placeholder while data loads, so it's not blank and alarming |
| Form validation | Warns you in real time if you mistype; won't submit |
| Pagination / infinite scroll | With lots of data, shows part at a time; scroll for more |
| Routing / route | Each screen has its own address you can link straight to |
| Dark mode | Switch to an easy-on-the-eyes dark screen |

### Backend / Data
| Technical | Plain |
|-----------|-------|
| Scheduling / cron | The system does something automatically at a set time, no button needed |
| Batch processing | Handles a whole batch at once instead of one by one |
| Access control | Different roles can see / do different things |
| Backup | Data can be recovered if something goes wrong |
| Import / export | Bring data in or take it out in bulk |

### Mobile app
| Technical | Plain |
|-----------|-------|
| Push notification | You get a reminder even when the app isn't open |
| Offline mode | Works without internet, syncs once you reconnect |
| Biometrics | Unlock with fingerprint or face, no password to type |

### CLI / tooling
| Technical | Plain |
|-----------|-------|
| Added a flag | Add an option after the command to change its behavior |
| Config file | Saves your common settings so you don't retype them |
| Exit code | Reports success or failure with a code, easy to chain next steps |

## How to describe "where it is" (by app type)

- **Web / desktop**: screen position + button label. "Top-right, the button labeled 'Export'."
- **Mobile app**: tab name + gesture. "The 'Me' tab at the bottom, scroll down to 'Security'."
- **CLI**: the command itself. "Type `xxx --export` in the terminal and it kicks in."
- **Invisible (background/automatic)**: the trigger and the result. "Runs automatically at midnight; you'll see the report in your inbox the next morning."

## Common mistakes (don't write these)
- ❌ Using a file path for "where" (`src/pages/Report.tsx`).
- ❌ Function names, package names, framework names.
- ❌ Saying "done" without saying what the user can now do.
- ❌ Selling implementation detail ("switched to useMemo" means nothing to a user).
- ❌ For background features, saying "added scheduling" without "when, and what happens".
