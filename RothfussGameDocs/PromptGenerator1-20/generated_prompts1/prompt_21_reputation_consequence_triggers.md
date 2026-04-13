KKC TEXT ADVENTURE — PROMPT 21 OF 180
==========================================
Reputation Consequence Triggers
==========================================


This prompt builds directly on Prompts 1 through 20.
Do not restructure, rename, or refactor anything from those prompts.
Only add to what exists.


This prompt follows the original Phase 1 plan role for Prompt 21:
write reputation consequence triggers so academic and social standing start affecting reactions and access in modest, deterministic ways.


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


Introduce consequence triggers on top of the centralised reputation system without adding a huge new world-simulation layer.


Focus on small, testable consequences. Examples: low academic standing affects how certain Masters or academic-facing systems respond; very poor trust with Ambrose-related social channels can make specific interactions more hostile. Keep this modest and deterministic.


═══════════════════════════════════════
SCOPE OF THIS PROMPT
═══════════════════════════════════════


This prompt covers:
  1. Add engine/reputationConsequences.ts
  2. Define trigger helpers for academic standing and selected NPC trust bands
  3. Wire modest consequence checks into existing relevant flows
  4. Add tests for trigger thresholds and non-trigger cases


This prompt does NOT cover:
  - Delayed reputation spread
  - Dynamic NPC schedules
  - Large-scale hostility systems
  - New commands


═══════════════════════════════════════
NEW FILES IN THIS PROMPT
═══════════════════════════════════════


Add exactly these files:
  - src/engine/reputationConsequences.ts
  - tests/reputationConsequences.test.ts


Modify these existing files:
  - src/engine/actions.ts
  - src/engine/npcEngine.ts
  - src/narration/renderStatus.ts


Do not add any other files.


═══════════════════════════════════════
IMPLEMENTATION DETAILS
═══════════════════════════════════════


Implement small, deterministic consequence helpers keyed off the shared reputation engine. Keep effects local and readable. Do not build a faction framework. Use threshold bands and explicit checks. If a consequence message is needed, keep it brief and in-world.


═══════════════════════════════════════
TESTS
═══════════════════════════════════════


Add tests for low academic standing trigger, no-trigger when standing is decent, and an Ambrose-trust-based social hostility check that remains local rather than global.


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
  - reputation consequences are centralised and deterministic
  - existing systems can query consequence state without duplicating threshold logic
  - no delayed spread system is introduced yet
  - all new tests pass


==========================================
END OF PROMPT 21
==========================================
