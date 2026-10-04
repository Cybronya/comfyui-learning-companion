from dataclasses import dataclass, field

from typing import Dict, List



@dataclass
class WorkflowContext:


    workflow_id:str = ""


    task_type:str = ""


    nodes:List[str] = field(
        default_factory=list
    )


    parameters:Dict = field(
        default_factory=dict
    )


    features:List[str] = field(
        default_factory=list
    )



    def update_from_workflow(
        self,
        workflow
    ):


        self.workflow_id = (
            workflow.workflow_id
        )


        self.task_type = (
            workflow.task_type
        )


        self.nodes = [

            node.node_type

            for node in workflow.nodes

        ]


        self.features = (
            workflow.features
        )



        return self



    def contains_node(
        self,
        node_type
    ):


        return node_type in self.nodes



    def summary(self):


        return {

            "workflow":
            self.workflow_id,


            "task_type":
            self.task_type,


            "nodes":
            self.nodes,


            "features":
            self.features

        }
