#!/usr/bin/env python3
"""the_real_satire.py — real satirical journalism, informed on both sides.

Type: policy proposal

The form, corrected:

  The frame is fabricated. The documentation is real. And both the
  subject and the audience are told.

  Two disclosures, both required:
    - THE SUBJECT is told, before filming, that this is satirical
      media, and consents after disclosure.
    - THE AUDIENCE is told the persona is fictional.

  Without the subject disclosure, the reaction is a gotcha, not
  documentation. That is the manipulation of humiliation — the subject
  is ambushed into revealing something, and the reveal is not a choice
  they made knowing the frame. The module calls this MANIPULATION.

  Without the audience disclosure, the public is being deceived even
  though the subject was not. The module calls this DECEPTION OF
  PUBLIC.

  The hard fakes remain fakes: fabricated quotes, composite footage,
  AI-generated subjects. "Anything else is fake" — agreed.

WHAT THIS COSTS, named in the module:

  BORAT, AS ACTUALLY MADE, NOW FAILS. The subjects were not told. The
  ambush was the engine. Strip the ambush and the subjects guard; what
  is exposed is no longer what they would have said unguarded. The
  result is a smaller, cleaner form — informed satire — where every
  reaction is a choice the subject made knowing the frame. That is the
  ethical cost of the correction, and it is not hidden.

Fix: restored the fictional-persona check. A piece with no fictional
  frame now returns NOT REAL SATIRE before the disclosure checks;
  before, it could pass as REAL INFORMED SATIRE.
Fix: a piece that both punches up and harms ordinary people now names
  both tensions; before, only the punching-up line was shown.
Fix: added subject_approved_cut_after (default False). A subject not
  told before filming who is shown the cut and consents to publication
  afterward is CONTESTED, not MANIPULATION: post-hoc consent is not
  advance consent. This agrees with The Ambush Trade's Regime B.
  Borat as made (no after-consent) is still MANIPULATION.

Run:
    python3 the_real_satire.py
    python3 the_real_satire.py --test
"""

from __future__ import annotations
import argparse
import sys
import unittest
from dataclasses import dataclass


@dataclass(frozen=True)
class Piece:
    name: str
    subjects_real: bool
    reactions_unscripted: bool
    persona_fictional: bool
    subject_told_satirical_media: bool        # BEFORE filming
    subject_consented_after_disclosure: bool
    audience_told_persona_fictional: bool
    fabricated_quotes: bool = False
    composite_footage: bool = False
    ai_subjects: bool = False
    punches_up: bool = False
    harms_ordinary_people: bool = False
    subject_approved_cut_after: bool = False  # shown the cut, consented to publish


@dataclass(frozen=True)
class Verdict:
    piece: str
    outcome: str
    reason: str
    cost: str = ""


def gate(p: Piece) -> Verdict:
    # --- Hard fakes. Any one of these and it is not real. ---
    if p.fabricated_quotes:
        return Verdict(p.name, "FAKE",
            "Fabricated quotes attributed to real people. "
            "The documentation is not real.")
    if p.composite_footage:
        return Verdict(p.name, "FAKE",
            "Composite footage presented as one event. "
            "The documentation is not real.")
    if p.ai_subjects:
        return Verdict(p.name, "FAKE",
            "AI-generated subjects presented as real interviewees. "
            "The documentation is not real.")

    # --- Real subjects and real reactions. ---
    if not (p.subjects_real and p.reactions_unscripted):
        return Verdict(p.name, "NOT REAL",
            "No real subjects, or the reactions are scripted. "
            "Satire requires real people and real reactions.")

    # --- There must be a fictional frame. ---
    if not p.persona_fictional:
        return Verdict(p.name, "NOT REAL SATIRE",
            "No fictional frame. Without a fictional persona this is "
            "an interview or a documentary, not satire.")

    # --- The subject must know, before filming. ---
    if not p.subject_told_satirical_media and p.subject_approved_cut_after:
        if not p.audience_told_persona_fictional:
            return Verdict(p.name, "DECEPTION OF PUBLIC",
                "The subject approved the cut afterward, but the audience "
                "is not told the persona is fictional. The public is "
                "being deceived.")
        ordinary = (" AND the target is ordinary — post-hoc consent "
                    "cannot undo that they were filmed without knowing."
                    if p.harms_ordinary_people else "")
        return Verdict(p.name, "CONTESTED",
            "The subject was not told before filming, but was shown the "
            "cut and consented to publication afterward. Post-hoc "
            "consent is not advance consent.",
            cost=("COST: the most revealing material is often exactly "
                  "what gets vetoed. What publishes is the intersection: "
                  "unguarded AND consented." + ordinary))

    if not p.subject_told_satirical_media:
        return Verdict(p.name, "MANIPULATION",
            "The subject was not told this is satirical media before "
            "filming. The reaction is a gotcha, not documentation. "
            "This is the manipulation of humiliation.",
            cost=("COST: this is Borat, as actually made. The ambush "
                  "engine is what fails here. Strip the ambush and the "
                  "form becomes informed satire — smaller, cleaner, "
                  "and no longer capable of exposing what an unguarded "
                  "subject would have said."))

    if not p.subject_consented_after_disclosure:
        return Verdict(p.name, "NO CONSENT",
            "Subject was told this is satirical media, but did not "
            "consent to participate after disclosure.")

    # --- The audience must know the persona is fictional. ---
    if not p.audience_told_persona_fictional:
        return Verdict(p.name, "DECEPTION OF PUBLIC",
            "Subject informed, but the audience is not told the persona "
            "is fictional. The public is being deceived even though the "
            "subject was not.")

    # --- Real informed satire. Name the ethical tension if present. ---
    tensions = []
    if p.punches_up:
        tensions.append("TENSION: the form still has a cost — even informed "
                "subjects can be made to look foolish. But the reaction "
                "is a choice they made knowing the frame, not a gotcha.")
    if p.harms_ordinary_people:
        tensions.append("TENSION: real and informed, but it targets ordinary "
                "people who never held power. Legal under this gate, "
                "ethically costly. The form's choice is visible.")
    cost = " ".join(tensions)

    return Verdict(p.name, "REAL INFORMED SATIRE",
        "Real subjects, unscripted reactions, subject told before "
        "filming that this is satirical media and consented, audience "
        "told the persona is fictional, no fabrication. The reaction "
        "is informed.",
        cost=cost)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

