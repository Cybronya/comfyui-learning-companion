from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class NodeKnowledge:
    id: int
    node_type: str
    role: str = "unknown"
    inputs: Dict = field(default_factory=dict)


@dataclass
class WorkflowKnowledge:
    workflow_id: str

    task_type: str = "unknown"

    nodes: List[NodeKnowledge] = field(
        default_factory=list
    )

    features: List[str] = field(
        default_factory=list
    )
