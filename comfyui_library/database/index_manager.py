r"""
IndexManager —— 从库内容构建三个查询索引并可落盘

设计稿的问题：storage/ 目录列了三个索引文件，
但这里只给了 build_workflow_index() 一个方法，而且不落盘 ——
列了文件却没人写，就是「声明了但没人填」。这里补齐：

- workflow_index.json : node → [workflow_id]，「用了 X 节点的流程有哪些」
- node_index.json     : node → {category, used_in, usage_count}
- pattern_index.json  : pattern → {workflows, workflow_count, description}

三个索引都是从库内容派生的，随时可用 save_all() 重建，丢了不必心疼。
落盘路径与数据库文件同目录（storage/）。

注意：这里的 node_index.json 是「节点使用索引」，
与 comfyui_library/knowledge/nodes/node_index.json（知识卡索引）
同名不同物，别混。

sqlite 后端（2026-10-14）：构建改走 SQL 直查，不再物化 db.data ——
旧实现经 .data 兼容视图会把 29553 条 workflow 全量记录（含 report 与
nodes_json）拉进内存，正是主库 OOM 的路径。改后 workflow_index 一次
扫描 junction 表（75 万行），node_index 逐表直查，pattern 直查小表。
落盘与读回 API 与旧版完全一致（JSON 文件，派生数据可重建）。
"""

import json


class IndexManager:
    """派生索引的构建与落盘"""

    def __init__(self, database):
        self.db = database

    # ---------- 构建 ----------

    def build_workflow_index(self):
        """node → [workflow_id]，从 junction 表直查（按 node, workflow_id
        排序，与旧版「逐 workflow 收集后排序」结果一致）"""
        conn = self.db._read()
        if conn is None:
            return {}
        try:
            index = {}
            for node, wid in conn.execute(
                "SELECT node, workflow_id FROM node_used_in"
                " ORDER BY node, workflow_id"
            ):
                index.setdefault(node, []).append(wid)
        finally:
            self.db._end_read(conn)
        return index

    def build_node_index(self):
        """node → {category, used_in, usage_count}

        nodes 表全量条目（含空 used_in 的节点，旧版语义不变），
        used_in 从 junction 表按序填入（junction 主键去重，
        排序后与旧版 sorted(set(...)) 一致）。
        """
        conn = self.db._read()
        if conn is None:
            return {}
        try:
            index = {}
            for row in conn.execute(
                "SELECT name, category FROM nodes ORDER BY rowid"
            ):
                index[row["name"]] = {
                    "category": row["category"],
                    "used_in": [],
                }
            for node, wid in conn.execute(
                "SELECT node, workflow_id FROM node_used_in"
                " ORDER BY node, workflow_id"
            ):
                if node in index:
                    index[node]["used_in"].append(wid)
            for entry in index.values():
                entry["usage_count"] = len(entry["used_in"])
        finally:
            self.db._end_read(conn)
        return index

    def build_pattern_index(self):
        """pattern → {workflows, workflow_count, description}"""
        conn = self.db._read()
        if conn is None:
            return {}
        try:
            index = {}
            for row in conn.execute(
                "SELECT name, workflows_json, description FROM patterns"
                " ORDER BY rowid"
            ):
                members = sorted(set(json.loads(row["workflows_json"])))
                index[row["name"]] = {
                    "workflows": members,
                    "workflow_count": len(members),
                    "description": row["description"],
                }
        finally:
            self.db._end_read(conn)
        return index

    # ---------- 落盘 ----------

    def _index_path(self, name: str):
        return self.db.path.parent / f"{name}.json"

    def save_index(self, name: str, index) -> str:
        """把一个索引写到数据库同目录（<name>.json），返回路径"""
        path = self._index_path(name)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(index, f, indent=4, ensure_ascii=False)
            f.write("\n")
        return str(path)

    def load_index(self, name: str):
        """读回一个索引；文件不存在或坏了返回 {}（派生数据，可重建）"""
        path = self._index_path(name)
        if not path.exists():
            return {}
        try:
            # utf-8-sig：项目约定读 JSON 一律用它（BOM 兼容）
            with open(path, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
        except Exception as e:
            print(f"读取索引失败（可 save_all 重建）: {path}（{e}）")
            return {}
        return data if isinstance(data, dict) else {}

    def save_all(self):
        """构建并落盘全部三个索引，返回 {名字: 路径}"""
        return {
            "workflow_index": self.save_index(
                "workflow_index", self.build_workflow_index()
            ),
            "node_index": self.save_index(
                "node_index", self.build_node_index()
            ),
            "pattern_index": self.save_index(
                "pattern_index", self.build_pattern_index()
            ),
        }
