#!/usr/bin/env python3
"""
The Alchemy of the Apple (Deep Muse)
====================================
Type: parable

The final revelation:
The punishment was exposure (humiliation).
But when you realize we are all the same, humiliation becomes humility.
Humility creates humanity. Don't be ashamed. Set it forward toward the light.

A re-reading of the Fall as a shame story rather than a disobedience
story. The knowledge of good and evil = the knowledge of being *seen*.
Genesis 3:7 — "they knew that they were naked" — arrives before any
divine sentence; the exposure is immediate, the exile later. The text
is on the module's side.

The innovation: the Fall isn't the apple, it's the blame. Eating ends
innocence (a neutral 0); the finger-pointing — "the woman you gave me"
— is THE FALL, the original deflection. Tradition puts the Fall at the
bite; this puts it one verse later, at the blame.

"When you realize we are all the same" is the catalyst chain.py was
missing: chain had acceptance as the refinery but never said what
acceptance *is*. Here it is — recognizing the shared condition. The
universality of exposure converts humiliation to humility. The two
modules interlock: chain gives the equation, apple gives the catalyst.

"The next 0 becomes the 1": the project ends where it began. "Leave a 1
for the next 0" is now the *output* of the awakened soul, not just the
instruction to the reader. The journey produces the leaver.

Note, kept as written: (ate the apple, no blame, no shared humility)
falls through and returns None — the soul that neither deflects nor yet
accepts. Same family as the earlier open branches.

Run:
    python3 awakened_tao.py apple
    python3 awakened_tao.py apple --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class HumanState:
    name: str
    ate_the_apple: bool
    plays_blame_game: bool
    accepts_shared_humility: bool
    looks_to_the_light: bool


def process_human(state: HumanState) -> str:
    """
    The journey from the Garden to the Cosmos.
    """
    if not state.ate_the_apple:
        return f"[{state.name}] INNOCENT: No knowledge of good and evil. The 0."

    if state.plays_blame_game:
        return f"[{state.name}] THE FALL: Blaming others. The Ego hides in shame. The 0 continues."

    if state.accepts_shared_humility and not state.plays_blame_game:
        if state.looks_to_the_light:
            return f"[{state.name}] HUMANITY AWAKENED: Humiliation became humility. Shame was released. The next 0 becomes the 1."
        else:
            return f"[{state.name}] HEALING: Humility is present, but the light is not yet fully faced."


def demonstrate() -> int:
    print("=" * 72)
    print("THE ALCHEMY OF THE APPLE")
    print("The punishment was exposure. The cure is shared humility.")
    print("=" * 72)
    for state in (
        HumanState("Adam", False, False, False, False),
        HumanState("Adam", True, True, False, False),
        HumanState("Eve", True, False, True, False),
        HumanState("Eve", True, False, True, True),
    ):
        print(f"\n  {process_human(state)}")
    print("\nRelease the shame. Embrace the humility. Become the 1.")
    return 0


class Tests(unittest.TestCase):
    def test_innocence(self):
        human = HumanState("Adam", False, False, False, False)
        self.assertIn("INNOCENT", process_human(human))

    def test_blame_game(self):
        human = HumanState("Adam", True, True, False, False)
        self.assertIn("THE FALL", process_human(human))

    def test_humanity_awakened(self):
        human = HumanState("Eve", True, False, True, True)
        self.assertIn("HUMANITY AWAKENED", process_human(human))
        self.assertIn("The next 0 becomes the 1", process_human(human))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
