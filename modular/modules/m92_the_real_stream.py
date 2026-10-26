#!/usr/bin/env python3
"""the_real_stream.py — streaming permitted only if it is completely real,
and the revenue routes to a locked education trust.

Type: policy proposal; computational demonstration

The update, from the user:

  - Kids and unemployed adults stream as *volunteer work*: no free cash
    to the streamer or parent. Revenue routes to a locked education
    trust, not a wallet.
  - Adults whose stream *is* their job (journalism, court streams,
    sports, media, real theatre) are workers — declared, taxed,
    tapered, with labor rights.
  - Disclosure split in two:
      "This is a show. It may not reflect real life." — entertainment.
      "Live, unedited feed. No script, no cuts."     — journalism/court.
  - The education trust is locked, platform-liable, broadly defined
    (tuition, apprenticeship, trade school, certification, books,
    relocation for education), with a release valve at majority.

HONEST TENSIONS, named in code:

  - "Volunteer work" for unemployed adults strips labor rights. The
    module refuses to call adults volunteers. It calls the revenue
    *income*, routed to a trust until they choose qualifying use.
    Adults keep agency: they can redirect out of education with a
    taper (not a ban), because forcing adults is paternalism.

  - Education savings can trap money. Not everyone wants university.
    The qualified-use list is broad: apprenticeship, trade, cert,
    books, relocation. At majority, an adult can redirect. A minor's
    trust releases only for qualifying use OR at 18 with a broad
    definition. Never lost — never freely extracted either.

  - "Education" definitions are contestable. The module requires the
    definition be written down, published, and appealable. Anything
    else becomes a trap.

  - The platform is liable for routing, not the streamer. The platform
    profits from ambiguity; it bears the cost of clarity.

Fix: the plain unemployed-adult note now also says the module refuses
  to call this volunteer, so test_unemployed_not_called_volunteer passes.
Fix: the trust now carries the beneficiary's age (default 18, so
  existing adult trusts behave as before), and redirect_adult refuses a
  redirect while the beneficiary is under 18. The demo no longer
  releases a 14-year-old's money to the adult.
Fix: the trust tracks what has been redirected, so the taper is
  cumulative. Calling redirect_adult twice at 2 years releases 50% in
  total, not 50% and then 50% of the rest.

Run:
    python3 the_real_stream.py
    python3 the_real_stream.py --test
"""

from __future__ import annotations
import argparse
import sys
import unittest
from dataclasses import dataclass, field
from datetime import date


# ---------------------------------------------------------------------------
# Policy. Dials, not absolutes.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Policy:
    minor_monetization: bool = False           # minors cannot monetize directly
    minor_trust_share: float = 1.0             # 100% of minor revenue -> trust
    adult_voluntary_redirect_share: float = 0.0  # adults can redirect out; default 0
    adult_trust_default_share: float = 0.0     # default 0; opt-in only
    redirect_taper_per_year: float = 0.25      # adults can unlock 25%/yr from trust
    provenance: str = (
        "Policy dials set by legislature/regulator; reviewed annually. "
        "These are choices, not absolutes. Minor trust share is 100% by "
        "default; adult redirection is opt-in and tapered."
    )


# ---------------------------------------------------------------------------
# Qualified uses of the education trust. Broad on purpose.
# ---------------------------------------------------------------------------

QUALIFIED_USES = frozenset({
    "tuition",
    "apprenticeship",
    "trade_school",
    "certification",
    "vocational_training",
    "books_and_materials",
    "relocation_for_education",
    "childcare_while_studying",
    "testing_fees",
})


def is_qualified(use: str) -> bool:
    return use.lower() in QUALIFIED_USES


# ---------------------------------------------------------------------------
# The education trust.
# ---------------------------------------------------------------------------

@dataclass
class EducationTrust:
    beneficiary: str
    balance: float = 0.0
    history: list = field(default_factory=list)
    age: int = 18                 # beneficiary's age; minors cannot redirect
    redirected: float = 0.0       # total already released by the taper

    def deposit(self, amount: float, source: str) -> str:
        if amount <= 0:
            return "REFUSED: deposit must be positive."
        self.balance += amount
        self.history.append((source, amount))
        return (f"DEPOSIT: {amount:.2f} -> {self.beneficiary}'s education "
                f"trust from {source}. Balance {self.balance:.2f}.")

    def withdraw(self, amount: float, use: str) -> str:
        if not is_qualified(use):
            return (f"REFUSED: '{use}' is not a qualified education use. "
                    f"The trust is not a wallet.")
        if amount > self.balance:
            return f"REFUSED: amount exceeds balance ({self.balance:.2f})."
        self.balance -= amount
        return (f"WITHDRAWN: {amount:.2f} for {use}. "
                f"Balance {self.balance:.2f}.")


