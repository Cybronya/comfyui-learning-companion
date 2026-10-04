import json
import argparse


def load_json(path):

    with open(path, encoding="utf-8-sig") as f:

        return json.load(f)


def create_documents(data_type, data):

    docs = []

    for item in data:

        docs.append({
            "type": data_type,
            "content": str(item),
            "metadata": item
        })

    return docs


if __name__ == "__main__":

    pass
