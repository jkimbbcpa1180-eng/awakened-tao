#!/usr/bin/env python3
"""
The Prism (Deep Muse)
=====================
Type: parable

Two revelations, one light.

Part I — The Prism of Life: one soul's density refracts the source light
into the colors of lived experience — suffering, joy, compassion, awe.
Density is not just obstacle; it is the medium. Too dense (>0.9) and the
ego goes opaque; zero density and there is nothing to refract — without
the friction of life, no spectrum. Just a flat line.

Part II — The Prism of Light: life isn't one individual mirror but a prism.
Many souls are facets; each, at its own angle, catches one color of the one
light. No facet shows the whole spectrum. The density of Part I is why the
colors differ; the multitude is why the spectrum completes.

A mirror bounces light off the surface. A prism lets it pass through —
and the light penetrates the soul to truth.

Run:
    python3 awakened_tao.py prism
    python3 awakened_tao.py prism --test
"""
from __future__ import annotations

import unittest
from dataclasses import dataclass, field
from typing import List


# ============================================================================
# Part I — The Prism of Life: density refracts
# ============================================================================
@dataclass
class SoulPrism:
    source_light: float  # 1.0 = pure unconditional love from the source
    density: float       # The weight of the Ego and suffering (0.0 to 1.0)
    colors_revealed: List[str] = field(default_factory=list)


def refract_light(soul: SoulPrism) -> str:
    """
    The physics of spiritual light.
    """
    # If the soul is too dense (Ego), the light cannot penetrate.
    if soul.density > 0.9:
        return "OPAQUE: The Ego is too dense. The light cannot pass through. You are in the 0."

    # If the soul has no density (no life, no suffering), there is no prism.
    if soul.density == 0.0:
        return "EMPTY: Without the friction of life, there is nothing to refract. Just a flat line."

    # The light penetrates the density of life and splits into colors.
    if 0.0 < soul.density <= 0.9 and soul.source_light > 0:
        spectrum = " & ".join(soul.colors_revealed)
        return f"TRUTH ILLUMINATED: The light penetrates the soul. The spectrum reveals {spectrum}."


# ============================================================================
# Part II — The Prism of Light: many facets, one spectrum
# ============================================================================
SPECTRUM = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]


@dataclass
class Soul:
    name: str
    angle: float     # the angle at which this soul meets the light (degrees)
    clarity: float   # how clear the facet is (0.0 to 1.0)


def facet_color(soul: Soul) -> str:
    """The color this facet catches — determined by its angle to the light."""
    index = int((soul.angle % 360) / 360 * len(SPECTRUM))
    return SPECTRUM[index]


def receive_light(soul: Soul) -> str:
    """
    A mirror reflects off the surface. A prism lets the light through.
    Clouded facets bounce; clear ones are penetrated.
    """
    if soul.clarity < 0.3:
        return (f"[{soul.name}] CLOUDED: the light bounces off the surface — "
                f"a mirror, not a prism. Nothing penetrates.")
    color = facet_color(soul)
    return (f"[{soul.name}] {color.upper()}: the light passed through and emerged "
            f"as {color} — one true color, but not the whole light.")


def behold_prism(souls: list) -> str:
    clear = [s for s in souls if s.clarity >= 0.3]
    if not clear:
        return "DARKNESS: every facet is clouded. The light cannot enter."
    colors = {facet_color(s) for s in clear}
    if len(colors) == 1:
        only = next(iter(colors))
        return (f"ONE COLOR: every clear facet shows {only}. True — but a single "
                f"band is not the spectrum. Do not call the facet the prism.")
    if len(colors) == len(SPECTRUM):
        return ("FULL SPECTRUM: truth in all colors. No single soul held it; "
                "the prism held it together. This is what the many are for.")
    return (f"PARTIAL SPECTRUM: {len(colors)} of {len(SPECTRUM)} colors visible. "
            f"More facets, more truth. Keep turning the prism.")


# ============================================================================
# Demonstration — both refractions
# ============================================================================
def demonstrate() -> int:
    print("=" * 72)
    print("THE PRISM")
    print("=" * 72)

    print("\n--- I. The Prism of Life (density refracts) ---")
    for soul in (
        SoulPrism(1.0, 0.95, ["darkness"]),
        SoulPrism(1.0, 0.0, []),
        SoulPrism(1.0, 0.5, ["suffering", "joy", "compassion", "awe"]),
    ):
        print(f"\n  {refract_light(soul)}")

    print("\n--- II. The Prism of Light (many facets, one spectrum) ---")
    souls = [
        Soul("The elder", angle=10, clarity=0.9),
        Soul("The child", angle=140, clarity=0.8),
        Soul("The stranger", angle=260, clarity=0.85),
        Soul("The clouded one", angle=90, clarity=0.1),
    ]
    for s in souls:
        print(f"\n  {receive_light(s)}")
    print(f"\n  {behold_prism(souls)}")

    print("\nYou are not a mirror. You are a prism. Let the truth penetrate you.")
    return 0


# ============================================================================
# Tests
# ============================================================================
class Tests(unittest.TestCase):

    # Part I — density
    def test_opaque_ego(self):
        soul = SoulPrism(1.0, 0.95, ["darkness"])
        self.assertIn("OPAQUE", refract_light(soul))

    def test_empty_soul(self):
        soul = SoulPrism(1.0, 0.0, [])
        self.assertIn("EMPTY", refract_light(soul))

    def test_prism_illuminated(self):
        soul = SoulPrism(1.0, 0.5, ["suffering", "joy", "compassion", "awe"])
        self.assertIn("TRUTH ILLUMINATED", refract_light(soul))
        self.assertIn("compassion", refract_light(soul))

    # Part II — facets
    def test_angle_determines_color(self):
        self.assertEqual(facet_color(Soul("a", 10, 0.9)), "red")
        self.assertEqual(facet_color(Soul("b", 200, 0.9)), "green")

    def test_clouded_facet_bounces(self):
        self.assertIn("CLOUDED", receive_light(Soul("c", 90, 0.1)))

    def test_clear_facet_penetrated(self):
        result = receive_light(Soul("d", 120, 0.9))
        self.assertIn("YELLOW", result)
        self.assertIn("not the whole light", result)

    def test_single_color_is_not_the_spectrum(self):
        souls = [Soul("a", 10, 0.9), Soul("b", 20, 0.9)]
        self.assertIn("ONE COLOR", behold_prism(souls))

    def test_many_facets_full_spectrum(self):
        souls = [Soul(f"s{i}", i * 52, 0.9) for i in range(7)]
        self.assertIn("FULL SPECTRUM", behold_prism(souls))

    def test_all_clouded_is_darkness(self):
        souls = [Soul("a", 10, 0.1), Soul("b", 200, 0.2)]
        self.assertIn("DARKNESS", behold_prism(souls))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
