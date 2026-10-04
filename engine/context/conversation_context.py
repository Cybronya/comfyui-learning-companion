class ConversationContext:


    MAX_QUESTIONS = 5


    def update_question(
        self,
        store,
        question,
        known_node_types
    ):


        recent = (
            store.get(
                "recent_questions",
                []
            )
            + [question]
        )


        store["recent_questions"] = (
            recent[
                -self.MAX_QUESTIONS:
            ]
        )


        # 从问题里识别正在讨论的节点主题
        topic = (
            self.detect_topic(
                question,
                known_node_types
            )
        )


        if topic:

            store["active_topic"] = topic



    def detect_topic(
        self,
        question,
        known_node_types
    ):


        question_lower = (
            question.lower()
        )


        for node_type in known_node_types:

            if (
                node_type.lower()
                in question_lower
            ):

                return node_type


        return None
