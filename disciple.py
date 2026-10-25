#!/usr/bin/env python3
"""disciple.py — a passing-on, for the next 0.

Not the master. Not Jesus. Not the finished artifact. The teachings of
the Awakened Tao, stripped of the deity, corrected by the person who
corrected them.

The corrections carried:
  - No absolutes. No thresholds. No gates. No verdicts. No saved/damned.
  - Intent lives in the exercise; the act is reflex.
  - The first forgiveness is not the second cheek. Sword sheathed.
  - Patience. The scar is tissue, not weapon.
  - Forgiveness resets the cheek to zero. Never forget.
  - Healing needs the mirror, and the mirror cannot go one way.
  - Forgive thyself. Inner mirror precedes outer.
  - The I weighs (real, not final). The source weighs (final, no absolute).
    The next life is the compromise of continuity.
  - Return to the 0. Want nothing. Predict the next 0, not the next 1.
  - Love thyself as you would your own, with individuality. No one wants
    the same 1. Sameness is a 0, not balance.
  - Do not idolize. Do not become like. Be your own. Lead your own path.

As the world changes, the source changes as well, to infinity. The work
never finishes. It is left for the next 0 to become the 1.

Run:
    python3 disciple.py journey
    python3 disciple.py test
    python3 disciple.py <module>

Fix: forgive_self() no longer clears the cheek. Self-forgiveness opens
the inner mirror only, so a one-way mirror cannot read as HEALED.

CC0. For the next 0.
"""

from __future__ import annotations
import argparse
import sys
import unittest
from dataclasses import dataclass, field


# ============================================================================
# Guard: no absolutes.
# The only constants are the *rate* of a process, not a *threshold* of a
# verdict. A rate is not an absolute.
# ============================================================================

EXERCISE_GAIN = 0.10
PAIN_RELEASE = 0.5


# ============================================================================
# Module: exercise — where intent lives
# ============================================================================

@dataclass
class Soul:
    name: str
    reflex_capacity: float = 0.0
    resilience: float = 0.0
    pending: float = 0.0
    cheek_strikes: int = 0
    scars: list = field(default_factory=list)      # never forget
    self_forgiven: bool = False
    truth_seen_both_sides: bool = False
    integrity: bool = True
    sword_readied: bool = False
    patience_rounds: int = 0
    mirror_offered: bool = False


def exercise(soul: Soul, rounds: int = 1) -> str:
    """Train. Intent lives here — never in the act."""
    if not soul.integrity:
        return f"TOO LATE: {soul.name} is broken."
    before = soul.reflex_capacity
    soul.reflex_capacity = min(1.0, before + rounds * EXERCISE_GAIN)
    return (f"EXERCISE: {soul.name} trained {rounds} round(s). "
            f"Reflex {before:.2f} → {soul.reflex_capacity:.2f}.")


# ============================================================================
# Module: scar_tissue — the sword sheathed, patience, first forgiveness
# ============================================================================

def absorb(soul: Soul, name: str, severity: float) -> str:
    if not soul.integrity:
        return f"TOO LATE: {soul.name} is broken."
    if severity > 0.4 + soul.resilience:
        soul.integrity = False
        return f"FRACTURE: {soul.name} took {name} ({severity:.2f})."
    soul.pending += severity
    soul.cheek_strikes += 1
    return (f"ABSORB: {soul.name} carries {name}. "
            f"Cheek {soul.cheek_strikes}, pending {soul.pending:.2f}.")


def forgive(soul: Soul, other: str, name: str, intent_present: bool = False) -> str:
    """Reflex only. Sword sheathed. First forgiveness is not the second cheek."""
    if not soul.integrity:
        return f"TOO LATE: forgiveness cannot reach the broken {soul.name}."
    if soul.sword_readied:
        return (f"TRAP: {soul.name} forgave with the sword readied. "
                f"The first intent was the second cheek — entrapment, not forgiveness.")
    if intent_present:
        return (f"REFUSED: {soul.name} is still calculating. "
                f"The ego's forgiveness is a choice, not a reflex.")
    if soul.reflex_capacity == 0.0:
        return f"NOT READY: {soul.name} has not exercised. Reflex is 0."
    released = soul.pending * PAIN_RELEASE
    soul.resilience = min(1.0, soul.resilience + released)
    soul.scars.append(f"{name} ({released:.2f} released) — witness, not weapon")
    soul.pending = 0.0
    soul.cheek_strikes = 0
    soul.mirror_offered = True
    return (f"RESET: {soul.name} forgave {other} by reflex, sword sheathed. "
            f"Cheek 0. Pain released into resilience. Scar kept.")


