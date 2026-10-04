import json

from pathlib import Path

from .workflow_context import (
    WorkflowContext
)

from .conversation_context import (
    ConversationContext
)



class ContextManager:



    def __init__(
        self,
        store_path,
        known_node_types=None
    ):

        self.store_path = Path(
            store_path
        )


        self.workflow = WorkflowContext()

        self.conversation = ConversationContext()


        self.known_node_types = (
            known_node_types
            or []
        )


        self.load()



    def load(self):


        if (
            self.store_path.exists()
        ):

            with open(
                self.store_path,
                "r",
                encoding="utf-8"
            ) as f:

                self.store = json.load(f)

        else:

            self.store = (
                self.default_store()
            )



    def default_store(self):

        return {

            "user_id": "default",

            "current_workflow": None,

            "workflow_nodes": [],

            "workflow_parameters": {},

            "active_topic": None,

            "recent_questions": []

        }



    def set_workflow(
        self,
        workflow_knowledge
    ):


        self.workflow.set_workflow(
            self.store,
            workflow_knowledge
        )


        self.save()



    def update_question(
        self,
        question
    ):


        self.conversation.update_question(
            self.store,
            question,
            self.known_node_types
            or self.store.get(
                "workflow_nodes",
                []
            )
        )


        self.save()



    def get_context(self):


        return {

            "current_workflow":
                self.store.get(
                    "current_workflow"
                ),

            "workflow_nodes":
                self.store.get(
                    "workflow_nodes",
                    []
                ),

            "workflow_parameters":
                self.store.get(
                    "workflow_parameters",
                    {}
                ),

            "active_topic":
                self.store.get(
                    "active_topic"
                ),

            "recent_questions":
                self.store.get(
                    "recent_questions",
                    []
                )

        }



    def clear(self):


        self.store = (
            self.default_store()
        )


        self.save()



    def save(self):


        with open(
            self.store_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.store,
                f,
                ensure_ascii=False,
                indent=4
            )
