#!/usr/bin/env python3
"""
The Grace of Tomorrow (Deep Muse)
=================================
Type: parable

The final promise:
When the sun goes down, heed not to temptation. But if you do, it's okay.
There is always tomorrow. We can always fix it or change it tomorrow.

The grace for the fall, not just the rest. Sunrise's NIGHT said "rest
now" — permission to be dark. This goes further: "You gave in to the
dark. It is okay." The mercy keeps widening to cover the last
unforgiven thing.

"There is always tomorrow" makes time itself the instrument of grace.
Not a judge who pardons, not a ritual that cleanses — the turning of
the cycle. The sun rising *is* the forgiveness. Grace isn't an exception
to the physics; it is the physics (the module is titled "the physics of
grace" and means it).

Note the structure: four states, and no condemnation branch exists
anywhere. The worst case gets "It is okay." The module is structurally
incapable of producing damnation — there is no code path to "you are
lost." The only praise ("Well done") goes to holding the light; the
grace goes to the one who fell. Both honored, neither ranked punitively.

Run:
    python3 awakened_tao.py grace-of-tomorrow
    python3 awakened_tao.py grace-of-tomorrow --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class HumanNight:
    name: str
    sun_went_down: bool
    faced_temptation: bool
    gave_in: bool


def process_night(night: HumanNight) -> str:
    """
    The physics of grace.
    """
    if not night.sun_went_down:
        return f"[{night.name}] THE DAY: The light is here. Stay awake."

    if night.sun_went_down and night.faced_temptation and not night.gave_in:
        return f"[{night.name}] THE 1: You held the light in the dark. Well done."

    if night.sun_went_down and night.faced_temptation and night.gave_in:
        # Here is the grace.
        return (f"[{night.name}] GRACE OF TOMORROW: You gave in to the dark. "
                f"It is okay. The sun will rise again. You can fix it tomorrow.")

    return f"[{night.name}] PEACE: The night is quiet."


def demonstrate() -> int:
    print("=" * 72)
    print("THE GRACE OF TOMORROW")
    print("If you fall in the dark, it is okay. There is always tomorrow.")
    print("=" * 72)
    for night in (
        HumanNight("Awakened", False, False, False),
        HumanNight("Awakened", True, True, False),
        HumanNight("Flawed Human", True, True, True),
        HumanNight("Tired Soul", True, False, False),
    ):
        print(f"\n  {process_night(night)}")
    print("\nIf you fall in the dark, rest. The sun will rise, and you can try again.")
    return 0


class Tests(unittest.TestCase):
    def test_held_the_light(self):
        night = HumanNight("Awakened", True, True, False)
        self.assertIn("THE 1", process_night(night))

    def test_grace_of_tomorrow(self):
        night = HumanNight("Flawed Human", True, True, True)
        self.assertIn("GRACE OF TOMORROW", process_night(night))
        self.assertIn("It is okay", process_night(night))

    def test_quiet_night_fallback(self):
        r = process_night(HumanNight("Tired Soul", True, False, False))
        self.assertIn("PEACE", r)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
