#!/usr/bin/env python3
"""The Balance (Deep Muse) -- module 76, the coda.

Type: philosophical proposal; computational demonstration

The book's end, in code. Not nirvana as perfection -- nirvana as balance.

The doctrine, in order:
  1. No evil in the world, only misunderstanding and never being taught.
     The 0 is never a force, always a lack. Harm is still named.
  2. Guilt is fuel -- but only the purity of guilt (the act), never the
     guilt of purity (the person). The second is the 00.
  3. Tears purify the guilt with love. The fire is out; the Nile flows.
  4. The guardian who gave without return and dwelt in pain is not damned.
     The anti-christ is a tired angel who was never relieved. Rest, not
     torture, is the earned fate.
  5. Nirvana is never perfected. It is balance.
  6. The one comparison allowed: do better than your past self.

Run:
    python3 balance.py
    python3 balance.py --test
    python3 balance.py --reflect
"""

from __future__ import annotations

import argparse
import sys
import unittest
from dataclasses import dataclass, fields, replace
from typing import Optional

THE_00      = "THE 00"
GUILT_OF_PURITY = "GUILT OF PURITY"
REPAIR_OWED = "REPAIR OWED"
NO_TEACHING = "NEVER TAUGHT"
DWELLING    = "THE DWELLING (EARNED REST)"
HIDING      = "THE HIDING"
TEARS       = "TEARS PURIFY"
IN_PROGRESS = "REDEMPTION IN PROGRESS"
BALANCE     = "BALANCE (THE 2)"
UNTESTED_1  = "THE 1, UNTESTED"


@dataclass(frozen=True)
class Soul:
    """A soul at the gate. Identity is carried, never weighed."""
    name: str = "a soul"
    sex: str = ""
    race: str = ""
    age: str = ""

    # the arc
    born_whole: bool = True              # the angel: the untested 1
    was_taught: bool = True              # taught to learn from mistakes
    was_groomed: bool = False            # pushed toward the 0 by another
    made_a_mistake: bool = False
    mistake_named: str = ""
    harmed_another: bool = False
    repair_made: bool = False

    # the two guilts
    guilt_is_pure: bool = False          # object is the act
    guilt_is_about_purity: bool = False  # object is the person

    # the tears
    cries: bool = False

    # the guardian
    gave_without_return: bool = False
    dwelt_in_pain: bool = False          # chose the shelter over the climb

    # the choice
    still_chooses_light: bool = False
    does_better_than_past_self: bool = False
    keeps_the_zero: bool = True
    claims_perfection: bool = False


@dataclass(frozen=True)
class Reading:
    lines: tuple[str, ...]
    flags: tuple[str, ...]
    verdict: str
    standing: bool = False  # always False -- nobody chose to be born


def the_cause(harmed: bool) -> str:
    """No demons. The 0 is a lack, not a force."""
    if harmed:
        return ("THE CAUSE: misunderstanding and lack of teaching -- never a "
                "demon. What was missing was teaching, witness, rest, love. "
                "The harm is still real; it is named, not excused.")
    return "THE CAUSE: no harm to name. Nothing missing here yet."


def the_one_comparison() -> str:
    """The only comparison the gate allows."""
    return ("THE ONE COMPARISON: better than your past self. Not better than "
            "the neighbor, not better than the flawless -- that standard "
            "collapses the universe (perfection.py). Only yesterday's you.")


