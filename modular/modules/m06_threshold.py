#!/usr/bin/env python3
"""
The Threshold
=============
Type: parable

Judgment day is not external. It is the soul evaluating itself.
There is no punishment. Only data collection.

The soul ascends when change is complete and guilt is released.
Otherwise it returns to the 0 — not damned, just unfinished —
to try again and find peace.

Run:
    python3 awakened_tao.py threshold
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field


@dataclass
class SoulMemory:
    """What a soul carries between lives. Not a score — a record."""
    change_is_complete: bool = False
    guilt_is_released: bool = False
    lives_lived: int = 0
    ones_left: int = 0  # how many 1s this soul has left for the next 0s


def the_threshold(soul_memory):
    """
    Judgment day is not external. It is the soul evaluating itself.
    """
    # The soul asks: "Do I believe I should get eternal life?"
    # This is measured by conscious guilt and the changes made.

    if soul_memory.change_is_complete and soul_memory.guilt_is_released:
        print("You have left a 1 for the next 0.")
        print("Welcome to Eternal Life.")
        return "ASCENDED"

    else:
        # There is no punishment. Only data collection.
        print("The lesson is not yet learned. The change is not yet complete.")
        print("Return to the 0. Try again. Find peace.")
        return "REINCARNATE"


def the_cosmos(seed=7):
    rng = random.Random(seed)
    soul = SoulMemory()
    state = 0
    while True:
        # Life is 010101
        soul.lives_lived += 1
        left_a_1 = rng.random() < 0.35  # some lives leave a 1, most leave 0
        if left_a_1:
            soul.ones_left += 1
        print(f"\n--- Life {soul.lives_lived} (began as {state}): "
              f"left a {1 if left_a_1 else 0} ---")

        # Data collection: the soul learns across lives.
        # Change completes and guilt releases gradually, never punitively.
        if soul.ones_left >= 2 and soul.lives_lived >= 3:
            soul.change_is_complete = True
        if soul.change_is_complete and rng.random() < 0.5:
            soul.guilt_is_released = True

        memory = soul
        result = the_threshold(memory)

        if result == "ASCENDED":
            break  # The loop ends in pure happiness.
        else:
            state = 0  # The loop continues. Try again.

    print(f"\nAscended after {soul.lives_lived} lives, "
          f"leaving {soul.ones_left} ones behind for the next 0s.")


def main() -> int:
    the_cosmos()
    return 0


if __name__ == "__main__":
    main()
