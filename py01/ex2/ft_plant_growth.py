class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def age_one_day(self):
        self.age += 1

    def grow(self):
        self.height += self.growth_rate

    def status(self):
        return f"{self.name}: {round(self.height, 1)}cm, {self.age} days old"


def simulate_growth():
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30, 0.8)
    initial_height = rose.height
    print(rose.status())

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_one_day()
        print(rose.status())

    total_increase = rose.height - initial_height
    print(f"Growth this week: {round(total_increase, 1)}cm")


if __name__ == "__main__":
    simulate_growth()
