"""workflow_index_manager.py — 管理已学习 workflow 的模式索引。

索引文件格式（JSON）：

    {
      "workflows": [
        {
          "name": "sd15-basic",
          "patterns": ["sd15-t2i-basic"],
          "nodes": ["KSampler", "CheckpointLoader"]
        }
      ]
    }

提供 find_similar_workflows()：按节点集合重叠度找出与目标 workflow 最相似的
已索引 workflow，供 pattern-learning 判断是"已知模式"还是"新模式"。
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

DEFAULT_INDEX_PATH = Path("comfyui_library") / "workflows" / "workflow_index.json"


class WorkflowIndexManager:

    def __init__(self, index_path: str | Path = DEFAULT_INDEX_PATH):
        self.index_path = Path(index_path)
        self.index: Dict[str, Any] = {"workflows": []}
        if self.index_path.exists():
            self.load()

    def load(self) -> Dict[str, Any]:
        with open(self.index_path, "r", encoding="utf-8") as f:
            self.index = json.load(f)
        if "workflows" not in self.index:
            self.index["workflows"] = []
        return self.index

    def save(self) -> None:
        self.index_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.index_path, "w", encoding="utf-8") as f:
            json.dump(self.index, f, ensure_ascii=False, indent=2)

    def add_workflow(self, name: str, patterns: List[str],
                     nodes: List[str]) -> Dict[str, Any]:
        entry = {"name": name, "patterns": patterns, "nodes": nodes}
        self.index["workflows"].append(entry)
        return entry

    def get_workflow(self, name: str) -> Dict[str, Any] | None:
        for w in self.index["workflows"]:
            if w.get("name") == name:
                return w
        return None

    def find_similar_workflows(self, nodes: List[str],
                               top_k: int = 3) -> List[Dict[str, Any]]:
        """按节点集合重叠度（Jaccard 相似度）返回最相似的已索引 workflow。"""
        target = set(nodes)
        results: List[Dict[str, Any]] = []
        for w in self.index["workflows"]:
            known = set(w.get("nodes", []))
            if not known and not target:
                score = 1.0
            elif not known or not target:
                score = 0.0
            else:
                score = len(target & known) / len(target | known)
            results.append({
                "name": w.get("name"),
                "patterns": w.get("patterns", []),
                "score": round(score, 3),
                "shared_nodes": sorted(target & known),
                "missing_nodes": sorted(known - target),
                "new_nodes": sorted(target - known),
            })
        results.sort(key=lambda r: r["score"], reverse=True)
        return results[:top_k]
