class Plant:
    def __init__(self, name, size=0.0, age=0):
        self.name = name
        self.size = float(size)
        self.age_days = age
        self._stats = self.Analytics()

    class Analytics:
        def __init__(self):
            self.__grow_calls = 0
            self.__age_calls = 0
            self.__show_calls = 0

        def increment(self, call_type):
            if call_type == "grow":
                self.__grow_calls += 1
            elif call_type == "age":
                self.__age_calls += 1
            elif call_type == "show":
                self.__show_calls += 1

        def display(self):
            print(f"Stats: {self.__grow_calls} grow, "
                  f"{self.__age_calls} age, {self.__show_calls} show")

    @staticmethod
    def is_older_than_year(days):
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    def grow(self, amount):
        self.size += amount
        self._stats.increment("grow")

    def age(self, days):
        self.age_days += days
        self._stats.increment("age")

    def show(self):
        print(f"{self.name}: {round(self.size, 1)}cm, "
              f"{self.age_days} days old")
        self._stats.increment("show")


class Flower(Plant):
    def __init__(self, name, size, age, color):
        super().__init__(name, size, age)
        self.color = color
        self.bloomed = False

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(self, name, size, age, color):
        super().__init__(name, size, age, color)
        self.seed_count = 0

    def set_seeds(self, count):
        if self.bloomed:
            self.seed_count = count

    def show(self):
        super().show()
        print(f"Seeds: {self.seed_count}")


class Tree(Plant):
    def __init__(self, name, size, age, trunk_diameter):
        super().__init__(name, size, age)
        self.trunk_diameter = trunk_diameter
        self._stats = self.TreeAnalytics()

    class TreeAnalytics(Plant.Analytics):
        def __init__(self):
            super().__init__()
            self.__shade_calls = 0

        def increment(self, call_type):
            if call_type == "shade":
                self.__shade_calls += 1
            else:
                super().increment(call_type)

        def display(self):
            super().display()
            print(f"{self.__shade_calls} shade")

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of "
              f"{self.size}cm long and {self.trunk_diameter}wide.")
        self._stats.increment("shade")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


def display_plant_stats(plant):
    print(f"[statistics for {plant.name}]")
    plant._stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("\n")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_stats(rose)
    print("\n")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)
    print("\n")

    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.set_seeds(42)
    sunflower.show()
    display_plant_stats(sunflower)
    print("\n")

    print("=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_plant_stats(anon)
