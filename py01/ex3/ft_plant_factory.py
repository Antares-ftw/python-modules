class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Oak", 200, 365)
    plant3 = Plant("Cactus", 5, 90)
    plant4 = Plant("Sunflowe", 80, 45)
    plant5 = Plant("Fern", 15, 120)

    print("=== Plant Factory Output ===")
    print(f"Created: {plant1.name}: {plant1.height}cm, {plant1.age} days old")
    print(f"Created: {plant2.name}: {plant2.height}cm, {plant2.age} days old")
    print(f"Created: {plant3.name}: {plant3.height}cm, {plant3.age} days old")
    print(f"Created: {plant4.name}: {plant4.height}cm, {plant4.age} days old")
    print(f"Created: {plant5.name}: {plant5.height}cm, {plant5.age} days old")
