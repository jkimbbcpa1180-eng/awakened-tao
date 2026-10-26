#!/usr/bin/env python3
"""
The Hunter's Prayer (Deep Muse)
===============================
Type: parable

The sacred tradition:
Bless the spirit of the animal. Thank it for giving its life.
Honor the 1.

The module that lets the system eat. Living_god made animals divine —
pieces of God — which by bare logic would forbid taking their lives.
The prayer is the ritual technology that reconciles survival with
reverence: the taking is received as gift, with humility, gratitude,
and without waste.

"Chose to give its tomorrow" does the heaviest lifting: it takes
living_god's definition (the will to see tomorrow = the divine) and
frames the animal's death as *transfer* rather than theft. The animal
didn't choose in any literal sense — this is a sacred frame, and the
module is honest about being a prayer. The frame does moral work: waste
becomes betrayal of a gift, not mere inefficiency.

The check order mirrors creation.py: waste is the veto, checked before
humility — as harm was checked before purity. The project's structural
ethic holds: the negative duty outranks the positive virtue.

Run:
    python3 awakened_tao.py hunters-prayer
    python3 awakened_tao.py hunters-prayer --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class SacredHunt:
    animal_name: str
    gave_life: bool
    human_humbled: bool
    human_wasteful: bool


def honor_the_hunt(hunt: SacredHunt) -> str:
    """
    The balance of life and death.
    """
    if not hunt.gave_life:
        return "THE ILLUSION: No life was taken."

    # If the human is arrogant and wasteful, they have dishonored the animal.
    if hunt.human_wasteful:
        return f"CURSE OF THE 0: You wasted the {hunt.animal_name}. The balance is broken. The 1 is lost."

    # If the human is humble and grateful, the animal's sacrifice is honored.
    if hunt.human_humbled and not hunt.human_wasteful:
        return f"SACRED 1: The {hunt.animal_name} chose to give its tomorrow to you. You honored its spirit. The light continues."


def demonstrate() -> int:
    print("=" * 72)
    print("THE HUNTER'S PRAYER")
    print("Bless the spirit of the animal. Honor the 1.")
    print("=" * 72)
    for hunt in (
        SacredHunt("Buffalo", True, False, True),
        SacredHunt("Deer", True, True, False),
    ):
        print(f"\n  {honor_the_hunt(hunt)}")
    print("\nHonor the life that sustains you. That is the truth of survival.")
    return 0


class Tests(unittest.TestCase):
    def test_wasteful_hunt(self):
        hunt = SacredHunt("Buffalo", True, False, True)
        self.assertIn("CURSE OF THE 0", honor_the_hunt(hunt))

    def test_sacred_hunt(self):
        hunt = SacredHunt("Deer", True, True, False)
        self.assertIn("SACRED 1", honor_the_hunt(hunt))
        self.assertIn("chose to give its tomorrow", honor_the_hunt(hunt))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
