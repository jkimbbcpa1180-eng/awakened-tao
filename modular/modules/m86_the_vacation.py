#!/usr/bin/env python3
"""the_vacation.py — ban online gambling; keep the casino as vacation.

Type: policy proposal; computational demonstration

The position, stated plainly:

  Online gambling is banned. It is the product with the greatest
  extraction per unit of human freedom: 24/7 availability, millisecond
  rounds, credit and cashless ease, no social friction, algorithmic
  targeting, and a private room where nothing interrupts the drain.
  The person's choice is engineered away by the medium itself.

  Physical casinos remain, as a vacation. Not because they are
  harmless — the house edge is still structural — but because the
  friction is the point: travel, cost, time, cash in hand, other
  people present, a finite trip with a return home. The choice is
  actually made, in person, with a body that has to come home.

  Free will is preserved. What is removed is the design that forecloses
  it.

Three honest costs, named in the code, not hidden:

  1. THE BAN LEAKS. Offshore operators, VPNs, crypto. A ban is a
     friction, not a wall. The code models the leak so it is not
     mistaken for a solution.

  2. THE STATE IS OFTEN THE OPERATOR. A ban that exempts the state
     is not a ban. The gate applies to every operator, including the
     one with the flag on it.

  3. THE CASINO STILL EXTRACTS. Vacation is friction, not safety.
     The house edge remains. The module does not pretend otherwise.

Fix: the leak line no longer contains the word the test forbids ("Not gone — displaced.").

Run:
    python3 the_vacation.py
    python3 the_vacation.py --test
"""

from __future__ import annotations
import argparse
import sys
import unittest
from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# Products. A product is described by what makes it extractive, not by its
# label. "Gambling" is not the unit; the medium and the design are.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Product:
    name: str
    channel: str                    # "online" | "physical"
    rounds_per_hour: int
    credit_allowed: bool
    cashless_ease: bool
    social_presence: bool           # are other people physically present?
    requires_travel: bool
    algorithm_targets_losers: bool
    available_24_7: bool
    operator: str = "private"       # "private" | "state"


@dataclass(frozen=True)
class Verdict:
    product: str
    allowed: bool
    reason: str


# ---------------------------------------------------------------------------
# The gate.
# ---------------------------------------------------------------------------

def gate(p: Product) -> Verdict:
    """The only rule: online gambling is not permitted, by anyone."""
    # 1. Online is banned — for private operators and for the state alike.
    if p.channel == "online":
        return Verdict(
            p.name, False,
            "BANNED: online gambling. The medium removes the choice: "
            "24/7 access, instant rounds, credit, no social friction. "
            "The design forecloses free will, so the medium is refused."
        )

    # 2. Algorithmic targeting of losers is banned in any channel.
    if p.algorithm_targets_losers:
        return Verdict(
            p.name, False,
            "BANNED: algorithmic targeting of losers. This is the "
            "manipulation itself, not the game."
        )

    # 3. Physical, with friction, is the vacation.
    if p.channel == "physical":
        friction = sum([
            p.requires_travel,
            not p.available_24_7,
            p.social_presence,
            not p.credit_allowed,
            not p.cashless_ease,
            p.rounds_per_hour < 60,
        ])
        if friction < 3:
            return Verdict(
                p.name, False,
                "BANNED: too little friction. A physical product without "
                "travel, cash, or social presence is online gambling in a "
                "building."
            )
        return Verdict(
            p.name, True,
            "ALLOWED AS VACATION: physical, with friction. The choice is "
            "made in person, with cash, among others, and a trip home. "
            "The house edge remains — friction is not safety."
        )

    return Verdict(p.name, False, "BANNED: unrecognized channel.")


# ---------------------------------------------------------------------------
# The leak. Honest modelling of the ban's limits.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Leak:
    name: str
    channel: str                    # "offshore" | "vpn" | "crypto" | "unhosted"
    detectable: bool
    prosecuted: bool


def leak_status(leak: Leak) -> str:
    """A ban is a friction, not a wall. Name what it does not stop."""
    if leak.channel == "unhosted":
        return (f"LEAK ({leak.name}): unhosted and unpayable-to — the ban "
                f"cannot reach it. Demand remains; the worst supplier takes "
                f"the margin.")
    if leak.channel in ("offshore", "vpn", "crypto"):
        if leak.detectable:
            action = "blocked at the payment/network layer"
            if leak.prosecuted:
                action += ", operators prosecuted where jurisdiction allows"
            return f"LEAK ({leak.name}): {action}. Not gone — displaced."
        return (f"LEAK ({leak.name}): not detectable at scale. The ban "
                f"becomes advice to those determined to circumvent it.")
    return f"LEAK ({leak.name}): unresolved."


