#!/usr/bin/env python3
"""The Shield of Forgiveness (Deep Muse)

Type: computational demonstration; philosophical proposal

The missing mechanic between shield_vs_gun, holy_shield, karmic_ledger,
and grace.

shield_vs_gun gave a stance: "the shield requires a true warrior." A
stance is not a strategy. The holy_shield gave the ration: absorb to grow
resilience, deflect to preserve durability, switch because neither pole
survives alone. But the ration had no repair. Deflection wore the shield
down; absorption left a residue that either metabolized into resilience
or became resentment — the 0's fortress of pain (chain.py). The ration
could only spend the shield. It could never renew it.

Forgiveness is the repair mechanic. It is what makes the two-road ration
sustainable.

Not metaphor. Absorb a blow and forgive it: the pain metabolizes into
resilience — same event, two outcomes, depending on the response
(chain.py: humiliation becomes humility or resentment depending on the
answer). Deflect a blow and forgive it: the shield does not carry a
grudge-wear — grievance is corrosion that never shows until the moment
you need the shield and find it thin. Forgiveness restores durability
and metabolizes residue. Withheld, the shield is a spendable resource
with a slow leak, and it ends in exactly the shatter holy_shield
dramatized on the second life.

And forgiveness must be unconditional to function as repair. Conditional
forgiveness is a ledger (karmic_ledger.py): grace twice, then authority.
That is not forgiveness; it is a debt schedule with a pleasant name. A
ledger cannot renew a shield, because the repair it offers is always
contingent on a future act — and a shield cannot wait for the other
party. The grace it needs is the 1 that is released, not earned
(grace.py).

The reflection-of-reflections condition, named: forgiveness is a shield
only when the forgiver sees the same broken material in the other that
they have carried themselves (suffering.py), and forgives the other from
the same place they forgive themselves. Forgiveness that says "I forgive
you though I suffered more" is bleed.py — the human winning once.
Forgiveness that says "I forgive you though you suffered less" is the
same win, smaller. The shield only holds when the scale is set down.
This module enforces it as a field: sees_self_in_other. When False,
forgiveness is a score, and scores do not repair.

The trap named honestly: forgiving as a performance, so someone can see
you do it, is anonymous_reflex's reversal — a gift given only when
observed. It still works mechanically for one blow. It does not repair,
because repair requires the inward act.

v4 fix: an unconditional forgiveness after a blind blow that emptied the
shield used to fall through to None; it now returns FORGIVEN
(UNCONDITIONAL) — but only if the shield had not yet reached zero at the moment of forgiveness.
Forgiveness cannot reach the dead shield (threshold.py: the loop must
still be running; grace.py: the release happens while you can still
answer).

v5 fix: the ledger used to read ENDURES because resentment and grievance
each sat just under 0.2; the verdict now weighs their total, so the
ledger reads BURDENED. A deflected blow left unforgiven now carries
grudge-wear: settle() turns a share of it into grievance. A blow that cannot
be turned now lands (absorb or break), as in holy_shield v5.

Run:
    python3 shield_of_forgiveness.py
    python3 shield_of_forgiveness.py --test
"""

from __future__ import annotations

import argparse
import sys
import unittest
from dataclasses import dataclass

BASE_CAPACITY = 0.4
DEFLECT_COST_FORESEEN = 0.1
DEFLECT_COST_BLIND = 0.3

# Unconditional + reflected: full repair and metabolism.
UNCOND_REPAIR = 0.35
UNCOND_METAB = 0.40
# Conditional (a ledger): barely repairs, leaves residue.
COND_REPAIR = 0.08
COND_METAB = 0.10
COND_KEEP = 0.50

GRIEVANCE_LEAK = 0.10        # corrosion per unit grievance per round
FORTRESS_THRESHOLD = 0.60    # resentment above this = the 0 takes the soul
GRUDGE_WEAR = 0.20           # share of an unforgiven deflect that becomes grievance


