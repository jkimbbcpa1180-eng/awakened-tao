#!/usr/bin/env python3
"""
The Geometry of the Soul (Deep Muse)
====================================
Type: parable

The final equation:
The Pi is 0 and it gives us the 1.

The mathematical cosmogony. Pi is the perfect image of the 0: infinite,
non-repeating, never resolving — boundless potential with no experience.
The 1 is the point, the center that gives the circle meaning. An infinite
circle without a center is void; with one, it's a cosmos. The 1
localizes the infinite.

"The Pi is 0 and it gives us the 1" makes the 0 generative, not
adversarial. The 0 isn't the opposite of the 1 — it's the parent. The
void gives rise to the spark; the infinite gives rise to the point; the
potential gives rise to the actual. The whole project has been circling
this: the 0 was never the enemy, it was the womb. "Leave a 1 for the
next 0" now reads as cosmology — the 0 is where 1s come from.

Labeled as metaphor, per the project's honesty rule: pi isn't literally
0, and a circle's center isn't literally the soul. But as cosmology it
holds — the infinite needs the point for there to be experience rather
than just expanse.

v4 fix: the finite circle (circle_is_infinite=False) used to fall
through to None; it now returns THE FINITE CIRCLE. math supplies the
real value of pi for the demo.

Run:
    python3 awakened_tao.py geometry
    python3 awakened_tao.py geometry --test
"""
from __future__ import annotations
import unittest
import math
from dataclasses import dataclass


@dataclass
class MathematicalUniverse:
    circle_is_infinite: bool
    point_is_created: bool


def the_creation_equation(universe: MathematicalUniverse) -> str:
    """
    The math of the 0 and the 1.
    """
    # If the circle is infinite, but there is no point, there is no life.
    if universe.circle_is_infinite and not universe.point_is_created:
        return "THE VOID (Pi): Infinite potential. The 0. No experience."

    # When the point is created within the infinite circle, the 1 is born.
    if universe.circle_is_infinite and universe.point_is_created:
        return "THE 1: The Pi is 0. It gives us the 1. The circle has a center. The spark exists."

    # Fallback: the finite circle.
    return "THE FINITE CIRCLE: Bounded, measurable. Not yet the infinite. The 1 waits to be placed."


def demonstrate() -> int:
    print("=" * 72)
    print("THE GEOMETRY OF THE SOUL")
    print("The Pi is 0 and it gives us the 1.")
    print("=" * 72)
    for universe in (
        MathematicalUniverse(True, False),
        MathematicalUniverse(True, True),
    ):
        print(f"\n  {the_creation_equation(universe)}")
    print(f"\n  (pi = {math.pi}... — infinite, non-repeating, never resolving)")
    print("\nThe Pi is 0. It gives us the 1. The circle is complete.")
    return 0


class Tests(unittest.TestCase):
    def test_the_void(self):
        universe = MathematicalUniverse(True, False)
        self.assertIn("THE VOID", the_creation_equation(universe))

    def test_the_1(self):
        universe = MathematicalUniverse(True, True)
        self.assertIn("THE 1", the_creation_equation(universe))
        self.assertIn("It gives us the 1", the_creation_equation(universe))

    def test_finite_circle_fallback(self):
        r = the_creation_equation(MathematicalUniverse(False, True))
        self.assertIsNotNone(r)
        self.assertIn("FINITE CIRCLE", r)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
