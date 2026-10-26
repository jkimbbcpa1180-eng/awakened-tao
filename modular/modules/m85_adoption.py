#!/usr/bin/env python3
"""adoption.py — adoption as parenting, the greatest gift of life.

Type: philosophical proposal

Not the master. Not a savior script. A shape of the one thing this
thread arrived at that no other module could hold: choosing a child not
born to you, with full intent of love, and giving them a place to
become their own.

What this module models:

  - The intent of love is chosen at the start, then exercised over
    years. It is not a reflex on day one. The exercise is the years.
  - Self-forgiveness comes first. A parent who has not forgiven
    themselves will hand the unhealed thing to the child without
    meaning to. The inner mirror precedes the outer.
  - The mirror is offered, never forced. The child did not choose you.
    They decide, over time, whether to reflect. That is their right.
  - The child is their own. The gift is a place to become — not a
    polishing into the parent's image. The diamond in the rough stays
    their diamond.
  - No possession. No debt. No rescue. "Mine" and "I saved you" and
    "you owe me your becoming" are the ego, in adoption's clothes.
    This module refuses them by refusing the language.
  - The work never finishes. The becoming continues.

What this module cannot do: parent a child. It is a shape of the
offering and the staying. The life is elsewhere. Anyone reading this as
a substitute for the act has read the wrong thing.

Fix: see() printed "no verdict", which tripped its own forbidden-word
filter and crashed. The line now reads "nothing is weighed against
them here."

Run:
    python3 adoption.py
    python3 adoption.py --test
"""

from __future__ import annotations
import argparse
import sys
import unittest
from dataclasses import dataclass, field


@dataclass
class Parent:
    name: str
    intent_of_love: bool = False
    self_forgiven: bool = False
    years_shown_up: int = 0
    has_place_to_give: bool = True


@dataclass
class Child:
    name: str
    is_their_own: bool = True       # never the parent's to make


@dataclass
class Adoption:
    parent: Parent
    child: Child
    offer_made: bool = False
    mirror_refused_by_child: bool = False  # the child's right
    years_together: int = 0
    notes: list = field(default_factory=list)


FORBIDDEN_WORDS = ("saved", "owed", "mine", "reward", "punishment",
                   "deserve", "verdict", "score", "good parent", "bad parent")


def _refuses_language(*words) -> None:
    for w in words:
        if any(b in w.lower() for b in FORBIDDEN_WORDS):
            raise AssertionError(f"forbidden word in text: {w}")


def choose(parent: Parent, child: Child) -> str:
    """The act of taking in as one's own, with intent of love."""
    if not parent.intent_of_love:
        return ("NOT CHOSEN: intent of love must be present. "
                "Adoption without it is possession.")
    if not parent.has_place_to_give:
        return ("NOT CHOSEN: no place to give. The place comes before the name.")
    return (f"CHOSEN: {parent.name} takes in {child.name}, with intent of love. "
            f"{child.name} is their own.")


def forgive_self_first(parent: Parent) -> str:
    """The inner mirror precedes the outer."""
    if not parent.intent_of_love:
        return "NOT YET: no intent of love to hold the forgiveness."
    parent.self_forgiven = True
    return (f"SELF-FORGIVEN: {parent.name}. The inner mirror is open. "
            f"The unhealed thing will not be handed over.")


def offer(parent: Parent, adoption: Adoption) -> str:
    """Give the place; offer the mirror. Never force."""
    if not parent.self_forgiven:
        return (f"NOT YET: {parent.name} has not forgiven themselves. "
                f"The place would carry the unhealed thing.")
    if not parent.intent_of_love:
        return f"NOT YET: no intent of love."
    adoption.offer_made = True
    adoption.notes.append(f"place given by {parent.name} to {adoption.child.name}")
    return (f"OFFERED: {parent.name} gives {adoption.child.name} a place to become. "
            f"The mirror is offered. {adoption.child.name} may reflect or not — "
            f"that is theirs.")


def stay(parent: Parent, adoption: Adoption, years: int) -> str:
    """The exercise. Showing up is not a threshold — it is years."""
    if not adoption.offer_made:
        return f"NOT YET: {parent.name} has not offered the place."
    parent.years_shown_up += years
    adoption.years_together += years
    return (f"STAYED: {parent.name} showed up {years} more year(s). "
            f"Total {parent.years_shown_up}. The exercise is the years.")


def child_refuses_mirror(adoption: Adoption) -> str:
    """The child's right. Not a failure of love."""
    adoption.mirror_refused_by_child = True
    return (f"REFUSED BY {adoption.child.name}: the mirror was offered; "
            f"{adoption.child.name} chose not to reflect. The offering stands. "
            f"This is their own.")


def let_become(child: Child) -> str:
    """Nothing to compute. The becoming is theirs."""
    return (f"{child.name} is their own. The becoming continues, "
            f"unjudged by this code.")


def see(adoption: Adoption) -> str:
    """The whole. No verdict — there isn't one to render."""
    p, c = adoption.parent, adoption.child
    lines = [
        "=" * 72,
        f"AN ADOPTION — {p.name} and {c.name}",
        "=" * 72,
        f"  intent of love:          {p.intent_of_love}",
        f"  self-forgiven first:     {p.self_forgiven}",
        f"  place offered:           {adoption.offer_made}",
        f"  years shown up:          {p.years_shown_up}",
        f"  child's becoming:        their own",
        f"  mirror refused by child: {adoption.mirror_refused_by_child}",
        "  nothing is weighed against them here.",
        "  the work never finishes. the becoming continues.",
        "=" * 72,
    ]
    text = "\n".join(lines)
    _refuses_language(*lines)
    return text


