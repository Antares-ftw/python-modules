from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing() -> None:
    print("Testing Creature with healing capability")
    factory = HealingCreatureFactory()
    for label, c in [("base", factory.create_base()),
                     ("evolved", factory.create_evolved())]:
        print(f"{label}:")
        print(c.describe())
        print(c.attack())
        if isinstance(c, HealCapability):
            print(c.heal())


def test_transform() -> None:
    print("\nTesting Creature with transform capability")
    factory = TransformCreatureFactory()
    for label, c in [("base", factory.create_base()),
                     ("evolved", factory.create_evolved())]:
        print(f"{label}:")
        print(c.describe())
        print(c.attack())
        if isinstance(c, TransformCapability):
            print(c.transform())
            print(c.attack())
            print(c.revert())


if __name__ == "__main__":
    test_healing()
    test_transform()
