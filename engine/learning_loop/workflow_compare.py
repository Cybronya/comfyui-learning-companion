"""
Workflow 比较器

比较两个 Workflow 的差异，识别节点变化和参数变化
"""

from typing import Dict, List
from .models import WorkflowSnapshot


class WorkflowComparator:
    """
    工作流比较器
    """

    def compare(
        self,
        old: WorkflowSnapshot,
        new: WorkflowSnapshot
    ) -> Dict:
        """
        比较两个工作流

        Args:
            old: 旧工作流快照
            new: 新工作流快照

        Returns:
            比较结果，包含：
            - nodes_changed: 发生变化的节点列表
            - parameters: 参数变化详情
        """
        result = {
            "nodes_changed": [],
            "parameters": {}
        }

        # 转换为集合进行比较
        old_nodes = set(old.nodes)
        new_nodes = set(new.nodes)

        # 检测节点变化
        if old_nodes != new_nodes:
            # 新增的节点（在 new 中但在 old 中不存在）
            added_nodes = new_nodes - old_nodes
            # 删除的节点（在 old 中但在 new 中不存在）
            removed_nodes = old_nodes - new_nodes

            if added_nodes:
                result["nodes_changed"].extend([f"added:{node}" for node in added_nodes])
            if removed_nodes:
                result["nodes_changed"].extend([f"removed:{node}" for node in removed_nodes])

        # 检测参数变化
        keys = set(old.parameters.keys()).union(set(new.parameters.keys()))

        for key in keys:
            old_value = old.parameters.get(key)
            new_value = new.parameters.get(key)

            # 只有当值不同时才记录
            if old_value != new_value:
                result["parameters"][key] = {
                    "old": old_value,
                    "new": new_value
                }

        return result

    def compare_dicts(
        self,
        old: Dict,
        new: Dict
    ) -> Dict:
        """
        比较两个字典（简化版本，不使用 WorkflowSnapshot）

        Args:
            old: 旧参数字典
            new: 新参数字典

        Returns:
            比较结果
        """
        result = {
            "nodes_changed": [],
            "parameters": {}
        }

        # 假设 nodes 存在
        if "nodes" in old and "nodes" in new:
            old_nodes = set(old["nodes"])
            new_nodes = set(new["nodes"])

            if old_nodes != new_nodes:
                added_nodes = new_nodes - old_nodes
                removed_nodes = old_nodes - new_nodes

                if added_nodes:
                    result["nodes_changed"].extend([f"added:{node}" for node in added_nodes])
                if removed_nodes:
                    result["nodes_changed"].extend([f"removed:{node}" for node in removed_nodes])

        # 检测参数变化
        keys = set(old.keys()).union(set(new.keys()))

        for key in keys:
            old_value = old.get(key)
            new_value = new.get(key)

            if old_value != new_value:
                result["parameters"][key] = {
                    "old": old_value,
                    "new": new_value
                }

        return result
