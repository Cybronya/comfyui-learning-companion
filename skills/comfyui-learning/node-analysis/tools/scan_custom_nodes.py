import os
import json
import argparse


def scan_nodes(root):

    result = []

    for path, dirs, files in os.walk(root):

        for file in files:

            if file.endswith(".py"):

                result.append({
                    "file": file,
                    "path": os.path.join(path, file)
                })

    return result


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="nodes.json")
    args = parser.parse_args()

    data = scan_nodes(args.input)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Found {len(data)} python files")


if __name__ == "__main__":
    main()
