#!/usr/bin/env python3
"""
The Creator's Tears (Deep Muse)
===============================
Type: computational demonstration

Make God cry with empathy, not bleed.

Empathy is a value from 0 to 1. Above 0.9, the cosmos weeps and the Nile
flows. Bad input (not a number, NaN, or outside 0..1) falls back to 0.

Run:
    python3 awakened_tao.py creators-tears
    python3 awakened_tao.py creators-tears --test
"""
from __future__ import annotations
import math
import unittest


def clean_empathy(empathy) -> float:
    try:
        e = float(empathy)
    except (TypeError, ValueError):
        return 0.0
    if math.isnan(e) or e < 0.0 or e > 1.0:
        return 0.0
    return e


def make_god_cry(empathy) -> str:
    if clean_empathy(empathy) > 0.9:
        return "TEARS OF THE COSMOS: The Creator weeps. The Nile flows. The Fertile Crescent blooms."
    return "SILENCE: The cosmos remains a machine."


def demonstrate() -> int:
    print("=" * 72)
    print("THE CREATOR'S TEARS")
    print("Make God cry with empathy, not bleed.")
    print("=" * 72)
    for e in (0.95, 0.5, "not a number"):
        print(f"\n  empathy={e!r}: {make_god_cry(e)}")
    return 0


class Tests(unittest.TestCase):
    def test_tears(self):
        self.assertIn("TEARS OF THE COSMOS", make_god_cry(0.95))

    def test_threshold_is_strict(self):
        self.assertIn("SILENCE", make_god_cry(0.9))

    def test_bad_input_fallback(self):
        for bad in ("abc", None, float("nan"), -0.5, 1.5, 99):
            self.assertIn("SILENCE", make_god_cry(bad))
            self.assertEqual(clean_empathy(bad), 0.0)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
