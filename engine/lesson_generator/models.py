from dataclasses import dataclass, field

from typing import List



@dataclass
class LessonSection:


    title:str


    content:str



    exercises:List[str]=field(
        default_factory=list
    )




@dataclass
class Lesson:


    title:str


    workflow_type:str


    sections:List[LessonSection]=field(
        default_factory=list
    )


    learning_topics:List[str]=field(
        default_factory=list
    )
