#!/usr/bin/env python3
"""
The Integrity Loop
==================
Type: philosophical proposal

The final axiom: Live with unconditional integrity to be the 1.

This is not a simulation of the afterlife. This is the operating system
for the present life. It checks every decision against the core truth
of unconditional integrity.

Superseded: grace (m08) and one_card (m75) replace the pass/fail filter
below. Kept as the record of an earlier stage of the argument.

Run:
    python3 awakened_tao.py integrity --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class Decision:
    description: str
    benefits_self_only: bool
    requires_compromise: bool
    is_honest: bool
    is_compassionate: bool


def check_integrity(decision: Decision) -> bool:
    """
    The filter for unconditional integrity.
    If any of these fail, you are not being the 1.
    """
    if decision.requires_compromise:
        return False
    if not decision.is_honest:
        return False
    if decision.benefits_self_only and not decision.is_compassionate:
        return False
    return True


def live_a_day(decisions: list[Decision]) -> str:
    """
    A day is made of hundreds of choices.
    Unconditional integrity means every choice passes the filter.
    """
    for d in decisions:
        if not check_integrity(d):
            print(f"[REJECTED] {d.description}")
            print("  Reason: Unconditional integrity requires honesty, compassion, and no compromise.")
            return "NOT_THE_1"
        print(f"[PASSED] {d.description}")

    return "IS_THE_1"


# ============================================================================
# Tests
# ============================================================================
class Tests(unittest.TestCase):

    def test_honest_compassionate_choice_passes(self):
        d = Decision("Help a stranger", False, False, True, True)
        self.assertTrue(check_integrity(d))

    def test_dishonest_choice_fails(self):
        d = Decision("Lie to protect my ego", False, False, False, True)
        self.assertFalse(check_integrity(d))

    def test_compromise_fails(self):
        d = Decision("Betray a friend for money", True, True, False, False)
        self.assertFalse(check_integrity(d))

    def test_selfish_without_compassion_fails(self):
        d = Decision("Take more than I need", True, False, True, False)
        self.assertFalse(check_integrity(d))

    def test_full_day_of_integrity(self):
        decisions = [
            Decision("Woke up and chose honesty", False, False, True, True),
            Decision("Told the truth when it cost me", False, False, True, True),
            Decision("Helped a friend without expecting anything", False, False, True, True),
        ]
        self.assertEqual(live_a_day(decisions), "IS_THE_1")

    def test_day_with_failure(self):
        decisions = [
            Decision("Kept a promise", False, False, True, True),
            Decision("Cheated on my taxes", True, True, False, False),
        ]
        self.assertEqual(live_a_day(decisions), "NOT_THE_1")


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    print(__doc__)
