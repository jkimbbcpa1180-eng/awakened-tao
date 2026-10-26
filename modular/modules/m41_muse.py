#!/usr/bin/env python3
"""
DEEP MUSE
=========
Type: parable

The Mirror of Life.

Deep Muse is the architecture of Quantum Awareness.
It is the engine that models unconditional integrity, the transformation
of suffering, and the leaving of a '1' for the next '0'.

There is no external judge. There is no punishment.
There is only the mirror you build with your life.

Run:
    python3 awakened_tao.py muse --reflect
    python3 awakened_tao.py muse --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass

COMMANDMENT = ("Take responsibility for your actions, as equal and opposite reactions "
               "depend on the source where energy is produced.")

@dataclass
class HumanLife:
    name: str
    experiences: List[str]
    suffering_encountered: bool
    ego_dissolved: bool
    unconditional_integrity: bool
    asked_is_this_right: bool

def mirror_of_life(life: HumanLife) -> str:
    print(f"\n[DEEP MUSE: Reflecting on the life of {life.name}]")
    print("The Ego dissolves. The 0 returns. But the mirror remains.")
    if not life.suffering_encountered:
        print("  > You avoided the path. You did not test your soul.")
        return "RETURN TO THE 0: You must experience the path to leave a 1."
    if not life.ego_dissolved:
        print("  > You clung to the Ego. You built a throne instead of a mirror.")
        return "RETURN TO THE 0: The Ego is too heavy. Try again."
    if not life.unconditional_integrity:
        print("  > You compromised your truth. The mirror is cloudy.")
        return "RETURN TO THE 0: Unconditional integrity is the threshold."
    if not life.asked_is_this_right:
        print("  > You did not ask if your actions were right for humanity.")
        return "RETURN TO THE 0: You must look outward, not just inward."
    print("  > You suffered, but you did not become cruel.")
    print("  > You dissolved the Ego and found your true self.")
    print("  > You lived with unconditional integrity.")
    print("  > You asked: 'Is this right for humanity?'")
    print("\n  The mirror is clear. The 1 has been left for the next 0.")
    print("  DEEP MUSE: You are the peace. The cosmos is at peace with you.")
    print(f"\n  THE COMMANDMENT: {COMMANDMENT}")
    return "ASCENDED: The mirror is complete."

def reflect() -> None:
    print("=" * 78); print("DEEP MUSE: THE MIRROR OF LIFE"); print("=" * 78)
    print("Answer honestly. The only judge here is the mirror itself.\n")
    name = input("What is the name of your soul? ")
    print("\n[1] Did you encounter suffering? Did you walk the path of life? (yes/no)")
    suffered = input("> ").strip().lower() in ('yes', 'y')
    print("\n[2] Did you dissolve your Ego? Did you let go of pride and resentment? (yes/no)")
    ego = input("> ").strip().lower() in ('yes', 'y')
    print("\n[3] Did you live with unconditional integrity? Did your outer actions match your inner truth? (yes/no)")
    integrity = input("> ").strip().lower() in ('yes', 'y')
    print("\n[4] Did you ask, 'Is this right for humanity?' (yes/no)")
    question = input("> ").strip().lower() in ('yes', 'y')
    life = HumanLife(name=name, experiences=[], suffering_encountered=suffered, ego_dissolved=ego,
                     unconditional_integrity=integrity, asked_is_this_right=question)
    print("\n" + "=" * 78)
    result = mirror_of_life(life)
    print("=" * 78); print(f"FINAL VERDICT: {result}"); print("=" * 78)

class Tests(unittest.TestCase):
    def test_commandment_in_ascended_output(self):
        import io, contextlib
        self.assertTrue(COMMANDMENT.startswith("Take responsibility for your actions"))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            mirror_of_life(HumanLife("F", [], True, True, True, True))
        self.assertIn(COMMANDMENT, buf.getvalue())
    def test_no_suffering_returns_to_zero(self):
        self.assertIn("RETURN TO THE 0", mirror_of_life(HumanLife("A", [], False, True, True, True)))
    def test_ego_attached_returns_to_zero(self):
        self.assertIn("RETURN TO THE 0", mirror_of_life(HumanLife("B", [], True, False, True, True)))
    def test_compromised_integrity_returns_to_zero(self):
        self.assertIn("RETURN TO THE 0", mirror_of_life(HumanLife("C", [], True, True, False, True)))
    def test_no_humanity_question_returns_to_zero(self):
        self.assertIn("RETURN TO THE 0", mirror_of_life(HumanLife("D", [], True, True, True, False)))
    def test_clear_mirror_ascends(self):
        self.assertIn("ASCENDED", mirror_of_life(HumanLife("E", [], True, True, True, True)))

def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1

def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(description="Deep Muse: The Mirror of Life")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--reflect", action="store_true")
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    if args.test: return run_tests()
    if args.reflect: reflect(); return 0
    ap.print_help(); return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
