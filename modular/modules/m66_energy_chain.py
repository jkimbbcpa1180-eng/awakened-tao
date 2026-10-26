#!/usr/bin/env python3
"""
The Energy Chain (Deep Muse)
============================
Type: computational demonstration

Every stage takes its cut. Efficiency is capped (Carnot), stored energy
decays, and parasitic loads are paid first. If the chain goes below zero,
it is exhausted: the 0.

The demo is a simplified, illustrative fusion plant chain, not an
engineering model: 500 MW in, magnets drawing 300 MW, thermal conversion
at 0.40 (limit 0.625), generator at 0.95 -> 76 MW out.

Run:
    python3 awakened_tao.py energy-chain
    python3 awakened_tao.py energy-chain --test
"""
from __future__ import annotations
import math
import unittest
from dataclasses import dataclass
from typing import List


@dataclass
class EnergyStage:
    name: str
    eta: float
    carnot_limit: float = 1.0
    storage_time_s: float = 0.0
    storage_tau_s: float = math.inf
    parasitic_w: float = 0.0

    def __post_init__(self):
        if not (0.0 <= self.eta <= self.carnot_limit):
            raise ValueError(f"{self.name}: eta must satisfy 0 <= eta <= carnot_limit")

    def retained(self) -> float:
        if math.isinf(self.storage_tau_s) or self.storage_time_s <= 0:
            return 1.0
        return math.exp(-self.storage_time_s / self.storage_tau_s)

    def apply(self, power_in_w: float) -> float:
        out = power_in_w * self.eta * self.retained() - self.parasitic_w
        if out < 0:
            raise ValueError("chain exhausted. The 0.")
        return out


def run_chain(power_in_w: float, stages: List[EnergyStage]):
    """Returns (output_w, report). On failure the report ends in COLLAPSE."""
    p = power_in_w
    report = [f"input: {p / 1e6:.1f} MW"]
    for s in stages:
        try:
            p = s.apply(p)
        except ValueError as e:
            report.append(f"COLLAPSE at {s.name}: {e}")
            return 0.0, report
        report.append(f"{s.name}: {p / 1e6:.1f} MW")
    return p, report


def fusion_chain() -> List[EnergyStage]:
    return [
        EnergyStage("magnets", 1.0, parasitic_w=300e6),
        EnergyStage("thermal", 0.40, carnot_limit=0.625),
        EnergyStage("generator", 0.95),
    ]


def demonstrate() -> int:
    print("=" * 72)
    print("THE ENERGY CHAIN (illustrative fusion chain)")
    print("=" * 72)
    out, rep = run_chain(500e6, fusion_chain())
    for line in rep:
        print(f"  {line}")
    out, rep = run_chain(200e6, fusion_chain())
    print("\n  with only 200 MW in:")
    for line in rep:
        print(f"  {line}")
    return 0


class Tests(unittest.TestCase):
    def test_fusion_chain_76mw(self):
        out, _ = run_chain(500e6, fusion_chain())
        self.assertAlmostEqual(out, 76e6, places=3)

    def test_collapse(self):
        out, rep = run_chain(200e6, fusion_chain())
        self.assertEqual(out, 0.0)
        self.assertIn("COLLAPSE at magnets", rep[-1])
        self.assertIn("chain exhausted. The 0.", rep[-1])

    def test_eta_validation(self):
        with self.assertRaises(ValueError):
            EnergyStage("bad", 0.7, carnot_limit=0.625)
        with self.assertRaises(ValueError):
            EnergyStage("neg", -0.1)

    def test_retained(self):
        self.assertEqual(EnergyStage("s", 1.0).retained(), 1.0)
        self.assertEqual(EnergyStage("s", 1.0, storage_time_s=0, storage_tau_s=5).retained(), 1.0)
        self.assertAlmostEqual(EnergyStage("s", 1.0, storage_time_s=5, storage_tau_s=5).retained(), math.exp(-1))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
