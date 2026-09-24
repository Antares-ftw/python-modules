class GardenError(Exception):
    def __init__(self, message="A general garden error occurred"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown watering error"):
        super().__init__(message)


def check_garden_status(issue_type):
    if issue_type == "wilt":
        raise PlantError("The tomato plant is wilting!")
    elif issue_type == "dry":
        raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")
    try:
        check_garden_status("wilt")
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")
    try:
        check_garden_status("dry")
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing catching all garden errors...")
    issues = ["wilt", "dry"]
    for issue in issues:
        try:
            check_garden_status(issue)
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
