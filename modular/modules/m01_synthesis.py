#!/usr/bin/env python3
"""
Theological Synthesis Engine
============================
Type: reference; computational demonstration

This is a structural and philosophical analysis tool, NOT a religious text.
It models the shared narrative architecture of three traditions:
  1. Ancient Egyptian (Osiris/Horus)
  2. Christianity (Jesus Christ)
  3. Buddhism (Siddhartha Gautama)

It then maps these structures onto a hypothetical fused narrative,
"The Cycle of the Awakened Light."

Run:
    python3 awakened_tao.py synthesis --compare
    python3 awakened_tao.py synthesis --fuse
    python3 awakened_tao.py synthesis --json
    python3 awakened_tao.py synthesis --test

Standard library only.
"""
from __future__ import annotations

import argparse
import json
import sys
import unittest
from dataclasses import dataclass, field
from typing import List, Dict, Optional


# ============================================================================
# Data Models
# ============================================================================
@dataclass
class Tradition:
    name: str
    origin: str
    problem: str           # What is the fundamental issue with the world?
    mechanism: str         # What causes the problem?
    solution: str          # How is it fixed?
    outcome: str           # What is the final state?
    deity_structure: str   # Monotheistic, Polytheistic, Non-theistic
    afterlife: str         # What happens when you die?
    core_archetype: str    # The central figure/role


@dataclass
class FusedNarrative:
    name: str
    cosmology: str
    the_fall: str
    the_incarnation: str
    the_trial: str
    the_descent: str
    the_resurrection: str
    the_judgment: str
    the_revelation: str
    thematic_map: Dict[str, str]  # Maps the fused concept to its origins


# ============================================================================
# 1. The Traditions
# ============================================================================
EGYPT = Tradition(
    name="Ancient Egyptian",
    origin="c. 2400 BCE, Nile Valley",
    problem="Chaos (Isfet) threatens the order of the cosmos and the state.",
    mechanism="The murder of Osiris by Set, the disruption of Maat (balance).",
    solution="The son (Horus) avenges the father, restores order, and takes the throne.",
    outcome="Maat (Truth/Order) is restored; the Pharaoh rules eternally.",
    deity_structure="Polytheistic (gods can die, be tricked, and resurrect).",
    afterlife="Weighing of the Heart against the feather of Maat.",
    core_archetype="The Dying and Rising God / The Avenging Son"
)

CHRISTIANITY = Tradition(
    name="Christianity",
    origin="c. 30 CE, Judea",
    problem="Sin and death separate humanity from God.",
    mechanism="Original Sin, the rebellion of the human will.",
    solution="God incarnates as Jesus, dies on the cross, and resurrects to defeat death.",
    outcome="Salvation and eternal life; reunion with God.",
    deity_structure="Monotheistic (Trinitarian: Father, Son, Holy Spirit).",
    afterlife="Heaven, Hell, or Purgatory; resurrection of the body at the end of time.",
    core_archetype="The Suffering Servant / The Resurrected Savior"
)

BUDDHISM = Tradition(
    name="Buddhism",
    origin="c. 500 BCE, Indian subcontinent",
    problem="Dukkha (Suffering) is inherent in existence.",
    mechanism="Attachment (Upadana) and Ignorance (Avidya) of the true nature of reality.",
    solution="The Noble Eightfold Path: mindfulness, meditation, and the dissolution of the ego.",
    outcome="Nirvana; the extinguishing of the flame of craving and the end of rebirth.",
    deity_structure="Non-theistic (no creator god; relies on karma and natural law).",
    afterlife="Rebirth (Samsara) until Nirvana is achieved.",
    core_archetype="The Awakened One (The Buddha)"
)

TRADITIONS = [EGYPT, CHRISTIANITY, BUDDHISM]


