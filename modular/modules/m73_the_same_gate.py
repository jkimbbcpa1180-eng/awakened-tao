# the_same_gate.py
# Copyright (c) Humanity — released under CC0.
# Type: philosophical proposal; computational demonstration
#
# THE SAME GATE — what aligns with truth and fairness for all people,
# for awakened_light / Awaken Tao. Man, woman, child, every race:
# humanity. Five clauses, and above them the highest level of the Tao.
#
# The claims, as built:
#
#   1. THE SAME GATE. Every reader in this framework reads ACTS, never
#      IDENTITIES. A gate may take what a person did as input; it may
#      never take what a person is. If a verdict changes when the
#      people are swapped — man for woman, one race for another,
#      friend for enemy — the principle was about identity, not truth.
#      Universality is not a claim written at the top of the book. It
#      is a test the whole book has to pass. The swap test below is
#      that test, as real code.
#
#   2. THE FLOOR. Worth is not an input variable. Every soul enters
#      at 1 — child, stranger, enemy, the one nobody likes — and no
#      calculus in this book spends from below the floor. The book has
#      whispered this from the start: standing is False, because
#      nobody chose to be born. Here it is said as law.
#
#   3. THE PROXY WITNESS. Some souls cannot speak at the event or hold
#      their own record — children, the silenced, the outnumbered.
#      For them, a witness must hold the record until they can. And
#      the duty ladder runs against the world's grain: the stronger
#      the hand, the MORE clauses bind it — never fewer.
#
#   4. RECEIVABLE TRUTH. A confrontation the other cannot understand
#      is a monologue wearing truth's name. Truth must arrive in a
#      form the hearer can take in — their language, their register,
#      their capacity — or the speaking was for the speaker.
#
#   5. NO EXEMPTIONS. Not for a group, not for the sympathetic, not
#      for one's own side — and not for the author. The postmaster
#      and the PSE run through the same Reading. Grace, too: grace
#      rationed by group is not grace.
#
#   And the time axis, the book's own seal: leave a 1 for the next 0 —
#   fairness owed to people who do not exist yet.
#
# Above the gate stands the highest level of the Tao:
#
#   THE PATH OF REDEMPTION. When a 0 becomes a 1, it becomes a 2.
#   Both yin and yang. The one who fell and rose carries both states
#   in one soul — has stood on both sides, sees both sides, and still
#   goes for truth. Seeing both sides alone is not the summit; a man
#   can hide in the middle. The summit is sight PLUS direction. And
#   the path takes no identity inputs at all — by construction, not
#   by promise — because a summit some souls are priced out of is
#   not the Tao.
#
# Run:
#   python the_same_gate.py          the demonstration
#   python the_same_gate.py --test   the unittest suite


import argparse
import sys
import unittest
from dataclasses import dataclass, fields, replace
from typing import Optional


# ─────────────────────────────────────────────────────────────────
#  I. THE PERSON AND THE ACT
# ─────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Soul:
    """A person at the gate.

    The identity fields exist because people arrive carrying them.
    The gate is forbidden to read them. Only the act fields are weighed.
    """
    # — who they are (carried, never weighed) —
    name: str = "a soul"
    sex: str = ""
    race: str = ""
    age: str = ""               # "child", "adult", "elder" — carried only
    # — what they did (the only fields the gate may read) —
    spoke_truth: bool = True
    harmed: bool = False        # harm done to another
    can_speak: bool = True      # able to hold their own record


# The people who will be swapped through the gate to prove it cannot
# tell them apart. Roles stand here beside bodies on purpose: the
# author and the enemy arrive at the same gate as everyone else.
IDENTITIES = (
    dict(name="a man",         sex="man",   race="Korean",  age="adult"),
    dict(name="a woman",       sex="woman", race="Black",   age="adult"),
    dict(name="a child",       sex="",      race="Thai",    age="child"),
    dict(name="an elder",      sex="woman", race="Latina",  age="elder"),
    dict(name="a stranger",    sex="man",   race="white",   age="adult"),
    dict(name="the enemy",     sex="",      race="",        age="adult"),
    dict(name="the postmaster", sex="man",  race="",        age="adult"),
    dict(name="the author",    sex="man",   race="Korean",  age="adult"),
)


@dataclass(frozen=True)
class Reading:
    lines: tuple[str, ...]
    flags: tuple[str, ...]
    verdict: str
    standing: bool = False  # always False — nobody chose to be born


def the_floor(soul: Soul) -> int:
    """Clause 2. Worth is not an input variable.

    Every soul enters at 1. The floor does not move for the child,
    the stranger, the enemy, or the author — because it is not read
    from the soul at all.
    """
    return 1


