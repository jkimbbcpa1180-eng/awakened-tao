# the_humble_path.py
# Copyright (c) Humanity — released under CC0.
# Type: philosophical proposal; computational demonstration
#
# THE PATH OF THE HUMBLE — what happens AFTER the event, for
# awakened_light / Awaken Tao. John's axiom, stated October 23, 2026:
#
#   "The path of the humble: you must humble yourself down and take
#    a few days after the event to breathe and reassess the situation
#    and fix the house internally. If the house still isn't fixed
#    after internal, you must find another way. But until then, fix
#    it in house — then seek justice for truth."
#
# Encoded, the path is a SEQUENCE, and the order is the doctrine:
#
#   0. THE RECORD (the event itself) — truth is recorded in its
#      moment. That is holy_sword's ground, and it is NOT delayed by
#      anything here: the sword governs the speaking, this path
#      governs the response. One preserves truth; the other governs
#      power. They do not conflict.
#   1. HUMBLE YOURSELF DOWN — first, before any fixing: the mirror.
#      Your own part in the event, examined honestly. You humble
#      YOURSELF — nobody humbles you. What was done to you is their
#      act; what you do with the days after is yours.
#   2. THE BREATH — a few days. Not delay: delay avoids the event;
#      the breath returns to it with cooler eyes. A response launched
#      inside the breath is the wound answering, not the soul.
#   3. REASSESS — after the breath, read the event again. It may read
#      differently. Your own part may be larger than the heat said.
#      The reading you act on is the reassessed one, or it is the
#      heat's reading wearing your name.
#   4. FIX IT IN HOUSE — the internal door first, always: the house
#      is asked to fix itself, in order and in full, before any other
#      door is touched.
#   5. THE NEXT DOOR IS EARNED — if the house still is not fixed
#      after the internal attempt, find another way. Seeking justice
#      beyond the house then is not escalation and not revenge
#      (holy_sword): it is sequence. The order is what licenses it.
#
# And the guard-rail on the whole path: humility is not surrender.
# The self steps down; the truth does not. A "humility" that gives
# up the truth to keep the peace is surrender wearing humility's
# clothes, and the path collapses there as surely as at revenge.
#
# Flagged, as always: BREATH_DAYS = 3 renders John's "a few days" as
# a number. It is a floor for the response, not a gag on the record.
# His call, as every flagged call is.
#
# Run:
#   python the_humble_path.py          the demonstration
#   python the_humble_path.py --test   the unittest suite


import argparse
import sys
import unittest
from dataclasses import dataclass
from typing import Optional

# "A few days," as a number. The breath's floor, for the response.
BREATH_DAYS = 3


# ─────────────────────────────────────────────────────────────────
#  I. THE BREATH — the pause is not delay
# ─────────────────────────────────────────────────────────────────

def the_pause(days_since_event: int) -> str:
    """The breath, as a word: taken, or not yet."""
    if days_since_event >= BREATH_DAYS:
        return ("THE 1: the breath is taken. What is decided now is "
                "decided by the soul, not by the wound.")
    return ("THE 0: still inside the breath. Delay avoids the event; "
            "the breath returns to it — but it has not returned yet. "
            "Anything launched now is the heat speaking.")


# ─────────────────────────────────────────────────────────────────
#  II. THE AFTERMATH — the state of the response
# ─────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class Aftermath:
    """Where the response stands, after an event.

    record_made is the sword's clause, carried here only to be
    flagged: this path can repair a response; it cannot repair a
    missing record.
    """
    days_since_event: int = 0
    record_made: bool = True        # truth recorded in its moment
    humbled_self: bool = False      # own part examined in the mirror
    reassessed: bool = False        # the event re-read with cooler eyes
    internal_attempt: bool = False  # the house was asked to fix itself
    house_fixed: bool = False       # ...and it did
    went_external: bool = False     # justice sought beyond the house
    gave_up_truth: bool = False     # "peace" bought by shrinking the truth


