import random


def data_alchemy():
    print("=== Game Data Alchemist ===")

    players = ['Alice', 'bob', 'Charlie', 'dylan',
               'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    all_cap = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_cap}")

    only_cap = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_cap}")

    score_dict = {name: random.randint(50, 1000) for name in all_cap}
    print(f"Score dict: {score_dict}")

    avg = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(avg, 2)}")

    high_scores = {name: score for name,
                   score in score_dict.items() if score > avg}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    data_alchemy()
