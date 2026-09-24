def input_temperature(temp_str):
    temp = int(temp_str)

    if temp < 0:
        raise Exception(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise Exception(f"{temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature():
    print("=== Garden Temperature Checker ===")

    test_cases = ["25", "abc", "100", "-50"]

    for data in test_cases:
        print(f"Input data is '{data}'")
        try:
            temp = input_temperature(data)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
