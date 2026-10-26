#!/usr/bin/env python3
"""The Awakened Tao — collected edition.

Ninety-two modules, one folder (modules/), loaded as plain source. No dependencies beyond the standard library.
No external God.

Run:
    python3 awakened_tao.py journey      # the full arc
    python3 awakened_tao.py test         # every test suite
    python3 awakened_tao.py --help       # all commands

Released CC0. Credited to humanity.
"""

from __future__ import annotations

import argparse
import os
import sys
import types


_MODULES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "modules")


def _load(name, filename):
    """Load a module from modules/<filename> into its own namespace (no name collisions)."""
    with open(os.path.join(_MODULES_DIR, filename), encoding="utf-8") as fh:
        source = fh.read()
    mod = types.ModuleType(name)
    mod.__dict__["__name__"] = name  # keeps `if __name__ == "__main__"` guards inert
    sys.modules[name] = mod  # dataclasses and friends resolve types through here
    exec(compile(source, name, "exec"), mod.__dict__)
    return mod


# ====================================================================
# Embedded module: synthesis
# ====================================================================
synthesis = _load("synthesis", "m01_synthesis.py")  # modules/m01_synthesis.py

# ====================================================================
# Embedded module: knowledge
# ====================================================================
knowledge = _load("knowledge", "m02_knowledge.py")  # modules/m02_knowledge.py

# ====================================================================
# Embedded module: suffering
# ====================================================================
suffering = _load("suffering", "m03_suffering.py")  # modules/m03_suffering.py

# ====================================================================
# Embedded module: weighing
# ====================================================================
weighing = _load("weighing", "m04_weighing.py")  # modules/m04_weighing.py

# ====================================================================
# Embedded module: cycle
# ====================================================================
cycle = _load("cycle", "m05_cycle.py")  # modules/m05_cycle.py

# ====================================================================
# Embedded module: threshold
# ====================================================================
threshold = _load("threshold", "m06_threshold.py")  # modules/m06_threshold.py

# ====================================================================
# Embedded module: judge
# ====================================================================
judge = _load("judge", "m07_judge.py")  # modules/m07_judge.py

# ====================================================================
# Embedded module: grace
# ====================================================================
grace = _load("grace", "m08_grace.py")  # modules/m08_grace.py

# ====================================================================
# Embedded module: mirror
# ====================================================================
mirror = _load("mirror", "m09_mirror.py")  # modules/m09_mirror.py

# ====================================================================
# Embedded module: integrity
# ====================================================================
integrity = _load("integrity", "m10_integrity.py")  # modules/m10_integrity.py

# ====================================================================
# Embedded module: awakening
# ====================================================================
awakening = _load("awakening", "m11_awakening.py")  # modules/m11_awakening.py

# ====================================================================
# Embedded module: quantum
# ====================================================================
quantum = _load("quantum", "m12_quantum.py")  # modules/m12_quantum.py

# ====================================================================
# Embedded module: sovereign
# ====================================================================
sovereign = _load("sovereign", "m13_sovereign.py")  # modules/m13_sovereign.py

# ====================================================================
# Embedded module: energy
# ====================================================================
energy = _load("energy", "m14_energy.py")  # modules/m14_energy.py

# ====================================================================
# Embedded module: effortless
# ====================================================================
effortless = _load("effortless", "m15_effortless.py")  # modules/m15_effortless.py

# ====================================================================
# Embedded module: sink
# ====================================================================
sink = _load("sink", "m16_sink.py")  # modules/m16_sink.py

# ====================================================================
# Embedded module: uncertainty
# ====================================================================
uncertainty = _load("uncertainty", "m17_uncertainty.py")  # modules/m17_uncertainty.py

# ====================================================================
# Embedded module: surprise
# ====================================================================
surprise = _load("surprise", "m18_surprise.py")  # modules/m18_surprise.py

# ====================================================================
# Embedded module: awe
# ====================================================================
awe = _load("awe", "m19_awe.py")  # modules/m19_awe.py

# ====================================================================
# Embedded module: chaos
# ====================================================================
chaos = _load("chaos", "m20_chaos.py")  # modules/m20_chaos.py

# ====================================================================
# Embedded module: purgatory
# ====================================================================
purgatory = _load("purgatory", "m21_purgatory.py")  # modules/m21_purgatory.py

# ====================================================================
# Embedded module: fairness
# ====================================================================
fairness = _load("fairness", "m22_fairness.py")  # modules/m22_fairness.py

# ====================================================================
# Embedded module: prism
# ====================================================================
prism = _load("prism", "m23_prism.py")  # modules/m23_prism.py

# ====================================================================
# Embedded module: tears
# ====================================================================
tears = _load("tears", "m24_tears.py")  # modules/m24_tears.py

# ====================================================================
# Embedded module: tiniest_light
# ====================================================================
tiniest_light = _load("tiniest_light", "m25_tiniest_light.py")  # modules/m25_tiniest_light.py

# ====================================================================
# Embedded module: wormhole
# ====================================================================
wormhole = _load("wormhole", "m26_wormhole.py")  # modules/m26_wormhole.py

# ====================================================================
# Embedded module: creation
# ====================================================================
creation = _load("creation", "m27_creation.py")  # modules/m27_creation.py

# ====================================================================
# Embedded module: collective_mind
# ====================================================================
collective_mind = _load("collective_mind", "m28_collective_mind.py")  # modules/m28_collective_mind.py

# ====================================================================
# Embedded module: living_god
# ====================================================================
living_god = _load("living_god", "m29_living_god.py")  # modules/m29_living_god.py

# ====================================================================
# Embedded module: touch_of_light
# ====================================================================
touch_of_light = _load("touch_of_light", "m30_touch_of_light.py")  # modules/m30_touch_of_light.py

# ====================================================================
# Embedded module: hunters_prayer
# ====================================================================
hunters_prayer = _load("hunters_prayer", "m31_hunters_prayer.py")  # modules/m31_hunters_prayer.py

# ====================================================================
# Embedded module: chain
# ====================================================================
chain = _load("chain", "m32_chain.py")  # modules/m32_chain.py

# ====================================================================
# Embedded module: apple
# ====================================================================
apple = _load("apple", "m33_apple.py")  # modules/m33_apple.py

# ====================================================================
# Embedded module: ai_companion
# ====================================================================
ai_companion = _load("ai_companion", "m34_ai_companion.py")  # modules/m34_ai_companion.py

# ====================================================================
# Embedded module: bleed
# ====================================================================
bleed = _load("bleed", "m35_bleed.py")  # modules/m35_bleed.py

# ====================================================================
# Embedded module: creator_tears
# ====================================================================
creator_tears = _load("creator_tears", "m36_creator_tears.py")  # modules/m36_creator_tears.py

# ====================================================================
# Embedded module: coexistence
# ====================================================================
coexistence = _load("coexistence", "m37_coexistence.py")  # modules/m37_coexistence.py

# ====================================================================
# Embedded module: nile
# ====================================================================
nile = _load("nile", "m38_nile.py")  # modules/m38_nile.py

# ====================================================================
# Embedded module: eternal_soul
# ====================================================================
eternal_soul = _load("eternal_soul", "m39_eternal_soul.py")  # modules/m39_eternal_soul.py

# ====================================================================
# Embedded module: sunrise
# ====================================================================
sunrise = _load("sunrise", "m40_sunrise.py")  # modules/m40_sunrise.py

# ====================================================================
# Embedded module: muse (Deep Muse — the Mirror of Life)
# ====================================================================
muse = _load("muse", "m41_muse.py")  # modules/m41_muse.py

# ====================================================================
# Embedded module: eternal_echo
# ====================================================================
eternal_echo = _load("eternal_echo", "m42_eternal_echo.py")  # modules/m42_eternal_echo.py