# ============================================================================
# 2. The Fused Narrative
# ============================================================================
FUSED = FusedNarrative(
    name="The Cycle of the Awakened Light",
    cosmology=(
        "Before time, there was the Void (Sunyata). Out of the Void came a vibration—the first "
        "sound, the first light. This light was The Architect (the Monotheistic God / Atum). "
        "The Architect desired to know itself, so it fractured its light into a million pieces. "
        "These pieces became the universe, matter, and living beings."
    ),
    the_fall=(
        "The shards of light fell into the physical world. To survive, they developed an Ego—a "
        "sense of 'I' separate from the whole. But the Ego became greedy, clinging to pleasure "
        "and avoiding pain. This clinging is the root of suffering (Buddhism). The Ego rebelled "
        "against the natural laws of harmony. It became The Adversary (Set / Satan / Mara). "
        "The Adversary is not an external demon; it is the personification of our own selfish "
        "attachment."
    ),
    the_incarnation=(
        "The Architect saw its children suffering under the weight of their own Egos. So, it "
        "decided to enter the cycle of Samsara itself to show the path out. The Architect "
        "incarnated as a human being—The Awakened One (Horus / Christ / Siddhartha). He was "
        "born in a humble, hidden place."
    ),
    the_trial=(
        "When the Awakened One began to teach that the Ego is an illusion, the Adversary "
        "(the collective greed of the world) conspired against him. He was tested, betrayed, "
        "and killed. He was dismembered (Osiris), crucified (Christ), and assaulted by Mara's "
        "armies (Buddha). The world thought the Ego had won."
    ),
    the_descent=(
        "But death was not the end. The Awakened One descended into the deepest part of the "
        "Void—the Underworld (Duat / Hell / Bardo). In the absolute darkness, he faced the "
        "ultimate test: the complete dissolution of the self. He let go of everything. By "
        "completely releasing the Ego, he achieved Nirvana."
    ),
    the_resurrection=(
        "Because he held no attachment to the self, death could not hold him. The fragments "
        "of his light reassembled. He rose again—the Resurrected King. He emerged from the "
        "tomb not as a ghost, but as the Living Spirit of the Universe. He had conquered "
        "death not by avoiding it, but by walking directly through it."
    ),
    the_judgment=(
        "Now, the Awakened One sits at the threshold between the physical world and the Void. "
        "When you die, you face the Weighing of the Heart (Egyptian). You are judged by Grace "
        "(Christian). If your heart is heavy with attachment, you are returned to the cycle "
        "(Reincarnation / Samsara). If you have learned to dissolve the Ego, you step across "
        "the threshold into the Field of Reeds (Egyptian) / Heaven (Christian) / Nirvana (Buddhist)."
    ),
    the_revelation=(
        "At the end of the great cycle, when all the shards of light have learned to dissolve "
        "their Egos, the physical universe will dissolve back into the Void. The Adversary is "
        "not destroyed, because it was always just a shadow cast by the Light. You are the "
        "Awakened One. The Light has returned to the Void, and the Void is at peace."
    ),
    thematic_map={
        "The Problem": "Combines Buddhist attachment, Christian sin, and Egyptian chaos.",
        "The Solution": "Combines Buddhist mindfulness, Christian faith/grace, and Egyptian ritual/order.",
        "The Afterlife": "Combines Egyptian weighing of the heart, Buddhist rebirth, and Christian resurrection.",
        "The Core Theme": "Turns worship of an external god into recognition of the divine spark inside yourself."
    }
)


# ============================================================================
# 3. Analysis Functions
# ============================================================================
def compare_traditions(traditions: List[Tradition]) -> List[Dict]:
    """Extract the core structural parallels."""
    rows = []
    for t in traditions:
        rows.append({
            "name": t.name,
            "origin": t.origin,
            "problem": t.problem,
            "mechanism": t.mechanism,
            "solution": t.solution,
            "outcome": t.outcome,
            "deity": t.deity_structure,
            "afterlife": t.afterlife,
            "archetype": t.core_archetype,
        })
    return rows


def find_archetypal_parallels(traditions: List[Tradition]) -> Dict[str, List[str]]:
    """Identify the shared motifs across all three."""
    return {
        "The Dying & Rising God": [
            "Osiris is murdered and resurrected as Lord of the Underworld.",
            "Jesus is crucified and resurrected on the third day.",
            "Buddha achieves Parinirvana (final death of the physical body).",
        ],
        "The Posthumous / Miraculous Birth": [
            "Isis conceives Horus magically after Osiris's death.",
            "Mary conceives Jesus through the Holy Spirit.",
            "Maya dreams of a white elephant and gives birth to Siddhartha.",
        ],
        "The Adversary": [
            "Set (chaos, brother of Osiris).",
            "Satan / The Devil (temptation, fallen angel).",
            "Mara (the demon of illusion and attachment).",
        ],
        "The Final Judgment": [
            "Weighing of the Heart against the feather of Maat.",
            "The Last Judgment at the throne of God.",
            "The cycle of rebirth determined by Karma.",
        ]
    }


# ============================================================================
# 4. Reporting
# ============================================================================
def render_comparison(rows: List[Dict]) -> None:
    print("=" * 78)
    print("THEOLOGICAL COMPARISON: EGYPT, CHRISTIANITY, BUDDHISM")
    print("=" * 78)
    for r in rows:
        print(f"\n[{r['name']}] ({r['origin']})")
        print(f"  Problem:    {r['problem']}")
        print(f"  Mechanism:  {r['mechanism']}")
        print(f"  Solution:   {r['solution']}")
        print(f"  Outcome:     {r['outcome']}")
        print(f"  Deity:      {r['deity']}")
        print(f"  Afterlife:  {r['afterlife']}")
        print(f"  Archetype:  {r['archetype']}")


