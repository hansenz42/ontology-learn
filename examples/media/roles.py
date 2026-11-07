"""查询林青（p01）的作品署名，可按角色筛选。"""

import argparse
import csv
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("role", nargs="?", help="只显示指定角色，例如导演")
    args = parser.parse_args()

    with Path(__file__).with_name("participations.csv").open(encoding="utf-8", newline="") as source:
        for row in csv.DictReader(source):
            if row["person_id"] == "p01" and (args.role is None or row["role"] == args.role):
                print("｜".join([row["person"], row["work"], row["role"]]))


if __name__ == "__main__":
    main()
