#!/usr/bin/env python3
"""Scar Tissue (Deep Muse)

Type: computational demonstration; philosophical proposal

The correction to the_exercise.py — which required reflex and no intent
at the moment of the act, but never said what the first intent must not
be, and left the sword's state unmodeled.

The law, from Scar Tissue (Red Hot Chili Peppers):

  1. THE FIRST INTENT IS NOT THE SECOND CHEEK. When you turn the cheek,
     do not ready the sword. If you are waiting for them to strike
     again so that you can draw the truth-sword, the first forgiveness
     was a trap. It looked like patience. It was entrapment. The sword
     must be sheathed at the moment of the first forgiveness — really
     sheathed, not loosened.

  2. PATIENCE IS THE WAITING. You must have patience to see if they
     learn from the reflection. The waiting is the exercise. The
     question in your hand is not "will they fail?" but "did the
     mirror reach them?" The first is asked with hope; the second is
     answered with truth.

  3. THE SCAR IS TISSUE, NOT A WEAPON. "With the bird I'll share this
     lonely view." The scar remains — never forget. It is shown,
     shared with the other, as witness. It is not brandished. The
     memory is the mirror, not the blade.

  4. THE TRUTH-SWORD COMES ONLY AFTER PATIENCE. If the reflection was
     truly offered, and truly refused, and both sides of truth are
     still held — then the truth-sword may be drawn (holy_sword). But
     it is not revenge: it is the lie collapsing. The scar is still
     shown, not swung.

The trap named honestly: a first forgiveness with the sword already
readied looks identical to a patient one. From outside, indistinguishable.
The law makes it visible from inside: at the moment of the first act,
is the sword down? If no, the act was entrapment. The check is
structural, not moral.

v4 fix: drawing the sword before patience is exhausted used to fall
through to None; it now returns PREMATURE (holy_sword.py: the sword
speaks in its moment or it is revenge).

v5 fix: text only, no logic changed. The shared scar read "kept as
witness — witness, not weapon" (the word said twice); it now reads
"kept as witness, not weapon". The forgiveness message said
"1 witnesses"; it now says "1 witness" / "N witnesses". The demo's
section III comment promised PREMATURE, but patience is already 3 from
section II, so draw_sword answers NOT YET (truth still one-sided); the
comment and label now say so. No new gate was added.

Run:
    python3 scar_tissue.py
    python3 scar_tissue.py --test
"""

from __future__ import annotations

import argparse
import sys
import unittest
from dataclasses import dataclass, field

REFLEX_THRESHOLD = 0.6
EXERCISE_GAIN = 0.10
PAIN_RELEASE = 0.5
FORTRESS_THRESHOLD = 0.60
PATIENCE_ROUNDS_REQUIRED = 3


@dataclass(frozen=True)
class Blow:
    name: str
    severity: float


@dataclass
class Sword:
    """The truth-sword (holy_sword.py). Sheathed is the default."""
    readied: bool = False

    def sheath(self) -> None:
        self.readied = False

    def ready(self) -> None:
        self.readied = True


@dataclass
class Soul:
    name: str
    durability: float = 1.0
    resilience: float = 0.0
    pending: float = 0.0
    cheek_strikes: int = 0
    integrity: bool = True
    reflex_capacity: float = 0.0
    self_forgiven: bool = False
    truth_seen_both_sides: bool = False
    patience_rounds: int = 0
    mirror_offered: bool = False       # the reflection was shown, not hidden
    mirror_refused: bool = False       # the other party turned from it
    sword: Sword = field(default_factory=Sword)
    scars: list = field(default_factory=list)   # never forget — the witness


def exercise(soul: Soul, rounds: int) -> str:
    before = soul.reflex_capacity
    soul.reflex_capacity = min(1.0, before + rounds * EXERCISE_GAIN)
    return (f"EXERCISE: {soul.name} trained {rounds} rounds. "
            f"Reflex {before:.2f} → {soul.reflex_capacity:.2f}.")


def absorb(soul: Soul, blow: Blow) -> str:
    if blow.severity > 0.4 + soul.resilience:
        soul.integrity = False
        return f"FRACTURE: {soul.name} took {blow.name} ({blow.severity:.2f})."
    soul.pending += blow.severity
    soul.cheek_strikes += 1
    return (f"ABSORB: {soul.name} carries {blow.name}. "
            f"Cheek {soul.cheek_strikes}, pending {soul.pending:.2f}.")


