import sys


def recover_and_preserve():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, 'r')

        print("---")
        content = f.read()
        print(content, end="")

        if content and not content.endswith('\n'):
            print()

        print("---")
        f.close()
        print(f"File '{filename}' closed.")

    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return
    transformed_content = content.replace('\n', '#\n')

    if content and not content.endswith('\n'):
        transformed_content += '#'

    print("Transform data:")
    print("---")
    print(transformed_content, end="")
    if transformed_content and not transformed_content.endswith('\n'):
        print()
    print("---")

    new_filename = input("Enter new file name (or empty): ")

    if new_filename == "":
        print("Not saving data.")
    else:
        print(f"Saving data to '{new_filename}'")
        try:
            out_f = open(new_filename, 'w')
            out_f.write(transformed_content)
            out_f.close()
            print(f"Data saved in file '{new_filename}'.")
        except Exception as e:
            print(f"Error saving to file '{new_filename}': {e}")


if __name__ == "__main__":
    recover_and_preserve()
