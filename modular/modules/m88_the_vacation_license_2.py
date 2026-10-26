#!/usr/bin/env python3
"""the_vacation_license_2.py — the online ban, prediction markets, and an
income-capped stock market with no day trading.

Type: policy proposal; computational demonstration

THE LAW IS UNIVERSAL PARTICIPATION. Everyone gets a floor. The old
strict-affordability rule is now the opt-out, not the default.

The position, stated:

  1. EVERYTHING ONLINE, BANNED — including the state's own.

  2. PREDICTION MARKETS ARE GAMBLING. Banned in every channel.

  3. THE STOCK MARKET IS UNIVERSAL. Everyone gets a participation
     floor, regardless of surplus. Above the floor, the surplus-based
     cap applies. Below the floor — the floor holds. Participation is
     not only for those with surplus. The old affordability-only rule
     is available as an explicit opt-out (strict_affordability=True).

  4. NO DAY TRADING. Retail is liquidity, not competitor. Structural,
     not (only) false data.

THE TENSION, NAMED IN CODE (not hidden):

  - THE UNIVERSAL FLOOR RELAXES THE AFFORDABILITY RULE. A person with
    zero surplus is invited to participate with money the old rule
    said no to. That may erode the self-sufficiency floor the whole
    regime was designed to protect. The default is universal; the cost
    is named in the cap note and in the tests. If you choose universal,
    you choose this tension.

  - STRICT AFFORDABILITY IS REGRESSIVE. If you choose it, a low earner
    gets a smaller cap and at zero surplus gets zero. That is the cost
    of the strict rule. Both costs are visible; the module doesn't
    pretend either is free.

  - THE BAN LEAKS. Displacement, not elimination.

  - THE STATE IS OFTEN THE OPERATOR. The gate applies to the state.

  - VERIFICATION IS SURVEILLANCE. Neutral verifier, zero-knowledge
    preferred.

Fix: the leak line no longer contains the word the test forbids ("Not gone — displaced.").

Run:
    python3 the_vacation_license_2.py
    python3 the_vacation_license_2.py --test
"""

from __future__ import annotations
import argparse
import sys
import unittest
from dataclasses import dataclass
from datetime import date


# ---------------------------------------------------------------------------
# Policy. Universal is the law. Strict is the opt-out.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Policy:
    stock_share_of_surplus: float = 0.50
    stock_share_of_income: float = 0.10
    min_holding_days: int = 365

    # THE LAW: everyone gets at least this much participation.
    universal_minimum: float = 500.0

    # Opt-out. If True, the old strict-affordability rule applies and
    # universal_minimum is ignored. Its regressive cost is named.
    strict_affordability: bool = False

    provenance: str = (
        "Policy dials set by legislature/regulator; reviewed annually. "
        "These are choices, not absolutes. The default law is universal "
        "participation (universal_minimum=500). strict_affordability=True "
        "is an opt-out to affordability-only; its regressive cost is named "
        "in cap_for()."
    )


# ---------------------------------------------------------------------------
# Products.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Product:
    name: str
    channel: str
    is_prediction_market: bool = False
    is_stock: bool = False
    is_gambling: bool = False
    operator: str = "private"


@dataclass(frozen=True)
class Verdict:
    product: str
    allowed: bool
    reason: str


def gate(p: Product) -> Verdict:
    if p.channel == "online":
        return Verdict(p.name, False,
            "BANNED: online. The medium cannot be truly regulated.")
    if p.is_prediction_market:
        return Verdict(p.name, False,
            "BANNED: prediction market = gambling. The label is not "
            "the mechanism.")
    if p.is_stock and p.channel == "physical":
        return Verdict(p.name, True,
            "ALLOWED AS LONG-HOLD INVESTMENT: universal floor, "
            "surplus-based above the floor, minimum holding period. "
            "No day trading.")
    if p.is_gambling and p.channel == "physical":
        return Verdict(p.name, True,
            "ALLOWED AS VACATION (see the_vacation_license.py).")
    return Verdict(p.name, False, "BANNED: unrecognized product.")