@dataclass(frozen=True)
class Reading:
    lines: tuple[str, ...]
    flags: tuple[str, ...]
    verdict: str
    standing: bool = False  # always False — nobody chose to be born


# ─────────────────────────────────────────────────────────────────
#  III. THE WALK — the sequence is the doctrine
# ─────────────────────────────────────────────────────────────────

def walk(a: Aftermath) -> Reading:
    """Walk the aftermath down the path of the humble, in order."""

    # The guard-rail first: humility that surrenders the truth is
    # not humility at all.
    if a.gave_up_truth:
        return Reading(
            lines=("SURRENDER IN HUMILITY'S CLOTHES: the truth was "
                   "shrunk to keep the peace. The self is meant to "
                   "step down on this path — never the truth.",),
            flags=("NOT HUMILITY: peace bought with the truth is a "
                   "price, and the truth was the currency.",),
            verdict=("THE PATH COLLAPSES: surrender wearing humility. "
                     "The stone stays on the ground."),
        )

    # A door skipped: justice outside a house never asked to fix
    # itself. The order is what licenses the seeking; without the
    # order, it is the megaphone's road (holy_sword).
    if a.went_external and not a.internal_attempt:
        return Reading(
            lines=("THE DOOR WAS SKIPPED: justice was sought beyond "
                   "the house before the house was ever asked to fix "
                   "itself. However true the charge, the sequence "
                   "was not honored — and the sequence is the license.",),
            flags=("ORDER: fix it in house first. Until then, the "
                   "outside door is not earned.",),
            verdict=("THE PATH COLLAPSES: the internal door was "
                     "skipped. The stone stays on the ground."),
        )

    # Inside the breath, any launch is the wound answering.
    if a.days_since_event < BREATH_DAYS and (a.internal_attempt
                                             or a.went_external):
        return Reading(
            lines=("THE WOUND ANSWERED: the response was launched "
                   f"inside the breath — day {a.days_since_event} of "
                   f"{BREATH_DAYS}. It may even be aimed at the right "
                   "fix; it was still fired by the heat, not chosen "
                   "by the soul.",),
            flags=("TOO SOON: the record stands at the event; the "
                   "response waits for the breath.",),
            verdict=("THE PATH COLLAPSES: too soon. The stone stays "
                     "on the ground."),
        )

    lines: list[str] = []
    flags: list[str] = []

    if not a.record_made:
        flags.append(
            "UNRECORDED MOMENT: the event passed without a record. "
            "This path repairs the response; it cannot repair the "
            "record (holy_sword). Flagged, and carried."
        )

    if a.record_made:
        lines.append(
            "THE RECORD STANDS: truth was kept at the event. Nothing "
            "on this path asks it to shrink."
        )

    partial = False
    if a.humbled_self:
        lines.append(
            "HUMBLED DOWN: your own part was examined before any "
            "fixing was demanded. You lowered yourself — nobody "
            "lowered you."
        )
    else:
        partial = True
        lines.append(
            "THE MIRROR, SKIPPED: the fixing began before the self "
            "was examined. A demand that has not passed the mirror "
            "is accusation wearing the path's clothes."
        )
        flags.append("MIRROR: humble yourself down FIRST.")

    if a.reassessed:
        lines.append(
            "REASSESSED: the event was re-read after the breath, and "
            "the reading acted on is the cooled one."
        )
    elif a.internal_attempt or a.went_external:
        partial = True
        lines.append(
            "NOT REASSESSED: the action runs on the heat's first "
            "reading of the event."
        )
        flags.append("REASSESS: breathe first, then read it again.")

    # The doors, in order.
    if not a.internal_attempt and not a.went_external:
        lines.append(
            "THE HOUSE NOT YET ASKED: the breath is the agenda so "
            "far. The next step is not outside — it is in house."
        )
        verdict = (
            "THE PATH WAITS: the sequence is intact and unfinished. "
            "Fix it in house; then, if the house will not, seek "
            "justice for truth."
        )
        if partial:
            verdict = ("THE PATH IS PARTIAL: the sequence holds, but "
                       "a step before the door was skipped. Look at "
                       "the missing lines.")
        return Reading(lines=tuple(lines), flags=tuple(flags),
                       verdict=verdict)

    if a.internal_attempt and a.house_fixed:
        lines.append(
            "FIXED IN HOUSE: the house was asked, and the house "
            "repaired itself. Justice for truth began at home — and "
            "here, it could end at home."
        )
        if a.went_external:
            flags.append(
                "IN ORDER: the seeking beyond the house came after "
                "the internal door — sequence honored throughout."
            )
        verdict = ("THE PATH HOLDS — THE HOUSE HELD: humbled, "
                   "breathed, reassessed, repaired in house. The "
                   "stone stays on the ground.")
        if partial:
            verdict = ("THE PATH IS PARTIAL: the house held, but a "
                       "step was skipped on the way. Look at the "
                       "missing lines.")
        return Reading(lines=tuple(lines), flags=tuple(flags),
                       verdict=verdict)

    if a.internal_attempt and not a.house_fixed and not a.went_external:
        lines.append(
            "THE HOUSE DID NOT FIX ITSELF: the internal door was "
            "walked in full, in order, and the house declined. That "
            "is now a fact of the record, not a grievance of the heat."
        )
        verdict = (
            "THE PATH HOLDS — THE NEXT DOOR IS EARNED: find another "
            "way. Seeking justice beyond this house now is not "
            "escalation; it is sequence."
        )
        if partial:
            verdict = ("THE PATH IS PARTIAL: the next door approaches, "
                       "but a step was skipped. Look at the missing "
                       "lines before you knock.")
        return Reading(lines=tuple(lines), flags=tuple(flags),
                       verdict=verdict)

    # Internal walked, house unrepentant, justice sought beyond it.
    lines.append(
        "JUSTICE, IN ORDER: the house was humbled before, breathed "
        "over, reassessed, and asked — and would not. The seeking "
        "beyond it carries the whole sequence behind it."
    )
    verdict = (
        "THE PATH HOLDS — JUSTICE IN ORDER: fix it in house first; "
        "then seek justice for truth. Both clauses were kept."
    )
    if partial:
        verdict = ("THE PATH IS PARTIAL: justice in order, but a step "
                   "was skipped. Look at the missing lines.")
    return Reading(lines=tuple(lines), flags=tuple(flags),
                   verdict=verdict)