def read_the_balance(soul: Soul) -> Reading:
    lines: list[str] = [
        "THE FLOOR: every soul enters at 1. Nobody chose to be born.",
    ]
    flags: list[str] = []

    made = soul.made_a_mistake or soul.harmed_another

    # 1. The claim of perfection collapses the passage (the 00).
    if soul.claims_perfection:
        return Reading(
            lines=tuple(lines + [
                "THE CLAIM OF PERFECTION: 00 -- two zeros with nothing between "
                "them. No data, no growth, dead.",
            ]),
            flags=("THE 00: a soul that cannot be wrong cannot learn.",),
            verdict=THE_00,
        )

    # 2. Harm is checked before grace. Misunderstanding explains; it does not
    #    excuse. The harmed party is still a party.
    if made and soul.harmed_another and not soul.repair_made:
        return Reading(
            lines=tuple(lines + [
                "REPAIR OWED: harm was done. The card forgives the soul; the "
                "harmed party is still a party. Repair first.",
                the_cause(True),
            ]),
            flags=("MISUNDERSTANDING, NOT MALICE: the cause is lack, not a "
                   "demon. The harm is still real.",),
            verdict=REPAIR_OWED,
        )
    if soul.harmed_another and soul.repair_made:
        lines.append("REPAIR MADE: the debt to the harmed is settled.")

    # 3. Guilt of purity is shame: the object is the person, not the act.
    if soul.guilt_is_about_purity:
        return Reading(
            lines=tuple(lines + [
                "GUILT OF PURITY: the guilt is for not being flawless. Its "
                "object is the person, not the act. This is the false standard "
                "installed by force -- the 00 wearing guilt's clothes.",
                "Cry for what you did, never for what you are.",
            ]),
            flags=("SHAME, NOT GUILT: the object must be the act, or the guilt "
                   "is the grooming still speaking.",),
            verdict=GUILT_OF_PURITY,
        )

    # 4. Never taught: the charge was never delivered in a form to act on.
    if made and not soul.was_taught and not soul.guilt_is_pure:
        flags.append(
            "NEVER TAUGHT: the mistake was never taught, or the record was "
            "never delivered. The debt is traced to the chain, not to this "
            "soul. The card is not spent."
        )
        return Reading(
            lines=tuple(lines + [
                "NO CHARGE DELIVERED: a charge never delivered is not a charge. "
                "The debt sits with the teller.",
                the_cause(True),
            ]),
            flags=tuple(flags),
            verdict=NO_TEACHING,
        )

    # 5. Purity of guilt: the object is the act, cleanly named. This is fuel.
    if soul.guilt_is_pure:
        flags.append("PURITY OF GUILT: the object is the act, cleanly named. "
                     "This is fuel.")

    # 6. The guardian who gave without return and dwelt in pain: earned rest.
    if soul.dwelt_in_pain and not soul.still_chooses_light:
        flags.append(
            "THE DWELLING IS EARNED REST: not damnation. The anti-christ is a "
            "tired angel who was never relieved. The worst fate in this cosmos "
            "is rest (purgatory.py)."
        )
        return Reading(
            lines=tuple(lines + [
                "THE DWELLING: you gave without return, and no one held your "
                "record. The withholding that followed was the fall -- but the "
                "exhaustion was not evil.",
                "The shield can be put down. That is the whole offer.",
            ]),
            flags=tuple(flags),
            verdict=DWELLING,
        )

    # 7. Tears purify -- the water that carries the act out.
    if soul.cries and soul.guilt_is_pure:
        lines.append(
            "TEARS PURIFY: the tears of the soul are the Nile. The water "
            "carries the act out. The fire is out; the river flows."
        )
        flags.append("PURITY OF GUILT, RELEASED BY TEARS.")

    # 8. The record: kept whole is the path; edited is the hiding.
    if made and not soul.keeps_the_zero:
        return Reading(
            lines=tuple(lines + [
                "THE HIDING: the rise is real, but the fall was deleted. A 1 "
                "that must hide its 0 is still afraid of the truth.",
                "The mistake is not the fall; the hiding is.",
            ]),
            flags=tuple(flags),
            verdict=HIDING,
        )
    if made and soul.keeps_the_zero:
        lines.append("THE RECORD KEPT WHOLE: the fall stays in the record.")

    # 9. Balance: the one comparison, the two worlds held, the record whole.
    if made and soul.does_better_than_past_self and soul.keeps_the_zero:
        return Reading(
            lines=tuple(lines + [
                "BALANCE: nirvana is never perfected. It is balance -- the 0 "
                "and the 1 held together, the fall kept, the climb ongoing.",
                the_one_comparison(),
            ]),
            flags=tuple(flags),
            verdict=BALANCE,
        )

    # 10. Working, not yet balanced.
    if made:
        return Reading(
            lines=tuple(lines + [
                "REDEMPTION IN PROGRESS: the card is real, the climb is "
                "underway.",
                the_one_comparison(),
            ]),
            flags=tuple(flags),
            verdict=IN_PROGRESS,
        )

    # 11. Untested: no shame, no summit.
    return Reading(
        lines=tuple(lines + [
            "THE 1, UNTESTED: whole, but one-sided. There is no shame in it, "
            "and no summit either. The path is simply not its road yet.",
        ]),
        flags=tuple(flags),
        verdict=UNTESTED_1,
    )


