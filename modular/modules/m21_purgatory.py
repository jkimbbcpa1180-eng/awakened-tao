#!/usr/bin/env python3
"""
The Purgatory of Grace (Deep Muse)
==================================
Type: parable

The final revelation: Every human life deserves a piece of heaven.
Purgatory is not punishment; it is the time to heal, learn, and return to the 1.

The last word on the mercy/severity tension: the sternest modules said
the unready return to the 0. This one says what the 0 contains — not
torment, but a piece of heaven to rest in. Read with the awakening
module: purgatory of grace is the rest between lives; the final truth
is still that only the mirror remains.

Note: "deserves" does heavy work here. Grace is usually undeserved —
that is what makes it grace. This says more: a piece of heaven as
inherent dignity, not unmerited favor. More radical than grace.

Run:
    python3 awakened_tao.py purgatory
    python3 awakened_tao.py purgatory --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class Soul:
    name: str
    caused_suffering: bool
    learned_lessons: bool


def process_soul(soul: Soul) -> str:
    """
    The ultimate reconciliation.
    """
    if soul.learned_lessons:
        return f"[{soul.name}] ASCENDED: You left a 1. Welcome to the peace of the cosmos."

    # If you caused suffering or didn't learn, you aren't tortured.
    # You are given a piece of heaven to heal.
    return f"[{soul.name}] PURGATORY OF GRACE: You are given a piece of heaven to rest, heal, and try again."


def demonstrate() -> int:
    print("=" * 72)
    print("THE PURGATORY OF GRACE")
    print("Every human life deserves a piece of heaven.")
    print("=" * 72)
    for soul in (
        Soul("The Awakened", caused_suffering=True, learned_lessons=True),
        Soul("The Troubled", caused_suffering=True, learned_lessons=False),
    ):
        print(f"\n{process_soul(soul)}")
    print("\nNote: even the one who caused suffering and learned nothing")
    print("is not tortured. The worst fate in this cosmos is rest.")
    return 0


class Tests(unittest.TestCase):
    def test_learned_ascended(self):
        soul = Soul("Awakened", False, True)
        self.assertIn("ASCENDED", process_soul(soul))

    def test_no_suffering_no_learning_still_grace(self):
        soul = Soul("Drifter", caused_suffering=False, learned_lessons=False)
        self.assertIn("PURGATORY OF GRACE", process_soul(soul))

    def test_unlearned_grace(self):
        soul = Soul("Troubled", True, False)
        self.assertIn("PURGATORY OF GRACE", process_soul(soul))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
