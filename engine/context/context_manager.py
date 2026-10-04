import json

from datetime import datetime

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
        store_path
    ):


        self.store_path = Path(
            store_path
        )


        self.workflow_context = (
            WorkflowContext()
        )


        self.conversation_context = (
            ConversationContext()
        )


        self.load()



    def load(self):


        if not self.store_path.exists():

            return



        with open(
            self.store_path,
            "r",
            encoding="utf-8"
        ) as f:


            data=json.load(f)



        current_workflow = (
            data.get(
                "current_workflow",
                {}
            )
        )



        self.workflow_context.workflow_id=(

            current_workflow.get(
                "workflow",
                ""
            )

        )



        self.workflow_context.task_type=(

            current_workflow.get(
                "task_type",
                ""
            )

        )



        self.workflow_context.features=(

            current_workflow.get(
                "features",
                []
            )

        )



        self.workflow_context.nodes=(

            data.get(
                "workflow_nodes",
                []
            )

        )



        self.workflow_context.parameters=(

            data.get(
                "workflow_parameters",
                {}
            )

        )



        self.conversation_context.active_topic=(

            data.get(
                "active_topic",
                ""
            )

        )



        self.conversation_context.recent_questions=(

            data.get(
                "recent_questions",
                []
            )

        )



    def save(self):


        data={


            "user_id":
            "default",


            "current_workflow":

            self.workflow_context.summary(),



            "workflow_nodes":

            self.workflow_context.nodes,



            "workflow_parameters":

            self.workflow_context.parameters,



            "active_topic":

            self.conversation_context.active_topic,



            "recent_questions":

            self.conversation_context.recent_questions,



            "last_update":

            datetime.now().isoformat(
                timespec="seconds"
            )

        }



        with open(
            self.store_path,
            "w",
            encoding="utf-8"
        ) as f:


            json.dump(

                data,

                f,

                indent=4,

                ensure_ascii=False

            )



    def set_workflow(
        self,
        workflow
    ):


        self.workflow_context.update_from_workflow(
            workflow
        )


        self.save()



    def update_question(
        self,
        question,
        topic=""
    ):


        self.conversation_context.add_question(
            question
        )


        if topic:


            self.conversation_context.set_topic(
                topic
            )


        self.save()



    def get_context(self):


        return {


            "workflow":

            self.workflow_context.summary(),



            "conversation":

            self.conversation_context.summary()

        }



    def clear(self):


        self.workflow_context = (
            WorkflowContext()
        )


        self.conversation_context = (
            ConversationContext()
        )


        self.save()
