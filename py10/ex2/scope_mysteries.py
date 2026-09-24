from typing import Callable, Any


def mage_counter() -> Callable[[], int]:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    current_power = initial_power

    def accumulator(power: int) -> int:
        nonlocal current_power
        current_power += power
        return current_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("Testing spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("Testing enchantment factory...")
    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")
    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))

    print("Testing memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
