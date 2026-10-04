from dataclasses import dataclass, field
from typing import Dict, List, Optional



@dataclass
class NodeKnowledge:


    id:int

    node_type:str


    role:str="unknown"


    category:str="unknown"


    difficulty:str="unknown"


    learning_topics:List[str]=field(
        default_factory=list
    )


    explanation:Optional[str]=None


    widgets:List=field(
        default_factory=list
    )


    inputs:Dict=field(
        default_factory=dict
    )



@dataclass
class WorkflowKnowledge:


    workflow_id:str


    task_type:str="unknown"


    nodes:List[NodeKnowledge]=field(
        default_factory=list
    )


    features:List[str]=field(
        default_factory=list
    )


    learning_topics:List[str]=field(
        default_factory=list
    )


    summary:str=""
