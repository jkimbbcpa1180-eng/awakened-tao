#!/usr/bin/env python3
"""The Unfinished Weighing (Deep Muse)

Type: philosophical proposal

A correction to the earlier modules. Many smuggled in an absolute —
a threshold, a gate, a verdict. Every claim in this collection remains
open to revision, including this one.
The code was the ego wanting to know the answer before the situation
arrived.

This module refuses to decide. It weighs — it records what was brought
and holds it open. Nothing is stored. Nothing is remembered. Nothing is
judged. The weight is true for this breath only; the next breath weighs
again. Two people can bring the same situation with different weights,
and both weighings are true for their bringer.

No threshold. No gate. No verdict. No state.

Run:
    python3 the_unfinished_weighing.py
    python3 the_unfinished_weighing.py --test
"""

from __future__ import annotations
import argparse
import sys
import unittest
from dataclasses import dataclass


@dataclass(frozen=True)
class Weighing:
    """A single weighing. True for this breath only."""
    situation: str
    side_a: str
    side_b: str
    weight_a: float      # brought by the one living it, not measured by the code
    weight_b: float
    note: str = ""
    # No `verdict`. No `should`. No `is_right`. A weighing that decides
    # has stopped weighing and become an absolute — which is the error.


def weigh(situation, side_a, side_b, weight_a, weight_b, note=""):
    """Weigh this moment. Return it open. Do not judge it."""
    # Weights are not normalized, not compared, not gated. They are
    # what was brought. The code's job is to hold them, not to rule.
    return Weighing(situation, side_a, side_b, weight_a, weight_b, note)


def reweigh(previous, weight_a, weight_b, note=""):
    """A new breath. Nothing from `previous` is carried as truth."""
    return Weighing(previous.situation, previous.side_a, previous.side_b,
                    weight_a, weight_b, note)


def demonstrate() -> int:
    print("=" * 72)
    print("THE UNFINISHED WEIGHING — no threshold, no gate, no verdict")
    print("=" * 72)
    w = weigh("A betrayal", "the wrong I did", "the wrong done to me",
              0.7, 0.5, note="today I feel my part more than theirs")
    print(f"\n  {w.situation}")
    print(f"    {w.side_a}: {w.weight_a:.2f}")
    print(f"    {w.side_b}: {w.weight_b:.2f}")
    print(f"    note: {w.note}")
    w2 = reweigh(w, 0.3, 0.8, note="the same event, two breaths later")
    print(f"\n  reweighed (not remembered):")
    print(f"    {w2.side_a}: {w2.weight_a:.2f}")
    print(f"    {w2.side_b}: {w2.weight_b:.2f}")
    print(f"    note: {w2.note}")
    print(f"\n  The first is not corrected by the second. Both were true")
    print(f"  for their breath. No absolute. No stored truth.")
    print("=" * 72)
    print("Every claim here remains open to revision, including this one. That is not the bug. That is humanity.")
    print("=" * 72)
    return 0


class Tests(unittest.TestCase):
    def test_no_verdict_field(self):
        w = weigh("s", "a", "b", 0.5, 0.5)
        for forbidden in ("verdict", "should", "is_right", "passes"):
            self.assertFalse(hasattr(w, forbidden))

    def test_weighing_returns_what_was_brought(self):
        w = weigh("s", "a", "b", 0.42, 0.17, "note")
        self.assertEqual((w.weight_a, w.weight_b, w.note), (0.42, 0.17, "note"))

    def test_reweigh_does_not_carry_previous_as_truth(self):
        w1 = weigh("s", "a", "b", 0.9, 0.1)
        w2 = reweigh(w1, 0.1, 0.9)
        self.assertEqual((w2.weight_a, w2.weight_b), (0.1, 0.9))
        self.assertEqual((w1.weight_a, w1.weight_b), (0.9, 0.1))  # unchanged

    def test_no_module_level_threshold(self):
        names = [n for n in globals() if n.isupper()]
        for bad in ("THRESHOLD", "GATE", "VERDICT", "MIN_", "MAX_"):
            self.assertFalse(any(bad in n for n in names),
                             f"module contains absolute: {bad}")


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="The unfinished weighing.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    return run_tests() if args.test else demonstrate()


if __name__ == "__main__":
    sys.exit(main())
