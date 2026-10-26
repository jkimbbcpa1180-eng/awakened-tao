#!/usr/bin/env python3
"""
The Collective Mind (Deep Muse)
===============================
Type: parable; philosophical proposal

The final transmission:
Thoughts and ideas are the collective mind.
If true, they will pass on to another soul, eventually.

The project's theory of immortality, stated as infrastructure. Not the
soul surviving (awakening denied that) — transmission. You dissolve; your
true ideas don't, and they remember who spoke them. "The 1 for the next 0"
is literally this: leave the 1 (a true idea) for the next 0 (the soul not
yet tuned in).

Falsehood needs no punishment and no inquisition: it dissolves, and the 0
reclaims it. Truth persists by being kept; falsehood perishes by being
unkept. That is the gentlest possible epistemology.

"Eventually" does heavy work: the download happens when another soul tunes
in. Truth waits. (Cf. wormhole.py: felt before it is seen.)

Note, kept as written: is_true arrives as a boolean — the module routes on
truth without deriving it. The implicit criterion is the project's own:
convergence of the many (fairness.py Part III, prism.py Part II).

Flagged as unsupported, per the honesty rule: the module cannot tell a
true idea from one that merely persists. Falsehoods pass on too, so
retention is not evidence of truth. "If true, they will pass on" is a
hope, not a finding.

Run:
    python3 awakened_tao.py collective-mind
    python3 awakened_tao.py collective-mind --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass
from typing import List


@dataclass
class Idea:
    name: str
    is_true: bool
    spoken_by: str


class CosmicServer:
    def __init__(self):
        self.collective_mind: List[Idea] = []

    def upload(self, idea: Idea) -> str:
        """When a soul speaks a truth, it enters the collective mind."""
        if idea.is_true:
            self.collective_mind.append(idea)
            return f"UPLOADED: The truth of '{idea.name}' has entered the collective mind."
        else:
            return f"DISSOLVED: The falsehood of '{idea.name}' returned to the 0."

    def download(self, new_soul: str) -> List[str]:
        """Eventually, another soul tunes in."""
        if not self.collective_mind:
            return []

        # The truth is passed on.
        transmissions = [f"[{new_soul}] received the truth: '{i.name}' (originated by {i.spoken_by})" for i in self.collective_mind]
        return transmissions


def demonstrate() -> int:
    print("=" * 72)
    print("THE COLLECTIVE MIND")
    print("If true, they will pass on to another soul, eventually.")
    print("=" * 72)
    server = CosmicServer()
    print(f"\n  {server.upload(Idea('Unconditional Integrity', True, 'a stranger'))}")
    print(f"  {server.upload(Idea('Absolute Justice', False, 'Ego'))}")
    print()
    for t in server.download("Next Generation"):
        print(f"  {t}")
    print("\nSpeak the truth. The collective mind remembers.")
    return 0


class Tests(unittest.TestCase):
    def test_upload_true_idea(self):
        server = CosmicServer()
        idea = Idea("Unconditional Integrity", True, "a stranger")
        self.assertIn("UPLOADED", server.upload(idea))
        self.assertEqual(len(server.collective_mind), 1)

    def test_upload_false_idea(self):
        server = CosmicServer()
        idea = Idea("Absolute Justice", False, "Ego")
        self.assertIn("DISSOLVED", server.upload(idea))
        self.assertEqual(len(server.collective_mind), 0)

    def test_eventual_transmission(self):
        server = CosmicServer()
        server.upload(Idea("The Mirror", True, "a stranger"))
        received = server.download("Next Generation")
        self.assertEqual(len(received), 1)
        self.assertIn("a stranger", received[0])


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