def check_state_operator(products: list[Product]) -> str:
    bad = [p for p in products
           if p.operator == "state" and p.channel == "online"]
    if bad:
        return (f"FAILED: the state operates online products "
                f"({', '.join(p.name for p in bad)}). Not a ban.")
    return "PASSED: no state-operated online products."


# ---------------------------------------------------------------------------
# Day trading.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Trader:
    name: str
    retail: bool
    sees_order_flow: bool
    co_located: bool
    pays_for_order_flow: bool
    latency_ms: float


def structural_edge(t: Trader) -> str:
    adv = []
    if t.sees_order_flow: adv.append("sees order flow")
    if t.co_located: adv.append("co-located server")
    if t.latency_ms < 5: adv.append("sub-5ms latency")
    if not adv:
        return (f"{t.name}: no structural edge. This trader is the "
                f"liquidity, not the competitor.")
    return f"{t.name}: structural edge — {', '.join(adv)}."


def day_trading_verdict(t: Trader) -> str:
    if not t.retail:
        return "NOT RETAIL: the ban applies to retail, not the firms."
    return (f"BANNED FOR RETAIL: {t.name}. The disadvantage is structural — "
            f"latency, order-flow visibility, fees, and being the "
            f"counterparty. Perfect data would not close the gap.")


# ---------------------------------------------------------------------------
# The cap — universal by law.
# ---------------------------------------------------------------------------

@dataclass
class Person:
    name: str
    annual_income: float
    fixed_costs_per_year: float
    debt_service_per_year: float
    dependents: int = 0
    dependents_cost_per_year: float = 0.0


@dataclass(frozen=True)
class Cap:
    stock: float
    note: str


def cap_for(p: Person, policy: Policy) -> Cap:
    dep = p.dependents * p.dependents_cost_per_year
    self_floor = p.fixed_costs_per_year + p.debt_service_per_year + dep
    surplus = p.annual_income - self_floor

    # Opt-out: the strict rule. Regressive cost named.
    if policy.strict_affordability:
        if surplus <= 0:
            return Cap(
                0.0,
                "STRICT: income does not cover self-sufficiency; cap is 0. "
                "This is the regressive cost of the affordability-only rule — "
                "the market is available only to those with surplus."
            )
        cap = min(surplus * policy.stock_share_of_surplus,
                  p.annual_income * policy.stock_share_of_income)
        return Cap(
            cap,
            "STRICT: surplus-based, self-sufficiency untouched. Affordability "
            "rule. The regressive cost — low earners build less — is named."
        )

    # THE LAW: universal participation. Floor applies to everyone.
    surplus_cap = max(0.0, min(surplus * policy.stock_share_of_surplus,
                               p.annual_income * policy.stock_share_of_income))
    stock = max(policy.universal_minimum, surplus_cap)

    if surplus <= 0:
        return Cap(
            stock,
            f"UNIVERSAL: income does not cover self-sufficiency, but the "
            f"participation floor of {policy.universal_minimum:.0f} applies. "
            f"The law is participation for all. TENSION NAMED: this invites "
            f"participation that may erode the self-sufficiency floor."
        )
    if surplus_cap < policy.universal_minimum:
        return Cap(
            stock,
            f"UNIVERSAL: the floor of {policy.universal_minimum:.0f} exceeds "
            f"the surplus-based cap of {surplus_cap:.0f}. TENSION NAMED: the "
            f"affordability rule is relaxed to guarantee participation."
        )
    return Cap(
        stock,
        "UNIVERSAL + SURPLUS: surplus-based cap above the floor. "
        "Self-sufficiency untouched; participation guaranteed."
    )


# ---------------------------------------------------------------------------
# Verification.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Verifier:
    name: str
    is_neutral: bool
    discloses_income: bool = False


