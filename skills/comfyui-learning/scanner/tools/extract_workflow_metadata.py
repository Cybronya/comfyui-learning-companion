import json
import os
import argparse

from extract_nodes import extract_nodes


def build_metadata(path):

    nodes = extract_nodes(path)

    return {
        "name": os.path.basename(path),
        "file_path": path,
        "nodes": nodes,
        "models": [],
        "category": "unknown",
        "human_review": {
            "verified": False
        }
    }


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--workflow", required=True)
    args = parser.parse_args()

    metadata = build_metadata(args.workflow)

    print(json.dumps(metadata, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