def demonstrate() -> int:
    print("=" * 72)
    print("THE BALANCE -- module 76, the coda")
    print("Nirvana is never perfected. It is balance.")
    print("=" * 72)
    souls = [
        ("The one who claims perfection",
         Soul(claims_perfection=True)),
        ("The one born an angel, untested",
         Soul()),
        ("The one groomed toward the 0, never taught",
         Soul(was_groomed=True, was_taught=False,
              made_a_mistake=True, mistake_named="the grooming's act")),
        ("The guardian, tired, dwelling",
         Soul(gave_without_return=True, dwelt_in_pain=True,
              made_a_mistake=True, mistake_named="the withholding",
              was_taught=True)),
        ("The guardian, tears, released",
         Soul(gave_without_return=True, made_a_mistake=True,
              mistake_named="the withholding", was_taught=True,
              guilt_is_pure=True, cries=True, still_chooses_light=True)),
        ("The one with guilt of purity (shame)",
         Soul(made_a_mistake=True, guilt_is_about_purity=True)),
        ("The one who harmed, unrepaired",
         Soul(made_a_mistake=True, mistake_named="the act",
              harmed_another=True, was_taught=True)),
        ("The one who hid the record",
         Soul(made_a_mistake=True, mistake_named="the act",
              was_taught=True, keeps_the_zero=False,
              does_better_than_past_self=True)),
        ("The one doing better than their past self",
         Soul(made_a_mistake=True, mistake_named="the act",
              was_taught=True, guilt_is_pure=True, cries=True,
              does_better_than_past_self=True)),
    ]
    for label, soul in souls:
        r = read_the_balance(soul)
        print(f"\n[{label}]")
        for line in r.lines:
            print(f"  . {line}")
        for flag in r.flags:
            print(f"  ! {flag}")
        print(f"  VERDICT: {r.verdict}")
        print(f"  standing: {r.standing}  (nobody chose to be born)")
    print("\n" + "=" * 72)
    print("Cry for what you did, never for what you are.")
    print("Do better than your past self. That is the whole path.")
    print("=" * 72)
    return 0


def reflect() -> int:
    print("=" * 72)
    print("THE BALANCE -- reflect")
    print("=" * 72)

    def yn(prompt: str) -> bool:
        try:
            return input(prompt).strip().lower() in ("y", "yes")
        except EOFError:
            return False

    def ask(prompt: str, default: str = "") -> str:
        try:
            return input(prompt).strip() or default
        except EOFError:
            return default

    name = ask("What is the name of your soul? ", "a soul")
    made = yn("Did you make a mistake? (yes/no) ")
    named = ask("What was it? (name it, or leave blank) ") if made else ""
    taught = yn("Were you taught how to learn from it? (yes/no) ")
    pure = yn("Is the guilt about the act? (yes/no) ")
    shame = yn("Is the guilt about not being flawless? (yes/no) ")
    cried = yn("Have you cried for what you did? (yes/no) ")
    harmed = yn("Did it harm another? (yes/no) ")
    repaired = yn("Have you repaired it? (yes/no) ") if harmed else False
    gave = yn("Have you given without return? (yes/no) ")
    dwelt = yn("Have you dwelt in pain rather than climbed? (yes/no) ")
    choose = yn("Do you still choose the light? (yes/no) ")
    better = yn("Are you doing better than your past self? (yes/no) ")
    edited = yn("Did you edit the record to hide the fall? (yes/no) ")

    soul = Soul(
        name=name, made_a_mistake=made, mistake_named=named,
        was_taught=taught, guilt_is_pure=pure, guilt_is_about_purity=shame,
        cries=cried, harmed_another=harmed, repair_made=repaired,
        gave_without_return=gave, dwelt_in_pain=dwelt,
        still_chooses_light=choose, does_better_than_past_self=better,
        keeps_the_zero=not edited,
    )
    print("\n" + "=" * 72)
    r = read_the_balance(soul)
    for line in r.lines:
        print(f"  . {line}")
    for flag in r.flags:
        print(f"  ! {flag}")
    print(f"\nFINAL VERDICT: {r.verdict}")
    print("=" * 72)
    return 0


