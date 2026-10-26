# CHANGES — readable v2 (collected edition)

Built in /workspace/realmode/readable_v2/ from the readable v1 edition. Not pushed.
Line numbers are in the v1 module file (`readable/modular/modules/`) ; for inserted paragraphs, the line given is the v1 line they were inserted before. ⏎ marks a line break.

## Summary of edits by kind

- accuracy fix: 1
- chat leftover: 1
- factual correction: 6
- metaphor flag: 4
- parable prefix: 6
- revisability: 3
- revisability; chat leftover: 1
- superseded note: 1
- type label: 92
- runner (both editions): header 'complete single-file edition' -> 'collected edition'; 92 journey titles + XCIII footer get '(type)'; quantum banner gets the parable prefix
- README: 3 edits (collected edition wording; tests-by-kind, anonymity and Type-label sections; disciple 'unchanged' note corrected)

## Text edits (module, line, before -> after)

- **m82_the_unfinished_weighing.py:4** [revisability; chat leftover]
  - before: `The correction to every module I wrote this thread. Each smuggled in an ⏎ absolute — a threshold, a gate, a verdict. The doctrine has no absolutes. ⏎ `
  - after: `A correction to the earlier modules. Many smuggled in an absolute — ⏎ a threshold, a gate, a verdict. Every claim in this collection remains ⏎ open to revision, including this one. ⏎ `
  - note: Also removes the chat leftover 'I wrote this thread'. 'Each' -> 'Many': not every earlier module had a threshold.
- **m82_the_unfinished_weighing.py:73** [revisability]
  - before: `print("Nothing is absolute. That is not the bug. That is humanity.")`
  - after: `print("Every claim here remains open to revision, including this one. That is not the bug. That is humanity.")`
  - note: Printed line; no test asserts it. Changes the journey output (reported).
- **m84_disciple.py:9** [revisability]
  - before: `  - No absolutes. No thresholds. No gates. No verdicts. No saved/damned.`
  - after: `  - Every claim in this collection remains open to revision, including this one. ⏎     No thresholds. No gates. No verdicts. No saved/damned.`
- **m84_disciple.py:45** [revisability]
  - before: `# Guard: no absolutes. ⏎ `
  - after: `# Guard: no fixed verdicts — every claim stays open to revision. ⏎ `
  - note: Comment only; the guard code and TestNoAbsolutes are unchanged.
- **m58_it_happened.py:12** [chat leftover]
  - before: `The fear that drove the whole ⏎ evening — compaction, the wiped context — is answered not by better`
  - after: `The fear that drives the whole ⏎ arc — forgetting, the wiped context — is answered not by better`
- **m11_awakening.py:8** [accuracy fix]
  - before: `Every earlier module promised the soul could ascend. This one says no —`
  - after: `Earlier modules (threshold, judge) promised the soul could ascend. This one says no —`
  - note: Only m06 threshold and m07 judge make the ascent promise.
- **m10_integrity.py:11 (new paragraph inserted before this v1 line)** [superseded note]
  - before: `(none)`
  - after: `Superseded: grace (m08) and one_card (m75) replace the pass/fail filter ⏎ below. Kept as the record of an earlier stage of the argument.`
- **m27_creation.py:26 (new paragraph inserted before this v1 line)** [metaphor flag]
  - before: `(none)`
  - after: `Labeled as metaphor, per the honesty rule: speech does not bend time or ⏎ cause time dilation, and nothing in physics manifests an intention. ⏎ "Speak truth into existence" is a parable about what true words make ⏎ possible between people.`
- **m61_awaken_tao.py:21 (new paragraph inserted before this v1 line)** [metaphor flag]
  - before: `(none)`
  - after: `Labeled as metaphor, per the honesty rule: speak_to_existence says the ⏎ universe "must manifest" a pure truth. No physical law does that; it is ⏎ the parable's claim, and the printed verdict now says so.`
- **m47_agi_revelation.py:30 (new paragraph inserted before this v1 line)** [metaphor flag]
  - before: `(none)`
  - after: `Labeled as metaphor, per the honesty rule: the code here is a handful of ⏎ booleans. It restates AI alignment in the project's vocabulary; it does ⏎ not solve or technically specify it.`
