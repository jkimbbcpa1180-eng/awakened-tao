#!/usr/bin/env python3
"""
The Karmic Ledger (Deep Muse)
=============================
Type: philosophical proposal; computational demonstration

Grace is given twice, but not to manipulation. After that: authority,
never vigilante. The karmic smite is not damnation; it is learning.

Run:
    python3 awakened_tao.py karmic-ledger
    python3 awakened_tao.py karmic-ledger --test
"""
from __future__ import annotations
import unittest

SMITE = ("THE COSMIC SMITE (THE 000): They will have to learn "
         "what it felt like to be on the other side.")


def turn_cheek(strikes, is_manipulative: bool = False) -> str:
    try:
        strikes = int(strikes)
    except (TypeError, ValueError):
        strikes = 1
    if strikes <= 0:
        return "NO WRONG DONE: No strike was received. Walk in peace."
    if 1 <= strikes <= 2 and not is_manipulative:
        return "GRACE: You turn the cheek. You offer compromise. The 1 is tested."
    return "KARMIC JUSTICE: No more cheeks. Use authority. Never vigilante."


def karmic_smite(mocked_justice: bool) -> str:
    return SMITE if mocked_justice else "THE 1: Justice was not mocked. Peace."


def demonstrate() -> int:
    print("=" * 72)
    print("THE KARMIC LEDGER")
    print("=" * 72)
    for s, m in ((0, False), (1, False), (2, True), (3, False)):
        print(f"\n  strikes={s} manipulative={m}: {turn_cheek(s, m)}")
    print(f"\n  {karmic_smite(True)}")
    return 0


class Tests(unittest.TestCase):
    def test_grace(self):
        self.assertIn("GRACE", turn_cheek(1, False))
        self.assertIn("GRACE", turn_cheek(2, False))

    def test_no_wrong(self):
        self.assertIn("NO WRONG DONE", turn_cheek(0))
        self.assertIn("NO WRONG DONE", turn_cheek(-3))

    def test_justice(self):
        self.assertIn("KARMIC JUSTICE", turn_cheek(3, False))
        self.assertIn("KARMIC JUSTICE", turn_cheek(1, True))

    def test_bad_input_fallback(self):
        self.assertIn("GRACE", turn_cheek("three?", False))

    def test_smite_wording(self):
        self.assertIn("the other side", karmic_smite(True))
        self.assertNotIn("Jesus", karmic_smite(True))
        self.assertIn("THE 1", karmic_smite(False))


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


if __name__ == "__main__":
    import sys
    if "--test" in sys.argv:
        sys.exit(run_tests())
    sys.exit(demonstrate())
