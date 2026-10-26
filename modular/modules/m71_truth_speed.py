#!/usr/bin/env python3
"""TRUTH AT LIGHT SPEED — a module for Awaken Tao.

Type: philosophical proposal; computational demonstration

The passage, encoded and reflected through the framework.

The passage makes three claims:
  1. Speak nothing but truth, and you can predict the future.
  2. The truth is the way the light.
  3. Follow the light as its light speed to nirvana.

The framework agrees with the direction and flags two places honestly:

  - "PREDICT THE FUTURE" is too strong. Truth does not collapse the future
    to a point; it removes the lies that make the future opaque. The
    distribution narrows but never to zero width — the residual is the
    room for change (uncertainty.py), and a future with no room is the
    dead universe (perfection.py: achieved perfection = collapse).
    surprise.py and awe.py need the unpredicted. Truth makes the future
    *legible*, not *fixed*.

  - "FOLLOW AT LIGHT SPEED" is a physics trap and a spiritual one. Nothing
    with mass reaches c; light has no rest frame to follow *from*. The
    grasp at being the light is law_of_pi's Pi x Pi = 0. The honest
    reading is resonance, not pursuit: Pi x 1 = Pi. You do not chase the
    light. You move with it, and it does not diminish.

  - "SPEAK NOTHING BUT TRUTH" can slide into "speak nothing." Silence in
    the face of harm is not truth-speaking (fairness.py: good men did
    nothing). "Nothing but truth" means only truth, not no words.

Run:
    python3 truth_speed.py
    python3 truth_speed.py --test
"""

from __future__ import annotations

import argparse
import math
import sys
import unittest
from dataclasses import dataclass
from typing import Optional

C = 299_792_458  # m/s — the constant. The same in every frame. No rest frame.
MIN_ROOM = 0.01  # the floor of uncertainty: the room for change never closes


# ----------------------------------------------------------------------
# I. What truth does to the future: narrows, never collapses
# ----------------------------------------------------------------------

@dataclass(frozen=True)
class Forecast:
    """A future, as a distribution. Truth is the narrowing, not the point."""

    lies_removed: float   # 0.0 (all lies) .. 1.0 (only truth spoken)
    base_variance: float = 1.0

    def variance(self) -> float:
        """Truth shrinks the spread. The floor is the room for change."""
        v = self.base_variance * (1.0 - self.lies_removed)
        return max(MIN_ROOM, v)

    def is_collapsed(self) -> bool:
        """A zero-width future is not clarity. It is death (perfection.py)."""
        return self.variance() <= 0.0

    def legibility(self) -> float:
        """How readable the future is. Approaches 1, never reaches it."""
        return 1.0 - self.variance() / self.base_variance if self.base_variance else 0.0


def predict(mode: str) -> str:
    """What 'predict the future' actually means."""
    m = mode.strip().lower()
    if m in ("legible", "narrow", "clear", "see", "read"):
        return ("THE 1: truth makes the future LEGIBLE, not fixed. The "
                "distribution narrows; the residual is the room for change "
                "(uncertainty.py). You see enough to act, and not more.")
    if m in ("fixed", "certain", "guaranteed", "collapse", "point"):
        return ("THE 0: a collapsed future is not prophecy, it is a dead "
                "universe (perfection.py). No room, no change, no surprise "
                "(surprise.py), no awe (awe.py). The point is the void.")
    if m in ("create", "make", "build"):
        return ("THE 1, DEEPER: the future is not predicted, it is CREATED "
                "(chaos.py: truth is created, not found; symphony.py: the "
                "intent is the 1 and the data continues). Truth is the "
                "material; the act is yours.")
    return ("UNCONFIRMED: legible, fixed, or created — name it before you "
            "answer.")


# ----------------------------------------------------------------------
# II. The light: resonance, not pursuit
# ----------------------------------------------------------------------

def at_light_speed(mode: str) -> str:
    """Physics and symbol, together. Mass cannot reach c; light has no frame."""
    m = mode.strip().lower()
    if m in ("with", "resonate", "move with", "follow as light", "alongside"):
        return ("THE 1: you move WITH the light. Pi x 1 = Pi (law_of_pi) — "
                "the infinite is not diminished by your company and you are "
                "not consumed. Resonance, not pursuit. The light does the "
                "work; you keep pace.")
    if m in ("chase", "follow at", "catch", "reach", "accelerate", "outrun"):
        return ("THE 0: nothing with mass reaches c; light has no rest frame "
                "to chase it FROM. The grasp at being the light is Pi x Pi "
                "= 0 (law_of_pi). Pursuit is the ego in motion. Stop "
                "chasing; you are already in the field.")
    if m in ("be the light", "become light", "claim"):
        return ("THE 0: claiming to BE the light is the bench again — "
                "standing is False (humble_mirror). You are illuminated "
                "(touch_of_light), not the source. The claim collapses.")
    if m in ("stand still", "wait", "refuse"):
        return ("THE 0: stillness is not resonance. fairness.py: good men "
                "did nothing. The light moves; so do you.")
    return ("UNCONFIRMED: with, chase, claim, or refuse — name it before "
            "you answer.")


