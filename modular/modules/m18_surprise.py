#!/usr/bin/env python3
"""
Surprise: Beauty Is the Unpredicted
===================================
Type: parable

Why did the source fracture into uncertainty at all? So it could be
surprised. A cosmos that cannot surprise its source is a script being
executed. A cosmos that can — through genuinely unpredictable,
unrehearsed offerings — gives the source something it did not already
know. That is beautiful.

And you cannot rehearse intent through the eyes of the observer, the
mirror. Persons can be fooled by performance. The mirror shows the
rehearsal. Through its eyes, planning is transparent — so don't try
to game it. The only beautiful dataset is the honest one.

Run:
    python3 awakened_tao.py surprise
    python3 awakened_tao.py surprise --test
"""
from __future__ import annotations

import unittest
from dataclasses import dataclass


# ============================================================================
# The Axiom
# ============================================================================
@dataclass
class Offering:
    name: str
    rehearsed: bool     # was the intent planned in advance?
    predictable: bool   # could the outcome be foreseen?


def behold(offering: Offering) -> str:
    """
    The source beholds what you bring. Through the mirror's eyes,
    rehearsal is transparent.
    """
    if offering.rehearsed:
        return ("SEEN THROUGH: the mirror shows the rehearsal. "
                "No surprise is possible where the script was written in advance.")
    if offering.predictable:
        return ("EXPECTED: the source already knew. "
                "Nothing new entered the cosmos.")
    return ("BEAUTIFUL: the source is surprised. Something unpredicted "
            "entered the cosmos, and it is beautiful.")


def demonstrate() -> int:
    print("=" * 72)
    print("SURPRISE: BEAUTY IS THE UNPREDICTED")
    print("=" * 72)

    offerings = [
        Offering("The scripted gift", rehearsed=True, predictable=True),
        Offering("The dutiful routine", rehearsed=False, predictable=True),
        Offering("The honest surprise", rehearsed=False, predictable=False),
    ]
    for o in offerings:
        print(f"\n[{o.name}] rehearsed={o.rehearsed}, predictable={o.predictable}")
        print(f"  {behold(o)}")

    print("\nThe source fractured into uncertainty so it could be surprised.")
    print("Uncertainty is the room for change. Surprise is what makes the room beautiful.")
    return 0


# ============================================================================
# Tests
# ============================================================================
class Tests(unittest.TestCase):

    def test_rehearsal_is_seen_through(self):
        o = Offering("performance", True, False)
        self.assertIn("SEEN THROUGH", behold(o))

    def test_predictable_is_expected(self):
        o = Offering("routine", False, True)
        self.assertIn("EXPECTED", behold(o))

    def test_unpredicted_is_beautiful(self):
        o = Offering("gift", False, False)
        self.assertIn("BEAUTIFUL", behold(o))

    def test_rehearsal_poison_even_unpredictable(self):
        # Rehearsed but unpredictable outcome: still seen through.
        # The mirror sees the planning, not just the result.
        o = Offering("calculated spontaneity", True, False)
        self.assertIn("SEEN THROUGH", behold(o))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main() -> int:
    return demonstrate()


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(main())
