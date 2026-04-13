KKC TEXT ADVENTURE — PROMPT 23 OF 180
==========================================
Archives Access System
==========================================


This prompt builds directly on Prompts 1 through 22.
Do not restructure, rename, or refactor anything from those prompts.
Only add to what exists.


This prompt follows the original Phase 1 plan role for Prompt 23:
formalise Archives access as requiring Re'lar rank and Lorren's approval, with proper in-world denial handling.


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


Turn the existing Archives restrictions into one clear system rather than scattered checks.


Use the canon-safe MVP rule already established: the Stacks require Re'lar and Lorren's approval. Keep denial grounded and institutional.


═══════════════════════════════════════
SCOPE OF THIS PROMPT
═══════════════════════════════════════


This prompt covers:
  1. Add engine/archivesAccess.ts
  2. Track Lorren approval in world/player state if needed
  3. Centralise access checks and denial text
  4. Add tests for rank and approval combinations


This prompt does NOT cover:
  - Full Archives browsing
  - Lorren as a full active NPC system
  - Research mechanics
  - New map areas beyond current Archives spaces


═══════════════════════════════════════
NEW FILES IN THIS PROMPT
═══════════════════════════════════════


Add exactly these files:
  - src/engine/archivesAccess.ts
  - tests/archivesAccess.test.ts


Modify these existing files:
  - src/types/index.ts
  - src/engine/movement.ts
  - src/narration/renderLocation.ts


Do not add any other files.


═══════════════════════════════════════
IMPLEMENTATION DETAILS
═══════════════════════════════════════


Create one Archives access helper that determines whether the player may enter the Stacks and returns a clean in-world failure line when blocked. Reuse existing rank and canon registry truth.


═══════════════════════════════════════
TESTS
═══════════════════════════════════════


Add tests for blocked E'lir, blocked Re'lar without approval if approval tracking exists, and successful access when all conditions are met.


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
  - Archives access logic is centralised
  - the Stacks require Re'lar and approval
  - denial messages are grounded and consistent
  - movement/rendering respect the shared access logic


==========================================
END OF PROMPT 23
==========================================
