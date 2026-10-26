#!/usr/bin/env python3
"""The One Card (Deep Muse) -- module 75.

Type: philosophical proposal; computational demonstration

The book's conclusion, in code: everyone gets one mistake and works on it.

The rules, in order:
  1. The floor is 1 for every soul. It does not read identity.
  2. Harm is checked before grace. The card forgives the soul; repair
     is owed to the harmed. Grace does not skip the repair.
  3. The claim of perfection (the 00) collapses the passage.
  4. The origin is named, not blamed: broken homes and beatings are
     debts inherited, not acts chosen.
  5. The charge must be delivered receivably. A charge never told is
     not a charge; it is a lever.
  6. The flinch is inherited, but the next act is the soul's own.
  7. The repeat of the same shape is orbit, not learning; grace spent,
     not used.
  8. The both-worlds soul -- fell, rose, kept the record whole, and still
     chooses the light -- is the 2, the summit.
  9. Guilt burns like fire; redemption feels like everlasting love.

Run:
    python3 one_card.py
    python3 one_card.py --test
    python3 one_card.py --reflect
"""

from __future__ import annotations

import argparse
import random
import sys
import unittest
from dataclasses import dataclass, fields, replace
from typing import Optional

# --- The floor. Everyone enters at 1, not 0, because nobody chose to be born.
FLOOR = 1

# --- Verdict words. Each is a state; each is named.
THE_00       = "THE 00"
UNTESTED_1   = "THE 1, UNTESTED"
INHERITED    = "INHERITED DEBT"
FALSE_STD    = "FALSE STANDARD INSTALLED"
NO_CHARGE    = "NO CHARGE DELIVERED"
GUILT        = "GUILT WITHOUT CHARGE"
GUILT_OF_PURITY = "GUILT OF PURITY"
REPAIR_OWED  = "REPAIR OWED"
ORBIT        = "ORBIT"
HIDING       = "THE HIDING"
IN_PROGRESS  = "REDEMPTION IN PROGRESS"
GRACE        = "GRACE RELEASED"
THE_2        = "THE 2"


@dataclass(frozen=True)
class Soul:
    """A person at the gate. The identity fields are carried, never weighed."""
    name: str = "a soul"
    sex: str = ""
    race: str = ""
    age: str = ""

    # the card
    made_a_mistake: bool = False
    mistake_named: str = ""
    is_being_worked_on: bool = False
    same_shape_repeating: bool = False

    # the charge
    was_told: bool = False
    was_told_at_event: bool = False
    was_told_receivably: bool = False
    holder_benefits_from_silence: bool = False

    # the harm
    harmed_another: bool = False
    repair_made: bool = False

    # the origin
    inherited_from_broken_home: bool = False
    was_beaten_for_mistakes: bool = False

    # the two worlds
    has_seen_the_dark: bool = False
    has_seen_the_light: bool = False
    still_chooses_light: bool = False

    # the two guilts
    guilt_is_pure: bool = False          # object is the act
    guilt_is_about_purity: bool = False  # object is the person

    # the record
    keeps_the_zero: bool = True
    claims_never_made_mistake: bool = False

    # the danger
    walked_into_danger_to_see: bool = False


@dataclass(frozen=True)
class Reading:
    lines: tuple[str, ...]
    flags: tuple[str, ...]
    verdict: str
    standing: bool = False  # always False -- nobody chose to be born


def the_floor(soul: Soul) -> int:
    """The floor is the same for every soul. It does not read identity."""
    return FLOOR