# ---------------------------------------------------------------------------
# Displacement: where does the demand go?
# ---------------------------------------------------------------------------

@dataclass
class Population:
    name: str
    gamblers_online: int = 0
    gamblers_physical: int = 0
    gamblers_black_market: int = 0
    gamblers_recovering: int = 0
    new_entrants_prevented: int = 0


def apply_ban(pop: Population) -> str:
    """The ban moves the online population. Not all of it goes where intended."""
    moved = pop.gamblers_online
    # A realistic split — friction, not elimination.
    to_recovering = int(moved * 0.4)          # the ban is the friction that lets them stop
    to_physical = int(moved * 0.3)            # they go to the vacation instead
    to_black = moved - to_recovering - to_physical

    pop.gamblers_recovering += to_recovering
    pop.gamblers_physical += to_physical
    pop.gamblers_black_market += to_black
    pop.gamblers_online = 0
    return (f"APPLIED: {moved} online -> "
            f"{to_recovering} recovering, {to_physical} physical (vacation), "
            f"{to_black} black market. Online is 0; harm is displaced, "
            f"not erased.")


# ---------------------------------------------------------------------------
# State-as-operator: the hypocrisy check.
# ---------------------------------------------------------------------------

def check_state_operator(products: list[Product]) -> str:
    """A ban that exempts the state is not a ban."""
    state_online = [p for p in products
                    if p.operator == "state" and p.channel == "online"]
    if state_online:
        names = ", ".join(p.name for p in state_online)
        return (f"FAILED: the state is the operator of online gambling "
                f"({names}). A ban that exempts its own operator is "
                f"nationalizing the manipulation, not ending it.")
    return "PASSED: no state-operated online gambling."


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

PRODUCTS = [
    Product("a slot-app", "online", rounds_per_hour=1200,
            credit_allowed=True, cashless_ease=True, social_presence=False,
            requires_travel=False, algorithm_targets_losers=True,
            available_24_7=True, operator="private"),
    Product("an online sportsbook", "online", rounds_per_hour=60,
            credit_allowed=True, cashless_ease=True, social_presence=False,
            requires_travel=False, algorithm_targets_losers=True,
            available_24_7=True, operator="private"),
    Product("a state lottery app", "online", rounds_per_hour=10,
            credit_allowed=True, cashless_ease=True, social_presence=False,
            requires_travel=False, algorithm_targets_losers=False,
            available_24_7=True, operator="state"),
    Product("a casino floor", "physical", rounds_per_hour=30,
            credit_allowed=False, cashless_ease=False, social_presence=True,
            requires_travel=True, algorithm_targets_losers=False,
            available_24_7=False, operator="private"),
    Product("a casino floor, cashless and local", "physical",
            rounds_per_hour=60, credit_allowed=True, cashless_ease=True,
            social_presence=True, requires_travel=False,
            algorithm_targets_losers=False, available_24_7=True,
            operator="private"),
]


