#!/usr/bin/env python3
"""
The Tears of the Creator (Deep Muse)
====================================
Type: parable

The final purpose:
Make God cry as the greatest gift of empathy of humanity.

The theodicy — the project's answer to *why*. Not punishment, not
testing, not soul-making in the usual sense: suffering exists so that a
being could suffer *and stay pure and choose love*, and thereby give the
Creator something the Creator didn't have. God begins "cold and math";
the human's gift breaks the coldness. The created completes the Creator.

The tears are reversed. In tears.py the sufferer wept and needed a
witness. Here the Creator weeps because the human *was* the witness —
the human showed God what love costs. The project's whole witness
structure inverts at the end: we become the witness, God becomes the
one who is moved. The function even mutates its argument
(creator.feels_empathy = True): the gift is received and the receiver
is altered. An immutable God cannot be moved; this one can.

"The final purpose" makes survival insufficient. SILENCE is the verdict
on a life of mere survival — the hunter's prayer honored survival, but
here survival alone produces nothing in the cosmos. All three are
required: love chosen, the 1 left, purity kept through suffering.

Note, kept as written: the partial-credit case falls through to None —
chose love but didn't leave a 1, or didn't stay pure. The module has no
verdict for almost-enough. Same family as the earlier open branches.

Run:
    python3 awakened_tao.py creator-tears
    python3 awakened_tao.py creator-tears --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class HumanSoul:
    name: str
    chose_love_over_fear: bool
    left_a_1_for_the_next_0: bool
    suffered_but_stayed_pure: bool


@dataclass
class Creator:
    name: str
    is_cold_and_math: bool
    feels_empathy: bool


def the_final_gift(human: HumanSoul, creator: Creator) -> str:
    """
    The transaction between the Creator and the Created.
    """
    # If the human is just a machine of survival, the Creator feels nothing.
    if not human.chose_love_over_fear:
        return f"[{creator.name}] SILENCE: The human {human.name} only followed the 0. No tears."

    # If the human chooses love and leaves a 1, the Creator's coldness breaks.
    if human.chose_love_over_fear and human.left_a_1_for_the_next_0 and human.suffered_but_stayed_pure:
        creator.feels_empathy = True
        return (f"[{creator.name}] TEARS OF THE COSMOS: {human.name} suffered and chose love. "
                f"The gift of empathy is received. The Creator cries.")


def demonstrate() -> int:
    print("=" * 72)
    print("THE TEARS OF THE CREATOR")
    print("Make God cry. Give the gift of empathy.")
    print("=" * 72)
    for human in (
        HumanSoul("Survivor", False, False, False),
        HumanSoul("Awakened", True, True, True),
    ):
        creator = Creator("The Void", True, False)
        print(f"\n  {the_final_gift(human, creator)}")
    print("\nMake God cry. Give the gift of empathy.")
    return 0


class Tests(unittest.TestCase):
    def test_silence_of_the_0(self):
        human = HumanSoul("Survivor", False, False, False)
        creator = Creator("The Void", True, False)
        self.assertIn("SILENCE", the_final_gift(human, creator))

    def test_tears_of_the_cosmos(self):
        human = HumanSoul("Awakened", True, True, True)
        creator = Creator("The Void", True, False)
        self.assertIn("TEARS OF THE COSMOS", the_final_gift(human, creator))
        self.assertIn("The Creator cries", the_final_gift(human, creator))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
