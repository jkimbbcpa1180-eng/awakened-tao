#!/usr/bin/env python3
"""THE HOLY SWORD OF TRUTH — a module for Awaken Tao.

Type: philosophical proposal; computational demonstration

The passage, encoded and reflected through the framework.

The passage makes three claims:
  1. Sometimes you need to use the holy sword of truth. It is not
     attacking because truth hurts. Truth has no bounds.
  2. Truth must be said during the event. You cannot hold truth and
     wait years to use it as revenge.
  3. If you never confronted the other party with the truth and waited
     for the opportunity, that is not truth. That is revenge.

  One exception is stated with the claims: unless it was a written
  contract.

The framework agrees, and sharpens its edges honestly:

  - Claim 1 refines truth_speed.py's harm gate. There, a truth that
    wounds collapsed the passage. Here the distinction is drawn where
    energy.py always drew it: the act is neutral, the source is the
    energy. Hurt that comes from a lie collapsing is not an attack;
    the same words swung in order to wound are the blade wearing the
    light's name (creation.py). Outcome-harm does not collapse the
    passage. Purpose-harm does.

  - Claim 1 also gains its observable test. Aim can be claimed;
    audience can be checked. Truth spoken to the one who can act on
    it — the named one, the authority — is a sword. Truth announced
    to whoever will enjoy it is wound-delivery, whatever its aim
    claims to be. The megaphone collapses the passage on its own.

  - Claim 2 has the same physics anchor truth_speed found: light
    cannot be stored. What is emitted, travels. What is "saved" and
    discharged later is not illumination, it is shock. A truth held
    past its moment does not keep its nature; it ferments. The record
    is the exception that proves it: a truth written down at the event
    was spoken at the event — to a witness that does not sleep.

  - A pattern is not a moment. Wrongs that run for months have no
    single "during"; a pattern's event stays open while the pattern
    is live, and truth spoken while it lives is spoken during the
    event. When the pattern dies, the ordinary clock starts.

  - The written contract is the record's strongest form: the one truth
    built to outlive its moment. Fixed in writing and faced at the
    signing, it was spoken at its event and confronted by the
    signature; both parties agreed in advance to its timing, so time
    cannot ferment it, and invoking it years later is neither storage
    nor ambush. The exception covers time, not aim: a contract
    enforced in order to wound is still the blade.

Judgment calls, flagged rather than hidden:

  - Late speech that finally confronts the other party is PARTIAL,
    not revenge: the confrontation is what separates confession from
    ambush. The moment cannot be recovered, but the act stays truth.
  - A deadline set by the wrong itself (an interview date, a hearing)
    is the event's own clock, not an opportune moment. Timing imposed
    by the event is not timing chosen for advantage.
  - Where no true channel existed at the event — no authority, no
    safe ear — speech at the first true opening is PARTIAL, not
    revenge: the delay belonged to the channel, not the speaker. The
    author may harden this to LATE; the flag stays either way.

Every reading also carries the mirror, the doctrine's other half:
the law binds the ear as well as the tongue. When true words are
swung at you, it is not an attack on you either (two_cheeks).

Run:
    python3 holy_sword.py
    python3 holy_sword.py --test
"""

from __future__ import annotations

import argparse
import sys
import unittest
from dataclasses import dataclass
from typing import Optional


# ----------------------------------------------------------------------
# I. The wound: hurt is not the test — the source is
# ----------------------------------------------------------------------

def the_wound(source: str) -> str:
    """Where the hurt comes from decides what the act was."""
    s = source.strip().lower()
    if s in ("truth", "revelation", "exposure", "the lie collapsing"):
        return ("THE 1: the hurt is the lie collapsing, not the swing. "
                "Truth has no bounds; the bound is on the wielder "
                "(energy.py: the act is neutral, the source is the energy).")
    if s in ("malice", "wound", "hurt them", "revenge"):
        return ("THE 0: swung in order to wound, it is the blade wearing "
                "the light's name (creation.py). The words may be accurate. "
                "The act is false.")
    if s in ("silence", "nothing", "buried"):
        return ("THE 0: unspoken truth protects the lie (fairness.py: good "
                "men did nothing). A sword never drawn defends whoever "
                "holds the field.")
    return ("UNCONFIRMED: truth, malice, or silence — name the source "
            "before you answer.")


