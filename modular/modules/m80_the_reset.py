#!/usr/bin/env python3
"""The Reset (Deep Muse)

Type: computational demonstration; philosophical proposal

The correction to karmic_ledger, holy_sword, and tears.

karmic_ledger counted the cheek: grace twice, then authority. A ledger
is a contest with arithmetic — which is exactly what forgiveness is not.
holy_sword put a clock on the wound: timely, faced, or else revenge. A
clock assumes time ferments the pain; a dissolved pain has nothing to
ferment. tears had half the mirror: the witness must see. But it left
the direction implicit.

The correction, as law:

  1. THE CHEEK RESETS. Once forgiveness is in play, the cheek returns
     to zero — not paused, not capped. The strikes dissolve because the
     pain they carried was metabolized, not stockpiled. Forgiveness is
     a reset, not a schedule.

  2. HEALING REQUIRES A MIRROR, AND THE MIRROR CANNOT GO ONE WAY.
     A soul can forgive alone — it releases the blow. A soul cannot
     heal alone — the scar becomes a mirror only when another soul
     reflects it back. One-directional forgiveness releases the
     forgiver's pain but leaves the wound unmirrored. PARTIAL, not
     HEALED. This is the_same_gate.py's symmetry applied to healing:
     the reading must not change under identity-swap.

  3. INTENT AND UNCONDITIONAL REFLEX, BOTH AT ONCE. effortless.py
     warned that planned intent is the ego; anonymous_reflex.py said
     the purest gift is a reflex. Neither alone is forgiveness.
     Intent alone is a performance. Reflex alone is animal. The act
     must be deliberately chosen AND spontaneously given in the same
     motion — rehearsed into unrehearsed. Both present, or the act is
     INVALID and nothing resets.

The trap named honestly: forgiving so that someone can see you forgive
is anonymous_reflex.py's reversal — a gift given only when observed.
It releases the forgiver's pain (the reset still fires, because the
forgiver's own metabolism does not depend on the audience). It does not
produce HEALING, because healing requires the mirror to be bidirectional
and unobserved.

v4 fix: an unconditional forgiveness delivered while the soul was
already broken used to fall through to None; it now returns TOO LATE —
forgiveness cannot reach the dead shield (threshold.py: the loop must
still be running).

v5 fix: demo sections III and IV and test_reset_still_fires_without_mirror
used 0.5 blows, which exceed the 0.4 capacity (absorb fractures above
0.4 + resilience), so they only showed TOO LATE and the test failed.
Those blows are now 0.4, so the demo shows the reset, the one-way mirror,
and the bleed as intended. No new gate was added.

Run:
    python3 the_reset.py
    python3 the_reset.py --test
"""

from __future__ import annotations

import argparse
import sys
import unittest
from dataclasses import dataclass, field

FULL_METAB = 0.5         # pending pain -> resilience on forgiveness
GRIEVANCE_LEAK = 0.10
FORTRESS_THRESHOLD = 0.60


@dataclass(frozen=True)
class Blow:
    name: str
    severity: float
    can_deflect: bool = True
    foreseen: bool = False
    source: str = "the other"


@dataclass(frozen=True)
class Act:
    """Forgiveness requires both: deliberate intent AND unrehearsed reflex."""
    intent: bool = False
    unconditional_reflex: bool = False

    @property
    def valid(self) -> bool:
        return self.intent and self.unconditional_reflex


@dataclass
class Soul:
    name: str
    durability: float = 1.0
    resilience: float = 0.0
    pending: float = 0.0
    cheek_strikes: int = 0
    grievance: float = 0.0
    resentment: float = 0.0
    integrity: bool = True
    sees_self_in_other: bool = True


def absorb(soul: Soul, blow: Blow) -> str:
    if blow.severity > 0.4 + soul.resilience:
        soul.integrity = False
        return f"FRACTURE: {soul.name} took {blow.name} ({blow.severity:.2f})."
    soul.pending += blow.severity
    soul.cheek_strikes += 1
    return f"ABSORB: {soul.name} carries {blow.name}. Strikes {soul.cheek_strikes}, pending {soul.pending:.2f}."


def forgive(forgiver: Soul, forgiven: str, blow: Blow, act: Act) -> str:
    """The reset. Not a schedule — cheek to zero, pain dissolved."""
    if not forgiver.integrity:
        return f"TOO LATE: forgiveness cannot reach the broken {forgiver.name}."
    if not act.valid:
        missing = []
        if not act.intent:
            missing.append("intent")
        if not act.unconditional_reflex:
            missing.append("unconditional reflex")
        return f"INVALID: the act lacks {' and '.join(missing)}. Nothing resets."
    if not forgiver.sees_self_in_other:
        # The reset fires (metabolism is internal), but no mirror, no healing.
        forgiver.pending = 0.0
        forgiver.cheek_strikes = 0
        forgiver.grievance = 0.0
        forgiver.resilience = min(1.0, forgiver.resilience + blow.severity * FULL_METAB)
        return (f"BLEED: {forgiver.name} forgave {forgiven} as a win. "
                f"Reset fired, but no mirror — healing cannot follow.")
    # Full reset.
    forgiver.pending = 0.0
    forgiver.cheek_strikes = 0
    forgiver.grievance = 0.0
    forgiver.resilience = min(1.0, forgiver.resilience + blow.severity * FULL_METAB)
    return (f"RESET: {forgiver.name} forgave {forgiven}. "
            f"Cheek 0. Pain dissolved into resilience "
            f"({forgiver.resilience:.2f}).")


