#!/usr/bin/env python3
"""The Holy Shield (Deep Muse)

Type: computational demonstration; philosophical proposal

The missing mechanic between shield_vs_gun and karmic_ledger.

shield_vs_gun gave a stance: "the shield requires a true warrior." A
stance is not a strategy. A shield raised against everything cracks; a
body that absorbs everything fractures. The sustainable path is neither
pole. It is load-balancing: a soul that sees the blow coming and chooses,
per blow, whether to absorb it (grow resilience) or deflect it (preserve
durability). Deflect every time and the shield dies of wear; absorb every
time and the body dies of fracture. Switching is sustainability — the 1
that keeps going is the one that rations its own endurance.

The trap named honestly: absorbing pain "to become stronger" is the ego's
martyrdom (bleed.py). The difference is motive. Absorbing to grow feeds
the 1; absorbing to prove you can take it feeds the 0. The module checks
motive before it credits resilience.

Foresight is the prerequisite for choice: a blow you did not see coming
cannot be chosen, only eaten — or reflex-turned blind at full cost.

v4 fix: a foreseen, deflected blow that empties the shield used to fall
through to None; it now returns the CRACKED verdict.

v5 fix: a blow that cannot be turned used to cost deflect() nothing; it
now lands (absorb or break), so deflect-everything pays for it.

Run:
    python3 holy_shield.py
    python3 holy_shield.py --test
"""

from __future__ import annotations
import argparse
import sys
import unittest
from dataclasses import dataclass

BASE_CAPACITY = 0.4          # what a fresh soul can absorb without fracture
DEFLECT_COST_FORESEEN = 0.1  # cheap, because you angled it
DEFLECT_COST_BLIND = 0.3     # expensive, because reflex guessed


@dataclass(frozen=True)
class Blow:
    name: str
    severity: float          # 0.0 .. 1.0
    can_deflect: bool = True
    foreseen: bool = False


@dataclass
class Shield:
    durability: float = 1.0  # worn by deflection
    resilience: float = 0.0  # grown by absorbed pain
    integrity: bool = True   # is the soul still the 1?
    motive: str = "grow"     # "grow" (the 1) or "prove" (the ego)

    @property
    def capacity(self) -> float:
        return BASE_CAPACITY + self.resilience


def absorb(shield: Shield, blow: Blow) -> str:
    """Take the blow. Resilience grows; durability untouched."""
    if shield.motive == "prove":
        shield.integrity = False
        shield.resilience = min(1.0, shield.resilience + blow.severity * 0.5)
        return (f"ABSORB (prove): {blow.name} taken to prove strength. "
                f"The ego grows, not the 1.")
    if blow.severity > shield.capacity:
        shield.integrity = False
        return (f"FRACTURE: {blow.name} (sev {blow.severity:.2f}) exceeds "
                f"capacity {shield.capacity:.2f}. Absorbing broke you.")
    gain = blow.severity * (0.3 if blow.foreseen else 0.15)
    shield.resilience = min(1.0, shield.resilience + gain)
    return (f"ABSORB (grow): {blow.name} taken. "
            f"Resilience +{gain:.2f} -> {shield.resilience:.2f}.")


def deflect(shield: Shield, blow: Blow) -> str:
    """Angle the blow away. Durability wears; resilience untouched."""
    if not blow.can_deflect:
        # It cannot be turned, so it lands: absorb or break.
        return f"NO DEFLECT: {blow.name} cannot be turned. " + absorb(shield, blow)
    factor = DEFLECT_COST_FORESEEN if blow.foreseen else DEFLECT_COST_BLIND
    cost = blow.severity * factor
    shield.durability = max(0.0, shield.durability - cost)
    if shield.durability <= 0.0:
        shield.integrity = False
        return (f"CRACKED: {blow.name} turned, but the shield shattered. "
                f"Durability exhausted.")
    return (f"DEFLECT: {blow.name} turned. "
            f"Durability -{cost:.2f} -> {shield.durability:.2f}.")


def choose(shield: Shield, blow: Blow) -> str:
    """The situational decision. Neither pole is doctrine."""
    # Not foreseen: the untrained reflex. Turn it if you can afford it.
    if not blow.foreseen:
        if blow.can_deflect and shield.durability > 0.5:
            return deflect(shield, blow)
        return absorb(shield, blow)

    # Foreseen. Can you even absorb this one?
    can_absorb = blow.severity <= shield.capacity

    # If it would fracture you and you can turn it, you must.
    if not can_absorb and blow.can_deflect:
        return deflect(shield, blow)
    # If the shield is thin, take a moderate blow to grow capacity back.
    if shield.durability < 0.35 and can_absorb:
        return absorb(shield, blow)
    # If you are already resilient enough, preserve the shield.
    if shield.resilience >= 0.5 and blow.can_deflect:
        return deflect(shield, blow)
    # Otherwise: absorb the moderate, deflect the large.
    if can_absorb and blow.severity <= 0.5:
        return absorb(shield, blow)
    if blow.can_deflect:
        return deflect(shield, blow)
    return absorb(shield, blow)


