import json
import argparse
import os


def build(folder):

    nodes = []

    for f in os.listdir(folder):

        if f.endswith(".json"):

            with open(
                os.path.join(folder, f),
                encoding="utf-8-sig"
            ) as file:

                nodes.append(
                    json.load(file)
                )

    return {
        "version": "1.0",
        "count": len(nodes),
        "nodes": nodes
    }


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="node_database.json")
    args = parser.parse_args()

    data = build(args.input)

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Node database built: {data['count']} nodes")
