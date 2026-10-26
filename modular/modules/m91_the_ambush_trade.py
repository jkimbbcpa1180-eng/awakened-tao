#!/usr/bin/env python3
"""the_ambush_trade.py — the contradiction, made explicit.

Type: policy proposal; computational demonstration

Borat's power is the ambush. The ethics forbid the ambush. These
cannot both hold.

This module does not resolve that. It models three real regimes,
names each one's cost, and requires the maker to CHOOSE and OWN the
cost. It never auto-selects.

  Regime A — INFORMED BEFORE. Subject told before filming.
    Preserves: no manipulation. The reaction is a choice.
    Loses: the ambush engine. What the subject would have said
      unguarded is not reached.
    This is what the_real_satire.py enforces.

  Regime B — INFORMED AFTER, CONSENT TO PUBLISH. Ambush filmed;
    subject shown the cut and consents to publication.
    Preserves: the unguarded moment, for the material that survives.
    Loses: the most revealing material is often exactly what gets
      vetoed. What publishes is the intersection: unguarded AND
      consented. Smaller, but real.
    Status: contested. The subject was filmed without knowing.
      Publication consent is post-hoc, not advance.

  Regime C — AMBUSH, PUBLISH ANYWAY. Borat as made.
    Preserves: the full ambush.
    Costs: manipulation of humiliation. The subject was not told
      and did not consent. The module labels this MANIPULATION. It
      models it anyway so the choice is visible, not hidden.

And a modifier that matters: WHO is ambushed.

  Ambushing a person of power is less harmful than ambushing an
  ordinary person. Not harmless — less harmful. The powerful have
  platforms, lawyers, and the ability to respond. The ordinary
  person does not. Power is a mitigating factor, not an exoneration.

Fix: record_choice now requires the defence to name the label it
  accepts (SATIRE, CONTESTED or MANIPULATION, any case). A blank
  defence, or one like "x" that names no cost, is REFUSED.
Fix: Regime A now adds an ordinary-person cost note when the target
  holds no power. Informed satire aimed at ordinary people still costs.
Fix: a custom regime that tells the subject only after filming, without
  needing consent to publish, no longer says "the subject was not
  told". It says they were told only after and did not consent.

Run:
    python3 the_ambush_trade.py
    python3 the_ambush_trade.py --test
"""

from __future__ import annotations
import argparse
import sys
import unittest
from dataclasses import dataclass


@dataclass(frozen=True)
class Piece:
    name: str
    target_is_person_of_power: bool


@dataclass(frozen=True)
class Regime:
    name: str
    informed_before: bool
    informed_after: bool
    publish_requires_consent: bool


INFORMED_BEFORE = Regime(
    "A: informed before",
    informed_before=True, informed_after=False, publish_requires_consent=False)
INFORMED_AFTER_WITH_CONSENT = Regime(
    "B: informed after, consent to publish",
    informed_before=False, informed_after=True, publish_requires_consent=True)
AMBUSH_PUBLISH_ANYWAY = Regime(
    "C: ambush, publish anyway",
    informed_before=False, informed_after=False, publish_requires_consent=False)


@dataclass(frozen=True)
class Evaluation:
    piece: str
    regime: str
    label: str          # "SATIRE" | "CONTESTED" | "MANIPULATION"
    preserves: str
    costs: str


