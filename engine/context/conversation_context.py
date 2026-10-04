from dataclasses import dataclass, field

from typing import List



@dataclass
class ConversationContext:


    active_topic:str = ""


    recent_questions:List[str] = field(
        default_factory=list
    )



    max_history:int = 10



    def add_question(
        self,
        question
    ):


        self.recent_questions.append(
            question
        )


        if len(
            self.recent_questions
        ) > self.max_history:


            self.recent_questions.pop(
                0
            )


        return self



    def set_topic(
        self,
        topic
    ):

        self.active_topic = topic



    def summary(self):


        return {


            "active_topic":
            self.active_topic,


            "recent_questions":
            self.recent_questions

        }
