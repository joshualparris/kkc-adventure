KKC TEXT ADVENTURE — PROMPT 25 OF 180
==========================================
Canon Event System
==========================================


This prompt builds directly on Prompts 1 through 24.
Do not restructure, rename, or refactor anything from those prompts.
Only add to what exists.


This prompt follows the original Phase 1 plan role for Prompt 25:
add a small event system where fixed or semi-fixed events can trigger from world conditions without railroading the player.


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


Create the structural layer needed for tuition hearing, first Eolian audition framing, and later University events.


Keep the event system modest: trigger conditions, fixed vs flexible framing, and world state changes. Do not explode into branching narrative infrastructure.


═══════════════════════════════════════
SCOPE OF THIS PROMPT
═══════════════════════════════════════


This prompt covers:
  1. Add engine/eventEngine.ts
  2. Define event shape and trigger condition checks
  3. Add world-state updates on event resolution
  4. Add tests for trigger evaluation


This prompt does NOT cover:
  - Large branching story graphs
  - Cinematic scripting
  - Multi-era story management
  - Frontend event UI


═══════════════════════════════════════
NEW FILES IN THIS PROMPT
═══════════════════════════════════════


Add exactly these files:
  - src/engine/eventEngine.ts
  - tests/eventEngine.test.ts


Modify these existing files:
  - src/types/index.ts
  - src/engine/actions.ts
  - src/engine/state.ts


Do not add any other files.


═══════════════════════════════════════
IMPLEMENTATION DETAILS
═══════════════════════════════════════


Implement a compact event model with id, trigger_conditions, is_fixed, and world_state_changes. Check triggers after actions. Keep it deterministic and engine-owned.


═══════════════════════════════════════
TESTS
═══════════════════════════════════════


Add tests for unmet triggers, met triggers, single-fire events, and world-state updates.


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
  - events can trigger from world conditions
  - world_state changes are applied deterministically
  - the system is ready for concrete Phase 1 events
  - all new tests pass


==========================================
END OF PROMPT 25
==========================================