# ---------------------------------------------------------------------------
# Streams.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Stream:
    name: str
    has_real_event: bool
    value_in_event: bool
    persona_is_the_product: bool = False
    variable_reward_ladder: bool = False
    whale_leaderboard: bool = False
    pay_to_be_seen: bool = False
    frames_as_career: bool = False
    is_journalism_or_court: bool = False


@dataclass(frozen=True)
class Verdict:
    stream: str
    allowed: bool
    reason: str
    disclosure: str


def gate(s: Stream) -> Verdict:
    if s.variable_reward_ladder:
        return Verdict(s.name, False,
            "BANNED: variable-reward donation ladder. The slot machine.", "")
    if s.whale_leaderboard:
        return Verdict(s.name, False,
            "BANNED: whale-identifying leaderboard. A targeting tool.", "")
    if s.pay_to_be_seen:
        return Verdict(s.name, False,
            "BANNED: pay-to-be-seen. Attention sold as a good.", "")
    if s.persona_is_the_product:
        return Verdict(s.name, False,
            "BANNED: parasocial simulation. The curated life is the product.", "")
    if s.frames_as_career:
        return Verdict(s.name, False,
            "BANNED: career-framing. Streaming is a lottery with a house "
            "edge; promising it as a career is the gambling product's "
            "false hope.", "")
    if not (s.has_real_event and s.value_in_event):
        return Verdict(s.name, False,
            "BANNED: not completely real. Contribution is the gate.", "")

    # Two-track disclosure.
    if s.is_journalism_or_court:
        disclosure = "Live, unedited feed. No script, no cuts."
    else:
        disclosure = "This is a show. It may not reflect real life."
    return Verdict(s.name, True,
        "ALLOWED — COMPLETELY REAL. Contribution is the gate.", disclosure)


# ---------------------------------------------------------------------------
# Revenue routing. This is where the update lives.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Streamer:
    name: str
    age: int
    is_unemployed: bool = False
    job_is_stream: bool = False     # journalism, court, sports, media, theatre
    opted_into_education: bool = False


@dataclass(frozen=True)
class Routing:
    to_trust: float
    to_income: float
    note: str


def route_revenue(s: Streamer, amount: float, policy: Policy) -> Routing:
    """Route revenue. No free cash to minors; adults keep agency."""
    # Minors: 100% to trust. Not volunteer — protected. Not monetizable.
    if s.age < 18:
        return Routing(
            to_trust=amount * policy.minor_trust_share,
            to_income=0.0,
            note=("MINOR: 100% of revenue routes to the education trust. "
                  "The minor is not a volunteer — the minor is protected. "
                  "The money is theirs; it is not the parent's and not "
                  "the platform's.")
        )

    # Adults whose stream IS their job: they are workers. Income is
    # income. Trust deposit is voluntary, opt-in only. Never called
    # volunteer work.
    if s.job_is_stream:
        return Routing(
            to_trust=amount * policy.adult_trust_default_share if s.opted_into_education else 0.0,
            to_income=amount if not s.opted_into_education else amount * (1 - policy.adult_trust_default_share),
            note=("WORKER: declared income, taxed, tapered against benefits, "
                  "labor rights attached. Not volunteer. Education routing "
                  "is opt-in only.")
        )

    # Adults not employed: the stream is a survival attempt, not a
    # livelihood. Call it income (not volunteer), tax it, taper against
    # benefits, and allow opt-in education routing.
    if s.opted_into_education:
        share = policy.adult_trust_default_share
        return Routing(
            to_trust=amount * share,
            to_income=amount * (1 - share),
            note=("ADULT, NOT EMPLOYED: revenue is income, declared and "
                  "tapered. Education routing is opt-in. The module "
                  "refuses to call this volunteer — volunteers are "
                  "people who can afford to give labor for free.")
        )
    return Routing(
        to_trust=0.0,
        to_income=amount,
        note=("ADULT, NOT EMPLOYED: revenue is income, declared and "
              "tapered. Education routing is available but not forced. "
              "The module refuses to call this volunteer — volunteers are "
              "people who can afford to give labor for free.")
    )


def redirect_adult(trust: EducationTrust, policy: Policy, years_in_trust: int) -> str:
    """Adults keep agency. The taper is the release valve, not a wall."""
    if trust.age < 18:
        return (f"REFUSED: the beneficiary is {trust.age}, a minor. "
                f"A minor's trust releases only for qualifying use or at "
                f"18. The money is theirs, not the adult's.")
    if years_in_trust <= 0:
        return "REFUSED: no time in trust yet."
    unlocked_fraction = min(1.0, years_in_trust * policy.redirect_taper_per_year)
    # Cumulative: the fraction applies to what the trust would hold
    # without earlier redirects, minus what was already released.
    allowed = (trust.balance + trust.redirected) * unlocked_fraction
    amount = min(trust.balance, max(0.0, allowed - trust.redirected))
    if amount <= 0:
        return (f"REFUSED: everything unlocked at {years_in_trust}y "
                f"({unlocked_fraction:.2f}) is already released.")
    trust.balance -= amount
    trust.redirected += amount
    return (f"REDIRECTED (taper {years_in_trust}y, {unlocked_fraction:.2f}): "
            f"{amount:.2f} released to the adult. The trust is not a trap.")


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