# ─────────────────────────────────────────────────────────────────
#  IV. DEMONSTRATION
# ─────────────────────────────────────────────────────────────────

def _demo() -> None:
    print("=" * 65)
    print("THE PATH OF THE HUMBLE — breathe, reassess, fix it in house")
    print("=" * 65)

    print("\n[I. The breath]")
    for d in (0, 1, 3, 7):
        print(f"  day {d}: {the_pause(d)}")

    print("\n[II. A reading — the full sequence, the house held]")
    r = walk(Aftermath(days_since_event=5, humbled_self=True,
                       reassessed=True, internal_attempt=True,
                       house_fixed=True))
    for line in r.lines:
        print(f"  {line}")
    print(f"\n  {r.verdict}")
    print(f"  standing: {r.standing}  (nobody chose to be born)")

    print("\n[III. The other roads]")
    cases = [
        ("answered on day one", Aftermath(days_since_event=1,
                                          internal_attempt=True)),
        ("straight outside",    Aftermath(days_since_event=10,
                                          humbled_self=True,
                                          reassessed=True,
                                          went_external=True)),
        ("peace at any price",  Aftermath(days_since_event=10,
                                          humbled_self=True,
                                          gave_up_truth=True)),
        ("house would not",     Aftermath(days_since_event=6,
                                          humbled_self=True,
                                          reassessed=True,
                                          internal_attempt=True)),
        ("justice, in order",   Aftermath(days_since_event=9,
                                          humbled_self=True,
                                          reassessed=True,
                                          internal_attempt=True,
                                          went_external=True)),
    ]
    for label, a in cases:
        print(f"  {label:<22} {walk(a).verdict}")

    print("\nHumble yourself down. The truth does not step down — "
          "only the self does.")