def evaluate(piece: Piece, regime: Regime) -> Evaluation:
    if regime.informed_before:
        ordinary_note = ""
        if not piece.target_is_person_of_power:
            ordinary_note = (" The target is ordinary: even informed, "
                             "satire aimed at someone who never held "
                             "power still has a cost.")
        return Evaluation(
            piece.name, regime.name, "SATIRE",
            preserves=("The reaction is a choice the subject made knowing "
                       "the frame. No manipulation of the subject."),
            costs=("The ambush engine is gone. A subject who knows they "
                   "are in satire guards; what they would have said "
                   "unguarded is not reached." + ordinary_note))

    if regime.informed_after and regime.publish_requires_consent:
        power_note = ""
        if not piece.target_is_person_of_power:
            power_note = (" AND the target is ordinary — post-hoc consent "
                          "cannot undo that they were filmed without "
                          "knowing. This is contested, not clean.")
        return Evaluation(
            piece.name, regime.name, "CONTESTED",
            preserves=("The unguarded moment survives for the material "
                       "the subject consents to publish. What publishes "
                       "is the intersection: unguarded AND consented."),
            costs=("The most revealing material is often exactly what "
                   "gets vetoed. The intersection is smaller than the "
                   "ambush. Post-hoc consent is not advance consent."
                   + power_note))

    power_note = (
        " The target is a person of power: less harmful than ambushing "
        "an ordinary person, but still manipulation. Power is a "
        "mitigating factor, not an exoneration."
        if piece.target_is_person_of_power else
        " The target is an ordinary person who never held power. This "
        "is the worst case of the manipulation.")
    told = ("The subject was told only after filming and did not "
            "consent to publish." if regime.informed_after else
            "The subject was not told and did not consent.")
    return Evaluation(
        piece.name, regime.name, "MANIPULATION",
        preserves="The full ambush. This is Borat as made.",
        costs=(told + " This is "
               "the manipulation of humiliation." + power_note))


def record_choice(piece: Piece, regime: Regime, maker: str,
                  defence: str) -> str:
    """The maker must choose and own the cost. The code will not choose."""
    if not defence.strip():
        return ("REFUSED: a choice without a defence is not a choice, "
                "it is a want. Name why you chose this regime and what "
                "you accept as its cost.")
    e = evaluate(piece, regime)
    if e.label.lower() not in defence.lower():
        return (f"REFUSED: the defence does not name the cost it accepts. "
                f"Name the label you are accepting ({e.label}) and why.")
    return (f"RECORDED: {maker} chose {regime.name} for {piece.name}. "
            f"Label: {e.label}. Preserves: {e.preserves} "
            f"Accepts as cost: {e.costs} Defence: {defence.strip()}")


DEMO_PIECES = [
    Piece("ambushing an official", target_is_person_of_power=True),
    Piece("ambushing an ordinary person", target_is_person_of_power=False),
]


def demonstrate() -> int:
    print("=" * 72)
    print("THE AMBUSH TRADE — the contradiction, made explicit")
    print("=" * 72)
    print("\nBorat's power is the ambush. The ethics forbid the ambush.")
    print("This module does not resolve that. It makes the choice")
    print("visible and requires the maker to own the cost.\n")
    for piece in DEMO_PIECES:
        print(f"\n  TARGET: {piece.name}")
        for regime in (INFORMED_BEFORE, INFORMED_AFTER_WITH_CONSENT,
                       AMBUSH_PUBLISH_ANYWAY):
            e = evaluate(piece, regime)
            print(f"\n    [{e.label}] {e.regime}")
            print(f"      preserves: {e.preserves}")
            print(f"      costs:     {e.costs}")
    print("\n" + "=" * 72)
    print("WHAT THE MODULE REFUSES TO DO")
    print("=" * 72)
    print("  It refuses to pick a regime. Picking would be the ego's")
    print("  answer before the situation arrives.")
    print("  It refuses to call C satire. C is manipulation, modelled")
    print("  so the choice is visible.")
    print("  It refuses to give A or B a clean bill. A loses the ambush.")
    print("  B's consent is post-hoc. Neither is free.")
    print("=" * 72)
    return 0


