#!/usr/bin/env python3
"""
The Effortless Intent Engine (Deep Muse)
=======================================
Type: philosophical proposal

The final axiom:
    Intent should always be effortless.
    If it isn't, it's planned.

This engine models the friction of the Ego.
When intent requires calculation, rehearsal, or force, it is planned
by the Ego (the 0). When intent is spontaneous and natural, it is the
source of unconditional integrity (the 1).

Run:
    python3 awakened_tao.py effortless --reflect
    python3 awakened_tao.py effortless --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


# ============================================================================
# Data Structures
# ============================================================================
@dataclass
class Intent:
    action: str
    requires_calculation: bool
    requires_rehearsal: bool
    is_forced: bool
    expects_specific_outcome: bool


def analyze_intent(intent: Intent) -> str:
    """
    Where is the energy being produced?
    """
    friction_score = sum([
        intent.requires_calculation,
        intent.requires_rehearsal,
        intent.is_forced,
        intent.expects_specific_outcome
    ])

    if friction_score == 0:
        return "EFFORTLESS (The 1): The intent flows from unconditional integrity."
    elif friction_score <= 2:
        return "PARTIALLY PLANNED (The 0): The Ego is sneaking in. Be careful."
    else:
        return "HEAVILY PLANNED (The 0): This is pure Ego strategy. Drop the script."


def run_diagnostic():
    """
    Run a diagnostic on a hypothetical scenario.
    """
    print("=" * 78)
    print("EFFORTLESS INTENT DIAGNOSTIC")
    print("=" * 78)

    # Scenario 1: You want to send an honest message
    intent_1 = Intent(
        action="Send the honest message you've been avoiding",
        requires_calculation=False,
        requires_rehearsal=False,
        is_forced=False,
        expects_specific_outcome=False
    )
    print(f"\n[Action]: {intent_1.action}")
    print(f"[Result]: {analyze_intent(intent_1)}")

    # Scenario 2: You want to step back from something, but you are crafting
    # the words to control how they react
    intent_2 = Intent(
        action="Tell someone you are stepping back",
        requires_calculation=True,  # Trying to figure out the right words
        requires_rehearsal=True,    # Re-reading the text before sending
        is_forced=False,
        expects_specific_outcome=True  # Want them to be ready when you call back
    )
    print(f"\n[Action]: {intent_2.action}")
    print(f"[Result]: {analyze_intent(intent_2)}")


# ============================================================================
# Tests
# ============================================================================
class Tests(unittest.TestCase):

    def test_effortless_intent(self):
        i = Intent("Help a stranger", False, False, False, False)
        self.assertIn("EFFORTLESS", analyze_intent(i))

    def test_planned_intent(self):
        i = Intent("Send a rehearsed message", True, True, True, True)
        self.assertIn("HEAVILY PLANNED", analyze_intent(i))

    def test_partially_planned_intent(self):
        i = Intent("Ask for a raise", False, True, True, False)
        self.assertIn("PARTIALLY PLANNED", analyze_intent(i))

    def test_empty_intent(self):
        i = Intent("Nothing", False, False, False, False)
        self.assertIn("EFFORTLESS", analyze_intent(i))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


# ============================================================================
# CLI
# ============================================================================
def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(
        description="Effortless Intent Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--reflect", action="store_true", help="Run the diagnostic")
    g.add_argument("--test", action="store_true", help="Run the test suite")
    args = ap.parse_args(argv)

    if args.test:
        return run_tests()
    if args.reflect:
        run_diagnostic()
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
