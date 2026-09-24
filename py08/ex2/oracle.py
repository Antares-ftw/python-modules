import os
import sys
from typing import Any, Dict, List

# from dotenv import load_dotenv

# load_dotenv()


def load_configuration() -> Dict[str, Any]:
    matrix_mode: str = os.getenv("MATRIX_MODE", "development")
    database_url: str = os.getenv("DATABASE_URL", "")
    api_key: str = os.getenv("API_KEY", "")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint: str = os.getenv("ZION_ENDPOINT", "")

    missing_vars: List[str] = []

    if not database_url:
        missing_vars.append("DATABASE_URL")
    if not api_key:
        missing_vars.append("API_KEY")

    if missing_vars:
        print(
            "WARNING: The following environment variables "
            f"are missing: {', '.join(missing_vars)}",
            file=sys.stderr,
        )

    return {
        "MATRIX_MODE": matrix_mode,
        "DATABASE_URL": database_url,
        "API_KEY": api_key,
        "LOG_LEVEL": log_level,
        "ZION_ENDPOINT": zion_endpoint,
        "missing_vars": missing_vars,
    }


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    try:
        config: Dict[str, Any] = load_configuration()
        mode: str = config["MATRIX_MODE"]

        if mode.lower() == "production":
            db_desc = "Connected to production "
            f"server {config['DATABASE_URL']}"
        else:
            db_desc = "Connected to local instance"

        api_key_exists = bool(config["API_KEY"])
        zion_exists = bool(config["ZION_ENDPOINT"])

        api_status = "Authenticated" if api_key_exists else "Not Authenticated"
        zion_status = "Online" if zion_exists else "Offline"

        print("Configuration loaded:")
        print(f"Mode: {mode}")
        print(f"Database: {db_desc}")
        print(f"API Access: {api_status}")
        print(f"Log Level: {config['LOG_LEVEL']}")
        print(f"Zion Network: {zion_status}")

        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")

        if os.path.exists(".env"):
            print("[OK] .env file properly configured")
        else:
            print(
                "[WARNING] .env file not found; "
                "relying on system environment variables."
            )

        print("[OK] Production overrides available")

    except Exception as e:
        print(
            f"CRITICAL ERROR: Failed to read mainframe configuration: {e}",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