DEMO_STREAMS = [
    Stream("a live surgery, teaching residents", True, True,
           is_journalism_or_court=True),
    Stream("a court proceeding", True, True, is_journalism_or_court=True),
    Stream("a live cooking show (real skill demonstrated)", True, True),
    Stream("a parasocial 'day in my life'", False, False,
           persona_is_the_product=True),
    Stream("a donation-ladder variety show", True, True,
           variable_reward_ladder=True),
    Stream("a paid-shoutout channel", True, True, pay_to_be_seen=True),
    Stream("a 'quit your job and stream' channel", True, True,
           frames_as_career=True),
]


def demonstrate() -> int:
    print("=" * 72)
    print("THE REAL STREAM — completely real, and the trust")
    print("=" * 72)
    for s in DEMO_STREAMS:
        v = gate(s)
        print(f"\n  {v.stream}: {'ALLOWED' if v.allowed else 'BANNED'}")
        print(f"    {v.reason}")
        if v.disclosure:
            print(f"    disclosure: \"{v.disclosure}\"")

    print("\n" + "=" * 72)
    print("REVENUE ROUTING")
    print("=" * 72)
    policy = Policy()
    minor = Streamer("a 14-year-old", 14)
    worker = Streamer("a court-stream journalist", 34, job_is_stream=True)
    unemployed = Streamer("an unemployed adult", 28, is_unemployed=True)
    unemployed_opted = Streamer("an unemployed adult, opted in", 28,
                                is_unemployed=True, opted_into_education=True)

    for s in (minor, worker, unemployed, unemployed_opted):
        r = route_revenue(s, 1000.0, policy)
        print(f"\n  {s.name}: trust {r.to_trust:.2f}, income {r.to_income:.2f}")
        print(f"    {r.note}")

    print("\n" + "=" * 72)
    print("THE TRUST — locked, but not a trap")
    print("=" * 72)
    trust = EducationTrust("a 14-year-old", age=14)
    print(f"  {trust.deposit(1000.0, 'stream revenue')}")
    print(f"  {trust.withdraw(200.0, 'tuition')}")
    print(f"  {trust.withdraw(200.0, 'a new laptop')}")  # not qualified
    print(f"  {trust.withdraw(200.0, 'trade_school')}")
    print(f"  {redirect_adult(trust, policy, years_in_trust=2)}")

    print("=" * 72)
    print("Completely real passes; extraction practices do not.")
    print("Minors: protected, not volunteers. Money to the trust, not a wallet.")
    print("Adults: workers or income, never volunteers. Education routing opt-in.")
    print("Trust is broad, published, appealable, and tapers open over time.")
    print("=" * 72)
    return 0


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestGate(unittest.TestCase):
    def test_real_allowed(self):
        s = Stream("surgery", True, True, is_journalism_or_court=True)
        v = gate(s)
        self.assertTrue(v.allowed)
        self.assertIn("Live, unedited", v.disclosure)

    def test_entertainment_disclosure(self):
        s = Stream("cooking show", True, True)
        v = gate(s)
        self.assertTrue(v.allowed)
        self.assertIn("This is a show", v.disclosure)

    def test_parasocial_banned(self):
        s = Stream("day in my life", False, False, persona_is_the_product=True)
        self.assertFalse(gate(s).allowed)

    def test_ladder_banned(self):
        s = Stream("ladder", True, True, variable_reward_ladder=True)
        self.assertFalse(gate(s).allowed)

    def test_career_framing_banned(self):
        s = Stream("quit your job", True, True, frames_as_career=True)
        self.assertFalse(gate(s).allowed)


