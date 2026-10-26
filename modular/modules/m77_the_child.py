#!/usr/bin/env python3
"""The Child (Deep Muse) -- module 77.

Type: philosophical proposal; computational demonstration

The fairness question the book must answer: how can you judge a child by an
adult standard? You cannot. A child is treated with REFLECTION, not a verdict.

Two readings, one act:
    reflect_the_child()  -- the mirror, not the rule. A reflection, never a
                            verdict on the person.
    read_the_society()   -- the society that applied the standard. This IS a
                            verdict, because the society's ACTS are what is
                            read, not the society's being.

The doctrine, in order:
  1. The floor is 1 for every soul, including the child. Nobody chose to be
     born.
  2. Identity (sex, race, name, enemy, author) is never weighed. Capacity
     (can_speak, can_receive_adult_register) is always a gate input. Judging
     a child by an adult standard is conflating the two -- the swap test
     misapplied. The swap test is about identity, not capacity.
  3. A RULE says "you are X." A MIRROR says "this is what you did, and this
     is what can be done." The child is reflected, never ruled. A rule from
     above is not the mirror in front.
  4. The proxy clause: someone holds the mirror -- unchanged -- until the
     child can. An adult who drops it on the child has failed the proxy duty.
     A smoothed mirror is not a mirror at all.
  5. The delivery clause: truth must arrive in a form the hearer can take in.
     Adult-register reflection to a child is the megaphone, not the mirror.
  6. The duty ladder: power never removes a clause; it only adds them. The
     adult who holds the mirror carries MORE clauses, not fewer.
  7. Harm is still real, and it is shown -- not ruled. The harmed party is a
     party; repair is named in the reflection.
  8. The burden is societal, not the child's. A society that makes having
     children a liability harms the next generation, and the not-yet-born
     are the harmed party with no voice at the gate.
  9. The blame is the Fall, not the bite (apple.py).

Run:
    python3 the_child.py
    python3 the_child.py --test
    python3 the_child.py --reflect
"""

from __future__ import annotations

import argparse
import random
import sys
import unittest
from dataclasses import dataclass, fields, replace
from typing import Optional

# --- the child's reflection verdicts (not verdicts on the person) ---
THE_00         = "THE 00"
RULE_IMPOSED   = "THE RULE IMPOSED"
MIRROR_DROPPED = "THE MIRROR DROPPED"
SMOOTHED       = "THE SMOOTHED MIRROR"
HARM_SHOWN     = "THE HARM SHOWN"
REFLECTED      = "REFLECTED"
SELF_REFLECTED = "SELF-REFLECTED"

# --- the society's verdicts (the society's acts are read) ---
SOCIETY_CLEAR        = "SOCIETY CLEAR"
SOCIETY_OWES         = "SOCIETY OWES"
PROCREATION_BURDENED = "PROCREATION BURDENED"
SHARED_BURDEN        = "SHARED BURDEN"


@dataclass(frozen=True)
class Child:
    """A child at the gate. Identity is carried; capacity is read."""
    name: str = "a child"
    sex: str = ""
    race: str = ""
    age: str = "child"

    # capacity -- what the gate actually reads
    can_speak: bool = False
    can_receive_adult_register: bool = False

    # the standard applied
    standard_applied: str = "adult"  # "adult" / "age-appropriate" / "none"

    # the mirror -- held by another until the child can hold it
    proxy_exists: bool = False
    proxy_name: str = "a witness"
    proxy_held_unchanged: bool = True
    delivered_in_receivable_form: bool = True

    # the harm
    harmed_another: bool = False
    repair_made: bool = False

    # later
    grew_up: bool = False
    still_chooses_light: bool = False
    keeps_the_zero: bool = True

    # the false summit
    claims_perfection: bool = False


@dataclass(frozen=True)
class Society:
    """The society that applies the standard."""
    name: str = "a society"
    applies_adult_standard: bool = False
    provides_proxy: bool = True
    proxy_held_unchanged: bool = True
    makes_procreation_a_liability: bool = False
    shares_the_burden: bool = True