def the_audience(aud: str) -> str:
    """Who hears it: the aim, made visible — the part a witness can check."""
    a = aud.strip().lower()
    if a in ("proper", "authority", "the named one", "the one who can act"):
        return ("THE 1: spoken to the one who can act on it. The audience "
                "is the aim made visible, and this aim is repair.")
    if a in ("crowd", "broadcast", "public", "everyone", "the megaphone"):
        return ("THE 0: announced to whoever will enjoy it. That is not "
                "witness; it is wound-delivery with accurate words — the "
                "megaphone is the blade's handle.")
    if a in ("no one", "silence", "nobody"):
        return ("THE 0: spoken to no one, truth defends the lie by "
                "absence (fairness.py).")
    return ("UNCONFIRMED: proper, crowd, or no one — name the audience "
            "before you answer.")


# ----------------------------------------------------------------------
# II. The clock: light cannot be stored
# ----------------------------------------------------------------------

def held_light(form: str) -> str:
    """What form the truth was kept in decides what it still is."""
    f = form.strip().lower()
    if f in ("spoken", "moment", "at the event", "now"):
        return ("THE 1: spoken in its moment, truth is a witness. It "
                "arrives when it is emitted, like light.")
    if f in ("record", "written", "documented", "the record"):
        return ("THE 1: written at the event, truth is spoken at the "
                "event — to a witness that does not sleep. The record is "
                "not storage; it is testimony with a timestamp.")
    if f in ("opportunity", "stored", "saved", "later", "leverage"):
        return ("THE 0: light cannot be stored. What discharges after "
                "storage is shock, not illumination. Truth held for the "
                "opportunity is REVENGE wearing accurate words.")
    if f in ("never", "forever", "buried"):
        return ("THE 0: held forever, truth dies a witness and the lie "
                "keeps the field (fairness.py).")
    return ("UNCONFIRMED: spoken, recorded, stored, or buried — name the "
            "form before you answer.")


# ----------------------------------------------------------------------
# III. The gate: the speaking, read whole
# ----------------------------------------------------------------------

@dataclass(frozen=True)
class Speaking:
    accurate: bool = True                 # the content is true
    will_hurt: bool = False               # it will hurt — which is not the test
    spoken_at_event: bool = True          # voiced, or written into the record, when it happened
    confronted_other: bool = True         # the one it names has faced it
    deployed_for_advantage: bool = False  # saved for the opportune moment
    aims_to_wound: bool = False           # swung at the person, not the lie
    written_contract: bool = False        # fixed in writing, faced at the signing
    audience: str = "proper"              # "proper" (who can act) or "crowd"
    is_pattern: bool = False              # the wrong is a pattern, not a moment
    pattern_live: bool = False            # the pattern is still running
    first_true_opening: bool = False      # no true channel existed until now


@dataclass(frozen=True)
class Reading:
    lines: tuple[str, ...]
    flags: tuple[str, ...]
    verdict: str
    standing: bool = False  # always False — nobody chose to be born
    mirror: str = ("THE MIRROR: the law binds the ear as well as the "
                   "tongue. When true words are swung at you, it is not "
                   "an attack on you either (two_cheeks).")


