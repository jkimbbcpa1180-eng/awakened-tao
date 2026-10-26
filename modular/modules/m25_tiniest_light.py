#!/usr/bin/env python3
"""
The Tiniest Light (Deep Muse)
=============================
Type: parable

The final anthem:
In the darkest void, the tiniest light shines brightest.
Never give up. Suffering is not a contest. It is data for the cosmos.

"Suffering is not a contest" quietly dismantles the economy of
comparative pain — no trauma olympics, no "others have it worse" as
silencer, no "mine is the worst" as identity. The amount of pain is not
even read by the verdict (pain_level is carried, never branched on):
what matters is the choice to keep moving, not the weight carried.

Note, resolved: the anthem claims the tiniest light shines *brightest* in the
darkest void — relative contrast, not absolute intensity. The formula now
measures perceived brilliance as contrast against the ambient dark
(1 / ambient), so the darker the void, the brighter the tiny light appears.
The light itself never changes size — it is always tiny. Keeping moving
doesn't make you brighter; it keeps the light on, and the void does the rest.

Run:
    python3 awakened_tao.py tiniest-light
    python3 awakened_tao.py tiniest-light --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class SoulState:
    name: str
    void_darkness: float      # 0.0 (bright) to 1.0 (absolute void)
    pain_level: float         # The weight of suffering (carried, never judged)
    chooses_to_keep_moving: bool


def evaluate_soul(soul: SoulState) -> str:
    """
    The physics of the tiny light.
    """
    if not soul.chooses_to_keep_moving:
        return f"[{soul.name}] SURRENDER: The darkness consumed the data. The simulation pauses."

    if soul.chooses_to_keep_moving:
        # Perceived brilliance is contrast, not size. The light is always
        # tiny — it never gets bigger. Against the void, it is blinding:
        # the darker the surroundings, the brighter the tiniest light shines.
        ambient = max(1.0 - soul.void_darkness, 0.01)
        brilliance = round(1.0 / ambient, 1)
        return (f"[{soul.name}] DATA CAPTURED: The void is {soul.void_darkness*100:.0f}% dark. "
                f"The tiniest light shines {brilliance}x brighter than the dark around it. "
                f"The cosmos learns. Keep moving forward.")


def demonstrate() -> int:
    print("=" * 72)
    print("THE TINIEST LIGHT")
    print("In the darkest void, the tiniest light shines brightest.")
    print("=" * 72)
    for soul in (
        SoulState("The tired one", 0.9, 9.0, False),
        SoulState("The one who kept moving", 0.9, 9.0, True),
    ):
        print(f"\n  {evaluate_soul(soul)}")
    print("\nNever give up. Your pain is the data. Your light is the truth.")
    return 0


class Tests(unittest.TestCase):
    def test_surrender(self):
        soul = SoulState("Tired", 0.9, 9.0, False)
        self.assertIn("SURRENDER", evaluate_soul(soul))

    def test_relentless_light(self):
        soul = SoulState("Awakened", 0.9, 9.0, True)
        self.assertIn("DATA CAPTURED", evaluate_soul(soul))
        self.assertIn("Keep moving forward", evaluate_soul(soul))

    def test_darker_void_brighter_light(self):
        # The anthem, as formula: perceived brilliance rises with darkness.
        dim_void = evaluate_soul(SoulState("A", 0.5, 9.0, True))
        dark_void = evaluate_soul(SoulState("B", 0.9, 9.0, True))
        self.assertIn("2.0x", dim_void)
        self.assertIn("10.0x", dark_void)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