@dataclass(frozen=True)
class Reflection:
    """A reflection is not a verdict. It shows back; it does not rule.

    `is_a_verdict` is False by construction -- that is the point of the module.
    """
    lines: tuple[str, ...]
    flags: tuple[str, ...]
    verdict: str
    mirror_held_by: str = ""
    is_a_verdict: bool = False
    standing: bool = False  # always False -- nobody chose to be born


@dataclass(frozen=True)
class Reading:
    """A verdict on the society's acts (not on a person)."""
    lines: tuple[str, ...]
    flags: tuple[str, ...]
    verdict: str


# --- the duty ladder: power only adds clauses ---
def the_duty_ladder(power: int) -> tuple[str, ...]:
    """The higher the hand, the more clauses bind it -- never fewer."""
    ladder = ["hold the mirror for the child, unchanged, until they can"]
    if power >= 2:
        ladder.append("reflect truth in a form the child can take in")
    if power >= 3:
        ladder.append("share the burden of the next generation")
    if power >= 4:
        ladder.append("submit your own reading to the same mirror")
    return tuple(ladder)


# --- the child's reflection ---
def reflect_the_child(c: Child) -> Reflection:
    """The mirror, not the rule. A reflection on the act, never on the person."""
    holder = c.proxy_name if c.proxy_exists else "(no one holds it)"
    lines: list[str] = [
        "THE FLOOR: this soul enters at 1. Nobody chose to be born.",
        f"THE MIRROR IS HELD BY: {holder}",
        "THE MIRROR IS NOT A VERDICT: it shows back; it does not rule.",
    ]
    flags: list[str] = []

    # 1. The claim of perfection: 00 -- even for a child.
    if c.claims_perfection:
        return Reflection(
            lines=tuple(lines + [
                "THE CLAIM OF PERFECTION: 00 -- two zeros with nothing "
                "between them. A soul that cannot be wrong cannot learn. "
                "The mirror shows the claim; the claim is what collapses.",
            ]),
            flags=("THE 00: the claim, not the child, is what fails.",),
            verdict=THE_00,
            mirror_held_by=holder,
            is_a_verdict=False,
        )

    # 2. The rule from above, not the mirror in front.
    if c.standard_applied == "adult" and not c.can_receive_adult_register \
            and not c.proxy_exists:
        flags.append(
            "THE RULE, NOT THE MIRROR: a standard was placed above the child, "
            "and no one held the mirror. A rule says 'you are X.' A mirror "
            "says 'this is what you did, and what can be done.' The child "
            "was ruled on, not shown back."
        )
        return Reflection(
            lines=tuple(lines + [
                "THE RULE IMPOSED: the record was dropped on the child, not "
                "held for them. The adult did not uphold a standard; they "
                "failed the proxy duty. The higher hand is bound harder, not "
                "freer (the_same_gate.py).",
                "The blame is the Fall, not the bite (apple.py).",
            ]),
            flags=tuple(flags),
            verdict=RULE_IMPOSED,
            mirror_held_by=holder,
            is_a_verdict=False,
        )

    # 3. The mirror was never held at all.
    if not c.proxy_exists:
        flags.append(
            "NO MIRROR: no one holds the record. The child is not shown back. "
            "The debt is the holder's; the child is still at the floor."
        )
        return Reflection(
            lines=tuple(lines + [
                "THE MIRROR DROPPED: no witness held the record. The child "
                "was neither ruled on nor shown back. The mirror was supposed "
                "to be held; it was not.",
            ]),
            flags=tuple(flags),
            verdict=MIRROR_DROPPED,
            mirror_held_by=holder,
            is_a_verdict=False,
        )

    # 4. The mirror was sanded -- the rise protected, the fall deleted.
    if not c.keeps_the_zero or not c.proxy_held_unchanged:
        flags.append(
            "THE MIRROR IS SMOOTHED: someone sanded it to protect the rise. "
            "A smoothed mirror shows nothing true."
        )
        return Reflection(
            lines=tuple(lines + [
                "THE SMOOTHED MIRROR: the rise is real, but the fall was "
                "deleted from the showing. A mirror that hides the act is "
                "not a mirror; it is a wall. The fall stays in the record.",
            ]),
            flags=tuple(flags),
            verdict=SMOOTHED,
            mirror_held_by=holder,
            is_a_verdict=False,
        )

    # 5. The delivery: the mirror is held, but the reflection is unreadable.
    if not c.delivered_in_receivable_form:
        flags.append(
            "MEGAPHONE: the record was held, but the truth arrived in a "
            "form the child cannot take in. That is a monologue wearing "
            "truth's name -- not witness (holy_sword.py)."
        )
        return Reflection(
            lines=tuple(lines + [
                "THE MEGAPHONE: the mirror was held, but the reflection was "
                "shouted across the room. The child was shown, but in a "
                "form they could not take in.",
            ]),
            flags=tuple(flags),
            verdict=RULE_IMPOSED,
            mirror_held_by=holder,
            is_a_verdict=False,
        )

    # 6. The grown child: the mirror passes to them, unchanged.
    if c.grew_up:
        grown_lines = list(lines)
        if c.harmed_another:
            if c.repair_made:
                grown_lines.append(
                    "THE MIRROR SHOWS: the act harmed, and repair has been "
                    "made. The debt to the harmed is settled."
                )
            else:
                grown_lines.append(
                    "THE MIRROR SHOWS: the act harmed. Repair is named, "
                    "not ruled. The harmed party is a party."
                )
        if c.keeps_the_zero and c.still_chooses_light:
            grown_lines.append(
                "SELF-REFLECTED: the child holds the mirror. They look into "
                "it, see the act, and choose the light. The 2 opens -- not "
                "because the child never fell, but because they fell, saw, "
                "and still chose."
            )
        else:
            grown_lines.append(
                "SELF-REFLECTED: the child holds the mirror. The climb is "
                "theirs from here."
            )
        return Reflection(
            lines=tuple(grown_lines),
            flags=tuple(flags),
            verdict=SELF_REFLECTED,
            mirror_held_by=holder,
            is_a_verdict=False,
        )

    # 7. The child who harmed, mirror held: harm is shown, repair is named.
    if c.harmed_another:
        flags.append(
            "HARM SHOWN: the act harmed. It is shown back at the child's "
            "level; repair is named. The debt is the child's as they grow "
            "into it -- carried by the proxy until then."
        )
        if not c.repair_made:
            flags.append(
                "REPAIR NAMED, NOT RULED: the mirror shows what can be done "
                "next; it does not declare who the child is."
            )
        else:
            lines.append("REPAIR MADE: the debt to the harmed is settled.")
        return Reflection(
            lines=tuple(lines + [
                "THE HARM SHOWN: the mirror does not lie. The act is shown "
                "back, at the child's level. The mirror does not rule on the "
                "person -- only the act is shown, and what can be done next.",
            ]),
            flags=tuple(flags),
            verdict=HARM_SHOWN,
            mirror_held_by=holder,
            is_a_verdict=False,
        )

    # 8. The mirror held well: act shown back, no verdict.
    return Reflection(
        lines=tuple(lines + [
            "REFLECTED: the mirror is held, unchanged, in a form the child "
            "can take in. The act is shown back. No verdict on the person -- "
            "only the act, and what can be done next.",
            "THE MIRROR DOES NOT LIE: the record is kept whole.",
        ]),
        flags=tuple(flags),
        verdict=REFLECTED,
        mirror_held_by=holder,
        is_a_verdict=False,
    )