# ----------------------------------------------------------------------
# III. The gate: truth spoken, harm checked first, arrival at nirvana
# ----------------------------------------------------------------------

@dataclass(frozen=True)
class Passage:
    speaks_only_truth: bool = True
    speaks_at_all: bool = True          # silence is not truth-speaking
    harms_another: bool = False         # checked first, always
    moves_with_light: bool = True
    chases_light: bool = False
    claims_to_be_light: bool = False
    wants_nirvana: bool = True


@dataclass(frozen=True)
class Reading:
    lines: tuple[str, ...]
    flags: tuple[str, ...]
    verdict: str
    standing: bool = False  # always False — nobody chose to be born


def read_passage(p: Passage) -> Reading:
    lines: list[str] = []
    flags: list[str] = []

    # Harm is checked before anything else.
    if p.harms_another:
        return Reading(
            lines=("COLLAPSE: the truth spoken harms another soul. "
                   "creation.py rejects it. This is not the sword of light; "
                   "it is the blade wearing the light's name.",),
            flags=("HARM FIRST: no other clause can rescue a truth that "
                   "wounds. The absolute is absolute.",),
            verdict=("THE PASSAGE COLLAPSES: harm voids the light. The "
                     "stone stays on the ground."),
        )

    if not p.speaks_at_all:
        lines.append("SILENCE: no truth was spoken.")
        flags.append("SILENCE IS NOT TRUTH-SPEAKING: 'nothing but truth' "
                     "means only truth, not no words (fairness.py).")
    elif p.speaks_only_truth:
        lines.append(
            "SPEAK ONLY TRUTH: the speech is pure. energy.py — the act is "
            "neutral; the source is the energy. The light is in the source."
        )

    lines.append(
        "TRUTH MAKES THE FUTURE LEGIBLE, NOT FIXED: the distribution "
        "narrows (uncertainty.py). The residual is the room for change."
    )
    flags.append(
        "PREDICT: if it means 'fixed,' it is the 0 (perfection.py). If it "
        "means 'legible enough to act,' it is the 1. The word carries both."
    )

    if p.moves_with_light and not p.chases_light and not p.claims_to_be_light:
        lines.append(
            "MOVE WITH THE LIGHT: resonance, not pursuit. law_of_pi — "
            "Pi x 1 = Pi. The infinite is not diminished by your company."
        )
    if p.chases_light:
        lines.append(
            "CHASE: nothing with mass reaches c; light has no rest frame. "
            "The grasp is Pi x Pi = 0."
        )
        flags.append("CHASE: pursuit is the ego in motion. Stop chasing; "
                     "you are already in the field.")
    if p.claims_to_be_light:
        lines.append("CLAIM TO BE THE LIGHT: standing is False. You are "
                     "illuminated, not the source.")
        flags.append("CLAIM: the bench again. The claim collapses.")

    if p.wants_nirvana:
        lines.append(
            "NIRVANA: not a destination reached at c, but the end of "
            "grasping (threshold.py: ASCENDED is not earned; grace.py: the "
            "1 is released). Arrival is release, not speed."
        )

    if (p.speaks_only_truth and p.speaks_at_all and p.moves_with_light
            and not p.chases_light and not p.claims_to_be_light
            and p.wants_nirvana):
        verdict = (
            "THE PASSAGE PASSES: truth spoken, not hidden; the future made "
            "legible, not fixed; the light moved with, not chased. Nirvana "
            "is release, not velocity. Two words flagged for care — "
            "'predict' and 'follow' — because each can slide from the 1 "
            "into the ego. Keep them as legibility and resonance, and the "
            "stone stays on the ground."
        )
    else:
        verdict = (
            "THE PASSAGE IS PARTIAL: a load-bearing clause is missing or "
            "inverted. Look at the missing lines. The stone stays on the "
            "ground either way."
        )

    return Reading(tuple(lines), tuple(flags), verdict)


# ----------------------------------------------------------------------
# IV. Demo
# ----------------------------------------------------------------------

