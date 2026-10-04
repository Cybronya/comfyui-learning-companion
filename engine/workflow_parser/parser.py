import json

from .models import (
    NodeKnowledge,
    WorkflowKnowledge
)


class WorkflowParser:


    def parse(self, filepath):

        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:
            data=json.load(f)


        nodes=[]


        for node in data.get(
            "nodes",
            []
        ):

            nodes.append(
                NodeKnowledge(
                    id=node["id"],
                    node_type=node["type"],
                    inputs=node.get(
                        "inputs",
                        {}
                    )
                )
            )


        return WorkflowKnowledge(
            workflow_id=filepath,
            nodes=nodes
        )
