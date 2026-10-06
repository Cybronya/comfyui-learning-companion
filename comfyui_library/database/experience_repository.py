r"""
Experience 仓库 —— 学习经验

按 workflow_id 存，同一 workflow 只保留最新一条：
重学后新经验覆盖旧经验 —— 经验是「当前理解」，不是历史流水
（历史流水在 engine/learning_loop 的 experience_store）。

设计稿只有 add / get；补 all 与 delete。
删除 workflow 不自动删经验 —— 悬空保持可见，要清就显式调 delete。
"""


class ExperienceRepository:
    """学习经验的存取"""

    def __init__(self, database):
        self.db = database

    def add(self, workflow_id: str, content: str, tags=None, data=None):
        """
        写入一条经验（同 workflow_id 覆盖旧条）

        Args:
            workflow_id: 所属 workflow 的记录 id
            content: 给人读的摘要
            tags: 标签列表
            data: 结构化载荷 dict（如 LearningRecord.to_dict()），
                  供 knowledge_consolidation 等下游按字段取用
        """
        self.db.data["experiences"][workflow_id] = {
            "content": content,
            "tags": list(tags or []),
            "data": dict(data or {}),
        }
        if self.db.auto_save:
            self.db.save()

    def get(self, workflow_id: str):
        """单条经验副本 dict；不存在返回 None"""
        entry = self.db.data["experiences"].get(workflow_id)
        return dict(entry) if entry is not None else None

    def all(self):
        """全部经验（dict，workflow_id → 详情副本）"""
        return {
            wid: dict(entry)
            for wid, entry in self.db.data["experiences"].items()
        }

    def delete(self, workflow_id: str) -> bool:
        """删除一条经验；删了返回 True，本来就没有返回 False"""
        removed = self.db.data["experiences"].pop(workflow_id, None)
        if removed is None:
            return False
        if self.db.auto_save:
            self.db.save()
        return True
