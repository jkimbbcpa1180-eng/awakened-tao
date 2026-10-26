#!/usr/bin/env python3
"""
The Survival Log (Deep Muse)
============================
Type: computational demonstration

An empty template for tracking a day: stress, nicotine, release, stimulus.

It ships with no real data. The demo and tests use obviously synthetic
entries labelled 'sample'.

Run:
    python3 awakened_tao.py survival-log
    python3 awakened_tao.py survival-log --test
"""
from __future__ import annotations
import unittest
from dataclasses import dataclass, field
from typing import List


@dataclass
class DailyEntry:
    day: str
    cycle_day: int
    stress: float
    nicotine_mg: float
    released: bool
    stimulus: str
    note: str = ""


@dataclass
class SurvivalLog:
    entries: List[DailyEntry] = field(default_factory=list)

    def add(self, entry: DailyEntry) -> None:
        self.entries.append(entry)

    def average_stress_on_released_days(self) -> float:
        vals = [e.stress for e in self.entries if e.released]
        return sum(vals) / len(vals) if vals else 0.0


def _samples() -> List[DailyEntry]:
    return [
        DailyEntry("sample-day-1", 1, 6.0, 4.0, True, "sample stimulus", "sample"),
        DailyEntry("sample-day-2", 2, 8.0, 6.0, False, "sample stimulus", "sample"),
        DailyEntry("sample-day-3", 3, 4.0, 2.0, True, "sample stimulus", "sample"),
    ]


def demonstrate() -> int:
    print("=" * 72)
    print("THE SURVIVAL LOG (empty template; sample entries only)")
    print("=" * 72)
    log = SurvivalLog()
    print(f"\n  empty log: average stress on released days = {log.average_stress_on_released_days()}")
    for e in _samples():
        log.add(e)
    print(f"  with {len(log.entries)} sample entries: average = {log.average_stress_on_released_days()}")
    return 0


class Tests(unittest.TestCase):
    def test_empty_template(self):
        self.assertEqual(SurvivalLog().entries, [])
        self.assertEqual(SurvivalLog().average_stress_on_released_days(), 0.0)

    def test_sample_average(self):
        log = SurvivalLog()
        for e in _samples():
            log.add(e)
        self.assertEqual(len(log.entries), 3)
        self.assertEqual(log.average_stress_on_released_days(), 5.0)

    def test_none_released_fallback(self):
        log = SurvivalLog()
        log.add(DailyEntry("sample", 1, 9.0, 0.0, False, "sample", "sample"))
        self.assertEqual(log.average_stress_on_released_days(), 0.0)


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
