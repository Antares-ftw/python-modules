import importlib
import importlib.metadata
import sys
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def check_dependencies() -> Tuple[bool, Dict[str, str]]:
    packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }

    versions = {}
    missing = False

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for pkg, desc in packages.items():
        try:
            mod = importlib.import_module(pkg)
            ver = getattr(mod, "__version__", None)
            if ver is None:
                try:
                    ver = importlib.metadata.version(pkg)
                except Exception:
                    ver = "Unknown"
            versions[pkg] = ver
            print(f"[OK] {pkg} ({ver}) - {desc}")
        except ImportError:
            print(f"[FAIL] {pkg} - Not installed")
            missing = True

    return not missing, versions


def compare_environments(versions: Dict[str, str]) -> None:
    print("\n--- Pip vs Poetry Dependency Management ---")
    print("Pip (requirements.txt):")
    print("  - Installs packages globally or in the active virtual env.")
    print("  - Requires manual tracking of dependencies and versions.")
    print("Poetry (pyproject.toml):")
    print(
        "  - Manages an isolated virtual environment "
        "and its dependencies automatically."
    )
    print("  - Uses poetry.lock to ensure reproducible builds.")
    print("\nInstalled package versions:")
    for pkg, ver in versions.items():
        print(f"  - {pkg}: {ver}")
    print("-------------------------------------------\n")


def main() -> None:
    success, versions = check_dependencies()

    if not success:
        print("\nPlease install the missing dependencies before running.")
        print("Using pip:    pip install -r requirements.txt")
        print("Using Poetry: poetry install")
        sys.exit(1)

    compare_environments(versions)

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    data = np.random.randn(1000, 2)
    df = pd.DataFrame(data, columns=["NodeX", "NodeY"])

    print("Generating visualization...")
    plt.figure(figsize=(8, 6))
    plt.scatter(df["NodeX"], df["NodeY"], c=df["NodeX"],
                cmap="plasma", alpha=0.6)
    plt.title("Matrix Data Analysis")
    plt.xlabel("Node X")
    plt.ylabel("Node Y")
    plt.colorbar(label="Intensity")

    output_file = "matrix_analysis.png"
    plt.savefig(output_file)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()
