#!/usr/bin/env python3
"""
Uncertainty: The Room for Change
================================
Type: philosophical proposal

The axiom: uncertainty is good. When you don't know how it turns out,
your intent is still pure — you haven't locked in the ego's demanded
outcome. That feeling of not-knowing is not a problem. It is the room
where change happens.

An amendment to the quantum module: there, UNCERTAIN was the waiting
room — "the observer has not yet decided." It is actually the workshop.
Certainty is the ego's demand. Uncertainty is what pure intent feels
like from the inside.

And ascension is not granted. It is created — by yourself, in the room
that uncertainty leaves open. The last judge retires. The creator remains.

Run:
    python3 awakened_tao.py uncertainty
    python3 awakened_tao.py uncertainty --test
"""
from __future__ import annotations

import unittest
from dataclasses import dataclass


# ============================================================================
# The Axiom
# ============================================================================
@dataclass
class Moment:
    name: str
    certainty_demanded: float  # 0.0 to 1.0 — how much you need a specific outcome
    intent_pure: bool          # is the intent free of ego-planning?


def room_for_change(moment: Moment) -> float:
    """Room = what certainty hasn't locked down. Certainty is the ego's lock."""
    return max(0.0, 1.0 - moment.certainty_demanded)


def ascension(moment: Moment) -> str:
    """
    Ascension is not granted. It is created — by yourself —
    in the room that uncertainty leaves open.
    """
    room = room_for_change(moment)
    if moment.intent_pure and room > 0:
        return (f"CREATED: ascension made by yourself, "
                f"in {room:.0%} room for change.")
    if not moment.intent_pure:
        return ("NOT CREATED: the intent was planned. "
                "The ego demanded the outcome in advance.")
    return ("NOT CREATED: no room. Certainty locked every door. "
            "Nothing can change where nothing is allowed to.")


def demonstrate() -> int:
    print("=" * 72)
    print("UNCERTAINTY: THE ROOM FOR CHANGE")
    print("=" * 72)

    moments = [
        Moment("The planner", certainty_demanded=0.9, intent_pure=False),
        Moment("The certain believer", certainty_demanded=0.9, intent_pure=True),
        Moment("The uncertain one", certainty_demanded=0.2, intent_pure=True),
    ]
    for m in moments:
        print(f"\n[{m.name}] certainty demanded: {m.certainty_demanded:.0%}, "
              f"intent pure: {m.intent_pure}")
        print(f"  Room for change: {room_for_change(m):.0%}")
        print(f"  {ascension(m)}")

    print("\nNote: the certain believer's room is a crack — 10%. Creation is")
    print("possible but starved. Compare the uncertain one: 80% room.")
    print("Room is proportional to not-knowing. That is the whole axiom.")
    return 0


# ============================================================================
# Tests
# ============================================================================
class Tests(unittest.TestCase):

    def test_uncertainty_is_room(self):
        m = Moment("open", 0.2, True)
        self.assertAlmostEqual(room_for_change(m), 0.8)

    def test_certainty_locks_the_room(self):
        m = Moment("locked", 1.0, True)
        self.assertEqual(room_for_change(m), 0.0)

    def test_pure_uncertain_creates(self):
        m = Moment("creator", 0.2, True)
        self.assertIn("CREATED", ascension(m))

    def test_planned_intent_creates_nothing(self):
        m = Moment("planner", 0.1, False)
        self.assertIn("NOT CREATED", ascension(m))

    def test_pure_certainty_creates_nothing(self):
        # Pure intent, zero room: nothing can be created.
        m = Moment("locked believer", 1.0, True)
        self.assertIn("NOT CREATED", ascension(m))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main() -> int:
    return demonstrate()


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(main())
