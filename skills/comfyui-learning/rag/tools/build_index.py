import json
import argparse


def build_index(documents):

    index = []

    for doc in documents:

        index.append({
            "text": doc["content"],
            "metadata": doc["metadata"]
        })

    return index


if __name__ == "__main__":

    pass