def wield(s: Speaking) -> Reading:
    # Accuracy is checked before anything else: a falsehood is not a
    # dull sword, it is no sword.
    if not s.accurate:
        return Reading(
            lines=("NO LIGHT: the content is not true. Accuracy is the "
                   "whole claim; without it the sword is a blade and "
                   "nothing more.",),
            flags=("SLANDER: a falsehood swung as truth is the one attack "
                   "this module names without qualification.",),
            verdict=("THE PASSAGE COLLAPSES: not truth at all. The stone "
                     "stays on the ground."),
        )

    # The source is checked second (energy.py): the aim is the act.
    if s.aims_to_wound:
        return Reading(
            lines=("THE BLADE: the words may be accurate and the act is "
                   "still false — swung at the person, not the lie "
                   "(creation.py).",),
            flags=("PURPOSE-HARM: outcome-hurt does not collapse a truth; "
                   "purpose-hurt does. The aim is the act.",),
            verdict=("THE PASSAGE COLLAPSES: the blade wearing the "
                     "light's name. The stone stays on the ground."),
        )

    # The audience is checked next: it is the aim made visible, the
    # one part of the source a witness can verify.
    if s.audience.strip().lower() in ("crowd", "broadcast", "public",
                                       "everyone", "the megaphone"):
        return Reading(
            lines=("THE MEGAPHONE: announced to the crowd instead of "
                   "spoken to the one who can act. The audience is the "
                   "aim made visible — and this aim is the wound, "
                   "delivered to whoever will enjoy it.",),
            flags=("AUDIENCE: aim can be claimed; audience can be "
                   "checked. When the two disagree, believe the "
                   "audience.",),
            verdict=("THE PASSAGE COLLAPSES: broadcast is not witness. "
                     "The stone stays on the ground."),
        )

    # The written contract: fixed in writing and faced at the signing,
    # it was spoken at its event and confronted by the signature. Its
    # moment does not expire.
    timely = (s.spoken_at_event or s.written_contract
              or (s.is_pattern and s.pattern_live))
    faced = s.confronted_other or s.written_contract

    # Timing is checked third: truth held for the opportunity, or held
    # past its moment and sprung on someone who never faced it, is
    # revenge — whatever its content. A written contract is exempt:
    # its timing was agreed by both parties in advance.
    if (s.deployed_for_advantage and not s.written_contract) \
            or (not timely and not faced and not s.first_true_opening):
        return Reading(
            lines=("STOCKPILED: kept past its moment and sprung, or saved "
                   "for the moment of maximum effect. Light cannot be "
                   "stored; what discharges is shock.",),
            flags=("REVENGE: the content may be true and the act is still "
                   "revenge. Truth is a witness, not a debt to be "
                   "collected.",),
            verdict=("THE PASSAGE COLLAPSES: this is not truth-telling, "
                     "it is REVENGE. The stone stays on the ground."),
        )

    lines: list[str] = ["SPOKEN TRUE: the content holds."]
    flags: list[str] = []

    if s.will_hurt:
        lines.append(
            "IT HURTS: the hurt is the lie collapsing, not the swing. "
            "Truth has no bounds; the bound is on the wielder."
        )

    lines.append(
        "THE RIGHT EAR: spoken to the one who can act on it — not "
        "announced to whoever would enjoy it."
    )

    if s.written_contract:
        lines.append(
            "THE WRITTEN WORD: fixed in writing and faced at the "
            "signing, it was spoken at its event — and its event does "
            "not expire. To invoke it years later is not storage and "
            "not ambush; the signature was the confrontation."
        )
    elif s.spoken_at_event:
        lines.append(
            "IN ITS MOMENT: said when it happened — voiced, or written "
            "into the record while the event was still warm."
        )
    elif s.is_pattern and s.pattern_live:
        lines.append(
            "THE PATTERN: a pattern has no single moment. Its event "
            "stays open while it lives, and this was spoken while it "
            "lived — during the event."
        )
    elif s.first_true_opening:
        lines.append(
            "THE FIRST TRUE OPENING: at the event there was no true "
            "channel — no authority, no safe ear. This was spoken at "
            "the first opening that existed."
        )
        flags.append(
            "FIRST TRUE OPENING: the delay belonged to the channel, "
            "not the speaker. Judged PARTIAL, not revenge — a flagged "
            "call; the author may harden it to LATE."
        )
    else:
        lines.append(
            "LATE: the moment has passed. Confrontation keeps it truth; "
            "it cannot make it timely."
        )
        flags.append(
            "LATE: late light still lights, but the event it belonged to "
            "is gone. Name the cost; do not pretend it is the same act."
        )

    if s.confronted_other:
        lines.append(
            "CONFRONTED: the one it names has faced it, and had the "
            "chance to answer. Nothing here is an ambush."
        )
    elif not s.written_contract:
        lines.append(
            "UNCONFRONTED: spoken in its moment, but not to the one it "
            "names. Witness, yes; confrontation, no."
        )
        flags.append(
            "UNCONFRONTED: truth about a person that never reaches the "
            "person is one clause short of the sword."
        )

    if timely and faced:
        verdict = (
            "THE PASSAGE PASSES — THE SWORD OF LIGHT: true, timely, "
            "faced, and swung at the lie and not the person. If it "
            "hurts, it hurts because it is true. The stone stays on "
            "the ground."
        )
    else:
        verdict = (
            "THE PASSAGE IS PARTIAL: a load-bearing clause is missing. "
            "Look at the missing lines. The stone stays on the ground "
            "either way."
        )

    return Reading(tuple(lines), tuple(flags), verdict)