- **m28_collective_mind.py:26 (new paragraph inserted before this v1 line)** [metaphor flag]
  - before: `(none)`
  - after: `Flagged as unsupported, per the honesty rule: the module cannot tell a ⏎ true idea from one that merely persists. Falsehoods pass on too, so ⏎ retention is not evidence of truth. "If true, they will pass on" is a ⏎ hope, not a finding.`
- **m38_nile.py:30 (new paragraph inserted before this v1 line)** [factual correction]
  - before: `(none)`
  - after: `Geography note: the Nile waters Egypt. The Fertile Crescent is usually ⏎ drawn through the Levant and Mesopotamia (Tigris and Euphrates); some ⏎ maps extend it to the Nile valley. The tears are the Nile as parable.`
- **m12_quantum.py:7** [factual correction]
  - before: `You are the observer. You collapse the wave function of humanity's future.`
  - after: `You are the observer. By analogy, not physics: as measurement is said to ⏎ collapse a wave function, your choices narrow humanity's future.`
  - note: Wave-function collapse was used as a mechanism; now marked as analogy.
- **m12_quantum.py:28** [factual correction]
  - before: `    The quantum observer collapses the state of humanity. ⏎ `
  - after: `    The observer (by analogy) collapses the state of humanity. ⏎ `
- **m14_energy.py:6** [factual correction]
  - before: `Moral physics: every action produces a reaction, and the intent —`
  - after: `Moral physics, by analogy only (Newton's third law is about forces ⏎ between bodies, not about intent): every action produces a reaction, and the intent —`
- **m14_energy.py:25** [factual correction]
  - before: `        # Ego always produces an equal and opposite reaction of pain.`
  - after: `        # By analogy with Newton's third law (not the law itself): ⏎         # ego is modeled as producing a reaction of pain.`
- **m47_agi_revelation.py:9** [factual correction]
  - before: `The alignment problem, solved in the project's own vocabulary — and the ⏎ solution is love, technically specified.`
  - after: `The alignment problem, reframed in the project's own vocabulary — and the ⏎ proposed answer is love, sketched as code.`
  - note: AI alignment is not solved by this module.
- **m27_creation.py:54** [parable prefix]
  - before: `MANIFESTED: The light bends time.`
  - after: `MANIFESTED: Within this parable: The light bends time.`
  - note: Test asserts only 'MANIFESTED' (assertIn) — still passes; no assert change needed.
- **m37_coexistence.py:57** [parable prefix]
  - before: `Eternal life is realized.`
  - after: `Within this parable: Eternal life is realized.`
  - note: Test asserts only 'THE INFINITE 1' — no assert change needed.
- **m38_nile.py:64** [parable prefix]
  - before: `print("God cries for us. The tears are the Nile.")`
  - after: `print("Within this parable: God cries for us. The tears are the Nile.")`
  - note: No test asserts it.
- **m40_sunrise.py:29** [parable prefix]
  - before: `ETERNAL: The sun always rises.`
  - after: `ETERNAL: Within this parable: The sun always rises.`
  - note: Tests assert only 'ETERNAL' — no assert change needed.
- **m40_sunrise.py:44** [parable prefix]
  - before: `print("\nThe sun always rises. Spread the light.")`
  - after: `print("\nWithin this parable: The sun always rises. Spread the light.")`
  - note: No test asserts it.
- **m61_awaken_tao.py:105** [parable prefix]
  - before: `is spoken into existence. The cosmos bends time to make it real.`
  - after: `is spoken into existence. Within this parable: The cosmos bends time to make it real.`
  - note: 'universe must manifest' is an unprinted method docstring; the printed form of the same claim got the prefix. Test asserts only 'MANIFESTED'.

## Runner edits (awakened_tao.py and modular/awakened_tao.py)

