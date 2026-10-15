r"""
Workflow 仓库 —— workflow 记录的增删查

add/delete 自动对账节点反向索引（node_used_in）：
- add：新节点登记进 nodes 表（条目永不删），junction 增行；
  删掉的节点从 junction 摘行（条目留空壳，不静默消失）
- delete：摘除该 workflow 的全部 junction 行，nodes 条目保留

patterns 语义：add 时的 patterns 与库里已有的取并集 ——
PatternRepository.add 回填进来的模式名不因重学被抹掉。

sqlite 后端（2026-10-14）：每操作短连接（用完即关，Windows 实测
持久连接会让 TemporaryDirectory 清理 PermissionError）；
批量模式（auto_save=False）走持有连接累积事务，save() 一次提交。
"""

import json


class WorkflowRepository:
    """workflow 记录的存取"""

    def __init__(self, database):
        self.db = database

    def _snapshot(self, workflow, nodes, patterns):
        """写库后回给调用方的全字段 dict（workflow_type 存作 type）"""
        return {
            "id": workflow.id,
            "name": workflow.name,
            "file_path": workflow.file_path,
            "status": workflow.status,
            "type": workflow.workflow_type,
            "nodes": list(nodes),
            "patterns": list(patterns),
            "report": workflow.report,
            "content_hash": workflow.content_hash,
            "official": bool(workflow.official),
        }

    def add(self, workflow) -> dict:
        """
        新增或更新一个 workflow（同 id 覆盖全字段），并对账节点反向索引

        Args:
            workflow: WorkflowRecord（models.py）
        """
        conn = self.db._begin_write()
        owned = conn is not self.db._conn
        try:
            row = conn.execute(
                "SELECT nodes_json, patterns_json FROM workflows WHERE id=?",
                (workflow.id,),
            ).fetchone()
            old_nodes = set(json.loads(row["nodes_json"])) if row else set()
            old_patterns = json.loads(row["patterns_json"]) if row else []

            new_nodes = list(dict.fromkeys(workflow.nodes or []))
            # patterns 并集合并：模式回填进来的名字不因重学被抹掉
            new_patterns = list(
                dict.fromkeys(list(old_patterns) + list(workflow.patterns or []))
            )

            conn.execute(
                "INSERT OR REPLACE INTO workflows VALUES (?,?,?,?,?,?,?,?,?,?)",
                (
                    workflow.id,
                    workflow.name,
                    workflow.file_path,
                    workflow.status,
                    workflow.workflow_type,
                    json.dumps(new_nodes, ensure_ascii=False),
                    json.dumps(new_patterns, ensure_ascii=False),
                    workflow.report,
                    workflow.content_hash,
                    1 if workflow.official else 0,
                ),
            )

            # 节点反向索引对账：新节点登记（category 只填空），减少的摘行
            for node in new_nodes:
                conn.execute(
                    "INSERT INTO nodes(name, category) VALUES (?, '')"
                    " ON CONFLICT(name) DO NOTHING",
                    (node,),
                )
                conn.execute(
                    "INSERT OR IGNORE INTO node_used_in(node, workflow_id)"
                    " VALUES (?,?)",
                    (node, workflow.id),
                )
            for node in old_nodes - set(new_nodes):
                conn.execute(
                    "DELETE FROM node_used_in WHERE node=? AND workflow_id=?",
                    (node, workflow.id),
                )
            self.db._end_write(conn)
        except Exception:
            if owned:
                conn.close()  # 短连接失败直接丢弃（未提交自动回滚）
            raise

        return self._snapshot(workflow, new_nodes, new_patterns)

    def delete(self, workflow_id: str) -> bool:
        """
        删除一个 workflow，连带清节点反向索引；
        删了返回 True，本来就没有返回 False
        """
        conn = self.db._begin_write()
        owned = conn is not self.db._conn
        try:
            cur = conn.execute(
                "DELETE FROM workflows WHERE id=?", (workflow_id,)
            )
            removed = cur.rowcount > 0
            # 反向索引清行；nodes 条目永不删（与其他记录解耦）
            conn.execute(
                "DELETE FROM node_used_in WHERE workflow_id=?", (workflow_id,)
            )
            self.db._end_write(conn)
        except Exception:
            if owned:
                conn.close()
            raise
        return removed

    def rename(
        self,
        old_id: str,
        new_id: str,
        file_path: str = None,
        name: str = None,
    ) -> bool:
        """
        改一条记录的 id（连带对账节点反向索引与经验键）

        库内文件改名 / 归类搬迁后调用，避免「删旧建新」把 nodes_json、
        report、content_hash 全丢光。同一事务内完成：写新键 → 清旧键
        的 junction 行 → 按原节点清单重挂 → 经验行换键 → 删旧键。

        Args:
            old_id: 旧 id（相对路径，如 "视频生成/文生视频/xxx_123.json"）
            new_id: 新 id
            file_path: 顺带改文件路径；None 表示沿用旧值
            name: 顺带改名字；None 表示沿用旧值
        Returns:
            改成功 True；旧键不存在 False
        """
        conn = self.db._begin_write()
        owned = conn is not self.db._conn
        try:
            row = conn.execute(
                "SELECT * FROM workflows WHERE id=?", (old_id,)
            ).fetchone()
            if row is None:
                self.db._end_write(conn)  # 提前返回也要收连接（否则泄漏）
                return False
            conn.execute(
                "INSERT OR REPLACE INTO workflows VALUES (?,?,?,?,?,?,?,?,?,?)",
                (
                    new_id,
                    name if name is not None else row["name"],
                    file_path if file_path is not None else row["file_path"],
                    row["status"],
                    row["type"],
                    row["nodes_json"],
                    row["patterns_json"],
                    row["report"],
                    row["content_hash"],
                    row["official"],
                ),
            )
            # junction 行随键搬迁：清旧键、按原清单重挂（nodes 条目不动）
            conn.execute(
                "DELETE FROM node_used_in WHERE workflow_id=?", (old_id,)
            )
            for node in json.loads(row["nodes_json"]):
                conn.execute(
                    "INSERT OR IGNORE INTO node_used_in(node, workflow_id)"
                    " VALUES (?,?)",
                    (node, new_id),
                )
            # 经验按 workflow_id 主键存，一并换键（旧键删掉，不留悬空）
            exp = conn.execute(
                "SELECT content, tags_json, data_json FROM experiences"
                " WHERE workflow_id=?",
                (old_id,),
            ).fetchone()
            if exp is not None:
                conn.execute(
                    "INSERT OR REPLACE INTO experiences(workflow_id, content,"
                    " tags_json, data_json) VALUES (?,?,?,?)",
                    (new_id, exp["content"], exp["tags_json"], exp["data_json"]),
                )
                conn.execute(
                    "DELETE FROM experiences WHERE workflow_id=?", (old_id,)
                )
            # 旧键落地删除（new_id == old_id 时上面 INSERT OR REPLACE 已原地更新）
            if new_id != old_id:
                conn.execute(
                    "DELETE FROM workflows WHERE id=?", (old_id,)
                )
            self.db._end_write(conn)
        except Exception:
            if owned:
                conn.close()
            raise
        return True

    def get(self, workflow_id: str):
        """单条记录副本 dict；不存在返回 None"""
        conn = self.db._read()
        if conn is None:
            return None
        try:
            row = conn.execute(
                "SELECT * FROM workflows WHERE id=?", (workflow_id,)
            ).fetchone()
        finally:
            self.db._end_read(conn)
        from .database import _record_dict

        return _record_dict(row) if row is not None else None

    def all(self) -> list:
        """全部记录（list[dict]，按插入序）"""
        conn = self.db._read()
        if conn is None:
            return []
        try:
            rows = conn.execute(
                "SELECT * FROM workflows ORDER BY rowid"
            ).fetchall()
        finally:
            self.db._end_read(conn)
        from .database import _record_dict

        return [_record_dict(row) for row in rows]
