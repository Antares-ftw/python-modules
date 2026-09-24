import time
import functools
from typing import Callable, Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power:
                    int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power_val = kwargs.get("power",
                                   args[2] if len(args) > 2 else args[0])
            if power_val >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts:
                int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                    else:
                        return (f"Spell casting failed after "
                                f"{max_attempts} attempts")
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.101)
        return "Fireball cast!"
    print(f"Result: {fireball()}")

    print("Testing retrying spell...")

    @retry_spell(3)
    def broken_spell():
        raise RuntimeError("Fizzle")

    @retry_spell(3)
    def wild_spell():
        return "Waaaaaaagh spelled !"

    print(broken_spell())
    print(wild_spell())

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("G4"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))
