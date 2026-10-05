r"""
数据模型 —— 数据库中四类对象的定义

这里是「学到了什么」的词汇表：
- WorkflowRecord 是写入口（WorkflowRepository.add 收它）；
- NodeRecord / PatternRecord / ExperienceRecord 描述各自仓库里
  的存储形状（仓库方法收原始参数，模型作统一参照）。

只描述数据，不含任何学习逻辑 —— 学习在 engine/ 里做。
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class WorkflowRecord:
    """一个 workflow 的学习状态记录"""

    id: str
    name: str
    file_path: str
    status: str = "unlearned"        # unlearned / learned / failed / skipped / stale
    workflow_type: str = ""
    nodes: List[str] = field(default_factory=list)
    patterns: List[str] = field(default_factory=list)
    report: str = ""
    # 文件内容指纹。调度器判断「要不要重学」必需：
    # 只看 status 的话，改了参数永远不算新内容（踩过的坑）
    content_hash: str = ""


@dataclass
class NodeRecord:
    """一个节点类型的使用情况"""

    name: str
    category: str = ""
    used_in: List[str] = field(default_factory=list)


@dataclass
class PatternRecord:
    """一个模式覆盖哪些 workflow"""

    name: str
    workflows: List[str] = field(default_factory=list)
    description: str = ""


@dataclass
class ExperienceRecord:
    """一条学习经验（按 workflow 存，同 id 新覆盖旧）"""

    workflow_id: str
    content: str
    tags: List[str] = field(default_factory=list)
    # 结构化载荷（如 LearningRecord.to_dict()）。
    # 归纳引擎要的是结构化字段（parameters / problems / nodes），
    # content 只是给人看的一段摘要
    data: Dict = field(default_factory=dict)
