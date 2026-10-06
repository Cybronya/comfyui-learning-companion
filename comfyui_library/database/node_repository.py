r"""
Node 仓库 —— 节点类型 → 哪些 workflow 在用它

设计稿的问题：NodeRecord 定义了 category 字段，但 register()
没有任何地方能填它 —— 「声明了但没人填」。这里给 register()
加可选 category，只在已有值为空时填充（后到的值不覆盖先到的
非空值，防手滑降级）。

正常路径下节点反向索引由 WorkflowRepository.add()/delete()
自动对账维护；register() 供零散补充（如先登记节点分类）用。
"""


class NodeRepository:
    """节点使用关系的登记与查询"""

    def __init__(self, database):
        self.db = database

    def register(self, node: str, workflow_id: str, category: str = ""):
        """
        登记「某 workflow 用了某节点」；重复登记不产生重复项

        Args:
            node: 节点类型名（如 "KSampler"）
            workflow_id: workflow 记录 id
            category: 节点分类；只在已有值为空时填充
        """
        nodes = self.db.data["nodes"]
        entry = nodes.setdefault(node, {"category": "", "used_in": []})
        if category and not entry.get("category"):
            entry["category"] = category
        if workflow_id not in entry["used_in"]:
            entry["used_in"].append(workflow_id)
        if self.db.auto_save:
            self.db.save()

    def workflows_using(self, node: str):
        """哪些 workflow 用了这个节点；没登记过返回空列表"""
        entry = self.db.data["nodes"].get(node, {})
        return list(entry.get("used_in", []))

    def get(self, node: str):
        """单节点详情副本 dict（含 category）；没登记过返回 None"""
        entry = self.db.data["nodes"].get(node)
        return dict(entry) if entry is not None else None

    def all(self):
        """全部节点（dict，name → 详情副本）"""
        return {
            name: dict(entry)
            for name, entry in self.db.data["nodes"].items()
        }
