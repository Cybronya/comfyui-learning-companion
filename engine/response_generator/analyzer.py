class QuestionAnalyzer:



    def analyze(
        self,
        question
    ):


        result = {


            "type":
            "general",


            "keywords":[]

        }



        keywords=[

            "为什么",

            "错误",

            "失败",

            "模糊",

            "参数",

            "怎么",

            "如何"

        ]



        for k in keywords:


            if k in question:

                result["keywords"].append(
                    k
                )



        if (
            "KSampler" in question
            or
            "steps" in question
            or
            "cfg" in question
        ):


            result["type"]="sampler"



        elif "VAE" in question:


            result["type"]="vae"



        elif "模型" in question:


            result["type"]="model"



        return result
