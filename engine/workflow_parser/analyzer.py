class WorkflowAnalyzer:


    def analyze(
        self,
        workflow
    ):


        node_types=[
            n.node_type
            for n in workflow.nodes
        ]



        # Text To Image

        if (

            "KSampler"
            in node_types

            and

            "CLIPTextEncode"
            in node_types

            and

            "EmptyLatentImage"
            in node_types

        ):

            workflow.task_type = (
                "text_to_image"
            )



        # Image Input

        if (
            "LoadImage"
            in node_types
        ):

            workflow.features.append(
                "image_input"
            )



        workflow.summary = (

            f"This workflow is "
            f"{workflow.task_type} "
            f"pipeline with "
            f"{len(workflow.nodes)} nodes."

        )


        return workflow
