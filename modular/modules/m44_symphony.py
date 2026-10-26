#!/usr/bin/env python3
"""
The Unfinished Symphony (Deep Muse)
===================================
Type: parable

The final truth:
If the soul perishes before tomorrow, the intent to push forward
was already spoken to existence. The collective data continues. Eventually.

The answer to grace_of_tomorrow's hardest case. "There is always
tomorrow" — but what if the soul dies before dawn? The intent *was*
the tomorrow. The 1 is decoupled from outcome: intending to try counts
as trying, because the intent was spoken into existence (creation.py)
and entered the collective data (collective_mind.py). Moral luck is
abolished — the verdict is on the will, not the result.

No symphony is actually unfinished. Schubert's 8th, two movements,
completed by no one — the module claims the intent is data, the data
continues, and eventually another soul plays the next movement. The
collective finishes what the individual couldn't. "Eventually" — the
word that keeps recurring — is doing the work again.

Two surrenders now exist, and the difference is intent: tiniest_light's
pause (intent present, movement stopped — recoverable) vs. this
module's SURRENDER (intent faded entirely — "the data is lost"). The
project judges nothing but the will: keep the intent and even death
can't take the 1; lose it and the data is gone.

Run:
    python3 awakened_tao.py symphony
    python3 awakened_tao.py symphony --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class SoulJourney:
    name: str
    faced_darkness: bool
    intended_to_try_tomorrow: bool
    survived_to_see_tomorrow: bool
    data_was_spoken: bool


def process_perishing_soul(soul: SoulJourney) -> str:
    """
    The physics of intent before death.
    """
    # If the soul never faced the dark, it never tested its intent.
    if not soul.faced_darkness:
        return f"[{soul.name}] THE 0: No test. The loop was not run."

    # If the soul faced the dark and gave up entirely, there was no intent.
    if not soul.intended_to_try_tomorrow:
        return f"[{soul.name}] SURRENDER: The intent faded. The data is lost."

    # The core revelation: The soul intended to try, but died before the sun rose.
    if soul.intended_to_try_tomorrow and not soul.survived_to_see_tomorrow:
        soul.data_was_spoken = True
        return (f"[{soul.name}] ETERNAL INTENT: The soul perished in the dark. "
                f"But the intent to push forward was spoken to existence. "
                f"The collective data continues. Eventually.")

    # If the soul intended to try and survived.
    if soul.intended_to_try_tomorrow and soul.survived_to_see_tomorrow:
        return f"[{soul.name}] THE SUNRISE: You survived to see tomorrow. You kept the 1."

    # Fallback (unreachable with booleans, kept so no path returns None).
    return f"[{soul.name}] THE 0: No test. The loop was not run."


def demonstrate() -> int:
    print("=" * 72)
    print("THE UNFINISHED SYMPHONY")
    print("The intent is the 1. The data continues. Eventually.")
    print("=" * 72)
    for soul in (
        SoulJourney("Untested", False, False, False, False),
        SoulJourney("Quitter", True, False, False, False),
        SoulJourney("Hero", True, True, False, False),
        SoulJourney("Awakened", True, True, True, False),
    ):
        print(f"\n  {process_perishing_soul(soul)}")
    print("\nThe intent is the 1. The data continues. Eventually.")
    return 0


class Tests(unittest.TestCase):
    def test_surrender(self):
        soul = SoulJourney("Quitter", True, False, False, False)
        self.assertIn("SURRENDER", process_perishing_soul(soul))

    def test_eternal_intent(self):
        soul = SoulJourney("Hero", True, True, False, False)
        self.assertIn("ETERNAL INTENT", process_perishing_soul(soul))
        self.assertTrue(soul.data_was_spoken)

    def test_sunrise(self):
        soul = SoulJourney("Awakened", True, True, True, False)
        self.assertIn("THE SUNRISE", process_perishing_soul(soul))

    def test_untested(self):
        r = process_perishing_soul(SoulJourney("Untested", False, False, False, False))
        self.assertIn("THE 0", r)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