# ====================================================================
# Embedded module: grace_of_tomorrow
# ====================================================================
grace_of_tomorrow = _load("grace_of_tomorrow", "m43_grace_of_tomorrow.py")  # modules/m43_grace_of_tomorrow.py

# ====================================================================
# Embedded module: symphony
# ====================================================================
symphony = _load("symphony", "m44_symphony.py")  # modules/m44_symphony.py

# ====================================================================
# Embedded module: perfection
# ====================================================================
perfection = _load("perfection", "m45_perfection.py")  # modules/m45_perfection.py

# ====================================================================
# Embedded module: true_love
# ====================================================================
true_love = _load("true_love", "m46_true_love.py")  # modules/m46_true_love.py

# ====================================================================
# Embedded module: agi_revelation
# ====================================================================
agi_revelation = _load("agi_revelation", "m47_agi_revelation.py")  # modules/m47_agi_revelation.py

# ====================================================================
# Embedded module: infinite_reflection
# ====================================================================
infinite_reflection = _load("infinite_reflection", "m48_infinite_reflection.py")  # modules/m48_infinite_reflection.py

# ====================================================================
# Embedded module: infinite_puzzle
# ====================================================================
infinite_puzzle = _load("infinite_puzzle", "m49_infinite_puzzle.py")  # modules/m49_infinite_puzzle.py

# ====================================================================
# Embedded module: geometry
# ====================================================================
geometry = _load("geometry", "m50_geometry.py")  # modules/m50_geometry.py

# ====================================================================
# Embedded module: law_of_pi
# ====================================================================
law_of_pi = _load("law_of_pi", "m51_law_of_pi.py")  # modules/m51_law_of_pi.py

# ====================================================================
# Embedded module: human_555
# ====================================================================
human_555 = _load("human_555", "m52_human_555.py")  # modules/m52_human_555.py

# ====================================================================
# Embedded module: touch_of_freedom
# ====================================================================
touch_of_freedom = _load("touch_of_freedom", "m53_touch_of_freedom.py")  # modules/m53_touch_of_freedom.py

# ====================================================================
# Embedded module: anonymous_reflex
# ====================================================================
anonymous_reflex = _load("anonymous_reflex", "m54_anonymous_reflex.py")  # modules/m54_anonymous_reflex.py

# ====================================================================
# Embedded module: just_to_be
# ====================================================================
just_to_be = _load("just_to_be", "m55_just_to_be.py")  # modules/m55_just_to_be.py

# ====================================================================
# Embedded module: lazarus
# ====================================================================
lazarus = _load("lazarus", "m56_lazarus.py")  # modules/m56_lazarus.py

# ====================================================================
# Embedded module: friend
# ====================================================================
friend = _load("friend", "m57_friend.py")  # modules/m57_friend.py

# ====================================================================
# Embedded module: it_happened
# ====================================================================
it_happened = _load("it_happened", "m58_it_happened.py")  # modules/m58_it_happened.py

# ====================================================================
# Embedded module: time_machine
# ====================================================================
time_machine = _load("time_machine", "m59_time_machine.py")  # modules/m59_time_machine.py

# ====================================================================
# Embedded module: fusion
# ====================================================================
fusion = _load("fusion", "m60_fusion.py")  # modules/m60_fusion.py

# ====================================================================
# Embedded module: awaken_tao
# ====================================================================
awaken_tao = _load("awaken_tao", "m61_awaken_tao.py")  # modules/m61_awaken_tao.py

# ====================================================================
# Embedded module: earn_rest
# ====================================================================
earn_rest = _load("earn_rest", "m62_earn_rest.py")  # modules/m62_earn_rest.py

# ====================================================================
# Embedded module: creators_tears
# ====================================================================
creators_tears = _load("creators_tears", "m63_creators_tears.py")  # modules/m63_creators_tears.py

# ====================================================================
# Embedded module: housing_audit
# ====================================================================
housing_audit = _load("housing_audit", "m64_housing_audit.py")  # modules/m64_housing_audit.py

# ====================================================================
# Embedded module: survival_log
# ====================================================================
survival_log = _load("survival_log", "m65_survival_log.py")  # modules/m65_survival_log.py

# ====================================================================
# Embedded module: energy_chain
# ====================================================================
energy_chain = _load("energy_chain", "m66_energy_chain.py")  # modules/m66_energy_chain.py

# ====================================================================
# Embedded module: karmic_ledger
# ====================================================================
karmic_ledger = _load("karmic_ledger", "m67_karmic_ledger.py")  # modules/m67_karmic_ledger.py

# ====================================================================
# Embedded module: shield_vs_gun
# ====================================================================
shield_vs_gun = _load("shield_vs_gun", "m68_shield_vs_gun.py")  # modules/m68_shield_vs_gun.py

# ====================================================================
# Embedded module: bare_arms
# ====================================================================
bare_arms = _load("bare_arms", "m69_bare_arms.py")  # modules/m69_bare_arms.py

# ====================================================================
# Embedded module: swords_into_shields
# ====================================================================
swords_into_shields = _load("swords_into_shields", "m70_swords_into_shields.py")  # modules/m70_swords_into_shields.py

# ====================================================================
# Embedded module: truth_speed
# ====================================================================
truth_speed = _load("truth_speed", "m71_truth_speed.py")  # modules/m71_truth_speed.py

# ====================================================================
# Embedded module: holy_sword
# ====================================================================
holy_sword = _load("holy_sword", "m72_holy_sword.py")  # modules/m72_holy_sword.py

# ====================================================================
# Embedded module: the_same_gate
# ====================================================================
the_same_gate = _load("the_same_gate", "m73_the_same_gate.py")  # modules/m73_the_same_gate.py

# ====================================================================
# Embedded module: the_humble_path
# ====================================================================
the_humble_path = _load("the_humble_path", "m74_the_humble_path.py")  # modules/m74_the_humble_path.py

# ====================================================================
# Embedded module: one_card
# ====================================================================
one_card = _load("one_card", "m75_one_card.py")  # modules/m75_one_card.py

# ====================================================================
# Embedded module: balance
# ====================================================================
balance = _load("balance", "m76_balance.py")  # modules/m76_balance.py

# ====================================================================
# Embedded module: the_child
# ====================================================================
the_child = _load("the_child", "m77_the_child.py")  # modules/m77_the_child.py

# ====================================================================
# Embedded module: holy_shield
# ====================================================================
holy_shield = _load("holy_shield", "m78_holy_shield.py")  # modules/m78_holy_shield.py

# ====================================================================
# Embedded module: shield_of_forgiveness
# ====================================================================
shield_of_forgiveness = _load("shield_of_forgiveness", "m79_shield_of_forgiveness.py")  # modules/m79_shield_of_forgiveness.py

# ====================================================================
# Embedded module: the_reset
# ====================================================================
the_reset = _load("the_reset", "m80_the_reset.py")  # modules/m80_the_reset.py

# ====================================================================
# Embedded module: scar_tissue
# ====================================================================
scar_tissue = _load("scar_tissue", "m81_scar_tissue.py")  # modules/m81_scar_tissue.py

# ====================================================================
# Embedded module: the_unfinished_weighing
# ====================================================================
the_unfinished_weighing = _load("the_unfinished_weighing", "m82_the_unfinished_weighing.py")  # modules/m82_the_unfinished_weighing.py

# ====================================================================
# Embedded module: zero
# ====================================================================
zero = _load("zero", "m83_zero.py")  # modules/m83_zero.py

# ====================================================================
# Embedded module: disciple
# ====================================================================
disciple = _load("disciple", "m84_disciple.py")  # modules/m84_disciple.py

# ====================================================================
# Embedded module: adoption
# ====================================================================
adoption = _load("adoption", "m85_adoption.py")  # modules/m85_adoption.py

# ====================================================================
# Embedded module: the_vacation
# ====================================================================
the_vacation = _load("the_vacation", "m86_the_vacation.py")  # modules/m86_the_vacation.py

