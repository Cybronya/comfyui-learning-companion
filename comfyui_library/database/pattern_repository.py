r"""
Pattern 仓库 —— 模式 ↔ workflow 的归属

设计稿的问题：只写了 add()，没有 get / all；且 pattern.workflows
与 workflow.patterns 互为引用却各写各的，必然漂移。
这里 add() 时把模式名回填进各 workflow 记录的 patterns 列表；
workflow 不存在时跳过 —— 悬空归属保持可见、不猜着连，
与 knowledge_graph 对悬空边的处理一致。

sqlite 后端（2026-10-14）：回填走 SQL 读改写，同一短连接内完成。
"""

import json


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
        conn = self.db._begin_write()
        owned = conn is not self.db._conn
        try:
            conn.execute(
                "INSERT OR REPLACE INTO patterns(name, workflows_json,"
                " description) VALUES (?,?,?)",
                (name, json.dumps(members, ensure_ascii=False), description),
            )
            for wid in members:
                row = conn.execute(
                    "SELECT patterns_json FROM workflows WHERE id=?", (wid,)
                ).fetchone()
                if row is None:
                    continue  # 悬空成员：只记录、不猜着建 workflow
                cur = json.loads(row["patterns_json"])
                if name not in cur:
                    cur.append(name)
                    conn.execute(
                        "UPDATE workflows SET patterns_json=? WHERE id=?",
                        (json.dumps(cur, ensure_ascii=False), wid),
                    )
            self.db._end_write(conn)
        except Exception:
            if owned:
                conn.close()
            raise

    def get(self, name: str):
        """单模式详情副本 dict；不存在返回 None"""
        conn = self.db._read()
        if conn is None:
            return None
        try:
            row = conn.execute(
                "SELECT workflows_json, description FROM patterns WHERE name=?",
                (name,),
            ).fetchone()
        finally:
            self.db._end_read(conn)
        if row is None:
            return None
        return {
            "workflows": json.loads(row["workflows_json"]),
            "description": row["description"],
        }

    def all(self) -> dict:
        """全部模式（dict，name → 详情副本）"""
        conn = self.db._read()
        if conn is None:
            return {}
        try:
            result = {}
            for row in conn.execute(
                "SELECT name, workflows_json, description FROM patterns"
                " ORDER BY rowid"
            ):
                result[row["name"]] = {
                    "workflows": json.loads(row["workflows_json"]),
                    "description": row["description"],
                }
        finally:
            self.db._end_read(conn)
        return result