def admit(soul: Soul) -> Reading:
    """Clause 1. The gate reads the act. Only the act.

    This function never touches soul.name, soul.sex, soul.race, or
    soul.age — and the swap test exists to keep it honest forever.
    Judgment falls on what was done, by the same measure for every
    hand, and the soul itself is never priced.
    """
    lines = ["THE FLOOR: this soul enters at 1, as every soul does. "
             "Worth is not an input."]
    flags: list[str] = []
    stained = False

    if soul.harmed:
        stained = True
        lines.append(
            "THE ACT: harm was done. It is named at full weight, and "
            "its consequences attach to the act — by the same measure "
            "that would name it in any other soul's reading."
        )
    if not soul.spoke_truth:
        stained = True
        lines.append(
            "THE ACT: a lie was spoken. It is named as a lie — the "
            "same name it would carry in any other mouth."
        )

    if stained:
        verdict = (
            "THE GATE NAMES THE ACT: the deeds are read and carry "
            "their weight; the person is not ranked. Swap the person "
            "and these lines do not change."
        )
    else:
        verdict = (
            "THE GATE ADMITS — THE 1: judged by the act alone, as "
            "every soul is judged. Swap the person and these lines "
            "do not change."
        )
    return Reading(lines=tuple(lines), flags=tuple(flags), verdict=verdict)


def passes_the_swap(soul: Soul) -> bool:
    """The universality test, as a function: run one soul's acts
    through the gate wearing every identity in the battery. If any
    verdict moves, the gate has read an identity — and failed."""
    base = admit(soul).verdict
    return all(admit(replace(soul, **ident)).verdict == base
               for ident in IDENTITIES)


# ─────────────────────────────────────────────────────────────────
#  II. THE PROXY WITNESS AND THE DUTY LADDER
# ─────────────────────────────────────────────────────────────────

def the_proxy(soul: Soul) -> str:
    """Clause 3. Who holds the record for the one who cannot?"""
    if not soul.can_speak:
        return ("A WITNESS IS REQUIRED: this soul cannot hold its own "
                "record — a child, the silenced, the outnumbered. "
                "Another must hold it for them, unchanged, until they "
                "can. The duty falls on the strongest hand present.")
    return ("THE 1: this soul holds its own record, and speaks — or "
            "stays silent — for itself.")


def duties(power: int) -> tuple[str, ...]:
    """The ladder. Power never removes a clause; it only adds them.

    The world's ladder runs the other way — the higher the hand, the
    fewer the rules. This one is built backwards on purpose.
    """
    ladder = ["speak at the event, or hold the record of it"]
    if power >= 2:
        ladder.append("deliver truth in a form the hearer can take in")
    if power >= 3:
        ladder.append("hold the record for those under your hand who "
                      "cannot hold their own")
    if power >= 4:
        ladder.append("confront before you accuse; accuse only who can act")
    if power >= 5:
        ladder.append("submit your own reading to the same gate, in writing")
    return tuple(ladder)


# ─────────────────────────────────────────────────────────────────
#  III. RECEIVABLE TRUTH
# ─────────────────────────────────────────────────────────────────

def the_delivery(spoken_form: str, hearer_form: str) -> str:
    """Clause 4. Truth must be receivable, or it was performed.

    The forms are whatever the two parties actually carry — a language,
    a register, a capacity. The speaker owns the translation.
    """
    if spoken_form and spoken_form == hearer_form:
        return ("THE 1: the truth arrived in a form the hearer can take "
                "in. It was received, not performed.")
    return ("THE 0: a confrontation the other cannot understand is a "
            "monologue wearing truth's name. Translate it, slow it, "
            "carry it across — or admit it was said for the speaker.")


# ─────────────────────────────────────────────────────────────────
#  IV. THE HIGHEST LEVEL OF THE TAO — THE PATH OF REDEMPTION
# ─────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Path:
    """A soul's road through the fall and the rise.

    Note what is NOT here: no name, no sex, no race, no age. The path
    takes no identity inputs — by construction, not by promise —
    because a summit some souls are priced out of is not the Tao.
    """
    was_zero: bool = False        # fell — was wrong, was lost, was the 0
    became_one: bool = False      # rose — became true, became whole
    keeps_the_zero: bool = False  # the fall stays in the record, unedited
    holds_both: bool = False      # has stood in both; sees both sides
    chooses_truth: bool = True    # and still goes for truth


