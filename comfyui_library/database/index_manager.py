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
"""

import json


class IndexManager:
    """派生索引的构建与落盘"""

    def __init__(self, database):
        self.db = database

    # ---------- 构建 ----------

    def build_workflow_index(self):
        """node → [workflow_id]，按 workflow 记录的 nodes 重建（排序保稳定）"""
        index = {}
        for wid, record in self.db.data["workflows"].items():
            for node in record.get("nodes", []):
                if wid not in index.setdefault(node, []):
                    index[node].append(wid)
        for members in index.values():
            members.sort()
        return index

    def build_node_index(self):
        """node → {category, used_in, usage_count}"""
        index = {}
        for node, entry in self.db.data["nodes"].items():
            used_in = sorted(set(entry.get("used_in", [])))
            index[node] = {
                "category": entry.get("category", ""),
                "used_in": used_in,
                "usage_count": len(used_in),
            }
        return index

    def build_pattern_index(self):
        """pattern → {workflows, workflow_count, description}"""
        index = {}
        for name, entry in self.db.data["patterns"].items():
            members = sorted(set(entry.get("workflows", [])))
            index[name] = {
                "workflows": members,
                "workflow_count": len(members),
                "description": entry.get("description", ""),
            }
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