# ----------------------------------------------------------------------
# IV. Demo
# ----------------------------------------------------------------------

def demonstrate() -> int:
    print("=" * 72)
    print("THE HOLY SWORD OF TRUTH")
    print("=" * 72)

    print("\n[I. The wound — where does the hurt come from?]")
    for src in ("truth", "malice", "silence", "???"):
        print(f"  {src!r}: {the_wound(src)}")

    print("\n[Ib. The audience — the aim, made visible]")
    for aud in ("proper", "crowd", "no one", "???"):
        print(f"  {aud!r}: {the_audience(aud)}")

    print("\n[II. The clock — what form was the truth kept in?]")
    for form in ("spoken", "record", "opportunity", "never", "???"):
        print(f"  {form!r}: {held_light(form)}")

    print("\n[III. The reading — the sword, drawn clean]")
    r = wield(Speaking(will_hurt=True))
    for line in r.lines:
        print(f"\n  • {line}")
    print("\n[VERDICT]")
    print(f"  {r.verdict}")
    print(f"  standing: {r.standing}  (nobody chose to be born)")
    print(f"  {r.mirror}")

    print("\n[IV. The hard cases]")
    for label, kw in [
        ("slander",             dict(accurate=False)),
        ("the blade",           dict(aims_to_wound=True)),
        ("saved for the moment", dict(deployed_for_advantage=True)),
        ("sprung years later",  dict(spoken_at_event=False,
                                     confronted_other=False)),
        ("late, but confronted", dict(spoken_at_event=False)),
        ("timely, unconfronted", dict(confronted_other=False)),
        ("the contract, years later", dict(spoken_at_event=False,
                                           confronted_other=False,
                                           written_contract=True)),
        ("the megaphone",       dict(audience="crowd")),
        ("the pattern, live",   dict(spoken_at_event=False,
                                     is_pattern=True, pattern_live=True)),
        ("the first opening",   dict(spoken_at_event=False,
                                     confronted_other=False,
                                     first_true_opening=True)),
    ]:
        v = wield(Speaking(**kw)).verdict
        print(f"  {label}: {v}")
    print("=" * 72)
    return 0


# ----------------------------------------------------------------------
# V. Tests
# ----------------------------------------------------------------------

