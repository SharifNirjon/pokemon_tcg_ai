"""Parse raw game logs into a structured format."""
import json
from pathlib import Path


def parse(log_dir="logs/", out_path="logs/parsed.json"):
    records = []
    for path in Path(log_dir).glob("*.log"):
        with open(path) as f:
            # TODO: implement log parsing
            pass
    with open(out_path, "w") as f:
        json.dump(records, f, indent=2)
    print(f"Wrote {len(records)} records to {out_path}")


if __name__ == "__main__":
    parse()