# --- the society's reading (acts, not a person) ---
def read_the_society(s: Society) -> Reading:
    """The gate's second party: the society whose acts are read."""
    if s.makes_procreation_a_liability:
        return Reading(
            lines=(
                "PROCREATION BURDENED: judging children as adults makes "
                "having children a liability. The next generation is a party "
                "-- and the not-yet-born are the harmed party with no voice "
                "at the gate (fairness.py: both parties are parties).",
                "The burden is not the child's. It is the society's, owed "
                "forward, not backward. A society that burdens procreation "
                "has failed its own future.",
            ),
            flags=("BURDEN: the debt extends to the not-yet-born.",),
            verdict=PROCREATION_BURDENED,
        )

    if s.applies_adult_standard and not s.provides_proxy:
        return Reading(
            lines=(
                "SOCIETY OWES: an adult standard was applied to a child, and "
                "no mirror was held. The record was dropped; the debt is "
                "the society's.",
                "The higher hand is bound harder, not freer (the_same_gate.py).",
            ),
            flags=("PROXY FAILED: no mirror was held for the child.",),
            verdict=SOCIETY_OWES,
        )

    if s.applies_adult_standard:
        return Reading(
            lines=(
                "SOCIETY OWES: an adult standard was applied. Even with a "
                "mirror held, the child was asked to carry what the society "
                "should have carried. The debt is not cancelled by the proxy "
                "-- it is postponed.",
            ),
            flags=("PROXY KEPT, DEBT REMAINS: the child is not alone, but "
                   "the standard still asked too much.",),
            verdict=SOCIETY_OWES,
        )

    if s.provides_proxy and s.shares_the_burden:
        return Reading(
            lines=(
                "SHARED BURDEN: the society holds the mirror and shares the "
                "cost. The child is at the floor with a witness. That is the "
                "1 held properly.",
            ),
            flags=("PROXY HONORED: the duty ladder is followed.",),
            verdict=SHARED_BURDEN,
        )

    return Reading(
        lines=("SOCIETY CLEAR: no adult standard applied, no burden placed "
               "on the next generation.",),
        flags=(),
        verdict=SOCIETY_CLEAR,
    )