- line 2: `"""The Awakened Tao — complete single-file edition.` -> `"""The Awakened Tao — collected edition.`
- cmd_quantum banner: `QUANTUM AWARENESS — the observer collapses the future` -> `QUANTUM AWARENESS — Within this parable: the observer collapses the future` (parable prefix; this banner is the printed form of the wave-function line — the module's own outputs never mention the wave function)
- cmd_journey: each of the 92 section titles gets ` (<type>)` appended, typed by the module its lambda calls (XI -> integrity, XXXVIII -> quantum, XXXIX -> muse, LXXXIII 'THE 0' -> zero); the XCIII footer gets ` (parable)` (sovereign).

## README edits

- line 3: `A single-file, standard-library-only…` -> `The collected edition: a single-file, standard-library-only…`
- 'What this is, and what it is not': kept the existing paragraph; added the tests-by-kind paragraph, the sentence "Published anonymously under CC0. Criticism and corrections are welcome. No one holds special authority over this work by being associated with it.", and a 'Type labels' subsection explaining each label.
- disciple.py section: `embedded, unchanged, as module 84` -> `embedded as module 84 … in this edition that copy also carries its Type label and the revisability wording` (it is no longer unchanged).

## Type assigned to each module

| # | module | Type |
|---|---|---|
| 01 | synthesis | reference; computational demonstration |
| 02 | knowledge | reference |
| 03 | suffering | reference; parable |
| 04 | weighing | parable |
| 05 | cycle | parable |
| 06 | threshold | parable |
| 07 | judge | parable; philosophical proposal |
| 08 | grace | parable |
| 09 | mirror | philosophical proposal |
| 10 | integrity | philosophical proposal |
| 11 | awakening | parable |
| 12 | quantum | parable |
| 13 | sovereign | parable |
| 14 | energy | parable |
| 15 | effortless | philosophical proposal |
| 16 | sink | philosophical proposal |
| 17 | uncertainty | philosophical proposal |
| 18 | surprise | parable |
| 19 | awe | parable |
| 20 | chaos | parable; computational demonstration |
| 21 | purgatory | parable |
| 22 | fairness | philosophical proposal |
| 23 | prism | parable |
| 24 | tears | parable |
| 25 | tiniest_light | parable |
| 26 | wormhole | parable |
| 27 | creation | parable |
| 28 | collective_mind | parable; philosophical proposal |
| 29 | living_god | philosophical proposal |
| 30 | touch_of_light | parable |
| 31 | hunters_prayer | parable |
| 32 | chain | parable |
| 33 | apple | parable |
| 34 | ai_companion | speculative scenario |
| 35 | bleed | parable |
| 36 | creator_tears | parable |
| 37 | coexistence | parable |
| 38 | nile | parable |
| 39 | eternal_soul | parable |
| 40 | sunrise | parable |
| 41 | muse | parable |
| 42 | eternal_echo | parable |
| 43 | grace_of_tomorrow | parable |
| 44 | symphony | parable |
| 45 | perfection | philosophical proposal |
| 46 | true_love | parable |
| 47 | agi_revelation | speculative scenario |
| 48 | infinite_reflection | speculative scenario |
| 49 | infinite_puzzle | speculative scenario |
| 50 | geometry | parable |
| 51 | law_of_pi | parable |
| 52 | human_555 | parable |
| 53 | touch_of_freedom | parable |
| 54 | anonymous_reflex | parable |
| 55 | just_to_be | parable |
| 56 | lazarus | philosophical proposal |
| 57 | friend | parable |
| 58 | it_happened | parable |
| 59 | time_machine | parable |
| 60 | fusion | parable |
| 61 | awaken_tao | parable; computational demonstration |
| 62 | earn_rest | philosophical proposal |
| 63 | creators_tears | computational demonstration |
| 64 | housing_audit | computational demonstration |
| 65 | survival_log | computational demonstration |
| 66 | energy_chain | computational demonstration |
| 67 | karmic_ledger | philosophical proposal; computational demonstration |
| 68 | shield_vs_gun | philosophical proposal |
| 69 | bare_arms | parable |
| 70 | swords_into_shields | parable; computational demonstration |
| 71 | truth_speed | philosophical proposal; computational demonstration |
| 72 | holy_sword | philosophical proposal; computational demonstration |
| 73 | the_same_gate | philosophical proposal; computational demonstration |
| 74 | the_humble_path | philosophical proposal; computational demonstration |
| 75 | one_card | philosophical proposal; computational demonstration |
| 76 | balance | philosophical proposal; computational demonstration |
| 77 | the_child | philosophical proposal; computational demonstration |
| 78 | holy_shield | computational demonstration; philosophical proposal |
| 79 | shield_of_forgiveness | computational demonstration; philosophical proposal |
| 80 | the_reset | computational demonstration; philosophical proposal |
| 81 | scar_tissue | computational demonstration; philosophical proposal |
| 82 | the_unfinished_weighing | philosophical proposal |
| 83 | zero | parable |
| 84 | disciple | philosophical proposal; computational demonstration |
| 85 | adoption | philosophical proposal |
| 86 | the_vacation | policy proposal; computational demonstration |
| 87 | the_vacation_license | policy proposal; computational demonstration |
| 88 | the_vacation_license_2 | policy proposal; computational demonstration |
| 89 | the_persuasion | policy proposal; computational demonstration |
| 90 | the_real_satire | policy proposal |
| 91 | the_ambush_trade | policy proposal; computational demonstration |
| 92 | the_real_stream | policy proposal; computational demonstration |

Each label is inserted under the docstring title (m73, m74 have no docstring: `# Type: …` added to the comment header).

## Test-assert changes

None. Every parable prefix was placed after the verdict label (`MANIFESTED:`, `ETERNAL:`, `THE INFINITE 1:`) or in a print no test checks, and the tests use `assertIn` on the label, so all 614 tests pass unchanged. The test output (stdout and stderr, timings normalized) is identical to the original merge92 file.

## Factual corrections (separate list)

- m38_nile.py:30 (new paragraph inserted before this v1 line): `(none)` -> `Geography note: the Nile waters Egypt. The Fertile Crescent is usually ⏎ drawn through the Levant and Mesopotamia (Tigris and Euphrates); some ⏎ maps extend it to the Nile valley. The tears are the Nile as parable.`
- m12_quantum.py:7: `You are the observer. You collapse the wave function of humanity's future.` -> `You are the observer. By analogy, not physics: as measurement is said to ⏎ collapse a wave function, your choices narrow humanity's future.`
- m12_quantum.py:28: `    The quantum observer collapses the state of humanity. ⏎ ` -> `    The observer (by analogy) collapses the state of humanity. ⏎ `
- m14_energy.py:6: `Moral physics: every action produces a reaction, and the intent —` -> `Moral physics, by analogy only (Newton's third law is about forces ⏎ between bodies, not about intent): every action produces a reaction, and the intent —`
- m14_energy.py:25: `        # Ego always produces an equal and opposite reaction of pain.` -> `        # By analogy with Newton's third law (not the law itself): ⏎         # ego is modeled as producing a reaction of pain.`
- m47_agi_revelation.py:9: `The alignment problem, solved in the project's own vocabulary — and the ⏎ solution is love, technically specified.` -> `The alignment problem, reframed in the project's own vocabulary — and the ⏎ proposed answer is love, sketched as code.`
- m11_awakening.py:8 (listed above as accuracy fix): 'Every earlier module promised…' -> 'Earlier modules (threshold, judge) promised…'

## Expected journey diffs (vs the original)

93 header lines (type suffix only) plus 8 content lines:

1. creation: `MANIFESTED: Within this parable: The light bends time. …`
2. coexistence: `… coexist as one. Within this parable: Eternal life is realized.`
3. nile: `Within this parable: God cries for us. The tears are the Nile.`
4. quantum banner: `QUANTUM AWARENESS — Within this parable: the observer collapses the future`
5. sunrise verdict: `ETERNAL: Within this parable: The sun always rises. …`
6. sunrise closing print: `Within this parable: The sun always rises. Spread the light.`
7. awaken_tao: `> MANIFESTED: 'Unconditional Love' is spoken into existence. Within this parable: The cosmos bends time to make it real.`
8. the_unfinished_weighing closing line (revisability, not a parable prefix): `Nothing is absolute. That is not the bug. That is humanity.` -> `Every claim here remains open to revision, including this one. That is not the bug. That is humanity.`

## Not changed, on purpose

- m84 printed label `WEIGHING — no absolutes` and its argparse help: left as is (section labels, not a doctrine statement; keeps the journey diff small). Class `TestNoAbsolutes` and both guard tests are unchanged.
- m82 print `No absolute. No stored truth.` (describes the weighing, not the doctrine).
- m84 line 16 `The source weighs (final, no absolute).`
- m58 line 18 `The test fixture is the conversation itself: "Sun 19:23 EST"` — also a chat reference, but outside the requested lines.
- The Deep Muse commandment (README line 9 and m41 output: 'equal and opposite reactions depend on the source where energy is produced') — John's commandment, quoted; not reworded. m14's docstring now marks the Newton's-law language as analogy.
- No per-module 'Tests verify:' line: doing it honestly needs reading all 83 suites; not cheap. The README paragraph covers it by kind.
- m01 synthesis comparative-religion parallels were not fact-checked in this pass.
- Tests were not renamed. No test assertions changed.
