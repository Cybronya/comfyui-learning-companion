class TeachingResponseGenerator:


    def __init__(
        self,
        knowledge_loader
    ):

        self.knowledge_loader = (
            knowledge_loader
        )



    def answer(
        self,
        question,
        context
    ):


        node_type = (
            self.find_node(
                question,
                context
            )
        )


        info = (
            self.knowledge_loader.load(
                node_type
            )
            if node_type
            else None
        )


        lines = []


        lines.append(
            "根据你的 workflow:"
        )


        lines.append(
            f"当前: {context.get('current_workflow')}"
        )


        if info:


            lines.append(
                f"发现: {info['node_type']}"
            )


            lines.append(
                f"作用: {info['category']}"
            )


            topics = info.get(
                "learning_topics",
                []
            )


            if topics:

                lines.append(
                    "学习主题: "
                    + ", ".join(topics)
                )


            lines.append(
                f"参考: {info['knowledge_file']}"
            )


        elif node_type:

            lines.append(
                f"发现: {node_type}"
            )


            lines.append(
                "暂无该节点的知识卡"
            )


        else:

            lines.append(
                "未在问题中识别到节点"
            )


        return "\n".join(lines)



    def find_node(
        self,
        question,
        context
    ):


        # 优先用上下文里已识别的话题
        if context.get(
            "active_topic"
        ):

            return context["active_topic"]


        # 否则在问题里匹配当前工作流的节点
        question_lower = (
            question.lower()
        )


        for node_type in context.get(
            "workflow_nodes",
            []
        ):

            if (
                node_type.lower()
                in question_lower
            ):

                return node_type


        return None
