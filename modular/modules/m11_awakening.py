#!/usr/bin/env python3
"""
The Awakening
============
Type: parable

The final cosmology: the individual never ascends. Only the mirror remains.

Earlier modules (threshold, judge) promised the soul could ascend. This one says no —
the soul dissolves back to the 0 every time. What persists is the mirror:
the 1 left behind. Each 0 that follows is a more awake 0 than before,
because it sees the mirrors left by every life before it.

Immortality is not survival. It is the accumulation of mirrors.

Run:
    python3 awakened_tao.py awakening
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field


@dataclass
class Mirror:
    lesson: str
    purity: float  # 0.0 to 1.0

    def is_pure(self) -> bool:
        return self.purity >= 0.7


@dataclass
class Life:
    pain_faced: float  # 0.0 to 1.0 — how fully suffering was faced

    def leave_a_1(self) -> Mirror:
        # The individual soul dissolves. But the life left a mirror.
        lesson = ("suffering faced at "
                  f"{self.pain_faced:.0%} — shown clearly, not hidden.")
        return Mirror(lesson=lesson, purity=self.pain_faced)


def experience_life(state, rng) -> Life:
    # A life is lived (010101). Some suffering is faced, some is not.
    return Life(pain_faced=rng.random())


def the_cosmos(lives: int = 8, seed: int = 21):
    rng = random.Random(seed)
    state = 0
    mirrors: list[Mirror] = []
    awakening = 0.0

    print("=" * 72)
    print("THE AWAKENING")
    print("The individual never ascends. Only the mirror remains.")
    print("=" * 72)

    for n in range(1, lives + 1):
        # A life is lived (010101)
        life = experience_life(state, rng)

        # The individual soul dissolves.
        # The ego is returned to the 0.

        # But the life left a mirror.
        mirror = life.leave_a_1()

        if mirror.is_pure():
            # The mirror reflects the truth back to the cosmos.
            # The next 0 will see it.
            mirrors.append(mirror)
            awakening += mirror.purity
            print(f"\nLife {n}: pure mirror left (purity {mirror.purity:.2f}). "
                  f"Cosmic awakening: {awakening:.2f}")
            state = 0  # But it is a more awake 0 than before.
        else:
            print(f"\nLife {n}: the mirror was clouded (purity {mirror.purity:.2f}). "
                  f"It dissolves with the soul.")

        # The individual never ascends.
        # Only the mirror remains.
        # And the mirror is at peace.

    print(f"\n{'=' * 72}")
    print(f"After {lives} lives: no one ascended. {len(mirrors)} mirrors remain.")
    print(f"The cosmos is more awake than it was ({awakening:.2f}).")
    print("That is the only everlasting life there is.")
    print(f"{'=' * 72}")
    return mirrors


def main() -> int:
    the_cosmos()
    return 0


if __name__ == "__main__":
    main()