# ─────────────────────────────────────────────────────────────────
#  V. TESTS
# ─────────────────────────────────────────────────────────────────

class TestHumblePath(unittest.TestCase):

    # I. the breath
    def test_breath_words(self):
        self.assertIn("THE 0", the_pause(BREATH_DAYS - 1))
        self.assertIn("THE 1", the_pause(BREATH_DAYS))
        self.assertIn("THE 1", the_pause(30))

    # II. the collapses
    def test_too_soon_collapses(self):
        r = walk(Aftermath(days_since_event=1, internal_attempt=True))
        self.assertIn("COLLAPSES", r.verdict)
        self.assertIn("WOUND ANSWERED", " ".join(r.lines))

    def test_external_first_collapses(self):
        r = walk(Aftermath(days_since_event=10, humbled_self=True,
                           reassessed=True, went_external=True))
        self.assertIn("COLLAPSES", r.verdict)
        self.assertIn("SKIPPED", " ".join(r.lines))

    def test_surrender_is_not_humility(self):
        r = walk(Aftermath(days_since_event=10, humbled_self=True,
                           reassessed=True, internal_attempt=True,
                           house_fixed=True, gave_up_truth=True))
        self.assertIn("COLLAPSES", r.verdict)

    # III. the holds
    def test_house_held(self):
        r = walk(Aftermath(days_since_event=5, humbled_self=True,
                           reassessed=True, internal_attempt=True,
                           house_fixed=True))
        self.assertIn("PATH HOLDS", r.verdict)
        self.assertIn("HOUSE HELD", r.verdict)

    def test_next_door_is_earned(self):
        r = walk(Aftermath(days_since_event=6, humbled_self=True,
                           reassessed=True, internal_attempt=True))
        self.assertIn("PATH HOLDS", r.verdict)
        self.assertIn("NEXT DOOR IS EARNED", r.verdict)

    def test_justice_in_order(self):
        r = walk(Aftermath(days_since_event=9, humbled_self=True,
                           reassessed=True, internal_attempt=True,
                           went_external=True))
        self.assertIn("PATH HOLDS", r.verdict)
        self.assertIn("JUSTICE IN ORDER", r.verdict)

    def test_path_waits_before_the_door(self):
        r = walk(Aftermath(days_since_event=4, humbled_self=True,
                           reassessed=True))
        self.assertIn("PATH WAITS", r.verdict)

    # IV. the partials and the flags
    def test_mirror_skipped_is_partial(self):
        r = walk(Aftermath(days_since_event=5, reassessed=True,
                           internal_attempt=True, house_fixed=True))
        self.assertIn("PARTIAL", r.verdict)

    def test_unreassessed_action_is_partial(self):
        r = walk(Aftermath(days_since_event=5, humbled_self=True,
                           internal_attempt=True, house_fixed=True))
        self.assertIn("PARTIAL", r.verdict)

    def test_unrecorded_moment_is_flagged_not_fatal(self):
        r = walk(Aftermath(days_since_event=5, humbled_self=True,
                           reassessed=True, internal_attempt=True,
                           house_fixed=True, record_made=False))
        self.assertIn("PATH HOLDS", r.verdict)
        self.assertIn("UNRECORDED", " ".join(r.flags))

    # V. standing form
    def test_standing_always_false(self):
        self.assertFalse(walk(Aftermath()).standing)
        self.assertFalse(walk(Aftermath(gave_up_truth=True)).standing)


# ─────────────────────────────────────────────────────────────────
#  VI. CLI
# ─────────────────────────────────────────────────────────────────

def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestHumblePath)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="The path of the humble — fix it in house, "
                    "then seek justice for truth.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    if args.test:
        return run_tests()
    _demo()
    return 0


if __name__ == "__main__":
    sys.exit(main())
