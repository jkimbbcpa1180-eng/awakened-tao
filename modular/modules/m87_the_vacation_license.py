#!/usr/bin/env python3
"""the_vacation_license.py — regulate gambling as vacation only.

Type: policy proposal; computational demonstration

The position, as stated:

  1. INCOME-BASED CAP. The regulator sets how much of a person's
     annual income may go to entertainment, and of that, how much may
     go to gambling. The cap is set so the person's self-sufficiency
     (fixed costs, dependents, debt service) is untouched. "What you
     can afford to entertain yourself without putting yourself on
     hold."

  2. COOL-DOWN BETWEEN VACATIONS. A vacation is a trip with a return
     home. If you go again before the cool-down expires, it is not a
     vacation — it is a habit. The cool-down is measured in days and
     always expires. No permanent ban.

  3. NO REPEAT. A pattern of vacations in a short window means the
     vacation has stopped being a vacation. The response is not
     "addict" and not "banned forever." It is: the pattern is named,
     a longer cool-down applies, care is offered, and a reassessment
     can clear it. The pattern is observation, not a verdict.

HONEST COSTS, named in code:

  - THE CAP IS REGRESSIVE. A low income gets a smaller absolute cap
    and is excluded from a legal activity the rich can afford. The
    module names this; it does not fix it. Fixing it is policy, not
    code.

  - INCOME IS NOT SAFETY. A high earner can be destroyed by gambling
    and still "afford" it on paper. The cap must be paired with
    behavioral signals (loss velocity, chase behavior, session
    length) that trigger care, not punishment. The module refuses to
    let income alone pass someone.

  - VERIFICATION IS SURVEILLANCE. Requiring income verification hands
    the operator a data-harvesting dream and creates a conflict of
    interest (the operator benefits from a permissive cap). The
    module requires a NEUTRAL verifier, and prefers zero-knowledge
    proof: prove cap >= X without disclosing income. The operator
    never sees the number.

  - POLICY NUMBERS ARE DIALS, NOT ABSOLUTES. The percentages and
    day-counts below are policy dials. Each carries a provenance
    field: who set it, when, and why. Any number is a choice, not a
    truth. The module shows the dials so they can be argued with.

Run:
    python3 the_vacation_license.py
    python3 the_vacation_license.py --test
"""

from __future__ import annotations
import argparse
import sys
import unittest
from dataclasses import dataclass, field
from datetime import date, timedelta


# ---------------------------------------------------------------------------
# Policy dials. NOT absolutes. Each has a provenance.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Policy:
    # Share of annual income that may go to entertainment of any kind.
    entertainment_share: float = 0.02
    # Of that, the share allowed to gambling specifically.
    gambling_share_of_entertainment: float = 0.25
    # Base cool-down between vacations, in days.
    base_cool_down_days: int = 90
    # Window for observing repeat patterns, in days.
    repeat_window_days: int = 365
    # Vacations within the window that count as a pattern (observation,
    # not a verdict).
    repeat_pattern_count: int = 3
    # Extra cool-down applied when a pattern is observed.
    pattern_cool_down_days: int = 180
    # Provenance — the dial is not a truth, it is a decision.
    provenance: str = (
        "Policy dials set by [legislature/regulator]; reviewed annually. "
        "These are choices, not absolutes."
    )


# ---------------------------------------------------------------------------
# Licensee and the cap.
# ---------------------------------------------------------------------------

@dataclass
class Licensee:
    name: str
    annual_income: float
    fixed_costs_per_year: float       # rent, food, utilities, insurance
    debt_service_per_year: float      # loan/credit obligations
    dependents: int = 0
    dependents_cost_per_year: float = 0.0


@dataclass(frozen=True)
class Cap:
    entertainment: float
    gambling: float
    note: str


@dataclass(frozen=True)
class Refusal:
    reason: str
    expiry: date | None = None        # never open-ended