class Tests(unittest.TestCase):
    def test_a_is_satire(self):
        self.assertEqual(evaluate(Piece("x", True), INFORMED_BEFORE).label, "SATIRE")

    def test_a_names_ambush_loss(self):
        e = evaluate(Piece("x", True), INFORMED_BEFORE)
        self.assertIn("ambush engine is gone", e.costs.lower())

    def test_b_is_contested(self):
        e = evaluate(Piece("x", True), INFORMED_AFTER_WITH_CONSENT)
        self.assertEqual(e.label, "CONTESTED")

    def test_b_names_post_hoc_consent(self):
        e = evaluate(Piece("x", True), INFORMED_AFTER_WITH_CONSENT)
        self.assertIn("post-hoc consent is not advance", e.costs.lower())

    def test_b_on_ordinary_is_worse(self):
        power = evaluate(Piece("x", True), INFORMED_AFTER_WITH_CONSENT)
        ordinary = evaluate(Piece("y", False), INFORMED_AFTER_WITH_CONSENT)
        self.assertIn("ordinary", ordinary.costs.lower())
        self.assertNotIn("ordinary", power.costs.lower())

    def test_c_is_manipulation(self):
        self.assertEqual(evaluate(Piece("x", True), AMBUSH_PUBLISH_ANYWAY).label,
                         "MANIPULATION")

    def test_c_names_mitigation_and_exoneration(self):
        e = evaluate(Piece("x", True), AMBUSH_PUBLISH_ANYWAY)
        self.assertIn("mitigating factor", e.costs.lower())
        self.assertIn("not an exoneration", e.costs.lower())

    def test_c_on_ordinary_is_worst(self):
        e = evaluate(Piece("x", False), AMBUSH_PUBLISH_ANYWAY)
        self.assertIn("worst case", e.costs.lower())

    def test_no_regime_is_silently_best(self):
        for regime in (INFORMED_BEFORE, INFORMED_AFTER_WITH_CONSENT,
                       AMBUSH_PUBLISH_ANYWAY):
            for power in (True, False):
                e = evaluate(Piece("x", power), regime)
                self.assertTrue(e.costs.strip(), regime.name)

    def test_record_choice_requires_defence(self):
        v = record_choice(Piece("x", True), INFORMED_BEFORE, "maker", "")
        self.assertIn("REFUSED", v)

    def test_record_choice_records_defence(self):
        v = record_choice(Piece("x", True), INFORMED_BEFORE, "maker",
                          "I accept SATIRE's cost: because no one is tricked")
        self.assertIn("RECORDED", v)
        self.assertIn("no one is tricked", v)

    def test_record_choice_refuses_defence_naming_no_cost(self):
        v = record_choice(Piece("x", True), INFORMED_BEFORE, "maker", "x")
        self.assertIn("REFUSED", v)

    def test_record_choice_label_is_case_insensitive(self):
        v = record_choice(Piece("x", True), AMBUSH_PUBLISH_ANYWAY, "maker",
                          "I own the manipulation; the official lied")
        self.assertIn("RECORDED", v)

    def test_a_on_ordinary_names_cost(self):
        power = evaluate(Piece("x", True), INFORMED_BEFORE)
        ordinary = evaluate(Piece("y", False), INFORMED_BEFORE)
        self.assertIn("ordinary", ordinary.costs.lower())
        self.assertNotIn("ordinary", power.costs.lower())

    def test_told_after_without_consent_not_called_untold(self):
        r = Regime("D: told after, publish anyway", informed_before=False,
                   informed_after=True, publish_requires_consent=False)
        e = evaluate(Piece("x", True), r)
        self.assertEqual(e.label, "MANIPULATION")
        self.assertNotIn("was not told", e.costs.lower())
        self.assertIn("told only after", e.costs.lower())
        self.assertIn("did not consent to publish", e.costs.lower())

    def test_no_auto_selection(self):
        ns = globals()
        auto = [n for n in ns if "auto" in n.lower()]
        self.assertEqual(auto, [])


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="The ambush trade: model the contradiction, force the choice.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    return run_tests() if args.test else demonstrate()


if __name__ == "__main__":
    sys.exit(main())
