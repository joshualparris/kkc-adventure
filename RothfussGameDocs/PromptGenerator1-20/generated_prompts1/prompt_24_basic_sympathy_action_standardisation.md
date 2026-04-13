KKC TEXT ADVENTURE — PROMPT 24 OF 180
==========================================
Basic Sympathy Action Standardisation
==========================================


This prompt builds directly on Prompts 1 through 23.
Do not restructure, rename, or refactor anything from those prompts.
Only add to what exists.


This prompt follows the original Phase 1 plan role for Prompt 24:
turn the early sympathy system into one clear MVP action path with deterministic pass/fail and consistent consequences.


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


Consolidate sympathy action handling so later prompts can build on a stable core.


Use the systems already introduced: links, warmth/body heat, materials, and simple backlash/slip outcomes. This is not full naming or advanced sympathy depth yet.


═══════════════════════════════════════
SCOPE OF THIS PROMPT
═══════════════════════════════════════


This prompt covers:
  1. Add engine/sympathyAction.ts or equivalent central module
  2. Route existing sympathy use through shared helpers
  3. Standardise consequences and result text hooks
  4. Add tests for successful, failed, and unsafe actions


This prompt does NOT cover:
  - Advanced sympathy chaining
  - Naming
  - Alchemy
  - Crafting


═══════════════════════════════════════
NEW FILES IN THIS PROMPT
═══════════════════════════════════════


Add exactly these files:
  - src/engine/sympathyAction.ts
  - tests/sympathyAction.test.ts


Modify these existing files:
  - src/engine/actions.ts
  - src/engine/sympathyEngine.ts
  - src/narration/narrationContext.ts


Do not add any other files.


═══════════════════════════════════════
IMPLEMENTATION DETAILS
═══════════════════════════════════════


Keep the logic deterministic and compact. The engine decides if the action works, what it costs, and what consequence bucket it lands in. The narration layer only expresses it.


═══════════════════════════════════════
TESTS
═══════════════════════════════════════


Add tests for a valid action, a blocked action due to missing material or unsafe condition, and a failed action with an appropriate consequence bucket.


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
  - sympathy action handling is centralised
  - the engine owns all success/failure truth
  - later prompts can build on this shared path
  - all new tests pass


==========================================
END OF PROMPT 24
==========================================
