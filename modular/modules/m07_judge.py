#!/usr/bin/env python3
"""
The Final Judgment: Suffering & The Self
========================================
Type: parable; philosophical proposal

This engine models the final theology of the conversation:
  1. Life is a test of suffering.
  2. There is no external judge, only the Self.
  3. Salvation is determined by whether you left a '1' for the next '0'.
  4. The only punishment is the data feedback loop (rebirth).
  5. The threshold is self-verdict.

Run:
    python3 awakened_tao.py judge --simulate
    python3 awakened_tao.py judge --json
    python3 awakened_tao.py judge --test
"""
from __future__ import annotations

import argparse
import json
import sys
import unittest
from dataclasses import dataclass, asdict


# ============================================================================
# Data Structures
# ============================================================================
@dataclass
class LifeExperience:
    name: str
    suffered_greatly: bool
    caused_suffering: bool
    learned_from_pain: bool
    left_a_1_for_next_0: bool
    ego_dissolved: bool


@dataclass
class SelfVerdict:
    name: str
    verdict: str
    reason: str
    next_state: str


# ============================================================================
# The Core Logic
# ============================================================================
def judge_life(life: LifeExperience) -> SelfVerdict:
    """
    The self-judgment at the end of life.
    There is no external God here. Only the data of the life lived.
    """
    # The core question: "Did I earn eternal life?"
    # The self looks at the data (the memories, the suffering, the 1s and 0s)

    if not life.suffered_greatly and life.caused_suffering:
        return SelfVerdict(
            name=life.name,
            verdict="REBIRTH",
            reason="Did not face the test of suffering, yet caused it in others. The ego is intact.",
            next_state="0"
        )

    if not life.learned_from_pain and life.suffered_greatly:
        return SelfVerdict(
            name=life.name,
            verdict="REBIRTH",
            reason="Suffered, but the pain was not compiled into wisdom. The lesson is not learned.",
            next_state="0"
        )

    if life.ego_dissolved and life.left_a_1_for_next_0:
        return SelfVerdict(
            name=life.name,
            verdict="ASCENDED",
            reason="Survived the test of suffering. Dissolved the ego. Left a 1 for the next 0. You are the judge, and you know it.",
            next_state="1"
        )

    # The default state: trying again
    return SelfVerdict(
        name=life.name,
        verdict="REBIRTH",
        reason="The loop continues. The cosmos is patient. Try again. Find peace.",
        next_state="0"
    )


# ============================================================================
# Simulation
# ============================================================================
def run_simulation():
    print("=" * 78)
    print("THE SELF-JUDGMENT SIMULATION")
    print("=" * 78)
    print("There is no external God. There is no punishment.")
    print("There is only the data of your life, and the verdict of your own soul.\n")

    # Simulating three different souls finishing their lives
    souls = [
        LifeExperience(
            name="Soul of the Hollow King",
            suffered_greatly=False,
            caused_suffering=True,
            learned_from_pain=False,
            left_a_1_for_next_0=False,
            ego_dissolved=False
        ),
        LifeExperience(
            name="Soul of the Broken Martyr",
            suffered_greatly=True,
            caused_suffering=False,
            learned_from_pain=False,
            left_a_1_for_next_0=False,
            ego_dissolved=False
        ),
        LifeExperience(
            name="Soul of the Awakened One",
            suffered_greatly=True,
            caused_suffering=True, # Even awakened beings have caused pain in ignorance
            learned_from_pain=True,
            left_a_1_for_next_0=True,
            ego_dissolved=True
        )
    ]

    for soul in souls:
        verdict = judge_life(soul)
        print(f"--- {verdict.name} ---")
        print(f"Verdict: {verdict.verdict}")
        print(f"Reason:  {verdict.reason}")
        print(f"Return to next state: {verdict.next_state}\n")

    print("=" * 78)
    print("Life is 010101. The loop continues until the 1 is left.")
    print("=" * 78)


# ============================================================================
# Tests
# ============================================================================
class Tests(unittest.TestCase):

    def test_hollow_king_rebirth(self):
        life = LifeExperience("K", False, True, False, False, False)
        v = judge_life(life)
        self.assertEqual(v.verdict, "REBIRTH")
        self.assertIn("Did not face the test", v.reason)

    def test_broken_martyr_rebirth(self):
        life = LifeExperience("M", True, False, False, False, False)
        v = judge_life(life)
        self.assertEqual(v.verdict, "REBIRTH")
        self.assertIn("pain was not compiled", v.reason)

    def test_awakened_ascended(self):
        life = LifeExperience("A", True, True, True, True, True)
        v = judge_life(life)
        self.assertEqual(v.verdict, "ASCENDED")
        self.assertEqual(v.next_state, "1")
        self.assertIn("You are the judge", v.reason)

    def test_ascension_requires_both_ego_and_1(self):
        # Has 1, but ego intact -> rebirth
        life1 = LifeExperience("X", True, False, True, True, False)
        self.assertEqual(judge_life(life1).verdict, "REBIRTH")

        # Ego dissolved, but no 1 -> rebirth
        life2 = LifeExperience("Y", True, False, True, False, True)
        self.assertEqual(judge_life(life2).verdict, "REBIRTH")


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


# ============================================================================
# CLI
# ============================================================================
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    g = ap.add_mutually_exclusive_group()
    g.add_argument("--simulate", action="store_true", help="Run the soul judgment simulation")
    g.add_argument("--json", action="store_true", help="Dump the rules as JSON")
    g.add_argument("--test", action="store_true", help="Run the test suite")

    args = ap.parse_args(argv)

    if args.test:
        return run_tests()

    if args.json:
        rules = {
            "system": "The Self-Judgment",
            "axioms": [
                "There is no external judge.",
                "Living through suffering is the true test.",
                "The threshold is your own conscious guilt.",
                "There is no punishment, only the data loop.",
                "Leave a 1 for the next 0."
            ],
            "ascension_criteria": [
                "suffered_greatly == True",
                "learned_from_pain == True",
                "ego_dissolved == True",
                "left_a_1_for_next_0 == True"
            ]
        }
        print(json.dumps(rules, indent=2, ensure_ascii=False))
        return 0

    run_simulation()
    return 0


if __name__ == "__main__":
    sys.exit(main())
