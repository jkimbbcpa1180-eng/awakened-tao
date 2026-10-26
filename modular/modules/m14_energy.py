#!/usr/bin/env python3
"""
The Source of Energy
====================
Type: parable

Moral physics, by analogy only (Newton's third law is about forces
between bodies, not about intent): every action produces a reaction, and the intent —
not the act — determines its nature. The same words spoken from Ego
produce suffering; spoken from Unconditional Integrity, they leave
a mirror.

The act is neutral. The energy source is everything.

Run:
    python3 awakened_tao.py energy
"""
from __future__ import annotations
import unittest


def source_of_energy(action, intent):
    """
    Where is the energy being produced?
    """
    if intent == "Ego":
        # By analogy with Newton's third law (not the law itself):
        # ego is modeled as producing a reaction of pain.
        return "Reaction: suffering"
    elif intent == "Unconditional Integrity":
        # The 1 produces a mirror.
        return "Reaction: the mirror remains"
    return "Reaction: unknown — the intent was not named."


def live(action, intent):
    print(f"Action: {action}")
    print(f"Source: {intent}")
    print(source_of_energy(action, intent))
    print("-" * 30)


def main() -> int:
    print("=" * 72)
    print("THE SOURCE OF ENERGY")
    print("The act is neutral. The intent is the energy source.")
    print("=" * 72 + "\n")
    # Example
    live("Tell the truth even when it costs you", "Ego")  # Fear of rejection, Ego
    live("Tell the truth even when it costs you", "Unconditional Integrity")  # The 1
    print("Same action. Different source. Different cosmos.")
    return 0


class Tests(unittest.TestCase):
    def test_ego_produces_suffering(self):
        self.assertIn("suffering", source_of_energy("Any act", "Ego"))

    def test_integrity_leaves_mirror(self):
        self.assertIn("mirror remains", source_of_energy("Any act", "Unconditional Integrity"))

    def test_same_act_different_source_differs(self):
        act = "Tell the truth even when it costs you"
        self.assertNotEqual(source_of_energy(act, "Ego"),
                            source_of_energy(act, "Unconditional Integrity"))

    def test_unnamed_intent_is_unknown(self):
        self.assertIn("unknown", source_of_energy("Any act", "Indifference"))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    main()