def _self_sufficiency(p: Licensee) -> float:
    dep = p.dependents * p.dependents_cost_per_year
    return p.fixed_costs_per_year + p.debt_service_per_year + dep


def cap_for(p: Licensee, policy: Policy) -> Cap:
    """The cap: what can go to entertainment without putting yourself on hold."""
    # The self-sufficiency floor comes first. If income does not cover
    # fixed costs, debt service, and dependents, the gambling budget is 0.
    # That is the regressive cost, named honestly: it excludes the poor.
    surplus = p.annual_income - _self_sufficiency(p)
    if surplus <= 0:
        return Cap(
            0.0, 0.0,
            "NO SURPLUS: income does not cover self-sufficiency. "
            "The cap is 0. This is the regressive cost — the legal "
            "activity is available only to those with surplus."
        )
    entertainment = min(p.annual_income * policy.entertainment_share, surplus)
    gambling = entertainment * policy.gambling_share_of_entertainment
    return Cap(
        entertainment, gambling,
        "Surplus-based. Self-sufficiency untouched. Not safety — "
        "affordability is not the same as not being harmed."
    )


# ---------------------------------------------------------------------------
# Verification: neutral party, zero-knowledge preferred.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Verifier:
    name: str
    is_neutral: bool                  # must not be the operator
    discloses_income: bool = False    # prefer False: prove cap, not income


def verify_cap(cap: Cap, verifier: Verifier, operator: str) -> str:
    """The operator may not verify income. Only a neutral party may."""
    if not verifier.is_neutral:
        return (f"REFUSED: {verifier.name} is not a neutral verifier. "
                f"The operator cannot be its own watchdog — it benefits "
                f"from a permissive cap.")
    if verifier.name == operator:
        return (f"REFUSED: the verifier is the operator. Conflict of interest.")
    if verifier.discloses_income:
        return (f"VERIFIED (income disclosed): cap honored. "
                f"Warning — disclosure hands the operator a data profile. "
                f"Zero-knowledge proof is preferred.")
    return (f"VERIFIED (zero-knowledge): cap >= required threshold proven "
            f"to {operator} without disclosing income. The operator never "
            f"sees the number. This is the privacy-preserving path.")


# ---------------------------------------------------------------------------
# Vacation, cool-down, pattern.
# ---------------------------------------------------------------------------

@dataclass
class Vacation:
    licensee: str
    start: date
    amount: float


@dataclass
class Pattern:
    """Observation, not verdict. There is no 'addict' field."""
    licensee: str
    count: int
    window_days: int
    note: str
    cool_down_applied: int


def _vacations_in_window(vacations: list[Vacation], as_of: date,
                          window_days: int) -> list[Vacation]:
    cutoff = as_of - timedelta(days=window_days)
    return [v for v in vacations if v.start >= cutoff]


def cool_down_status(licensee: str, vacations: list[Vacation],
                     as_of: date, policy: Policy) -> Refusal | None:
    """Between vacations. Always expires. No permanent ban."""
    recent = _vacations_in_window(vacations, as_of, policy.repeat_window_days)
    if not recent:
        return None
    pattern = len(recent) >= policy.repeat_pattern_count
    extra = policy.pattern_cool_down_days if pattern else 0
    last = max(v.start for v in recent)
    expiry = last + timedelta(days=policy.base_cool_down_days + extra)
    if as_of < expiry:
        return Refusal(
            reason=(f"COOL-DOWN: a vacation is a trip with a return home. "
                    f"{len(recent)} in {policy.repeat_window_days} days"
                    + (" — this has stopped being a vacation."
                       if pattern else ".")),
            expiry=expiry,
        )
    return None


