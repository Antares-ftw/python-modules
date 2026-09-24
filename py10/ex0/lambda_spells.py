from typing import Any


def artifact_sorter(artifacts:
                    list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts,
                  key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_p = max(mages, key=lambda m: m['power'])['power']
    min_p = min(mages, key=lambda m: m['power'])['power']
    avg_p = round(sum(map(lambda m: m['power'], mages)) / len(mages), 2)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_p
    }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'scrying'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'destruction'}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    print(f"{sorted_artifacts[0]['name']} "
          f"({sorted_artifacts[0]['power']} power) "
          f"comes before {sorted_artifacts[1]['name']} "
          f"({sorted_artifacts[1]['power']} power)")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    mages = [
        {'name': 'Evoker', 'power': 100, 'element': 'Fire'},
        {'name': 'Apprentice', 'power': 20, 'element': 'Water'},
        {'name': 'Scholar', 'power': 45, 'element': 'Earth'}
    ]
    print("\nTesting mage stats...")
    print(mage_stats(mages))
