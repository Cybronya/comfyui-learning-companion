import json

from .models import (
    NodeKnowledge,
    WorkflowKnowledge
)



class WorkflowParser:


    def __init__(
        self,
        knowledge_loader,
        context=None
    ):

        self.knowledge_loader = (
            knowledge_loader
        )


        # 可选的 ContextManager：
        # 解析后自动写入 WorkflowContext
        self.context = (
            context
        )



    def parse(
        self,
        filepath
    ):


        with open(
            filepath,
            "r",
            encoding="utf-8"
        ) as f:

            data=json.load(f)



        nodes=[]

        topics=set()



        for node in data.get(
            "nodes",
            []
        ):


            node_type=node[
                "type"
            ]


            info = (
                self.knowledge_loader
                .load(node_type)
            )


            if info:


                topics.update(
                    info.get(
                        "learning_topics",
                        []
                    )
                )


                knowledge = NodeKnowledge(

                    id=node["id"],

                    node_type=node_type,

                    role=
                    info.get(
                        "role",
                        "unknown"
                    ),

                    category=
                    info.get(
                        "category",
                        "unknown"
                    ),

                    difficulty=
                    info.get(
                        "difficulty",
                        "unknown"
                    ),

                    learning_topics=
                    info.get(
                        "learning_topics",
                        []
                    ),

                    explanation=
                    info.get(
                        "content"
                    ),

                    widgets=
                    node.get(
                        "widgets_values",
                        []
                    ),

                    inputs=
                    node.get(
                        "inputs",
                        {}
                    )

                )


            else:


                knowledge = NodeKnowledge(

                    id=node["id"],

                    node_type=node_type,

                    widgets=
                    node.get(
                        "widgets_values",
                        []
                    ),

                    inputs=
                    node.get(
                        "inputs",
                        {}
                    )

                )


            nodes.append(
                knowledge
            )



        workflow = WorkflowKnowledge(

            workflow_id=filepath,

            nodes=nodes,

            # 排序保证输出顺序稳定
            learning_topics=sorted(
                topics
            )

        )


        # 解析后自动写入 WorkflowContext
        if self.context:

            self.context.set_workflow(
                workflow
            )


        return workflow
