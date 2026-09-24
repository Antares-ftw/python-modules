import sys


def command_quest():
    program_name = sys.argv[0]
    arguments = sys.argv[1:]
    arg_count = len(arguments)
    total_count = len(sys.argv)

    print("=== Command Quest ===")
    print(f"Program name: {program_name}")

    if arg_count == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arg_count}")
        for i, arg in enumerate(arguments, 1):
            print(f"Argument {i}: {arg}")

    print(f"Total arguments: {total_count}")


if __name__ == "__main__":
    command_quest()
