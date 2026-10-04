import ast
import json
import argparse


def analyze_file(path):

    result = []

    with open(path, encoding="utf-8-sig") as f:

        tree = ast.parse(f.read())

    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):

            result.append({
                "class": node.name
            })

    return result


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    print(
        json.dumps(
            analyze_file(args.file),
            indent=2
        )
    )
