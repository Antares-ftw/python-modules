import functools
import operator
from typing import Callable, Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")

    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable[[int, str, str],
                      str]) -> dict[str, Callable[[str], str]]:
    return {
        "fire": functools.partial(base_enchantment, power=50, element="fire"),
        "ice": functools.partial(base_enchantment, power=50, element="ice"),
        "lightning": functools.partial(base_enchantment,
                                       power=50, element="lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Fibonacci sequence is "
                         "undefined for negative integers.")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(3.14))
