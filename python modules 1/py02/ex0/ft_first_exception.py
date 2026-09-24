def input_temperature(temp_str):
    return int(temp_str)


def test_temperature():
    print("=== Garden Temperature ===")
    data_1 = "25"
    print(f"Input data is '{data_1}'")

    try:
        temp = input_temperature(data_1)
        print(f"Temperature is now {temp}°C")

    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    data_2 = "abc"
    print(f"Input data is '{data_2}'")

    try:
        temp = input_temperature(data_2)
        print(f"Temperature is now {temp}°C")

    except Exception as e:
        print(f"Caught input_temperature error: {e}")
        print("\n")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