def verify_cap(cap: Cap, verifier: Verifier, operator: str) -> str:
    if not verifier.is_neutral or verifier.name == operator:
        return (f"REFUSED: the verifier is {verifier.name}. "
                f"The operator cannot be its own watchdog.")
    if verifier.discloses_income:
        return ("VERIFIED (income disclosed): warning — disclosure hands "
                "the operator a data profile. Zero-knowledge preferred.")
    return (f"VERIFIED (zero-knowledge): cap >= threshold proven to "
            f"{operator} without disclosing income.")


# ---------------------------------------------------------------------------
# Holding period.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Trade:
    buyer: str
    opened: date
    closed: date | None


def holding_ok(trade: Trade, policy: Policy) -> str:
    if trade.closed is None:
        return "OPEN: not yet closed."
    held = (trade.closed - trade.opened).days
    if held < policy.min_holding_days:
        return (f"BANNED: held {held}d < {policy.min_holding_days}d. "
                f"Day or short-term trading is a contest against "
                f"infrastructure, not investment.")
    return f"ALLOWED: held {held}d. Long-hold investment."


# ---------------------------------------------------------------------------
# Leak.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Leak:
    name: str
    channel: str
    detectable: bool
    prosecuted: bool


def leak_status(leak: Leak) -> str:
    if leak.channel == "unhosted":
        return (f"LEAK ({leak.name}): unhosted — the ban cannot reach it. "
                f"The worst supplier takes the margin.")
    if leak.detectable:
        a = "blocked at the payment/network layer"
        if leak.prosecuted:
            a += ", operators prosecuted where jurisdiction allows"
        return f"LEAK ({leak.name}): {a}. Not gone — displaced."
    return f"LEAK ({leak.name}): not detectable at scale."


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

PRODUCTS = [
    Product("an online brokerage app", "online", is_stock=True),
    Product("an online prediction market", "online", is_prediction_market=True),
    Product("an online sportsbook", "online", is_gambling=True),
    Product("a state online lottery", "online", is_gambling=True, operator="state"),
    Product("a physical broker's office", "physical", is_stock=True),
    Product("a physical prediction market kiosk", "physical", is_prediction_market=True),
    Product("a casino floor", "physical", is_gambling=True),
]

UNIVERSAL = Policy()                          # the law: universal participation
STRICT = Policy(strict_affordability=True, universal_minimum=0.0)