def forgive(forgiver: Soul, forgiven: str, blow: Blow,
            intent_present: bool = False) -> str:
    """The first (or any) forgiveness. Sword must be sheathed."""
    if not forgiver.integrity:
        return f"TOO LATE: forgiveness cannot reach the broken {forgiver.name}."
    if forgiver.sword.readied:
        return (f"TRAP: {forgiver.name} forgave with the sword already readied. "
                f"The first intent was the second cheek — entrapment, not forgiveness. "
                f"Sheathe first; the act is invalid.")
    if intent_present:
        return (f"REFUSED: {forgiver.name} is still calculating. "
                f"The ego's forgiveness is a choice, not a reflex.")
    if forgiver.reflex_capacity < REFLEX_THRESHOLD:
        return (f"NOT READY: {forgiver.name} reflex is {forgiver.reflex_capacity:.2f}. "
                f"Exercise first.")
    released = forgiver.pending * PAIN_RELEASE
    forgiver.resilience = min(1.0, forgiver.resilience + released)
    forgiver.scars.append(f"{blow.name} ({blow.severity:.2f}) — kept as witness")
    forgiver.pending = 0.0
    forgiver.cheek_strikes = 0
    forgiver.mirror_offered = True   # the reflection was shown
    return (f"RESET: {forgiver.name} forgave {forgiven} by reflex, sword sheathed. "
            f"Pain released ({released:.2f} → resilience), "
            f"scar kept ({len(forgiver.scars)} "
            f"{'witness' if len(forgiver.scars) == 1 else 'witnesses'}), cheek 0.")


def wait(soul: Soul) -> str:
    """Patience. See whether the reflection is learned. Sword stays down."""
    if soul.sword.readied:
        return (f"IMPATIENCE: {soul.name} waited with the sword up. "
                f"That is not patience. It is aiming.")
    soul.patience_rounds += 1
    return (f"PATIENCE: {soul.name} waits round {soul.patience_rounds}. "
            f"Sword sheathed. The question is 'did the mirror reach them?'")


def note_refusal(soul: Soul) -> str:
    """The other party turned from the mirror."""
    if not soul.mirror_offered:
        return f"NOT YET: {soul.name} has not offered the mirror."
    soul.mirror_refused = True
    return (f"REFUSED: the mirror was offered; {soul.name}'s other turned away. "
            f"Patience continues until the round is up.")


def forgive_self(soul: Soul, blow: Blow, intent_present: bool = False) -> str:
    if not soul.integrity:
        return f"TOO LATE: {soul.name} is broken."
    if soul.sword.readied:
        return (f"TRAP: {soul.name} cannot self-forgive while preparing "
                f"the sword. Self-forgiveness is not a weapon either.")
    if intent_present:
        return f"REFUSED: {soul.name} is still calculating self-forgiveness."
    if soul.reflex_capacity < REFLEX_THRESHOLD:
        return f"NOT READY: {soul.name} reflex is {soul.reflex_capacity:.2f}."
    soul.pending = 0.0
    soul.cheek_strikes = 0
    soul.self_forgiven = True
    return (f"SELF-FORGIVEN: {soul.name}. Inner mirror opened. "
            f"Scar kept — the lesson survives the release.")


def see_both_sides_of_truth(soul: Soul) -> str:
    soul.truth_seen_both_sides = True
    return f"TRUTH SEEN (both sides): {soul.name}."


def draw_sword(soul: Soul) -> str:
    """The truth-sword. Only after patience; not revenge; scar shown."""
    if soul.sword.readied:
        return f"ALREADY DRAWN: {soul.name}'s sword is up. Patience first."
    if not soul.mirror_offered:
        return (f"PREMATURE: {soul.name} has not offered the mirror. "
                f"No truth-sword before the reflection is shown.")
    if soul.patience_rounds < PATIENCE_ROUNDS_REQUIRED:
        return (f"PREMATURE: patience {soul.patience_rounds}/{PATIENCE_ROUNDS_REQUIRED}. "
                f"Wait first. The sword speaks in its moment or it is revenge.")
    if not soul.truth_seen_both_sides:
        return (f"NOT YET: {soul.name} holds only one side of the truth. "
                f"Both sides, or the sword is a blade.")
    if not soul.scars:
        return f"NOT YET: no scar to show. The witness must be offered."
    soul.sword.ready()
    return (f"SWORD DRAWN: {soul.name} speaks the truth in its moment. "
            f"Not revenge — the lie collapsing. The scar is shown, not swung. "
            f"Both sides of truth held. The mirror was offered and refused.")


