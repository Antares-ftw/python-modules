def secure_archive(filename: str, mode: str = 'r',
                   content: str = "") -> tuple[bool, str]:

    try:
        if mode == 'r':
            with open(filename, 'r') as f:
                data = f.read()
                return (True, data)

        elif mode == 'w':
            with open(filename, 'w') as f:
                f.write(content)
                return (True, "Content successfully written to file")

        else:
            return (False, f"Unsupported mode: {mode}")

    except Exception as e:
        return (False, str(e))


def main():
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive('/not/existing/file'))
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive('/etc/master.passwd'))

    dummy_name = "ancient_fragment.txt"
    dummy_content = (
        "[FRAGMENT 001] Digital preservation protocols established 2087\n"
        "[FRAGMENT 002] Knowledge must survive the entropy wars\n"
        "[FRAGMENT 003] Every byte saved is a victory against oblivion\n"
    )

    with open(dummy_name, 'w') as f:
        f.write(dummy_content)

    print("\nUsing 'secure_archive' to read from a regular file:")
    success, result = secure_archive(dummy_name)
    print((success, result))
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("vault_backup.txt", 'w', result))


if __name__ == "__main__":
    main()
