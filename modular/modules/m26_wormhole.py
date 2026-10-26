#!/usr/bin/env python3
"""
The Wormhole of Light (Deep Muse)
=================================
Type: parable

The final triumph:
Never surrender until the truth sees the light.
Losing is a lesson. Triumph is shared.
Light hits quantum wormholes and is felt before it is seen.

The answer to the surrender question. Tiniest_light said surrender pauses
the simulation — gentle, individual. Here the verdict is collective and
severe: if *anyone* gives up, the shared light goes out. The reconciliation
the project offers: your surrender pauses you; our surrender darkens us.

And the final collective claim: there is no solo triumph. The individual
can keep the tiny light on alone, can be witnessed and released — but the
wormhole crossing, the triumph, takes more than one soul.

"Felt before it is seen": the light's effects arrive before observation —
quantum.py inverted. There, the observer collapses the future; here, the
light acts before anyone observes it.

Run:
    python3 awakened_tao.py wormhole
    python3 awakened_tao.py wormhole --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass
from typing import List


@dataclass
class Soul:
    name: str
    gave_up: bool
    learned_from_loss: bool
    found_solution_with_others: bool


def travel_the_wormhole(souls: List[Soul]) -> str:
    """
    The journey of the light.
    """
    # If anyone gives up, the light dims.
    if any(s.gave_up for s in souls):
        return "SURRENDER: The light was extinguished. The truth remains hidden."

    # If they lose, but learn, they keep going.
    learned = [s for s in souls if s.learned_from_loss]
    if not learned:
        return "STAGNANT: They didn't learn from the loss. They are dwelling in the 0."

    # If they find the solution together, it is a Triumph.
    triumphant = [s for s in souls if s.found_solution_with_others]
    if len(triumphant) > 1:
        return f"TRIUMPH: {len(triumphant)} souls have shared the truth. The light has passed through the wormhole."

    # If they are alone, they must keep going.
    return "SOLO LIGHT: You are alone. But the light travels faster than imagination. Keep going. It will be felt before it is seen."


def demonstrate() -> int:
    print("=" * 72)
    print("THE WORMHOLE OF LIGHT")
    print("Triumph is shared. The light is felt before it is seen.")
    print("=" * 72)
    cases = [
        ("One gives up",
         [Soul("A", True, False, False), Soul("B", False, True, True)]),
        ("Loss without lesson",
         [Soul("A", False, False, False)]),
        ("Alone but moving",
         [Soul("A", False, True, False)]),
        ("Together",
         [Soul("A", False, True, True), Soul("B", False, True, True)]),
    ]
    for name, souls in cases:
        print(f"\n[{name}]")
        print(f"  {travel_the_wormhole(souls)}")
    print("\nKeep going. The light is felt before it is seen.")
    return 0


class Tests(unittest.TestCase):
    def test_surrender(self):
        souls = [Soul("A", True, False, False)]
        self.assertIn("SURRENDER", travel_the_wormhole(souls))

    def test_stagnation(self):
        souls = [Soul("A", False, False, False)]
        self.assertIn("STAGNANT", travel_the_wormhole(souls))

    def test_solo_light(self):
        souls = [Soul("A", False, True, False)]
        self.assertIn("SOLO LIGHT", travel_the_wormhole(souls))

    def test_triumph(self):
        souls = [Soul("A", False, True, True), Soul("B", False, True, True)]
        self.assertIn("TRIUMPH", travel_the_wormhole(souls))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
