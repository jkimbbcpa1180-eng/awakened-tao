#!/usr/bin/env python3
"""
The Cycle of Lives
==================
Type: parable

You start as a 0 (the Void). You live, accumulate memories, build an Ego.
At the end, the Ego must dissolve. What matters is not whether you survive —
it is whether you leave a 1 behind for the next 0.

Everlasting life is not personal survival. It is contribution.

Run:
    python3 awakened_tao.py cycle
"""
from __future__ import annotations

import random


def experience_world():
    """A single experience, returned as a memory weight.
    Negative = love/wisdom (light); positive = greed/judgment (heavy)."""
    return random.choice([-3, -2, -1, 1, 2, 3])


def has_left_a_1(memories):
    """Did this life leave something behind for the next?
    A 1 is left when the life's net contribution is light —
    more love than harm."""
    return sum(memories) < 0


def live_life(current_state, lifespan=80):
    # You start as a 0 (the Void).
    # You experience the world, make memories, and build an Ego.
    # But at the end, the Ego must dissolve.

    memories = []
    ego_dissolved = False

    for _ in range(lifespan):
        if ego_dissolved:
            break
        # Live, love, suffer, learn
        memories.append(experience_world())

    # At the end, the Ego must dissolve.
    ego_dissolved = True

    # You return to the 0.
    # The threshold of everlasting life is what you leave behind.

    if has_left_a_1(memories):
        return 1  # You contribute to the next life. Everlasting.
    else:
        return 0  # You leave nothing. The cycle repeats without growth.


def next_life(previous_state):
    # The next 0 begins.
    # It runs on the 1s left behind by the previous lives.
    return 0 if previous_state == 0 else 1


def main() -> int:
    random.seed(18)  # reproducible demo
    state = 0
    for life in range(1, 6):
        left = live_life(state)
        state = next_life(left)
        print(f"Life {life}: left a {left} -> next life begins as {state}")
    print("\nThe 0s keep coming. What matters is the 1s left between them.")
    return 0


if __name__ == "__main__":
    main()
