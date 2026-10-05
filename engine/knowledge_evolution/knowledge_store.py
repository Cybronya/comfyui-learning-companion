"""
知识存储

保存演化产出的 Pattern Knowledge，支持 JSON 持久化。
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Optional

from .models import EvolutionKnowledge, WorkflowPattern


class KnowledgeStore:
    """
    演化知识存储
    """

    def __init__(self, path: str = "engine/knowledge_evolution/evolution_store.json") -> None:
        """
        初始化存储

        Args:
            path: 存储文件路径
        """
        self.path = Path(path)
        self.data: List[Dict] = []
        self.load()

    def load(self) -> None:
        """
        从文件加载知识数据
        """
        if self.path.exists():
            try:
                with open(self.path, "r", encoding="utf-8-sig") as f:
                    data = json.load(f)

                # 兼容两种结构：纯列表，或 {"patterns": [...]} 包装
                if isinstance(data, dict):
                    self.data = data.get("patterns", [])
                else:
                    self.data = data
            except Exception as e:
                print(f"加载演化知识失败: {e}")
                self.data = []
        else:
            self.data = []

    def add(self, knowledge: Any) -> None:
        """
        添加一条知识

        Args:
            knowledge: 知识字典、WorkflowPattern 或 EvolutionKnowledge
        """
        if isinstance(knowledge, EvolutionKnowledge):
            entries = [p.to_dict() for p in knowledge.patterns]
        elif isinstance(knowledge, WorkflowPattern):
            entries = [knowledge.to_dict()]
        else:
            entries = [knowledge]

        for entry in entries:
            self.data.append(entry)

        self.save()

    def replace_all(self, knowledge: EvolutionKnowledge) -> None:
        """
        用一次演化的结果整体替换存储内容

        演化是全量重算的（模式统计不支持增量），所以覆盖比追加更准确，
        避免同一模式在多次演化后堆出多条重复记录。

        Args:
            knowledge: 本次演化产出的知识集合
        """
        self.data = [p.to_dict() for p in knowledge.patterns]
        self.save()

    def get_all(self) -> List[Dict]:
        """
        获取全部知识
        """
        return list(self.data)

    def find_by_name(self, name: str) -> List[Dict]:
        """
        按名称查找知识

        Args:
            name: 模式名称

        Returns:
            匹配的知识列表
        """
        return [
            item for item in self.data
            if item.get("name") == name
            or item.get("pattern") == name
        ]

    def clear(self) -> None:
        """
        清空存储
        """
        self.data = []
        self.save()

    def save(self) -> None:
        """
        保存到文件
        """
        try:
            self.path.parent.mkdir(parents=True, exist_ok=True)

            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(
                    self.data,
                    f,
                    indent=4,
                    ensure_ascii=False
                )
        except Exception as e:
            print(f"保存演化知识失败: {e}")
