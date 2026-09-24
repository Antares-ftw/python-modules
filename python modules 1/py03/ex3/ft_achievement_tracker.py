import random


ACHIEVEMENT_POOL = [
    "World Savior", "Master Explorer", "Collector Supreme", "Untouchable",
    "Boss Slayer", "Crafting Genius", "Strategist", "Unstoppable",
    "Speed Runner", "Survivor", "Treasure Hunter", "First Steps",
    "Sharp Mind", "Hidden Path Finder"
]


def gen_player_achievements():
    num = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENT_POOL, num))


def main():
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }

    all_sets = []
    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
        all_sets.append(achievements)

    distinct_all = set().union(*all_sets)
    print(f"\nAll distinct achievements: {distinct_all}")

    common = set(all_sets[0]).intersection(*all_sets[1:])
    print(f"Common achievements: {common}")

    for name, current_set in players.items():
        others_combined = (set().union
                           (*(s for n, s in players.items() if n != name)))
        unique_to_player = current_set.difference(others_combined)
        print(f"Only {name} has: {unique_to_player}")

    total_pool_set = set(ACHIEVEMENT_POOL)
    for name, current_set in players.items():
        missing = total_pool_set.difference(current_set)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    main()
