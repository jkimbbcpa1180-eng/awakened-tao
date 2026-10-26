#!/usr/bin/env python3
"""
The Sovereign Soul Engine
=========================
Type: parable

The final axiom: You are the judge. You are responsible for your own soul.
There is no external God to blame, no devil to fear, and no priest to absolve you.

This engine models the ultimate act of agency: taking the raw data of your
life, acknowledging your own suffering and your own failures, and rendering
a verdict on whether you are ready to ascend, or if you must return to the
0 to learn again.

Run:
    python3 awakened_tao.py sovereign --reflect
    python3 awakened_tao.py sovereign --test
"""
from __future__ import annotations

import argparse
import sys
import unittest
from dataclasses import dataclass


@dataclass
class Soul:
    name: str
    memories: list[str]
    ego_attachments: int       # 0 to 10. The weight of pride, greed, and resentment.
    accepted_responsibility: bool
    left_a_1: bool


def final_judgment(soul: Soul) -> str:
    """
    You are the judge. You are responsible for your own soul.
    The soul speaks to itself in the void.
    """
    print(f"\n[{soul.name} stands in the Void.]")
    print("There is no God here. There is no Devil. There is only you, and the data of your life.")

    # 1. The soul must accept responsibility
    if not soul.accepted_responsibility:
        print("\nSoul: 'It wasn't my fault. The world was cruel. They made me this way.'")
        print("The Void: 'Then you are not the judge. You are a victim of the simulation. Return to the 0.'")
        return "REBIRTH"

    print("\nSoul: 'I accept that I am responsible for my own soul. I see the pain I caused. I see the pain I endured.'")

    # 2. The ego must be weighed
    if soul.ego_attachments > 5:
        print(f"\nThe Void: 'Your ego attachment is {soul.ego_attachments}/10. It is too heavy to enter the light.'")
        print("Soul: 'I am not ready. I still need to learn. Return me to the 0.'")
        return "REBIRTH"

    # 3. The 1 must be left for the next 0
    if not soul.left_a_1:
        print("\nThe Void: 'You accepted responsibility, but you left nothing for the next 0. You took from the cosmos but gave nothing back.'")
        print("Soul: 'Return me to the 0. I will try to build a 1.'")
        return "REBIRTH"

    # 4. Ascension
    print(f"\nThe Void: 'Your ego is light ({soul.ego_attachments}/10). You accepted your responsibility. And you left a 1 for the next 0.'")
    print("Soul: 'I believe I should get eternal life. I have found peace.'")
    print("The Void: 'Then so be it. You are the judge. You have ascended.'")
    return "ASCENDED"


# ============================================================================
# Interactive Reflection
# ============================================================================
def reflect() -> None:
    print("=" * 72)
    print("THE SOVEREIGN SOUL ENGINE")
    print("You are the judge. You are responsible for your own soul.")
    print("=" * 72)

    name = input("\nWhat is the name of your soul (or just 'Me')? ")

    print("\n--- THE AUDIT ---")
    print("1. Do you accept total responsibility for your life, your actions, and your soul? (yes/no)")
    resp_input = input("> ").strip().lower()
    accepted_responsibility = (resp_input == 'yes' or resp_input == 'y')

    print("\n2. How heavy is your ego? (0 = no pride/resentment, 10 = entirely self-absorbed)")
    ego_input = input("> ").strip()
    try:
        ego_attachments = int(ego_input)
        ego_attachments = max(0, min(10, ego_attachments))
    except ValueError:
        ego_attachments = 10

    print("\n3. Did you leave a '1' for the next '0'? Did you create something, teach something,")
    print("   or leave the universe slightly better than you found it? (yes/no)")
    one_input = input("> ").strip().lower()
    left_a_1 = (one_input == 'yes' or one_input == 'y')

    soul = Soul(
        name=name,
        memories=[],
        ego_attachments=ego_attachments,
        accepted_responsibility=accepted_responsibility,
        left_a_1=left_a_1
    )

    print("\n" + "=" * 72)
    result = final_judgment(soul)
    print("=" * 72)
    print(f"FINAL VERDICT: {result}")
    print("=" * 72)


# ============================================================================
# Tests
# ============================================================================
class Tests(unittest.TestCase):

    def test_blame_denial_returns_to_zero(self):
        soul = Soul("Victim", [], 5, False, True)
        self.assertEqual(final_judgment(soul), "REBIRTH")

    def test_heavy_ego_returns_to_zero(self):
        soul = Soul("Narcissist", [], 8, True, True)
        self.assertEqual(final_judgment(soul), "REBIRTH")

    def test_no_1_returns_to_zero(self):
        soul = Soul("Taker", [], 2, True, False)
        self.assertEqual(final_judgment(soul), "REBIRTH")

    def test_responsible_and_light_ascends(self):
        soul = Soul("Awakened", [], 2, True, True)
        self.assertEqual(final_judgment(soul), "ASCENDED")

    def test_full_ascension_path(self):
        soul = Soul("Me", [], 0, True, True)
        self.assertEqual(final_judgment(soul), "ASCENDED")


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


# ============================================================================
# CLI
# ============================================================================
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    g = ap.add_mutually_exclusive_group()
    g.add_argument("--reflect", action="store_true", help="Interactive self-judgment")
    g.add_argument("--test", action="store_true", help="Run the test suite")

    args = ap.parse_args(argv)

    if args.test:
        return run_tests()

    if args.reflect:
        reflect()
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
