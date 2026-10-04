import os
import json
import argparse


def build_manifest(folder):

    workflows = []

    for file in os.listdir(folder):

        if file.endswith(".json"):

            path = os.path.join(folder, file)

            with open(path, encoding="utf-8-sig") as f:
                workflows.append(json.load(f))

    return {
        "version": "1.0",
        "count": len(workflows),
        "workflows": workflows
    }


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="workflow_manifest.json")
    args = parser.parse_args()

    data = build_manifest(args.input)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Manifest built: {data['count']} workflows")


if __name__ == "__main__":
    main()
