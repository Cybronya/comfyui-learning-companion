import os
import json
import argparse


EXTENSIONS = [
    ".safetensors",
    ".ckpt",
    ".pt",
    ".pth"
]


def scan(root):

    result = []

    for path, dirs, files in os.walk(root):

        for file in files:

            ext = os.path.splitext(file)[1]

            if ext in EXTENSIONS:

                full = os.path.join(path, file)

                result.append({
                    "name": file,
                    "path": full,
                    "size": os.path.getsize(full)
                })

    return result


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="models.json")
    args = parser.parse_args()

    data = scan(args.input)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Found {len(data)} model files")