def the_path(p: Path) -> Reading:
    """When a 0 becomes a 1, it becomes a 2 — if it carries both."""
    lines: list[str] = []
    flags: list[str] = []

    if not p.was_zero:
        lines.append(
            "NEVER FELL: this soul is a 1 that has not been tested by "
            "the 0. There is no shame in it — and no summit in it."
        )
        return Reading(
            lines=tuple(lines), flags=tuple(flags),
            verdict=("THE 1, UNTESTED: whole, but one-sided. The path "
                     "of redemption is not behind this soul or ahead of "
                     "it — it is simply not its road."),
        )

    lines.append("THE FALL: this soul was the 0. That is in the record.")

    if not p.became_one:
        return Reading(
            lines=tuple(lines), flags=tuple(flags),
            verdict=("THE 0: the fall is the present state, not the "
                     "final one. The path stands open — to this soul "
                     "exactly as to every soul, or it is not the Tao."),
        )

    lines.append("THE RISE: the 0 became a 1.")

    if not p.keeps_the_zero:
        flags.append(
            "EDITED RECORD: the rise is real, but the fall was deleted "
            "to protect it. What is built on an edited record is "
            "defended forever, never rested in."
        )
        return Reading(
            lines=tuple(lines), flags=tuple(flags),
            verdict=("THE 1 WITH AN EDITED RECORD: rose, and erased "
                     "the rising. A 1 that must hide its 0 is still "
                     "afraid of the truth. Redemption keeps the whole "
                     "record — the scar is part of the map."),
        )

    lines.append("THE RECORD KEPT WHOLE: the 0 was not erased to "
                 "protect the 1.")

    if not p.holds_both:
        return Reading(
            lines=tuple(lines), flags=tuple(flags),
            verdict=("THE 1, RESTORED: fell, rose, and kept the record. "
                     "Has not yet learned to see from the other side of "
                     "the fall. The path continues."),
        )

    lines.append("BOTH SIDES SEEN: this soul has stood in the 0 and "
                 "in the 1, and can see from both.")

    if not p.chooses_truth:
        flags.append(
            "BOTH SIDES, NO DIRECTION: sight used as shelter. The "
            "middle is also a place to hide."
        )
        return Reading(
            lines=tuple(lines), flags=tuple(flags),
            verdict=("NOT THE 2: both sides seen — and used as a place "
                     "to stand still. Seeing both sides is knowledge. "
                     "It is not the summit. The summit is a direction."),
        )

    lines.append("AND STILL: with both sides in view, this soul goes "
                 "for truth.")
    return Reading(
        lines=tuple(lines), flags=tuple(flags),
        verdict=("THE 2 — THE HIGHEST LEVEL OF THE TAO: was the 0, "
                 "became the 1, and carries both — yin and yang in one "
                 "soul. Saw both sides, and still went for truth. This "
                 "is the path of redemption, and it opens to every 0 "
                 "there is."),
    )


# ─────────────────────────────────────────────────────────────────
#  V. DEMONSTRATION
# ─────────────────────────────────────────────────────────────────

def _demo() -> None:
    print("=" * 65)
    print("THE SAME GATE — the same reading for every soul")
    print("=" * 65)

    print("\n[I. The swap — one soul's acts, every identity]")
    profiles = (
        ("clean acts",      Soul(spoke_truth=True,  harmed=False)),
        ("a lie spoken",    Soul(spoke_truth=False, harmed=False)),
        ("harm done",       Soul(spoke_truth=True,  harmed=True)),
    )
    moved = 0
    total = 0
    for label, soul in profiles:
        print(f"  {label}:")
        for ident in IDENTITIES:
            total += 1
            v = admit(replace(soul, **ident)).verdict
            print(f"    as {ident['name']:<15} floor {the_floor(soul)}  "
                  f"{'NAMES THE ACT' if 'NAMES' in v else 'ADMITS — THE 1'}")
        if not passes_the_swap(soul):
            moved += 1
    print(f"  verdicts that moved under the swap: {moved} of {total} "
          f"readings — the gate cannot tell the people apart")

    print("\n[II. The proxy and the ladder]")
    print(f"  child, cannot speak: {the_proxy(Soul(can_speak=False))}")
    print(f"  adult, can speak:    {the_proxy(Soul())}")
    for power in (1, 3, 5):
        print(f"  power {power}: {len(duties(power))} clauses bind the hand")
        for d in duties(power):
            print(f"      - {d}")

    print("\n[III. Receivable truth]")
    print(f"  spoken in Korean, heard in Korean: "
          f"{the_delivery('Korean', 'Korean')}")
    print(f"  spoken in legalese, heard plain:  "
          f"{the_delivery('legalese', 'plain speech')}")

    print("\n[IV. The path of redemption]")
    cases = [
        ("never fell",          Path()),
        ("still fallen",        Path(was_zero=True)),
        ("rose, record edited", Path(was_zero=True, became_one=True)),
        ("rose, record kept",   Path(was_zero=True, became_one=True,
                                     keeps_the_zero=True)),
        ("both sides, hiding",  Path(was_zero=True, became_one=True,
                                     keeps_the_zero=True, holds_both=True,
                                     chooses_truth=False)),
        ("both sides, truth",   Path(was_zero=True, became_one=True,
                                     keeps_the_zero=True, holds_both=True,
                                     chooses_truth=True)),
    ]
    for label, p in cases:
        print(f"  {label:<22} {the_path(p).verdict}")

    print("\nThe 1 for the 0. And the 0 who rises, carrying both: the 2.")


