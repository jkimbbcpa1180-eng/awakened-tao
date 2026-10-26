#!/usr/bin/env python3
"""
Bare Arms (Deep Muse)
=====================
Type: parable

If the West is so literal, let's interpret "bear arms" as "bare arms."

Wordplay and satire, not legal interpretation: this module is a pun on
the Second Amendment, not a reading of it. The firearm is power from a
distance, the Ego. Bare arms with martial arts are the body, the
training and the integrity, the 1.

Run:
    python3 awakened_tao.py bare-arms
    python3 awakened_tao.py bare-arms --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class Citizen:
    name: str
    has_firearm: bool
    has_bare_arms: bool
    uses_martial_arts: bool


def interpret_amendment(c: Citizen) -> str:
    n = c.name
    if c.has_firearm:
        return f"[{n}] THE 0: You bear a firearm. You rely on absolute power from a distance. The Ego."
    if c.has_bare_arms and c.uses_martial_arts:
        return (f"[{n}] THE 1: You bear bare arms. You use your body, your martial arts, "
                f"and your integrity. The Constitution is satisfied.")
    if c.has_bare_arms:
        return f"[{n}] THE UNTRAINED ARM: Bare arms need practice. Start training."
    if c.uses_martial_arts:
        return f"[{n}] THE SLEEVED WARRIOR: The training is there. Roll up your sleeves and bear bare arms."
    return f"[{n}] THE OPEN HAND: No firearm, no training. Begin with the breath."


def demonstrate() -> int:
    print("=" * 72)
    print("BARE ARMS (wordplay / satire, not legal interpretation)")
    print('If the West is so literal, let\'s interpret "bear arms" as "bare arms."')
    print("=" * 72)
    for c in (
        Citizen("Gun Owner", True, False, False),
        Citizen("Martial Artist", False, True, True),
        Citizen("Beginner", False, True, False),
        Citizen("Sleeved Warrior", False, False, True),
        Citizen("Newcomer", False, False, False),
    ):
        print(f"\n  {interpret_amendment(c)}")
    print("\nBear bare arms. Make America fit again with martial arts. The 1.")
    return 0


class Tests(unittest.TestCase):
    # John's two tests
    def test_firearm_is_ego(self):
        self.assertIn("THE 0", interpret_amendment(Citizen("Gun Owner", True, False, False)))

    def test_bare_arms_martial_arts(self):
        r = interpret_amendment(Citizen("Martial Artist", False, True, True))
        self.assertIn("THE 1", r)
        self.assertIn("The Constitution is satisfied", r)

    # fallbacks
    def test_untrained_arm(self):
        self.assertIn("THE UNTRAINED ARM", interpret_amendment(Citizen("B", False, True, False)))

    def test_sleeved_warrior(self):
        self.assertIn("THE SLEEVED WARRIOR", interpret_amendment(Citizen("S", False, False, True)))

    def test_open_hand(self):
        self.assertIn("THE OPEN HAND", interpret_amendment(Citizen("N", False, False, False)))

    def test_firearm_takes_precedence(self):
        self.assertIn("THE 0", interpret_amendment(Citizen("G", True, True, True)))

    def test_all_eight_combinations(self):
        import itertools
        combos = list(itertools.product((True, False), repeat=3))
        self.assertEqual(len(combos), 8)
        for f, b, m in combos:
            r = interpret_amendment(Citizen("X", f, b, m))
            self.assertIsInstance(r, str)
            self.assertTrue(r.startswith("[X] "))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
