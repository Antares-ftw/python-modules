class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self.name}:"
              f"{self._height}cm, {self._age} days old")

    def set_height(self, height):

        if height > 0:
            self._height = height
            print(f"Height updated: {self._height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age):

        if age > 0:
            self._age = age
            print(f"Age updated: {self._age} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self):

        return self._height

    def get_age(self):

        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 15, 10)
    print("\n")
    plant1.set_height(25)
    plant1.set_age(30)
    print("\n")
    plant1.set_height(-25)
    plant1.set_age(-30)
    print("\n")
    print(
        f"\nCurrent state: {plant1.name} {plant1.get_height()}cm, "
        f"{plant1.get_age()} days old"
    )
