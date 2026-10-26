#!/usr/bin/env python3
"""STANDING — codifying the epistemic boundary of simulation ledgers.

Ensures that no model, ledger, or verdict can claim authority or rule
on value judgments. The ledger reports; it does not rule.

Fix: the guard now refuses anything that is not exactly False (1, "yes"
and [True] used to slip through), and the demo uses the corrected
ledger figure (975.36 kJ, compute energy counted once).

Run:
    python3 standing.py
    python3 standing.py --test
"""

from __future__ import annotations

import argparse
import sys
import unittest
from dataclasses import dataclass


# ----------------------------------------------------------------------
# I. The Epistemic Boundary Enforcement
# ----------------------------------------------------------------------

@dataclass(frozen=True)
class Verdict:
    """Represents a descriptive report that explicitly renounces standing."""
    statement: str
    standing: bool = False

    def __post_init__(self):
        if self.standing is not False:
            raise ValueError(
                "Epistemic Violation: A mathematical model or energy ledger "
                "cannot possess standing. It calculates consequences; "
                "it does not rule on values."
            )

    def render(self) -> str:
        return (
            f"{self.statement}\n"
            f"STANDING: {str(self.standing)} — the ledger reports; it does not rule."
        )


# ----------------------------------------------------------------------
# II. Demo & Test Suite
# ----------------------------------------------------------------------

def demonstrate() -> int:
    print("=" * 72)
    print("STANDING — the epistemic boundary of simulation ledgers")
    print("=" * 72)
    v = Verdict("Exergy destruction quantified: 975.36 kJ.")
    print(f"\n{v.render()}")
    return 0


class Tests(unittest.TestCase):

    def test_standing_is_false_by_default(self):
        v = Verdict("Test statement.")
        self.assertFalse(v.standing)

    def test_standing_true_is_strictly_rejected(self):
        """A ledger claiming authority must crash. Software cannot rule."""
        with self.assertRaises(ValueError):
            Verdict("We declare this system 100% green.", standing=True)

    def test_truthy_standing_is_rejected(self):
        """Anything that is not exactly False is a claim of standing."""
        for val in (1, "yes", [True], None, 0.5):
            with self.assertRaises(ValueError, msg=repr(val)):
                Verdict("x", standing=val)

    def test_verdict_renders_honestly(self):
        v = Verdict("Mass balance verified.")
        self.assertIn("STANDING: False", v.render())
        self.assertIn("the ledger reports; it does not rule", v.render())


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Standing enforcement module.")
    ap.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    if args.test:
        return run_tests()
    return demonstrate()


if __name__ == "__main__":
    sys.exit(main())
