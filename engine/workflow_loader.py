import json
import os

from .models import WorkflowObject


class WorkflowLoader:

    def load(self, path: str) -> WorkflowObject:

        if not os.path.exists(path):
            raise FileNotFoundError(path)

        with open(
            path,
            "r",
            encoding="utf-8-sig"
        ) as f:

            data = json.load(f)

        workflow_id = os.path.splitext(
            os.path.basename(path)
        )[0]

        return WorkflowObject(
            id=workflow_id,
            path=path,
            nodes=data.get("nodes", []),
            links=data.get("links", []),
            metadata=data.get("extra", {})
        )
