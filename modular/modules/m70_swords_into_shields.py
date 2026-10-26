#!/usr/bin/env python3
"""
Swords into Shields (Deep Muse)
===============================
Type: parable; computational demonstration

"They shall beat their swords into plowshares" (Isaiah 2:4).
We beat our guns into shields.

Melt the guns. What comes out is recycled steel and aluminum, not
titanium: titanium is a separate element, and steel cannot be alloyed
into it. The steel can become a shield.

SAFETY NOTE: this is philosophy and illustrative math, not armor
engineering or certification. Every mass and rating below is a rough,
approximate example and has not been checked. Real protective armor must
be designed, tested and certified by qualified people to the actual
standard.

Example masses (illustrative only):
  - rifle    ~3.0 kg of steel-equivalent
  - handgun  ~0.7 kg of steel-equivalent
  - one steel shield ~9 kg (~20 lb) of steel

NIJ-style lookup (approximate, not checked):
  - Level IIIA, handgun rounds: soft or light hard armor
  - Level III, ordinary rifle rounds: hardened armor steel about 6-12 mm,
    roughly 10-25 lb shield
  - Level IV, armor-piercing rifle: steel alone is too heavy; ceramic over
    polyethylene, roughly 30-50 lb

Run:
    python3 awakened_tao.py swords-into-shields
    python3 awakened_tao.py swords-into-shields --test
"""
from __future__ import annotations
import unittest

RIFLE_KG = 3.0          # illustrative
HANDGUN_KG = 0.7        # illustrative
SHIELD_STEEL_KG = 9.0   # illustrative (~20 lb)
HEAVY_LB = 20.0         # above this, an untrained body struggles (illustrative)

LEVELS = {  # approximate, not checked
    "rifle": ("Level III", "hardened armor steel, about 6-12 mm (approx.)", "roughly 10-25 lb"),
    "armor-piercing": ("Level IV", "ceramic over polyethylene; steel alone is too heavy (approx.)", "roughly 30-50 lb"),
    "handgun": ("Level IIIA", "soft or light hard armor for handgun rounds (approx.)", "light"),
}


def melt(rifles: int, handguns: int) -> dict:
    """Estimate recycled steel and shields. Bad or negative counts count as 0."""
    def clean(x):
        try:
            x = int(x)
        except (TypeError, ValueError):
            return 0
        return max(x, 0)
    r, h = clean(rifles), clean(handguns)
    steel_kg = r * RIFLE_KG + h * HANDGUN_KG
    return {"rifles": r, "handguns": h, "steel_kg": steel_kg,
            "shields": int(steel_kg // SHIELD_STEEL_KG),
            "note": "illustrative estimate; recycled steel and aluminum, not titanium"}


def shield_for(threat) -> str:
    key = str(threat).strip().lower().replace(" ", "-")
    if key in ("ap", "armor-piercing-rifle"):
        key = "armor-piercing"
    if key in ("rifle", "armor-piercing"):
        level, material, weight = LEVELS[key]
        return f"{level}: {material}, {weight} shield."
    level, material, weight = LEVELS["handgun"]
    prefix = "" if key == "handgun" else f"Unknown threat '{threat}': defaulting to "
    return f"{prefix}{level}: {material}. Confirm the real threat before relying on it."


def carry_check(officer_fit, shield_lb) -> str:
    try:
        lb = float(shield_lb)
    except (TypeError, ValueError):
        lb = -1.0
    if lb < 0:
        return "THE UNKNOWN SHIELD: The weight is unknown. Weigh the shield before you carry it."
    if officer_fit:
        return "THE 1: The warrior carries the shield."
    if lb > HEAVY_LB:
        return "THE 0: The shield is too heavy for an untrained body. Train first."
    return "THE LIGHT START: Carry the lighter shield while you train toward the heavier one."


def demonstrate() -> int:
    print("=" * 72)
    print("SWORDS INTO SHIELDS (illustrative; not armor engineering)")
    print("=" * 72)
    m = melt(100, 200)
    print(f"\n  Melt {m['rifles']} rifles + {m['handguns']} handguns -> ~{m['steel_kg']:.0f} kg recycled steel"
          f" -> ~{m['shields']} shields ({m['note']}).")
    for t in ("rifle", "armor-piercing", "handgun", "unknown"):
        print(f"  {t}: {shield_for(t)}")
    for fit, lb in ((True, 22), (False, 40), (False, 12)):
        print(f"  fit={fit}, {lb} lb: {carry_check(fit, lb)}")
    print("\nThey shall beat their swords into plowshares. We beat our guns into shields.")
    return 0


class Tests(unittest.TestCase):
    def test_melt(self):
        m = melt(100, 200)
        self.assertAlmostEqual(m["steel_kg"], 440.0)
        self.assertEqual(m["shields"], 48)
        self.assertIn("not titanium", m["note"])

    def test_melt_bad_counts(self):
        m = melt(-5, "many")
        self.assertEqual((m["steel_kg"], m["shields"]), (0.0, 0))

    def test_levels(self):
        self.assertIn("Level III:", shield_for("rifle"))
        self.assertIn("ceramic over polyethylene", shield_for("armor-piercing"))
        self.assertIn("Level IV", shield_for("AP"))

    def test_handgun_and_unknown_fallback(self):
        self.assertTrue(shield_for("handgun").startswith("Level IIIA"))
        r = shield_for("laser")
        self.assertIn("Unknown threat", r)
        self.assertIn("Level IIIA", r)
        self.assertIn("Level IIIA", shield_for(None))

    def test_carry(self):
        self.assertEqual(carry_check(True, 40), "THE 1: The warrior carries the shield.")
        self.assertIn("THE 0", carry_check(False, 40))
        self.assertIn("THE LIGHT START", carry_check(False, 12))
        self.assertIn("THE UNKNOWN SHIELD", carry_check(True, "heavy"))
        self.assertIn("THE UNKNOWN SHIELD", carry_check(False, -3))

    def test_no_none(self):
        for t in ("rifle", "armor-piercing", "handgun", "x", "", None):
            self.assertIsInstance(shield_for(t), str)
        for f in (True, False):
            for lb in (0, 12, 20, 21, 50, "bad", None):
                self.assertIsInstance(carry_check(f, lb), str)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