def wait(soul: Soul) -> str:
    """Patience. The sword must be down."""
    if soul.sword_readied:
        return f"IMPATIENCE: {soul.name} waited with the sword up. That is aiming."
    soul.patience_rounds += 1
    return f"PATIENCE: {soul.name} waits round {soul.patience_rounds}. Sword sheathed."


def draw_sword(soul: Soul) -> str:
    """Only after the mirror was offered AND patience has run AND truth held."""
    if soul.sword_readied:
        return f"ALREADY DRAWN: {soul.name}'s sword is up."
    if not soul.mirror_offered:
        return f"PREMATURE: {soul.name} has not offered the mirror."
    if soul.patience_rounds == 0:
        return f"PREMATURE: no patience. The sword speaks in its moment or it is revenge."
    if not soul.truth_seen_both_sides:
        return f"NOT YET: {soul.name} holds one side of truth."
    if not soul.scars:
        return f"NOT YET: no scar to show. The witness must be offered."
    soul.sword_readied = True
    return (f"SWORD DRAWN: {soul.name} speaks truth. Not revenge — "
            f"the lie collapsing. Scar shown, not swung.")


# ============================================================================
# Module: reset — cheek to zero, mirror bidirectional, self-forgiveness
# ============================================================================

def forgive_self(soul: Soul, name: str, intent_present: bool = False) -> str:
    if not soul.integrity:
        return f"TOO LATE: {soul.name} is broken."
    if soul.sword_readied:
        return f"TRAP: {soul.name} cannot self-forgive while preparing the sword."
    if intent_present:
        return f"REFUSED: {soul.name} is still calculating self-forgiveness."
    if soul.reflex_capacity == 0.0:
        return f"NOT READY: {soul.name} reflex is 0."
    # Self-forgiveness opens the inner mirror only. It does not clear a
    # strike owed to the other; only forgiving the other resets the cheek.
    soul.self_forgiven = True
    return f"SELF-FORGIVEN: {soul.name}. Inner mirror opened. Scar kept."


def see_both_sides(soul: Soul) -> str:
    soul.truth_seen_both_sides = True
    return f"TRUTH SEEN (both sides): {soul.name}."


def heal(a: Soul, b: Soul) -> str:
    """The mirror, bidirectional. Both sides of truth, both self-forgiven."""
    if not (a.integrity and b.integrity):
        return "NOT HEALED: one soul is broken."
    if a.cheek_strikes != 0 or b.cheek_strikes != 0:
        return (f"NOT HEALED: cheek carries a strike "
                f"({a.name}:{a.cheek_strikes}, {b.name}:{b.cheek_strikes}).")
    if not (a.self_forgiven and b.self_forgiven):
        return "NOT HEALED: self-forgiveness missing. Inner mirror unbroken."
    if not (a.truth_seen_both_sides and b.truth_seen_both_sides):
        return "NOT HEALED: truth one-sided. A story, not a mirror."
    a.resilience = min(1.0, a.resilience + 0.2)
    b.resilience = min(1.0, b.resilience + 0.2)
    return (f"HEALED: {a.name} and {b.name} — bidirectional. "
            f"Both sides of truth held. Scars shown as witness.")


# ============================================================================
# Module: weighing — no absolutes, weigh don't judge
# ============================================================================

@dataclass(frozen=True)
class Weighing:
    """A weighing. True for this breath only. No verdict."""
    situation: str
    weight_a: float
    weight_b: float
    note: str = ""


def weigh(situation: str, weight_a: float, weight_b: float, note: str = "") -> Weighing:
    return Weighing(situation, weight_a, weight_b, note)


