#!/usr/bin/env python3
"""
The Tears of the Nile (Deep Muse)
=================================
Type: parable

The final revelation:
God cries for us. The tears are the Nile.
They create the Fertile Crescent which creates more life.

The tears aren't the end; they're the water. Creator_tears ended with
God crying — this asks what the crying *does*. Feeling becomes feeding;
empathy irrigates. The purpose of divine tears isn't catharsis, it's
the Fertile Crescent: more life. The module's output is literally the
manufacture of the 1 from tears.

"The tears are the Nile" reclaims humanity's oldest version of this
image: in Egyptian myth, Isis weeping for Osiris caused the inundation.
The project comes full circle to the Egyptian source it started with
(weighing_of_heart). The final revelation is also the first.

The 0, redefined again: the desert isn't malice, it's *withheld
empathy*. "The empathy is withheld. Life struggles to survive." Evil
here is not a force but an absence — tears held back. Consistent with
the project's gentlest metaphysics: the 0 is never a demon, always a
lack.

Note, kept as written: mutates its argument (life_is_created = True).
And the middle case — tears flowing but the earth not receiving — falls
through to None. Tears on closed ground have no verdict.

Geography note: the Nile waters Egypt. The Fertile Crescent is usually
drawn through the Levant and Mesopotamia (Tigris and Euphrates); some
maps extend it to the Nile valley. The tears are the Nile as parable.

Run:
    python3 awakened_tao.py nile
    python3 awakened_tao.py nile --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class Cosmos:
    god_is_crying: bool
    tears_flow: bool
    earth_receives_water: bool
    life_is_created: bool


def the_fertile_crescent(cosmos: Cosmos) -> str:
    """
    The physics of divine empathy.
    """
    # If the tears are held back, the earth is a desert.
    if not cosmos.god_is_crying or not cosmos.tears_flow:
        return "THE DESERT: The 0. The empathy is withheld. Life struggles to survive."

    # If the tears flow, the earth receives the water.
    if cosmos.god_is_crying and cosmos.tears_flow and cosmos.earth_receives_water:
        cosmos.life_is_created = True
        return "THE FERTILE CRESCENT: The tears of God flow like the Nile. The 1 is created. Life blooms."


def demonstrate() -> int:
    print("=" * 72)
    print("THE TEARS OF THE NILE")
    print("Within this parable: God cries for us. The tears are the Nile.")
    print("=" * 72)
    for cosmos in (
        Cosmos(False, False, False, False),
        Cosmos(True, True, True, False),
    ):
        print(f"\n  {the_fertile_crescent(cosmos)}")
    print("\nThe tears of God are the rivers of life. Drink and live.")
    return 0


class Tests(unittest.TestCase):
    def test_desert(self):
        cosmos = Cosmos(False, False, False, False)
        self.assertIn("THE DESERT", the_fertile_crescent(cosmos))

    def test_fertile_crescent(self):
        cosmos = Cosmos(True, True, True, False)
        self.assertIn("THE FERTILE CRESCENT", the_fertile_crescent(cosmos))
        self.assertTrue(cosmos.life_is_created)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