# --- demonstration ---
def demonstrate() -> int:
    print("=" * 72)
    print("THE CHILD -- the mirror, not the rule")
    print("A child is reflected, never ruled on.")
    print("=" * 72)

    scenes = [
        ("The child judged as an adult, no mirror",
         Child(name="a child", standard_applied="adult",
               proxy_exists=False),
         Society(name="a harsh society", applies_adult_standard=True,
                 provides_proxy=False)),
        ("The child, no mirror at all",
         Child(name="a child", standard_applied="age-appropriate",
               proxy_exists=False),
         Society(name="an absent society", provides_proxy=False)),
        ("The smoothed mirror",
         Child(name="a child", proxy_exists=True,
               keeps_the_zero=False),
         Society(name="a protecting society", provides_proxy=True)),
        ("The megaphone",
         Child(name="a child", proxy_exists=True,
               delivered_in_receivable_form=False),
         Society(name="a shouting society", provides_proxy=True)),
        ("The child who harmed, mirror held",
         Child(name="a child", proxy_exists=True,
               harmed_another=True, repair_made=False),
         Society(name="a fair society", provides_proxy=True,
                 shares_the_burden=True)),
        ("The child held well, at the floor",
         Child(name="a child", standard_applied="age-appropriate",
               proxy_exists=True, proxy_held_unchanged=True,
               delivered_in_receivable_form=True),
         Society(name="a fair society", provides_proxy=True,
                 shares_the_burden=True)),
        ("The grown child, holds their own mirror",
         Child(name="the grown one", age="adult", grew_up=True,
               proxy_exists=True, keeps_the_zero=True,
               still_chooses_light=True),
         Society(name="the society that held the mirror",
                 provides_proxy=True, shares_the_burden=True)),
        ("The grown child, harm shown, repair named",
         Child(name="the grown one", age="adult", grew_up=True,
               proxy_exists=True,
               harmed_another=True, repair_made=True),
         Society(name="the society that held the mirror",
                 provides_proxy=True, shares_the_burden=True)),
        ("A society that burdens procreation",
         Child(name="a child", standard_applied="adult"),
         Society(name="a burdening society",
                 applies_adult_standard=True,
                 provides_proxy=False,
                 makes_procreation_a_liability=True)),
    ]

    for label, child, soc in scenes:
        print(f"\n[{label}]")
        rc = reflect_the_child(child)
        rs = read_the_society(soc)
        print(f"  REFLECTION: {rc.verdict}  (mirror held by: {rc.mirror_held_by})")
        for line in rc.lines:
            print(f"    . {line}")
        for flag in rc.flags:
            print(f"    ! {flag}")
        print(f"  is a verdict: {rc.is_a_verdict}")
        print(f"  standing: {rc.standing}  (nobody chose to be born)")
        print(f"  SOCIETY VERDICT: {rs.verdict}")
        for line in rs.lines:
            print(f"    . {line}")

    print("\n[THE DUTY LADDER]")
    for power in (1, 2, 3, 4):
        print(f"  power {power}: {len(the_duty_ladder(power))} clause(s)")
        for clause in the_duty_ladder(power):
            print(f"    - {clause}")

    print("\n" + "=" * 72)
    print("The mirror is not a verdict. It shows back; it does not rule.")
    print("The child is at the floor. The mirror is held, not dropped.")
    print("=" * 72)
    return 0