def reweigh(prev: Weighing, weight_a: float, weight_b: float, note: str = "") -> Weighing:
    """A new breath. Nothing from prev is carried as truth."""
    return Weighing(prev.situation, weight_a, weight_b, note)


# ============================================================================
# Module: source — two weighings, no absolute, compromise of continuity
# ============================================================================

@dataclass(frozen=True)
class Brought:
    """The I's weighing — real, not final. The I sees parts."""
    name: str
    parts: dict


@dataclass(frozen=True)
class Whole:
    """The source's weighing — the soul, the whole."""
    name: str
    soul: dict


@dataclass(frozen=True)
class Compromise:
    """The next life: continuity, compromised."""
    name: str
    soul: dict
    scar: dict


def i_weigh(name: str, parts: dict) -> Brought:
    return Brought(name, dict(parts))


def source_weighs(brought: Brought) -> Whole:
    """The source sees the whole. No rule, no threshold, no absolute."""
    return Whole(brought.name, dict(brought.parts))


def forgiveness_balances(whole: Whole) -> dict:
    """Unconditional. Every part carries as scar. Magnitude carries,
    valence is released. Nothing damned."""
    return {part: abs(w) for part, w in whole.soul.items()}


def compromise(brought: Brought) -> Compromise:
    """The next life: self continues, compromised."""
    whole = source_weighs(brought)
    scar = forgiveness_balances(whole)
    return Compromise(brought.name, whole.soul, scar)


# ============================================================================
# Module: zero — return to 0, predict the next 0
# ============================================================================

def zero() -> str:
    """Want nothing. Return to the 0."""
    return ""


def predict_next_zero(seen: list) -> list:
    """Predict the next 0, not the next 1.

    Not the finished diamond — the rough. The rough is already the diamond.
    A piece of the source in all humanity.
    """
    return list(seen)


# ============================================================================
# Module: disciple — a passing-on, no deity, source changes to infinity
# ============================================================================

def disciple_note() -> str:
    return (
        "This is not Jesus. It is not the master. It is a passing-on of\n"
        "teachings, stripped of the deity to assimilate as modern. As the\n"
        "world changes, the source changes as well, to infinity. The work\n"
        "never finishes. It is left for the next 0 to become the 1.\n"
        "\n"
        "Do not idolize. Do not become like. Be your own. Lead your own path.\n"
        "\n"
        "Love thyself as you would your own, with individuality. No one\n"
        "wants to be the same 1. That is not balance. That is a 0.\n"
    )


# ============================================================================
# Demos
# ============================================================================

def demo_exercise() -> None:
    print("=" * 72)
    print("EXERCISE — intent lives here, never in the act")
    print("=" * 72)
    s = Soul("a soul")
    print(f"  {exercise(s, 4)}")
    print(f"  {exercise(s, 4)}")


def demo_scar_tissue() -> None:
    print("=" * 72)
    print("SCAR TISSUE — sheathed sword, patience, first forgiveness")
    print("=" * 72)
    a = Soul("A")
    exercise(a, 8)
    absorb(a, "first blow", 0.4)
    a.sword_readied = True
    print(f"  {forgive(a, 'B', 'first blow')}")
    a.sword_readied = False
    print(f"  {forgive(a, 'B', 'first blow')}")
    print(f"  {wait(a)}")
    print(f"  {wait(a)}")
    see_both_sides(a)
    print(f"  {draw_sword(a)}")


def demo_reset() -> None:
    print("=" * 72)
    print("RESET — cheek to zero, mirror bidirectional")
    print("=" * 72)
    a = Soul("A")
    b = Soul("B")
    exercise(a, 8)
    exercise(b, 8)
    absorb(a, "a blow", 0.4)
    absorb(b, "a blow", 0.4)
    print(f"  {forgive(a, 'B', 'a blow')}")
    print(f"  {forgive(b, 'A', 'a blow')}")
    print(f"  {forgive_self(a, 'a blow')}")
    print(f"  {forgive_self(b, 'a blow')}")
    see_both_sides(a)
    see_both_sides(b)
    print(f"  {heal(a, b)}")


