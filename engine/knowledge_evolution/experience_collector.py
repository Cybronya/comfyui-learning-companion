"""
经验收集器

把 learning_loop 产出的 LearningExperience（孤立、带改动记录的经验）
转换成 knowledge_evolution 需要的 WorkflowExperience（带完整节点清单的经验）。

为什么需要转换：
    learning_loop 记录的是「一次改动」，只存了发生变化的节点（added:KSampler 形式），
    没有工作流的完整节点清单。而挖模式需要知道「这个工作流由哪些节点组成」，
    所以这里把节点清单单独补上，再把参数从 parameter_changes 的 new 侧抽出来。
"""

from typing import List, Dict, Optional, Iterable, Any

from .models import WorkflowExperience


class ExperienceCollector:
    """
    收集并归一化工作流经验
    """

    def __init__(self) -> None:
        """
        初始化收集器
        """
        self.experiences: List[WorkflowExperience] = []
        # workflow_type -> 该类型工作流的已知节点清单
        self.node_registry: Dict[str, List[str]] = {}

    def add(self, experience: Any) -> WorkflowExperience:
        """
        添加一条经验

        Args:
            experience: WorkflowExperience 或其字典形式

        Returns:
            归一化后的 WorkflowExperience
        """
        if isinstance(experience, dict):
            experience = WorkflowExperience.from_dict(experience)

        # 节点清单为空时，尝试从登记表补全
        if not experience.nodes and experience.workflow_type in self.node_registry:
            experience.nodes = list(self.node_registry[experience.workflow_type])

        self.experiences.append(experience)
        return experience

    def register_nodes(self, workflow_type: str, nodes: List[str]) -> None:
        """
        登记某类工作流的节点清单

        mining_loop 那边只记了「哪个节点被改动过」，这里补上「工作流原本有哪些节点」，
        否则 PatternMiner 只能看到残缺的节点集合。

        Args:
            workflow_type: 工作流类型
            nodes: 完整节点清单
        """
        self.node_registry[workflow_type] = list(nodes)

    def from_learning_experience(
        self,
        learning_experience: Any,
        nodes: Optional[List[str]] = None
    ) -> WorkflowExperience:
        """
        从 learning_loop.LearningExperience 转换

        Args:
            learning_experience: LearningExperience 对象或字典
            nodes: 该工作流的完整节点清单（可选）

        Returns:
            WorkflowExperience
        """
        if isinstance(learning_experience, dict):
            change = learning_experience.get("change", {})
            workflow_type = learning_experience.get("workflow_type", "")
            observation = learning_experience.get("observation", "")
            tags = learning_experience.get("tags", [])
            timestamp = learning_experience.get("timestamp", "")
            result = learning_experience.get("result", "")
        else:
            change = {
                "changed_nodes": learning_experience.change.changed_nodes,
                "parameter_changes": learning_experience.change.parameter_changes,
            }
            workflow_type = learning_experience.workflow_type
            observation = learning_experience.observation
            tags = learning_experience.tags
            timestamp = learning_experience.timestamp
            result = getattr(learning_experience, "result", "")

        changed_nodes = change.get("changed_nodes", [])
        parameter_changes = change.get("parameter_changes", {})

        # 参数取 new 侧：那是改动后工作流实际在用的值
        parameters = {
            key: value.get("new")
            for key, value in parameter_changes.items()
            if isinstance(value, dict) and "new" in value
        }

        return self.add(
            WorkflowExperience(
                workflow_type=workflow_type,
                nodes=list(nodes) if nodes else [],
                changes={
                    "changed_nodes": list(changed_nodes),
                    "parameter_changes": dict(parameter_changes),
                },
                parameters=parameters,
                result=result,
                observation=observation,
                tags=list(tags),
                timestamp=timestamp,
            )
        )

    def get_all(self) -> List[WorkflowExperience]:
        """
        获取所有收集到的经验
        """
        return list(self.experiences)

    def get_by_type(self, workflow_type: str) -> List[WorkflowExperience]:
        """
        按工作流类型过滤
        """
        return [
            exp for exp in self.experiences
            if exp.workflow_type == workflow_type
        ]

    def load_from_store(self, path: str) -> int:
        """
        从 learning_loop 的 experience_store.json 读取原始数据

        只读取不转换 —— 原始数据缺节点清单，转换需要配合 register_nodes 使用，
        否则挖出来的模式会是一堆残缺节点组合。

        Args:
            path: experience_store.json 路径

        Returns:
            读到的记录条数
        """
        import json
        from pathlib import Path

        store_path = Path(path)
        if not store_path.exists():
            return 0

        try:
            with open(store_path, "r", encoding="utf-8-sig") as f:
                raw = json.load(f)
        except Exception as e:
            print(f"读取经验存储失败: {e}")
            return 0

        for item in raw:
            self.from_learning_experience(item)

        return len(raw)

    def clear(self) -> None:
        """
        清空已收集的经验
        """
        self.experiences = []
