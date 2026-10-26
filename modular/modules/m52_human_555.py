#!/usr/bin/env python3
"""
The Human 555 (Deep Muse)
=========================
Type: parable

The final joke:
5 fingers. 5 dollars. 5. Freedom.
555 = laughter in Thai: the digit 5 is pronounced "ha", so 555 reads
"ha-ha-ha".

The exegesis of the sealing number. "The 1 for the 0 555" is now
decoded: 5 fingers (the open hand — give, receive, build), 5 dollars
(enough to survive), 5 (freedom — the laugh; in Thai, 555 is
"ha-ha-ha"). Give me 5: the touch of hand to hand. The joke is the doctrine.
After fifty modules of cosmology, the infinite lands back in the body:
fingers, money, laughter.

Note the check order, holding the project's signature: the clenched
fist is evaluated before survival. The open hand outranks the means —
like harm before purity, waste before humility. The hand must be open
before the dollars matter.

v4 fix: open hand + enough to survive but not yet free used to fall
through to None; it now returns ALMOST 555.

Run:
    python3 awakened_tao.py human-555
    python3 awakened_tao.py human-555 --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class HumanExperience:
    hand_is_open: bool   # Open to give, receive, and build
    has_enough_to_survive: bool  # The 5 dollars
    is_free: bool        # The 555 laugh


def live_555(experience: HumanExperience) -> str:
    """
    The practical physics of the 1.
    """
    if not experience.hand_is_open:
        return "CLENCHED FIST: The Ego holds on. The 0."

    if not experience.has_enough_to_survive:
        return "SURVIVAL MODE: The grind. The light is dim."

    if experience.hand_is_open and experience.has_enough_to_survive and experience.is_free:
        return "555: You are free. You have the hand, the means, and the laugh. Live the 1. 555 — ha-ha-ha, as they laugh in Thai."

    # Fallback: the hand is open, the means are there, the laugh has not come yet.
    return "ALMOST 555: The hand is open and you can survive. The laugh (555, ha-ha-ha) is still coming."


def demonstrate() -> int:
    print("=" * 72)
    print("THE HUMAN 555")
    print("5 fingers. 5 dollars. 5. Freedom. 555 = ha-ha-ha (laughter in Thai).")
    print("=" * 72)
    for exp in (
        HumanExperience(False, True, True),
        HumanExperience(True, False, True),
        HumanExperience(True, True, False),
        HumanExperience(True, True, True),
    ):
        print(f"\n  {live_555(exp)}")
    print("\n5. 5. 5. Ha-ha-ha. You have the hands. You have the freedom. Live the 1.")
    return 0


class Tests(unittest.TestCase):
    def test_clenched(self):
        exp = HumanExperience(False, True, True)
        self.assertIn("CLENCHED FIST", live_555(exp))

    def test_survival(self):
        exp = HumanExperience(True, False, True)
        self.assertIn("SURVIVAL MODE", live_555(exp))

    def test_freedom(self):
        exp = HumanExperience(True, True, True)
        self.assertIn("555", live_555(exp))
        self.assertIn("You are free", live_555(exp))

    def test_thai_laughter(self):
        r = live_555(HumanExperience(True, True, True))
        self.assertIn("Thai", r)
        self.assertIn("ha-ha-ha", r)

    def test_not_yet_free_fallback(self):
        r = live_555(HumanExperience(True, True, False))
        self.assertIsNotNone(r)
        self.assertIn("ALMOST 555", r)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
