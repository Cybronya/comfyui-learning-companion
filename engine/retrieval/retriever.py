"""
知识检索器（核心入口）

把「用户问题」变成「喂给回答生成器的知识片段」。

数据来源（统一汇进同一个 KnowledgeIndex）：
    node        comfyui_library/knowledge/nodes/*.md          静态节点知识卡
    pattern     comfyui_library/knowledge/patterns/*.md        Pattern 卡
    experience  engine/learning_loop/experience_store.json     历史调整经验
    evolution   engine/knowledge_evolution/evolution_store.json 演化知识（多经验统计，可信度最高）

索引构建一次即可，检索时只查倒排索引，不扫描知识目录。
"""

import json
from pathlib import Path
from typing import List, Dict, Any, Optional

from .knowledge_matcher import KnowledgeMatcher
from .knowledge_index import KnowledgeIndex
from .ranking import KnowledgeRanker


DEFAULT_INDEX_PATH = "engine/retrieval/retrieval_store.json"
KNOWLEDGE_DIR = "comfyui_library/knowledge"
EXPERIENCE_STORE = "engine/learning_loop/experience_store.json"
EVOLUTION_STORE = "engine/knowledge_evolution/evolution_store.json"


class KnowledgeRetriever:
    """
    知识检索器
    """

    def __init__(
        self,
        knowledge_base: Any = None,
        index_path: str = DEFAULT_INDEX_PATH,
        auto_build: bool = False
    ) -> None:
        """
        初始化检索器

        Args:
            knowledge_base: 知识库。
                            传 dict 则直接当 {主题: [条目]} 用（测试与临时场景）；
                            传 KnowledgeIndex 则复用已有索引；
                            传 None 则用 index_path 指向的索引文件。
            index_path: 索引文件路径
            auto_build: 是否在索引为空时自动从 comfyui_library 重建
        """
        self.matcher = KnowledgeMatcher()
        self.ranker = KnowledgeRanker()
        self.index_path = index_path

        if isinstance(knowledge_base, KnowledgeIndex):
            self.base = knowledge_base
        elif isinstance(knowledge_base, dict):
            self.base = self._dict_to_index(knowledge_base)
        else:
            self.base = KnowledgeIndex(index_path)
            if auto_build and not self.base.index:
                self.build_index(index_path)

    def _dict_to_index(self, knowledge: Dict[str, List[Dict]]) -> KnowledgeIndex:
        """
        把 {主题: [条目]} 形式的字典包装成 KnowledgeIndex
        """
        # auto_load=False：dict 是独立知识源，不得混入磁盘索引
        index = KnowledgeIndex(self.index_path, auto_load=False)
        for key, items in knowledge.items():
            for item in items:
                index.add(key, item)
        return index

    # ---------- 检索 ----------

    def retrieve(
        self,
        question: str,
        context: Dict = None,
        limit: int = 0
    ) -> List[Dict]:
        """
        检索与问题相关的知识

        Args:
            question: 用户问题
            context: 上下文，可含 workflow_nodes / workflow_type / parameters
            limit: 最多返回条数，0 表示不限制

        Returns:
            排序后的知识条目列表
        """
        if context is None:
            context = {}

        keywords = self.matcher.match(
            question, extra_keys=self.base.keys()
        )

        # 症状词（脸崩 / 色偏等）成因不止一个，把候选成因主题并入召回范围。
        # 「为什么脸崩」不该只召回 KSampler，而漏掉 LoRA 权重过高、VAE 解码异常。
        for topic in self.ranker.symptom_topics((question or "").lower()):
            if topic not in keywords:
                keywords.append(topic)

        results = []
        seen = set()

        for key in keywords:
            for item in self.base.search(key):
                signature = (
                    item.get("type", ""),
                    item.get("name", ""),
                    item.get("source", ""),
                )
                if signature in seen:
                    continue
                seen.add(signature)
                results.append(item)

        # 问题没命中任何主题时，退回当前工作流相关知识
        if not results:
            results = self._by_workflow_nodes(context)

        ranked = self.ranker.rank(results, context, question)

        if limit:
            return ranked[:limit]

        return ranked

    def _by_workflow_nodes(self, context: Dict) -> List[Dict]:
        """
        兜底：按当前工作流的节点召回知识
        """
        results = []
        seen = set()

        for node in context.get("workflow_nodes", []) or []:
            for keyword in self.matcher.index_keywords_for_node(node):
                for item in self.base.search(keyword):
                    signature = (
                        item.get("type", ""),
                        item.get("name", ""),
                        item.get("source", ""),
                    )
                    if signature in seen:
                        continue
                    seen.add(signature)
                    results.append(item)

        return results

    def retrieve_for_topics(
        self,
        topics: List[str],
        context: Dict = None,
        question: str = ""
    ) -> List[Dict]:
        """
        按指定主题检索（问题解析器已给出主题时用）

        Args:
            topics: 主题列表
            context: 上下文
            question: 原始问题（参与排序）

        Returns:
            排序后的知识条目
        """
        results = []
        seen = set()

        for topic in topics:
            for item in self.base.search(topic):
                signature = (
                    item.get("type", ""),
                    item.get("name", ""),
                    item.get("source", ""),
                )
                if signature in seen:
                    continue
                seen.add(signature)
                results.append(item)

        return self.ranker.rank(results, context, question)

    def format_for_prompt(self, items: List[Dict]) -> str:
        """
        把知识条目拼成 response_generator 可直接使用的文本

        Args:
            items: 排序后的知识条目

        Returns:
            Markdown 文本
        """
        if not items:
            return "（本次未检索到相关知识）"

        lines = []

        for i, item in enumerate(items, 1):
            kind = item.get("type", "knowledge")
            name = item.get("name", "未命名")
            lines.append(f"[{i}] ({kind}) {name}")

            content = item.get("content") or item.get("description")
            if content:
                lines.append(f"    {content}")

            for rec in item.get("recommendations", []) or []:
                lines.append(f"    - {rec}")

            if item.get("common_parameters"):
                lines.append(f"    参数区间: {item['common_parameters']}")

            if item.get("match_reasons"):
                lines.append(
                    f"    命中原因: {', '.join(item['match_reasons'])}"
                )

        return "\n".join(lines)

    # ---------- 索引构建 ----------

    def build_index(
        self,
        index_path: str = DEFAULT_INDEX_PATH,
        knowledge_dir: str = KNOWLEDGE_DIR,
        experience_store: str = EXPERIENCE_STORE,
        evolution_store: str = EVOLUTION_STORE
    ) -> KnowledgeIndex:
        """
        从各知识源构建倒排索引

        Args:
            index_path: 索引输出路径
            knowledge_dir: 静态知识卡目录
            experience_store: learning_loop 经验库
            evolution_store: knowledge_evolution 知识库

        Returns:
            构建好的 KnowledgeIndex
        """
        index = KnowledgeIndex(index_path)

        self._index_node_cards(index, knowledge_dir)
        self._index_pattern_cards(index, knowledge_dir)
        self._index_experiences(index, experience_store)
        self._index_evolution(index, evolution_store)

        self.base = index
        index.save()
        return index

    def _index_node_cards(
        self,
        index: KnowledgeIndex,
        knowledge_dir: str
    ) -> None:
        """
        索引静态节点知识卡
        """
        nodes_dir = Path(knowledge_dir) / "nodes"
        node_index_file = Path(knowledge_dir) / "node_index.json"

        # node_index.json 提供 category / role / difficulty / learning_topics。
        # 它的键是**节点类型**（KSampler），而目录里的文件名是小写下划线
        # （ksampler.md），两者不相等 —— 直接用 card.stem 去查永远查不到，
        # 导致所有知识卡的元信息都是空的。所以先建一张 stem → 节点类型 的反查表。
        meta_by_node = {}
        if node_index_file.exists():
            try:
                with open(node_index_file, "r", encoding="utf-8-sig") as f:
                    raw = json.load(f)
                meta_by_node = raw.get("nodes", {})
            except Exception as e:
                print(f"读取 node_index.json 失败: {e}")

        # 节点类型（小写） -> 真实节点类型。
        # 必须去掉下划线再比：文件名是 snake_case（clip_text_encode.md），
        # 而 node_index.json 的键是 PascalCase（CLIPTextEncode），
        # 只 lower() 的话 clip_text_encode 匹配不上 CLIPTextEncode，
        # 知识卡的 node 字段会退化成 snake_case 文件名，
        # 与工作流里的节点类型对不上，覆盖率统计随之全错。
        node_type_by_stem = {
            node_type.replace("_", "").lower(): node_type
            for node_type in meta_by_node
        }

        if not nodes_dir.exists():
            return

        for card in sorted(nodes_dir.glob("*.md")):
            try:
                with open(card, "r", encoding="utf-8-sig") as f:
                    content = f.read()
            except Exception as e:
                print(f"读取知识卡失败 {card}: {e}")
                continue

            # 真实节点类型。取不到时退回文件名（小写），
            # 至少保证 item["node"] 非空
            node_type = node_type_by_stem.get(
                card.stem.replace("_", "").lower(), card.stem
            )
            meta = meta_by_node.get(node_type, {})

            item = {
                "type": "node",
                # 用真实节点类型而非文件名：排序器的「节点是否在当前工作流」
                # 匹配、workflow_learning 的覆盖率统计都靠这个字段
                "node": node_type,
                "name": node_type,
                "card": card.stem,
                "content": content,
                "source": str(card).replace("\\", "/"),
                "category": meta.get("category", ""),
                "role": meta.get("role", ""),
                "difficulty": meta.get("difficulty", ""),
                "learning_topics": meta.get("learning_topics", []),
            }

            index.add_many(
                self.matcher.index_keywords_for_node(node_type), item
            )

    def _index_pattern_cards(
        self,
        index: KnowledgeIndex,
        knowledge_dir: str
    ) -> None:
        """
        索引 Pattern 卡
        """
        patterns_dir = Path(knowledge_dir) / "patterns"
        if not patterns_dir.exists():
            return

        for card in sorted(patterns_dir.glob("*.md")):
            try:
                with open(card, "r", encoding="utf-8-sig") as f:
                    content = f.read()
            except Exception as e:
                print(f"读取 Pattern 卡失败 {card}: {e}")
                continue

            keywords = [card.stem.replace("_", " "), card.stem]

            item = {
                "type": "workflow_pattern",
                "name": card.stem,
                "content": content,
                "source": str(card).replace("\\", "/"),
            }
            index.add_many(keywords, item)

            # Pattern 卡里出现的节点类型也挂上，方便按节点反查
            for node in self._nodes_mentioned_in(content):
                index.add_many(
                    self.matcher.index_keywords_for_node(node), item
                )

    def _nodes_mentioned_in(self, content: str) -> List[str]:
        """
        从文本中找出已知主题对应的节点类型

        只认主题表里登记过的节点名，避免把正文里随便一个 CamelCase 词当节点。
        """
        found = set()
        known_nodes = set()

        for config in self.matcher.TOPICS.values():
            known_nodes.update(config["nodes"])

        for node in known_nodes:
            if node in content:
                found.add(node)

        return sorted(found)

    def _index_experiences(
        self,
        index: KnowledgeIndex,
        experience_store: str
    ) -> None:
        """
        索引 learning_loop 的历史调整经验
        """
        path = Path(experience_store)
        if not path.exists():
            return

        try:
            with open(path, "r", encoding="utf-8-sig") as f:
                raw = json.load(f)
        except Exception as e:
            print(f"读取经验库失败: {e}")
            return

        for record in raw:
            change = record.get("change", {})
            params = change.get("parameter_changes", {})

            # 每个改动参数挂一条经验知识
            for param_name, param_change in params.items():
                new_value = param_change.get("new")
                old_value = param_change.get("old")

                name = f"{param_name} 调整经验"
                content = (
                    f"{param_name}: {old_value} → {new_value}\n"
                    f"观察: {record.get('observation', '')}\n"
                    f"结论: {record.get('conclusion', '')}"
                )

                keywords = [param_name, param_name.lower()]
                keywords.extend(record.get("tags", []))
                keywords.append(record.get("workflow_type", ""))

                # 参数名能反查到主题（cfg → KSampler）
                for topic in self.matcher.topics_for_node(param_name):
                    keywords.append(topic)

                item = {
                    "type": "experience",
                    "name": name,
                    "content": content,
                    "param": param_name,
                    "old_value": old_value,
                    "new_value": new_value,
                    "workflow_type": record.get("workflow_type", ""),
                    "tags": record.get("tags", []),
                    "source": str(path).replace("\\", "/"),
                }
                index.add_many(
                    [k for k in keywords if k], item
                )

    def _index_evolution(
        self,
        index: KnowledgeIndex,
        evolution_store: str
    ) -> None:
        """
        索引 knowledge_evolution 的演化知识
        """
        path = Path(evolution_store)
        if not path.exists():
            return

        try:
            with open(path, "r", encoding="utf-8-sig") as f:
                raw = json.load(f)
        except Exception as e:
            print(f"读取演化知识失败: {e}")
            return

        entries = raw.get("patterns", []) if isinstance(raw, dict) else raw

        for entry in entries:
            nodes = entry.get("common_nodes", []) or []
            tags = entry.get("tags", [])

            keywords = list(tags)
            keywords.append(entry.get("name", ""))
            keywords.append(entry.get("workflow_type", ""))

            for node in nodes:
                keywords.extend(self.matcher.index_keywords_for_node(node))

            item = {
                "type": "evolution_knowledge",
                "name": entry.get("name", ""),
                "content": entry.get("description", ""),
                "nodes": nodes,
                "frequency": entry.get("frequency", 0),
                "common_parameters": entry.get("common_parameters", {}),
                "recommendations": entry.get("recommendations", []),
                "tags": tags,
                "workflow_type": entry.get("workflow_type", ""),
                "source": str(path).replace("\\", "/"),
            }
            index.add_many([k for k in keywords if k], item)

    def stats(self) -> Dict:
        """
        索引统计
        """
        return {
            "keyword_count": len(self.base.keys()),
            "knowledge_count": self.base.size(),
            "keywords": sorted(self.base.keys()),
        }
