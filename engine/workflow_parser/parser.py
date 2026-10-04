import json

from .models import (
    NodeKnowledge,
    WorkflowKnowledge
)

from .knowledge_loader import (
    NodeKnowledgeLoader
)


class WorkflowParser:


    def __init__(
        self,
        knowledge_path=None
    ):

        self.knowledge_loader = (
            NodeKnowledgeLoader(
                knowledge_path
            )
            if knowledge_path
            else None
        )


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


            knowledge = (
                self.knowledge_loader.load(
                    node["type"]
                )
                if self.knowledge_loader
                else None
            )


            nodes.append(
                NodeKnowledge(
                    id=node["id"],
                    node_type=node["type"],
                    role=knowledge.get(
                        "role",
                        "unknown"
                    )
                    if knowledge
                    else "unknown",
                    category=knowledge.get(
                        "category",
                        "unknown"
                    )
                    if knowledge
                    else "unknown",
                    learning_topics=knowledge.get(
                        "learning_topics",
                        []
                    )
                    if knowledge
                    else [],
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
