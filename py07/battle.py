from ex0 import FlameFactory, AquaFactory, CreatureFactory


def verify_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    for c in [base, evolved]:
        print(c.describe())
        print(c.attack())


def battle(f1: CreatureFactory, f2: CreatureFactory) -> None:
    print("Testing battle")
    c1 = f1.create_base()
    c2 = f2.create_base()
    print(f"{c1.describe()}\nvs.\n{c2.describe()}\nfight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    flame_fact = FlameFactory()
    aqua_fact = AquaFactory()
    verify_factory(flame_fact)
    verify_factory(aqua_fact)
    battle(flame_fact, aqua_fact)