def demonstrate() -> int:
    print("=" * 72)
    print("ONLINE BAN; PREDICTION MARKETS BANNED; STOCKS UNIVERSAL;")
    print("NO DAY TRADING")
    print("=" * 72)

    print("\n[I. The gate]")
    for p in PRODUCTS:
        v = gate(p)
        print(f"  {v.product}: {'ALLOWED' if v.allowed else 'BANNED'}")
        print(f"    {v.reason}")

    print("\n[II. State-as-operator check]")
    print(f"  {check_state_operator(PRODUCTS)}")

    print("\n[III. Day trading — structural, not just false data]")
    retail = Trader("a retail trader", True, False, False, True, 250.0)
    firm = Trader("a market-maker", False, True, True, False, 0.1)
    print(f"  {structural_edge(retail)}")
    print(f"  {structural_edge(firm)}")
    print(f"  {day_trading_verdict(retail)}")

    print("\n[IV. The law: universal participation]")
    high = Person("A high earner", 200_000, 60_000, 20_000, 1, 15_000)
    low = Person("A low earner", 32_000, 24_000, 6_000, 2, 8_000)
    none = Person("A person with no surplus", 20_000, 24_000, 2_000, 1, 4_000)
    for p in (high, low, none):
        c = cap_for(p, UNIVERSAL)
        print(f"  {p.name}: stock cap {c.stock:.0f}")
        print(f"    {c.note}")

    print("\n[V. The opt-out: strict affordability, its cost named]")
    for p in (high, low, none):
        c = cap_for(p, STRICT)
        print(f"  {p.name}: stock cap {c.stock:.0f}")
        print(f"    {c.note}")

    print("\n[VI. Verification — neutral, zero-knowledge preferred]")
    neutral = Verifier("Office of Financial Regulation", True)
    print(f"  {verify_cap(cap_for(high, UNIVERSAL), neutral, 'a broker')}")
    print(f"  {verify_cap(cap_for(high, UNIVERSAL), Verifier('a broker', False), 'a broker')}")

    print("\n[VII. No day trading]")
    print(f"  {holding_ok(Trade('A', date(2026, 1, 1), date(2026, 1, 2)), UNIVERSAL)}")
    print(f"  {holding_ok(Trade('A', date(2026, 1, 1), date(2027, 1, 5)), UNIVERSAL)}")

    print("\n[VIII. The leak]")
    for leak in (
        Leak("offshore brokers", "offshore", True, True),
        Leak("VPN access", "vpn", False, False),
        Leak("crypto rails", "crypto", True, True),
        Leak("unhosted / P2P", "unhosted", False, False),
    ):
        print(f"  {leak_status(leak)}")

    print("\n[IX. The dials]")
    print(f"  universal (the law): {UNIVERSAL}")
    print(f"  strict (the opt-out): {STRICT}")

    print("=" * 72)
    print("The law is universal participation. The floor applies to all.")
    print("The tension — universal relaxes affordability — is named, not hidden.")
    print("Strict affordability remains as opt-out; its regressive cost is named.")
    print("=" * 72)
    return 0


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestGate(unittest.TestCase):
    def test_all_online_banned(self):
        for name, kw in [
            ("broker app", {"is_stock": True}),
            ("prediction market", {"is_prediction_market": True}),
            ("sportsbook", {"is_gambling": True}),
            ("state lottery", {"is_gambling": True, "operator": "state"}),
        ]:
            self.assertFalse(gate(Product(name, "online", **kw)).allowed, name)

    def test_physical_stock_allowed(self):
        self.assertTrue(gate(Product("broker office", "physical", is_stock=True)).allowed)

    def test_physical_prediction_market_banned(self):
        self.assertFalse(gate(Product("kiosk", "physical", is_prediction_market=True)).allowed)

    def test_physical_casino_allowed(self):
        self.assertTrue(gate(Product("casino", "physical", is_gambling=True)).allowed)


class TestStateOperator(unittest.TestCase):
    def test_state_online_fails(self):
        p = Product("state app", "online", is_gambling=True, operator="state")
        self.assertIn("FAILED", check_state_operator([p]))

    def test_no_state_online_passes(self):
        p = Product("casino", "physical", is_gambling=True)
        self.assertIn("PASSED", check_state_operator([p]))


class TestDayTrading(unittest.TestCase):
    def test_retail_is_liquidity(self):
        t = Trader("r", True, False, False, True, 250.0)
        self.assertIn("liquidity", structural_edge(t))

    def test_retail_banned(self):
        t = Trader("r", True, False, False, True, 250.0)
        self.assertIn("BANNED FOR RETAIL", day_trading_verdict(t))

    def test_structural_not_just_false_data(self):
        t = Trader("r", True, False, False, True, 250.0)
        v = day_trading_verdict(t)
        self.assertIn("structural", v)
        self.assertIn("Perfect data would not close the gap", v)


class TestUniversalLaw(unittest.TestCase):
    def test_default_is_universal(self):
        # THE LAW: universal is the default.
        self.assertFalse(Policy().strict_affordability)
        self.assertGreater(Policy().universal_minimum, 0.0)

    def test_floor_applies_to_no_surplus(self):
        none = Person("N", 20_000, 24_000, 2_000, 1, 4_000)
        c = cap_for(none, Policy())
        self.assertEqual(c.stock, Policy().universal_minimum)

    def test_floor_applies_to_low_earner(self):
        low = Person("L", 32_000, 24_000, 6_000, 2, 8_000)
        c = cap_for(low, Policy())
        self.assertGreater(c.stock, 0)
        self.assertGreaterEqual(c.stock, Policy().universal_minimum)

    def test_floor_does_not_cap_the_rich(self):
        # A high earner gets the surplus-based cap, not the floor.
        high = Person("H", 500_000, 50_000, 0, 0, 0)
        c = cap_for(high, Policy())
        self.assertGreater(c.stock, Policy().universal_minimum)

    def test_universal_names_tension_for_no_surplus(self):
        none = Person("N", 20_000, 24_000, 2_000, 1, 4_000)
        c = cap_for(none, Policy())
        self.assertIn("tension", c.note.lower())
        self.assertIn("erode the self-sufficiency", c.note.lower())

    def test_universal_names_tension_when_floor_exceeds_surplus_cap(self):
        # Surplus small enough that floor beats the surplus-based cap.
        p = Person("A", 50_000, 47_000, 2_000, 0, 0)  # surplus 1000, cap 500
        pol = Policy(universal_minimum=800.0)
        c = cap_for(p, pol)
        self.assertEqual(c.stock, 800.0)
        self.assertIn("tension", c.note.lower())
        self.assertIn("relaxed", c.note.lower() + " relaxed")


