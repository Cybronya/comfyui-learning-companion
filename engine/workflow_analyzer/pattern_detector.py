class PatternDetector:



    def detect(
        self,
        node_types
    ):


        patterns=[]



        if (

        "KSampler" in node_types

        and

        "CLIPTextEncode" in node_types

        and

        "EmptyLatentImage" in node_types

        ):


            patterns.append(
                "text_to_image"
            )



        if (

        "LoadImage" in node_types

        and

        "VAEEncode" in node_types

        and

        "KSampler" in node_types

        ):


            patterns.append(
                "image_to_image"
            )



        if (

        "ControlNetApply" in node_types

        ):


            patterns.append(
                "controlnet"
            )



        if (

        "LoraLoader" in node_types

        ):


            patterns.append(
                "lora"
            )


        return patterns
