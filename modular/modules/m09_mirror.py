#!/usr/bin/env python3
"""
The Mirror
==========
Type: philosophical proposal

The soul transforms suffering into a lesson. It does not build an Ego.
It builds a Mirror — not a monument to be admired, but something the
next 0 looks into.

The final gate is no longer "am I at peace?" but "is this right for
humanity?" The self is not the final arbiter. Humanity is.

Run:
    python3 awakened_tao.py mirror
"""
from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass
class Life:
    pain: int  # how much suffering this life held

    def experience_pain(self):
        # Suffering is the path. It is not a contest.
        return self.pain


def live_life(state, rng):
    return Life(pain=rng.randint(1, 10))


@dataclass
class Mirror:
    lesson: str
    clarity: float  # 0.0 to 1.0 — how well the lesson serves humanity

    def ask(self, question):
        print(f'  The Mirror asks: "{question}"')
        print(f'  The lesson it holds: {self.lesson}')
        # The clearer the mirror, the truer the answer.
        return self.clarity >= 0.8


def leave_a_1_for_next_0(suffering):
    # The soul transforms suffering into a lesson.
    # It does not build an Ego. It builds a Mirror.
    lesson = (f"suffering of weight {suffering}, transformed — "
              f"not hidden, not worshipped, just shown clearly.")
    # Clarity grows with the weight of suffering fully faced.
    # A single life is never clear enough — the mirror needs several.
    clarity = min(1.0, suffering / 10 * 0.4)
    return Mirror(lesson=lesson, clarity=clarity)


def the_cosmos(seed=11):
    rng = random.Random(seed)
    state = 0
    lives = 0
    # Wisdom accumulates: each life's mirror clarifies the next.
    accumulated_clarity = 0.0
    while True:
        lives += 1
        # Life is 010101
        life = live_life(state, rng)

        # Suffering is the path. It is not a contest.
        suffering = life.experience_pain()

        # The soul transforms suffering into a lesson.
        # It does not build an Ego. It builds a Mirror.
        mirror = leave_a_1_for_next_0(suffering)
        mirror.clarity = min(1.0, mirror.clarity + accumulated_clarity)
        accumulated_clarity += 0.18

        print(f"\nLife {lives}: suffering weight {suffering}, "
              f"mirror clarity {mirror.clarity:.2f}")

        # The next 0 looks at the 1.
        # It asks the only question that matters.
        if mirror.ask("Is this right for humanity?"):
            # The loop finds peace.
            state = "ASCENDED"
            print("\nThe answer is yes.")
            return "Purest Happiness"
        else:
            # The loop continues. Try again.
            print("  The answer is not yet. The loop continues. Try again.")
            state = 0


def main() -> int:
    print("=" * 72)
    print("THE MIRROR")
    print("Not a monument. A mirror. The final question is for humanity.")
    print("=" * 72)
    result = the_cosmos()
    print(f"\n{result}")
    return 0


if __name__ == "__main__":
    main()