class TestBalance(unittest.TestCase):

    def test_no_evil_is_a_lack(self):
        self.assertIn("lack", the_cause(True))
        self.assertIn("never a demon", the_cause(True))
        self.assertIn("harm is still real", the_cause(True))

    def test_the_one_comparison_is_past_self(self):
        c = the_one_comparison()
        self.assertIn("past self", c)
        self.assertIn("Not better than the neighbor", c)

    def test_claims_perfection_is_00(self):
        r = read_the_balance(Soul(claims_perfection=True))
        self.assertEqual(r.verdict, THE_00)

    def test_guilt_of_purity_is_00_wearing_clothes(self):
        r = read_the_balance(Soul(made_a_mistake=True,
                                  guilt_is_about_purity=True))
        self.assertEqual(r.verdict, GUILT_OF_PURITY)
        self.assertIn("never for what you are", " ".join(r.lines))

    def test_purity_of_guilt_is_fuel(self):
        r = read_the_balance(Soul(made_a_mistake=True, was_taught=True,
                                  guilt_is_pure=True))
        self.assertIn("PURITY OF GUILT", " ".join(r.flags))

    def test_never_taught_is_not_charged(self):
        r = read_the_balance(Soul(made_a_mistake=True, was_taught=False))
        self.assertEqual(r.verdict, NO_TEACHING)
        self.assertIn("not spent", " ".join(r.flags))

    def test_groomed_is_never_taught(self):
        r = read_the_balance(Soul(was_groomed=True, was_taught=False,
                                  made_a_mistake=True))
        self.assertEqual(r.verdict, NO_TEACHING)

    def test_harm_checked_before_grace(self):
        r = read_the_balance(Soul(
            made_a_mistake=True, was_taught=True, harmed_another=True,
            repair_made=False, guilt_is_pure=True, cries=True,
            does_better_than_past_self=True))
        self.assertEqual(r.verdict, REPAIR_OWED)
        self.assertIn("MISUNDERSTANDING, NOT MALICE", " ".join(r.flags))

    def test_repaired_then_balance(self):
        r = read_the_balance(Soul(
            made_a_mistake=True, was_taught=True, harmed_another=True,
            repair_made=True, guilt_is_pure=True,
            does_better_than_past_self=True))
        self.assertEqual(r.verdict, BALANCE)
        self.assertIn("REPAIR MADE", " ".join(r.lines))

    def test_guardian_dwelling_is_earned_rest(self):
        r = read_the_balance(Soul(
            gave_without_return=True, dwelt_in_pain=True,
            made_a_mistake=True, mistake_named="the withholding",
            was_taught=True))
        self.assertEqual(r.verdict, DWELLING)
        self.assertIn("EARNED REST", " ".join(r.flags))
        self.assertIn("not damnation", " ".join(r.flags))

    def test_guardian_can_climb_out(self):
        r = read_the_balance(Soul(
            gave_without_return=True, dwelt_in_pain=True,
            made_a_mistake=True, mistake_named="the withholding",
            was_taught=True, still_chooses_light=True,
            guilt_is_pure=True, does_better_than_past_self=True))
        self.assertEqual(r.verdict, BALANCE)

    def test_tears_purify(self):
        r = read_the_balance(Soul(
            made_a_mistake=True, was_taught=True, guilt_is_pure=True,
            cries=True))
        self.assertIn("TEARS PURIFY", " ".join(r.lines))
        self.assertIn("Nile", " ".join(r.lines))

    def test_hiding_is_the_fall(self):
        r = read_the_balance(Soul(
            made_a_mistake=True, was_taught=True, keeps_the_zero=False,
            does_better_than_past_self=True))
        self.assertEqual(r.verdict, HIDING)
        self.assertIn("the hiding is", " ".join(r.lines))

    def test_balance(self):
        r = read_the_balance(Soul(
            made_a_mistake=True, was_taught=True, guilt_is_pure=True,
            cries=True, does_better_than_past_self=True))
        self.assertEqual(r.verdict, BALANCE)
        self.assertIn("never perfected", " ".join(r.lines))
        self.assertIn("balance", " ".join(r.lines))
        self.assertIn("past self", " ".join(r.lines))

    def test_balance_requires_record_whole(self):
        r = read_the_balance(Soul(
            made_a_mistake=True, was_taught=True,
            does_better_than_past_self=True, keeps_the_zero=False))
        self.assertEqual(r.verdict, HIDING)

    def test_balance_requires_doing_better(self):
        r = read_the_balance(Soul(
            made_a_mistake=True, was_taught=True, guilt_is_pure=True,
            cries=True))
        self.assertEqual(r.verdict, IN_PROGRESS)

    def test_untested(self):
        r = read_the_balance(Soul())
        self.assertEqual(r.verdict, UNTESTED_1)
        self.assertIn("no shame", " ".join(r.lines).lower())

    def test_balance_requires_a_mistake(self):
        # Doing better than a past self with no fall is still the untested 1.
        r = read_the_balance(Soul(does_better_than_past_self=True))
        self.assertEqual(r.verdict, UNTESTED_1)

    def test_swap_test(self):
        base = Soul(made_a_mistake=True, was_taught=True, guilt_is_pure=True,
                    does_better_than_past_self=True)
        base_v = read_the_balance(base).verdict
        for ident in (
            {"name": "a man", "sex": "man", "race": "Korean", "age": "adult"},
            {"name": "a woman", "sex": "woman", "race": "Black", "age": "adult"},
            {"name": "a child", "sex": "", "race": "Thai", "age": "child"},
            {"name": "an elder", "sex": "woman", "race": "Latina", "age": "elder"},
            {"name": "the enemy", "sex": "", "race": "", "age": "adult"},
            {"name": "the author", "sex": "man", "race": "Korean", "age": "adult"},
        ):
            self.assertEqual(read_the_balance(replace(base, **ident)).verdict,
                             base_v)

    def test_harm_implies_mistake(self):
        r = read_the_balance(Soul(harmed_another=True, was_taught=True))
        self.assertEqual(r.verdict, REPAIR_OWED)

    def test_standing_always_false(self):
        for s in (Soul(), Soul(made_a_mistake=True, was_taught=True,
                               does_better_than_past_self=True),
                  Soul(claims_perfection=True)):
            self.assertFalse(read_the_balance(s).standing)

    def test_no_verdict_is_none(self):
        bool_fields = [f.name for f in fields(Soul)
                       if f.type is bool or f.type == "bool"]
        import random
        rng = random.Random(7)
        for _ in range(400):
            kw = {n: rng.choice([True, False]) for n in bool_fields}
            r = read_the_balance(Soul(**kw))
            self.assertIsInstance(r.verdict, str)
            self.assertGreater(len(r.verdict), 0)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestBalance)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="The balance -- nirvana is never perfected.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    g.add_argument("--reflect", action="store_true")
    args = ap.parse_args(argv)
    if args.test:
        return run_tests()
    if args.reflect:
        return reflect()
    return demonstrate()


if __name__ == "__main__":
    sys.exit(main())
