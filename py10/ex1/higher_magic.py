from typing import Callable


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int],
                   str]) -> Callable[[str, int], tuple[str, str]]:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int],
                       str]) -> Callable[[str, int], str]:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable[[str, int],
                   str]]) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res_a, res_b = combined("Dragon", 10)
    print(f"Combined spell result: {res_a}, {res_b}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: 10, Amplified power calc: {mega_fireball('Goblin', 10)}")

    print("\nTesting conditional caster...")
    high_power_only = conditional_caster(lambda t, p: p > 50, fireball)
    print(f"Low power: {high_power_only('Orc', 20)}")
    print(f"High power: {high_power_only('Orc', 80)}")