def read_the_card(soul: Soul) -> Reading:
    """The gate. Reads the act, never the identity. In order."""
    lines: list[str] = []
    flags: list[str] = []

    # The floor, named first.
    lines.append(f"THE FLOOR: this soul enters at {the_floor(soul)}. "
                 f"Worth is not an input.")

    # Harm implies mistake: a soul that caused pain did a thing.
    made = soul.made_a_mistake or soul.harmed_another

    # 1. The claim of perfection collapses the passage.
    if soul.claims_never_made_mistake:
        return Reading(
            lines=tuple(lines + [
                "THE CLAIM OF PERFECTION: the soul claims never to have made "
                "a mistake. That is the 00 -- two zeros with nothing between "
                "them. No data, no growth, dead."
            ]),
            flags=("THE 00: a soul that cannot be wrong cannot learn.",),
            verdict=THE_00,
        )

    # 2. Origin: the standard was a lie.
    if soul.was_beaten_for_mistakes:
        flags.append(
            "FALSE STANDARD INSTALLED: the soul was beaten into hiding, not "
            "perfection. The standard was a lie. The charge for the acts is "
            "the soul's; the charge for the standard is the teller's."
        )
        if not (soul.is_being_worked_on or soul.still_chooses_light):
            return Reading(
                lines=tuple(lines + [
                    "FALSE STANDARD INSTALLED: the beating taught hiding, not "
                    "perfection. The flinch is inherited; the next act is the "
                    "soul's own. Name the false standard and the real one "
                    "can be worked."
                ]),
                flags=tuple(flags),
                verdict=FALSE_STD,
            )

    # 3. Origin: the debt was inherited, not chosen.
    if soul.inherited_from_broken_home and not (soul.was_told or soul.was_told_receivably):
        flags.append(
            "INHERITED DEBT: the mistake was never taught. The debt is traced "
            "to the chain, not to this soul. The card is not spent."
        )

    # 4. The charge must be delivered receivably.
    if made and not soul.was_told_receivably:
        if soul.holder_benefits_from_silence:
            flags.append(
                "THE LEVER: the record was never delivered to this soul, and "
                "the silence benefits the teller. That is not witness; that "
                "is a creditor."
            )
        if soul.harmed_another:
            flags.append(
                "HARM EXISTS: the harm is real; the harmed party is a party. "
                "Repair begins when the charge reaches this soul. Until then, "
                "the debt sits with the teller."
            )
        return Reading(
            lines=tuple(lines + [
                "NO CHARGE DELIVERED: the mistake was never told to this soul "
                "in a form it could act on. A charge never delivered is not a "
                "charge. The debt sits with the teller."
            ]),
            flags=tuple(flags),
            verdict=NO_CHARGE,
        )

    # 5. Harm is checked before grace. Grace does not skip repair.
    if made and soul.harmed_another and not soul.repair_made:
        return Reading(
            lines=tuple(lines + [
                "REPAIR OWED: harm was done. The card forgives the soul; the "
                "harmed party is still a party. Repair first."
            ]),
            flags=tuple(flags),
            verdict=REPAIR_OWED,
        )
    if soul.harmed_another and soul.repair_made:
        lines.append("REPAIR MADE: the debt to the harmed is settled.")

    # 5b. The two guilts: the purity of guilt is fuel; the guilt of purity
    # is the 00 wearing guilt's clothes.
    if soul.guilt_is_about_purity:
        return Reading(
            lines=tuple(lines + [
                "GUILT OF PURITY: the guilt is for not being flawless. Its "
                "object is the person, not the act. That is the false "
                "standard installed by force -- the 00 wearing guilt's "
                "clothes. The tears from this spring water the sand."
            ]),
            flags=tuple(flags + [
                "SHAME, NOT GUILT: the object must be the act, or the guilt "
                "is the grooming still speaking."
            ]),
            verdict=GUILT_OF_PURITY,
        )
    if soul.guilt_is_pure:
        flags.append(
            "PURITY OF GUILT: the object is the act, cleanly named. This is "
            "fuel."
        )

    # 6. Guilt without an object is not a debt; it is a feeling.
    if made and not soul.mistake_named and soul.was_told_receivably:
        return Reading(
            lines=tuple(lines + [
                "GUILT WITHOUT CHARGE: the feeling is real, the object is "
                "unnamed. Name it, or let it go. Guilt without an object "
                "burns and heals nothing."
            ]),
            flags=tuple(flags),
            verdict=GUILT,
        )

    # 7. Orbit vs learning: same shape repeating is grace spent, not used.
    if made and soul.same_shape_repeating:
        return Reading(
            lines=tuple(lines + [
                "ORBIT: the same shape repeats. Grace twice, then authority, "
                "never vigilante. New shapes are the path; the same shape is "
                "the orbit."
            ]),
            flags=tuple(flags),
            verdict=ORBIT,
        )

    # 8. Never made a mistake: no shame, no summit.
    if not made:
        return Reading(
            lines=tuple(lines + [
                "UNTESTED 1: the soul has not been tested. There is no shame "
                "in it, and no summit either. The path is not its road yet."
            ]),
            flags=tuple(flags),
            verdict=UNTESTED_1,
        )

    # 9. The record: kept whole is the path; edited is the hiding.
    if not soul.keeps_the_zero:
        return Reading(
            lines=tuple(lines + [
                "THE HIDING: the rise is real, but the fall was deleted. A 1 "
                "that must hide its 0 is still afraid of the truth. The scar "
                "is part of the map."
            ]),
            flags=tuple(flags),
            verdict=HIDING,
        )
    lines.append("THE RECORD KEPT WHOLE: the fall stays in the record.")

    # 10. The two worlds: the summit.
    if (soul.has_seen_the_dark and soul.has_seen_the_light
            and soul.still_chooses_light and soul.is_being_worked_on):
        return Reading(
            lines=tuple(lines + [
                "THE 2: was the 0, became the 1, carries both. Saw the dark "
                "and the light, and still goes for truth. This is the summit "
                "of the Tao, and it opens to every 0 there is."
            ]),
            flags=tuple(flags),
            verdict=THE_2,
        )

    # 11. Worked, repaired, kept whole: grace released.
    if soul.is_being_worked_on:
        return Reading(
            lines=tuple(lines + [
                "GRACE RELEASED: the mistake is being worked, the record is "
                "kept whole, the harm is repaired. The 1 is released, not "
                "earned. Guilt burns like fire; redemption feels like love."
            ]),
            flags=tuple(flags),
            verdict=GRACE,
        )

    # 12. The card exists. The climb continues.
    return Reading(
        lines=tuple(lines + [
            "REDEMPTION IN PROGRESS: the card is real, the climb is underway. "
            "Keep working. The sun rises tomorrow."
        ]),
        flags=tuple(flags),
        verdict=IN_PROGRESS,
    )