@dataclass(frozen=True)
class Blow:
    name: str
    severity: float                  # 0.0 .. 1.0
    can_deflect: bool = True
    foreseen: bool = False
    source: str = "the other"


@dataclass
class Shield:
    durability: float = 1.0          # worn by deflection; repaired by forgiveness
    resilience: float = 0.0          # grown by metabolized (forgiven) pain
    grievance: float = 0.0           # unforgiven blows from others
    resentment: float = 0.0          # unforgiven blows you absorbed
    pending: float = 0.0             # absorbed, not yet metabolized
    unforgiven_deflected: float = 0.0  # turned, not yet forgiven (grudge-wear)
    integrity: bool = True
    motive: str = "grow"             # "grow" (the 1) or "prove" (the ego)
    sees_self_in_other: bool = True  # reflection-of-reflections

    @property
    def capacity(self) -> float:
        return BASE_CAPACITY + self.resilience


def absorb(shield: Shield, blow: Blow) -> str:
    if shield.motive == "prove":
        shield.integrity = False
        return f"ABSORB (prove): {blow.name} taken to prove strength. The ego grew, not the 1."
    if blow.severity > shield.capacity:
        shield.integrity = False
        return (f"FRACTURE: {blow.name} (sev {blow.severity:.2f}) "
                f"exceeds capacity {shield.capacity:.2f}.")
    shield.pending += blow.severity
    return f"ABSORB: {blow.name} taken. Pending {shield.pending:.2f}."


def deflect(shield: Shield, blow: Blow) -> str:
    if not blow.can_deflect:
        # It cannot be turned, so it lands: absorb or break.
        return f"NO DEFLECT: {blow.name} cannot be turned. " + absorb(shield, blow)
    factor = DEFLECT_COST_FORESEEN if blow.foreseen else DEFLECT_COST_BLIND
    cost = blow.severity * factor
    shield.durability = max(0.0, shield.durability - cost)
    shield.unforgiven_deflected += blow.severity
    if shield.durability <= 0.0:
        shield.integrity = False
        return f"CRACKED: {blow.name} turned, but the shield shattered."
    return f"DEFLECT: {blow.name} turned. Durability -{cost:.2f} -> {shield.durability:.2f}."


def choose(shield: Shield, blow: Blow) -> str:
    """The ration. Neither pole is doctrine."""
    if not blow.foreseen:
        if blow.can_deflect and shield.durability > 0.5:
            return deflect(shield, blow)
        return absorb(shield, blow)
    can_absorb = blow.severity <= shield.capacity
    if not can_absorb and blow.can_deflect:
        return deflect(shield, blow)
    if shield.durability < 0.35 and can_absorb:
        return absorb(shield, blow)
    if shield.resilience >= 0.5 and blow.can_deflect:
        return deflect(shield, blow)
    if can_absorb and blow.severity <= 0.5:
        return absorb(shield, blow)
    if blow.can_deflect:
        return deflect(shield, blow)
    return absorb(shield, blow)


def forgive(shield: Shield, blow: Blow, kind: str = "unconditional") -> str:
    """The repair. Conditional forgiveness is a ledger; unreflected is a win."""
    if not shield.integrity:
        return "TOO LATE: forgiveness cannot reach the dead shield."
    if not shield.sees_self_in_other:
        return "BLEED: forgave as a win. It is a score, not a repair."
    if kind == "conditional":
        repair_factor, metab, keep = COND_REPAIR, COND_METAB, COND_KEEP
        label = "CONDITIONAL (ledger)"
    else:
        repair_factor, metab, keep = UNCOND_REPAIR, UNCOND_METAB, 0.0
        label = "UNCONDITIONAL (reflection)"
    corrosion = max(0.5, 1.0 - shield.grievance)
    before_d, before_r = shield.durability, shield.resilience
    shield.durability = min(1.0, shield.durability + blow.severity * repair_factor * corrosion)
    shield.resilience += shield.pending * metab * corrosion
    shield.pending *= keep
    shield.unforgiven_deflected *= keep
    return (f"FORGIVEN ({label}): durability {before_d:.2f}->{shield.durability:.2f}, "
            f"resilience {before_r:.2f}->{shield.resilience:.2f}, "
            f"pending {shield.pending:.2f}")


