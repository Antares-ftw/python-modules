import sys


def recover_fragment():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
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


if __name__ == "__main__":
    recover_fragment()