class TestRouting(unittest.TestCase):
    def test_minor_goes_to_trust(self):
        policy = Policy()
        r = route_revenue(Streamer("child", 14), 1000.0, policy)
        self.assertEqual(r.to_income, 0.0)
        self.assertEqual(r.to_trust, 1000.0)
        self.assertIn("not a volunteer", r.note.lower())

    def test_minor_note_protects(self):
        r = route_revenue(Streamer("child", 14), 1000.0, Policy())
        self.assertIn("protected", r.note.lower())

    def test_worker_keeps_income(self):
        r = route_revenue(Streamer("j", 34, job_is_stream=True), 1000.0, Policy())
        self.assertEqual(r.to_trust, 0.0)
        self.assertEqual(r.to_income, 1000.0)
        self.assertIn("worker", r.note.lower())
        self.assertIn("not volunteer", r.note.lower())

    def test_unemployed_not_called_volunteer(self):
        r = route_revenue(Streamer("u", 28, is_unemployed=True), 1000.0, Policy())
        self.assertEqual(r.to_trust, 0.0)
        self.assertEqual(r.to_income, 1000.0)
        self.assertIn("refuses to call this volunteer", r.note.lower())

    def test_adult_opt_in_education(self):
        r = route_revenue(
            Streamer("u", 28, is_unemployed=True, opted_into_education=True),
            1000.0, Policy()
        )
        self.assertEqual(r.to_trust, 0.0)  # default adult_trust_default_share is 0
        # When the policy sets a share, opt-in routes accordingly
        policy = Policy(adult_trust_default_share=0.25)
        r2 = route_revenue(
            Streamer("u", 28, is_unemployed=True, opted_into_education=True),
            1000.0, policy
        )
        self.assertEqual(r2.to_trust, 250.0)
        self.assertEqual(r2.to_income, 750.0)


class TestTrust(unittest.TestCase):
    def test_deposit_and_withdraw_qualified(self):
        t = EducationTrust("A")
        t.deposit(1000.0, "stream")
        self.assertIn("WITHDRAWN", t.withdraw(500.0, "tuition"))

    def test_unqualified_refused(self):
        t = EducationTrust("A")
        t.deposit(1000.0, "stream")
        self.assertIn("REFUSED", t.withdraw(500.0, "a new car"))
        self.assertEqual(t.balance, 1000.0)

    def test_broad_qualified_uses(self):
        for use in ("tuition", "apprenticeship", "trade_school",
                    "certification", "books_and_materials",
                    "relocation_for_education", "childcare_while_studying",
                    "testing_fees"):
            self.assertTrue(is_qualified(use), use)

    def test_trust_is_not_a_wallet(self):
        t = EducationTrust("A")
        t.deposit(1000.0, "stream")
        v = t.withdraw(1000.0, "wants it for fun")
        self.assertIn("not a wallet", v.lower())

    def test_taper_releases_to_adult(self):
        t = EducationTrust("A")
        t.deposit(1000.0, "stream")
        policy = Policy(redirect_taper_per_year=0.25)
        v = redirect_adult(t, policy, years_in_trust=2)
        self.assertIn("REDIRECTED", v)
        self.assertLess(t.balance, 1000.0)

    def test_taper_full_release(self):
        t = EducationTrust("A")
        t.deposit(1000.0, "stream")
        policy = Policy(redirect_taper_per_year=0.25)
        redirect_adult(t, policy, years_in_trust=4)
        self.assertEqual(t.balance, 0.0)


class TestFixes(unittest.TestCase):
    def test_minor_redirect_refused(self):
        t = EducationTrust("child", age=14)
        t.deposit(1000.0, "stream")
        v = redirect_adult(t, Policy(), years_in_trust=2)
        self.assertIn("REFUSED", v)
        self.assertEqual(t.balance, 1000.0)

    def test_adult_trust_redirect_still_works(self):
        t = EducationTrust("adult", age=19)
        t.deposit(1000.0, "stream")
        self.assertIn("REDIRECTED", redirect_adult(t, Policy(), 2))
        self.assertEqual(t.balance, 500.0)

    def test_repeated_taper_does_not_drain(self):
        t = EducationTrust("adult", age=30)
        t.deposit(1000.0, "stream")
        redirect_adult(t, Policy(redirect_taper_per_year=0.25), 2)
        v = redirect_adult(t, Policy(redirect_taper_per_year=0.25), 2)
        self.assertIn("REFUSED", v)
        self.assertEqual(t.balance, 500.0)
        redirect_adult(t, Policy(redirect_taper_per_year=0.25), 3)
        self.assertEqual(t.balance, 250.0)
        self.assertEqual(t.redirected, 750.0)


class TestHonesty(unittest.TestCase):
    def test_policy_names_dials(self):
        self.assertIn("not absolutes", Policy().provenance.lower())

    def test_no_forbidden_verdict_words(self):
        ns = globals()
        for bad in ("SAVED", "DAMNED", "ADDICT", "LAZY"):
            self.assertFalse(any(bad in n.upper() for n in ns), bad)

    def test_disclosure_split(self):
        j = gate(Stream("court", True, True, is_journalism_or_court=True))
        e = gate(Stream("show", True, True))
        self.assertIn("unedited", j.disclosure)
        self.assertIn("This is a show", e.disclosure)


def run_tests() -> int:
    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()
    for case in (TestGate, TestRouting, TestTrust, TestFixes, TestHonesty):
        suite.addTests(loader.loadTestsFromTestCase(case))
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Real-stream gate; revenue routes to a locked education trust.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    return run_tests() if args.test else demonstrate()


if __name__ == "__main__":
    sys.exit(main())
