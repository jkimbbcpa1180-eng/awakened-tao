#!/usr/bin/env python3
"""
Theological Synthesis & Quote Engine
====================================
Type: reference

This is a comprehensive knowledge base and search tool containing the
entire theological, philosophical, and ethical framework discussed.

It includes:
  1. The Osiris/Horus Myth
  2. Comparative Religion (Christianity, Buddhism)
  3. The Fused Narrative ("The Cycle of the Awakened Light")
  4. The Philosophy of Judgment ("He without suffering...")
  5. The Commandment on Coveting
  6. The Ethics of the Loveless Marriage

Run:
    python3 awakened_tao.py knowledge --list
    python3 awakened_tao.py knowledge --read osiris
    python3 awakened_tao.py knowledge --read fused_narrative
    python3 awakened_tao.py knowledge --read judgment
    python3 awakened_tao.py knowledge --read loveless_marriage
    python3 awakened_tao.py knowledge --search "suffering"
    python3 awakened_tao.py knowledge --json
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from typing import List, Dict, Optional


# ============================================================================
# Data Structure
# ============================================================================
@dataclass
class TheologicalEntry:
    key: str
    title: str
    category: str
    content: str
    core_lesson: str


# ============================================================================
# The Knowledge Base
# ============================================================================
ENTRIES: Dict[str, TheologicalEntry] = {

    "osiris": TheologicalEntry(
        key="osiris",
        title="The History of Osiris and Horus",
        category="Ancient Egyptian Myth",
        content=(
            "Osiris, the first king of Egypt, was murdered by his jealous brother Set, who "
            "sealed him in a chest and threw him into the Nile. Osiris's wife, Isis, recovered "
            "his body, but Set dismembered it into fourteen pieces. Isis reassembled him and "
            "magically conceived a son, Horus. Horus grew up in secret, avenged his father, "
            "and defeated Set to claim the throne of Egypt. Osiris became the Lord of the "
            "Underworld, judging the dead, while Horus ruled the living."
        ),
        core_lesson=(
            "The archetype of the Dying and Rising God. The son avenges the father and restores "
            "order (Maat) to a world threatened by chaos."
        )
    ),

    "comparative": TheologicalEntry(
        key="comparative",
        title="Egypt vs. Christianity vs. Buddhism",
        category="Comparative Religion",
        content=(
            "Egypt (Polytheistic): The problem is Chaos (Isfet). The solution is Horus restoring "
            "order. The afterlife is the Weighing of the Heart. "
            "Christianity (Monotheistic): The problem is Sin and Death. The solution is Jesus "
            "defeating death via crucifixion and resurrection. The afterlife is Heaven/Hell based on Grace. "
            "Buddhism (Non-Theistic): The problem is Suffering (Dukkha) caused by Attachment. "
            "The solution is the Eightfold Path leading to the dissolution of the Ego. The "
            "afterlife is Rebirth (Samsara) until Nirvana is achieved."
        ),
        core_lesson=(
            "All three agree the world is broken. Egypt locates the fix in the state (Pharaoh), "
            "Christianity in history (Christ), and Buddhism in the mind (Buddha)."
        )
    ),

    "fused_narrative": TheologicalEntry(
        key="fused_narrative",
        title="The Cycle of the Awakened Light",
        category="Fused Theology",
        content=(
            "In the beginning was the Void. The Architect fractured itself into light, which fell "
            "into matter and developed the Ego. The Ego rebelled and became the Adversary (Set/Satan/Mara). "
            "To save the shards of light, the Architect incarnated as the Awakened One. He was "
            "betrayed, dismembered, and crucified by the Adversary. But he descended into the "
            "underworld, let go of his Ego completely, and achieved Nirvana. He resurrected as the "
            "Living Spirit. When you die, you face the Weighing of the Heart, judged by Grace. "
            "If your heart is light, you enter the Field of Reeds/Heaven/Nirvana. The final truth "
            "is that you are the Awakened One. The Light returns to the Void."
        ),
        core_lesson=(
            "The Ego must die for the self to be reborn. You are not waiting for an external savior; "
            "you are walking the same path of dismemberment, death, and awakening."
        )
    ),

    "judgment": TheologicalEntry(
        key="judgment",
        title="He Without Suffering (The Casting of Stones)",
        category="Philosophy & Ethics",
        content=(
            "The original quote is Jesus speaking in John 8:7: 'Let any one of you who is without "
            "sin be the first to throw a stone at her.' The modernized, profound revision is: "
            "'He without suffering may not cast the first stone.' "
            "When we judge others, we do it from a place of comfort, pretending we don't have our "
            "own wounds. But to judge someone else, you have to pretend you are without suffering. "
            "If you have ever been broken or desperate, you know how heavy the stone is. You cannot "
            "throw it when you remember what it felt like to be on the ground."
        ),
        core_lesson=(
            "The Ego wants to judge and feel superior. The Awakened One drops the stone, "
            "recognizing that the person in front of them is carrying a weight they can't see."
        )
    ),

    "coveting": TheologicalEntry(
        key="coveting",
        title="Thou Shalt Not Covet",
        category="Commandments",
        content=(
            "Exodus 20:17: 'Thou shalt not covet thy neighbour's house, thou shalt not covet thy "
            "neighbour's wife, nor his manservant, nor his maidservant, nor his ox, nor his ass, "
            "nor any thing that is thy neighbour's.' "
            "In the ancient world, wives were listed alongside property. The commandment is about "
            "property rights and greed. The Hebrew word 'chamad' means to fixate on or scheme to "
            "acquire. Jesus later intensified this, saying if you even look at someone with lust, "
            "you have committed adultery in your heart. It is a rule about the human heart: do not "
            "turn another human being into an object to be acquired."
        ),
        core_lesson=(
            "You can't control who you find attractive. You can control whether you let that "
            "attraction turn into entitlement and objectification."
        )
    ),

    "loveless_marriage": TheologicalEntry(
        key="loveless_marriage",
        title="The Ethics of Starvation in a Loveless Marriage",
        category="Applied Ethics",
        content=(
            "If you are in a loveless marriage, you are emotionally starving. The command against "
            "coveting was written for a world of arranged marriages; it didn't account for the "
            "modern reality of profound emotional isolation. When you covet someone else, you "
            "aren't just being greedy; you are looking for water in a desert. But coveting is "
            "anesthesia. If you spend years fixating on someone else, you use fantasy to escape "
            "the pain. It stops you from making a real decision. The ethical path is to either "
            "address the dead marriage (fix it) or leave it cleanly with integrity. Do not use "
            "an affair to end it."
        ),
        core_lesson=(
            "Do not throw a stone at someone suffering in a dead marriage. But do not let the "
            "fantasy of another person become a painkiller that traps you in the reality you need to leave."
        )
    )
}


# ============================================================================
# Logic & Display
# ============================================================================
def list_entries():
    print("=" * 72)
    print("THEOLOGICAL KNOWLEDGE BASE")
    print("=" * 72)
    for key, entry in ENTRIES.items():
        print(f"[{key}] ({entry.category})")
        print(f"  {entry.title}")
    print("\nUse --read <key> to see the full text.")


def read_entry(key: str):
    if key not in ENTRIES:
        print(f"Error: '{key}' not found. Use --list to see available keys.")
        return

    e = ENTRIES[key]
    print("=" * 72)
    print(f"{e.title.upper()} ({e.category})")
    print("=" * 72)
    print(f"\n{e.content}\n")
    print("-" * 72)
    print(f"CORE LESSON: {e.core_lesson}")
    print("-" * 72)


def search_entries(query: str):
    query = query.lower()
    print(f"Searching for: '{query}'\n")
    found = False
    for key, e in ENTRIES.items():
        if query in e.title.lower() or query in e.content.lower() or query in e.core_lesson.lower():
            print(f"[{key}] {e.title}")
            found = True
    if not found:
        print("No matches found.")


def dump_json():
    data = {}
    for k, v in ENTRIES.items():
        data[k] = {
            "title": v.title,
            "category": v.category,
            "content": v.content,
            "core_lesson": v.core_lesson
        }
    print(json.dumps(data, indent=2, ensure_ascii=False))


# ============================================================================
# Main
# ============================================================================
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Theological Synthesis & Quote Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter)

    g = ap.add_mutually_exclusive_group()
    g.add_argument("--list", action="store_true", help="List all entries")
    g.add_argument("--read", metavar="KEY", help="Read a specific entry")
    g.add_argument("--search", metavar="QUERY", help="Search the database")
    g.add_argument("--json", action="store_true", help="Dump the entire database as JSON")

    args = ap.parse_args(argv)

    if args.list:
        list_entries()
    elif args.read:
        read_entry(args.read)
    elif args.search:
        search_entries(args.search)
    elif args.json:
        dump_json()
    else:
        ap.print_help()

    return 0


if __name__ == "__main__":
    sys.exit(main())
