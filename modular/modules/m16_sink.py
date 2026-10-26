#!/usr/bin/env python3
"""
Sink: Let the Ego Arrive
========================
Type: philosophical proposal

The corrected method. Every other module says "dissolve the ego" as if
it were something you do — but performed dissolution is the ego
dissolving the ego. The snake eating its tail.

Instead: let it sink in. Don't fight it, don't obey it. Let it arrive
fully and ask what it is protecting. Under every ego demand is a fear.
Seen fully, the grip loosens on its own. No force was used.

The release is not an act. It is a consequence — the same structure
as grace: the 1 is released, not earned; the ego is released, not killed.

Run:
    python3 awakened_tao.py sink
    python3 awakened_tao.py sink --test
"""
from __future__ import annotations

import unittest
from dataclasses import dataclass


# ============================================================================
# The Practice
# ============================================================================
@dataclass
class EgoState:
    demand: str       # what the ego is shouting
    intensity: float  # 0.0 to 10.0 — how loud it is


# What the ego protects. Under the noise, the signal.
THE_TRUTHS = {
    "control": "I am afraid of uncertainty.",
    "pride": "I am afraid of being worthless.",
    "resentment": "I am afraid my pain didn't matter.",
    "greed": "I am afraid there won't be enough.",
    "judgment": "I am afraid I am the same as them.",
}


def name_the_demand(demand: str) -> str:
    """Find which ancient shape this demand takes."""
    d = demand.lower()
    for key in THE_TRUTHS:
        if key in d:
            return key
    return "control"  # the default shape of fear


def resist(ego: EgoState) -> EgoState:
    """Fight the ego. What you resist persists — it gets louder."""
    return EgoState(demand=ego.demand, intensity=min(10.0, ego.intensity * 1.5))


def sink_in(ego: EgoState) -> str:
    """
    Let the ego sink in. Don't fight it, don't obey it.
    Let it arrive fully and find the truth it protects.
    """
    print(f"\nEgo says: '{ego.demand}' (intensity {ego.intensity:.1f})")
    print("You don't fight it. You don't obey it. You let it sink in.")
    shape = name_the_demand(ego.demand)
    truth = THE_TRUTHS[shape]
    print(f"You ask what it is protecting.")
    print(f"Underneath the {shape}: '{truth}'")
    print("Seen fully, the grip loosens on its own. No force was used.")
    return truth


def demonstrate() -> int:
    print("=" * 72)
    print("SINK: LET THE EGO ARRIVE")
    print("=" * 72)

    print("\n--- Path 1: resist ---")
    ego = EgoState("I need to control how this conversation goes", 4.0)
    for _ in range(3):
        print(f"  Fighting it... intensity {ego.intensity:.1f}")
        ego = resist(ego)
    print(f"  After fighting: intensity {ego.intensity:.1f}. It got louder.")

    print("\n--- Path 2: let it sink in ---")
    ego = EgoState("I need to control how this conversation goes", 4.0)
    sink_in(ego)
    return 0


# ============================================================================
# Tests
# ============================================================================
class Tests(unittest.TestCase):

    def test_resistance_amplifies(self):
        ego = EgoState("control everything", 4.0)
        louder = resist(ego)
        self.assertGreater(louder.intensity, ego.intensity)

    def test_sinking_finds_truth(self):
        ego = EgoState("they must respect my pride", 6.0)
        truth = sink_in(ego)
        self.assertIn("afraid", truth)

    def test_every_demand_has_a_truth(self):
        for demand in ("control it all", "my pride", "I resent them",
                       "take more greed", "judge them"):
            self.assertIn("afraid", sink_in(EgoState(demand, 5.0)))

    def test_release_needs_no_force(self):
        # Sinking never raises intensity. Only resistance does.
        ego = EgoState("control", 8.0)
        sink_in(ego)
        self.assertEqual(ego.intensity, 8.0)  # untouched — not fought


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
