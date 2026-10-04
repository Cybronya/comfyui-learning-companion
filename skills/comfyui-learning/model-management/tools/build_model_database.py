import json
import argparse
import os


def build(folder):

    models = []

    for file in os.listdir(folder):

        if file.endswith(".json"):

            with open(
                os.path.join(folder, file),
                encoding="utf-8-sig"
            ) as f:

                models.append(
                    json.load(f)
                )

    return {
        "version": "1.0",
        "count": len(models),
        "models": models
    }


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    print(
        json.dumps(
            build(args.input),
            indent=2
        )
    )
