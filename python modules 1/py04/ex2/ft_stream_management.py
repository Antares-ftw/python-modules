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
        print(f"[STDERR] Error opening file '"
              f"{filename}': {e}", file=sys.stderr)
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
    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    new_filename = sys.stdin.readline()

    if new_filename.endswith('\n'):
        new_filename = new_filename[:-1]

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
            print(f"[STDERR] Error opening file '"
                  f"{new_filename}': {e}", file=sys.stderr)
            print("Data not saved.")


if __name__ == "__main__":
    recover_and_preserve()
