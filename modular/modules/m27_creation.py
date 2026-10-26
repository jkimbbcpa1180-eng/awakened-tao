#!/usr/bin/env python3
"""
Ontological Creation (Deep Muse)
================================
Type: parable

The final power:
Bend time and dilation. Speak truth into existence.
But it must be pure, it must serve more than one soul,
and it must not harm another.

"Let there be" as a gated function. The creative Word is not free —
it has three locks, checked in a moral order: harm first, then purity
and universality together. A pure intention that harms another still
collapses; purity alone does not license creation. That is the answer
to the fanatic's question.

"Serves every soul" makes creation inherently collective: no private
truths get spoken into existence. The universe only manifests what
serves the many — the final form of the project's collective turn.
The wormhole callback is load-bearing: the creative word travels
*through* the wormhole. The modules are becoming a system.

Note the docstring/code gap, kept as written: the docstring says "more
than one soul" (plurality) but the code demands serves_every_soul
(universality). The code is stricter than the prose.

Labeled as metaphor, per the honesty rule: speech does not bend time or
cause time dilation, and nothing in physics manifests an intention.
"Speak truth into existence" is a parable about what true words make
possible between people.

Run:
    python3 awakened_tao.py creation
    python3 awakened_tao.py creation --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class SpokenTruth:
    intention: str
    is_pure: bool
    serves_every_soul: bool
    harms_another: bool


def speak_to_existence(truth: SpokenTruth) -> str:
    """
    The physics of creation.
    """
    if truth.harms_another:
        return "COLLAPSE: The universe rejects the truth. It harms another. The Ego has corrupted the light."

    if not truth.is_pure or not truth.serves_every_soul:
        return "DISTORTION: The truth is not pure or does not serve all souls. The wormhole closes."

    if truth.is_pure and truth.serves_every_soul and not truth.harms_another:
        return f"MANIFESTED: Within this parable: The light bends time. '{truth.intention}' is spoken into existence because it is true."


def demonstrate() -> int:
    print("=" * 72)
    print("ONTOLOGICAL CREATION")
    print("Speak truth into existence.")
    print("=" * 72)
    cases = [
        ("The conquest",
         SpokenTruth("Take their land", False, False, True)),
        ("The private wish",
         SpokenTruth("Make me rich", False, True, False)),
        ("The blessing",
         SpokenTruth("Let there be peace for all souls", True, True, False)),
    ]
    for name, t in cases:
        print(f"\n[{name}]")
        print(f"  {speak_to_existence(t)}")
    print("\nSpeak it into existence. Because it is true.")
    return 0


class Tests(unittest.TestCase):
    def test_harmful_truth(self):
        t = SpokenTruth("Take their land", False, False, True)
        self.assertIn("COLLAPSE", speak_to_existence(t))

    def test_impure_truth(self):
        t = SpokenTruth("Make me rich", False, True, False)
        self.assertIn("DISTORTION", speak_to_existence(t))

    def test_manifested_truth(self):
        t = SpokenTruth("Let there be peace for all souls", True, True, False)
        self.assertIn("MANIFESTED", speak_to_existence(t))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
