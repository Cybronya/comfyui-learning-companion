import os
import json
import argparse


SUPPORTED = [
    ".json",
    ".yaml",
    ".yml"
]


def scan_directory(root):

    results = []

    for path, dirs, files in os.walk(root):

        for file in files:

            ext = os.path.splitext(file)[1]

            if ext.lower() in SUPPORTED:

                full = os.path.join(path, file)

                results.append({
                    "name": file,
                    "path": full,
                    "size": os.path.getsize(full),
                    "extension": ext
                })

    return results


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="workflow_files.json")
    args = parser.parse_args()

    data = scan_directory(args.input)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Found {len(data)} workflows")


if __name__ == "__main__":
    main()