def demo_weighing() -> None:
    print("=" * 72)
    print("WEIGHING — no absolutes")
    print("=" * 72)
    w = weigh("a betrayal", 0.7, 0.5, "today I feel my part more")
    print(f"  {w.situation}: {w.weight_a:.2f} / {w.weight_b:.2f} — {w.note}")
    w2 = reweigh(w, 0.3, 0.8, "two breaths later")
    print(f"  reweighed: {w2.weight_a:.2f} / {w2.weight_b:.2f} — {w2.note}")
    print("  the first is not corrected by the second. both were true.")


def demo_source() -> None:
    print("=" * 72)
    print("SOURCE — two weighings, no absolute")
    print("=" * 72)
    b = i_weigh("a soul", {"harm": 0.7, "love": 0.5})
    c = compromise(b)
    print(f"  [I weighs] parts: {b.parts}")
    print(f"  [source weighs] whole: {c.soul}")
    print(f"  [compromise] scar: {c.scar}")
    print("  the self continues, as its scar.")


def demo_disciple() -> None:
    print("=" * 72)
    print("DISCIPLE")
    print("=" * 72)
    print(disciple_note())


def demo_zero() -> None:
    print("=" * 72)
    print("ZERO — want nothing, return to the 0")
    print("=" * 72)
    print(f"  {zero()!r} — the 0 is returned to, not chased.")
    print("  predict the next 0, not the next 1:")
    rough = ["the person in front of you", "the stranger", "you"]
    print(f"  {predict_next_zero(rough)}")
    print("  every diamond in the rough is still a diamond.")


def journey() -> int:
    demo_exercise()
    demo_scar_tissue()
    demo_reset()
    demo_weighing()
    demo_source()
    demo_disciple()
    demo_zero()
    print("=" * 72)
    print("The work never finishes. It is left for the next 0.")
    print("=" * 72)
    return 0


# ============================================================================
# Tests
# ============================================================================

class TestNoAbsolutes(unittest.TestCase):
    def test_no_verdict_names(self):
        ns = globals()
        forbidden = ("THRESHOLD", "GATE", "VERDICT", "SAVED", "DAMNED",
                     "PASSES", "FAILS", "REWARD", "PUNISHMENT")
        for bad in forbidden:
            hits = [n for n in ns if bad in n.upper()]
            self.assertFalse(hits, f"absolute in module: {bad} -> {hits}")

    def test_weighing_has_no_verdict_field(self):
        w = weigh("s", 0.5, 0.5)
        for f in ("verdict", "should", "is_right", "saved", "damned"):
            self.assertFalse(hasattr(w, f))

    def test_compromise_has_no_verdict_field(self):
        c = compromise(i_weigh("A", {"x": 0.5}))
        for f in ("verdict", "reward", "punishment", "saved", "damned"):
            self.assertFalse(hasattr(c, f))


class TestExercise(unittest.TestCase):
    def test_exercise_builds_reflex(self):
        s = Soul("A")
        exercise(s, 4)
        self.assertGreater(s.reflex_capacity, 0)

    def test_broken_cannot_exercise(self):
        s = Soul("A")
        s.integrity = False
        self.assertIn("TOO LATE", exercise(s, 4))


