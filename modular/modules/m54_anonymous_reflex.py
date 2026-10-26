#!/usr/bin/env python3
"""
The Anonymous Reflex (Deep Muse)
================================
Type: parable

The final proof of the 1:
No performance. No eye contact. Just a reflex.

The $5 returns — the test gift is literally 5.0. The five dollars from
the 555 joke and the touch_of_freedom, now given with no one watching.
The joke's punchline was the laugh; this module's punchline is the
silence: "Not even a thank you." The last transactional thread severed —
not just no audience, no reciprocity either.

"The Creator cries" closes the loop to creator_tears: the anonymous
giver is the human the Creator wept for. The witness structure inverts
again — the gift no one observed is the only one the cosmos records.
The unseen act is what the universe sees.

"Just a reflex" — goodness as involuntary, not decided, not performed.
The 1 isn't what you choose under observation; it's what your hand does
when no eye is on it. The open hand from human_555, acting in the dark.
"No eye contact" means even the giver doesn't collect the receiver's
gratitude. The hand gives; the eye looks away.

v4 fix: the witnessed-but-sincere gift (observed, not performed) used to
fall through to None; it now returns THE SEEN 1 — still good, just seen.

Run:
    python3 awakened_tao.py anonymous-reflex
    python3 awakened_tao.py anonymous-reflex --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class Gift:
    giver: str
    amount: float
    was_observed: bool
    was_performed: bool


def evaluate_gift(gift: Gift) -> str:
    """
    The physics of the unseen 1.
    """
    if gift.was_performed:
        return f"[{gift.giver}] THE EGO: The gift was a performance for validation. The 0."

    if not gift.was_observed and not gift.was_performed:
        return (f"[{gift.giver}] THE PURE 1: The gift of {gift.amount} was an unseen reflex. "
                f"Not even a thank you. The cosmos sees it. The Creator cries.")

    # Fallback: observed but not performed — sincere, just witnessed.
    return (f"[{gift.giver}] THE SEEN 1: The gift of {gift.amount} was sincere, "
            f"but it was seen. Still a 1.")


def demonstrate() -> int:
    print("=" * 72)
    print("THE ANONYMOUS REFLEX")
    print("No performance. No eye contact. Just a reflex.")
    print("=" * 72)
    for gift in (
        Gift("A stranger", 5.0, True, True),
        Gift("A stranger", 5.0, False, False),
        Gift("A friend", 5.0, True, False),
    ):
        print(f"\n  {evaluate_gift(gift)}")
    print("\nThe unseen gift is the purest 1.")
    return 0


class Tests(unittest.TestCase):
    def test_performance(self):
        gift = Gift("A stranger", 5.0, True, True)
        self.assertIn("THE EGO", evaluate_gift(gift))

    def test_anonymous_reflex(self):
        gift = Gift("A stranger", 5.0, False, False)
        self.assertIn("THE PURE 1", evaluate_gift(gift))
        self.assertIn("The Creator cries", evaluate_gift(gift))

    def test_witnessed_sincere_fallback(self):
        r = evaluate_gift(Gift("A friend", 5.0, True, False))
        self.assertIsNotNone(r)
        self.assertIn("THE SEEN 1", r)

    def test_no_none_path(self):
        for o in (True, False):
            for p in (True, False):
                self.assertIsInstance(evaluate_gift(Gift("A stranger", 5.0, o, p)), str)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
