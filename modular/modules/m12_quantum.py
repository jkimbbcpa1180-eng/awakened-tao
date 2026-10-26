#!/usr/bin/env python3
"""
Quantum Awareness Engine
========================
Type: parable

The final manifesto.
You are the observer. By analogy, not physics: as measurement is said to
collapse a wave function, your choices narrow humanity's future.
If you live unconditionally, you leave a 1. If you forget history, you repeat the 0.

Run:
    python3 awakened_tao.py quantum --observe
    python3 awakened_tao.py quantum --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class QuantumState:
    observed_history: bool
    living_unconditionally: bool
    choosing_love_over_fear: bool


def observe_future(state: QuantumState) -> str:
    """
    The observer (by analogy) collapses the state of humanity.
    """
    # If we forget history, we repeat the 0
    if not state.observed_history:
        return "REPEAT_THE_0: The void of ignorance consumes the future."

    # If we observe history but choose fear, we repeat the 0
    if not state.choosing_love_over_fear:
        return "REPEAT_THE_0: Fear and ego build walls instead of mirrors."

    # If we live unconditionally and choose love, we leave a 1
    if state.living_unconditionally and state.choosing_love_over_fear:
        return "LEAVE_THE_1: Humanity moves forward without pain."

    return "UNCERTAIN: The observer has not yet decided."


class Tests(unittest.TestCase):
    def test_unconditional_love_leaves_1(self):
        state = QuantumState(
            observed_history=True,
            living_unconditionally=True,
            choosing_love_over_fear=True
        )
        self.assertIn("LEAVE_THE_1", observe_future(state))

    def test_forgetting_history_repeats_0(self):
        state = QuantumState(
            observed_history=False,
            living_unconditionally=True,
            choosing_love_over_fear=True
        )
        self.assertIn("REPEAT_THE_0", observe_future(state))

    def test_fear_repeats_0(self):
        state = QuantumState(
            observed_history=True,
            living_unconditionally=False,
            choosing_love_over_fear=False
        )
        self.assertIn("REPEAT_THE_0", observe_future(state))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    print(__doc__)