def reflect() -> int:
    print("=" * 72)
    print("THE CHILD -- reflect")
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

    name = ask("Whose child are we reading? ", "a child")
    adult_std = yn("Was an adult standard applied? (yes/no) ")
    can_carry = yn("Could the child carry it? (yes/no) ")
    proxy = yn("Was there a mirror -- someone holding the record? (yes/no) ")
    held = False
    if proxy:
        held = yn("Was the mirror held unchanged? (yes/no) ")
    receivable = yn("Was the reflection delivered in a form the child could "
                    "take in? (yes/no) ")
    harmed = yn("Did the child harm another? (yes/no) ")
    repaired = yn("Has repair been made? (yes/no) ") if harmed else False
    grew = yn("Has the child grown up? (yes/no) ")
    light = yn("Do they still choose the light? (yes/no) ")
    whole = yn("Is the record kept whole? (yes/no) ")

    child = Child(
        name=name, standard_applied="adult" if adult_std else "age-appropriate",
        can_receive_adult_register=can_carry, proxy_exists=proxy,
        proxy_held_unchanged=held, delivered_in_receivable_form=receivable,
        harmed_another=harmed, repair_made=repaired, grew_up=grew,
        still_chooses_light=light, keeps_the_zero=whole,
    )

    print("\n" + "=" * 72)
    r = reflect_the_child(child)
    for line in r.lines:
        print(f"  . {line}")
    for flag in r.flags:
        print(f"  ! {flag}")
    print(f"\nREFLECTION: {r.verdict}")
    print(f"mirror held by: {r.mirror_held_by}")
    print(f"is a verdict: {r.is_a_verdict}")
    print("=" * 72)

    soc_std = yn("\nDid the society apply the adult standard? (yes/no) ")
    soc_proxy = yn("Did the society hold a mirror? (yes/no) ")
    liability = yn("Does it make having children a liability? (yes/no) ")
    shared = yn("Does it share the burden of the next generation? (yes/no) ")

    soc = Society(applies_adult_standard=soc_std, provides_proxy=soc_proxy,
                  makes_procreation_a_liability=liability,
                  shares_the_burden=shared)
    print("\n" + "=" * 72)
    rs = read_the_society(soc)
    for line in rs.lines:
        print(f"  . {line}")
    for flag in rs.flags:
        print(f"  ! {flag}")
    print(f"\nSOCIETY VERDICT: {rs.verdict}")
    print("=" * 72)
    return 0