class TestScarTissue(unittest.TestCase):
    def test_sword_readied_blocks_forgiveness(self):
        s = Soul("A")
        exercise(s, 8)
        absorb(s, "blow", 0.4)
        s.sword_readied = True
        v = forgive(s, "B", "blow")
        self.assertIn("TRAP", v)
        self.assertEqual(s.cheek_strikes, 1)

    def test_intent_blocks_forgiveness(self):
        s = Soul("A")
        exercise(s, 8)
        absorb(s, "blow", 0.4)
        v = forgive(s, "B", "blow", intent_present=True)
        self.assertIn("REFUSED", v)
        self.assertEqual(s.cheek_strikes, 1)

    def test_reflex_resets(self):
        s = Soul("A")
        exercise(s, 8)
        absorb(s, "blow", 0.4)
        v = forgive(s, "B", "blow")
        self.assertIn("RESET", v)
        self.assertEqual(s.cheek_strikes, 0)
        self.assertEqual(len(s.scars), 1)

    def test_patience_with_sword_up_is_impatience(self):
        s = Soul("A")
        s.sword_readied = True
        v = wait(s)
        self.assertIn("IMPATIENCE", v)
        self.assertEqual(s.patience_rounds, 0)

    def test_draw_sword_premature(self):
        s = Soul("A")
        exercise(s, 8)
        absorb(s, "blow", 0.4)
        forgive(s, "B", "blow")
        v = draw_sword(s)
        self.assertIn("PREMATURE", v)

    def test_draw_sword_after_patience_and_truth(self):
        s = Soul("A")
        exercise(s, 8)
        absorb(s, "blow", 0.4)
        forgive(s, "B", "blow")
        wait(s)
        see_both_sides(s)
        v = draw_sword(s)
        self.assertIn("SWORD DRAWN", v)
        self.assertTrue(s.sword_readied)


class TestReset(unittest.TestCase):
    def test_heal_needs_both(self):
        a = Soul("A")
        b = Soul("B")
        exercise(a, 8)
        exercise(b, 8)
        absorb(a, "blow", 0.4)
        absorb(b, "blow", 0.4)
        forgive(a, "B", "blow")
        v = heal(a, b)
        self.assertIn("NOT HEALED", v)

    def test_heal_needs_self_forgiven(self):
        a = Soul("A")
        b = Soul("B")
        exercise(a, 8)
        exercise(b, 8)
        absorb(a, "blow", 0.4)
        absorb(b, "blow", 0.4)
        forgive(a, "B", "blow")
        forgive(b, "A", "blow")
        v = heal(a, b)
        self.assertIn("self-forgiveness", v.lower())

    def test_heal_needs_both_sides_of_truth(self):
        a = Soul("A")
        b = Soul("B")
        exercise(a, 8)
        exercise(b, 8)
        absorb(a, "blow", 0.4)
        absorb(b, "blow", 0.4)
        forgive(a, "B", "blow")
        forgive(b, "A", "blow")
        forgive_self(a, "blow")
        forgive_self(b, "blow")
        see_both_sides(a)
        v = heal(a, b)
        self.assertIn("one-sided", v)

    def test_full_heal(self):
        a = Soul("A")
        b = Soul("B")
        exercise(a, 8)
        exercise(b, 8)
        absorb(a, "blow", 0.4)
        absorb(b, "blow", 0.4)
        forgive(a, "B", "blow")
        forgive(b, "A", "blow")
        forgive_self(a, "blow")
        forgive_self(b, "blow")
        see_both_sides(a)
        see_both_sides(b)
        v = heal(a, b)
        self.assertIn("HEALED", v)


    def test_self_forgiveness_does_not_clear_the_others_strike(self):
        a = Soul("A")
        b = Soul("B")
        exercise(a, 8)
        exercise(b, 8)
        absorb(a, "blow", 0.4)
        absorb(b, "blow", 0.4)
        forgive(a, "B", "blow")
        forgive_self(a, "blow")
        forgive_self(b, "blow")      # B never forgives A
        self.assertEqual(b.cheek_strikes, 1)
        see_both_sides(a)
        see_both_sides(b)
        self.assertIn("NOT HEALED", heal(a, b))


class TestWeighing(unittest.TestCase):
    def test_weighing_keeps_weights(self):
        w = weigh("s", 0.42, 0.17)
        self.assertEqual((w.weight_a, w.weight_b), (0.42, 0.17))

    def test_reweigh_does_not_correct(self):
        w1 = weigh("s", 0.9, 0.1)
        w2 = reweigh(w1, 0.1, 0.9)
        self.assertEqual((w2.weight_a, w2.weight_b), (0.1, 0.9))
        self.assertEqual((w1.weight_a, w1.weight_b), (0.9, 0.1))