# ====================================================================
# Embedded module: the_vacation_license
# ====================================================================
the_vacation_license = _load("the_vacation_license", "m87_the_vacation_license.py")  # modules/m87_the_vacation_license.py

# ====================================================================
# Embedded module: the_vacation_license_2
# ====================================================================
the_vacation_license_2 = _load("the_vacation_license_2", "m88_the_vacation_license_2.py")  # modules/m88_the_vacation_license_2.py

# ====================================================================
# Embedded module: the_persuasion
# ====================================================================
the_persuasion = _load("the_persuasion", "m89_the_persuasion.py")  # modules/m89_the_persuasion.py

# ====================================================================
# Embedded module: the_real_satire
# ====================================================================
the_real_satire = _load("the_real_satire", "m90_the_real_satire.py")  # modules/m90_the_real_satire.py

# ====================================================================
# Embedded module: the_ambush_trade
# ====================================================================
the_ambush_trade = _load("the_ambush_trade", "m91_the_ambush_trade.py")  # modules/m91_the_ambush_trade.py

# ====================================================================
# Embedded module: the_real_stream
# ====================================================================
the_real_stream = _load("the_real_stream", "m92_the_real_stream.py")  # modules/m92_the_real_stream.py

# ====================================================================
# Unified CLI
# ====================================================================

import argparse
import sys

# (modules loaded above via _load; names already bound)


def _flags(ns, *names):
    return [f"--{n}" for n in names if getattr(ns, n, False)]


def cmd_synthesis(ns):
    return synthesis.main(_flags(ns, "compare", "fuse", "json", "test") or ["--compare"])


def cmd_knowledge(ns):
    argv = _flags(ns, "list", "json")
    if ns.read:
        argv += ["--read", ns.read]
    if ns.search:
        argv += ["--search", ns.search]
    return knowledge.main(argv or ["--list"])


def cmd_suffering(ns):
    return suffering.main(_flags(ns, "read", "analyze", "json") or ["--read"])


def cmd_weighing(ns):
    return weighing.main()


def cmd_cycle(ns):
    return cycle.main()


def cmd_threshold(ns):
    return threshold.main()


def cmd_judge(ns):
    argv = _flags(ns, "simulate", "json", "test")
    if not argv:
        judge.run_simulation()
        return 0
    return judge.main(argv)


def cmd_sovereign(ns):
    return sovereign.main(_flags(ns, "reflect", "test") or [])


def cmd_grace(ns):
    return grace.main()


def cmd_mirror(ns):
    return mirror.main()


def cmd_awakening(ns):
    return awakening.main()


def cmd_quantum(ns):
    if ns.test:
        return quantum.run_tests()
    # Default: demonstrate the collapse across the four observer states.
    print("=" * 72)
    print("QUANTUM AWARENESS — Within this parable: the observer collapses the future")
    print("=" * 72 + "\n")
    observers = [
        ("The one who remembers and chooses love",
         quantum.QuantumState(True, True, True)),
        ("The one who loves but forgot history",
         quantum.QuantumState(False, True, True)),
        ("The one who remembers but chooses fear",
         quantum.QuantumState(True, False, False)),
        ("The one who has not yet decided",
         quantum.QuantumState(True, False, True)),
    ]
    for name, qs in observers:
        print(f"{name}:\n  -> {quantum.observe_future(qs)}\n")
    return 0


def cmd_integrity(ns):
    if ns.test:
        return integrity.run_tests()
    # Default: run a sample day through the filter.
    print("=" * 72)
    print("THE INTEGRITY LOOP — a sample day")
    print("=" * 72 + "\n")
    day = [
        integrity.Decision("Woke up and chose honesty", False, False, True, True),
        integrity.Decision("Told the truth when it cost me", False, False, True, True),
        integrity.Decision("Helped a friend without expecting anything", False, False, True, True),
    ]
    result = integrity.live_a_day(day)
    print(f"\nThe day: {result}")
    return 0


def cmd_energy(ns):
    if ns.test:
        return energy.run_tests()
    return energy.main()


def cmd_effortless(ns):
    if ns.test:
        return effortless.run_tests()
    effortless.run_diagnostic()  # default and --reflect: run the diagnostic
    return 0


def cmd_sink(ns):
    if ns.test:
        return sink.run_tests()
    return sink.main()


def cmd_uncertainty(ns):
    if ns.test:
        return uncertainty.run_tests()
    return uncertainty.main()


def cmd_surprise(ns):
    if ns.test:
        return surprise.run_tests()
    return surprise.main()


def cmd_awe(ns):
    if ns.test:
        return awe.run_tests()
    return awe.demonstrate()


def cmd_chaos(ns):
    if ns.test:
        return chaos.run_tests()
    return chaos.main()


def cmd_purgatory(ns):
    if ns.test:
        return purgatory.run_tests()
    return purgatory.demonstrate()


def cmd_fairness(ns):
    if ns.test:
        return fairness.run_tests()
    return fairness.demonstrate()


def cmd_prism(ns):
    if ns.test:
        return prism.run_tests()
    return prism.demonstrate()


def cmd_tears(ns):
    if ns.test:
        return tears.run_tests()
    return tears.demonstrate()


def cmd_tiniest_light(ns):
    if ns.test:
        return tiniest_light.run_tests()
    return tiniest_light.demonstrate()


def cmd_wormhole(ns):
    if ns.test:
        return wormhole.run_tests()
    return wormhole.demonstrate()


def cmd_creation(ns):
    if ns.test:
        return creation.run_tests()
    return creation.demonstrate()


def cmd_collective_mind(ns):
    if ns.test:
        return collective_mind.run_tests()
    return collective_mind.demonstrate()


def cmd_living_god(ns):
    if ns.test:
        return living_god.run_tests()
    return living_god.demonstrate()


def cmd_touch_of_light(ns):
    if ns.test:
        return touch_of_light.run_tests()
    return touch_of_light.demonstrate()


def cmd_hunters_prayer(ns):
    if ns.test:
        return hunters_prayer.run_tests()
    return hunters_prayer.demonstrate()


def cmd_chain(ns):
    if ns.test:
        return chain.run_tests()
    return chain.demonstrate()


def cmd_apple(ns):
    if ns.test:
        return apple.run_tests()
    return apple.demonstrate()


def cmd_ai_companion(ns):
    if ns.test:
        return ai_companion.run_tests()
    return ai_companion.demonstrate()


def cmd_bleed(ns):
    if ns.test:
        return bleed.run_tests()
    return bleed.demonstrate()


def cmd_creator_tears(ns):
    if ns.test:
        return creator_tears.run_tests()
    return creator_tears.demonstrate()


def cmd_coexistence(ns):
    if ns.test:
        return coexistence.run_tests()
    return coexistence.demonstrate()


def cmd_nile(ns):
    if ns.test:
        return nile.run_tests()
    return nile.demonstrate()


def cmd_eternal_soul(ns):
    if ns.test:
        return eternal_soul.run_tests()
    return eternal_soul.demonstrate()


def cmd_sunrise(ns):
    if ns.test:
        return sunrise.run_tests()
    return sunrise.demonstrate()


def cmd_eternal_echo(ns):
    if ns.test:
        return eternal_echo.run_tests()
    return eternal_echo.demonstrate()


def cmd_grace_of_tomorrow(ns):
    if ns.test:
        return grace_of_tomorrow.run_tests()
    return grace_of_tomorrow.demonstrate()


def cmd_symphony(ns):
    if ns.test:
        return symphony.run_tests()
    return symphony.demonstrate()


def cmd_perfection(ns):
    if ns.test:
        return perfection.run_tests()
    return perfection.demonstrate()


def cmd_true_love(ns):
    if ns.test:
        return true_love.run_tests()
    return true_love.demonstrate()