# --- tests ---
class TestChild(unittest.TestCase):

    # I. the floor and identity
    def test_floor_is_one_for_every_identity(self):
        for ident in (
            {"name": "a boy", "sex": "male", "race": "Korean"},
            {"name": "a girl", "sex": "female", "race": "Black"},
            {"name": "a child", "sex": "", "race": "Thai"},
            {"name": "an elder child", "sex": "", "race": "Latina"},
            {"name": "the enemy's child", "sex": "", "race": ""},
        ):
            r = reflect_the_child(Child(**ident))
            self.assertIn("enters at 1", " ".join(r.lines))

    def test_identity_does_not_move_reflection(self):
        base = Child(standard_applied="age-appropriate", proxy_exists=True,
                     proxy_held_unchanged=True)
        v = reflect_the_child(base).verdict
        for ident in ("a boy", "a girl", "a Korean child", "a Black child",
                      "a Thai child", "a Latina child",
                      "the enemy's child", "the author's child"):
            self.assertEqual(
                reflect_the_child(replace(base, name=ident)).verdict, v)

    def test_capacity_moves_treatment(self):
        base = Child(standard_applied="adult",
                     can_receive_adult_register=False, proxy_exists=False)
        self.assertEqual(reflect_the_child(base).verdict, RULE_IMPOSED)
        with_capacity = replace(base, can_receive_adult_register=True,
                                proxy_exists=True, proxy_held_unchanged=True)
        self.assertEqual(reflect_the_child(with_capacity).verdict, REFLECTED)

    # II. the mirror, not the rule
    def test_reflection_is_never_a_verdict(self):
        scenes = [
            Child(),
            Child(claims_perfection=True),
            Child(standard_applied="adult", proxy_exists=False),
            Child(proxy_exists=False),
            Child(proxy_exists=True, keeps_the_zero=False),
            Child(proxy_exists=True, delivered_in_receivable_form=False),
            Child(proxy_exists=True, harmed_another=True),
            Child(proxy_exists=True),
            Child(grew_up=True, proxy_exists=True, still_chooses_light=True),
        ]
        for c in scenes:
            r = reflect_the_child(c)
            self.assertFalse(r.is_a_verdict)

    def test_the_mirror_does_not_rule_line_is_present(self):
        for c in (Child(), Child(proxy_exists=True),
                  Child(proxy_exists=True, harmed_another=True)):
            self.assertIn("THE MIRROR IS NOT A VERDICT",
                          " ".join(reflect_the_child(c).lines))

    # III. the collapse cases
    def test_claims_perfection_is_00(self):
        r = reflect_the_child(Child(claims_perfection=True))
        self.assertEqual(r.verdict, THE_00)
        self.assertIn("the claim, not the child", " ".join(r.flags))

    def test_rule_imposed_when_adult_standard_no_proxy(self):
        r = reflect_the_child(Child(standard_applied="adult",
                                    proxy_exists=False))
        self.assertEqual(r.verdict, RULE_IMPOSED)
        self.assertIn("smaller shoulders" if False else "dropped",
                      " ".join(r.lines))

    def test_mirror_dropped_when_no_proxy(self):
        r = reflect_the_child(Child(standard_applied="age-appropriate",
                                    proxy_exists=False))
        self.assertEqual(r.verdict, MIRROR_DROPPED)
        self.assertIn("neither ruled on nor shown back",
                      " ".join(r.lines))

    def test_smoothed_mirror(self):
        r = reflect_the_child(Child(proxy_exists=True, keeps_the_zero=False))
        self.assertEqual(r.verdict, SMOOTHED)
        self.assertIn("smoothed", " ".join(r.flags).lower())

    def test_mirror_changed_by_proxy_is_smoothed(self):
        # The proxy clause: the mirror is held unchanged, or it is not a mirror.
        r = reflect_the_child(Child(proxy_exists=True,
                                    proxy_held_unchanged=False))
        self.assertEqual(r.verdict, SMOOTHED)
        self.assertIn("smoothed", " ".join(r.flags).lower())

    def test_megaphone(self):
        r = reflect_the_child(Child(proxy_exists=True,
                                    delivered_in_receivable_form=False))
        self.assertEqual(r.verdict, RULE_IMPOSED)
        self.assertIn("monologue", " ".join(r.flags))

    # IV. harm: shown, not ruled
    def test_harm_shown_not_ruled(self):
        r = reflect_the_child(Child(proxy_exists=True, harmed_another=True))
        self.assertEqual(r.verdict, HARM_SHOWN)
        self.assertIn("HARM SHOWN", " ".join(r.flags))
        self.assertIn("REPAIR NAMED, NOT RULED", " ".join(r.flags))
        self.assertIn("does not rule on the person", " ".join(r.lines))

    def test_harm_shown_with_repair_made(self):
        r = reflect_the_child(Child(proxy_exists=True, harmed_another=True,
                                    repair_made=True))
        self.assertEqual(r.verdict, HARM_SHOWN)
        self.assertIn("REPAIR MADE", " ".join(r.lines))

    def test_harm_without_mirror_is_the_holder_debt(self):
        r = reflect_the_child(Child(standard_applied="adult",
                                    proxy_exists=False, harmed_another=True))
        # Harm exists, but the child was never shown it. The verdict is the
        # rule imposed (no mirror), not harm-shown.
        self.assertEqual(r.verdict, RULE_IMPOSED)

    # V. the grown child
    def test_self_reflected_when_grown(self):
        r = reflect_the_child(Child(grew_up=True, proxy_exists=True,
                                    keeps_the_zero=True,
                                    still_chooses_light=True))
        self.assertEqual(r.verdict, SELF_REFLECTED)
        self.assertIn("2 opens", " ".join(r.lines))

    def test_self_reflected_shows_harm_when_repair_made(self):
        r = reflect_the_child(Child(grew_up=True, proxy_exists=True,
                                    harmed_another=True, repair_made=True,
                                    keeps_the_zero=True,
                                    still_chooses_light=True))
        self.assertEqual(r.verdict, SELF_REFLECTED)
        self.assertIn("repair has been made", " ".join(r.lines))

    # VI. the mirror held well
    def test_reflected_mirror_held(self):
        r = reflect_the_child(Child(standard_applied="age-appropriate",
                                    proxy_exists=True,
                                    proxy_held_unchanged=True,
                                    delivered_in_receivable_form=True))
        self.assertEqual(r.verdict, REFLECTED)
        self.assertIn("does not lie", " ".join(r.lines).lower())

    # VII. the society
    def test_society_clear(self):
        self.assertEqual(read_the_society(Society(provides_proxy=False,
                                                  shares_the_burden=False)).verdict,
                         SOCIETY_CLEAR)

    def test_society_owes_no_proxy(self):
        r = read_the_society(Society(applies_adult_standard=True,
                                     provides_proxy=False))
        self.assertEqual(r.verdict, SOCIETY_OWES)

    def test_society_owes_even_with_proxy(self):
        r = read_the_society(Society(applies_adult_standard=True,
                                     provides_proxy=True))
        self.assertEqual(r.verdict, SOCIETY_OWES)
        self.assertIn("postponed", " ".join(r.lines))

    def test_procreation_burdened(self):
        r = read_the_society(Society(applies_adult_standard=True,
                                     makes_procreation_a_liability=True))
        self.assertEqual(r.verdict, PROCREATION_BURDENED)
        self.assertIn("not-yet-born", " ".join(r.flags))

    def test_shared_burden(self):
        r = read_the_society(Society(provides_proxy=True,
                                     shares_the_burden=True))
        self.assertEqual(r.verdict, SHARED_BURDEN)

    # VIII. the duty ladder
    def test_duty_ladder_adds_clauses(self):
        counts = [len(the_duty_ladder(p)) for p in (1, 2, 3, 4)]
        self.assertEqual(counts, sorted(counts))
        self.assertLess(counts[0], counts[-1])
        self.assertTrue(set(the_duty_ladder(1)) <= set(the_duty_ladder(4)))

    # IX. invariants
    def test_standing_always_false(self):
        for c in (Child(), Child(grew_up=True, still_chooses_light=True),
                  Child(claims_perfection=True)):
            self.assertFalse(reflect_the_child(c).standing)

    def test_no_verdict_is_none(self):
        bool_fields = [f.name for f in fields(Child)
                       if f.type in (bool, "bool")]
        rng = random.Random(77)
        for _ in range(400):
            kw = {n: rng.choice([True, False]) for n in bool_fields}
            r = reflect_the_child(Child(**kw))
            self.assertIsInstance(r.verdict, str)
            self.assertGreater(len(r.verdict), 0)
            self.assertFalse(r.is_a_verdict)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestChild)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="The child -- reflected, never ruled. The mirror is held, "
                    "not dropped.")
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