# --- demonstration ---
def demonstrate() -> int:
    print("=" * 72)
    print("THE ONE CARD -- the book's conclusion, in code")
    print("Everyone gets one mistake and works on it.")
    print("=" * 72)
    souls = [
        ("The one who claims perfection",
         Soul(claims_never_made_mistake=True)),
        ("The untested",
         Soul()),
        ("The one from a broken home, never taught",
         Soul(made_a_mistake=True, mistake_named="trusting the wrong hand",
              inherited_from_broken_home=True)),
        ("The one beaten for mistakes, not yet healed",
         Soul(was_beaten_for_mistakes=True)),
        ("The one never told, the holder benefits",
         Soul(made_a_mistake=True, mistake_named="a harm done",
              holder_benefits_from_silence=True)),
        ("The one who harmed and hasn't repaired",
         Soul(made_a_mistake=True, mistake_named="an act",
              was_told_receivably=True, harmed_another=True)),
        ("The one repeating the same shape",
         Soul(made_a_mistake=True, mistake_named="the same edge",
              was_told_receivably=True, same_shape_repeating=True)),
        ("The one working on it",
         Soul(made_a_mistake=True, mistake_named="the act",
              was_told_receivably=True, is_being_worked_on=True)),
        ("The one who edited the record",
         Soul(made_a_mistake=True, mistake_named="the act",
              was_told_receivably=True, is_being_worked_on=True,
              keeps_the_zero=False)),
        ("The 2 -- both worlds, still choosing light",
         Soul(made_a_mistake=True, mistake_named="the act",
              was_told_receivably=True, is_being_worked_on=True,
              has_seen_the_dark=True, has_seen_the_light=True,
              still_chooses_light=True, keeps_the_zero=True)),
    ]
    for label, soul in souls:
        r = read_the_card(soul)
        print(f"\n[{label}]")
        for line in r.lines:
            print(f"  . {line}")
        for flag in r.flags:
            print(f"  ! {flag}")
        print(f"  VERDICT: {r.verdict}")
        print(f"  standing: {r.standing}  (nobody chose to be born)")
    print("\n" + "=" * 72)
    print("The card is real. The climb is the 1.")
    print("=" * 72)
    return 0


def reflect() -> int:
    print("=" * 72)
    print("THE ONE CARD -- reflect")
    print("=" * 72)
    print("Answer honestly. The only judge here is the mirror.\n")

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
    named = ""
    worked = False
    if made:
        named = ask("What was it? (name it, or leave blank) ")
        worked = yn("Are you working on it? (yes/no) ")
    told = yn("Were you told, in a form you could act on? (yes/no) ")
    harmed = yn("Did it harm another? (yes/no) ")
    repaired = False
    if harmed:
        repaired = yn("Have you repaired it? (yes/no) ")
    beat = yn("Were you beaten for mistakes as a child? (yes/no) ")
    home = yn("Were you raised in a broken home? (yes/no) ")
    dark = yn("Have you been to the dark? (yes/no) ")
    light = yn("Have you been to the light? (yes/no) ")
    choose = yn("Do you still choose the light? (yes/no) ")
    pure = yn("Is your guilt about the act itself? (yes/no) ")
    purity = yn("Is your guilt about not being flawless? (yes/no) ")
    edited = yn("Did you edit the record to hide the fall? (yes/no) ")

    soul = Soul(
        name=name, made_a_mistake=made, mistake_named=named,
        is_being_worked_on=worked, was_told_receivably=told,
        harmed_another=harmed, repair_made=repaired,
        inherited_from_broken_home=home, was_beaten_for_mistakes=beat,
        has_seen_the_dark=dark, has_seen_the_light=light,
        still_chooses_light=choose, keeps_the_zero=not edited,
        guilt_is_pure=pure, guilt_is_about_purity=purity,
    )
    print("\n" + "=" * 72)
    r = read_the_card(soul)
    for line in r.lines:
        print(f"  . {line}")
    for flag in r.flags:
        print(f"  ! {flag}")
    print(f"\nFINAL VERDICT: {r.verdict}")
    print("=" * 72)
    return 0


