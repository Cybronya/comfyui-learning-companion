r"""
Workflow 仓库 —— workflow 记录的增删查

设计稿的问题，落地时补上：

1. 标题说「增删查」但没有 delete。补上，且删除时把该 workflow
   从各节点的 used_in 里摘掉 —— 反向索引留悬空引用，
   就是 knowledge_graph 里「悬空边」那类问题。
2. add() 只写 workflow 自身字段、不管节点反向索引的话，
   workflow.nodes 与 node.used_in 就是两份各自漂移的状态
   （learning_scheduler 里 SchedulerState 与 TaskQueue 漂移同款）。
   这里让 add() 顺手对账：节点增了就登记 used_in，减了就摘除。
3. workflow.patterns 与 PatternRepository.add 的回填是两个写者，
   更新 workflow 时不带 patterns 会把回填抹掉 —— 改成并集合并。
"""

from .models import WorkflowRecord


class WorkflowRepository:
    """workflow 记录的增删查 + 节点反向索引对账"""

    def __init__(self, database):
        self.db = database

    # ---------- 写 ----------

    def add(self, workflow: WorkflowRecord):
        """
        新增或更新一条记录（按 id 覆盖）

        同时做两件对账：
        - 节点反向索引：workflow.nodes 增了登记 used_in，减了摘除；
        - patterns 归属：与已有记录并集合并，
          避免抹掉 PatternRepository 回填的归属。

        Returns:
            存储后的记录副本 dict
        """
        workflows = self.db.data["workflows"]
        old = workflows.get(workflow.id, {})
        old_nodes = set(old.get("nodes", []))

        new_nodes = list(dict.fromkeys(workflow.nodes))
        new_patterns = list(dict.fromkeys(
            list(old.get("patterns", [])) + list(workflow.patterns)
        ))

        workflows[workflow.id] = {
            "id": workflow.id,
            "name": workflow.name,
            "file_path": workflow.file_path,
            "status": workflow.status,
            "type": workflow.workflow_type,
            "nodes": new_nodes,
            "patterns": new_patterns,
            "report": workflow.report,
            "content_hash": workflow.content_hash,
            "official": bool(workflow.official),
        }

        nodes = self.db.data["nodes"]
        for node in new_nodes:
            entry = nodes.setdefault(node, {"category": "", "used_in": []})
            if workflow.id not in entry["used_in"]:
                entry["used_in"].append(workflow.id)
        for node in old_nodes - set(new_nodes):
            entry = nodes.get(node)
            if entry and workflow.id in entry["used_in"]:
                entry["used_in"].remove(workflow.id)

        if self.db.auto_save:
            self.db.save()
        return dict(workflows[workflow.id])

    def delete(self, workflow_id: str) -> bool:
        """
        删除一条记录，并清理它在节点反向索引里的引用

        注意：patterns / experiences 里对它的引用**不**连带删，
        悬空保持可见（与 knowledge_graph 对悬空边的处理一致）；
        要清就显式调对应仓库的 delete。

        Returns:
            删了返回 True；本来就不存在返回 False
        """
        removed = self.db.data["workflows"].pop(workflow_id, None)
        if removed is None:
            return False
        for entry in self.db.data["nodes"].values():
            if workflow_id in entry["used_in"]:
                entry["used_in"].remove(workflow_id)
        if self.db.auto_save:
            self.db.save()
        return True

    # ---------- 查 ----------

    def get(self, workflow_id: str):
        """单条记录副本 dict；不存在返回 None"""
        record = self.db.data["workflows"].get(workflow_id)
        return dict(record) if record is not None else None

    def all(self):
        """全部记录（list[dict]，按插入序）"""
        return [
            dict(record)
            for record in self.db.data["workflows"].values()
        ]
