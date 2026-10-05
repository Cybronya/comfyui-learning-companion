"""
知识索引

建立关键词到知识条目的倒排索引，避免每次检索都扫描全部知识文件。

索引结构：
    {关键词: [知识条目, ...]}

知识条目统一格式：
    {
        "type": "node" | "workflow_pattern" | "experience" | "evolution_knowledge",
        "node": "ControlNetApply",       # 关联节点（type=node 时使用）
        "name": "ControlNet 权重控制",
        "content": "...",
        "source": "comfyui_library/knowledge/nodes/controlnet.md"
    }
"""

import json
from pathlib import Path
from typing import Dict, List, Any


class KnowledgeIndex:
    """
    关键词倒排索引
    """

    def __init__(
        self,
        path: str = "engine/retrieval/retrieval_store.json",
        auto_load: bool = True
    ) -> None:
        """
        初始化索引

        Args:
            path: 索引文件路径
            auto_load: 是否自动加载该路径的已有文件。
                       **传 False 的场景**：dict 知识库包装成索引时
                       （KnowledgeRetriever._dict_to_index）——
                       否则磁盘上的真实索引会混进 dict，两条数据源
                       悄悄合并（2026-10-06 实跑踩到：dict 测试因
                       真实 retrieval_store.json 里有 pattern 卡而
                       多召回两条，此前能过纯属侥幸）
        """
        self.path = Path(path)
        self.index: Dict[str, List[Dict]] = {}
        if auto_load:
            self.load()

    def load(self) -> None:
        """
        从文件加载索引
        """
        if self.path.exists():
            try:
                with open(self.path, "r", encoding="utf-8-sig") as f:
                    self.index = json.load(f)
            except Exception as e:
                print(f"加载检索索引失败: {e}")
                self.index = {}
        else:
            self.index = {}

    def add(self, keyword: str, item: Dict) -> None:
        """
        添加一条知识到指定关键词下

        Args:
            keyword: 关键词
            item: 知识条目
        """
        if keyword not in self.index:
            self.index[keyword] = []

        # 同一关键词下避免重复条目
        signature = (item.get("type", ""), item.get("name", ""),
                     item.get("source", ""))
        for existing in self.index[keyword]:
            existing_sig = (existing.get("type", ""),
                            existing.get("name", ""),
                            existing.get("source", ""))
            if existing_sig == signature:
                return

        self.index[keyword].append(item)

    def add_many(self, keywords: List[str], item: Dict) -> None:
        """
        把同一条知识挂到多个关键词下

        Args:
            keywords: 关键词列表
            item: 知识条目
        """
        for keyword in keywords:
            if keyword:
                self.add(keyword, item)

    def search(self, keyword: str) -> List[Dict]:
        """
        按关键词检索

        Args:
            keyword: 关键词

        Returns:
            知识条目列表，无匹配时返回空列表
        """
        return self.index.get(keyword, [])

    def keys(self) -> List[str]:
        """
        索引中已有的全部关键词
        """
        return list(self.index.keys())

    def size(self) -> int:
        """
        索引中不重复的知识条目总数
        """
        seen = set()
        for items in self.index.values():
            for item in items:
                seen.add((
                    item.get("type", ""),
                    item.get("name", ""),
                    item.get("source", ""),
                ))
        return len(seen)

    def clear(self) -> None:
        """
        清空索引
        """
        self.index = {}

    def save(self) -> None:
        """
        保存到文件
        """
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)

            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(
                    self.index,
                    f,
                    indent=4,
                    ensure_ascii=False
                )
        except Exception as e:
            print(f"保存检索索引失败: {e}")
