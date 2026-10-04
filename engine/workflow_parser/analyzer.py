class WorkflowAnalyzer:


    def analyze(
        self,
        knowledge
    ):


        types=[
            n.node_type
            for n in knowledge.nodes
        ]


        if (
            "KSampler" in types
            and
            "CLIPTextEncode" in types
        ):

            knowledge.task_type = (
                "text_to_image"
            )


        if (
            "LoadImage" in types
        ):

            knowledge.features.append(
                "image_input"
            )


        return knowledge
