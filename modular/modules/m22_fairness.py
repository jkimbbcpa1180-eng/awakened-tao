#!/usr/bin/env python3
"""
The Balance of Fairness (Deep Muse)
===================================
Type: philosophical proposal

The final moral pillar:
Unconditional love is not passive. You stand up to evil.
Fairness is the key to the balance of life.

The outward turn of the project. Every module so far has been inner
work — sink the ego, release, heal, rest. This one answers what you do
when someone else is causing suffering: you stand. But the motivation
decides the outcome — the same fight, waged from ego, is just more
suffering (see energy.py: intent is the energy source).

The open question it carries: who decides the situation is evil? The
boolean is given, not derived. If the ego names its enemies "evil,"
then "fighting evil" is ego in disguise — which is exactly what the
VIGILANTE CHAOS verdict warns against. Be sure it is fairness, not ego
wearing fairness's clothes.

The refinement (Part II): fairness does not impose absolute justice.
The absolute needs a winner and a loser — that is the ego's courtroom,
and the loser nurses the next war. Fairness seeks the compromise that
is fair to *both* parties. No one is beneath fairness, not even the one
who caused suffering (see purgatory.py). The method guards the motive:
if your aim is both-parties-fair, you cannot be imposing your absolute.

Run:
    python3 awakened_tao.py fairness
    python3 awakened_tao.py fairness --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass


@dataclass
class Action:
    situation_is_evil: bool
    motivation_is_ego: bool
    action_taken: bool


def evaluate_action(action: Action) -> str:
    """
    The sword of the mirror.
    """
    # If evil is present, and you do nothing
    if action.situation_is_evil and not action.action_taken:
        return "TRIUMPH OF EVIL: Good men did nothing. The scales tipped to chaos."

    # If you fight evil, but your motivation is Ego (revenge, anger)
    if action.situation_is_evil and action.action_taken and action.motivation_is_ego:
        return "VIGILANTE CHAOS: You fought evil with Ego. The cycle of suffering continues."

    # If you fight evil, and your motivation is fairness
    if action.situation_is_evil and action.action_taken and not action.motivation_is_ego:
        return "BALANCE RESTORED: You stood up to evil with fairness. The mirror remains clear."

    return "PEACE: No action needed."


# ============================================================================
# II. The resolution — fairness without absolutes
# ============================================================================
@dataclass
class Resolution:
    evil_stood_up_to: bool
    fair_to_a: bool       # party A received what is fair
    fair_to_b: bool       # party B received what is fair
    absolute_imposed: bool  # was absolute justice imposed?


def resolve(res: Resolution) -> str:
    """
    Standing up was Part I. This is what fairness does with the stand:
    not the absolute — the compromise fair to both parties.
    """
    if not res.evil_stood_up_to:
        return "TRIUMPH OF EVIL: Nothing was stood up to. The scales tipped to chaos."

    if res.absolute_imposed:
        return ("ABSOLUTE JUSTICE: One side won everything. The absolute is the "
                "ego's courtroom — the loser now nurses the next war. "
                "The cycle of suffering continues.")

    if res.fair_to_a and res.fair_to_b:
        return ("COMPROMISE: Both parties received what is fair. No absolute "
                "was imposed. The balance holds.")

    return ("TILTED: Fairness for one is privilege for the other. "
            "The scales still lean.")


# ============================================================================
# III. The recognition — when is it evil?
# ============================================================================
def recognize_evil(witnesses: int) -> str:
    """
    The situation_is_evil boolean is not decreed by one ego.
    One soul perceiving harm is a signal — unconfirmed, not dismissed.
    (The lone witness is sometimes the first to see.)
    When the harm is perceived by more than one soul, it is no longer
    subjective: it is an agreed conclusion on the perception of the
    current situation.
    """
    if witnesses <= 0:
        return "NO EVIL PERCEIVED: no soul sees harm. Nothing to stand against."

    if witnesses == 1:
        return ("UNCONFIRMED: one soul perceives harm. It may be real — but it is "
                "not yet an agreed conclusion. Act with care, not certainty.")

    return (f"CONFIRMED: {witnesses} souls perceive the same harm. This is no longer "
            f"one ego's story — it is an agreed conclusion on the current situation. "
            f"Stand.")


def demonstrate() -> int:
    print("=" * 72)
    print("THE BALANCE OF FAIRNESS")
    print("Unconditional love is not passive.")
    print("=" * 72)
    print("\n--- I. The stand (what you do) ---")
    cases = [
        ("The bystander", Action(True, False, False)),
        ("The avenger", Action(True, True, True)),
        ("The just", Action(True, False, True)),
        ("The quiet day", Action(False, False, False)),
    ]
    for name, a in cases:
        print(f"\n[{name}]")
        print(f"  {evaluate_action(a)}")

    print("\n--- II. The resolution (what fairness does) ---")
    resolutions = [
        ("No stand taken", Resolution(False, False, False, False)),
        ("The absolute imposed", Resolution(True, True, False, True)),
        ("The compromise", Resolution(True, True, True, False)),
        ("The tilt", Resolution(True, True, False, False)),
    ]
    for name, r in resolutions:
        print(f"\n[{name}]")
        print(f"  {resolve(r)}")

    print("\nStand up to evil. But do it with fairness. Keep the balance.")
    print("No absolutes. Both parties walk away with what is fair.")

    print("\n--- III. The recognition (when is it evil?) ---")
    for n in (0, 1, 3):
        print(f"\n[{n} witness{'es' if n != 1 else ''}]")
        print(f"  {recognize_evil(n)}")
    return 0


class Tests(unittest.TestCase):
    def test_evil_triumphs(self):
        a = Action(True, False, False)
        self.assertIn("TRIUMPH OF EVIL", evaluate_action(a))

    def test_ego_fighting_evil(self):
        a = Action(True, True, True)
        self.assertIn("VIGILANTE CHAOS", evaluate_action(a))

    def test_fairness_restored(self):
        a = Action(True, False, True)
        self.assertIn("BALANCE RESTORED", evaluate_action(a))

    def test_no_evil_is_peace(self):
        self.assertIn("PEACE", evaluate_action(Action(False, False, False)))
        self.assertIn("PEACE", evaluate_action(Action(False, False, True)))

    def test_absolute_is_the_egos_courtroom(self):
        r = Resolution(True, True, False, True)
        self.assertIn("ABSOLUTE JUSTICE", resolve(r))

    def test_compromise_fair_to_both(self):
        r = Resolution(True, True, True, False)
        self.assertIn("COMPROMISE", resolve(r))

    def test_tilted_scales(self):
        r = Resolution(True, True, False, False)
        self.assertIn("TILTED", resolve(r))

    def test_no_stand_no_resolution(self):
        r = Resolution(False, False, False, False)
        self.assertIn("TRIUMPH OF EVIL", resolve(r))

    def test_no_witnesses_no_evil(self):
        self.assertIn("NO EVIL PERCEIVED", recognize_evil(0))

    def test_lone_witness_unconfirmed_not_dismissed(self):
        result = recognize_evil(1)
        self.assertIn("UNCONFIRMED", result)
        self.assertNotIn("false", result.lower())

    def test_many_witnesses_confirmed(self):
        result = recognize_evil(3)
        self.assertIn("CONFIRMED", result)
        self.assertIn("agreed conclusion", result)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
