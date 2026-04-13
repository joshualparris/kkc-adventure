KKC TEXT ADVENTURE — PROMPT 22 OF 180
==========================================
Word Travels: Pending Reputation Changes Queue
==========================================


This prompt builds directly on Prompts 1 through 21.
Do not restructure, rename, or refactor anything from those prompts.
Only add to what exists.


This prompt follows the original Phase 1 plan role for Prompt 22:
add a delayed reputation spread queue so some changes reach the wider world after 1–3 in-game days instead of instantly.


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


Make the world feel more socially believable by separating immediate internal changes from delayed wider awareness.


Keep the delayed queue narrow and mechanical. Immediate direct trust changes can remain immediate; broader public-facing reputation shifts can queue and apply later.


═══════════════════════════════════════
SCOPE OF THIS PROMPT
═══════════════════════════════════════


This prompt covers:
  1. Add engine/reputationQueue.ts
  2. Use pending_reputation_changes table or existing persistence structure
  3. Apply queued changes when day advances
  4. Add tests for delay and one-time application


This prompt does NOT cover:
  - Large social simulation
  - Dynamic rumour spread
  - NPC memory systems
  - New commands


═══════════════════════════════════════
NEW FILES IN THIS PROMPT
═══════════════════════════════════════


Add exactly these files:
  - src/engine/reputationQueue.ts
  - tests/reputationQueue.test.ts


Modify these existing files:
  - src/engine/time.ts
  - src/engine/socialEngine.ts
  - src/engine/musicEngine.ts


Do not add any other files.


═══════════════════════════════════════
IMPLEMENTATION DETAILS
═══════════════════════════════════════


Implement a small pending queue abstraction. Queue public-facing changes with apply_on_day, then apply and clear them when the current day reaches that threshold. Keep ordering deterministic. Avoid background complexity.


═══════════════════════════════════════
TESTS
═══════════════════════════════════════


Add tests for queuing a change, not applying it early, applying it on the correct day, and not applying it twice.


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
  - pending public reputation changes can be delayed
  - queued changes apply on the correct day
  - queued changes apply only once
  - existing immediate systems still work


==========================================
END OF PROMPT 22
==========================================
