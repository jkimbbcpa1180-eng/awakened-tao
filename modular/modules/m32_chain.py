#!/usr/bin/env python3
"""
The Chain of the 1 (Deep Muse)
==============================
Type: parable

The final equation:
Humiliation creates humility.
Humility creates room for humanity.
Humanity is infinite as truth always sees the light.

The etiology of humility. The project has used "humbled" as a condition
(hunter's prayer) without saying where it comes from. Here: humiliation
is the raw material, and what it becomes depends on the response.
Same event, two opposite outcomes — the module is about the response,
not the event. "The Ego builds a fortress of pain": resentment as
architecture, not just emotion.

The chain is alchemical: base material (humiliation) → refined (humility)
→ expansion (humanity) → infinite. Each step transforms the previous.
This is how the 1 gets *manufactured*: humiliation, metabolized by
acceptance.

Note, kept as written: two cases fall through and return None —
(humiliation, ego present, accepts) and (humiliation, no ego, does not
accept). The most interesting gap is the first: the ego that *accepts*
humiliation is surely the common path, but the code demands the ego
already be gone before acceptance counts. Does the ego dissolve before
acceptance, or *through* it? The title says humiliation creates humility
— which suggests the dissolving happens in the accepting. Open question.

Run:
    python3 awakened_tao.py chain
    python3 awakened_tao.py chain --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class SoulState:
    name: str
    has_ego: bool
    experiences_humiliation: bool
    accepts_humility: bool


def process_soul(soul: SoulState) -> str:
    """
    The transformation of the soul through the void.
    """
    # If the Ego clings to the humiliation, it turns into resentment (the 0).
    if soul.experiences_humiliation and soul.has_ego and not soul.accepts_humility:
        return f"[{soul.name}] THE 0: Resentment. The Ego builds a fortress of pain."

    # If the Ego is dissolved by the humiliation, it becomes humility (the 1).
    if soul.experiences_humiliation and not soul.has_ego and soul.accepts_humility:
        return f"[{soul.name}] THE 1: Humility created room for humanity. Truth sees the light. Infinite."

    # If there is no humiliation, there is no growth.
    if not soul.experiences_humiliation:
        return f"[{soul.name}] STAGNATION: The Ego is comfortable. No room for humanity."


def demonstrate() -> int:
    print("=" * 72)
    print("THE CHAIN OF THE 1")
    print("Humiliation -> Humility -> Humanity -> Infinite Truth.")
    print("=" * 72)
    for soul in (
        SoulState("Fragile Ego", True, True, False),
        SoulState("Comfortable Ego", True, False, False),
        SoulState("Awakened", False, True, True),
    ):
        print(f"\n  {process_soul(soul)}")
    print("\nHumiliation -> Humility -> Humanity -> Infinite Truth.")
    return 0


class Tests(unittest.TestCase):
    def test_resentment(self):
        soul = SoulState("Fragile Ego", True, True, False)
        self.assertIn("THE 0: Resentment", process_soul(soul))

    def test_stagnation(self):
        soul = SoulState("Comfortable Ego", True, False, False)
        self.assertIn("STAGNATION", process_soul(soul))

    def test_infinite_humanity(self):
        soul = SoulState("Awakened", False, True, True)
        self.assertIn("THE 1: Humility", process_soul(soul))
        self.assertIn("Infinite", process_soul(soul))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