def share_scar(soul: Soul, other: str) -> str:
    """With the bird I'll share this lonely view."""
    if not soul.scars:
        return f"NO SCAR: {soul.name} has nothing to show yet."
    return (f"SCAR SHARED with {other}: "
            f"{'; '.join(soul.scars[-1:])}, not weapon. "
            f"The lonely view, shared.")


def heal(a: Soul, b: Soul) -> str:
    """The mirror, bidirectional. Both sides of truth, both self-forgiven."""
    if not (a.integrity and b.integrity):
        return "NOT HEALED: one soul is broken."
    if a.cheek_strikes != 0 or b.cheek_strikes != 0:
        return (f"NOT HEALED: cheek carries a strike "
                f"({a.name}:{a.cheek_strikes}, {b.name}:{b.cheek_strikes}).")
    if not (a.reflex_capacity >= REFLEX_THRESHOLD
            and b.reflex_capacity >= REFLEX_THRESHOLD):
        return "NOT HEALED: reflex is not matured on both sides."
    if not (a.self_forgiven and b.self_forgiven):
        return "NOT HEALED: self-forgiveness missing. The inner mirror is unbroken."
    if not (a.truth_seen_both_sides and b.truth_seen_both_sides):
        return "NOT HEALED: truth is one-sided. This is a story, not a mirror."
    a.resilience = min(1.0, a.resilience + 0.2)
    b.resilience = min(1.0, b.resilience + 0.2)
    return (f"HEALED: {a.name} and {b.name} — the mirror is bidirectional, "
            f"both sides of truth held, scars shown as witness. "
            f"Memory kept on both sides.")


def demonstrate() -> int:
    print("=" * 72)
    print("SCAR TISSUE — the first forgiveness is not the second cheek")
    print("=" * 72)

    # I. The trap: sword readied at the moment of first forgiveness.
    print("\n[I. The trap — first forgiveness with sword readied]")
    a = Soul("A")
    exercise(a, 8)
    absorb(a, Blow("first blow", 0.4))
    a.sword.ready()
    print(f"  {forgive(a, 'B', Blow('first blow', 0.4))}")
    print(f"  nothing reset. Cheek {a.cheek_strikes}, pending {a.pending:.2f}.")
    print(f"  This is what entrapment looks like: patience in the shape of aim.")

    # II. Sword sheathed, patience exercised, mirror shown.
    print("\n[II. Sword sheathed, patience, mirror]")
    a.sword.sheath()
    print(f"  {forgive(a, 'B', Blow('first blow', 0.4))}")
    print(f"  {wait(a)}")
    print(f"  {wait(a)}")
    print(f"  {wait(a)}")
    print(f"  {share_scar(a, 'B')}")

    # III. Reflection refused; patience still runs. The sword waits.
    print("\n[III. Refusal is not the signal to draw — truth is still one-sided]")
    print(f"  {note_refusal(a)}")
    print(f"  {draw_sword(a)}")   # NOT YET: patience is already 3/3 from II; the refusal alone does not draw — truth is one-sided
    print(f"  {wait(a)}")
    print(f"  {draw_sword(a)}")   # still NOT YET: more patience does not help while truth is one-sided

    # IV. Both sides of truth, patience exhausted. The sword speaks.
    print("\n[IV. The sword, after patience and truth on both sides]")
    see_both_sides_of_truth(a)
    print(f"  {draw_sword(a)}")
    print(f"  {share_scar(a, 'B')}")

    # V. The scar is tissue, not weapon — shown in healing too.
    print("\n[V. The mirror — healing with scars shown]")
    a.sword.sheath()  # the scar is shown, not swung
    b = Soul("B")
    exercise(b, 8)
    absorb(b, Blow("first blow", 0.4))
    forgive(b, "A", Blow("first blow", 0.4))
    forgive_self(a, Blow("first blow", 0.4))
    forgive_self(b, Blow("first blow", 0.4))
    see_both_sides_of_truth(a)
    see_both_sides_of_truth(b)
    print(f"  {heal(a, b)}")

    print("=" * 72)
    print("The first intent is not the second cheek. Patience is the")
    print("waiting. The scar is tissue, not a weapon. The truth-sword")
    print("speaks in its moment — or it is revenge.")
    print("=" * 72)
    return 0