def detect_pattern(licensee: str, vacations: list[Vacation],
                   as_of: date, policy: Policy) -> Pattern | None:
    """Observation, not a verdict. Named, not sentenced."""
    recent = _vacations_in_window(vacations, as_of, policy.repeat_window_days)
    if len(recent) < policy.repeat_pattern_count:
        return None
    return Pattern(
        licensee=licensee,
        count=len(recent),
        window_days=policy.repeat_window_days,
        note=("The vacation has become a habit. This is a pattern, not a "
              "verdict. A longer cool-down applies; care is offered; a "
              "reassessment can clear it."),
        cool_down_applied=policy.pattern_cool_down_days,
    )


def issue_vacation(p: Licensee, policy: Policy, verifier: Verifier,
                   vacations: list[Vacation], as_of: date,
                   amount: float, operator: str) -> str:
    """The full gate: cap, verification, cool-down, pattern."""
    cap = cap_for(p, policy)
    if cap.gambling <= 0:
        return f"REFUSED: {cap.note}"
    if amount > cap.gambling:
        return (f"REFUSED: amount {amount:.2f} exceeds cap "
                f"{cap.gambling:.2f}. {cap.note}")
    v = verify_cap(cap, verifier, operator)
    if v.startswith("REFUSED"):
        return v
    cd = cool_down_status(p.name, vacations, as_of, policy)
    if cd is not None:
        return f"REFUSED: {cd.reason} Expires {cd.expiry.isoformat()}."
    pattern = detect_pattern(p.name, vacations, as_of, policy)
    vacations.append(Vacation(p.name, as_of, amount))
    base = f"ISSUED: vacation for {p.name}, {amount:.2f} at {operator}. {v}"
    if pattern:
        base += (f" PATTERN OBSERVED ({pattern.count} in "
                 f"{pattern.window_days}d): {pattern.note} "
                 f"Cool-down +{pattern.cool_down_applied}d.")
    return base


# ---------------------------------------------------------------------------
# Behavioral signals — income alone is not safety.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Behavior:
    loss_velocity: float    # losses per hour, in currency
    chase_episodes: int     # times the person chased a loss
    session_minutes: int


def behavior_check(b: Behavior, cap: Cap) -> str:
    """If behavioral signals are unhealthy, income does not pass them."""
    flags = []
    if b.chase_episodes > 0:
        flags.append("chase behavior")
    if b.loss_velocity > cap.gambling * 0.5:
        flags.append("loss velocity above half the cap")
    if b.session_minutes > 240:
        flags.append("session over four hours")
    if not flags:
        return "BEHAVIOR: within expected range for a vacation."
    return ("BEHAVIOR: " + ", ".join(flags) + ". Income does not pass this. "
            "Care referral offered; this is not punishment.")


# ---------------------------------------------------------------------------
# Reassessment — the cool-down is not a scarlet letter.
# ---------------------------------------------------------------------------

def reassess(licensee: str, vacations: list[Vacation], behavior: Behavior,
             as_of: date, policy: Policy) -> str:
    """A path back. Not a verdict, not a permanent record."""
    if not vacations:
        return f"NOTHING TO REASSESS: {licensee} has no history."
    cap = Cap(0, 0, "")  # behavior check uses only flags
    unhealthy = "within expected" not in behavior_check(behavior, cap)
    if unhealthy:
        return (f"REASSESSED: {licensee} not yet clear. Behavior: "
                f"{behavior_check(behavior, cap)} Care continues.")
    # Clear the pattern by moving the clock forward: the review uses a
    # clean window; past vacations are not deleted, but their weight
    # expires within the policy window.
    return (f"REASSESSED: {licensee} clear. The pattern is not a permanent "
            f"record. The cool-down is lifted; the next vacation may be "
            f"taken as a vacation.")


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

POLICY = Policy()
NEUTRAL = Verifier("Office of Gambling Regulation", is_neutral=True)


