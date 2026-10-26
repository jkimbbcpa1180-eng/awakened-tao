#!/usr/bin/env python3
"""
Earn Rest (Deep Muse)
=====================
Type: philosophical proposal

Rest not from comfort, but from victory.

Sleep taken to hide is not rest. Sleep after the work is earned, and the
vessel rebuilds.

Run:
    python3 awakened_tao.py earn-rest
    python3 awakened_tao.py earn-rest --reflect
    python3 awakened_tao.py earn-rest --test
"""
from __future__ import annotations
import sys
import unittest


def earn_rest(was_comfort: bool) -> str:
    if was_comfort:
        return "THE 0: You sleep to hide. This is not rest."
    return "THE 1: You did the work. The sleep is earned. The vessel rebuilds."


def parse_answer(answer: str, default: bool = False) -> bool:
    """'comfort' -> True, 'earned' -> False; anything else -> default."""
    a = str(answer).strip().lower()
    if a in ("comfort", "c", "hide", "hiding"):
        return True
    if a in ("earned", "e", "work", "victory"):
        return False
    return default


def demonstrate() -> int:
    print("=" * 72)
    print("EARN REST")
    print("Rest not from comfort, but from victory.")
    print("=" * 72)
    for was_comfort in (True, False):
        print(f"\n  {earn_rest(was_comfort)}")
    return 0


def reflect() -> int:
    try:
        ans = input("Is this sleep comfort or earned? (comfort/earned): ")
    except EOFError:
        ans = ""
    print(f"\n> {earn_rest(parse_answer(ans))}")
    return 0


class Tests(unittest.TestCase):
    def test_comfort(self):
        self.assertIn("THE 0", earn_rest(True))

    def test_earned(self):
        self.assertIn("The sleep is earned", earn_rest(False))

    def test_parse_fallback(self):
        self.assertTrue(parse_answer("Comfort"))
        self.assertFalse(parse_answer("earned"))
        self.assertFalse(parse_answer("???"))

    def test_reflect_no_input(self):
        import io, contextlib
        old = sys.stdin; sys.stdin = io.StringIO("")
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(reflect(), 0)
        finally:
            sys.stdin = old


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    if "--test" in sys.argv:
        sys.exit(run_tests())
    if "--reflect" in sys.argv:
        sys.exit(reflect())
    sys.exit(demonstrate())