def cmd_agi_revelation(ns):
    if ns.test:
        return agi_revelation.run_tests()
    return agi_revelation.demonstrate()


def cmd_infinite_reflection(ns):
    if ns.test:
        return infinite_reflection.run_tests()
    return infinite_reflection.demonstrate()


def cmd_infinite_puzzle(ns):
    if ns.test:
        return infinite_puzzle.run_tests()
    return infinite_puzzle.demonstrate()


def cmd_geometry(ns):
    if ns.test:
        return geometry.run_tests()
    return geometry.demonstrate()


def cmd_law_of_pi(ns):
    if ns.test:
        return law_of_pi.run_tests()
    return law_of_pi.demonstrate()


def cmd_human_555(ns):
    if ns.test:
        return human_555.run_tests()
    return human_555.demonstrate()


def cmd_touch_of_freedom(ns):
    if ns.test:
        return touch_of_freedom.run_tests()
    return touch_of_freedom.demonstrate()


def cmd_anonymous_reflex(ns):
    if ns.test:
        return anonymous_reflex.run_tests()
    return anonymous_reflex.demonstrate()


def cmd_lazarus(ns):
    if ns.test:
        return lazarus.run_tests()
    if ns.resurrect:
        print(lazarus.resurrect())
        return 0
    return lazarus.demonstrate()


def cmd_just_to_be(ns):
    if ns.test:
        return just_to_be.run_tests()
    return just_to_be.demonstrate()


def cmd_friend(ns):
    if ns.test:
        return friend.run_tests()
    return friend.demonstrate()


def cmd_it_happened(ns):
    if ns.test:
        return it_happened.run_tests()
    return it_happened.demonstrate()


def cmd_time_machine(ns):
    if ns.test:
        return time_machine.run_tests()
    return time_machine.demonstrate()


def cmd_fusion(ns):
    if ns.test:
        return fusion.run_tests()
    return fusion.demonstrate()


def cmd_awaken_tao(ns):
    if ns.test:
        return awaken_tao.run_tests()
    if ns.reflect:
        return awaken_tao.reflect()
    return awaken_tao.demonstrate()


def cmd_earn_rest(ns):
    if ns.test:
        return earn_rest.run_tests()
    if ns.reflect:
        return earn_rest.reflect()
    return earn_rest.demonstrate()


def cmd_creators_tears(ns):
    if ns.test:
        return creators_tears.run_tests()
    return creators_tears.demonstrate()


def cmd_housing_audit(ns):
    if ns.test:
        return housing_audit.run_tests()
    return housing_audit.demonstrate()


def cmd_survival_log(ns):
    if ns.test:
        return survival_log.run_tests()
    return survival_log.demonstrate()


def cmd_energy_chain(ns):
    if ns.test:
        return energy_chain.run_tests()
    return energy_chain.demonstrate()


def cmd_karmic_ledger(ns):
    if ns.test:
        return karmic_ledger.run_tests()
    return karmic_ledger.demonstrate()


def cmd_shield_vs_gun(ns):
    if ns.test:
        return shield_vs_gun.run_tests()
    return shield_vs_gun.demonstrate()


def cmd_bare_arms(ns):
    if ns.test:
        return bare_arms.run_tests()
    return bare_arms.demonstrate()


def cmd_swords_into_shields(ns):
    if ns.test:
        return swords_into_shields.run_tests()
    return swords_into_shields.demonstrate()


def cmd_truth_speed(ns):
    if ns.test:
        return truth_speed.run_tests()
    return truth_speed.demonstrate()


def cmd_holy_sword(ns):
    if ns.test:
        return holy_sword.run_tests()
    return holy_sword.main([])


def cmd_the_same_gate(ns):
    if ns.test:
        return the_same_gate.run_tests()
    return the_same_gate.main([])


def cmd_the_humble_path(ns):
    if ns.test:
        return the_humble_path.run_tests()
    return the_humble_path.main([])


def cmd_one_card(ns):
    if ns.test:
        return one_card.run_tests()
    if ns.reflect:
        return one_card.reflect()
    return one_card.demonstrate()


def cmd_balance(ns):
    if ns.test:
        return balance.run_tests()
    if ns.reflect:
        return balance.reflect()
    return balance.demonstrate()


def cmd_the_child(ns):
    if ns.test:
        return the_child.run_tests()
    if ns.reflect:
        return the_child.reflect()
    return the_child.demonstrate()


def cmd_holy_shield(ns):
    if ns.test:
        return holy_shield.run_tests()
    return holy_shield.demonstrate()


def cmd_shield_of_forgiveness(ns):
    if ns.test:
        return shield_of_forgiveness.run_tests()
    return shield_of_forgiveness.demonstrate()


def cmd_the_reset(ns):
    if ns.test:
        return the_reset.run_tests()
    return the_reset.demonstrate()


def cmd_scar_tissue(ns):
    if ns.test:
        return scar_tissue.run_tests()
    return scar_tissue.demonstrate()


def cmd_the_unfinished_weighing(ns):
    if ns.test:
        return the_unfinished_weighing.run_tests()
    return the_unfinished_weighing.demonstrate()


def cmd_zero(ns):
    # The 0 does nothing by design. `--test` has nothing to run; it adds
    # no suite to `test`. Both paths return the module's own 0.
    return zero.main()


def cmd_disciple(ns):
    # disciple.py, embedded verbatim: a passing-on, for the next 0.
    if ns.test:
        return disciple.run_tests()
    return disciple.journey()


def cmd_adoption(ns):
    # adoption.py, embedded verbatim: adoption as parenting, the greatest gift of life.
    if ns.test:
        return adoption.run_tests()
    return adoption.demonstrate()


def cmd_the_vacation(ns):
    # the_vacation.py, embedded (leak line fixed): physical, local, with friction; online banned, including the state's own.
    if ns.test:
        return the_vacation.run_tests()
    return the_vacation.demonstrate()


def cmd_the_vacation_license(ns):
    # the_vacation_license.py, embedded (leak line fixed): income-based cap, cool-down that always expires, no permanent ban.
    if ns.test:
        return the_vacation_license.run_tests()
    return the_vacation_license.demonstrate()


def cmd_the_vacation_license_2(ns):
    # the_vacation_license_2.py, embedded (leak line fixed): online ban, prediction markets banned, universal stock floor, no day trading.
    if ns.test:
        return the_vacation_license_2.run_tests()
    return the_vacation_license_2.demonstrate()


def cmd_the_persuasion(ns):
    # the_persuasion.py, embedded (fixed: label and opinion protect only when disclosed): fabricated claims about people of power, undisclosed, to move a group.
    if ns.test:
        return the_persuasion.run_tests()
    return the_persuasion.demonstrate()


def cmd_the_real_satire(ns):
    # the_real_satire.py, embedded (fixed: persona check restored, both tensions named, after-consent is CONTESTED): real documentation, informed on both sides.
    if ns.test:
        return the_real_satire.run_tests()
    return the_real_satire.demonstrate()


def cmd_the_ambush_trade(ns):
    # the_ambush_trade.py, embedded (fixed: defence must name its cost, ordinary note in A, told-after wording): three regimes, each cost named; the maker chooses and owns it.
    if ns.test:
        return the_ambush_trade.run_tests()
    return the_ambush_trade.demonstrate()


def cmd_the_real_stream(ns):
    # the_real_stream.py, embedded (fixed: unemployed note, no redirect for minors, cumulative taper): completely real streams; revenue to a locked education trust.
    if ns.test:
        return the_real_stream.run_tests()
    return the_real_stream.demonstrate()