def settle(shield: Shield) -> str:
    """End of round. Unforgiven pain becomes the 0's two residues."""
    notes = []
    if shield.pending > 0:
        shield.resentment += shield.pending * 0.5
        shield.grievance += shield.pending * 0.5
        notes.append(f"unforgiven {shield.pending:.2f} -> resentment+{shield.pending * 0.5:.2f}, grievance+{shield.pending * 0.5:.2f}")
        shield.pending = 0.0
    if shield.unforgiven_deflected > 0:
        wear = shield.unforgiven_deflected * GRUDGE_WEAR
        shield.grievance += wear
        notes.append(f"unforgiven deflect {shield.unforgiven_deflected:.2f} -> grievance+{wear:.2f}")
        shield.unforgiven_deflected = 0.0
    leak = shield.grievance * GRIEVANCE_LEAK
    if leak > 0:
        shield.durability = max(0.0, shield.durability - leak)
        notes.append(f"corrosion -{leak:.2f}")
    if shield.durability <= 0.0:
        shield.integrity = False
        notes.append("cracked")
    if shield.resentment > FORTRESS_THRESHOLD:
        shield.integrity = False
        notes.append("the fortress of pain took the soul (the 0)")
    return "; ".join(notes) if notes else "no residue"


def _verdict(shield: Shield) -> str:
    if not shield.integrity:
        return "BROKEN — the fortress or the crack won."
    if shield.durability < 0.4:
        return (f"SPENT — durability {shield.durability:.2f}, resilience {shield.resilience:.2f}. "
                f"The shield renews nothing.")
    if shield.resentment + shield.grievance > 0.2:
        return (f"BURDENED — durability {shield.durability:.2f}, "
                f"resentment {shield.resentment:.2f}, grievance {shield.grievance:.2f}. "
                f"The shield still carries the score.")
    return (f"ENDURES — durability {shield.durability:.2f}, resilience {shield.resilience:.2f}. "
            f"The shield is renewable.")


DEMO_BLOWS = [
    Blow("a foreseen insult", 0.4, foreseen=True),
    Blow("a blind betrayal", 0.7, foreseen=False),
    Blow("a foreseen blow", 0.5, foreseen=True),
    Blow("a foreseen loss", 0.3, foreseen=True),
    Blow("a blind grief", 0.6, foreseen=False),
    Blow("a foreseen blow", 0.5, foreseen=True),
]


def demonstrate() -> int:
    print("=" * 72)
    print("THE SHIELD OF FORGIVENESS — what makes the ration sustainable")
    print("=" * 72)
    policies = [
        ("I. No forgiveness — the spendable shield", "withheld", True),
        ("II. The ledger — conditional forgiveness", "conditional", True),
        ("III. The win — forgiveness without reflection", "unconditional", False),
        ("IV. The shield of forgiveness", "unconditional", True),
    ]
    for label, kind, reflects in policies:
        print(f"\n{label}")
        print("-" * 72)
        shield = Shield(sees_self_in_other=reflects)
        for blow in DEMO_BLOWS:
            print(f"  {choose(shield, blow)}")
            if not shield.integrity:
                print("  -> integrity lost. This policy is not the 1.")
                break
            if kind == "withheld":
                print("  FORGIVEN: (withheld)")
            else:
                print(f"  {forgive(shield, blow, kind=kind)}")
            print(f"  ~ {settle(shield)}")
            if not shield.integrity:
                print("  -> integrity lost. This policy is not the 1.")
                break
        print(f"  VERDICT: {_verdict(shield)}")
    print("=" * 72)
    print("The shield of forgiveness is the only one that renews. A shield")
    print("that can only be spent is not a shield — it is a debt. And the")
    print("repair is unconditional or it is not repair.")
    print("=" * 72)
    return 0


