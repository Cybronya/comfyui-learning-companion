import json
import argparse


def extract_nodes(path):

    with open(path, "r", encoding="utf-8-sig") as f:
        data = json.load(f)

    nodes = []

    for node_id, node in data.items():

        if isinstance(node, dict):

            node_type = (
                node.get("class_type")
                or
                node.get("type")
            )

            if node_type:
                nodes.append(node_type)

    return {
        "node_count": len(nodes),
        "node_types": list(set(nodes))
    }


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--workflow", required=True)
    args = parser.parse_args()

    result = extract_nodes(args.workflow)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