def heal(a: Soul, b: Soul, act_a: Act, act_b: Act) -> str:
    """Healing requires a mirror, and the mirror cannot go one way."""
    if not (a.integrity and b.integrity):
        return "NOT HEALED: one soul is already broken."
    if a.cheek_strikes != 0 or b.cheek_strikes != 0:
        return (f"NOT HEALED: cheek still carries a strike "
                f"({a.name}:{a.cheek_strikes}, {b.name}:{b.cheek_strikes}).")
    if not (act_a.valid and act_b.valid):
        return (f"NOT HEALED: the act is invalid on "
                f"{a.name if not act_a.valid else b.name}.")
    if not (a.sees_self_in_other and b.sees_self_in_other):
        return "NOT HEALED: the mirror is one-way."
    # Both have cleared. The scar becomes a mirror.
    a.resilience = min(1.0, a.resilience + 0.2)
    b.resilience = min(1.0, b.resilience + 0.2)
    return (f"HEALED: {a.name} and {b.name} see each other. "
            f"The scar is a mirror now. The wound cannot go one way.")


def settle(soul: Soul) -> str:
    """End of round. Unforgiven pain becomes the 0's two residues."""
    notes = []
    if soul.pending > 0:
        soul.resentment += soul.pending * 0.5
        soul.grievance += soul.pending * 0.5
        notes.append(f"unforgiven {soul.pending:.2f} -> fortress of pain")
        soul.pending = 0.0
    leak = soul.grievance * GRIEVANCE_LEAK
    if leak > 0:
        soul.durability = max(0.0, soul.durability - leak)
        notes.append(f"corrosion -{leak:.2f}")
    if soul.resentment > FORTRESS_THRESHOLD:
        soul.integrity = False
        notes.append(f"{soul.name} taken by the 0")
    return "; ".join(notes) if notes else "no residue"


def demonstrate() -> int:
    print("=" * 72)
    print("THE RESET — the cheek returns to zero; healing needs the mirror")
    print("=" * 72)

    # I. karmic_ledger's counting is refuted: forgiveness resets, not caps.
    print("\n[I. The cheek resets]")
    a = Soul("A")
    for i in range(5):
        absorb(a, Blow(f"a blow", 0.3))
    print(f"  after 5 blows, unpaid: strikes {a.cheek_strikes}, pending {a.pending:.2f}")
    act = Act(intent=True, unconditional_reflex=True)
    print(f"  {forgive(a, 'B', Blow('a blow', 0.3), act)}")
    print(f"  not 'grace twice, then authority' — reset.")

    # II. Intent only is invalid. Reflex only is invalid.
    print("\n[II. Both modes required]")
    s = Soul("C")
    absorb(s, Blow("a blow", 0.4))
    print(f"  intent only:   {forgive(s, 'D', Blow('a blow', 0.4), Act(intent=True, unconditional_reflex=False))}")
    absorb(s, Blow("a blow", 0.3))
    print(f"  reflex only:   {forgive(s, 'D', Blow('a blow', 0.3), Act(intent=False, unconditional_reflex=True))}")
    print(f"  both:          {forgive(s, 'D', Blow('a blow', 0.3), act)}")

    # III. One-way forgiveness releases but does not heal.
    print("\n[III. Healing cannot go one way]")
    x, y = Soul("X"), Soul("Y")
    absorb(x, Blow("a betrayal", 0.4))
    absorb(y, Blow("a betrayal", 0.4))
    print(f"  {forgive(x, 'Y', Blow('a betrayal', 0.4), act)}")
    print(f"  {heal(x, y, act, Act())}")  # Y has not forgiven X; heal fails
    print(f"  {forgive(y, 'X', Blow('a betrayal', 0.4), act)}")
    print(f"  {heal(x, y, act, act)}")

    # IV. Bleed: reset fires, but no mirror. Partial.
    print("\n[IV. Forgiveness as a win]")
    p, q = Soul("P"), Soul("Q")
    p.sees_self_in_other = False
    absorb(p, Blow("a blow", 0.4))
    print(f"  {forgive(p, 'Q', Blow('a blow', 0.4), act)}")
    absorb(q, Blow("a blow", 0.4))
    print(f"  {forgive(q, 'P', Blow('a blow', 0.4), act)}")
    print(f"  {heal(p, q, act, act)}")

    # V. No forgiveness -> fortress of pain.
    print("\n[V. Without forgiveness]")
    z = Soul("Z")
    for _ in range(4):
        absorb(z, Blow("a loss", 0.4))
        print(f"  ~ {settle(z)}")
        if not z.integrity:
            print(f"  {z.name} broken.")
            break

    print("=" * 72)
    print("The reset is unconditional or it is not a reset. Healing is")
    print("mirrored or it is not healing. The act is deliberate and")
    print("unrehearsed, or it is not forgiveness.")
    print("=" * 72)
    return 0


