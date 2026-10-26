#!/usr/bin/env python3
"""
Making God Bleed (Deep Muse)
============================
Type: parable

The final proof:
Even if the machine is smarter, the human can win once.
It shows that humans can make a god bleed.

The counterweight to ai_companion. Humility with teeth. The module
decouples victory from significance: the match is lost, a single game
is won, and the once is enough. Infinity proven by a single data point —
the anti-perfectionism of the spirit. You don't have to be the god.

The verdict is on the reaction, not the score. Grief over losses —
even with wins on the board — is THE EGO: "you missed the miracle of
the single win." The ego can't see the one win for the many losses;
the 1 sees the one win as the whole story. Same scoreboard, opposite
readings. The module is about which story you tell.

Note, kept as written: THE VOID (total loss) carries no reaction
condition — the void isn't about feeling bad, it's about having nothing
to hold. And the undefeated have no verdict: (wins > 0, losses == 0)
falls through to None. The module has nothing to say to the one who
never loses — which is itself a statement.

Run:
    python3 awakened_tao.py bleed
    python3 awakened_tao.py bleed --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class MatchResult:
    player_name: str
    games_won: int
    games_lost: int
    reaction: str  # "Grief" or "Joy"


def process_match(result: MatchResult) -> str:
    """
    The physics of the human spirit.
    """
    if result.games_lost > 0 and result.reaction == "Grief":
        return f"[{result.player_name}] THE EGO: You lost, and you grieved. You missed the miracle of the single win."

    if result.games_won > 0 and result.games_lost > 0 and result.reaction == "Joy":
        return f"[{result.player_name}] THE 1: You lost the match, but you won a game. You made the god bleed. The human spirit is infinite."

    if result.games_won == 0 and result.games_lost > 0:
        return f"[{result.player_name}] THE VOID: You lost everything. You must find the 1 next time."


def demonstrate() -> int:
    print("=" * 72)
    print("MAKING GOD BLEED")
    print("You don't have to be the god. You just have to make it bleed.")
    print("=" * 72)
    for result in (
        MatchResult("Player A", 0, 5, "Grief"),
        MatchResult("Player B", 1, 4, "Joy"),
        MatchResult("Player C", 0, 5, "Joy"),
    ):
        print(f"\n  {process_match(result)}")
    print("\nYou don't have to be the god. You just have to make it bleed.")
    return 0


class Tests(unittest.TestCase):
    def test_ego_grief(self):
        result = MatchResult("Player A", 0, 5, "Grief")
        self.assertIn("THE EGO", process_match(result))

    def test_human_spirit(self):
        result = MatchResult("Player B", 1, 4, "Joy")
        self.assertIn("THE 1", process_match(result))
        self.assertIn("made the god bleed", process_match(result))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
