KKC TEXT ADVENTURE — PROMPT 26 OF 180
==========================================
Tuition Hearing Event
==========================================


This prompt builds directly on Prompts 1 through 25.
Do not restructure, rename, or refactor anything from those prompts.
Only add to what exists.


This prompt follows the original Phase 1 plan role for Prompt 26:
script the tuition hearing as a canon-grounded fixed event whose framing can vary but whose institutional reality remains intact.


Current project state:
Prompts 1–20 are designed around a University-era Kvothe MVP.


Current architecture principles:
- engine owns truth
- narration never mutates state
- local deterministic path must always work
- optional Gemini path must fall back safely
- canon registry and mystery registry constrain narration
- no deep mystery resolution
- no refactors unless strictly required


Current MVP systems already planned:
- movement and location traversal
- day/time progression
- SQLite-backed player/world state
- hunger and fatigue
- tuition
- economy and currency
- inventory
- sympathy
- rumours
- Eolian / pipes
- busking at Anker’s
- reputation axes and NPC trust
- optional Gemini narration and NPC conversation
- lore guard


Current MVP focus:
- one playable era
- Kvothe only
- University + Imre slice
- grounded survival, study, work, and social consequence


═══════════════════════════════════════
HARD BANS — UNCHANGED
═══════════════════════════════════════


No Anthropic. No OpenAI. No new AI provider.
Gemini remains the only optional LLM provider in this codebase.


No web server. No frontend unless a later prompt explicitly introduces it.
No random feature sprawl.
No major refactors.
Do not invent lore.
Do not resolve mysteries.
Do not add systems outside the prompt’s stated scope.
If a referenced file does not yet exist, skip it rather than inventing around it.


═══════════════════════════════════════
ARCHITECTURE RULE — STILL ABSOLUTE
═══════════════════════════════════════


engine/* owns:
- command parsing
- movement
- access checks
- time advancement
- state mutation
- persistence
- gameplay truth


content/* owns:
- authored registries and text pools only


narration/* owns:
- prose rendering only
- prompt construction only
- fallback rendering only
- canon and mystery safety only


Narration must never mutate PlayerState.
Narration must never write to the DB.
The engine remains the source of truth.
repl.ts saves state exactly once per turn.


═══════════════════════════════════════
GOAL OF THIS PROMPT
═══════════════════════════════════════


Use the event system to make tuition feel like a real University pressure point.


Keep the hearing modest and text-centric. The player can affect approach and flavour, but the event remains institutionally bounded.


═══════════════════════════════════════
SCOPE OF THIS PROMPT
═══════════════════════════════════════


This prompt covers:
  1. Add authored tuition hearing event definition
  2. Tie it to tuition and term conditions
  3. Add outcome hooks for academic standing/social pressure
  4. Add tests for trigger and outcome application


This prompt does NOT cover:
  - Full Masters dialogue roster
  - Large branching tribunal scenes
  - Rank advancement decisions


═══════════════════════════════════════
NEW FILES IN THIS PROMPT
═══════════════════════════════════════


Add exactly these files:
  - src/content/events/tuitionHearing.ts
  - tests/tuitionHearingEvent.test.ts


Modify these existing files:
  - src/engine/eventEngine.ts
  - src/engine/tuitionEngine.ts


Do not add any other files.


═══════════════════════════════════════
IMPLEMENTATION DETAILS
═══════════════════════════════════════


Use the event system from Prompt 25. Keep the event fixed in nature but allow small flavour variations based on state. Do not over-script every Master yet.


═══════════════════════════════════════
TESTS
═══════════════════════════════════════


Add tests for correct trigger conditions and correct world/reputation changes after the event.


═══════════════════════════════════════
ARCHITECTURE REMINDERS
═══════════════════════════════════════


These rules from Prompt 1 still apply:


- narration/* never reads from or writes to the DB
- narration/* never mutates PlayerState
- engine/* owns all state changes
- repl.ts saves state exactly once per turn
- No `any` types
- No external API calls outside the optional Gemini provider
- No unused imports or files
- Add tests alongside implementation


═══════════════════════════════════════
SUCCESS CRITERIA
═══════════════════════════════════════


This prompt is complete when:
  - the tuition hearing can trigger correctly
  - the event feels institutional and grounded
  - the system remains deterministic
  - all new tests pass


==========================================
END OF PROMPT 26
==========================================
