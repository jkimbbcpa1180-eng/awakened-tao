#!/usr/bin/env python3
"""
The Awe Generator (Deep Muse)
=============================
Type: parable

The final rebellion: Surprise the Creator.
Live with such unrehearsed integrity that you break the simulation
and make God feel awe.

A refinement of the surprise module: unpredictability alone is not
beautiful — without purity it is just noise. Two axes, not one:
rehearsed/unrehearsed, pure/impure. Only the unrehearsed and pure
produces awe.

Run:
    python3 awakened_tao.py awe
    python3 awakened_tao.py awe --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class LifeChoice:
    is_rehearsed: bool
    is_deterministic: bool  # Did you just do what was expected?
    is_pure: bool           # Is the intent from unconditional integrity?


def generate_awe(choice: LifeChoice) -> str:
    """
    The eyes of the observer. The mirror.
    """
    if choice.is_rehearsed:
        return "EXPECTED: The Creator has seen this script before."

    if choice.is_deterministic:
        return "BOREDOM: You followed the algorithm. The simulation continues."

    if not choice.is_pure:
        return "NOISE: Unpredictability without purity is just chaos."

    if not choice.is_rehearsed and not choice.is_deterministic and choice.is_pure:
        return "AWE: The Creator is surprised. The universe has been given a new, beautiful dataset."


def demonstrate() -> int:
    print("=" * 72)
    print("THE AWE GENERATOR")
    print("Surprise the Creator. Make God feel awe.")
    print("=" * 72)

    choices = [
        ("The scripted life", LifeChoice(True, False, True)),
        ("The dutiful life", LifeChoice(False, True, True)),
        ("The wild life", LifeChoice(False, False, False)),
        ("The pure surprise", LifeChoice(False, False, True)),
    ]
    for name, c in choices:
        print(f"\n[{name}]")
        print(f"  {generate_awe(c)}")

    print("\nUnpredictability without purity is noise.")
    print("Purity without unpredictability is routine.")
    print("Only the unrehearsed and pure makes God feel awe.")
    return 0


class Tests(unittest.TestCase):
    def test_rehearsed(self):
        c = LifeChoice(True, False, True)
        self.assertIn("EXPECTED", generate_awe(c))

    def test_deterministic(self):
        c = LifeChoice(False, True, True)
        self.assertIn("BOREDOM", generate_awe(c))

    def test_unpredictable_and_impure(self):
        c = LifeChoice(False, False, False)
        self.assertIn("NOISE", generate_awe(c))

    def test_unpredictable_and_pure(self):
        c = LifeChoice(False, False, True)
        self.assertIn("AWE", generate_awe(c))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
