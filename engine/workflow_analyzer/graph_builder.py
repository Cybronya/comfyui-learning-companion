from dataclasses import dataclass, field

from typing import Dict, List



@dataclass
class WorkflowNode:


    id:int


    node_type:str


    inputs:Dict = field(
        default_factory=dict
    )


    outputs:Dict = field(
        default_factory=dict
    )



@dataclass
class WorkflowEdge:


    source:int


    target:int


    data_type:str=""



@dataclass
class WorkflowGraph:


    nodes:Dict[int,WorkflowNode]=field(
        default_factory=dict
    )


    edges:List[WorkflowEdge]=field(
        default_factory=list
    )



class GraphBuilder:



    def build(
        self,
        workflow_json
    ):


        graph=WorkflowGraph()



        for node in workflow_json.get(
            "nodes",
            []
        ):


            graph.nodes[node["id"]] = WorkflowNode(

                id=node["id"],

                node_type=node["type"],

                inputs=node.get(
                    "inputs",
                    {}
                )

            )



        for link in workflow_json.get(
            "links",
            []
        ):


            edge=WorkflowEdge(

                source=link[1],

                target=link[3],

                data_type=link[5]

            )


            graph.edges.append(
                edge
            )


        return graph