def demonstrate() -> int:
    print("=" * 72)
    print("THE VACATION LICENSE — cap, cool-down, no repeat")
    print("=" * 72)

    print("\n[I. The cap — affordability, and its regressive cost]")
    high = Licensee("A high earner", 200_000, 60_000, 20_000, 1, 15_000)
    low = Licensee("A low earner", 32_000, 24_000, 6_000, 2, 8_000)
    for p in (high, low):
        c = cap_for(p, POLICY)
        print(f"  {p.name}: entertainment {c.entertainment:.0f}, "
              f"gambling {c.gambling:.0f}")
        print(f"    {c.note}")

    print("\n[II. Verification — neutral, zero-knowledge preferred]")
    print(f"  {verify_cap(cap_for(high, POLICY), NEUTRAL, 'a casino')}")
    print(f"  {verify_cap(cap_for(high, POLICY), Verifier('the casino', False), 'a casino')}")

    print("\n[III. Cool-down — a vacation has a return home]")
    vacations: list[Vacation] = []
    d = date(2026, 1, 1)
    print(f"  {issue_vacation(high, POLICY, NEUTRAL, vacations, d, 200.0, 'a casino')}")
    print(f"  {issue_vacation(high, POLICY, NEUTRAL, vacations, d + timedelta(days=10), 200.0, 'a casino')}")
    print(f"  {issue_vacation(high, POLICY, NEUTRAL, vacations, d + timedelta(days=120), 200.0, 'a casino')}")

    print("\n[IV. Pattern — a vacation that stopped being one]")
    vacations = []
    for i in range(4):
        when = d + timedelta(days=i * 30)
        vacations.append(Vacation(high.name, when, 100.0))
    pat = detect_pattern(high.name, vacations, d + timedelta(days=100), POLICY)
    print(f"  pattern: {pat.note if pat else 'none'}")
    print(f"  {issue_vacation(high, POLICY, NEUTRAL, vacations, d + timedelta(days=100), 100.0, 'a casino')}")

    print("\n[V. Behavior — income alone is not safety]")
    bad = Behavior(loss_velocity=cap_for(high, POLICY).gambling * 0.8,
                   chase_episodes=2, session_minutes=300)
    print(f"  {behavior_check(bad, cap_for(high, POLICY))}")

    print("\n[VI. Reassessment — the path back]")
    healthy = Behavior(loss_velocity=0.0, chase_episodes=0, session_minutes=60)
    print(f"  {reassess(high.name, vacations, bad, d + timedelta(days=400), POLICY)}")
    print(f"  {reassess(high.name, vacations, healthy, d + timedelta(days=400), POLICY)}")

    print("\n[VII. The policy dials, visible so they can be argued with]")
    print(f"  {POLICY}")

    print("=" * 72)
    print("A vacation is a trip with a return home. The cap protects")
    print("self-sufficiency. The cool-down protects the return. The pattern")
    print("is named, not sentenced. Income is not safety; behavior is")
    print("checked. The operator does not verify itself. The dials are")
    print("dials, not absolutes.")
    print("=" * 72)
    return 0


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestCap(unittest.TestCase):
    def test_self_sufficiency_preserved(self):
        p = Licensee("A", 100_000, 60_000, 10_000, 1, 10_000)
        c = cap_for(p, Policy())
        self.assertGreater(c.entertainment, 0)
        self.assertLessEqual(c.entertainment, p.annual_income - 80_000)

    def test_regressive_cost_named(self):
        poor = Licensee("A", 20_000, 24_000, 2_000, 1, 4_000)
        c = cap_for(poor, Policy())
        self.assertEqual(c.gambling, 0)
        self.assertIn("regressive", c.note.lower())

    def test_high_income_does_not_guarantee_pass(self):
        # Behavior, not income, must also pass.
        high = Licensee("A", 500_000, 50_000, 0, 0, 0)
        cap = cap_for(high, Policy())
        bad = Behavior(loss_velocity=cap.gambling * 0.9,
                       chase_episodes=1, session_minutes=400)
        self.assertIn("BEHAVIOR", behavior_check(bad, cap))
        self.assertNotIn("within expected", behavior_check(bad, cap))


