import json
from pathlib import Path

manifest_path = Path(r"c:\Users\joshu_w0zb8cp\Documents\Project-Hub\RothfussGame\RothfussGameDocs\PromptGenerator1-20\prompt_manifest_41_100.json")
with manifest_path.open('r', encoding='utf-8') as f:
    entries = json.load(f)

# if len(entries) != 60:
#     raise SystemExit(f'Expected 60 entries, found {len(entries)}')

new_entries = [
    {
        "number": 61,
        "title": "Tuition Payment and Due Ledger",
        "phase_role": "Add a deterministic tuition payment action and due-date ledger so the player can settle obligations explicitly.",
        "goal": "Allow the player to pay tuition through a clear in-game command and see outstanding balances.",
        "goal_detail": "Track tuition due dates and amounts as ledger entries in state, then expose a payment action that reduces debt predictably. Keep the flow narrow and safe for the current University slice.",
        "scope": [
            "Add engine/tuitionPayment.ts",
            "Track tuition obligations as due_date ledger entries in world_state",
            "Expose a pay tuition command in the parser",
            "Add tests for payment success, insufficient funds, and due ledger updates"
        ],
        "out_of_scope": [
            "Loans, interest, or credit systems",
            "Open-ended financial planning",
            "Any banking or investment mechanics"
        ],
        "new_files": [
            "src/engine/tuitionPayment.ts",
            "tests/tuitionPayment.test.ts"
        ],
        "modified_files": [
            "src/engine/actions.ts",
            "src/engine/tuitionEngine.ts",
            "src/engine/state.ts",
            "src/narration/renderStatus.ts"
        ],
        "implementation_sections": "Implement a tuition payment action that checks available currency, applies payment to the nearest due tuition entry, and updates world_state. Keep the logic deterministic and avoid any financial forecasting.",
        "tests": "Verify the player can pay tuition when they have enough currency, that payment reduces the due amount and removes completed ledger entries, and that payment is rejected when funds are insufficient.",
        "success_criteria": [
            "The player can explicitly pay tuition",
            "Due amounts are tracked in state",
            "Payment results are deterministic",
            "All new tests pass"
        ]
    },
    {
        "number": 62,
        "title": "Academic Study Action",
        "phase_role": "Introduce a narrow study action that increases academic standing based on deterministic effort rather than random skill checks.",
        "goal": "Make studying a meaningful, trackable action that improves the player's academic condition over time.",
        "goal_detail": "Add a study command that records effort and boosts academic standing in a predictable way. Keep it limited to the current University systems and avoid broad RPG-style studies or stats.",
        "scope": [
            "Add engine/studyAction.ts",
            "Track study effort using a simple numeric state field",
            "Apply study effects to academic standing or attendance outcomes",
            "Add tests for study success and diminishing returns"
        ],
        "out_of_scope": [
            "Complex learning trees or skill progressions",
            "Open-ended mini-games",
            "Multiple subject systems"
        ],
        "new_files": [
            "src/engine/studyAction.ts",
            "tests/studyAction.test.ts"
        ],
        "modified_files": [
            "src/engine/actions.ts",
            "src/engine/state.ts",
            "src/engine/attendance.ts",
            "src/narration/renderStatus.ts"
        ],
        "implementation_sections": "Implement a study helper that increments a study_score and applies that score to academic standing or exam readiness. Keep the effect deterministic and additive.",
        "tests": "Verify the study action increases the study score, that repeated study has predictable effects, and that the score influences related academic outcomes.",
        "success_criteria": [
            "A study action exists",
            "It improves academic standing predictably",
            "The behaviour remains narrow and deterministic",
            "All new tests pass"
        ]
    },
    {
        "number": 63,
        "title": "Busking Reward Scaling",
        "phase_role": "Make busking income depend on performance readiness and mood, giving musical practice tangible rewards.",
        "goal": "Connect the player's music preparation to earnings in a narrow, deterministic busking flow.",
        "goal_detail": "Use the existing performance readiness state to adjust busking reward outcomes. Keep the system small and appropriate for the University slice.",
        "scope": [
            "Add engine/busking.ts",
            "Use performance readiness and current location to compute busking reward",
            "Wire busking into the existing actions parser",
            "Add tests for reward scaling and blocked conditions"
        ],
        "out_of_scope": [
            "Full performance mechanics or open stage simulation",
            "Large reputation-driven concert systems",
            "Non-deterministic income outcomes"
        ],
        "new_files": [
            "src/engine/busking.ts",
            "tests/busking.test.ts"
        ],
        "modified_files": [
            "src/engine/actions.ts",
            "src/engine/musicPractice.ts",
            "src/narration/renderStatus.ts"
        ],
        "implementation_sections": "Implement a busking helper that computes a fixed reward based on readiness state and other simple modifiers. Ensure the reward is deterministic and that readiness is consumed or preserved predictably.",
        "tests": "Verify busking pays more when readiness is higher, that the busking action is available only at suitable locations, and that the reward calculation is deterministic.",
        "success_criteria": [
            "Busking income depends on readiness",
            "The action is deterministic",
            "No broad new performance system is introduced",
            "All new tests pass"
        ]
    },
    {
        "number": 64,
        "title": "Rumour Ripple Integration",
        "phase_role": "Connect the reputation ripple system to the rumour pool so world-state changes can be reflected in gossip.",
        "goal": "Make reputation changes influence the rumour system in a small, deterministic way.",
        "goal_detail": "When the reputation ripple resolves, publish a related rumour or public reaction note. Keep the integration focused and avoid full social networking.",
        "scope": [
            "Add engine/rumourRipple.ts",
            "Publish a rumour when a delayed reputation change resolves",
            "Ensure the rumour remains canon-safe and deterministic",
            "Add tests for rumour publication timing"
        ],
        "out_of_scope": [
            "Wide rumour networks or reputation markets",
            "Open-ended multiplayer-style gossip systems",
            "Non-deterministic rumour generation"
        ],
        "new_files": [
            "src/engine/rumourRipple.ts",
            "tests/rumourRipple.test.ts"
        ],
        "modified_files": [
            "src/engine/reputationRipple.ts",
            "src/engine/rumourPool.ts",
            "src/engine/time.ts"
        ],
        "implementation_sections": "Implement a helper that turns a resolved reputation queue item into one fixed rumour note. Keep the published rumour narrow, canned, and limited to the current MVP cast.",
        "tests": "Verify the rumour is published only when the reputation change resolves and that it reflects the correct reputation band.",
        "success_criteria": [
            "Reputation ripple publishes a rumour",
            "The integration is deterministic",
            "The rumour stays within MVP scope",
            "All new tests pass"
        ]
    },
    {
        "number": 65,
        "title": "Campus Availability Schedule",
        "phase_role": "Add a narrow availability schedule for key NPCs and activities based on the in-game day/time.",
        "goal": "Make frequent University actions feel more grounded by limiting them to plausible windows and NPC availability.",
        "goal_detail": "Define availability for one or two NPCs or actions and use the current schedule engine to block or allow them. Keep the feature simple and deterministic.",
        "scope": [
            "Extend engine/schedule.ts with NPC availability rules",
            "Define availability windows for one or two core NPCs",
            "Prevent actions when the NPC is unavailable",
            "Add tests for availability behaviour"
        ],
        "out_of_scope": [
            "Large NPC scheduling systems",
            "Full campus timetable management",
            "Dynamic availability based on many unrelated conditions"
        ],
        "new_files": [
            "tests/availabilitySchedule.test.ts"
        ],
        "modified_files": [
            "src/engine/schedule.ts",
            "src/engine/npcEngine.ts",
            "src/narration/renderLocation.ts"
        ],
        "implementation_sections": "Implement a small availability helper in schedule.ts that returns whether an NPC or activity is available in the current time slice. Use it in action resolution to block unavailable cases.",
        "tests": "Verify a sample NPC is only available during the defined window and that actions fail cleanly when it is not.",
        "success_criteria": [
            "NPC availability exists",
            "The system is deterministic",
            "The scope remains narrow",
            "All new tests pass"
        ]
    },
    {
        "number": 66,
        "title": "Research Notes and Journal Cross-Reference",
        "phase_role": "Add a simple research note entry that records a Library visit and cross-references it in the player journal.",
        "goal": "Give Stacks access a concrete reward by recording research notes the player can review later.",
        "goal_detail": "When research access succeeds, add a short note to world_state and expose it through the journal or status. Keep the entry factual and narrow.",
        "scope": [
            "Extend engine/stacksAccess.ts with note recording",
            "Record a research note in world_state",
            "Expose the note through the in-world journal",
            "Add tests for note creation and display"
        ],
        "out_of_scope": [
            "Full research or book reading systems",
            "Large archives browsing",
            "Complex note-taking interfaces"
        ],
        "new_files": [
            "tests/researchNotes.test.ts"
        ],
        "modified_files": [
            "src/engine/stacksAccess.ts",
            "src/engine/journal.ts",
            "src/engine/state.ts",
            "src/narration/renderStatus.ts"
        ],
        "implementation_sections": "When Stacks access succeeds, append a canonical research note to the world_state journal. Ensure the note is concise and only records the fact of the visit and the topic.",
        "tests": "Verify a research note is stored on successful access and that it appears in the journal output.",
        "success_criteria": [
            "Research notes are recorded",
            "The journal displays them",
            "The behaviour stays narrow",
            "All new tests pass"
        ]
    },
    {
        "number": 67,
        "title": "NPC Schedule and Presence",
        "phase_role": "Add a small NPC presence tracker so location descriptions can mention which key NPCs are currently present.",
        "goal": "Make the University world feel more alive by identifying which important NPCs are in the current space.",
        "goal_detail": "Use existing time and location state to determine presence for one or two MVP NPCs and render that in the location summary. Keep the tracker lightweight and deterministic.",
        "scope": [
            "Add engine/npcPresence.ts",
            "Track presence based on time/location rules",
            "Render presence in location summaries",
            "Add tests for presence tracking"
        ],
        "out_of_scope": [
            "Large NPC scheduling or patrol systems",
            "Open-ended NPC pathfinding",
            "Dynamic crowd simulation"
        ],
        "new_files": [
            "src/engine/npcPresence.ts",
            "tests/npcPresence.test.ts"
        ],
        "modified_files": [
            "src/engine/movement.ts",
            "src/narration/renderLocation.ts"
        ],
        "implementation_sections": "Implement a small presence helper returning which key NPCs are in the current location at the current time. Use that helper in location rendering.",
        "tests": "Verify presence changes when the time window passes and that location descriptions reflect the current NPCs.",
        "success_criteria": [
            "NPC presence is tracked",
            "Location rendering uses it",
            "The system is deterministic",
            "All new tests pass"
        ]
    },
    {
        "number": 68,
        "title": "Morning Pass Status Summary",
        "phase_role": "Add a concise morning pass summary that surfaces current obligations, status, and salient world-state notes.",
        "goal": "Help the player start each day with a clear view of what matters in the current University slice.",
        "goal_detail": "When the morning pass runs, include a short status summary note listing overdue obligations, upcoming events, and key conditions. Keep the summary factual and brief.",
        "scope": [
            "Extend src/engine/time.ts morning pass output",
            "Add a summary helper for current obligations and world-state notes",
            "Ensure the summary is deterministic and concise",
            "Add tests for summary content"
        ],
        "out_of_scope": [
            "A full tutorial or onboarding system",
            "Meta-game checklist UIs",
            "Open-ended advice generation"
        ],
        "new_files": [
            "tests/morningSummary.test.ts"
        ],
        "modified_files": [
            "src/engine/time.ts",
            "src/narration/localNarrator.ts",
            "src/narration/renderStatus.ts"
        ],
        "implementation_sections": "Implement a morning summary helper that collects due dates, event status, and key journal notes into a fixed paragraph. Render it during the morning pass.",
        "tests": "Verify the summary includes overdue tuition, an upcoming audition, and any new journal note without being verbose.",
        "success_criteria": [
            "A morning summary appears",
            "It is concise and deterministic",
            "It surfaces the right obligations",
            "All new tests pass"
        ]
    },
    {
        "number": 69,
        "title": "Exam Preparation and Assessment",
        "phase_role": "Add a narrow exam event that assesses study, attendance, and readiness to produce a deterministic outcome.",
        "goal": "Introduce a small academic assessment event that rewards preparation and attendance in a predictable way.",
        "goal_detail": "Define a single exam event with a fixed pass/fail outcome based on prior study score, attendance, and readiness. Keep the event small and avoid any broader grading system.",
        "scope": [
            "Add engine/examEvent.ts",
            "Define pass/fail conditions based on study and attendance",
            "Render a concise exam result and record it in world_state",
            "Add tests for exam outcomes"
        ],
        "out_of_scope": [
            "Detailed gradebook mechanics",
            "Open-ended exam question generation",
            "Multiple subject exams"
        ],
        "new_files": [
            "src/engine/examEvent.ts",
            "tests/examEvent.test.ts"
        ],
        "modified_files": [
            "src/engine/eventEngine.ts",
            "src/engine/studyAction.ts",
            "src/engine/attendance.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement an exam event with a deterministic evaluation function that considers study_score, attendance flags, and current readiness. Store the result for later reference.",
        "tests": "Verify a well-prepared player passes, a poorly prepared player fails, and the event result is stored correctly.",
        "success_criteria": [
            "An exam event exists",
            "It evaluates deterministically",
            "The player can see the result",
            "All new tests pass"
        ]
    },
    {
        "number": 70,
        "title": "Academic Loop End-of-Day Review",
        "phase_role": "Add a deterministic end-of-day review that summarises the player's key University progress and obligations.",
        "goal": "Close each day with a clear, narrow review that reinforces the current academic flow.",
        "goal_detail": "After the evening pass, render a short review paragraph summarising grades, notes, debt, and upcoming obligations. Keep it factual and limited to the current systems.",
        "scope": [
            "Add engine/endOfDayReview.ts",
            "Hook the review into the evening pass",
            "Include fixed summaries for exam results and tuition status",
            "Add tests for review output"
        ],
        "out_of_scope": [
            "Open-ended journal entries",
            "Meta-game score screens",
            "Large narrative epilogues"
        ],
        "new_files": [
            "src/engine/endOfDayReview.ts",
            "tests/endOfDayReview.test.ts"
        ],
        "modified_files": [
            "src/engine/time.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement a review helper that collects key state markers and renders them at the end of the day. Ensure the review is readable and deterministic.",
        "tests": "Verify the review includes the exam result, tuition status, and current journal note in the expected format.",
        "success_criteria": [
            "An end-of-day review exists",
            "It is concise and deterministic",
            "It reflects the current academic loop",
            "All new tests pass"
        ]
    },
    {
        "number": 71,
        "title": "Save/Load Version and Migration Support",
        "phase_role": "Add a narrow save version marker so future state changes can be migrated safely.",
        "goal": "Make the save format future-proof by recording a version identifier and supporting one deterministic migration path.",
        "goal_detail": "Store a simple save_version field alongside player_state and world_state, and implement one migration helper for the current prompt additions. Keep the feature narrowly scoped.",
        "scope": [
            "Add engine/saveVersion.ts",
            "Record save_version in saved state",
            "Implement one migration for newly introduced fields",
            "Add tests for save loading with version checks"
        ],
        "out_of_scope": [
            "Full versioned migration framework",
            "Multiple incompatible version branches",
            "Automatic schema discovery"
        ],
        "new_files": [
            "src/engine/saveVersion.ts",
            "tests/saveVersion.test.ts"
        ],
        "modified_files": [
            "src/engine/state.ts",
            "src/engine/db/connection.ts",
            "src/engine/time.ts"
        ],
        "implementation_sections": "Implement a save version field and a migration helper that upgrades older save state to include the new tuition and journal fields. Keep the logic simple and explicit.",
        "tests": "Verify a state record missing the new fields can be loaded and upgraded deterministically.",
        "success_criteria": [
            "Save version is recorded",
            "One migration path exists",
            "Save loading remains deterministic",
            "All new tests pass"
        ]
    },
    {
        "number": 72,
        "title": "Help Command with Obligations",
        "phase_role": "Enhance the in-world help command to include the player's current obligations and simple schedule hints.",
        "goal": "Make the help output more useful by surfacing relevant upcoming actions without breaking immersion.",
        "goal_detail": "Add a small obligation summary to the help text based on due dates, exam status, and active journal entries. Keep the command output fixed and narrative.",
        "scope": [
            "Extend engine/helpCommand.ts output",
            "Use world_state obligations and journal entries in the help text",
            "Keep the text short and in-world",
            "Add tests for obligation-aware help output"
        ],
        "out_of_scope": [
            "Full quest log systems",
            "Meta-game checklist UI",
            "Open-ended advice generation"
        ],
        "new_files": [
            "tests/helpCommandObligations.test.ts"
        ],
        "modified_files": [
            "src/engine/helpCommand.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Append a fixed obligation summary paragraph to help responses when there are due obligations or upcoming exams. Keep the phrasing consistent with in-world advice.",
        "tests": "Verify the help text includes a tuition reminder or upcoming exam notice when applicable.",
        "success_criteria": [
            "Help command surfaces obligations",
            "The output stays immersive",
            "The behaviour is deterministic",
            "All new tests pass"
        ]
    },
    {
        "number": 73,
        "title": "NPC Response Template Standardisation",
        "phase_role": "Standardise a small set of NPC response templates so replies are consistent and easy to maintain.",
        "goal": "Make NPC reactions more predictable and reduce hardcoded response duplication.",
        "goal_detail": "Move one or two common NPC response patterns into shared templates. Use them for current reputation and attendance replies only.",
        "scope": [
            "Add engine/npcResponseTemplates.ts",
            "Replace duplicate NPC reply strings with template helpers",
            "Add tests for template selection",
            "Keep the scope limited to the current MVP NPC set"
        ],
        "out_of_scope": [
            "Full dialogue system refactors",
            "Open-ended narrative templating",
            "Large text generation pipelines"
        ],
        "new_files": [
            "src/engine/npcResponseTemplates.ts",
            "tests/npcResponseTemplates.test.ts"
        ],
        "modified_files": [
            "src/engine/npcEngine.ts",
            "src/narration/renderLocation.ts"
        ],
        "implementation_sections": "Implement a set of fixed response templates and use them for the current NPC reaction cases. Keep the templates simple and deterministic.",
        "tests": "Verify the correct template is selected for low, neutral, and high reputation replies.",
        "success_criteria": [
            "NPC replies use shared templates",
            "Behaviour is deterministic",
            "Text remains narrow and consistent",
            "All new tests pass"
        ]
    },
    {
        "number": 74,
        "title": "Peer Request Scene",
        "phase_role": "Add a narrow student request scene from Simmon or Wilem that reflects prior progress and offers a small, fixed choice.",
        "goal": "Introduce one small social beat that makes the University cast feel reactive without branching into a quest system.",
        "goal_detail": "Trigger a short request scene dependent on a recent event or world_state note. Keep the interaction fixed and the outcome deterministic.",
        "scope": [
            "Add engine/peerRequest.ts",
            "Trigger the scene once after a relevant completed event",
            "Record the response outcome in world_state",
            "Add tests for each scene variant"
        ],
        "out_of_scope": [
            "Full companion relationship arcs",
            "Open-ended choice trees",
            "Dynamic NPC quest systems"
        ],
        "new_files": [
            "src/engine/peerRequest.ts",
            "tests/peerRequest.test.ts"
        ],
        "modified_files": [
            "src/engine/eventEngine.ts",
            "src/engine/state.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement one fixed request scene with deterministic text variants based on a prior event result. Keep the scene short and limited to one NPC.",
        "tests": "Verify the scene triggers after the right event and that the text variant matches the prior world_state.",
        "success_criteria": [
            "A peer request scene exists",
            "It is based on prior progress",
            "The result is deterministic",
            "All new tests pass"
        ]
    },
    {
        "number": 75,
        "title": "Fixed Campus Errand Job",
        "phase_role": "Add one small errand job separate from busking so the player has another predictable income source.",
        "goal": "Provide a narrow, deterministic campus job action that pays a fixed reward for completing a simple task.",
        "goal_detail": "Implement one fixed errand such as delivering a note or fetching a book. Keep the job simple, with a fixed reward and clear preconditions.",
        "scope": [
            "Add engine/errandJob.ts",
            "Define the task, preconditions, and reward",
            "Wire it into command parsing",
            "Add tests for success and blocking conditions"
        ],
        "out_of_scope": [
            "Large job markets",
            "Open-ended task generation",
            "Complex item or inventory puzzles"
        ],
        "new_files": [
            "src/engine/errandJob.ts",
            "tests/errandJob.test.ts"
        ],
        "modified_files": [
            "src/engine/actions.ts",
            "src/engine/state.ts",
            "src/narration/renderStatus.ts"
        ],
        "implementation_sections": "Implement the errand job action with deterministic reward and conditions. The task should feel like a small University task, not a full job system.",
        "tests": "Verify the action succeeds when conditions are met, that the reward is granted, and that the action is blocked otherwise.",
        "success_criteria": [
            "A fixed errand job exists",
            "It pays a predictable reward",
            "The scope stays narrow",
            "All new tests pass"
        ]
    },
    {
        "number": 76,
        "title": "Reputation Recovery and Forgiveness",
        "phase_role": "Add a narrow mechanic for recovering reputation after a poor outcome without creating broad reputation farming.",
        "goal": "Allow the player to recover from a low-reputation state through deterministic effort.",
        "goal_detail": "Implement one recovery action such as apologising, studying, or performing a small service. Keep the recovery modest and deterministic.",
        "scope": [
            "Add engine/reputationRecovery.ts",
            "Define the recovery action and its effect on reputation bands",
            "Wire it into existing action parsing",
            "Add tests for recovery conditions"
        ],
        "out_of_scope": [
            "Large reputation farming systems",
            "Open-ended popularity mechanics",
            "Dynamic social economy"
        ],
        "new_files": [
            "src/engine/reputationRecovery.ts",
            "tests/reputationRecovery.test.ts"
        ],
        "modified_files": [
            "src/engine/actions.ts",
            "src/engine/npcReactionRules.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement one recovery action that shifts reputation bands by a fixed amount when performed in the right context. Keep the effect small and deterministic.",
        "tests": "Verify the recovery action increases reputation when allowed and that it is rejected in inappropriate contexts.",
        "success_criteria": [
            "Reputation recovery exists",
            "It is deterministic and modest",
            "No broad social system is added",
            "All new tests pass"
        ]
    },
    {
        "number": 77,
        "title": "Canon-Safe Narrative Guard",
        "phase_role": "Add a small canon-safe guard specifically for NPC names and locations in narration.",
        "goal": "Prevent obvious non-canon names or locations from appearing in generated text.",
        "goal_detail": "Implement one narrow guard that checks narration fragments against a known safe set for the MVP cast and University locations. Keep the guard explicit and deterministic.",
        "scope": [
            "Extend engine/canonGuard.ts",
            "Add a canon-safe name/location validator",
            "Use it in narration generation","Add tests for canonical and forbidden text"
        ],
        "out_of_scope": [
            "Broad hallucination detection",
            "Large external lore validation",
            "New lore invention"
        ],
        "new_files": [
            "tests/canonSafety.test.ts"
        ],
        "modified_files": [
            "src/engine/canonGuard.ts",
            "src/narration/localNarrator.ts",
            "src/narration/renderLocation.ts"
        ],
        "implementation_sections": "Implement a validator for a small set of allowed names and locations and reject output fragments that violate the list. Keep the list narrow and tied to known MVP content.",
        "tests": "Verify the guard rejects a known forbidden phrase and allows valid University names.",
        "success_criteria": [
            "A canon-safe narrative guard exists",
            "It checks names and locations",
            "It remains narrow and explicit",
            "All new tests pass"
        ]
    },
    {
        "number": 78,
        "title": "Alternate Busking Outcome Path",
        "phase_role": "Add a second deterministic outcome for busking that depends on location and mood.",
        "goal": "Make busking feel less repetitive by adding one alternate reward path.",
        "goal_detail": "When busking at a particular location or under a specific readiness band, trigger a different fixed reward or narrative note. Keep the branch simple.",
        "scope": [
            "Extend engine/busking.ts with alternate outcome logic",
            "Add one additional busking narrative branch",
            "Keep rewards deterministic and narrow",
            "Add tests for both outcome paths"
        ],
        "out_of_scope": [
            "Open-ended performance branching",
            "Complex mood or reputation systems",
            "Large multiple-stage performance mechanics"
        ],
        "new_files": [
            "tests/buskingOutcomes.test.ts"
        ],
        "modified_files": [
            "src/engine/busking.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement a second fixed busking outcome based on a narrow condition such as location or readiness level. Render a distinct narrative line for the alternate path.",
        "tests": "Verify both busking paths are reachable under the right conditions and that the selected narrative is deterministic.",
        "success_criteria": [
            "An alternate busking path exists",
            "It is deterministic",
            "The branch is narrow",
            "All new tests pass"
        ]
    },
    {
        "number": 79,
        "title": "Study Help Request Command",
        "phase_role": "Add a narrow command that lets the player request help with study or preparation in-world.",
        "goal": "Provide a small in-world help action that supports the new study and exam systems.",
        "goal_detail": "Implement a fixed command such as ask for study help that produces a short, deterministic response and optionally modifies readiness or academic standing slightly.",
        "scope": [
            "Add engine/helpStudy.ts",
            "Wire the command into the parser",
            "Keep the response fixed and narrative",
            "Add tests for command behaviour"
        ],
        "out_of_scope": [
            "Full tutoring systems",
            "Open-ended learning interactions",
            "Complex social benefit calculations"
        ],
        "new_files": [
            "src/engine/helpStudy.ts",
            "tests/helpStudy.test.ts"
        ],
        "modified_files": [
            "src/engine/actions.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement one fixed help study command that returns a short narrative response and applies a small deterministic bonus to readiness or study score.",
        "tests": "Verify the command is recognized, returns the expected text, and applies the correct state change when available.",
        "success_criteria": [
            "A study help command exists",
            "The response is immersive",
            "The bonus is deterministic",
            "All new tests pass"
        ]
    },
    {
        "number": 80,
        "title": "Developer State Dump Command",
        "phase_role": "Add a narrow developer-facing command that dumps critical state for debugging without changing gameplay.",
        "goal": "Help developers inspect player and world state deterministically from the REPL.",
        "goal_detail": "Add a fixed command that prints a compact JSON-like snapshot of key state fields. Keep it hidden from normal gameplay and not part of production decision logic.",
        "scope": [
            "Add engine/debugDump.ts",
            "Wire a debug command into the parser",
            "Limit output to key deterministic fields",
            "Add tests for the command output"
        ],
        "out_of_scope": [
            "Full debug consoles",
            "Gameplay-affecting debug features",
            "Non-deterministic state exports"
        ],
        "new_files": [
            "src/engine/debugDump.ts",
            "tests/debugDump.test.ts"
        ],
        "modified_files": [
            "src/engine/actions.ts",
            "src/repl.ts"
        ],
        "implementation_sections": "Implement a debug dump helper that prints the selected state fields in a compact, deterministic format. Ensure it is only reachable through a developer command.",
        "tests": "Verify the debug dump command produces the expected state snapshot text.",
        "success_criteria": [
            "A developer state dump command exists",
            "The output is deterministic",
            "It does not affect gameplay",
            "All new tests pass"
        ]
    },
    {
        "number": 81,
        "title": "Debt and Tuition Repayment Tracker",
        "phase_role": "Add a narrow repayment tracker that records outstanding debt and repayment progress over multiple turns.",
        "goal": "Make tuition debt feel persistent while keeping repayment predictable.",
        "goal_detail": "Track remaining debt after payments and show progress in the journal or status. Keep the tracker simple and tied only to tuition obligations.",
        "scope": [
            "Extend engine/tuitionPayment.ts with remaining debt tracking",
            "Expose repayment progress in status or journal",
            "Keep the data deterministic and explicit",
            "Add tests for debt tracking"
        ],
        "out_of_scope": [
            "Open-ended credit systems",
            "Interest or compound debt",
            "Large financial planning tools"
        ],
        "new_files": [
            "tests/debtTracker.test.ts"
        ],
        "modified_files": [
            "src/engine/tuitionPayment.ts",
            "src/engine/state.ts",
            "src/narration/renderStatus.ts"
        ],
        "implementation_sections": "Implement a remaining debt field and update it when tuition payments occur. Display the current debt clearly in status output.",
        "tests": "Verify the debt decreases after payment and that the status output shows the correct remaining amount.",
        "success_criteria": [
            "Debt is tracked",
            "Repayment progress is visible",
            "The system stays deterministic",
            "All new tests pass"
        ]
    },
    {
        "number": 82,
        "title": "Small Academic Reputation Event",
        "phase_role": "Add one narrow event where academic performance affects a key NPC's opinion.",
        "goal": "Give academic activity a small social consequence in the MVP world.",
        "goal_detail": "When the player performs well or poorly academically, trigger a fixed reaction from one authority figure. Keep the event deterministic and focused.",
        "scope": [
            "Add engine/academicReputationEvent.ts",
            "Trigger the event after exam or study outcomes",
            "Record the response in world_state",
            "Add tests for event triggering"
        ],
        "out_of_scope": [
            "Large reputation systems",
            "Dynamic reputation markets",
            "Open-ended NPC opinion tracking"
        ],
        "new_files": [
            "src/engine/academicReputationEvent.ts",
            "tests/academicReputationEvent.test.ts"
        ],
        "modified_files": [
            "src/engine/eventEngine.ts",
            "src/engine/examEvent.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement a small event that runs after an academic result and produces a fixed authority reaction. Keep the effect modest and tied to a single NPC.",
        "tests": "Verify the event only triggers after the academic outcome and that the reaction matches the performance.",
        "success_criteria": [
            "An academic reputation event exists",
            "It is deterministic and modest",
            "It ties to a single NPC reaction",
            "All new tests pass"
        ]
    },
    {
        "number": 83,
        "title": "Term Deadline Alert System",
        "phase_role": "Add narrow alerts for upcoming term deadlines so the player can plan around exam and tuition due dates.",
        "goal": "Help the player stay aware of pending academic obligations with brief alerts.",
        "goal_detail": "When a due date is approaching, render a fixed alert during the morning pass. Keep the alert limited to the current term and obligations.",
        "scope": [
            "Add engine/deadlineAlerts.ts",
            "Define alert thresholds for tuition and exams",
            "Render alerts during morning pass",
            "Add tests for alert timing"
        ],
        "out_of_scope": [
            "Open-ended planner systems",
            "Large calendar UIs",
            "Multiple-term management"
        ],
        "new_files": [
            "src/engine/deadlineAlerts.ts",
            "tests/deadlineAlerts.test.ts"
        ],
        "modified_files": [
            "src/engine/time.ts",
            "src/narration/localNarrator.ts",
            "src/narration/renderStatus.ts"
        ],
        "implementation_sections": "Implement a deadline alert helper that checks upcoming due dates and adds a fixed reminder line to the morning pass.",
        "tests": "Verify alerts appear the day before a due date and do not appear too early or after the deadline.",
        "success_criteria": [
            "Deadline alerts exist",
            "They are deterministic",
            "They stay within the current term model",
            "All new tests pass"
        ]
    },
    {
        "number": 84,
        "title": "Master Approval Event",
        "phase_role": "Add one small approval event that depends on a master or authority figure saying yes before a special action can occur.",
        "goal": "Make one special action feel gated by University authority in a narrow, deterministic way.",
        "goal_detail": "Implement one event where the player must obtain approval before pursuing a research or performance action. Keep it binary and based on current state.",
        "scope": [
            "Add engine/approvalEvent.ts",
            "Require approval for one special action",
            "Record approval state in world_state",
            "Add tests for approval denial and success"
        ],
        "out_of_scope": [
            "Large politics systems",
            "Open-ended persuasion mechanics",
            "Multiple approval chains"
        ],
        "new_files": [
            "src/engine/approvalEvent.ts",
            "tests/approvalEvent.test.ts"
        ],
        "modified_files": [
            "src/engine/state.ts",
            "src/engine/eventEngine.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement one approval requirement and store its result in world_state. Use the approval result to gate the relevant special action.",
        "tests": "Verify the action is blocked when approval is absent and allowed when approval is present.",
        "success_criteria": [
            "A master approval event exists",
            "It is binary and deterministic",
            "It gates one special action",
            "All new tests pass"
        ]
    },
    {
        "number": 85,
        "title": "Narrow Lore Clue Entry",
        "phase_role": "Add one small lore-safe clue note that is fact-based and avoids new canon invention.",
        "goal": "Introduce a subtle, narrow clue to the world that feels grounded in the University slice.",
        "goal_detail": "Record one fixed lore clue in world_state and expose it in the journal or a research note. Keep it explicit, small, and canon-safe.",
        "scope": [
            "Add engine/loreClue.ts",
            "Record a single clue note in world_state",
            "Expose the note through journal or research summary",
            "Add tests for the clue note"
        ],
        "out_of_scope": [
            "New major lore or mysteries",
            "Open-ended clue networks",
            "Large speculative content"
        ],
        "new_files": [
            "src/engine/loreClue.ts",
            "tests/loreClue.test.ts"
        ],
        "modified_files": [
            "src/engine/journal.ts",
            "src/engine/state.ts",
            "src/narration/renderStatus.ts"
        ],
        "implementation_sections": "Implement a single fixed lore clue record and render it as a note. Keep the text factual and consistent with the University setting.",
        "tests": "Verify the clue appears after the triggering condition and is stored correctly.",
        "success_criteria": [
            "A lore clue note exists",
            "It is canon-safe",
            "It remains narrow and explicit",
            "All new tests pass"
        ]
    },
    {
        "number": 86,
        "title": "Missed Deadline Follow-Up",
        "phase_role": "Add a narrow follow-up consequence for missing an important obligation such as tuition or an exam.",
        "goal": "Make missed deadlines produce a small, visible response instead of disappearing from the game.",
        "goal_detail": "When a term obligation is missed, render a deterministic follow-up note and apply a modest state consequence. Keep the effect modest and clear.",
        "scope": [
            "Extend engine/missedEventChecks.ts",
            "Record missed-deadline follow-up notes",
            "Render the follow-up in the morning pass",
            "Add tests for the follow-up behaviour"
        ],
        "out_of_scope": [
            "Harsh failure states",
            "Large branching story consequences",
            "Open-ended punishment systems"
        ],
        "new_files": [
            "tests/missedDeadlineFollowUp.test.ts"
        ],
        "modified_files": [
            "src/engine/missedEventChecks.ts",
            "src/engine/time.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Add a follow-up note when a deadline is missed and apply one small predetermined penalty. Ensure the note is rendered at the next morning pass.",
        "tests": "Verify the follow-up appears after a missed deadline and that the penalty is applied once.",
        "success_criteria": [
            "Missed deadlines have visible follow-up",
            "The behaviour remains narrow",
            "The penalty is modest and deterministic",
            "All new tests pass"
        ]
    },
    {
        "number": 87,
        "title": "Performance Critique and Reward Adjustment",
        "phase_role": "Add a narrow critique output after performances that adjusts future reward expectations.",
        "goal": "Make performance outcomes more informative by giving one fixed critique and adjusting the player's readiness or reward forecast.",
        "goal_detail": "After a busking or audition event, produce a short critique line and optionally adjust a performance readiness or expectation field. Keep the adjustment small and deterministic.",
        "scope": [
            "Extend engine/busking.ts or engine/auditionResults.ts",
            "Add one fixed critique output for performance outcomes",
            "Adjust readiness or forecast state deterministically",
            "Add tests for critique generation"
        ],
        "out_of_scope": [
            "Open-ended critic systems",
            "Large performance review mechanics",
            "Non-deterministic critique text"
        ],
        "new_files": [
            "tests/performanceCritique.test.ts"
        ],
        "modified_files": [
            "src/engine/busking.ts",
            "src/engine/auditionResults.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement one fixed critique line for a performance event and apply a small deterministic state adjustment. Keep the critique short and grounded.",
        "tests": "Verify the critique appears and that the state adjustment is applied correctly.",
        "success_criteria": [
            "A performance critique exists",
            "It is deterministic and narrow",
            "It adjusts future reward expectations",
            "All new tests pass"
        ]
    },
    {
        "number": 88,
        "title": "Peer Gossip Beat",
        "phase_role": "Add one narrow student gossip beat that reflects the player's recent actions in a compact, deterministic way.",
        "goal": "Ground the player's social world with a small, predictable gossip reaction.",
        "goal_detail": "After a relevant event, render a short gossip line from another student that mirrors the outcome in a limited way. Keep the beat small and fixed.",
        "scope": [
            "Add engine/peerGossip.ts",
            "Trigger the gossip after one event or state change",
            "Render it during the next appropriate pass",
            "Add tests for gossip timing"
        ],
        "out_of_scope": [
            "Large social networks",
            "Open-ended gossip mechanics",
            "Non-deterministic dialogue"
        ],
        "new_files": [
            "src/engine/peerGossip.ts",
            "tests/peerGossip.test.ts"
        ],
        "modified_files": [
            "src/engine/time.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement a fixed gossip trigger that creates one line of student commentary after a relevant event. Ensure the line is deterministic and narrow.",
        "tests": "Verify the gossip appears at the right time and reflects the prior event.",
        "success_criteria": [
            "A gossip beat exists",
            "It is tied to prior progress",
            "It remains narrow and deterministic",
            "All new tests pass"
        ]
    },
    {
        "number": 89,
        "title": "Exam Result Summary",
        "phase_role": "Add a concise exam result summary that appears after an assessment event.",
        "goal": "Make the result of academic exams explicit and reviewable.",
        "goal_detail": "After the exam event, render one fixed summary line describing the outcome and record the result in state. Keep the summary short and factual.",
        "scope": [
            "Extend engine/examEvent.ts with summary recording",
            "Render the summary after the exam",
            "Expose the result in journal or status",
            "Add tests for summary output"
        ],
        "out_of_scope": [
            "Open-ended result narratives",
            "Detailed grading transcripts",
            "Large academic reports"
        ],
        "new_files": [
            "tests/examSummary.test.ts"
        ],
        "modified_files": [
            "src/engine/examEvent.ts",
            "src/engine/journal.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Add a short exam summary output and store the outcome so it can be reviewed later. Keep the description factual and direct.",
        "tests": "Verify the summary appears and contains the correct pass/fail language.",
        "success_criteria": [
            "An exam summary exists",
            "It is concise and deterministic",
            "The outcome is reviewable",
            "All new tests pass"
        ]
    },
    {
        "number": 90,
        "title": "Day-End Turn Recap Command",
        "phase_role": "Add a narrow command that recaps the current day’s key events and obligations on demand.",
        "goal": "Let the player review the current day without forcing a new narrative pass.",
        "goal_detail": "Implement a fixed command that prints a deterministic recap of the current day's completed events, upcoming obligations, and key state markers.",
        "scope": [
            "Add engine/dayRecap.ts",
            "Wire the command into the parser",
            "Render a compact deterministic recap",
            "Add tests for recap output"
        ],
        "out_of_scope": [
            "Full diary systems",
            "Open-ended narrative recaps",
            "Large summary engines"
        ],
        "new_files": [
            "src/engine/dayRecap.ts",
            "tests/dayRecap.test.ts"
        ],
        "modified_files": [
            "src/engine/actions.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement a day recap command that gathers completed events and current obligations into one fixed output. Keep it deterministic and concise.",
        "tests": "Verify the command returns the expected recap text for a known state.",
        "success_criteria": [
            "A day recap command exists",
            "It is deterministic",
            "It helps review the current day",
            "All new tests pass"
        ]
    },
    {
        "number": 91,
        "title": "Save/Load Persistence Integration Test",
        "phase_role": "Add a narrow integration test that validates save/load persistence for the new academic and journal features.",
        "goal": "Ensure the new state fields survive a save and load cycle.",
        "goal_detail": "Write one deterministic test that saves the current game, reloads it, and verifies the new tuition, journal, and research note state.",
        "scope": [
            "Add tests/integrationSaveLoad.test.ts",
            "Simulate saving and reloading state",
            "Assert persistence of key fields",
            "Keep the test deterministic and narrow"
        ],
        "out_of_scope": [
            "Full end-to-end UI tests",
            "Multiple save slot systems",
            "Open-ended persistence scenarios"
        ],
        "new_files": [
            "tests/integrationSaveLoad.test.ts"
        ],
        "modified_files": [],
        "implementation_sections": "Write a deterministic integration test that saves a game state, loads it back, and checks the expected fields.",
        "tests": "The test itself is the required coverage for this prompt.",
        "success_criteria": [
            "A save/load integration test exists",
            "It validates the new fields",
            "It is deterministic",
            "The test passes"
        ]
    },
    {
        "number": 92,
        "title": "Obligation Status UI Polish",
        "phase_role": "Polish status rendering to highlight active obligations, tuition, and journal entries more clearly.",
        "goal": "Improve the readability of the player's current status without changing mechanics.",
        "goal_detail": "Refine renderStatus so active obligations, debt, and journal notes are presented with clearer labels and spacing. Keep the polish within the existing text UI.",
        "scope": [
            "Modify src/narration/renderStatus.ts",
            "Add formatting for obligations and debt",
            "Keep existing fields unchanged",
            "Add tests for formatted output"
        ],
        "out_of_scope": [
            "New UI frameworks",
            "Graphical displays",
            "Major layout redesigns"
        ],
        "new_files": [
            "tests/renderStatusObligations.test.ts"
        ],
        "modified_files": [
            "src/narration/renderStatus.ts"
        ],
        "implementation_sections": "Improve renderStatus output formatting for obligation and journal sections while keeping the underlying state the same.",
        "tests": "Verify the formatted status shows the obligation label and amount in the expected text form.",
        "success_criteria": [
            "Status output is clearer",
            "Formatting remains deterministic",
            "No mechanics change",
            "All new tests pass"
        ]
    },
    {
        "number": 93,
        "title": "Command Alias Support",
        "phase_role": "Add a small parser alias for one common command to improve usability.",
        "goal": "Make the REPL friendlier by accepting a short alias for a frequently used action.",
        "goal_detail": "Support one additional alias for an existing command such as 'pay' for 'pay tuition' or 'look' for 'status'. Keep the parser change narrow and deterministic.",
        "scope": [
            "Modify src/engine/actions.ts parser rules",
            "Add one alias mapping",
            "Keep alias behaviour identical to the core command",
            "Add tests for alias recognition"
        ],
        "out_of_scope": [
            "Full natural-language parsing",
            "Large synonym dictionaries",
            "Open-ended command discovery"
        ],
        "new_files": [
            "tests/commandAlias.test.ts"
        ],
        "modified_files": [
            "src/engine/actions.ts"
        ],
        "implementation_sections": "Add a single alias mapping in the parser and ensure it resolves to the same action handler. Keep it simple and explicit.",
        "tests": "Verify the alias is accepted and produces the same result as the main command.",
        "success_criteria": [
            "A command alias exists",
            "It maps to an existing action",
            "The parser change is deterministic",
            "All new tests pass"
        ]
    },
    {
        "number": 94,
        "title": "Schedule Breach Penalty Test",
        "phase_role": "Add a test that verifies schedule breaches are handled consistently by the action resolver.",
        "goal": "Ensure actions attempted outside the allowed window are rejected reliably.",
        "goal_detail": "Write one deterministic test that tries a scheduled action at the wrong time and verifies the rejection message and no state change.",
        "scope": [
            "Add tests/scheduleBreach.test.ts",
            "Simulate the action outside its allowed window",
            "Assert the correct rejection behaviour",
            "Keep the test narrow and deterministic"
        ],
        "out_of_scope": [
            "Broad parser behaviour tests",
            "Open-ended schedule logic coverage",
            "Large action policy changes"
        ],
        "new_files": [
            "tests/scheduleBreach.test.ts"
        ],
        "modified_files": [],
        "implementation_sections": "Write a deterministic test that exercises a wrong-time action and verifies the schedule enforcement response.",
        "tests": "The test itself is the prompt coverage.",
        "success_criteria": [
            "Schedule breaches are tested",
            "The enforcement behaviour is reliable",
            "The test is deterministic",
            "The test passes"
        ]
    },
    {
        "number": 95,
        "title": "Faculty Conflict Event",
        "phase_role": "Add one modest faculty conflict event that reflects authority tension without broad politics.",
        "goal": "Introduce a narrow, deterministic conflict scene involving a faculty member and the player.",
        "goal_detail": "Implement one fixed conflict event with a predictable outcome based on a simple state check. Keep it grounded in the University slice and avoid any large political system.",
        "scope": [
            "Add engine/facultyConflict.ts",
            "Trigger the conflict based on a simple state condition",
            "Render a short deterministic scene",
            "Add tests for the conflict outcome"
        ],
        "out_of_scope": [
            "Large political systems",
            "Open-ended negotiation mechanics",
            "Multiple branching outcomes"
        ],
        "new_files": [
            "src/engine/facultyConflict.ts",
            "tests/facultyConflict.test.ts"
        ],
        "modified_files": [
            "src/engine/eventEngine.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement one fixed faculty conflict scene with deterministic resolution. Keep the trigger narrow and the outcome explicit.",
        "tests": "Verify the conflict triggers under the right condition and produces the expected scene text.",
        "success_criteria": [
            "A faculty conflict event exists",
            "It is deterministic and limited",
            "The outcome is fixed",
            "All new tests pass"
        ]
    },
    {
        "number": 96,
        "title": "Debt and Tuition Guard",
        "phase_role": "Add a small guard that prevents the player from performing non-essential actions when tuition debt is overdue.",
        "goal": "Encourage the player to address overdue tuition without introducing harsh failure states.",
        "goal_detail": "Block one optional action when debt is overdue and render a fixed reminder instead. Keep the guard narrow and deterministic.",
        "scope": [
            "Extend engine/tuitionPayment.ts or engine/missedEventChecks.ts",
            "Define one optional action to block when overdue",
            "Render a fixed reminder message",
            "Add tests for the overdue guard"
        ],
        "out_of_scope": [
            "Full punishment systems",
            "Open-ended debt mechanics",
            "Large action gating schemes"
        ],
        "new_files": [
            "tests/debtGuard.test.ts"
        ],
        "modified_files": [
            "src/engine/tuitionPayment.ts",
            "src/engine/actions.ts",
            "src/narration/localNarrator.ts"
        ],
        "implementation_sections": "Implement one narrow overdue guard that blocks an optional action and returns a deterministic reminder notice.",
        "tests": "Verify the action is blocked when debt is overdue and allowed otherwise.",
        "success_criteria": [
            "A tuition overdue guard exists",
            "It is narrow and deterministic",
            "The player receives a reminder",
            "All new tests pass"
        ]
    },
    {
        "number": 97,
        "title": "Rumour Reliability Filter",
        "phase_role": "Add a narrow filter that keeps only reliable, deterministic rumours in the rumour pool.",
        "goal": "Ensure rumours are grounded and not overly speculative.",
        "goal_detail": "Implement a filter for rumour entries that rejects any entry not tied to a known world_state event or reputation effect. Keep the filter explicit and narrow.",
        "scope": [
            "Extend src/engine/rumourPool.ts with a reliability filter",
            "Tie rumours to known state changes",
            "Add tests for filtered rumour publishing",
            "Keep the filter deterministic"
        ],
        "out_of_scope": [
            "Open-ended rumor generation",
            "Large gossip systems",
            "Non-deterministic content selection"
        ],
        "new_files": [
            "tests/rumourReliability.test.ts"
        ],
        "modified_files": [
            "src/engine/rumourPool.ts",
            "src/engine/rumourRipple.ts"
        ],
        "implementation_sections": "Implement a filter that only publishes rumours when they are backed by a specific world_state event. Reject or ignore any unverified rumour candidates.",
        "tests": "Verify only reliable rumours are published and that unsupported candidates are rejected.",
        "success_criteria": [
            "Rumour filtering exists",
            "It is deterministic",
            "Published rumours are tied to state",
            "All new tests pass"
        ]
    },
    {
        "number": 98,
        "title": "Exam Preparation Linkage",
        "phase_role": "Connect study, attendance, and readiness into one narrow exam preparation evaluation.",
        "goal": "Make exam outcomes depend on the player's combined preparation state.",
        "goal_detail": "Evaluate exam readiness from study score, attendance, and performance readiness in one deterministic function. Keep the linkage simple and transparent.",
        "scope": [
            "Extend engine/examEvent.ts evaluation logic",
            "Combine study, attendance, and readiness fields",
            "Keep the function deterministic and explainable",
            "Add tests covering the linkage"
        ],
        "out_of_scope": [
            "Large skill or stat systems",
            "Open-ended exam difficulty scaling",
            "Random outcome modifiers"
        ],
        "new_files": [
            "tests/examPreparationLinkage.test.ts"
        ],
        "modified_files": [
            "src/engine/examEvent.ts",
            "src/engine/studyAction.ts",
            "src/engine/attendance.ts"
        ],
        "implementation_sections": "Implement a deterministic preparation score for exams based on the relevant state fields. Use it to decide the outcome in a transparent way.",
        "tests": "Verify different preparation state combinations produce the expected exam result.",
        "success_criteria": [
            "Exam preparation is linked",
            "The function is deterministic",
            "The relationship is transparent",
            "All new tests pass"
        ]
    },
    {
        "number": 99,
        "title": "Developer Journal State Debug Command",
        "phase_role": "Add one focused developer command that dumps the journal and world_state for debugging.",
        "goal": "Make it easier to inspect journal and world_state during development in a deterministic way.",
        "goal_detail": "Add a developer command that prints a compact summary of journal entries and key world_state flags without altering gameplay.",
        "scope": [
            "Extend engine/debugDump.ts with journal/world_state output",
            "Wire the command into the parser",
            "Keep output compact and deterministic",
            "Add tests for the debug command"
        ],
        "out_of_scope": [
            "Production gameplay changes",
            "Open-ended debug consoles",
            "Non-deterministic output"
        ],
        "new_files": [
            "tests/debugJournalState.test.ts"
        ],
        "modified_files": [
            "src/engine/debugDump.ts",
            "src/engine/actions.ts"
        ],
        "implementation_sections": "Implement a focused debug command that outputs journal and world_state fields in a compact format.",
        "tests": "Verify the command output includes the journal entries and key world state flags.",
        "success_criteria": [
            "A journal debug command exists",
            "It is deterministic",
            "It aids development",
            "All new tests pass"
        ]
    },
    {
        "number": 100,
        "title": "Phase 1 Review and MVP Lockdown",
        "phase_role": "Add a final prompt that reviews the Phase 1 MVP boundary and locks further changes to the current University slice.",
        "goal": "End the current prompt series with a clear statement of the Phase 1 scope and no new systems beyond the MVP slice.",
        "goal_detail": "Summarise the current Phase 1 scope, the systems implemented, and the hard boundaries for the University/Kvothe MVP. Keep the summary concrete and tied to existing prompts.",
        "scope": [
            "Write a final review prompt document or developer note",
            "Summarise the current MVP systems and boundaries",
            "Explicitly mark future features as out of scope for Phase 1",
            "Add tests if appropriate for the review content"
        ],
        "out_of_scope": [
            "New feature implementation",
            "Open-ended scope expansion",
            "Non-MVP era content"
        ],
        "new_files": [
            "docs/phase1_review.md"
        ],
        "modified_files": [
            "RothfussGameDocs/PromptGenerator1-20/prompt_manifest_41_100.json"
        ],
        "implementation_sections": "Create a clear review of the Phase 1 MVP boundary and the systems currently in scope. Keep it concise and developer-facing.",
        "tests": "Not applicable unless a documentation test exists in the repository.",
        "success_criteria": [
            "Phase 1 boundaries are documented",
            "The review is concrete and scoped",
            "No new systems are introduced",
            "The documentation is available"
        ]
    }
]

entries[20:] = new_entries
with manifest_path.open('w', encoding='utf-8') as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)
    f.write('\n')

print(f'Updated {len(new_entries)} entries from 61 to 100 in {manifest_path}')
