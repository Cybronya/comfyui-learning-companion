r"""
Experience 仓库 —— 学习经验

按 workflow_id 存，同一 workflow 只保留最新一条：
重学后新经验覆盖旧经验 —— 经验是「当前理解」，不是历史流水
（历史流水在 engine/learning_loop 的 experience_store）。

设计稿只有 add / get；补 all 与 delete。
删除 workflow 不自动删经验 —— 悬空保持可见，要清就显式调 delete。

sqlite 后端（2026-10-14）：data_json 走 zlib 压缩（实测 3.06x，
压后 3.0KB/条、压前 9.2KB/条，30616 条合计 39MB）；新增 iter_items()
流式迭代 —— 全部载荷物化成 dict 会吃掉 400MB+ 内存（JSON 文本本身
约 120MB，Python 对象膨胀 3-5 倍），归纳引擎等大消费方走本方法逐条取用。
"""

import json


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
        conn = self.db._begin_write()
        owned = conn is not self.db._conn
        try:
            conn.execute(
                "INSERT OR REPLACE INTO experiences(workflow_id, content,"
                " tags_json, data_json) VALUES (?,?,?,?)",
                (
                    workflow_id,
                    content,
                    json.dumps(list(tags or []), ensure_ascii=False),
                    _zlib_compress_data(dict(data or {})),
                ),
            )
            self.db._end_write(conn)
        except Exception:
            if owned:
                conn.close()
            raise

    def get(self, workflow_id: str):
        """单条经验副本 dict；不存在返回 None"""
        conn = self.db._read()
        if conn is None:
            return None
        try:
            row = conn.execute(
                "SELECT content, tags_json, data_json FROM experiences"
                " WHERE workflow_id=?",
                (workflow_id,),
            ).fetchone()
        finally:
            self.db._end_read(conn)
        if row is None:
            return None
        from .database import _decode_data

        return {
            "content": row["content"],
            "tags": json.loads(row["tags_json"]),
            "data": _decode_data(row["data_json"]),
        }

    def all(self) -> dict:
        """全部经验（dict，workflow_id → 详情副本）"""
        conn = self.db._read()
        if conn is None:
            return {}
        from .database import _decode_data

        try:
            result = {}
            for row in conn.execute(
                "SELECT workflow_id, content, tags_json, data_json FROM"
                " experiences ORDER BY rowid"
            ):
                result[row["workflow_id"]] = {
                    "content": row["content"],
                    "tags": json.loads(row["tags_json"]),
                    "data": _decode_data(row["data_json"]),
                }
        finally:
            self.db._end_read(conn)
        return result

    def iter_items(self, order: str = "insertion"):
        """
        流式迭代全部经验：(workflow_id, {"content", "tags", "data"})

        Args:
            order: "insertion" 按写入序；"key" 按 workflow_id 排序
                   （与旧版 sorted(experiences) 同序，归纳引擎用）

        30616 条经验全量物化会吃掉 400MB+ 内存（载荷 JSON 约 120MB，
        Python 对象膨胀 3-5 倍）；knowledge_consolidation.ExperienceLoader
        走本方法逐条取用。

        注意：生成器持有读连接直到消费完或被 GC。消费方若中途放弃迭代，
        连接可能残留（Windows 上 TemporaryDirectory 清理会因此报
        PermissionError）—— 要么消费完，要么显式 close()。
        """
        from .database import _decode_data

        sql = "SELECT workflow_id, content, tags_json, data_json FROM experiences"
        if order == "key":
            sql += " ORDER BY workflow_id"
        else:
            sql += " ORDER BY rowid"
        conn = self.db._read()
        if conn is None:
            return
        try:
            for row in conn.execute(sql):
                yield (
                    row["workflow_id"],
                    {
                        "content": row["content"],
                        "tags": json.loads(row["tags_json"]),
                        "data": _decode_data(row["data_json"]),
                    },
                )
        finally:
            self.db._end_read(conn)

    def delete(self, workflow_id: str) -> bool:
        """删除一条经验；删了返回 True，本来就没有返回 False"""
        conn = self.db._begin_write()
        owned = conn is not self.db._conn
        try:
            cur = conn.execute(
                "DELETE FROM experiences WHERE workflow_id=?", (workflow_id,)
            )
            removed = cur.rowcount > 0
            self.db._end_write(conn)
        except Exception:
            if owned:
                conn.close()
            raise
        return removed


def _zlib_compress_data(data: dict) -> bytes:
    """data dict → zlib 压缩的 JSON blob（级 6，实测约 3.3x）"""
    import zlib

    return zlib.compress(
        json.dumps(data, ensure_ascii=False).encode("utf-8"), 6
    )
