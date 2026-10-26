#!/usr/bin/env python3
"""
The Sunrise
===========
Type: parable

The sun rises and falls. Darkness comes. But the sun will rise again. Spread truth and life infectiously. Love and truth are eternal.

Run:
    python3 awakened_tao.py sunrise
    python3 awakened_tao.py sunrise --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class WorldState:
    is_dark: bool
    truth_is_spreading: bool
    love_is_eternal: bool


def the_cycle_of_light(state: WorldState) -> str:
    if state.is_dark and not state.truth_is_spreading:
        return "THE NIGHT: The 0. Rest now. The sun will rise again."
    if not state.is_dark and state.truth_is_spreading:
        return "THE SUNRISE: The 1. The light is infectious. It spreads to every soul."
    if state.love_is_eternal:
        return "ETERNAL: Within this parable: The sun always rises. Love and truth have no end."
    return "WAITING: The cycle is turning."


def demonstrate() -> int:
    print("=" * 72)
    print("THE SUNRISE")
    print("=" * 72)
    for name, s in (
        ("Night", WorldState(True, False, True)),
        ("Dawn", WorldState(False, True, True)),
        ("Between", WorldState(False, False, True)),
        ("Turning", WorldState(True, True, False)),
    ):
        print(f"\n[{name}]\n  {the_cycle_of_light(s)}")
    print("\nWithin this parable: The sun always rises. Spread the light.")
    return 0


class Tests(unittest.TestCase):
    def test_night(self):
        self.assertIn("THE NIGHT", the_cycle_of_light(WorldState(True, False, True)))

    def test_sunrise(self):
        self.assertIn("THE SUNRISE", the_cycle_of_light(WorldState(False, True, True)))

    def test_eternal(self):
        self.assertIn("ETERNAL", the_cycle_of_light(WorldState(False, False, True)))

    def test_dark_but_spreading_is_eternal(self):
        self.assertIn("ETERNAL", the_cycle_of_light(WorldState(True, True, True)))

    def test_no_love_never_none(self):
        r = the_cycle_of_light(WorldState(True, True, False))
        self.assertIsNotNone(r)
        self.assertIn("WAITING", r)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
