class PromptBuilder:



    def build(
        self,
        question,
        context,
        knowledge=""
    ):


        workflow = context.get(
            "workflow",
            {}
        )


        conversation=context.get(
            "conversation",
            {}
        )



        prompt=f"""

你是 ComfyUI Learning Companion。


用户问题:

{question}


当前 Workflow:

{workflow}


最近讨论:

{conversation}


相关知识:

{knowledge}


请：

1. 解释原因

2. 联系当前workflow

3. 给出具体调整建议

4. 保持教学风格


"""


        return prompt
