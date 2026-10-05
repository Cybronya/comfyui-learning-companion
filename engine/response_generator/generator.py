from .analyzer import (
    QuestionAnalyzer
)


from .prompt_builder import (
    PromptBuilder
)


from .response_template import (
    DEFAULT_TEMPLATE
)



from .answer_builder import (
    AnswerBuilder
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



        self.answer_builder = (
            AnswerBuilder()
        )



    def generate(
        self,
        question,
        context,
        knowledge=None
    ):


        analysis = (
            self.analyzer
            .analyze(question)
        )



        # retrieval 抽出的知识优先；没有传时才回退到 knowledge_loader 按
        # 问题类型硬编码取卡（KSampler / VAEDecode 两种），覆盖面太窄。
        knowledge_text = (
            knowledge
            if knowledge
            else ""
        )



        # 根据关键词寻找知识

        if self.knowledge_loader:


            if analysis["type"]=="sampler":


                data=self.knowledge_loader.load(
                    "KSampler"
                )


                if data and not knowledge_text:

                    knowledge_text=data.get(
                        "content",
                        ""
                    )



            elif analysis["type"]=="vae":


                data=self.knowledge_loader.load(
                    "VAEDecode"
                )


                if data and not knowledge_text:

                    knowledge_text=data.get(
                        "content",
                        ""
                    )



        prompt=self.builder.build(

            question,

            context,

            knowledge_text

        )



        return {

            "prompt":

            prompt,


            "analysis":

            analysis

        }



    def answer(
        self,
        state
    ):


        """不调 LLM，直接把 AgentState 拼成可读回答。

        与 generate() 的区别：generate() 产出的是「给 LLM 的提示词」，
        适合把本项目当 Agent 框架、后端接自有模型；
        answer() 产出的是「给人看的回答」，全规则拼装，无需 LLM。
        """


        return self.answer_builder.build(

            state

        )