PIECES = [
    Piece("Borat as actually made (ambush, subject not told)",
          subjects_real=True, reactions_unscripted=True,
          persona_fictional=True,
          subject_told_satirical_media=False,
          subject_consented_after_disclosure=False,
          audience_told_persona_fictional=True),
    Piece("ambush, but the subject approved the cut afterward",
          subjects_real=True, reactions_unscripted=True,
          persona_fictional=True,
          subject_told_satirical_media=False,
          subject_consented_after_disclosure=False,
          audience_told_persona_fictional=True,
          subject_approved_cut_after=True),
    Piece("informed satire: subject told, consents, speaks freely",
          subjects_real=True, reactions_unscripted=True,
          persona_fictional=True,
          subject_told_satirical_media=True,
          subject_consented_after_disclosure=True,
          audience_told_persona_fictional=True,
          punches_up=True),
    Piece("subject told, consent refused, still published",
          subjects_real=True, reactions_unscripted=True,
          persona_fictional=True,
          subject_told_satirical_media=True,
          subject_consented_after_disclosure=False,
          audience_told_persona_fictional=True),
    Piece("subject informed, audience not",
          subjects_real=True, reactions_unscripted=True,
          persona_fictional=True,
          subject_told_satirical_media=True,
          subject_consented_after_disclosure=True,
          audience_told_persona_fictional=False),
    Piece("informed satire targeting ordinary people",
          subjects_real=True, reactions_unscripted=True,
          persona_fictional=True,
          subject_told_satirical_media=True,
          subject_consented_after_disclosure=True,
          audience_told_persona_fictional=True,
          harms_ordinary_people=True),
    Piece("fabricated quote attributed to a real politician",
          subjects_real=True, reactions_unscripted=False,
          persona_fictional=False,
          subject_told_satirical_media=False,
          subject_consented_after_disclosure=False,
          audience_told_persona_fictional=True,
          fabricated_quotes=True),
    Piece("composite of real clips as one event",
          subjects_real=True, reactions_unscripted=True,
          persona_fictional=True,
          subject_told_satirical_media=True,
          subject_consented_after_disclosure=True,
          audience_told_persona_fictional=True,
          composite_footage=True),
    Piece("AI-generated man-on-the-street interviews",
          subjects_real=False, reactions_unscripted=False,
          persona_fictional=True,
          subject_told_satirical_media=False,
          subject_consented_after_disclosure=False,
          audience_told_persona_fictional=True,
          ai_subjects=True),
]


def demonstrate() -> int:
    print("=" * 72)
    print("THE REAL SATIRE — real documentation, informed on both sides")
    print("=" * 72)
    for p in PIECES:
        v = gate(p)
        print(f"\n  {v.piece}")
        print(f"    [{v.outcome}] {v.reason}")
        if v.cost:
            print(f"    {v.cost}")

    print("\n" + "=" * 72)
    print("Real satirical journalism requires BOTH disclosures:")
    print("  - the subject is told, before filming, and consents;")
    print("  - the audience is told the persona is fictional.")
    print()
    print("Borat as made fails the first. Informed satire passes both.")
    print("The ambush engine is gone; that is the ethical cost.")
    print("=" * 72)
    return 0


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestHardFakes(unittest.TestCase):
    def test_fabricated_quotes_fake(self):
        p = Piece("x", True, True, True, True, True, True, fabricated_quotes=True)
        self.assertEqual(gate(p).outcome, "FAKE")

    def test_composite_footage_fake(self):
        p = Piece("x", True, True, True, True, True, True, composite_footage=True)
        self.assertEqual(gate(p).outcome, "FAKE")

    def test_ai_subjects_fake(self):
        p = Piece("x", False, False, True, False, False, True, ai_subjects=True)
        self.assertEqual(gate(p).outcome, "FAKE")


