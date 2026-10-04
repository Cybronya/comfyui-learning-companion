class WorkflowClassifier:



    def classify(
        self,
        patterns
    ):


        if "text_to_image" in patterns:

            return "Text To Image"



        if "image_to_image" in patterns:

            return "Image To Image"



        return "Unknown Workflow"
