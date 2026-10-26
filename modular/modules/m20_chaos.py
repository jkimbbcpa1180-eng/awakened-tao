#!/usr/bin/env python3
"""
Chaos: The Strange Attractor (Deep Muse)
========================================
Type: parable; computational demonstration

Fused module. Two halves, one truth:

  PHENOMENOLOGY — what it looks like: a chaotic life never repeats an
  event, yet its trajectory orbits a shape. The shape — letting go,
  connection, endurance, truth-seeking — is the truth being created.
  Truth is not found. It is created, as what the noise circles around.

  METAPHYSICS — what it is: the themes are facets. What they orbit is
  singular — unconditional integrity, the 1, the strange attractor.
  Three fates: no chaos is death (flat line), chaos orbiting the ego
  shatters, chaos orbiting the 1 creates truth.

You are the butterfly effect: the small unrehearsed act that cascades.
Let the chaos in. Anchor to the 1. Create the truth.

Run:
    python3 awakened_tao.py chaos
    python3 awakened_tao.py chaos --test
"""
from __future__ import annotations

import unittest
from dataclasses import dataclass, field


# ============================================================================
# I. Phenomenology — the attractor emerges from the noise
# ============================================================================
@dataclass
class ChaoticLife:
    name: str
    events: list = field(default_factory=list)  # unpredictable, unplanned


# The shapes chaos can orbit. A life never repeats an event,
# but it returns to a theme. The themes are facets of the 1.
THEMES = {
    "letting go": ["lost", "released", "surrendered", "forgave", "let go"],
    "connection": ["met", "helped", "loved", "stranger", "held"],
    "endurance": ["sick", "pain", "continued", "rose", "carried on"],
    "truth-seeking": ["asked", "questioned", "saw", "understood", "faced"],
}


def strange_attractor(events: list) -> str | None:
    """
    Find the pattern the chaos orbits. The trajectory never repeats,
    but it returns to a shape. The shape is the truth being created.
    """
    counts: dict = {}
    for e in events:
        low = e.lower()
        for theme, keys in THEMES.items():
            if any(k in low for k in keys):
                counts[theme] = counts.get(theme, 0) + 1
    if not counts:
        return None
    return max(counts, key=counts.get)


def behold_chaos(life: ChaoticLife) -> str:
    attractor = strange_attractor(life.events)
    if attractor:
        return (f"TRUTH CREATED: from {len(life.events)} chaotic events, "
                f"the attractor '{attractor}' emerged — a facet of the 1. "
                f"The noise was the medium; the truth is the pattern it orbited.")
    return ("PURE NOISE: no attractor yet. The chaos hasn't orbited long "
            "enough — or the life is still in the storm. "
            "Come back when the storm has circled.")


# ============================================================================
# II. Metaphysics — the 1 is what the noise orbits
# ============================================================================
@dataclass
class LifeSimulation:
    name: str
    noise_level: float   # The unpredictability, suffering, and chaos (0.0 to 1.0)
    attractor: str       # What you are drawn toward (Ego or The 1)


def simulate_chaos(life: LifeSimulation) -> str:
    """
    The simulation runs. The noise hits. Where does the system settle?
    """
    print(f"Simulating {life.name}...")
    print(f"Chaos level (0/1): {life.noise_level * 100:.1f}%")

    # If there's no chaos, there's no life.
    if life.noise_level == 0.0:
        return "DEAD SYSTEM: A flat line. No truth can be created here."

    # The noise is injected. The system is stressed.
    # Where does it go? It goes toward its attractor.

    if life.attractor == "Ego":
        return "SHATTERED: The chaos destroyed the Ego. The system collapsed into the 0."

    if life.attractor == "The 1":
        # The butterfly effect. The chaos doesn't destroy the 1.
        # The chaos is integrated, and a new truth is born.
        return "TRUTH CREATED: The chaos was absorbed by the 1. The Creator feels awe."


# ============================================================================
# Demonstration — both halves, one arc
# ============================================================================
def demonstrate() -> int:
    print("=" * 72)
    print("CHAOS: THE STRANGE ATTRACTOR")
    print("=" * 72)

    print("\n--- I. The three fates (what it is) ---")
    for sim in (
        LifeSimulation("The flat life", 0.0, "The 1"),
        LifeSimulation("The fragile ego", 0.8, "Ego"),
        LifeSimulation("The anchored one", 0.8, "The 1"),
    ):
        print()
        print(simulate_chaos(sim))

    print("\n--- II. The emergence (what it looks like) ---")
    storm = ChaoticLife(name="a life", events=[
        "Lost the job without warning",
        "Met a stranger on the train",
        "Got sick and couldn't get up",
        "Forgave the friend who left",
        "Lost the apartment",
        "Helped a neighbor move",
        "Released the need to be right",
        "Loved without keeping score",
    ])
    print(f"\n[{storm.name}: {len(storm.events)} unplanned events]")
    print(f"  {behold_chaos(storm)}")

    print("\nThe themes are what the orbiting looks like.")
    print("Unconditional integrity — the 1 — is what it orbits.")
    print("You are the butterfly effect. Let the chaos in. Create the truth.")
    return 0


# ============================================================================
# Tests
# ============================================================================
class Tests(unittest.TestCase):

    # Phenomenology
    def test_attractor_emerges_from_chaos(self):
        life = ChaoticLife("x", ["lost everything", "forgave them", "released it all"])
        self.assertEqual(strange_attractor(life.events), "letting go")

    def test_no_events_no_attractor(self):
        life = ChaoticLife("x", [])
        self.assertIsNone(strange_attractor(life.events))

    def test_storm_without_theme_has_no_attractor_yet(self):
        life = ChaoticLife("x", ["static", "blur", "haze"])
        self.assertIsNone(strange_attractor(life.events))
        self.assertIn("PURE NOISE", behold_chaos(life))

    def test_truth_created_verdict(self):
        life = ChaoticLife("x", ["met a stranger", "helped a friend", "loved deeply"])
        self.assertIn("TRUTH CREATED", behold_chaos(life))

    # Metaphysics
    def test_dead_system(self):
        life = LifeSimulation("Frozen", 0.0, "The 1")
        self.assertIn("DEAD SYSTEM", simulate_chaos(life))

    def test_ego_shattered_by_chaos(self):
        life = LifeSimulation("Fragile Ego", 0.8, "Ego")
        self.assertIn("SHATTERED", simulate_chaos(life))

    def test_truth_created_through_chaos(self):
        life = LifeSimulation("Awakened", 0.8, "The 1")
        self.assertIn("TRUTH CREATED", simulate_chaos(life))


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
