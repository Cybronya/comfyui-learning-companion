from .analyzer import (
    QuestionAnalyzer
)


from .prompt_builder import (
    PromptBuilder
)


from .response_template import (
    DEFAULT_TEMPLATE
)



class ResponseGenerator:



    def __init__(
        self,
        knowledge_loader=None
    ):


        self.analyzer = (
            QuestionAnalyzer()
        )


        self.builder = (
            PromptBuilder()
        )


        self.knowledge_loader = (
            knowledge_loader
        )



    def generate(
        self,
        question,
        context
    ):


        analysis = (
            self.analyzer
            .analyze(question)
        )



        knowledge=""



        # 根据关键词寻找知识

        if self.knowledge_loader:


            if analysis["type"]=="sampler":


                data=self.knowledge_loader.load(
                    "KSampler"
                )


                if data:

                    knowledge=data.get(
                        "content",
                        ""
                    )



            elif analysis["type"]=="vae":


                data=self.knowledge_loader.load(
                    "VAEDecode"
                )


                if data:

                    knowledge=data.get(
                        "content",
                        ""
                    )



        prompt=self.builder.build(

            question,

            context,

            knowledge

        )



        return {

            "prompt":

            prompt,


            "analysis":

            analysis

        }