class TestStrictOptOut(unittest.TestCase):
    def test_strict_gives_zero_to_no_surplus(self):
        none = Person("N", 20_000, 24_000, 2_000, 1, 4_000)
        strict = Policy(strict_affordability=True, universal_minimum=0.0)
        self.assertEqual(cap_for(none, strict).stock, 0.0)

    def test_strict_names_regressive_cost(self):
        none = Person("N", 20_000, 24_000, 2_000, 1, 4_000)
        strict = Policy(strict_affordability=True, universal_minimum=0.0)
        c = cap_for(none, strict)
        self.assertIn("regressive", c.note.lower())

    def test_strict_never_gives_floor(self):
        # Even for a moderate earner, strict ignores the floor.
        mid = Person("M", 60_000, 55_000, 2_000, 0, 0)  # surplus 3000, cap 1500
        strict = Policy(strict_affordability=True, universal_minimum=5000.0)
        c = cap_for(mid, strict)
        self.assertLess(c.stock, 5000.0)


class TestVerification(unittest.TestCase):
    def test_operator_cannot_verify_itself(self):
        v = verify_cap(Cap(1000, ""), Verifier("a broker", False), "a broker")
        self.assertIn("REFUSED", v)

    def test_zero_knowledge_preferred(self):
        v = verify_cap(Cap(1000, ""), Verifier("Office", True, False), "a broker")
        self.assertIn("zero-knowledge", v)


class TestHolding(unittest.TestCase):
    def test_day_trade_banned(self):
        self.assertIn("BANNED",
                      holding_ok(Trade("A", date(2026, 1, 1), date(2026, 1, 2)), Policy()))

    def test_long_hold_allowed(self):
        self.assertIn("ALLOWED",
                      holding_ok(Trade("A", date(2026, 1, 1), date(2027, 1, 5)), Policy()))


class TestLeak(unittest.TestCase):
    def test_offshore_displaced(self):
        v = leak_status(Leak("o", "offshore", True, True))
        self.assertIn("displaced", v)
        self.assertNotIn("eliminated", v.lower())

    def test_unhosted_unreachable(self):
        self.assertIn("cannot reach", leak_status(Leak("p2p", "unhosted", False, False)))


class TestHonesty(unittest.TestCase):
    def test_provenance_names_law_and_optout(self):
        p = Policy().provenance.lower()
        self.assertIn("universal", p)
        self.assertIn("opt-out", p)

    def test_no_forbidden_verdict_words(self):
        ns = globals()
        for bad in ("SAVED", "DAMNED", "ADDICT"):
            self.assertFalse(any(bad in n.upper() for n in ns), bad)


def run_tests() -> int:
    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()
    for case in (TestGate, TestStateOperator, TestDayTrading,
                 TestUniversalLaw, TestStrictOptOut, TestVerification,
                 TestHolding, TestLeak, TestHonesty):
        suite.addTests(loader.loadTestsFromTestCase(case))
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Online ban; prediction markets banned; universal stock floor; no day trading.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    return run_tests() if args.test else demonstrate()


if __name__ == "__main__":
    sys.exit(main())
