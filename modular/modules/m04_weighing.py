#!/usr/bin/env python3
"""
The Weighing of the Heart
=========================
Type: parable

At death, the heart is weighed against the feather of Maat.
In the fused narrative ("The Cycle of the Awakened Light"):
memories of love and wisdom are light; memories of greed and
judgment are heavy. The Ego (the Adversary) must dissolve for
the heart to be light.

Sign convention (assumption — see note below):
  each memory is a number. Acts of love and wisdom are negative
  (they lighten the heart); acts of greed and judgment are positive
  (they weigh it down). A net weight below the threshold means
  the heart is lighter than the feather.

Run:
    python3 awakened_tao.py weighing
"""
from __future__ import annotations


def process_life(memories, ego_attachments, threshold=0):
    """
    At the end of a life, the Ego dissolves.
    The memories are judged by their weight.
    """
    # The ego is the Adversary. It must die.
    ego_attachments = 0

    # Memories of love and wisdom are light.
    # Memories of greed and judgment are heavy.
    weight = sum(memories) + ego_attachments

    if weight < threshold:
        return "Purest Happiness: Return to the Cosmos"
    else:
        return "Rebirth: The memories carry forward to learn again"


def main() -> int:
    # A life of more love than harm: light heart.
    light_life = [-3, -2, -5, 1, -1]      # kindnesses outweigh one cruelty
    # A life of more harm than love: heavy heart.
    heavy_life = [4, 3, -1, 5, 2]          # greed and judgment dominate

    print(f"Light life -> {process_life(light_life, ego_attachments=99)}")
    print(f"Heavy life -> {process_life(heavy_life, ego_attachments=99)}")
    print("\nNote: ego_attachments is accepted and then dissolved to 0,")
    print("because the Adversary must die before the weighing.")
    return 0


if __name__ == "__main__":
    main()