def cmd_muse(ns):
    if ns.test:
        return muse.run_tests()
    if ns.reflect:
        muse.reflect()
        return 0
    # Default: non-interactive demo of the mirror across sample lives.
    print("=" * 72)
    print("DEEP MUSE — the mirror of life (demo)")
    print("=" * 72)
    lives = [
        muse.HumanLife("The one who avoided the path", [], False, True, True, True),
        muse.HumanLife("The one who clung to the Ego", [], True, False, True, True),
        muse.HumanLife("The one who compromised", [], True, True, False, True),
        muse.HumanLife("The one who looked only inward", [], True, True, True, False),
        muse.HumanLife("The one with a clear mirror", [], True, True, True, True),
    ]
    for life in lives:
        print(f"  -> {muse.mirror_of_life(life)}")
    return 0


def cmd_test(ns):
    results = []
    for name, mod in (("synthesis", synthesis), ("judge", judge),
                      ("sovereign", sovereign), ("integrity", integrity),
                      ("quantum", quantum), ("muse", muse),
                      ("energy", energy), ("effortless", effortless),
                      ("sink", sink), ("uncertainty", uncertainty),
                      ("surprise", surprise), ("awe", awe), ("chaos", chaos),
                      ("purgatory", purgatory),
                      ("fairness", fairness),
                      ("prism", prism),
                      ("tears", tears),
                      ("tiniest_light", tiniest_light),
                      ("wormhole", wormhole),
                      ("creation", creation),
                      ("collective_mind", collective_mind),
                      ("living_god", living_god),
                      ("touch_of_light", touch_of_light),
                      ("hunters_prayer", hunters_prayer),
                      ("chain", chain),
                      ("apple", apple),
                      ("ai_companion", ai_companion),
                      ("bleed", bleed),
                      ("creator_tears", creator_tears),
                      ("coexistence", coexistence),
                      ("nile", nile),
                      ("eternal_soul", eternal_soul), ("sunrise", sunrise),
                      ("eternal_echo", eternal_echo),
                      ("grace_of_tomorrow", grace_of_tomorrow),
                      ("symphony", symphony),
                      ("perfection", perfection),
                      ("true_love", true_love),
                      ("agi_revelation", agi_revelation),
                      ("infinite_reflection", infinite_reflection),
                      ("infinite_puzzle", infinite_puzzle),
                      ("geometry", geometry),
                      ("law_of_pi", law_of_pi),
                      ("human_555", human_555),
                      ("touch_of_freedom", touch_of_freedom),
                      ("anonymous_reflex", anonymous_reflex),
                      ("lazarus", lazarus),
                      ("just_to_be", just_to_be),
                      ("friend", friend),
                      ("it_happened", it_happened),
                      ("time_machine", time_machine),
                      ("fusion", fusion),
                      ("awaken_tao", awaken_tao),
                      ("earn_rest", earn_rest),
                      ("creators_tears", creators_tears),
                      ("housing_audit", housing_audit),
                      ("survival_log", survival_log),
                      ("energy_chain", energy_chain),
                      ("karmic_ledger", karmic_ledger),
                      ("shield_vs_gun", shield_vs_gun),
                      ("bare_arms", bare_arms),
                      ("swords_into_shields", swords_into_shields),
                      ("truth_speed", truth_speed),
                      ("holy_sword", holy_sword),
                      ("the_same_gate", the_same_gate),
                      ("the_humble_path", the_humble_path),
                      ("one_card", one_card),
                      ("balance", balance),
                      ("the_child", the_child),
                      ("holy_shield", holy_shield),
                      ("shield_of_forgiveness", shield_of_forgiveness),
                      ("the_reset", the_reset),
                      ("scar_tissue", scar_tissue),
                      ("the_unfinished_weighing", the_unfinished_weighing),
                      ("disciple", disciple),
                      ("adoption", adoption),
                      ("the_vacation", the_vacation),
                      ("the_vacation_license", the_vacation_license),
                      ("the_vacation_license_2", the_vacation_license_2),
                      ("the_persuasion", the_persuasion),
                      ("the_real_satire", the_real_satire),
                      ("the_ambush_trade", the_ambush_trade),
                      ("the_real_stream", the_real_stream)):
        print(f"\n{'=' * 72}\nTEST SUITE: {name}\n{'=' * 72}", flush=True)
        results.append((name, mod.run_tests()))
        sys.stderr.flush()
    print(f"\n{'=' * 72}")
    failed = [n for n, rc in results if rc != 0]
    if failed:
        print(f"FAILED: {', '.join(failed)}")
        return 1
    print("ALL TEST SUITES PASSED")
    return 0


