from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class WorkflowObject:
    """
    Parsed ComfyUI Workflow
    """

    id: str

    path: str

    nodes: List[Dict[str, Any]] = field(
        default_factory=list
    )

    links: List[Any] = field(
        default_factory=list
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )


@dataclass
class AnalysisResult:
    """
    Workflow analysis result
    """

    workflow_id: str

    nodes: List[Dict[str, Any]] = field(
        default_factory=list
    )

    models: List[str] = field(
        default_factory=list
    )

    pipeline: str = ""

    patterns: List[str] = field(
        default_factory=list
    )


@dataclass
class KnowledgeObject:
    """
    Generated knowledge object
    """

    type: str

    name: str

    content: str

    tags: List[str] = field(
        default_factory=list
    )