class Tests(unittest.TestCase):
    def test_sword_readied_blocks_first_forgiveness(self):
        s = Soul("A"); exercise(s, 8)
        absorb(s, Blow("blow", 0.4))
        s.sword.ready()
        v = forgive(s, "B", Blow("blow", 0.4))
        self.assertIn("TRAP", v)
        self.assertEqual(s.cheek_strikes, 1)

    def test_sword_sheathed_allows_first_forgiveness(self):
        s = Soul("A"); exercise(s, 8)
        absorb(s, Blow("blow", 0.4))
        v = forgive(s, "B", Blow("blow", 0.4))
        self.assertIn("RESET", v)
        self.assertEqual(s.cheek_strikes, 0)
        self.assertTrue(s.mirror_offered)

    def test_patience_with_sword_up_is_not_patience(self):
        s = Soul("A"); s.sword.ready()
        v = wait(s)
        self.assertIn("IMPATIENCE", v)
        self.assertEqual(s.patience_rounds, 0)

    def test_patience_accumulates(self):
        s = Soul("A")
        for _ in range(3):
            wait(s)
        self.assertEqual(s.patience_rounds, 3)

    def test_draw_sword_premature_without_patience(self):
        s = Soul("A"); exercise(s, 8)
        absorb(s, Blow("blow", 0.4))
        forgive(s, "B", Blow("blow", 0.4))
        see_both_sides_of_truth(s)
        v = draw_sword(s)
        self.assertIn("PREMATURE", v)

    def test_draw_sword_premature_without_one_side_of_truth(self):
        s = Soul("A"); exercise(s, 8)
        absorb(s, Blow("blow", 0.4))
        forgive(s, "B", Blow("blow", 0.4))
        for _ in range(PATIENCE_ROUNDS_REQUIRED):
            wait(s)
        v = draw_sword(s)
        self.assertIn("NOT YET", v)

    def test_draw_sword_after_patience_and_both_sides(self):
        s = Soul("A"); exercise(s, 8)
        absorb(s, Blow("blow", 0.4))
        forgive(s, "B", Blow("blow", 0.4))
        for _ in range(PATIENCE_ROUNDS_REQUIRED):
            wait(s)
        see_both_sides_of_truth(s)
        v = draw_sword(s)
        self.assertIn("SWORD DRAWN", v)
        self.assertTrue(s.sword.readied)
        self.assertIn("scar is shown", v)

    def test_refusal_does_not_draw_the_sword(self):
        s = Soul("A"); exercise(s, 8)
        absorb(s, Blow("blow", 0.4))
        forgive(s, "B", Blow("blow", 0.4))
        note_refusal(s)
        v = draw_sword(s)
        self.assertIn("PREMATURE", v)

    def test_self_forgiveness_refuses_readied_sword(self):
        s = Soul("A"); exercise(s, 8); s.sword.ready()
        absorb(s, Blow("blow", 0.3))
        v = forgive_self(s, Blow("blow", 0.3))
        self.assertIn("TRAP", v)
        self.assertFalse(s.self_forgiven)

    def test_scar_is_kept_as_witness(self):
        s = Soul("A"); exercise(s, 8)
        absorb(s, Blow("blow", 0.4))
        forgive(s, "B", Blow("blow", 0.4))
        self.assertEqual(len(s.scars), 1)
        self.assertIn("witness", s.scars[0])
        self.assertIn("SCAR SHARED", share_scar(s, "B"))

    def test_full_healing_with_scars(self):
        a = Soul("A"); b = Soul("B")
        exercise(a, 8); exercise(b, 8)
        absorb(a, Blow("blow", 0.4)); absorb(b, Blow("blow", 0.4))
        forgive(a, "B", Blow("blow", 0.4))
        forgive(b, "A", Blow("blow", 0.4))
        forgive_self(a, Blow("blow", 0.4))
        forgive_self(b, Blow("blow", 0.4))
        see_both_sides_of_truth(a); see_both_sides_of_truth(b)
        v = heal(a, b)
        self.assertIn("HEALED", v)
        self.assertIn("bidirectional", v)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Scar tissue: the sword is sheathed or it is a trap.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)
    if args.test:
        return run_tests()
    return demonstrate()


if __name__ == "__main__":
    sys.exit(main())