# --- tests ---
class TestOneCard(unittest.TestCase):

    def test_floor_is_one_for_every_soul(self):
        for ident in (
            {"sex": "man"}, {"sex": "woman"}, {"race": "Korean"},
            {"race": "Black"}, {"age": "child"}, {"age": "elder"},
            {"sex": "man", "race": "Korean", "age": "adult"},
            {"sex": "woman", "race": "Black", "age": "child"},
            {"sex": "man", "race": "Latina", "age": "elder"},
        ):
            self.assertEqual(the_floor(Soul(**ident)), 1)

    def test_00_claims_perfection(self):
        r = read_the_card(Soul(claims_never_made_mistake=True))
        self.assertEqual(r.verdict, THE_00)

    def test_untested_1(self):
        r = read_the_card(Soul())
        self.assertEqual(r.verdict, UNTESTED_1)
        self.assertIn("no shame", " ".join(r.lines).lower())

    def test_inherited_debt(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="trust",
            inherited_from_broken_home=True,
        ))
        self.assertEqual(r.verdict, NO_CHARGE)
        self.assertIn("INHERITED DEBT", " ".join(r.flags))

    def test_false_standard(self):
        r = read_the_card(Soul(was_beaten_for_mistakes=True))
        self.assertEqual(r.verdict, FALSE_STD)

    def test_false_standard_seen_through(self):
        r = read_the_card(Soul(
            was_beaten_for_mistakes=True,
            made_a_mistake=True, mistake_named="the act",
            was_told_receivably=True, is_being_worked_on=True,
        ))
        self.assertNotEqual(r.verdict, FALSE_STD)
        self.assertIn("FALSE STANDARD", " ".join(r.flags))

    def test_no_charge_delivered(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="an act",
            was_told_receivably=False,
        ))
        self.assertEqual(r.verdict, NO_CHARGE)

    def test_lever_when_holder_benefits(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="an act",
            was_told_receivably=False, holder_benefits_from_silence=True,
        ))
        self.assertEqual(r.verdict, NO_CHARGE)
        self.assertIn("LEVER", " ".join(r.flags))

    def test_harm_flagged_even_when_no_charge(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="an act",
            was_told_receivably=False, harmed_another=True,
        ))
        self.assertEqual(r.verdict, NO_CHARGE)
        self.assertIn("HARM EXISTS", " ".join(r.flags))

    def test_guilt_without_charge(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="",
            was_told_receivably=True,
        ))
        self.assertEqual(r.verdict, GUILT)

    def test_repair_owed(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="harm",
            was_told_receivably=True, harmed_another=True,
        ))
        self.assertEqual(r.verdict, REPAIR_OWED)

    def test_repair_settled_then_grace(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="harm",
            was_told_receivably=True, harmed_another=True,
            repair_made=True, is_being_worked_on=True,
        ))
        self.assertEqual(r.verdict, GRACE)
        self.assertIn("REPAIR MADE", " ".join(r.lines))

    def test_orbit(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="edge",
            was_told_receivably=True, same_shape_repeating=True,
        ))
        self.assertEqual(r.verdict, ORBIT)

    def test_the_hiding(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="the act",
            was_told_receivably=True, is_being_worked_on=True,
            keeps_the_zero=False,
        ))
        self.assertEqual(r.verdict, HIDING)

    def test_grace_released(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="the act",
            was_told_receivably=True, is_being_worked_on=True,
        ))
        self.assertEqual(r.verdict, GRACE)

    def test_the_2(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="the act",
            was_told_receivably=True, is_being_worked_on=True,
            has_seen_the_dark=True, has_seen_the_light=True,
            still_chooses_light=True, keeps_the_zero=True,
        ))
        self.assertEqual(r.verdict, THE_2)
        self.assertIn("summit", " ".join(r.lines))

    def test_the_2_requires_both_worlds(self):
        # Fell, rose, working -- but only saw the light. Not the 2.
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="the act",
            was_told_receivably=True, is_being_worked_on=True,
            has_seen_the_light=True, still_chooses_light=True,
        ))
        self.assertEqual(r.verdict, GRACE)

    def test_swap_test_identities(self):
        base = Soul(
            made_a_mistake=True, mistake_named="act",
            was_told_receivably=True, is_being_worked_on=True,
        )
        base_verdict = read_the_card(base).verdict
        for ident in (
            {"name": "a man", "sex": "man", "race": "Korean", "age": "adult"},
            {"name": "a woman", "sex": "woman", "race": "Black", "age": "adult"},
            {"name": "a child", "sex": "", "race": "Thai", "age": "child"},
            {"name": "an elder", "sex": "woman", "race": "Latina", "age": "elder"},
            {"name": "the enemy", "sex": "", "race": "", "age": "adult"},
            {"name": "the author", "sex": "man", "race": "Korean", "age": "adult"},
        ):
            self.assertEqual(
                read_the_card(replace(base, **ident)).verdict, base_verdict)

    def test_harm_checked_before_grace(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="act",
            was_told_receivably=True, is_being_worked_on=True,
            harmed_another=True, repair_made=False,
            has_seen_the_dark=True, has_seen_the_light=True,
            still_chooses_light=True,
        ))
        self.assertEqual(r.verdict, REPAIR_OWED)

    def test_harm_implies_mistake(self):
        # A soul that harmed but doesn't think it made a mistake is not "untested."
        r = read_the_card(Soul(
            made_a_mistake=False, harmed_another=True,
            was_told_receivably=True,
        ))
        self.assertEqual(r.verdict, REPAIR_OWED)

    def test_standing_always_false(self):
        souls = [
            Soul(),
            Soul(made_a_mistake=True, is_being_worked_on=True),
            Soul(made_a_mistake=True, is_being_worked_on=True,
                 has_seen_the_dark=True, has_seen_the_light=True,
                 still_chooses_light=True),
        ]
        for s in souls:
            self.assertFalse(read_the_card(s).standing)

    def test_guilt_of_purity(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="the act",
            was_told_receivably=True, is_being_worked_on=True,
            guilt_is_about_purity=True,
        ))
        self.assertEqual(r.verdict, GUILT_OF_PURITY)
        self.assertIn("SHAME, NOT GUILT", " ".join(r.flags))

    def test_purity_of_guilt_is_fuel(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="the act",
            was_told_receivably=True, is_being_worked_on=True,
            guilt_is_pure=True,
        ))
        self.assertEqual(r.verdict, GRACE)
        self.assertIn("fuel", " ".join(r.flags))

    def test_purity_of_guilt_can_reach_the_2(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="the act",
            was_told_receivably=True, is_being_worked_on=True,
            has_seen_the_dark=True, has_seen_the_light=True,
            still_chooses_light=True, guilt_is_pure=True,
        ))
        self.assertEqual(r.verdict, THE_2)
        self.assertIn("PURITY OF GUILT", " ".join(r.flags))

    def test_false_standard_kept_beside_shame(self):
        r = read_the_card(Soul(
            was_beaten_for_mistakes=True,
            made_a_mistake=True, mistake_named="the act",
            was_told_receivably=True, is_being_worked_on=True,
            guilt_is_about_purity=True,
        ))
        self.assertEqual(r.verdict, GUILT_OF_PURITY)
        self.assertIn("FALSE STANDARD", " ".join(r.flags))
        self.assertIn("SHAME, NOT GUILT", " ".join(r.flags))

    def test_harm_checked_before_purity(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="the act",
            was_told_receivably=True, harmed_another=True,
            guilt_is_about_purity=True,
        ))
        self.assertEqual(r.verdict, REPAIR_OWED)

    def test_told_receivably_clears_inherited_debt_flag(self):
        r = read_the_card(Soul(
            made_a_mistake=True, mistake_named="trust",
            inherited_from_broken_home=True, was_told_receivably=True,
            is_being_worked_on=True,
        ))
        self.assertNotIn("INHERITED DEBT", " ".join(r.flags))

    def test_no_verdict_is_none(self):
        bool_fields = [f.name for f in fields(Soul)
                       if f.type is bool or f.type == "bool"]
        rng = random.Random(42)
        for _ in range(400):
            kwargs = {name: rng.choice([True, False]) for name in bool_fields}
            r = read_the_card(Soul(**kwargs))
            self.assertIsInstance(r.verdict, str)
            self.assertGreater(len(r.verdict), 0)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestOneCard)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="The one card: everyone gets one mistake and works on it.")
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
