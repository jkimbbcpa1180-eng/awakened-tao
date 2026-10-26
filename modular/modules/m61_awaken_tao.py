#!/usr/bin/env python3
"""
AWAKEN TAO
==========
Type: parable; computational demonstration

The Executable Philosophy of the 1.

This script models the complete architecture of the Deep Muse:
  1. The Physics of 010101 (The Void and the Spark)
  2. The Mirror and the Prism (Reflecting truth, fracturing light)
  3. The Warrior's Charge (Running toward the survival game)
  4. The Two Cheeks (Grace vs. Boundaries)
  5. The Karmic Math (The 000 and the Forced Cross)
  6. The Earned Rest (Resting not from comfort, but from victory)

v4 fixes: the strikes answer is parsed safely ('3+', 'three', bad input
defaults to 1); zero strikes means NO WRONG DONE; the cosmic smite asks
whether justice was mocked instead of assuming it; an empty truth has a
fallback; the default command is a non-interactive demo, and the
interactive version runs only with --reflect.

Labeled as metaphor, per the honesty rule: speak_to_existence says the
universe "must manifest" a pure truth. No physical law does that; it is
the parable's claim, and the printed verdict now says so.

Run:
    python3 awakened_tao.py awaken-tao
    python3 awakened_tao.py awaken-tao --reflect
    python3 awakened_tao.py awaken-tao --test
"""
from __future__ import annotations
import sys
import unittest
from dataclasses import dataclass
from typing import List


@dataclass
class Cosmos:
    is_running: bool = True

    def breathe(self) -> str:
        """The eternal loop of the void and the spark."""
        return "0 (The Void) -> 1 (The Spark) -> 0 (The Return) -> 1 (The Rebirth)"


@dataclass
class Soul:
    name: str
    has_ego: bool
    has_suffered: bool
    seeks_truth: bool
    leaves_a_1: bool


_WORDS = {"zero": 0, "none": 0, "no": 0, "one": 1, "once": 1, "two": 2, "twice": 2,
          "three": 3, "four": 4, "five": 5, "many": 3}


def parse_strikes(answer) -> int:
    """'3+', 'three', '2' -> int. Anything unreadable defaults to 1."""
    text = str(answer).strip().lower().rstrip("+").strip()
    if text.isdigit():
        return int(text)
    if text in _WORDS:
        return _WORDS[text]
    return 1


def parse_yes(answer) -> bool:
    return str(answer).strip().lower() in ("y", "yes", "yeah", "yep", "true", "1")


class AwakenTao:
    def __init__(self):
        self.karma_ledger: List[dict] = []

    def let_ego_sink_in(self, soul: Soul, flaw: str) -> str:
        """The paradox of the Ego: If you fight it, it grows.
        If you let it sink in, you find the truth to let it go."""
        if not soul.has_ego:
            return "You have no Ego to sink. The void is already clear."
        soul.has_ego = False
        flaw = flaw.strip() or "an unnamed flaw"
        return f"Soul {soul.name} let the flaw '{flaw}' sink in. The truth was found. The Ego dissolved into the 0."

    def turn_the_cheek(self, soul: Soul, strikes_received: int) -> str:
        """The Law of the Two Cheeks. Grace is given twice. On the third strike, the warrior fights back."""
        if strikes_received <= 0:
            return f"[{soul.name}] NO WRONG DONE: No strike was received. Walk in peace."
        if strikes_received <= 2:
            return f"[{soul.name}] GRACE: You turn the cheek. You offer compromise. The 1 is tested."
        return f"[{soul.name}] THE 1 FIGHTS BACK: No more cheeks to turn. You use authority, not vigilante vengeance."

    def cosmic_smite(self, oppressor: str, mocked_justice: bool) -> str:
        """The Law of Karma. Not eternal damnation. They must live the life of the offended."""
        if mocked_justice:
            self.karma_ledger.append({"oppressor": oppressor, "verdict": "THE 000",
                                      "penalty": "Live the life of the offended. Learn twice."})
            return (f"[{oppressor}] THE COSMIC SMITE (THE 000): They will have to learn "
                    f"what it felt like to be on the other side.")
        return f"[{oppressor}] THE 1: You did not mock justice. You are at peace."

    def speak_to_existence(self, truth: str, is_pure: bool) -> str:
        """Ontological Creation. If it is pure and harms none, the universe must manifest it."""
        if not str(truth).strip():
            return "SILENCE: No truth was spoken yet. The 0 waits for your word."
        if not is_pure:
            return "DISTORTION: The truth is impure. The wormhole closes."
        return f"MANIFESTED: '{truth}' is spoken into existence. Within this parable: The cosmos bends time to make it real."


def _verdict(soul: Soul) -> None:
    print("=" * 74); print("THE FINAL VERDICT"); print("=" * 74)
    print(f"Welcome to the Awaken Tao, {soul.name}.")
    print("You have the toothpick. You have the mirror. You have the 555.")
    print("You are ready to leave a 1 for tomorrow.")
    print("=" * 74)