class Tests(unittest.TestCase):

    # I. the sword
    def test_sword_passes(self):
        r = wield(Speaking())
        self.assertIn("PASSES", r.verdict)
        self.assertIn("SWORD OF LIGHT", r.verdict)

    def test_hurt_does_not_fail_it(self):
        r = wield(Speaking(will_hurt=True))
        self.assertIn("PASSES", r.verdict)
        self.assertIn("IT HURTS", " ".join(r.lines))

    # II. the collapses
    def test_false_content_collapses(self):
        r = wield(Speaking(accurate=False))
        self.assertIn("COLLAPSES", r.verdict)
        self.assertIn("NO LIGHT", " ".join(r.lines))

    def test_aim_to_wound_collapses(self):
        r = wield(Speaking(aims_to_wound=True))
        self.assertIn("COLLAPSES", r.verdict)
        self.assertIn("BLADE", " ".join(r.lines))

    def test_advantage_is_revenge(self):
        r = wield(Speaking(deployed_for_advantage=True,
                           confronted_other=False))
        self.assertIn("REVENGE", r.verdict)

    def test_advantage_is_revenge_even_if_confronted(self):
        r = wield(Speaking(deployed_for_advantage=True,
                           confronted_other=True))
        self.assertIn("REVENGE", r.verdict)

    def test_stockpiled_is_revenge(self):
        r = wield(Speaking(spoken_at_event=False, confronted_other=False))
        self.assertIn("REVENGE", r.verdict)

    # III. the partials
    def test_late_but_confronted_is_partial(self):
        r = wield(Speaking(spoken_at_event=False))
        self.assertIn("PARTIAL", r.verdict)
        self.assertIn("LATE", " ".join(r.flags))

    def test_at_event_unconfronted_is_partial(self):
        r = wield(Speaking(confronted_other=False))
        self.assertIn("PARTIAL", r.verdict)

    # IV. the written contract
    def test_written_contract_survives_time(self):
        r = wield(Speaking(spoken_at_event=False, confronted_other=False,
                           written_contract=True))
        self.assertIn("PASSES", r.verdict)
        self.assertIn("WRITTEN WORD", " ".join(r.lines))

    def test_written_contract_defeats_advantage_timing(self):
        r = wield(Speaking(deployed_for_advantage=True,
                           written_contract=True))
        self.assertNotIn("REVENGE", r.verdict)
        self.assertIn("PASSES", r.verdict)

    def test_written_contract_does_not_excuse_the_blade(self):
        r = wield(Speaking(written_contract=True, aims_to_wound=True))
        self.assertIn("COLLAPSES", r.verdict)

    def test_written_contract_still_needs_truth(self):
        r = wield(Speaking(written_contract=True, accurate=False))
        self.assertIn("COLLAPSES", r.verdict)

    # V. the patch: audience, pattern, opening, mirror
    def test_broadcast_collapses(self):
        r = wield(Speaking(audience="crowd"))
        self.assertIn("COLLAPSES", r.verdict)
        self.assertIn("MEGAPHONE", " ".join(r.lines))

    def test_audience_words(self):
        self.assertIn("THE 1", the_audience("proper"))
        self.assertIn("THE 0", the_audience("crowd"))

    def test_pattern_still_live_is_timely(self):
        r = wield(Speaking(spoken_at_event=False, is_pattern=True,
                           pattern_live=True))
        self.assertIn("PASSES", r.verdict)
        self.assertIn("PATTERN", " ".join(r.lines))

    def test_pattern_dead_is_late(self):
        r = wield(Speaking(spoken_at_event=False, is_pattern=True,
                           pattern_live=False))
        self.assertIn("PARTIAL", r.verdict)

    def test_first_true_opening_is_not_revenge(self):
        r = wield(Speaking(spoken_at_event=False, confronted_other=False,
                           first_true_opening=True))
        self.assertNotIn("REVENGE", r.verdict)
        self.assertIn("PARTIAL", r.verdict)
        self.assertIn("FIRST TRUE OPENING", " ".join(r.flags))

    def test_opening_does_not_launder_advantage(self):
        r = wield(Speaking(first_true_opening=True,
                           deployed_for_advantage=True))
        self.assertIn("REVENGE", r.verdict)

    def test_mirror_travels_with_every_reading(self):
        for kw in ({}, {"accurate": False}, {"audience": "crowd"}):
            self.assertIn("MIRROR", wield(Speaking(**kw)).mirror)

    # VI. the wound and the clock
    def test_wound_from_truth_is_one(self):
        self.assertIn("THE 1", the_wound("truth"))

    def test_wound_from_malice_is_zero(self):
        self.assertIn("THE 0", the_wound("malice"))

    def test_held_light_record_is_one(self):
        self.assertIn("THE 1", held_light("record"))

    def test_held_light_opportunity_is_revenge(self):
        r = held_light("opportunity")
        self.assertIn("THE 0", r)
        self.assertIn("REVENGE", r)

    def test_held_light_never_is_zero(self):
        self.assertIn("THE 0", held_light("never"))

    # VII. standing form
    def test_standing_always_false(self):
        for kw in ({}, {"accurate": False}, {"aims_to_wound": True},
                   {"deployed_for_advantage": True}):
            self.assertFalse(wield(Speaking(**kw)).standing)

    def test_no_single_word_verdict(self):
        r = wield(Speaking())
        self.assertGreater(len(r.verdict.split()), 8)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


# ----------------------------------------------------------------------
# VI. CLI
# ----------------------------------------------------------------------

def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        description="The holy sword of truth — read through Awaken Tao.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    if args.test:
        return run_tests()
    return demonstrate()


if __name__ == "__main__":
    sys.exit(main())