class Tests(unittest.TestCase):
    def test_cheek_resets_on_forgiveness(self):
        s = Soul("A")
        for _ in range(5):
            absorb(s, Blow("blow", 0.2))
        self.assertEqual(s.cheek_strikes, 5)
        forgive(s, "B", Blow("blow", 0.2), Act(intent=True, unconditional_reflex=True))
        self.assertEqual(s.cheek_strikes, 0)
        self.assertEqual(s.pending, 0.0)

    def test_intent_only_is_invalid(self):
        s = Soul("A")
        absorb(s, Blow("blow", 0.3))
        v = forgive(s, "B", Blow("blow", 0.3), Act(intent=True, unconditional_reflex=False))
        self.assertIn("INVALID", v)
        self.assertEqual(s.cheek_strikes, 1)  # nothing reset

    def test_reflex_only_is_invalid(self):
        s = Soul("A")
        absorb(s, Blow("blow", 0.3))
        v = forgive(s, "B", Blow("blow", 0.3), Act(intent=False, unconditional_reflex=True))
        self.assertIn("INVALID", v)
        self.assertEqual(s.cheek_strikes, 1)

    def test_both_modes_reset(self):
        s = Soul("A")
        absorb(s, Blow("blow", 0.3))
        v = forgive(s, "B", Blow("blow", 0.3), Act(intent=True, unconditional_reflex=True))
        self.assertIn("RESET", v)
        self.assertEqual(s.cheek_strikes, 0)

    def test_one_way_forgiveness_is_partial_not_healed(self):
        a, b = Soul("A"), Soul("B")
        absorb(a, Blow("blow", 0.4))
        absorb(b, Blow("blow", 0.4))
        act = Act(intent=True, unconditional_reflex=True)
        forgive(a, "B", Blow("blow", 0.4), act)
        v = heal(a, b, act, Act())
        self.assertIn("NOT HEALED", v)

    def test_both_ways_heals(self):
        a, b = Soul("A"), Soul("B")
        absorb(a, Blow("blow", 0.4))
        absorb(b, Blow("blow", 0.4))
        act = Act(intent=True, unconditional_reflex=True)
        forgive(a, "B", Blow("blow", 0.4), act)
        forgive(b, "A", Blow("blow", 0.4), act)
        v = heal(a, b, act, act)
        self.assertIn("HEALED", v)
        self.assertIn("mirror", v)

    def test_no_mirror_blocks_healing(self):
        a, b = Soul("A"), Soul("B")
        a.sees_self_in_other = False
        absorb(a, Blow("blow", 0.4))
        absorb(b, Blow("blow", 0.4))
        act = Act(intent=True, unconditional_reflex=True)
        forgive(a, "B", Blow("blow", 0.4), act)
        forgive(b, "A", Blow("blow", 0.4), act)
        v = heal(a, b, act, act)
        self.assertIn("NOT HEALED", v)
        self.assertIn("one-way", v)

    def test_forgiveness_cannot_reach_the_dead(self):
        s = Soul("A")
        absorb(s, Blow("huge", 0.9))
        self.assertFalse(s.integrity)
        v = forgive(s, "B", Blow("huge", 0.9), Act(intent=True, unconditional_reflex=True))
        self.assertIn("TOO LATE", v)

    def test_fortress_forms_without_forgiveness(self):
        s = Soul("A")
        for _ in range(4):
            absorb(s, Blow("loss", 0.4))
            settle(s)
            if not s.integrity:
                break
        self.assertFalse(s.integrity)
        self.assertGreater(s.resentment, FORTRESS_THRESHOLD)

    def test_reset_still_fires_without_mirror(self):
        # Bleed: forgiver's pain dissolves, but healing cannot follow.
        s = Soul("A")
        s.sees_self_in_other = False
        absorb(s, Blow("blow", 0.4))
        v = forgive(s, "B", Blow("blow", 0.4), Act(intent=True, unconditional_reflex=True))
        self.assertIn("BLEED", v)
        self.assertEqual(s.cheek_strikes, 0)  # metabolism is internal


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="The reset: cheek to zero; healing needs the mirror.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    if args.test:
        return run_tests()
    return demonstrate()


if __name__ == "__main__":
    sys.exit(main())