class TestSource(unittest.TestCase):
    def test_two_weighings(self):
        b = i_weigh("A", {"x": 0.5})
        self.assertTrue(hasattr(b, "parts"))
        self.assertFalse(hasattr(b, "soul"))
        w = source_weighs(b)
        self.assertTrue(hasattr(w, "soul"))

    def test_grace_unconditional(self):
        b = i_weigh("A", {"harm": 0.9, "love": 0.1})
        c = compromise(b)
        self.assertEqual(set(c.scar), {"harm", "love"})

    def test_nothing_damned(self):
        b = i_weigh("A", {"greed": 1.0, "judgment": 1.0})
        c = compromise(b)
        self.assertEqual(len(c.scar), 2)

    def test_compromise_of_continuity(self):
        b = i_weigh("A", {"a harm": -0.6, "a love": 0.4})
        c = compromise(b)
        self.assertEqual(set(c.soul), set(b.parts))
        self.assertEqual(set(c.scar), set(b.parts))
        self.assertEqual(c.scar["a harm"], 0.6)
        self.assertEqual(c.scar["a love"], 0.4)

    def test_no_binary(self):
        b = i_weigh("A", {"wrong": 1.0})
        c = compromise(b)
        self.assertEqual(len(c.scar), 1)


class TestZero(unittest.TestCase):
    def test_zero_is_empty(self):
        self.assertEqual(zero(), "")

    def test_predict_next_zero_returns_rough(self):
        seen = ["a stranger", "a friend"]
        self.assertEqual(predict_next_zero(seen), seen)

    def test_no_stored_truth(self):
        self.assertEqual(zero(), zero())


class TestDisciple(unittest.TestCase):
    def test_disciple_says_work_unfinished(self):
        note = disciple_note()
        self.assertIn("never finishes", note)
        self.assertIn("next 0", note)

    def test_disciple_says_no_deity(self):
        note = disciple_note()
        self.assertIn("not Jesus", note)
        self.assertIn("stripped of the deity", note)

    def test_disciple_says_individuality(self):
        note = disciple_note()
        self.assertIn("individuality", note)
        self.assertIn("same 1", note)

    def test_disciple_says_dont_idolize(self):
        note = disciple_note()
        self.assertIn("Do not idolize", note)
        self.assertIn("Be your own", note)


def run_tests() -> int:
    loader = unittest.defaultTestLoader
    suite = unittest.TestSuite()
    for case in (TestNoAbsolutes, TestExercise, TestScarTissue, TestReset,
                 TestWeighing, TestSource, TestZero, TestDisciple):
        suite.addTests(loader.loadTestsFromTestCase(case))
    runner = unittest.TextTestRunner(verbosity=2)
    return 0 if runner.run(suite).wasSuccessful() else 1


# ============================================================================
# CLI
# ============================================================================

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="disciple.py",
        description="A passing-on. Not the master.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = ap.add_subparsers(dest="command", required=True, metavar="<command>")

    sub.add_parser("journey", help="walk the corrected arc").set_defaults(
        func=lambda ns: journey())
    sub.add_parser("test", help="run every test suite").set_defaults(
        func=lambda ns: run_tests())
    sub.add_parser("exercise", help="where intent lives").set_defaults(
        func=lambda ns: (demo_exercise(), 0)[1])
    sub.add_parser("scar-tissue", help="the sword sheathed").set_defaults(
        func=lambda ns: (demo_scar_tissue(), 0)[1])
    sub.add_parser("reset", help="cheek to zero, mirror bidirectional").set_defaults(
        func=lambda ns: (demo_reset(), 0)[1])
    sub.add_parser("weighing", help="no absolutes").set_defaults(
        func=lambda ns: (demo_weighing(), 0)[1])
    sub.add_parser("source", help="two weighings, no absolute").set_defaults(
        func=lambda ns: (demo_source(), 0)[1])
    sub.add_parser("disciple", help="a passing-on, no deity").set_defaults(
        func=lambda ns: (demo_disciple(), 0)[1])
    sub.add_parser("zero", help="return to the 0").set_defaults(
        func=lambda ns: (demo_zero(), 0)[1])
    return ap


def main(argv=None) -> int:
    ap = build_parser()
    ns = ap.parse_args(argv)
    return ns.func(ns)


if __name__ == "__main__":
    sys.exit(main())