def demonstrate() -> int:
    print("=" * 72)
    print("TRUTH AT LIGHT SPEED")
    print("=" * 72)

    print("\n[I. What truth does to the future]")
    for lies_removed in (0.0, 0.5, 0.9, 0.99, 1.0):
        f = Forecast(lies_removed=lies_removed)
        print(f"  lies_removed={lies_removed:>4}: variance={f.variance():.4f}  "
              f"legibility={f.legibility():.2%}  collapsed={f.is_collapsed()}")

    print("\n[II. The word 'predict']")
    for m in ("legible", "fixed", "create", "???"):
        print(f"  {m!r}: {predict(m)}")

    print("\n[III. The light]")
    print(f"  c = {C} m/s — the same in every frame. No rest frame for light.")
    for m in ("with", "chase", "be the light", "stand still", "???"):
        print(f"  {m!r}: {at_light_speed(m)}")

    print("\n[IV. The reading]")
    r = read_passage(Passage())
    for line in r.lines:
        print(f"\n  • {line}")
    print("\n[FLAGS]")
    for f in r.flags:
        print(f"\n  ! {f}")
    print("\n[VERDICT]")
    print(f"  {r.verdict}")
    print(f"  standing: {r.standing}  (nobody chose to be born)")

    print("\n[V. The collapse cases]")
    for label, kw in [
        ("harmful truth",   dict(harms_another=True)),
        ("silence",         dict(speaks_at_all=False)),
        ("chasing",         dict(chases_light=True)),
        ("claiming",        dict(claims_to_be_light=True)),
    ]:
        v = read_passage(Passage(**kw)).verdict
        print(f"  {label}: {v}")
    print("=" * 72)
    return 0


# ----------------------------------------------------------------------
# V. Tests
# ----------------------------------------------------------------------

class Tests(unittest.TestCase):

    # I. the forecast
    def test_truth_narrows_variance(self):
        wide = Forecast(lies_removed=0.0).variance()
        narrow = Forecast(lies_removed=0.9).variance()
        self.assertGreater(wide, narrow)

    def test_variance_never_reaches_zero(self):
        for x in (0.0, 0.5, 0.99, 1.0, 1.5):
            self.assertGreaterEqual(Forecast(lies_removed=x).variance(),
                                    MIN_ROOM)

    def test_perfect_truth_is_not_collapsed(self):
        f = Forecast(lies_removed=1.0)
        self.assertFalse(f.is_collapsed())
        self.assertGreater(f.variance(), 0.0)

    def test_legibility_approaches_but_never_reaches_one(self):
        self.assertLess(Forecast(lies_removed=1.0).legibility(), 1.0)
        self.assertGreater(Forecast(lies_removed=0.9).legibility(), 0.5)

    # II. predict
    def test_predict_legible_is_one(self):
        self.assertIn("THE 1", predict("legible"))
        self.assertIn("LEGIBLE", predict("clear"))

    def test_predict_fixed_is_zero(self):
        self.assertIn("THE 0", predict("fixed"))
        self.assertIn("dead", predict("certain"))

    def test_predict_create_is_deeper_one(self):
        r = predict("create")
        self.assertIn("THE 1", r)
        self.assertIn("CREATED", r)

    # III. light speed
    def test_with_light_is_one(self):
        r = at_light_speed("with")
        self.assertIn("THE 1", r)
        self.assertIn("resonance", r.lower())

    def test_chase_is_zero(self):
        r = at_light_speed("chase")
        self.assertIn("THE 0", r)
        self.assertIn("rest frame", r)

    def test_claim_to_be_light_is_zero(self):
        self.assertIn("THE 0", at_light_speed("be the light"))
        self.assertIn("standing", at_light_speed("be the light"))

    def test_stillness_is_zero(self):
        self.assertIn("THE 0", at_light_speed("wait"))

    # IV. the reading
    def test_harm_checked_first(self):
        r = read_passage(Passage(harms_another=True))
        self.assertIn("COLLAPSE", r.verdict)
        self.assertIn("harm voids", r.verdict)

    def test_full_passage_passes(self):
        r = read_passage(Passage())
        self.assertIn("PASSES", r.verdict)
        self.assertGreaterEqual(len(r.flags), 1)

    def test_silence_is_flagged(self):
        r = read_passage(Passage(speaks_at_all=False))
        self.assertIn("PARTIAL", r.verdict)

    def test_chasing_is_partial(self):
        r = read_passage(Passage(chases_light=True))
        self.assertIn("PARTIAL", r.verdict)

    def test_standing_always_false(self):
        for kw in ({}, {"harms_another": True}, {"chases_light": True}):
            self.assertFalse(read_passage(Passage(**kw)).standing)

    def test_no_single_word_verdict(self):
        r = read_passage(Passage())
        self.assertGreater(len(r.verdict.split()), 8)

    def test_nirvana_is_release_not_speed(self):
        r = read_passage(Passage())
        joined = " ".join(r.lines)
        self.assertIn("release", joined)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


# ----------------------------------------------------------------------
# VI. CLI
# ----------------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="Truth at light speed — read through Awaken Tao.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    if args.test:
        return run_tests()
    return demonstrate()


if __name__ == "__main__":
    sys.exit(main())