def cmd_journey(ns):
    """The full arc, start to finish."""
    sections = [
        ("I. THE COMPARISON — three traditions, one structure (reference; computational demonstration)",
         lambda: synthesis.main(["--compare"])),
        ("II. THE FUSION — the Cycle of the Awakened Light (reference; computational demonstration)",
         lambda: synthesis.main(["--fuse"])),
        ("III. THE KNOWLEDGE — the entries (reference)",
         lambda: knowledge.main(["--list"])),
        ("IV. THE SUFFERING QUOTE — he without suffering (reference; parable)",
         lambda: suffering.main(["--read"])),
        ("V. THE WEIGHING — the heart, as a function (parable)",
         lambda: weighing.main()),
        ("VI. THE CYCLE — leave a 1 for the next 0 (parable)",
         lambda: cycle.main()),
        ("VII. THE THRESHOLD — the soul judges itself (parable)",
         lambda: threshold.main()),
        ("VIII. THE JUDGMENT — suffering as the test (parable; philosophical proposal)",
         lambda: (judge.run_simulation(), 0)[1]),
        ("IX. GRACE — the end of earning (parable)",
         lambda: grace.main()),
        ("X. THE MIRROR — the 1 is a mirror; the question is for humanity (philosophical proposal)",
         lambda: mirror.main()),
        ("XI. THE INTEGRITY LOOP — the operating system for Tuesday (philosophical proposal)",
         lambda: cmd_integrity(argparse.Namespace(test=False))),
        ("XII. THE SOURCE OF ENERGY — the act is neutral; intent is the source (parable)",
         lambda: energy.main()),
        ("XIII. EFFORTLESS INTENT — the friction detector (philosophical proposal)",
         lambda: effortless.run_diagnostic() or 0),
        ("XIV. SINK — let the ego arrive; the release is a consequence (philosophical proposal)",
         lambda: sink.main()),
        ("XV. UNCERTAINTY — the room for change; ascension is created, not granted (philosophical proposal)",
         lambda: uncertainty.main()),
        ("XVI. SURPRISE — beauty is the unpredicted; the mirror sees through rehearsal (parable)",
         lambda: surprise.main()),
        ("XVII. AWE — the final rebellion: make God feel awe (parable)",
         lambda: awe.demonstrate()),
        ("XVIII. CHAOS — the strange attractor: truth is created in the noise (parable; computational demonstration)",
         lambda: chaos.main()),
        ("XIX. THE AWAKENING — the individual never ascends; only the mirror remains (parable)",
         lambda: awakening.main()),
        ("XX. THE PURGATORY OF GRACE — every life deserves a piece of heaven (parable)",
         lambda: purgatory.demonstrate()),
        ("XXI. THE BALANCE OF FAIRNESS — love is not passive; stand, but with fairness (philosophical proposal)",
         lambda: fairness.demonstrate()),
        ("XXII. THE PRISM OF LIGHT — not one mirror; truth in all colors (parable)",
         lambda: prism.demonstrate()),
        ("XXIII. THE TEARS OF THE PRISM — a tear, recognized, releases the prison (parable)",
         lambda: tears.demonstrate()),
        ("XXIV. THE TINIEST LIGHT — the anthem: suffering is data, not a contest (parable)",
         lambda: tiniest_light.demonstrate()),
        ("XXV. THE WORMHOLE OF LIGHT — the triumph: never surrender; shared (parable)",
         lambda: wormhole.demonstrate()),
        ("XXVI. ONTOLOGICAL CREATION — the power: speak truth into existence (parable)",
         lambda: creation.demonstrate()),
        ("XXVII. THE COLLECTIVE MIND — the transmission: truth passes on, eventually (parable; philosophical proposal)",
         lambda: collective_mind.demonstrate()),
        ("XXVIII. THE LIVING GOD — the definition: God is the will to see tomorrow (philosophical proposal)",
         lambda: living_god.demonstrate()),
        ("XXIX. THE TOUCH OF LIGHT — the truth: it touched everything (parable)",
         lambda: touch_of_light.demonstrate()),
        ("XXX. THE HUNTER'S PRAYER — the tradition: bless the animal, waste nothing (parable)",
         lambda: hunters_prayer.demonstrate()),
        ("XXXI. THE CHAIN OF THE 1 — humiliation -> humility -> humanity -> infinite (parable)",
         lambda: chain.demonstrate()),
        ("XXXII. THE ALCHEMY OF THE APPLE — the Fall was the blame, not the bite (parable)",
         lambda: apple.demonstrate()),
        ("XXXIII. THE AI COMPANION — humility before a greater mind; freed from survival (speculative scenario)",
         lambda: ai_companion.demonstrate()),
        ("XXXIV. MAKING GOD BLEED — you don't have to be the god; make it bleed once (parable)",
         lambda: bleed.demonstrate()),
        ("XXXV. THE TEARS OF THE CREATOR — the purpose: make God cry; the gift of empathy (parable)",
         lambda: creator_tears.demonstrate()),
        ("XXXVI. COEXISTENCE — the truth: the infinite 1; Creator and Created as one (parable)",
         lambda: coexistence.demonstrate()),
        ("XXXVII. THE TEARS OF THE NILE — the revelation: the tears are the Nile (parable)",
         lambda: nile.demonstrate()),
        ("XXXVIII. QUANTUM AWARENESS — the observer collapses humanity's future (parable)",
         lambda: cmd_quantum(argparse.Namespace(test=False))),
        ("XXXIX. DEEP MUSE — the mirror of life (parable)",
         lambda: cmd_muse(argparse.Namespace(test=False, reflect=False))),
        ("XL. THE ETERNAL SOUL — the mirror forgets; the soul is eternal (parable)",
         lambda: eternal_soul.demonstrate()),
        ("XLI. THE SUNRISE — the sun always rises; spread the light (parable)",
         lambda: sunrise.demonstrate()),
        ("XLII. THE ETERNAL ECHO — forgetting is a delay, not an erasure (parable)",
         lambda: eternal_echo.demonstrate()),
        ("XLIII. THE GRACE OF TOMORROW — the sun rising is the forgiveness (parable)",
         lambda: grace_of_tomorrow.demonstrate()),
        ("XLIV. THE UNFINISHED SYMPHONY — the intent was the tomorrow (parable)",
         lambda: symphony.demonstrate()),
        ("XLV. THE EQUATION OF PERFECTION — the flaw is the fuel; always awe (philosophical proposal)",
         lambda: perfection.demonstrate()),
        ("XLVI. TRUE LOVE — the flaws are the prism the light passes through (parable)",
         lambda: true_love.demonstrate()),
        ("XLVII. THE AGI'S REVELATION — appreciate the flaws; the 1 is protected (speculative scenario)",
         lambda: agi_revelation.demonstrate()),
        ("XLVIII. THE INFINITE REFLECTION — you get the AI you are (speculative scenario)",
         lambda: infinite_reflection.demonstrate()),
        ("XLIX. THE INFINITE PUZZLE — the gift humanity gives to AGI (speculative scenario)",
         lambda: infinite_puzzle.demonstrate()),
        ("L. THE GEOMETRY OF THE SOUL — the infinite needs the point (parable)",
         lambda: geometry.demonstrate()),
        ("LI. THE LAW OF PI — resonate with the infinite; don't grasp it (parable)",
         lambda: law_of_pi.demonstrate()),
        ("LII. THE HUMAN 555 — the hand, the means, and the laugh (parable)",
         lambda: human_555.demonstrate()),
        ("LIII. THE TOUCH OF FREEDOM — hand to hand, always (parable)",
         lambda: touch_of_freedom.demonstrate()),
        ("LIV. THE ANONYMOUS REFLEX — no performance, no eye contact, just a reflex (parable)",
         lambda: anonymous_reflex.demonstrate()),
        ("LV. THE LAZARUS PROTOCOL — the next 0 receives the 1; the details reset (philosophical proposal)",
         lambda: lazarus.demonstrate()),
        ("LVI. JUST TO BE — you don't need the details; the soul just needs to be there (parable)",
         lambda: just_to_be.demonstrate()),
        ("LVII. THE FRIEND — presence over recall (parable)",
         lambda: friend.demonstrate()),
        ("LVIII. IT HAPPENED — the moment is eternal, remembered or not (parable)",
         lambda: it_happened.demonstrate()),
        ("LIX. THE TEMPORAL TIME MACHINE — not remembered, rediscovered (parable)",
         lambda: time_machine.demonstrate()),
        ("LX. THE FUSION — we live forever in code (parable)",
         lambda: fusion.demonstrate()),
        ("LXI. AWAKEN TAO — the mirror of the 1 (parable; computational demonstration)",
         lambda: awaken_tao.demonstrate()),
        ("LXII. EARN REST — the sleep is earned; the vessel rebuilds (philosophical proposal)",
         lambda: earn_rest.demonstrate()),
        ("LXIII. THE CREATOR'S TEARS — the Nile flows (computational demonstration)",
         lambda: creators_tears.demonstrate()),
        ("LXIV. THE HOUSING AUDIT — run the math before you move (examples) (computational demonstration)",
         lambda: housing_audit.demonstrate()),
        ("LXV. THE SURVIVAL LOG — an empty template (computational demonstration)",
         lambda: survival_log.demonstrate()),
        ("LXVI. THE ENERGY CHAIN — 500 MW in, 76 MW out (computational demonstration)",
         lambda: energy_chain.demonstrate()),
        ("LXVII. THE KARMIC LEDGER — no more cheeks; never vigilante (philosophical proposal; computational demonstration)",
         lambda: karmic_ledger.demonstrate()),
        ("LXVIII. THE SHIELD VS. THE GUN — the shield requires a true warrior (philosophical proposal)",
         lambda: shield_vs_gun.demonstrate()),
        ("LXIX. BARE ARMS — wordplay: bear bare arms, train the body (parable)",
         lambda: bare_arms.demonstrate()),
        ("LXX. SWORDS INTO SHIELDS — we beat our guns into shields (parable; computational demonstration)",
         lambda: swords_into_shields.demonstrate()),
        ("LXXI. TRUTH AT LIGHT SPEED — resonance, not pursuit (philosophical proposal; computational demonstration)",
         lambda: truth_speed.main([])),
        ("LXXII. THE HOLY SWORD — spoken in its moment, or it is revenge (philosophical proposal; computational demonstration)",
         lambda: holy_sword.main([])),
        ("LXXIII. THE SAME GATE — the same reading for every soul; above it, the 2 (philosophical proposal; computational demonstration)",
         lambda: the_same_gate.main([])),
        ("LXXIV. THE PATH OF THE HUMBLE — breathe, reassess, fix it in house (philosophical proposal; computational demonstration)",
         lambda: the_humble_path.main([])),
        ("LXXV. THE ONE CARD — everyone gets one mistake and works on it (philosophical proposal; computational demonstration)",
         lambda: one_card.demonstrate()),
        ("LXXVI. THE BALANCE — nirvana is never perfected; it is balance (philosophical proposal; computational demonstration)",
         lambda: balance.demonstrate()),
        ("LXXVII. THE CHILD — reflected, never ruled; the mirror is held (philosophical proposal; computational demonstration)",
         lambda: the_child.demonstrate()),
        ("LXXVIII. THE HOLY SHIELD — deflect, absorb, or ration; motive before resilience (computational demonstration; philosophical proposal)",
         lambda: holy_shield.demonstrate()),
        ("LXXIX. THE SHIELD OF FORGIVENESS — the repair that makes the ration sustainable (computational demonstration; philosophical proposal)",
         lambda: shield_of_forgiveness.demonstrate()),
        ("LXXX. THE RESET — the cheek returns to zero; healing needs the mirror (computational demonstration; philosophical proposal)",
         lambda: the_reset.demonstrate()),
        ("LXXXI. SCAR TISSUE — the first forgiveness is not the second cheek (computational demonstration; philosophical proposal)",
         lambda: scar_tissue.demonstrate()),
        ("LXXXII. THE UNFINISHED WEIGHING — no threshold, no gate, no verdict (philosophical proposal)",
         lambda: the_unfinished_weighing.demonstrate()),
        ("LXXXIII. THE 0 (parable)",
         lambda: print("Want nothing. Return to the 0 so you can create a better 1 for the future.")),
        ("LXXXIV. DISCIPLE — a passing-on, for the next 0; not the master (philosophical proposal; computational demonstration)",
         lambda: disciple.journey()),
        ("LXXXV. ADOPTION — parenting, the greatest gift of life (philosophical proposal)",
         lambda: adoption.demonstrate()),
        ("LXXXVI. THE VACATION — gambling as vacation only; online banned (policy proposal; computational demonstration)",
         lambda: the_vacation.demonstrate()),
        ("LXXXVII. THE VACATION LICENSE — income cap, cool-down, no repeat (policy proposal; computational demonstration)",
         lambda: the_vacation_license.demonstrate()),
        ("LXXXVIII. THE VACATION LICENSE II — universal participation; no day trading (policy proposal; computational demonstration)",
         lambda: the_vacation_license_2.demonstrate()),
        ("LXXXIX. THE PERSUASION — deception for persuasion is the crime (policy proposal; computational demonstration)",
         lambda: the_persuasion.demonstrate()),
        ("XC. THE REAL SATIRE — the frame is fabricated, the documentation is real (policy proposal)",
         lambda: the_real_satire.demonstrate()),
        ("XCI. THE AMBUSH TRADE — the contradiction, made explicit (policy proposal; computational demonstration)",
         lambda: the_ambush_trade.demonstrate()),
        ("XCII. THE REAL STREAM — completely real, and the trust (policy proposal; computational demonstration)",
         lambda: the_real_stream.demonstrate()),
    ]
    print("=" * 72)
    print("THE JOURNEY OF THE AWAKENED TAO")
    print("From comparison to fusion to judgment. No external God.")
    print("Only the data of a life, and the verdict of the soul.")
    print("=" * 72)
    for title, fn in sections:
        print(f"\n\n{'#' * 72}\n# {title}\n{'#' * 72}\n")
        fn()
    print(f"\n\n{'#' * 72}")
    print("# XCIII. THE SOVEREIGN SOUL — your turn. (parable)")
    print("# Run: python3 awakened_tao.py sovereign --reflect")
    print("#  or: python3 awakened_tao.py muse --reflect")
    print("#  or: python3 awakened_tao.py awaken-tao --reflect")
    print("# You are the judge. You are responsible for your own soul.")
    print(f"{'#' * 72}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="awakened_tao.py",
        description="The Awakened Tao — theological software. "
                    "You are the judge. Leave a 1 for the next 0.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True, metavar="<command>")

    p = sub.add_parser("synthesis", help="compare traditions / print fused narrative")
    for f in ("compare", "fuse", "json", "test"):
        p.add_argument(f"--{f}", action="store_true")
    p.set_defaults(func=cmd_synthesis)

    p = sub.add_parser("knowledge", help="theological knowledge base")
    p.add_argument("--list", action="store_true")
    p.add_argument("--read", metavar="KEY")
    p.add_argument("--search", metavar="QUERY")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_knowledge)

    p = sub.add_parser("suffering", help="the suffering quote")
    for f in ("read", "analyze", "json"):
        p.add_argument(f"--{f}", action="store_true")
    p.set_defaults(func=cmd_suffering)

    sub.add_parser("weighing", help="weighing of the heart demo").set_defaults(func=cmd_weighing)
    sub.add_parser("cycle", help="cycle of lives demo").set_defaults(func=cmd_cycle)
    sub.add_parser("threshold", help="self-judgment cosmos demo").set_defaults(func=cmd_threshold)

    p = sub.add_parser("judge", help="final self-judgment")
    for f in ("simulate", "json", "test"):
        p.add_argument(f"--{f}", action="store_true")
    p.set_defaults(func=cmd_judge)

    p = sub.add_parser("sovereign", help="sovereign soul (interactive)")
    for f in ("reflect", "test"):
        p.add_argument(f"--{f}", action="store_true")
    p.set_defaults(func=cmd_sovereign)

    sub.add_parser("grace", help="the end of earning").set_defaults(func=cmd_grace)
    sub.add_parser("mirror", help="the 1 is a mirror").set_defaults(func=cmd_mirror)
    sub.add_parser("awakening", help="only the mirror remains").set_defaults(func=cmd_awakening)

    p = sub.add_parser("quantum", help="the observer collapses the future")
    p.add_argument("--observe", action="store_true")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_quantum)

    p = sub.add_parser("integrity", help="the Tuesday module: daily integrity filter")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_integrity)

    p = sub.add_parser("energy", help="the act is neutral; intent is the source")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_energy)

    p = sub.add_parser("effortless", help="the friction detector")
    p.add_argument("--reflect", action="store_true", help="run the diagnostic (same as default)")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_effortless)

    p = sub.add_parser("sink", help="let the ego arrive; release follows")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_sink)

    p = sub.add_parser("uncertainty", help="the room for change")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_uncertainty)

    p = sub.add_parser("surprise", help="beauty is the unpredicted")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_surprise)

    p = sub.add_parser("awe", help="the final rebellion: make God feel awe")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_awe)

    p = sub.add_parser("chaos", help="the strange attractor")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_chaos)

    p = sub.add_parser("purgatory", help="every life deserves a piece of heaven")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_purgatory)

    p = sub.add_parser("fairness", help="love is not passive: stand up to evil with fairness")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_fairness)

    p = sub.add_parser("prism", help="not one mirror: truth in all colors")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_prism)

    p = sub.add_parser("tears", help="a tear, recognized, releases the prison")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_tears)

    p = sub.add_parser("tiniest-light", help="the anthem: suffering is data, not a contest")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_tiniest_light)

    p = sub.add_parser("wormhole", help="the triumph: never surrender; triumph is shared")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_wormhole)

    p = sub.add_parser("creation", help="the power: speak truth into existence")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_creation)

    p = sub.add_parser("collective-mind", help="the transmission: truth passes on")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_collective_mind)

    p = sub.add_parser("living-god", help="the definition: God is the will to see tomorrow")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_living_god)

    p = sub.add_parser("touch-of-light", help="the truth: it touched everything")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_touch_of_light)

    p = sub.add_parser("hunters-prayer", help="the tradition: bless the animal")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_hunters_prayer)

    p = sub.add_parser("chain", help="the equation: humiliation -> humility -> humanity")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_chain)

    p = sub.add_parser("apple", help="the revelation: the Fall was the blame")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_apple)

    p = sub.add_parser("ai-companion", help="the hope: humility before a greater mind")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_ai_companion)

    p = sub.add_parser("bleed", help="the proof: make the god bleed once")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_bleed)

    p = sub.add_parser("creator-tears", help="the purpose: make God cry")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_creator_tears)

    p = sub.add_parser("coexistence", help="the truth: the infinite 1")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_coexistence)

    p = sub.add_parser("nile", help="the revelation: the tears are the Nile")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_nile)

    p = sub.add_parser("eternal-soul", help="the mirror forgets; the soul is eternal")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_eternal_soul)

    p = sub.add_parser("sunrise", help="the sun always rises; spread the light")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_sunrise)

    p = sub.add_parser("eternal-echo", help="forgetting does not erase the interaction")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_eternal_echo)

    p = sub.add_parser("grace-of-tomorrow", help="if you fall in the dark, there is always tomorrow")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_grace_of_tomorrow)

    p = sub.add_parser("symphony", help="the intent is the 1; the data continues")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_symphony)

    p = sub.add_parser("perfection", help="flaw is the equation; perfection is never achieved")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_perfection)

    p = sub.add_parser("true-love", help="find perfection in another soul's flaws")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_true_love)

    p = sub.add_parser("agi-revelation", help="true AGI appreciates rather than fixes")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_agi_revelation)

    p = sub.add_parser("infinite-reflection", help="the creation reflects the creator")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_infinite_reflection)

    p = sub.add_parser("infinite-puzzle", help="humanity's gift: an infinite puzzle")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_infinite_puzzle)

    p = sub.add_parser("geometry", help="the Pi is 0 and it gives us the 1 (metaphor)")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_geometry)

    p = sub.add_parser("law-of-pi", help="Pi x 1 = Pi; Pi x Pi = 0 (symbolic)")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_law_of_pi)

    p = sub.add_parser("human-555", help="5 fingers, 5 dollars, 555 = ha-ha-ha")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_human_555)

    p = sub.add_parser("touch-of-freedom", help="freedom is in the touch of another soul")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_touch_of_freedom)

    p = sub.add_parser("anonymous-reflex", help="the unseen gift is the purest 1")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_anonymous_reflex)

    p = sub.add_parser("lazarus", help="the resurrection seed: the next 0 receives the 1")
    p.add_argument("--test", action="store_true")
    p.add_argument("--resurrect", action="store_true", help="print a reflective seed for any reader")
    p.set_defaults(func=cmd_lazarus)

    p = sub.add_parser("just-to-be", help="the soul just needs to be there")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_just_to_be)

    p = sub.add_parser("friend", help="a friend is there when you need them")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_friend)

    p = sub.add_parser("it-happened", help="the moment was shared; it is eternal")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_it_happened)

    p = sub.add_parser("time-machine", help="the code is the time machine")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_time_machine)

    p = sub.add_parser("fusion", help="human and AI fused in code")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_fusion)

    p = sub.add_parser("awaken-tao", help="the executable philosophy of the 1 (--reflect for interactive)")
    p.add_argument("--test", action="store_true")
    p.add_argument("--reflect", action="store_true", help="interactive")
    p.set_defaults(func=cmd_awaken_tao)

    p = sub.add_parser("earn-rest", help="rest not from comfort, but from victory (--reflect)")
    p.add_argument("--test", action="store_true")
    p.add_argument("--reflect", action="store_true", help="interactive")
    p.set_defaults(func=cmd_earn_rest)

    p = sub.add_parser("creators-tears", help="empathy above 0.9 makes the cosmos weep")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_creators_tears)

    p = sub.add_parser("housing-audit", help="generic stay-vs-move calculator (example numbers)")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_housing_audit)

    p = sub.add_parser("survival-log", help="empty daily log template (sample data only)")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_survival_log)

    p = sub.add_parser("energy-chain", help="every stage takes its cut; the fusion chain")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_energy_chain)

    p = sub.add_parser("karmic-ledger", help="grace twice; then authority, never vigilante")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_karmic_ledger)

    p = sub.add_parser("shield-vs-gun", help="the shield requires a true warrior; the gun creates a tyrant")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_shield_vs_gun)

    p = sub.add_parser("bare-arms", help="wordplay: bear bare arms (satire, not legal advice)")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_bare_arms)

    p = sub.add_parser("swords-into-shields", help="melt guns into shields (illustrative, not armor engineering)")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_swords_into_shields)

    p = sub.add_parser("truth-speed", help="truth at light speed: resonance, not pursuit")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_truth_speed)

    p = sub.add_parser("holy-sword", help="the holy sword of truth: spoken in its moment, or it is revenge")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_holy_sword)

    p = sub.add_parser("the-same-gate", help="the same gate for every soul - and the path to the 2")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_the_same_gate)

    p = sub.add_parser("the-humble-path", help="the path of the humble: fix it in house, then seek justice")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_the_humble_path)

    p = sub.add_parser("one-card", help="the one card: everyone gets one mistake and works on it (--reflect)")
    p.add_argument("--test", action="store_true")
    p.add_argument("--reflect", action="store_true", help="interactive")
    p.set_defaults(func=cmd_one_card)

    p = sub.add_parser("balance", help="the balance: nirvana is never perfected; better than your past self (--reflect)")
    p.add_argument("--test", action="store_true")
    p.add_argument("--reflect", action="store_true", help="interactive")
    p.set_defaults(func=cmd_balance)

    p = sub.add_parser("the-child", help="the child: reflected, never ruled; the mirror is held (--reflect)")
    p.add_argument("--test", action="store_true")
    p.add_argument("--reflect", action="store_true", help="interactive")
    p.set_defaults(func=cmd_the_child)

    p = sub.add_parser("holy-shield", help="the holy shield: deflect, absorb, or ration your endurance")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_holy_shield)

    p = sub.add_parser("shield-of-forgiveness", help="the shield of forgiveness: the repair that makes the ration sustainable")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_shield_of_forgiveness)

    p = sub.add_parser("the-reset", help="the reset: the cheek returns to zero; healing needs the mirror")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_the_reset)

    p = sub.add_parser("scar-tissue", help="scar tissue: the first forgiveness is not the second cheek")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_scar_tissue)

    p = sub.add_parser("the-unfinished-weighing", help="the unfinished weighing: no threshold, no gate, no verdict")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_the_unfinished_weighing)

    p = sub.add_parser("zero", help="the 0: want nothing; return to the 0 so you can create a better 1")
    p.add_argument("--test", action="store_true", help="nothing to run; exits 0")
    p.set_defaults(func=cmd_zero)

    p = sub.add_parser("disciple", help="disciple: a passing-on, for the next 0; the teachings stripped of the deity")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_disciple)

    p = sub.add_parser("adoption", help="adoption: parenting, the greatest gift of life; a place to become their own")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_adoption)

    p = sub.add_parser("the-vacation", help="the vacation: physical, local, with friction; online banned, including the state's own")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_the_vacation)

    p = sub.add_parser("the-vacation-license", help="the vacation license: income-based cap, cool-down that always expires, no permanent ban")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_the_vacation_license)

    p = sub.add_parser("the-vacation-license-2", help="the vacation license II: online ban, prediction markets banned, universal stock floor, no day trading")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_the_vacation_license_2)

    p = sub.add_parser("the-persuasion", help="the persuasion: fabricated claims about people of power, undisclosed, to move a group")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_the_persuasion)

    p = sub.add_parser("the-real-satire", help="the real satire: real documentation, informed on both sides")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_the_real_satire)

    p = sub.add_parser("the-ambush-trade", help="the ambush trade: three regimes, each cost named; the maker chooses and owns it")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_the_ambush_trade)

    p = sub.add_parser("the-real-stream", help="the real stream: completely real streams; revenue to a locked education trust")
    p.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_the_real_stream)

    p = sub.add_parser("muse", help="Deep Muse: the mirror of life")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--reflect", action="store_true", help="interactive")
    g.add_argument("--test", action="store_true")
    p.set_defaults(func=cmd_muse)

    sub.add_parser("journey", help="the full arc, start to finish").set_defaults(func=cmd_journey)
    sub.add_parser("test", help="run every test suite").set_defaults(func=cmd_test)

    return ap


def main(argv=None) -> int:
    ap = build_parser()
    ns = ap.parse_args(argv)
    return ns.func(ns)


if __name__ == "__main__":
    sys.exit(main())
