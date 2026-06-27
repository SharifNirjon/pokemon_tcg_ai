"""Parse game logs and compute aggregate statistics."""
import json
from pathlib import Path


def analyze(log_dir="logs/"):
    log_files = list(Path(log_dir).glob("*.json"))
    print(f"Analyzing {len(log_files)} game logs...")
    # TODO: parse logs and compute win rates, average game length, etc.


if __name__ == "__main__":
    analyze()
