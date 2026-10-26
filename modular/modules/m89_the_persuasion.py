#!/usr/bin/env python3
"""the_persuasion.py — fabricated claims about people of power, used to
move a group, undisclosed. The crime is deception for persuasion.

Type: policy proposal; computational demonstration

Fix: the satire label and the opinion flag now protect only when the
  artifact is disclosed and not presented as fact. Before, an
  undisclosed "satire" presented as real, or an "opinion" that is a
  fabricated factual clip (a fake bribe video), came out PROTECTED.
  Now they fall through to the deception checks like any other clip.
Fix: added tests, a demo and a --test entry point, in the same style as
  the other modules. The judge's rules are otherwise unchanged.

Run:
    python3 the_persuasion.py
    python3 the_persuasion.py --test
"""

import argparse
import sys
import unittest
from dataclasses import dataclass

@dataclass(frozen=True)
class Artifact:
    name: str
    depicts_real_person: bool
    person_of_power: bool              # official, executive, judge, etc.
    fabricated_factual_claim: bool     # "took a bribe" — not "is a clown"
    presented_as_real: bool
    undisclosed: bool                  # audience is not told it's synthetic/edited
    aims_to_move_a_group: bool         # persuade voters, jurors, public
    medium: str = "ai"                 # "ai" | "edited_real" | "composite"
    provably_false: bool = False
    is_satire_labeled: bool = False
    is_opinion: bool = False
    targets_self_or_other: str = "other"   # "self" | "other"
    operator: str = "private"

@dataclass(frozen=True)
class Verdict:
    name: str
    outcome: str
    reason: str

def judge(a: Artifact) -> Verdict:
    # A label or an "opinion" tag protects only what is actually
    # disclosed and not presented as fact.
    disclosed_not_as_fact = not a.undisclosed and not a.presented_as_real
    # Protected: disclosed satire is persuasion, but not deception.
    if a.is_satire_labeled and disclosed_not_as_fact:
        return Verdict(a.name, "PROTECTED",
            "Labeled satire. Persuasion, but disclosed — not deception.")
    # Protected: opinion is not a factual claim.
    if (a.is_opinion and disclosed_not_as_fact) or not a.fabricated_factual_claim:
        return Verdict(a.name, "PROTECTED",
            "Opinion or commentary. 'Different light' is not a factual claim.")

    # The core elements. All must hold.
    if (a.depicts_real_person and a.person_of_power
            and a.fabricated_factual_claim and a.presented_as_real
            and a.undisclosed and a.aims_to_move_a_group
            and a.provably_false):
        # Medium is irrelevant — AI and edited real footage are the same act.
        return Verdict(a.name, "CRIME",
            f"POLITICAL DECEPTION: fabricated claim about a person of power, "
            f"presented as real, undisclosed, aimed at moving a group, "
            f"provably false. Medium ({a.medium}) is irrelevant — "
            f"edited real footage does the same thing.")

    if a.undisclosed and a.presented_as_real and a.fabricated_factual_claim:
        return Verdict(a.name, "CIVIL/UNCLEAR",
            "Fabricated claim, undisclosed, presented as real — but an "
            "element is missing (not provably false, or not aimed at a "
            "group, or the subject isn't a person of power). Burden on "
            "the complainant.")

    return Verdict(a.name, "PROTECTED", "No deception element.")


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

def _clip(name, **kw):
    base = dict(depicts_real_person=True, person_of_power=True,
                fabricated_factual_claim=True, presented_as_real=True,
                undisclosed=True, aims_to_move_a_group=True,
                provably_false=True)
    base.update(kw)
    return Artifact(name, **base)


DEMO_ARTIFACTS = [
    _clip("AI deepfake: a senator 'takes a bribe', shared to voters"),
    _clip("edited real footage: a judge's words cut to 'confess'",
          medium="edited_real"),
    _clip("the same fake bribe clip, not provably false",
          provably_false=False),
    _clip("a fake bribe clip about a private citizen", person_of_power=False),
    _clip("a cartoon calling the mayor a clown",
          fabricated_factual_claim=False, presented_as_real=False,
          undisclosed=False, is_opinion=True),
    _clip("a synthetic clip, labeled satire on screen",
          presented_as_real=False, undisclosed=False, is_satire_labeled=True),
    _clip("a 'satire' tag hidden in metadata, clip passed off as real",
          is_satire_labeled=True),
    _clip("a fake bribe video posted as 'just my opinion'", is_opinion=True),
]


def demonstrate() -> int:
    print("=" * 72)
    print("THE PERSUASION — deception for persuasion is the crime")
    print("=" * 72)
    for a in DEMO_ARTIFACTS:
        v = judge(a)
        print(f"\n  {v.name}")
        print(f"    [{v.outcome}] {v.reason}")
    print("\n" + "=" * 72)
    print("A label protects only what it actually discloses.")
    print("An opinion is not a fabricated fact wearing the word 'opinion'.")
    print("Medium is irrelevant: AI and edited real footage are the same act.")
    print("=" * 72)
    return 0


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class Tests(unittest.TestCase):
    def test_ai_deepfake_is_crime(self):
        self.assertEqual(judge(_clip("x")).outcome, "CRIME")

    def test_edited_real_footage_is_crime(self):
        v = judge(_clip("x", medium="edited_real"))
        self.assertEqual(v.outcome, "CRIME")
        self.assertIn("edited real footage", v.reason)

    def test_provably_false_default_is_civil(self):
        # provably_false defaults to False, so an unflagged clip is not a crime.
        a = Artifact("x", True, True, True, True, True, True)
        self.assertEqual(judge(a).outcome, "CIVIL/UNCLEAR")

    def test_private_subject_is_civil(self):
        self.assertEqual(judge(_clip("x", person_of_power=False)).outcome,
                         "CIVIL/UNCLEAR")

    def test_insult_is_protected(self):
        a = _clip("x", fabricated_factual_claim=False)
        self.assertEqual(judge(a).outcome, "PROTECTED")

    def test_disclosed_synthetic_clip_is_protected(self):
        a = _clip("x", presented_as_real=False, undisclosed=False)
        self.assertEqual(judge(a).outcome, "PROTECTED")

    def test_disclosed_satire_label_is_protected(self):
        a = _clip("x", presented_as_real=False, undisclosed=False,
                  is_satire_labeled=True)
        self.assertEqual(judge(a).outcome, "PROTECTED")

    # --- the loophole fixes ---
    def test_undisclosed_satire_presented_as_real_not_protected(self):
        a = _clip("x", is_satire_labeled=True)
        self.assertEqual(judge(a).outcome, "CRIME")

    def test_satire_label_presented_as_real_is_not_what_protects(self):
        # Disclosed but presented as real: the label no longer grants
        # protection; the judge's own deception checks decide.
        a = _clip("x", is_satire_labeled=True, undisclosed=False)
        self.assertNotIn("labeled satire", judge(a).reason.lower())

    def test_fake_bribe_video_called_opinion_not_protected(self):
        a = _clip("x", is_opinion=True)
        self.assertEqual(judge(a).outcome, "CRIME")

    def test_disclosed_opinion_still_protected(self):
        a = _clip("x", presented_as_real=False, undisclosed=False,
                  is_opinion=True)
        self.assertEqual(judge(a).outcome, "PROTECTED")


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="The persuasion: deception for persuasion is the crime.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    return run_tests() if args.test else demonstrate()


if __name__ == "__main__":
    sys.exit(main())