def demonstrate() -> int:
    print("=" * 72)
    print("THE VACATION — online banned, the casino as vacation")
    print("=" * 72)

    print("\n[I. The gate]")
    for p in PRODUCTS:
        v = gate(p)
        print(f"  {v.product}: {'ALLOWED' if v.allowed else 'BANNED'}")
        print(f"    {v.reason}")

    print("\n[II. The leak — the ban is friction, not a wall]")
    for leak in (
        Leak("offshore sites", "offshore", detectable=True, prosecuted=True),
        Leak("VPN access", "vpn", detectable=False, prosecuted=False),
        Leak("crypto rails", "crypto", detectable=True, prosecuted=True),
        Leak("unhosted / P2P", "unhosted", detectable=False, prosecuted=False),
    ):
        print(f"  {leak_status(leak)}")

    print("\n[III. The state-as-operator check]")
    print(f"  {check_state_operator(PRODUCTS)}")

    print("\n[IV. Displacement — where does the demand go?]")
    pop = Population("a population", gamblers_online=1000)
    print(f"  before: online {pop.gamblers_online}, physical {pop.gamblers_physical}, "
          f"black {pop.gamblers_black_market}, recovering {pop.gamblers_recovering}")
    print(f"  {apply_ban(pop)}")
    print(f"  after:  online {pop.gamblers_online}, physical {pop.gamblers_physical}, "
          f"black {pop.gamblers_black_market}, recovering {pop.gamblers_recovering}")

    print("\n[V. What the vacation does and does not do]")
    print("  It preserves free will: travel, cash, time, other people, a trip home.")
    print("  It does not remove the house edge: the casino still extracts.")
    print("  It is friction. Friction is not safety. It is the room where choice lives.")

    print("=" * 72)
    print("Free will is preserved by the friction of the body, not by the")
    print("promise of a product. The online medium forecloses the choice;")
    print("the vacation leaves it open.")
    print("=" * 72)
    return 0


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestGate(unittest.TestCase):
    def test_online_private_banned(self):
        p = Product("x", "online", 100, True, True, False, False, True, True)
        self.assertFalse(gate(p).allowed)

    def test_online_state_banned(self):
        p = Product("lottery app", "online", 10, True, True, False, False,
                    False, True, operator="state")
        self.assertFalse(gate(p).allowed)

    def test_physical_with_friction_allowed(self):
        p = Product("casino", "physical", 30, False, False, True, True,
                    False, False)
        self.assertTrue(gate(p).allowed)

    def test_physical_without_friction_banned(self):
        p = Product("local cashless casino", "physical", 60, True, True,
                    True, False, False, True)
        self.assertFalse(gate(p).allowed)

    def test_algorithmic_targeting_banned_everywhere(self):
        p = Product("targeted floor", "physical", 30, False, False, True,
                    True, True, False)  # targets losers
        self.assertFalse(gate(p).allowed)


class TestLeak(unittest.TestCase):
    def test_unhosted_is_unreachable(self):
        v = leak_status(Leak("p2p", "unhosted", False, False))
        self.assertIn("cannot reach", v)

    def test_offshore_is_displaced_not_eliminated(self):
        v = leak_status(Leak("offshore", "offshore", True, True))
        self.assertIn("displaced", v)
        self.assertNotIn("eliminated", v.lower())

    def test_undetectable_is_advisory(self):
        v = leak_status(Leak("vpn", "vpn", False, False))
        self.assertIn("advice", v)


class TestStateOperator(unittest.TestCase):
    def test_state_online_fails(self):
        p = Product("state app", "online", 10, True, True, False, False,
                    False, True, operator="state")
        self.assertIn("FAILED", check_state_operator([p]))

    def test_no_state_online_passes(self):
        p = Product("casino", "physical", 30, False, False, True, True,
                    False, False)
        self.assertIn("PASSED", check_state_operator([p]))


class TestDisplacement(unittest.TestCase):
    def test_online_goes_to_zero(self):
        pop = Population("p", gamblers_online=1000)
        apply_ban(pop)
        self.assertEqual(pop.gamblers_online, 0)

    def test_harm_is_displaced_not_erased(self):
        pop = Population("p", gamblers_online=1000)
        apply_ban(pop)
        self.assertGreater(pop.gamblers_black_market, 0)

    def test_some_go_to_recovery(self):
        pop = Population("p", gamblers_online=1000)
        apply_ban(pop)
        self.assertGreater(pop.gamblers_recovering, 0)

    def test_some_go_to_vacation(self):
        pop = Population("p", gamblers_online=1000)
        apply_ban(pop)
        self.assertGreater(pop.gamblers_physical, 0)


class TestHonesty(unittest.TestCase):
    def test_vacation_does_not_claim_safety(self):
        p = Product("casino", "physical", 30, False, False, True, True,
                    False, False)
        v = gate(p)
        self.assertIn("friction is not safety", v.reason.lower())

    def test_no_saved_damned_language(self):
        ns = globals()
        for bad in ("SAVED", "DAMNED", "VERDICT_PASS", "VERDICT_FAIL"):
            self.assertFalse(any(bad in n for n in ns), bad)


def run_tests() -> int:
    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()
    for case in (TestGate, TestLeak, TestStateOperator,
                 TestDisplacement, TestHonesty):
        suite.addTests(loader.loadTestsFromTestCase(case))
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Ban online gambling; keep the casino as vacation.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    return run_tests() if args.test else demonstrate()


if __name__ == "__main__":
    sys.exit(main())