DEMO_BLOWS = [
    Blow("a foreseen insult", 0.4, foreseen=True),
    Blow("a blind betrayal", 0.7, foreseen=False),
    Blow("a foreseen blow", 0.5, foreseen=True),
    Blow("a foreseen loss", 0.3, foreseen=True),
    Blow("a blind grief", 0.6, foreseen=False),
    Blow("a foreseen blow", 0.5, foreseen=True),
]


def run_policy(name, shield, fn, blows):
    print(f"\n[{name}]")
    for b in blows:
        print(f"  {fn(shield, b)}")
        if not shield.integrity:
            print(f"  -> BROKEN. shield {shield.durability:.2f}, "
                  f"resilience {shield.resilience:.2f}")
            return
    verdict = ("ENDURES" if shield.durability > 0.2 and shield.resilience > 0.2
               else "SURVIVED, ONE ROAD SHORT")
    print(f"  -> {verdict}. shield {shield.durability:.2f}, "
          f"resilience {shield.resilience:.2f}")


def demonstrate() -> int:
    print("=" * 72)
    print("THE HOLY SHIELD — deflect, absorb, or ration?")
    print("=" * 72)
    run_policy("I. Deflect everything (two lives)", Shield(), deflect, DEMO_BLOWS * 2)
    run_policy("II. Absorb everything", Shield(), absorb, DEMO_BLOWS)
    run_policy("III. The ration", Shield(), choose, DEMO_BLOWS)
    run_policy("IV. The ego's absorption", Shield(motive="prove"), absorb, DEMO_BLOWS)
    print("=" * 72)
    return 0


class Tests(unittest.TestCase):
    def test_deflect_everything_wears_out(self):
        s = Shield()
        for b in DEMO_BLOWS * 2:
            deflect(s, b)
            if not s.integrity:
                break
        self.assertFalse(s.integrity)

    def test_absorb_everything_fractures(self):
        s = Shield()
        self.assertIn("FRACTURE", absorb(s, Blow("blind betrayal", 0.7)))
        self.assertFalse(s.integrity)

    def test_ration_endures(self):
        s = Shield()
        for b in DEMO_BLOWS:
            choose(s, b)
        self.assertTrue(s.integrity)
        self.assertGreater(s.durability, 0.2)
        self.assertGreater(s.resilience, 0.2)

    def test_reflex_turns_a_blind_blow(self):
        s = Shield()
        choose(s, Blow("huge blind", 0.9, foreseen=False))
        self.assertTrue(s.integrity)  # reflex turned it; did not eat it

    def test_v4_foreseen_deflect_that_empties_shield_cracks(self):
        s = Shield(durability=0.03)
        result = choose(s, Blow("x", 0.9, foreseen=True))
        self.assertIn("CRACKED", result)
        self.assertFalse(s.integrity)

    def test_undeflectable_large_blow_lands_and_fractures(self):
        s = Shield()
        result = deflect(s, Blow("unturnable", 0.9, can_deflect=False))
        self.assertIn("NO DEFLECT", result)
        self.assertIn("FRACTURE", result)
        self.assertFalse(s.integrity)
        self.assertEqual(s.durability, 1.0)  # the shield was never touched

    def test_undeflectable_small_blow_lands_and_grows(self):
        s = Shield()
        result = deflect(s, Blow("a small unavoidable loss", 0.3, can_deflect=False))
        self.assertIn("ABSORB (grow)", result)
        self.assertTrue(s.integrity)
        self.assertGreater(s.resilience, 0.0)

    def test_prove_motive_breaks_integrity(self):
        s = Shield(motive="prove")
        absorb(s, Blow("show them", 0.3))
        self.assertFalse(s.integrity)

    def test_small_undeflectable_is_absorbed(self):
        s = Shield()
        absorb(s, Blow("a small unavoidable loss", 0.3, can_deflect=False))
        self.assertTrue(s.integrity)
        self.assertGreater(s.resilience, 0.0)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="The holy shield.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    if args.test:
        return run_tests()
    return demonstrate()


if __name__ == "__main__":
    sys.exit(main())