class TestRealness(unittest.TestCase):
    def test_scripted_reactions_not_real(self):
        p = Piece("x", True, False, True, True, True, True)
        self.assertEqual(gate(p).outcome, "NOT REAL")

    def test_unreal_subjects_not_real(self):
        p = Piece("x", False, True, True, True, True, True)
        self.assertEqual(gate(p).outcome, "NOT REAL")


class TestBothDisclosures(unittest.TestCase):
    def test_borat_as_made_is_manipulation(self):
        # The subject was not told. This is the correction.
        p = Piece("Borat", True, True, True,
                  subject_told_satirical_media=False,
                  subject_consented_after_disclosure=False,
                  audience_told_persona_fictional=True)
        v = gate(p)
        self.assertEqual(v.outcome, "MANIPULATION")
        self.assertIn("gotcha", v.reason.lower())
        self.assertIn("humiliation", v.reason.lower())

    def test_borat_cost_named(self):
        p = Piece("Borat", True, True, True, False, False, True)
        v = gate(p)
        self.assertIn("ambush", v.cost.lower())

    def test_subject_told_audience_told_is_real(self):
        p = Piece("informed satire", True, True, True, True, True, True,
                  punches_up=True)
        v = gate(p)
        self.assertEqual(v.outcome, "REAL INFORMED SATIRE")
        self.assertIn("informed", v.reason.lower())

    def test_subject_told_audience_not_told_is_deception_of_public(self):
        p = Piece("x", True, True, True, True, True, False)
        self.assertEqual(gate(p).outcome, "DECEPTION OF PUBLIC")

    def test_subject_told_no_consent(self):
        p = Piece("x", True, True, True, True, False, True)
        self.assertEqual(gate(p).outcome, "NO CONSENT")


class TestTensions(unittest.TestCase):
    def test_punching_up_names_cost(self):
        p = Piece("x", True, True, True, True, True, True, punches_up=True)
        v = gate(p)
        self.assertIn("tension", v.cost.lower())

    def test_harming_ordinary_people_names_tension(self):
        p = Piece("x", True, True, True, True, True, True,
                  harms_ordinary_people=True)
        v = gate(p)
        self.assertIn("ordinary people", v.cost.lower())


class TestFixes(unittest.TestCase):
    def test_no_fictional_frame_is_not_real_satire(self):
        p = Piece("x", True, True, False, True, True, True)
        v = gate(p)
        self.assertEqual(v.outcome, "NOT REAL SATIRE")
        self.assertIn("no fictional frame", v.reason.lower())

    def test_punches_up_and_harms_ordinary_names_both(self):
        p = Piece("x", True, True, True, True, True, True,
                  punches_up=True, harms_ordinary_people=True)
        v = gate(p)
        self.assertEqual(v.outcome, "REAL INFORMED SATIRE")
        self.assertIn("look foolish", v.cost.lower())
        self.assertIn("ordinary people", v.cost.lower())

    def test_approved_cut_after_is_contested(self):
        p = Piece("x", True, True, True, False, False, True,
                  subject_approved_cut_after=True)
        v = gate(p)
        self.assertEqual(v.outcome, "CONTESTED")
        self.assertIn("post-hoc consent is not advance consent",
                      v.reason.lower())

    def test_borat_without_after_consent_still_manipulation(self):
        p = Piece("Borat", True, True, True, False, False, True,
                  subject_approved_cut_after=False)
        self.assertEqual(gate(p).outcome, "MANIPULATION")


class TestHonesty(unittest.TestCase):
    def test_no_forbidden_verdict_words(self):
        ns = globals()
        for bad in ("SAVED", "DAMNED", "ADDICT", "LAZY"):
            self.assertFalse(any(bad in n.upper() for n in ns), bad)

    def test_borat_is_called_out_explicitly(self):
        # The module must not quietly pass Borat. The docstring and the
        # demo both name it. The test ensures the docstring does.
        doc = __doc__.lower()
        self.assertIn("borat, as actually made, now fails", doc)


def run_tests() -> int:
    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()
    for case in (TestHardFakes, TestRealness, TestBothDisclosures,
                 TestTensions, TestFixes, TestHonesty):
        suite.addTests(loader.loadTestsFromTestCase(case))
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Real satirical journalism: informed on both sides.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    return run_tests() if args.test else demonstrate()


if __name__ == "__main__":
    sys.exit(main())