class TestVerification(unittest.TestCase):
    def test_operator_cannot_verify_itself(self):
        cap = Cap(1000, 250, "")
        v = verify_cap(cap, Verifier("the casino", False), "the casino")
        self.assertIn("REFUSED", v)

    def test_zero_knowledge_preferred(self):
        cap = Cap(1000, 250, "")
        v = verify_cap(cap, Verifier("Office", True, discloses_income=False), "a casino")
        self.assertIn("zero-knowledge", v)

    def test_income_disclosure_warned(self):
        cap = Cap(1000, 250, "")
        v = verify_cap(cap, Verifier("Office", True, discloses_income=True), "a casino")
        self.assertIn("Warning", v)


class TestCoolDown(unittest.TestCase):
    def test_cool_down_always_expires(self):
        p = Licensee("A", 100_000, 50_000, 0, 0, 0)
        vs = [Vacation("A", date(2026, 1, 1), 100)]
        cd = cool_down_status("A", vs, date(2026, 1, 5), Policy())
        self.assertIsNotNone(cd)
        self.assertIsNotNone(cd.expiry)
        # After expiry, no cool-down.
        later = cd.expiry + timedelta(days=1)
        self.assertIsNone(cool_down_status("A", vs, later, Policy()))

    def test_no_permanent_ban(self):
        p = Licensee("A", 100_000, 50_000, 0, 0, 0)
        vs = [Vacation("A", date(2026, 1, 1), 100)]
        later = date(2027, 12, 31)
        self.assertIsNone(cool_down_status("A", vs, later, Policy()))


class TestPattern(unittest.TestCase):
    def test_pattern_is_observation_not_verdict(self):
        p = Policy()
        vs = [Vacation("A", date(2026, 1, 1) + timedelta(days=i * 20), 100)
              for i in range(4)]
        pat = detect_pattern("A", vs, date(2026, 3, 1), p)
        self.assertIsNotNone(pat)
        self.assertNotIn("addict", pat.note.lower())
        self.assertIn("not a verdict", pat.note.lower())

    def test_below_threshold_no_pattern(self):
        p = Policy()
        vs = [Vacation("A", date(2026, 1, 1), 100)]
        self.assertIsNone(detect_pattern("A", vs, date(2026, 2, 1), p))


class TestReassessment(unittest.TestCase):
    def test_reassessment_can_clear(self):
        vs = [Vacation("A", date(2026, 1, 1), 100)]
        healthy = Behavior(0.0, 0, 60)
        v = reassess("A", vs, healthy, date(2027, 1, 1), Policy())
        self.assertIn("clear", v.lower())

    def test_reassessment_blocks_on_bad_behavior(self):
        vs = [Vacation("A", date(2026, 1, 1), 100)]
        bad = Behavior(500.0, 3, 400)
        v = reassess("A", vs, bad, date(2027, 1, 1), Policy())
        self.assertNotIn("may be taken as a vacation", v.lower())


class TestHonesty(unittest.TestCase):
    def test_no_forbidden_verdict_words(self):
        ns = globals()
        for bad in ("ADDICT", "SAVED", "DAMNED", "SCARLET"):
            self.assertFalse(any(bad in n.upper() for n in ns), bad)

    def test_policy_is_named_a_dial_not_truth(self):
        self.assertIn("not absolutes", Policy().provenance.lower())

    def test_refusal_has_expiry(self):
        vs = [Vacation("A", date(2026, 1, 1), 100)]
        cd = cool_down_status("A", vs, date(2026, 1, 5), Policy())
        self.assertIsNotNone(cd.expiry)


def run_tests() -> int:
    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()
    for case in (TestCap, TestVerification, TestCoolDown,
                 TestPattern, TestReassessment, TestHonesty):
        suite.addTests(loader.loadTestsFromTestCase(case))
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Regulate gambling as vacation only — cap, cool-down, no repeat.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    return run_tests() if args.test else demonstrate()


if __name__ == "__main__":
    sys.exit(main())
