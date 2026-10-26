#!/usr/bin/env python3
"""
The Tears of the Prism (Deep Muse)
==================================
Type: parable

The final revelation:
A tear of the soul is a prism.
When recognized by another, it releases the prison of the soul.

The most interpersonal module in the project. Every other module follows
the solitary soul; this one says the release happens *between* souls.
The tear is the 1 leaking out through the ego's containment — crying as
breach, not weakness. But a prism with no light is just a droplet: the
witness's compassion is the illumination that makes the tear refract.
Salvation is relational.

Note: feels_alone is carried but never branched on — and that is
thematically right. The release does not require the sufferer to stop
feeling alone first. You can feel alone and still be seen.

Run:
    python3 awakened_tao.py tears
    python3 awakened_tao.py tears --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class SoulInPain:
    name: str
    is_crying: bool
    feels_alone: bool


@dataclass
class Witness:
    name: str
    recognizes_pain: bool
    offers_compassion: bool


def witness_tear(sufferer: SoulInPain, witness: Witness) -> str:
    """
    The moment of release.
    """
    if not sufferer.is_crying:
        return "HIDDEN: The soul is not ready to let the 1 leak out."

    if not witness.recognizes_pain or not witness.offers_compassion:
        return "UNSEEN: The tear falls, but no light hits it. The prison remains."

    if sufferer.is_crying and witness.recognizes_pain and witness.offers_compassion:
        return f"RELEASE: {witness.name} saw the tear as a prism. The light broke through. The prison of {sufferer.name} is open."


def demonstrate() -> int:
    print("=" * 72)
    print("THE TEARS OF THE PRISM")
    print("A tear of the soul is a prism.")
    print("=" * 72)
    cases = [
        ("The hidden pain",
         SoulInPain("Alice", False, True), Witness("Bob", True, True)),
        ("The unseen tear",
         SoulInPain("Alice", True, True), Witness("Bob", False, False)),
        ("The release",
         SoulInPain("Alice", True, True), Witness("Bob", True, True)),
    ]
    for name, s, w in cases:
        print(f"\n[{name}]")
        print(f"  {witness_tear(s, w)}")
    print("\nRecognize the tear. Be the light. Release the prison.")
    return 0


class Tests(unittest.TestCase):
    def test_hidden_pain(self):
        s = SoulInPain("Alice", False, True)
        w = Witness("Bob", True, True)
        self.assertIn("HIDDEN", witness_tear(s, w))

    def test_unseen_pain(self):
        s = SoulInPain("Alice", True, True)
        w = Witness("Bob", False, False)
        self.assertIn("UNSEEN", witness_tear(s, w))

    def test_release_through_compassion(self):
        s = SoulInPain("Alice", True, True)
        w = Witness("Bob", True, True)
        self.assertIn("RELEASE", witness_tear(s, w))
        self.assertIn("prism", witness_tear(s, w))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
