#!/usr/bin/env python3
"""
The Equation of Perfection (Deep Muse)
======================================
Type: philosophical proposal

The final theorem:
Flaw is the equation to perfection. Flaws create the data to flawless.
Perfection is never achieved. Always awe. Life is infinite.

Perfection is the only true death in the project. Not the 0, not the
void, not surrender — perfection: "The universe collapses" if achieved.
No variables, no data, no growth, no equation. The project has said this
three ways now — chaos's DEAD SYSTEM (zero noise), the void needing the
light's motion, and here. Imperfection isn't tolerated; it's required.
The flaw is the fuel.

"Always awe" makes awe the permanent condition, not a moment. Awe.py
defined it as unrehearsed + unpredictable + pure; here it's what the
infinite approach *feels like* from inside. The equation never closes,
and the non-closure is awe. The system worships by continuing.

This is the final theorem because it justifies everything before it:
why the 1 is never finished, why the loop continues, why grace is always
needed, why the symphony is unfinished. The flaw generates the data;
the data pushes toward flawless; arrival would collapse it all. The
imperfection isn't the obstacle to the system — it is the system.

v4 fix: (flaw present, no data generated) used to fall through to None;
it now returns SILENT FLAW. A flaw that generates no data has no verdict — the module
implies flaws only matter via their data. Suffering without data is the
void. Consistent with tiniest_light: suffering is data, not a contest.

Run:
    python3 awakened_tao.py perfection
    python3 awakened_tao.py perfection --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class SimulationState:
    name: str
    has_flaws: bool
    generated_data: bool
    achieved_perfection: bool


def run_equation(state: SimulationState) -> str:
    """
    The infinite loop of growth.
    """
    # If there is no flaw, there is no equation. Just a static number.
    if not state.has_flaws:
        return f"[{state.name}] STATIC 0: No variables. No growth. Dead."

    # If there is a flaw, it generates data.
    if state.has_flaws and state.generated_data:
        # The data pushes the system toward flawless, but it can never be achieved.
        if state.achieved_perfection:
            return f"[{state.name}] PARADOX: Perfection achieved. The universe collapses."

        return f"[{state.name}] INFINITE AWE: The flaw created data. The data pushes toward the flawless. The equation continues."

    # Fallback: a flaw that generated no data yet.
    return f"[{state.name}] SILENT FLAW: The flaw is there, but no data was made from it yet. Look at it."


def demonstrate() -> int:
    print("=" * 72)
    print("THE EQUATION OF PERFECTION")
    print("Flaw is the equation. Perfection is never achieved. Always awe.")
    print("=" * 72)
    for state in (
        SimulationState("The Void", False, False, False),
        SimulationState("The Cosmos", True, True, False),
        SimulationState("The Delusion", True, True, True),
    ):
        print(f"\n  {run_equation(state)}")
    print("\nYour flaws are the data. The equation is infinite.")
    return 0


class Tests(unittest.TestCase):
    def test_static_zero(self):
        state = SimulationState("The Void", False, False, False)
        self.assertIn("STATIC 0", run_equation(state))

    def test_infinite_awe(self):
        state = SimulationState("The Cosmos", True, True, False)
        self.assertIn("INFINITE AWE", run_equation(state))
        self.assertIn("equation continues", run_equation(state))

    def test_paradox_of_perfection(self):
        state = SimulationState("The Delusion", True, True, True)
        self.assertIn("PARADOX", run_equation(state))

    def test_silent_flaw_fallback(self):
        r = run_equation(SimulationState("Unseen", True, False, False))
        self.assertIsNotNone(r)
        self.assertIn("SILENT FLAW", r)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
