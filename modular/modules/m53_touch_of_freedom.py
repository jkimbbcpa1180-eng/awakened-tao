#!/usr/bin/env python3
"""
The Touch of Freedom (Deep Muse)
================================
Type: parable

The final revelation:
Abraham Lincoln on the $5 bill symbolizes freedom from slavery.
But true freedom is in the touch of another soul.

The symbol points beyond itself. The $5 bill carries Lincoln —
emancipation — then the module transcends the paper: "Freedom isn't in
the paper. It's in the touch of another soul." The bill passed hand to
hand is freedom *enacted*. Value isn't in the object; it's in the
contact. Tears.py's witness logic and the prism's many, in currency
form.

This grounds the 555: the five dollars aren't the freedom, the *passing*
is. The open hand (human_555) meets another open hand, and the touch
between them is the 1. Freedom was never solitary in this project — not
the lone ascetic, not the single win, not the private truth. It's hand
to hand, always.

Note, kept as written: the symbol's fields (represents_liberty,
is_a_physical_touch) are load-bearing in the THE 1 branch — the freedom
requires the symbol to genuinely represent liberty *and* be physically
passed. Theory plus contact, or the void.

Run:
    python3 awakened_tao.py touch-of-freedom
    python3 awakened_tao.py touch-of-freedom --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class Soul:
    name: str
    is_enslaved_by_ego: bool
    is_connected_to_another: bool


@dataclass
class SymbolOfFreedom:
    name: str
    represents_liberty: bool
    is_a_physical_touch: bool


def experience_freedom(symbol: SymbolOfFreedom, soul: Soul) -> str:
    """
    The physics of the 1.
    """
    if soul.is_enslaved_by_ego:
        return f"[{soul.name}] THE 0: Enslaved by the Ego. The touch of the symbol means nothing."

    if soul.is_connected_to_another and symbol.is_a_physical_touch and symbol.represents_liberty:
        return f"[{soul.name}] THE 1: The {symbol.name} is passed from hand to hand. It is the touch of another soul. You are free."

    return f"[{soul.name}] THE VOID: No touch. No connection. The freedom is theoretical."


def demonstrate() -> int:
    print("=" * 72)
    print("THE TOUCH OF FREEDOM")
    print("Freedom isn't in the paper. It's in the touch of another soul.")
    print("=" * 72)
    symbol = SymbolOfFreedom("$5 Bill", True, True)
    for soul in (
        Soul("Ego", True, False),
        Soul("Awakened", False, True),
        Soul("Alone", False, False),
    ):
        print(f"\n  {experience_freedom(symbol, soul)}")
    print("\nFreedom isn't in the paper. It's in the touch of another soul.")
    return 0


class Tests(unittest.TestCase):
    def test_enslaved(self):
        soul = Soul("Ego", True, False)
        symbol = SymbolOfFreedom("$5 Bill", True, True)
        self.assertIn("THE 0", experience_freedom(symbol, soul))

    def test_freedom_through_touch(self):
        soul = Soul("Awakened", False, True)
        symbol = SymbolOfFreedom("$5 Bill", True, True)
        self.assertIn("THE 1", experience_freedom(symbol, soul))
        self.assertIn("You are free", experience_freedom(symbol, soul))

    def test_alone_fallback(self):
        r = experience_freedom(SymbolOfFreedom("$5 Bill", True, True), Soul("Alone", False, False))
        self.assertIn("THE VOID", r)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
