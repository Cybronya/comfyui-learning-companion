r"""
comfyui_library/database —— Workflow 学习数据库（长期知识存储底座）

定位边界：
- engine/ 负责「怎么学」（解析 / 分析 / 检索 / 归纳等学习与推理）；
- 本包负责「学到了什么」—— 保存学习产物并提供统一查询接口。

最简用法：

    from comfyui_library.database import WorkflowDatabase, WorkflowRecord

    db = WorkflowDatabase()                  # 默认本包 storage/workflow_database.json
    db.workflows.add(WorkflowRecord(...))    # 节点反向索引自动对账
    db.nodes.register("KSampler", wid, category="sampling")
    db.patterns.add("sdxl-portrait", [wid])
    db.experiences.add(wid, "cfg 降到 8 出图更稳", tags=["cfg"])
    db.indexes.save_all()                    # 三个派生索引落盘
"""

from .database import WorkflowDatabase
from .workflow_repository import WorkflowRepository
from .node_repository import NodeRepository
from .pattern_repository import PatternRepository
from .experience_repository import ExperienceRepository
from .index_manager import IndexManager
from .models import (
    ExperienceRecord,
    NodeRecord,
    PatternRecord,
    WorkflowRecord,
)

__all__ = [
    "WorkflowDatabase",
    "WorkflowRepository",
    "NodeRepository",
    "PatternRepository",
    "ExperienceRepository",
    "IndexManager",
    "WorkflowRecord",
    "NodeRecord",
    "PatternRecord",
    "ExperienceRecord",
]