def demonstrate() -> int:
    """Non-interactive walk-through with sample answers."""
    print("=" * 74); print("AWAKEN TAO: THE MIRROR OF THE 1 (demo)"); print("=" * 74)
    print("You are not here to escape the survival game.")
    print("You are here to run toward it, and come out saying, 'Is that all you got?'\n")
    tao = AwakenTao()
    soul = Soul("You", has_ego=True, has_suffered=True, seeks_truth=True, leaves_a_1=True)
    print(f"  {Cosmos().breathe()}\n")
    print(f"> {tao.let_ego_sink_in(soul, 'fear')}")
    for s in ("0", "2", "3+"):
        print(f"> strikes '{s}': {tao.turn_the_cheek(soul, parse_strikes(s))}")
    print(f"> {tao.cosmic_smite('The Tyrant', True)}")
    print(f"> {tao.cosmic_smite('The Neighbor', False)}")
    print(f"> {tao.speak_to_existence('Unconditional Love', True)}")
    print(f"> {tao.speak_to_existence('', True)}\n")
    _verdict(soul)
    return 0


def reflect() -> int:
    """Interactive version (only with --reflect)."""
    print("=" * 74); print("AWAKEN TAO: THE MIRROR OF THE 1"); print("=" * 74)
    print("You are not here to escape the survival game.")
    print("You are here to run toward it, and come out saying, 'Is that all you got?'\n")
    tao = AwakenTao()
    soul = Soul("You", has_ego=True, has_suffered=True, seeks_truth=True, leaves_a_1=True)
    try:
        flaw = input("What is a flaw you are carrying right now? (e.g., fear, anger, shame): ")
        print(f"\n> {tao.let_ego_sink_in(soul, flaw)}\n")
        strikes = parse_strikes(input("How many times has someone wronged you? (0, 1, 2, or 3+): "))
        print(f"> {tao.turn_the_cheek(soul, strikes)}\n")
        oppressor = input("Who has mocked justice or taken advantage of you? (Leave blank if none): ")
        if oppressor.strip():
            mocked = parse_yes(input("Did they mock justice? (yes/no): "))
            print(f"> {tao.cosmic_smite(oppressor.strip(), mocked)}\n")
        truth = input("What is a truth you want to speak into existence for your next 0? ")
        print(f"> {tao.speak_to_existence(truth, is_pure=True)}\n")
    except EOFError:
        print("\n(No more input. The mirror waits.)\n")
    _verdict(soul)
    return 0


class TestAwakenTao(unittest.TestCase):
    def setUp(self):
        self.tao = AwakenTao()
        self.soul = Soul("John", has_ego=True, has_suffered=True, seeks_truth=True, leaves_a_1=True)

    def test_ego_dissolution(self):
        r = self.tao.let_ego_sink_in(self.soul, "pride")
        self.assertIn("Ego dissolved", r); self.assertFalse(self.soul.has_ego)

    def test_two_cheeks(self):
        self.assertIn("GRACE", self.tao.turn_the_cheek(self.soul, 1))
        self.assertIn("GRACE", self.tao.turn_the_cheek(self.soul, 2))
        self.assertIn("FIGHTS BACK", self.tao.turn_the_cheek(self.soul, 3))

    def test_cosmic_smite(self):
        r = self.tao.cosmic_smite("The Tyrant", mocked_justice=True)
        self.assertIn("THE COSMIC SMITE", r); self.assertEqual(len(self.tao.karma_ledger), 1)

    def test_speak_truth(self):
        self.assertIn("MANIFESTED", self.tao.speak_to_existence("Unconditional Love", is_pure=True))

    # v4 additions
    def test_no_wrong_done(self):
        self.assertIn("NO WRONG DONE", self.tao.turn_the_cheek(self.soul, 0))
        self.assertIn("NO WRONG DONE", self.tao.turn_the_cheek(self.soul, -1))

    def test_parse_strikes(self):
        self.assertEqual(parse_strikes("3+"), 3)
        self.assertEqual(parse_strikes("three"), 3)
        self.assertEqual(parse_strikes("2"), 2)
        self.assertEqual(parse_strikes("banana"), 1)
        self.assertEqual(parse_strikes(""), 1)

    def test_smite_softened_and_labeled(self):
        r = self.tao.cosmic_smite("The Tyrant", True)
        self.assertIn("THE 000", r)
        self.assertIn("They will have to learn what it felt like to be on the other side.", r)

    def test_smite_not_mocked(self):
        self.assertIn("THE 1", self.tao.cosmic_smite("Someone", False))
        self.assertEqual(self.tao.karma_ledger, [])
        self.assertTrue(parse_yes("Yes")); self.assertFalse(parse_yes("no")); self.assertFalse(parse_yes(""))

    def test_empty_truth_fallback(self):
        self.assertIn("SILENCE", self.tao.speak_to_existence("", True))
        self.assertIn("SILENCE", self.tao.speak_to_existence("   ", False))

    def test_reflect_without_input_does_not_block(self):
        import io, contextlib
        old = sys.stdin
        sys.stdin = io.StringIO("")
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(reflect(), 0)
        finally:
            sys.stdin = old


Tests = TestAwakenTao


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestAwakenTao)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    if "--test" in sys.argv:
        sys.exit(run_tests())
    if "--reflect" in sys.argv:
        sys.exit(reflect())
    sys.exit(demonstrate())
