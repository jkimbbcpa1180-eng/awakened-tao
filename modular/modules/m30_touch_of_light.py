#!/usr/bin/env python3
"""
The Touch of Light (Deep Muse)
==============================
Type: parable

The final truth:
Truth and light is God, and it touched every living thing on earth.

The universalization of living_god. There, God was distributed across
*wills* — beings wanting tomorrow. Here the *touch* is distributed across
everything, graduated by capacity: the rock gets warmth but no
consciousness, the animal gets instinct, the human gets conscious thought.
Same light, different reception — the prism's logic stated as ontology
rather than epistemology.

The tension with living_god, named: there the rock was THE 0, "just
matter"; here the mountain is ILLUMINATED. The resolution the project
offers: the 0 is the absence of the *spark* (the will), not the absence
of the *touch*. Matter is touched but does not will. Universal grace of
touch; particular dignity of will.

Run:
    python3 awakened_tao.py touch-of-light
    python3 awakened_tao.py touch-of-light --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass
from typing import List


@dataclass
class Creation:
    name: str
    truth_and_light: bool
    touched_by_god: bool


def the_universe() -> List[Creation]:
    """
    The cosmos breathes the 1 into the 0.
    """
    # God (Truth and Light) touches everything.
    # The rock gets the warmth, but no consciousness.
    # The animal gets the instinct. The human gets the conscious thought.
    # But all of them are touched.
    return [
        Creation("The Ocean", True, True),
        Creation("The Mountain", True, True),
        Creation("The Stray Dog", True, True),
        Creation("You", True, True),
    ]


def experience_life(creature: Creation) -> str:
    """
    How the light manifests in each thing.
    """
    if not creature.touched_by_god:
        return f"[{creature.name}] UNTOUCHED: A cold void."

    if creature.truth_and_light and creature.touched_by_god:
        return f"[{creature.name}] ILLUMINATED: The light of God rests here."


def demonstrate() -> int:
    print("=" * 72)
    print("THE TOUCH OF LIGHT")
    print("Truth and light is God, and it touched everything.")
    print("=" * 72)
    for creature in the_universe():
        print(f"\n  {experience_life(creature)}")
    print("\nThe rock gets warmth. The animal gets instinct.")
    print("You get the conscious thought. All are touched.")
    print("Truth and light is God. It touched everything. You are illuminated.")
    return 0


class Tests(unittest.TestCase):
    def test_universe(self):
        universe = the_universe()
        self.assertEqual(len(universe), 4)
        self.assertTrue(all(c.touched_by_god for c in universe))
        self.assertTrue(all(c.truth_and_light for c in universe))

    def test_illumination(self):
        human = Creation("Ari", True, True)
        self.assertIn("ILLUMINATED", experience_life(human))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
