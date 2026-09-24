import os
import site
import sys


def is_in_virtualenv() -> bool:
    return sys.base_prefix != sys.prefix


def get_venv_path() -> str:
    return sys.prefix


def get_venv_name(path: str) -> str:
    return os.path.basename(path)


def get_package_path() -> str:
    try:
        paths = site.getsitepackages()
        if paths:
            return paths[0]
    except Exception:
        pass
    return os.path.join(
        sys.prefix,
        "lib",
        f"python{sys.version_info.major}.{sys.version_info.minor}",
        "site-packages",
    )


def main() -> None:
    try:
        in_venv = is_in_virtualenv()

        if not in_venv:
            print("MATRIX STATUS: You're still plugged in")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate # On Windows")
            print("Then run this program again.")
        else:
            env_path = get_venv_path()
            venv_name = get_venv_name(env_path)
            print("MATRIX STATUS: Welcome to the construct")
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {env_path}")
            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.")
            print("\nPackage installation path:")
            print(get_package_path())
    except (IOError, OSError) as e:
        print(f"An error occurred while writing "
              f"to standard output: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
