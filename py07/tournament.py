from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory, CreatureFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import (
    BattleStrategy, NormalStrategy, AggressiveStrategy,
    DefensiveStrategy, StrategyError
)


def tournament(opponents: List[Tuple[CreatureFactory,
                               BattleStrategy]]) -> None:
    print(f"*** Tournament ***\n{len(opponents)} opponents involved")

    creatures = []
    for fact, strat in opponents:
        creatures.append((fact.create_base(), strat))

    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            c1, s1 = creatures[i]
            c2, s2 = creatures[j]
            print("* Battle *")
            print(f"{c1.describe()}\nvs.\n{c2.describe()}\nnow fight!")

            try:
                s1.act(c1)
                s2.act(c2)
            except StrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    f_flame = FlameFactory()
    f_aqua = AquaFactory()
    f_heal = HealingCreatureFactory()
    f_trans = TransformCreatureFactory()

    s_norm = NormalStrategy()
    s_aggr = AggressiveStrategy()
    s_def = DefensiveStrategy()

    print("Tournament 0 (basic)")
    tournament([(f_flame, s_norm), (f_heal, s_def)])

    print("\nTournament 1 (error)")
    tournament([(f_flame, s_aggr), (f_heal, s_def)])

    print("\nTournament 2 (multiple)")
    tournament([(f_aqua, s_norm), (f_heal, s_def), (f_trans, s_aggr)])