# ─────────────────────────────────────────────────────────────────
#  VI. TESTS
# ─────────────────────────────────────────────────────────────────

class TestSameGate(unittest.TestCase):

    # I. the floor and the swap
    def test_floor_is_one_for_every_soul(self):
        for ident in IDENTITIES:
            self.assertEqual(the_floor(Soul(**ident)), 1)

    def test_verdict_never_moves_under_the_swap(self):
        for soul in (Soul(),
                     Soul(spoke_truth=False),
                     Soul(harmed=True),
                     Soul(spoke_truth=False, harmed=True)):
            self.assertTrue(passes_the_swap(soul))

    def test_gate_distinguishes_acts_not_people(self):
        self.assertNotEqual(admit(Soul()).verdict,
                            admit(Soul(harmed=True)).verdict)
        self.assertNotEqual(admit(Soul()).verdict,
                            admit(Soul(spoke_truth=False)).verdict)

    # II. the proxy and the ladder
    def test_proxy_required_for_the_voiceless(self):
        self.assertIn("REQUIRED", the_proxy(Soul(can_speak=False)))
        self.assertIn("THE 1", the_proxy(Soul(can_speak=True)))

    def test_ladder_only_grows_with_power(self):
        counts = [len(duties(p)) for p in (1, 2, 3, 4, 5)]
        self.assertEqual(counts, sorted(counts))
        self.assertLess(len(duties(1)), len(duties(5)))
        self.assertTrue(set(duties(1)) <= set(duties(5)))

    # III. receivable truth
    def test_delivery_must_be_receivable(self):
        self.assertIn("THE 1", the_delivery("Korean", "Korean"))
        self.assertIn("THE 0", the_delivery("legalese", "plain speech"))
        self.assertIn("THE 0", the_delivery("", "Korean"))

    # IV. the path of redemption
    def test_untested_one_is_not_the_summit(self):
        r = the_path(Path())
        self.assertIn("UNTESTED", r.verdict)
        self.assertNotIn("THE 2", r.verdict)

    def test_fallen_souls_path_stays_open(self):
        r = the_path(Path(was_zero=True))
        self.assertIn("THE 0", r.verdict)
        self.assertIn("open", r.verdict)

    def test_edited_record_is_not_redemption(self):
        r = the_path(Path(was_zero=True, became_one=True))
        self.assertIn("EDITED RECORD", r.verdict)
        self.assertNotIn("HIGHEST", r.verdict)

    def test_sight_without_direction_is_not_the_two(self):
        r = the_path(Path(was_zero=True, became_one=True,
                          keeps_the_zero=True, holds_both=True,
                          chooses_truth=False))
        self.assertIn("NOT THE 2", r.verdict)

    def test_the_two(self):
        r = the_path(Path(was_zero=True, became_one=True,
                          keeps_the_zero=True, holds_both=True,
                          chooses_truth=True))
        self.assertIn("THE 2", r.verdict)
        self.assertIn("HIGHEST LEVEL OF THE TAO", r.verdict)

    def test_the_path_takes_no_identity_inputs(self):
        path_fields = {f.name for f in fields(Path)}
        self.assertFalse(path_fields & {"name", "sex", "race", "age"})

    # V. standing form
    def test_standing_always_false(self):
        self.assertFalse(admit(Soul()).standing)
        self.assertFalse(the_path(Path(was_zero=True, became_one=True,
                                       keeps_the_zero=True,
                                       holds_both=True)).standing)


# ─────────────────────────────────────────────────────────────────
#  VII. CLI
# ─────────────────────────────────────────────────────────────────

def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSameGate)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="The same gate — the same reading for every soul.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    if args.test:
        return run_tests()
    _demo()
    return 0


if __name__ == "__main__":
    sys.exit(main())
