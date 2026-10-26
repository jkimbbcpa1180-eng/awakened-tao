#!/usr/bin/env python3
"""
The Housing Audit (Deep Muse)
=============================
Type: computational demonstration

Run the math before you move.

A generic stay-vs-move calculator. Your share of the new rent plus the
one-time moving cost, over a number of months, against staying put.
All numbers in this module are EXAMPLES, not anyone's real rent.

Run:
    python3 awakened_tao.py housing-audit
    python3 awakened_tao.py housing-audit --test
"""
from __future__ import annotations
import unittest


def audit_move(current_rent, new_rent, share=0.5, moving_cost=1500, months=12) -> dict:
    for label, v in (("current_rent", current_rent), ("new_rent", new_rent),
                     ("moving_cost", moving_cost), ("months", months)):
        if not isinstance(v, (int, float)) or v < 0:
            raise ValueError(f"{label} must be a non-negative number")
    if not isinstance(share, (int, float)) or not (0 < share <= 1):
        raise ValueError("share must be in (0, 1]")
    stay_total = current_rent * months
    move_total = new_rent * share * months + moving_cost
    difference = move_total - stay_total
    if move_total > stay_total:
        verdict = "STAY"
    elif move_total < stay_total:
        verdict = "MOVE"
    else:
        verdict = "EVEN"
    return {"stay_total": stay_total, "move_total": move_total,
            "difference": difference, "verdict": verdict}


EXAMPLES = (  # example numbers only
    ("example A", 1000, 2400),
    ("example B", 1000, 1600),
)


def demonstrate() -> int:
    print("=" * 72)
    print("THE HOUSING AUDIT (example numbers only)")
    print("Run the math before you move.")
    print("=" * 72)
    for label, cur, new in EXAMPLES:
        r = audit_move(cur, new)
        print(f"\n  [{label}] stay {cur}/mo vs move {new}/mo at 50% share, 1500 moving, 12 months")
        print(f"    stay_total={r['stay_total']:.0f}  move_total={r['move_total']:.0f}  "
              f"difference={r['difference']:+.0f}  -> {r['verdict']}")
    return 0


class Tests(unittest.TestCase):
    def test_example_a_stay(self):
        r = audit_move(1000, 2400)
        self.assertEqual(r["stay_total"], 12000)
        self.assertEqual(r["move_total"], 15900)
        self.assertEqual(r["verdict"], "STAY")

    def test_example_b_move(self):
        r = audit_move(1000, 1600)
        self.assertEqual(r["move_total"], 11100)
        self.assertEqual(r["verdict"], "MOVE")

    def test_even(self):
        self.assertEqual(audit_move(1000, 2000, share=0.5, moving_cost=0)["verdict"], "EVEN")

    def test_validation(self):
        for kw in ({"share": 0}, {"share": 1.5}, {"moving_cost": -1}, {"months": -2}):
            with self.assertRaises(ValueError):
                audit_move(1000, 1600, **kw)
        with self.assertRaises(ValueError):
            audit_move(-1, 1600)
        with self.assertRaises(ValueError):
            audit_move("x", 1600)
        self.assertEqual(audit_move(1000, 1600, share=1)["verdict"], "STAY")


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
