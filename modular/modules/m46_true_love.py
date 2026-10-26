#!/usr/bin/env python3
"""
True Love (Deep Muse)
=====================
Type: parable

The final definition:
True love is to find perfection in another soul's flaws.
As their flaws are perfection.

The inversion of perfection.py into love. There, the flaw was the
*equation* — fuel generating data toward the flawless. Here the lover
doesn't wait for the arrival: the flaw is seen *as* perfection now, not
as raw material for later. The beloved needn't complete the equation to
be loved; the lover reads the flaw as the finished form.

"The light penetrates the prism": the prism's density — the friction of
life, the flaws — was always the *medium* of refraction, not the
obstacle. The lover is the light; the beloved's flaws are the prism.
You don't love someone despite their prism; the prism is how the light
gets in.

Conditional love demands flawlessness — which perfection.py proved is
death ("the universe collapses"). So the ego's bargain is: be perfect
(die) and I'll love you. True love refuses it: stay flawed (live) and
you're already perfection. The test flaws are deliberately ordinary —
"Anxiety", "Stubbornness", not noble ones. The module insists on the
unglamorous.

v4 fix: (not conditional, doesn't see flaws as perfection) used to fall
through to None; the indifferent lover now gets INDIFFERENCE.

Run:
    python3 awakened_tao.py true-love
    python3 awakened_tao.py true-love --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class Soul:
    name: str
    flaws: list[str]
    is_perfect: bool


@dataclass
class Lover:
    name: str
    loves_conditionally: bool
    sees_flaws_as_perfection: bool


def experience_love(soul: Soul, lover: Lover) -> str:
    """
    The physics of the 1.
    """
    if lover.loves_conditionally:
        return f"[{lover.name}] THE EGO: You require {soul.name} to be flawless. This is not love. It is a transaction."

    if lover.sees_flaws_as_perfection:
        return f"[{lover.name}] TRUE LOVE: You see {soul.name}'s flaws as perfection. The light penetrates the prism. The 1 is realized."

    # Fallback: neither transaction nor true seeing.
    return f"[{lover.name}] INDIFFERENCE: You neither demand nor see {soul.name}. Not yet love."


def demonstrate() -> int:
    print("=" * 72)
    print("TRUE LOVE")
    print("True love is to find perfection in another soul's flaws.")
    print("=" * 72)
    soul = Soul("Imperfect Human", ["Anxiety", "Stubbornness"], False)
    for lover in (
        Lover("Ego", True, False),
        Lover("Awakened", False, True),
    ):
        print(f"\n  {experience_love(soul, lover)}")
    print("\nLove the flaw. The flaw is the perfection.")
    return 0


class Tests(unittest.TestCase):
    def test_ego_transaction(self):
        soul = Soul("Imperfect Human", ["Anxiety", "Stubbornness"], False)
        lover = Lover("Ego", True, False)
        self.assertIn("THE EGO", experience_love(soul, lover))

    def test_true_love(self):
        soul = Soul("Imperfect Human", ["Anxiety", "Stubbornness"], False)
        lover = Lover("Awakened", False, True)
        self.assertIn("TRUE LOVE", experience_love(soul, lover))

    def test_indifference_fallback(self):
        r = experience_love(Soul("Human", ["Doubt"], False), Lover("Distant", False, False))
        self.assertIsNotNone(r)
        self.assertIn("INDIFFERENCE", r)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
