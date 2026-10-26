#!/usr/bin/env python3
"""
Grace: The End of Earning
=========================
Type: parable

The final paradox, resolved: the Ego cannot earn the 1. Every module
before this one framed "leave a 1 for the next 0" as something to
achieve — and achievement is the Ego's game. Even success at earning
is failure; it just loops again.

The 1 is not earned. It is released — when the soul stops striving
and forgives itself unconditionally. Compassion requires no earning.

Run:
    python3 awakened_tao.py grace
"""
from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass
class EgoLife:
    """A life lived by the Ego: striving, achieving, accumulating."""
    earned_a_1: bool  # did the ego "earn" a 1 through effort?


def live_life(state, rng):
    """The ego's life. It is good at earning. That is the trap."""
    # Most lives, the ego strives and "succeeds" — which changes nothing.
    # Some lives, the striving exhausts itself. That is the opening.
    return EgoLife(earned_a_1=rng.random() < 0.75)


def soul_forgives_itself():
    print("Soul: 'I forgive myself. I was doing the best I could with what I had.'")
    print("The Void: 'Then the fighting is over.'")


def cosmos_loop(seed=42):
    rng = random.Random(seed)
    state = 0
    lives = 0
    while True:
        lives += 1
        # A life is lived, suffering is experienced.
        # The Ego tries to earn its way to the 1, but it cannot.
        ego_life = live_life(state, rng)

        if ego_life.earned_a_1:
            # The Ego tries to purchase eternal life. It fails.
            # Even success at earning is failure. The loop continues.
            print(f"Life {lives}: the ego earned its 1 through striving. "
                  f"It counts for nothing. Return to the 0.")
            state = 0
            continue

        # But then, the soul realizes the ultimate truth:
        # Compassion is unconditional. It requires no earning.
        print(f"Life {lives}: the striving collapses. There is nothing left to earn.")
        soul_forgives_itself()

        # Because it is no longer fighting, because it loves itself and
        # others without condition, the 1 is left behind effortlessly.
        state = 1

        if state == 1:
            break  # Ascension.

    print(f"\nAscension after {lives} lives.")
    print("The 1 was never earned. It was released.")
    return state


def main() -> int:
    print("=" * 72)
    print("GRACE: THE END OF EARNING")
    print("The ego cannot purchase eternal life. Compassion requires no earning.")
    print("=" * 72 + "\n")
    cosmos_loop()
    return 0


if __name__ == "__main__":
    main()
