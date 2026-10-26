#!/usr/bin/env python3
"""
The Shield vs. the Gun (Deep Muse)
==================================
Type: philosophical proposal

The shield requires a true warrior. The gun creates a tyrant.

Law enforcement as the 0 and the 1: the one who carries only the gun
holds absolute power and enforces the 000; the one who carries the
shield, trained and uncorrupted, risks their own body and becomes the
Bodhisattva of the law. Every combination has a verdict; no path is
silent.

Run:
    python3 awakened_tao.py shield-vs-gun
    python3 awakened_tao.py shield-vs-gun --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class LawEnforcement:
    name: str
    carries_gun: bool
    carries_shield: bool
    is_corrupted: bool
    is_a_warrior: bool


def evaluate_law_enforcement(agency: LawEnforcement) -> str:
    n = agency.name
    if agency.carries_gun and not agency.carries_shield:
        msg = (f"[{n}] THE 0: You carry the gun. Absolute power corrupts. "
               f"You become the Anti-Cosmos. You enforce the 000.")
        if agency.is_corrupted:
            msg += " The corruption is already complete."
        return msg
    if agency.carries_gun and agency.carries_shield:
        if agency.is_corrupted:
            return (f"[{n}] THE CORRUPTED BALANCE: The shield is a mask and the gun is the rule. "
                    f"Integrity first, or there is no balance.")
        return f"[{n}] THE BALANCE: The shield first. The gun locked away as the last resort."
    if agency.carries_shield:
        if agency.is_corrupted:
            return f"[{n}] THE HOLLOW SHIELD: A shield without integrity is just armor."
        if agency.is_a_warrior:
            return (f"[{n}] THE 1: You carry the shield. You use martial arts. "
                    f"You risk your own body. You are the Bodhisattva of the law.")
        return f"[{n}] THE UNTRAINED SHIELD: The shield requires a true warrior. Train first."
    return f"[{n}] THE OPEN HAND: No weapon, no shield. Authority rests on trust alone."


def demonstrate() -> int:
    print("=" * 72)
    print("THE SHIELD VS. THE GUN")
    print("=" * 72)
    for a in (
        LawEnforcement("Gun Agency", True, False, False, False),
        LawEnforcement("Shield Warrior", False, True, False, True),
        LawEnforcement("Balanced Agency", True, True, False, True),
        LawEnforcement("Hollow Agency", False, True, True, True),
        LawEnforcement("Recruit", False, True, False, False),
        LawEnforcement("Community Watch", False, False, False, False),
    ):
        print(f"\n  {evaluate_law_enforcement(a)}")
    print("\nThe shield requires a true warrior. The gun creates a tyrant.")
    return 0


class Tests(unittest.TestCase):
    # John's two tests
    def test_gun_creates_tyrant(self):
        a = LawEnforcement("Gun Agency", True, False, False, False)
        self.assertIn("THE 0", evaluate_law_enforcement(a))

    def test_shield_warrior(self):
        a = LawEnforcement("Shield Warrior", False, True, False, True)
        r = evaluate_law_enforcement(a)
        self.assertIn("THE 1", r)
        self.assertIn("Bodhisattva of the law", r)

    # fallbacks
    def test_balance(self):
        self.assertIn("THE BALANCE", evaluate_law_enforcement(LawEnforcement("B", True, True, False, True)))

    def test_corrupted_balance(self):
        self.assertIn("THE CORRUPTED BALANCE", evaluate_law_enforcement(LawEnforcement("B", True, True, True, True)))

    def test_corrupted_gun(self):
        r = evaluate_law_enforcement(LawEnforcement("G", True, False, True, False))
        self.assertIn("THE 0", r)
        self.assertIn("corruption is already complete", r)

    def test_hollow_shield(self):
        self.assertIn("THE HOLLOW SHIELD", evaluate_law_enforcement(LawEnforcement("H", False, True, True, True)))
        self.assertIn("THE HOLLOW SHIELD", evaluate_law_enforcement(LawEnforcement("H", False, True, True, False)))

    def test_untrained_shield(self):
        self.assertIn("THE UNTRAINED SHIELD", evaluate_law_enforcement(LawEnforcement("U", False, True, False, False)))

    def test_open_hand(self):
        for c in (True, False):
            for w in (True, False):
                self.assertIn("THE OPEN HAND", evaluate_law_enforcement(LawEnforcement("O", False, False, c, w)))

    def test_no_none_path(self):
        import itertools
        for g, s, c, w in itertools.product((True, False), repeat=4):
            r = evaluate_law_enforcement(LawEnforcement("X", g, s, c, w))
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
