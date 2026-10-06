r"""
Pattern 仓库 —— 模式 ↔ workflow 的归属

设计稿的问题：只写了 add()，没有 get / all；且 pattern.workflows
与 workflow.patterns 互为引用却各写各的，必然漂移。
这里 add() 时把模式名回填进各 workflow 记录的 patterns 列表；
workflow 不存在时跳过 —— 悬空归属保持可见、不猜着连，
与 knowledge_graph 对悬空边的处理一致。
"""


class PatternRepository:
    """模式的登记与查询"""

    def __init__(self, database):
        self.db = database

    def add(self, name: str, workflows, description: str = ""):
        """
        新增或更新一个模式（同名覆盖），并回填 workflow.patterns

        Args:
            name: 模式名
            workflows: 模式覆盖的 workflow id 列表（去重保序）
            description: 模式说明
        """
        members = list(dict.fromkeys(workflows))
        self.db.data["patterns"][name] = {
            "workflows": members,
            "description": description,
        }
        for wid in members:
            record = self.db.data["workflows"].get(wid)
            if record is None:
                continue
            if name not in record.get("patterns", []):
                record.setdefault("patterns", []).append(name)
        if self.db.auto_save:
            self.db.save()

    def get(self, name: str):
        """单模式详情副本 dict；不存在返回 None"""
        entry = self.db.data["patterns"].get(name)
        return dict(entry) if entry is not None else None

    def all(self):
        """全部模式（dict，name → 详情副本）"""
        return {
            name: dict(entry)
            for name, entry in self.db.data["patterns"].items()
        }