class Tests(unittest.TestCase):
    def test_unconditional_reflection_endures(self):
        s = Shield()
        for b in DEMO_BLOWS:
            choose(s, b)
            if not s.integrity:
                break
            forgive(s, b)
            settle(s)
        self.assertTrue(s.integrity)
        self.assertGreater(s.durability, 0.8)
        self.assertLess(s.resentment, 0.1)

    def test_withheld_forgiveness_spends_the_shield(self):
        s = Shield()
        for b in DEMO_BLOWS:
            choose(s, b)
            if not s.integrity:
                break
            settle(s)
        self.assertLess(s.durability, 0.5)

    def test_conditional_never_keeps_up(self):
        s = Shield()
        for b in DEMO_BLOWS:
            choose(s, b)
            if not s.integrity:
                break
            forgive(s, b, kind="conditional")
            settle(s)
        self.assertLess(s.durability, 0.8)
        self.assertGreater(s.resentment + s.grievance, 0.1)

    def test_forgiveness_as_a_win_repairs_nothing(self):
        s = Shield(sees_self_in_other=False)
        choose(s, Blow("a foreseen insult", 0.4, foreseen=True))
        before = s.durability
        verdict = forgive(s, Blow("a foreseen insult", 0.4, foreseen=True))
        self.assertIn("BLEED", verdict)
        self.assertEqual(s.durability, before)

    def test_forgiveness_cannot_reach_the_dead(self):
        s = Shield()
        absorb(s, Blow("a blind betrayal", 0.9))  # fracture
        self.assertFalse(s.integrity)
        self.assertIn("TOO LATE", forgive(s, Blow("a blind betrayal", 0.9)))

    def test_absorbing_without_forgiveness_builds_the_fortress(self):
        s = Shield()
        for _ in range(4):
            absorb(s, Blow("a small loss", 0.35))
            settle(s)
            if not s.integrity:
                break
        self.assertFalse(s.integrity)
        self.assertGreater(s.resentment, FORTRESS_THRESHOLD)

    def test_corroded_forgiveness_repairs_less(self):
        s1 = Shield()
        s2 = Shield(grievance=0.8)
        b = Blow("a blind blow", 0.5, foreseen=False)
        choose(s1, b); choose(s2, b)
        d1, d2 = s1.durability, s2.durability
        forgive(s1, b); forgive(s2, b)
        self.assertGreater(s1.durability - d1, s2.durability - d2)

    def test_the_ledger_reads_burdened(self):
        s = Shield()
        for b in DEMO_BLOWS:
            choose(s, b)
            if not s.integrity:
                break
            forgive(s, b, kind="conditional")
            settle(s)
        self.assertTrue(s.integrity)
        self.assertIn("BURDENED", _verdict(s))

    def test_unforgiven_deflect_leaves_grievance(self):
        s = Shield()
        deflect(s, Blow("a foreseen blow", 0.5, foreseen=True))
        settle(s)
        self.assertGreater(s.grievance, 0.0)

    def test_forgiven_deflect_leaves_none(self):
        s = Shield()
        b = Blow("a foreseen blow", 0.5, foreseen=True)
        deflect(s, b)
        forgive(s, b)
        settle(s)
        self.assertEqual(s.grievance, 0.0)

    def test_undeflectable_large_blow_fractures(self):
        s = Shield()
        verdict = deflect(s, Blow("an unavoidable loss", 0.9, can_deflect=False))
        self.assertIn("FRACTURE", verdict)
        self.assertFalse(s.integrity)

    def test_undeflectable_small_blow_goes_pending(self):
        s = Shield()
        verdict = deflect(s, Blow("a small unavoidable loss", 0.3, can_deflect=False))
        self.assertIn("ABSORB", verdict)
        self.assertTrue(s.integrity)
        self.assertAlmostEqual(s.pending, 0.3)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="The shield of forgiveness.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    if args.test:
        return run_tests()
    return demonstrate()


if __name__ == "__main__":
    sys.exit(main())