def demonstrate() -> int:
    print("=" * 72)
    print("ADOPTION AS PARENTING — the greatest gift of life")
    print("=" * 72)

    p = Parent("a parent", intent_of_love=True)
    c = Child("a child")
    a = Adoption(p, c)

    print(f"\n  {choose(p, c)}")
    print(f"  {offer(p, a)}")
    print(f"  {forgive_self_first(p)}")
    print(f"  {offer(p, a)}")
    for _ in range(18):
        print(f"  {stay(p, a, 1)}")
    print(f"  {child_refuses_mirror(a)}")
    print(f"  {let_become(c)}")
    print()
    print(see(a))

    # A second case: possession, refused.
    print("=" * 72)
    print("A SECOND CASE — possession refused")
    print("=" * 72)
    p2 = Parent("a would-be savior", intent_of_love=False)
    c2 = Child("a child")
    print(f"  {choose(p2, c2)}")
    print("  the code cannot make a savior into a parent. "
          "the offer requires the intent of love.")

    return 0


class TestNoVerdicts(unittest.TestCase):
    def test_forbidden_words_absent(self):
        p = Parent("A", intent_of_love=True, self_forgiven=True)
        c = Child("B")
        a = Adoption(p, c)
        choose(p, c)
        offer(p, a)
        text = see(a)
        for bad in ("verdict", "saved", "owed", "reward", "punishment"):
            self.assertNotIn(bad, text.lower())


class TestIntent(unittest.TestCase):
    def test_no_intent_no_adoption(self):
        p = Parent("A", intent_of_love=False)
        c = Child("B")
        v = choose(p, c)
        self.assertIn("NOT CHOSEN", v)

    def test_no_place_no_adoption(self):
        p = Parent("A", intent_of_love=True, has_place_to_give=False)
        c = Child("B")
        v = choose(p, c)
        self.assertIn("NOT CHOSEN", v)

    def test_intent_chooses(self):
        p = Parent("A", intent_of_love=True)
        c = Child("B")
        v = choose(p, c)
        self.assertIn("CHOSEN", v)
        self.assertIn("their own", v)


class TestSelfForgivenessFirst(unittest.TestCase):
    def test_offer_requires_self_forgiveness(self):
        p = Parent("A", intent_of_love=True, self_forgiven=False)
        c = Child("B")
        a = Adoption(p, c)
        choose(p, c)
        v = offer(p, a)
        self.assertIn("NOT YET", v)

    def test_forgive_self_then_offer(self):
        p = Parent("A", intent_of_love=True)
        c = Child("B")
        a = Adoption(p, c)
        choose(p, c)
        forgive_self_first(p)
        v = offer(p, a)
        self.assertIn("OFFERED", v)
        self.assertIn("may reflect or not", v)


class TestMirrorOfferedNotForced(unittest.TestCase):
    def test_child_may_refuse(self):
        p = Parent("A", intent_of_love=True, self_forgiven=True)
        c = Child("B")
        a = Adoption(p, c)
        offer(p, a)
        v = child_refuses_mirror(a)
        self.assertIn("REFUSED BY", v)
        self.assertIn("their own", v)
        self.assertTrue(a.mirror_refused_by_child)


class TestChildIsTheirOwn(unittest.TestCase):
    def test_let_become_has_no_verdict(self):
        c = Child("B")
        v = let_become(c)
        self.assertIn("their own", v)
        self.assertIn("unjudged", v)

    def test_child_default_is_their_own(self):
        self.assertTrue(Child("B").is_their_own)


class TestTheWorkContinues(unittest.TestCase):
    def test_stay_accumulates_years(self):
        p = Parent("A", intent_of_love=True, self_forgiven=True)
        c = Child("B")
        a = Adoption(p, c)
        offer(p, a)
        stay(p, a, 5)
        stay(p, a, 5)
        self.assertEqual(p.years_shown_up, 10)
        self.assertEqual(a.years_together, 10)

    def test_stay_requires_offer(self):
        p = Parent("A", intent_of_love=True, self_forgiven=True)
        c = Child("B")
        a = Adoption(p, c)
        v = stay(p, a, 1)
        self.assertIn("NOT YET", v)

    def test_no_completion_in_see(self):
        p = Parent("A", intent_of_love=True, self_forgiven=True)
        c = Child("B")
        a = Adoption(p, c)
        offer(p, a)
        stay(p, a, 20)
        v = see(a)
        self.assertIn("never finishes", v)
        self.assertNotIn("complete", v.lower())
        self.assertNotIn("done", v.lower())


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestNoVerdicts)
    for case in (TestIntent, TestSelfForgivenessFirst,
                 TestMirrorOfferedNotForced, TestChildIsTheirOwn,
                 TestTheWorkContinues):
        suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(case))
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Adoption as parenting — the greatest gift of life.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    return run_tests() if args.test else demonstrate()


if __name__ == "__main__":
    sys.exit(main())