def render_fused(fused: FusedNarrative) -> None:
    print("=" * 78)
    print(f"FUSED NARRATIVE: {fused.name}")
    print("=" * 78)
    print(f"\n[Cosmology]\n  {fused.cosmology}")
    print(f"\n[The Fall]\n  {fused.the_fall}")
    print(f"\n[The Incarnation]\n  {fused.the_incarnation}")
    print(f"\n[The Trial]\n  {fused.the_trial}")
    print(f"\n[The Descent]\n  {fused.the_descent}")
    print(f"\n[The Resurrection]\n  {fused.the_resurrection}")
    print(f"\n[The Judgment]\n  {fused.the_judgment}")
    print(f"\n[The Final Revelation]\n  {fused.the_revelation}")
    print("\n[Thematic Map]")
    for k, v in fused.thematic_map.items():
        print(f"  {k}: {v}")


def render_parallels(parallels: Dict[str, List[str]]) -> None:
    print("=" * 78)
    print("ARCHETYPAL PARALLELS")
    print("=" * 78)
    for motif, examples in parallels.items():
        print(f"\n{motif}:")
        for e in examples:
            print(f"  • {e}")


# ============================================================================
# 5. CLI
# ============================================================================
def cmd_compare(args) -> int:
    render_comparison(compare_traditions(TRADITIONS))
    render_parallels(find_archetypal_parallels(TRADITIONS))
    return 0


def cmd_fuse(args) -> int:
    render_fused(FUSED)
    return 0


def cmd_json(args) -> int:
    out = {
        "traditions": compare_traditions(TRADITIONS),
        "parallels": find_archetypal_parallels(TRADITIONS),
        "fused_narrative": {
            "name": FUSED.name,
            "cosmology": FUSED.cosmology,
            "the_fall": FUSED.the_fall,
            "the_incarnation": FUSED.the_incarnation,
            "the_trial": FUSED.the_trial,
            "the_descent": FUSED.the_descent,
            "the_resurrection": FUSED.the_resurrection,
            "the_judgment": FUSED.the_judgment,
            "the_revelation": FUSED.the_revelation,
            "thematic_map": FUSED.thematic_map,
        }
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


# ============================================================================
# 6. Tests
# ============================================================================
class Tests(unittest.TestCase):

    def test_traditions_have_all_fields(self):
        for t in TRADITIONS:
            self.assertTrue(t.name)
            self.assertTrue(t.problem)
            self.assertTrue(t.solution)
            self.assertTrue(t.core_archetype)

    def test_egypt_is_polytheistic(self):
        self.assertIn("Polytheistic", EGYPT.deity_structure)

    def test_buddhism_is_nontheistic(self):
        self.assertIn("Non-theistic", BUDDHISM.deity_structure)

    def test_christianity_is_monotheistic(self):
        self.assertIn("Monotheistic", CHRISTIANITY.deity_structure)

    def test_parallels_have_motifs(self):
        p = find_archetypal_parallels(TRADITIONS)
        self.assertIn("The Dying & Rising God", p)
        self.assertIn("The Adversary", p)
        self.assertIn("The Final Judgment", p)
        self.assertEqual(len(p["The Adversary"]), 3)

    def test_fused_has_all_sections(self):
        f = FUSED
        for section in (f.cosmology, f.the_fall, f.the_incarnation,
                        f.the_trial, f.the_descent, f.the_resurrection,
                        f.the_judgment, f.the_revelation):
            self.assertTrue(section)
            self.assertGreater(len(section), 20)

    def test_cli_compare_runs(self):
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = cmd_compare(argparse.Namespace())
        self.assertEqual(rc, 0)
        out = buf.getvalue()
        self.assertIn("Ancient Egyptian", out)
        self.assertIn("Christianity", out)
        self.assertIn("Buddhism", out)
        self.assertIn("The Adversary", out)

    def test_cli_fuse_runs(self):
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = cmd_fuse(argparse.Namespace())
        self.assertEqual(rc, 0)
        out = buf.getvalue()
        self.assertIn("The Cycle of the Awakened Light", out)
        self.assertIn("Void", out)
        self.assertIn("Nirvana", out)

    def test_cli_json_is_valid(self):
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            cmd_json(argparse.Namespace())
        data = json.loads(buf.getvalue())
        self.assertEqual(len(data["traditions"]), 3)
        self.assertEqual(data["fused_narrative"]["name"], "The Cycle of the Awakened Light")


def run_tests() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
    return 0 if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful() else 1


# ============================================================================
# Main
# ============================================================================
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--compare", action="store_true", help="show structural comparison")
    g.add_argument("--fuse", action="store_true", help="print the fused narrative")
    g.add_argument("--json", action="store_true", help="dump everything as JSON")
    g.add_argument("--test", action="store_true")
    args = ap.parse_args(argv)

    if args.test:
        return run_tests()
    if args.compare:
        return cmd_compare(args)
    if args.fuse:
        return cmd_fuse(args)
    if args.json:
        return cmd_json(args)

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
