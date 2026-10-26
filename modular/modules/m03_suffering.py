#!/usr/bin/env python3
"""
The Suffering Quote Engine
==========================
Type: reference; parable

A focused module on the philosophy of judgment, suffering, and the
"casting of stones."

It contrasts the original Biblical text (John 8:7) with the modernized
revision ("He without suffering...") and breaks down the psychological
mechanics of why judgment is an act of the Ego.

Run:
    python3 awakened_tao.py suffering --read
    python3 awakened_tao.py suffering --analyze
    python3 awakened_tao.py suffering --json
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict


@dataclass
class QuoteAnalysis:
    original_text: str
    original_source: str
    revised_text: str
    core_theme: str
    psychological_mechanics: list[str]
    the_stone: str
    the_suffering: str
    the_awakened_response: str


SUFFERING_QUOTE = QuoteAnalysis(
    original_text="Let any one of you who is without sin be the first to throw a stone at her.",
    original_source="Jesus of Nazareth, John 8:7 (The Bible)",
    revised_text="He without suffering may not cast the first stone.",
    core_theme="The illusion of moral superiority and the heavy weight of human judgment.",
    psychological_mechanics=[
        "1. The Comfort of Judgment: We usually judge others from a place of comfort. We look at their mistakes or identity and feel a temporary boost to our Ego. We think, 'At least I am not like them.'",
        "2. The Erasure of Wounds: To judge someone else, you have to pretend you don't have your own wounds. You have to pretend you are 'without suffering'—or at least, without the kind of suffering that makes you messy and human.",
        "3. The Weight of the Stone: In the ancient world, stoning was a brutal, communal act of violence. To cast a stone meant you were declaring the person in front of you was beyond redemption.",
        "4. The Memory of the Ground: If you have ever suffered deeply—if you have ever been humiliated, broken, or desperate—you know how heavy that stone is. You cannot throw it when you remember what it felt like to be on the ground."
    ],
    the_stone="The stone is the declaration that someone else is beyond redemption. It is the ultimate act of the Ego, saying: 'I am the judge. I am the standard. You are the sinner.'",
    the_suffering="Suffering is the great equalizer. It strips away the pretense of purity. The person who has suffered knows they are made of the same broken material as the person they are judging.",
    the_awakened_response="The Awakened One (Jesus/Buddha/Osiris) looks at the brokenness in the world and drops the stone, because they know they are made of the same material. Dropping the stone isn't about agreeing with everyone; it's about realizing you are not God."
)


def print_analysis(q: QuoteAnalysis):
    print("=" * 74)
    print("THE SUFFERING QUOTE: A PHILOSOPHICAL BREAKDOWN")
    print("=" * 74)

    print("\n[THE ORIGINAL QUOTE]")
    print(f"  \"{q.original_text}\"")
    print(f"  — {q.original_source}")

    print("\n[THE REVISION]")
    print(f"  \"{q.revised_text}\"")

    print("\n[CORE THEME]")
    print(f"  {q.core_theme}")

    print("\n[PSYCHOLOGICAL MECHANICS]")
    for step in q.psychological_mechanics:
        print(f"  {step}")

    print("\n[THE STONE]")
    print(f"  {q.the_stone}")

    print("\n[THE SUFFERING]")
    print(f"  {q.the_suffering}")

    print("\n[THE AWAKENED RESPONSE]")
    print(f"  {q.the_awakened_response}")
    print("\n" + "=" * 74)


def print_diagnostic(q: QuoteAnalysis):
    print("=" * 74)
    print("DIAGNOSTIC: WHERE ARE YOU HOLDING THE STONE?")
    print("=" * 74)
    print("\nWalk through each mechanic honestly. This is a mirror, not a test.\n")
    prompts = [
        ("The Comfort of Judgment",
         "Who are you judging right now — and what does feeling superior to them give you?"),
        ("The Erasure of Wounds",
         "What wound of yours are you pretending doesn't exist while you judge?"),
        ("The Weight of the Stone",
         "Are you declaring this person beyond redemption? Would you accept that verdict on yourself?"),
        ("The Memory of the Ground",
         "Remember the last time you were the one on the ground. Can you still throw it?"),
    ]
    for title, prompt in prompts:
        print(f"[{title}]")
        print(f"  Ask yourself: {prompt}\n")
    print("=" * 74)
    print("If you can answer all four honestly, you already know what to do with the stone.")
    print("=" * 74)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="Philosophy of the Suffering Quote",
        formatter_class=argparse.RawDescriptionHelpFormatter)

    g = ap.add_mutually_exclusive_group()
    g.add_argument("--read", action="store_true", help="Print the full philosophical breakdown")
    g.add_argument("--analyze", action="store_true", help="Run the judgment self-diagnostic")
    g.add_argument("--json", action="store_true", help="Output as JSON")

    args = ap.parse_args(argv)

    if args.json:
        print(json.dumps(asdict(SUFFERING_QUOTE), indent=2, ensure_ascii=False))
    elif args.analyze:
        print_diagnostic(SUFFERING_QUOTE)
    elif args.read or not argv:
        print_analysis(SUFFERING_QUOTE)
    else:
        ap.print_help()

    return 0


if __name__ == "__main__":
    sys.exit(main())
