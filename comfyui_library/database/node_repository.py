r"""
Node 仓库 —— 节点类型 → 哪些 workflow 在用它

设计稿的问题：NodeRecord 定义了 category 字段，但 register()
没有任何地方能填它 —— 「声明了但没人填」。这里给 register()
加可选 category，只在已有值为空时填充（后到的值不覆盖先到的
非空值，防手滑降级）。

正常路径下节点反向索引由 WorkflowRepository.add()/delete()
自动对账维护；register() 供零散补充（如先登记节点分类）用。

sqlite 后端（2026-10-14）：节点主表 + junction 表（node_used_in），
按 id 查询 O(索引) 而非全库扫描。
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
        conn = self.db._begin_write()
        owned = conn is not self.db._conn
        try:
            # 主表条目：不存在则插入（带 category）；存在则不动（保旧值）
            conn.execute(
                "INSERT INTO nodes(name, category) VALUES (?,?)"
                " ON CONFLICT(name) DO NOTHING",
                (node, category),
            )
            if category:
                # 只填空：已有非空分类时不覆盖（后到的值不覆盖先到的非空值）
                conn.execute(
                    "UPDATE nodes SET category=? WHERE name=? AND category=''",
                    (category, node),
                )
            conn.execute(
                "INSERT OR IGNORE INTO node_used_in(node, workflow_id) VALUES (?,?)",
                (node, workflow_id),
            )
            self.db._end_write(conn)
        except Exception:
            if owned:
                conn.close()
            raise

    def workflows_using(self, node: str) -> list:
        """哪些 workflow 用了这个节点；没登记过返回空列表（按登记序）"""
        conn = self.db._read()
        if conn is None:
            return []
        try:
            rows = conn.execute(
                "SELECT workflow_id FROM node_used_in WHERE node=? ORDER BY rowid",
                (node,),
            ).fetchall()
        finally:
            self.db._end_read(conn)
        return [r["workflow_id"] for r in rows]

    def get(self, node: str):
        """单节点详情副本 dict（含 category）；没登记过返回 None"""
        conn = self.db._read()
        if conn is None:
            return None
        try:
            row = conn.execute(
                "SELECT category FROM nodes WHERE name=?", (node,)
            ).fetchone()
            if row is None:
                return None
            used_in = [
                r["workflow_id"]
                for r in conn.execute(
                    "SELECT workflow_id FROM node_used_in WHERE node=?"
                    " ORDER BY rowid",
                    (node,),
                )
            ]
        finally:
            self.db._end_read(conn)
        return {"category": row["category"], "used_in": used_in}

    def all(self) -> dict:
        """全部节点（dict，name → 详情副本）"""
        conn = self.db._read()
        if conn is None:
            return {}
        try:
            result = {}
            for row in conn.execute(
                "SELECT name, category FROM nodes ORDER BY rowid"
            ):
                result[row["name"]] = {
                    "category": row["category"],
                    "used_in": [],
                }
            for node, wid in conn.execute(
                "SELECT node, workflow_id FROM node_used_in ORDER BY rowid"
            ):
                if node in result:
                    result[node]["used_in"].append(wid)
        finally:
            self.db._end_read(conn)
        return result
