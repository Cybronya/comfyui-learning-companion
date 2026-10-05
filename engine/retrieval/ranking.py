"""
知识排序器

检索会召回多个候选知识，需要决定「先给 Agent 看哪条」。

排序权重（分高在前）：
    +10  条目关联的节点出现在当前 workflow 里 —— 用户的当前工作流就是最强上下文信号
    +5   来自演化知识（workflow_pattern / evolution_knowledge）—— 由多条经验统计得出，
         比单条静态知识卡更可信
    +3   来自历史经验（experience）
    +2   条目主题是问题所描述症状的候选成因（如「脸崩」→ KSampler / LoRA / VAE）
    +2   主题与问题直接字面命中
    +1   条目有 learning_topics 与问题关键词交集
    -5   风险条目降权：需要提示但不该抢在解释性知识之前
"""

from typing import List, Dict


# 视为「高可信度」的类型，排序时加权
TRUSTED_TYPES = {
    "evolution_knowledge": 5,
    "workflow_pattern": 5,
    "experience": 3,
    "node": 2,
    "diagnostic": 1,
}


# 主题 -> 该主题的代表性节点类名片段。用于反推条目所属主题。
TOPIC_NODE_HINTS = {
    "ControlNet": ["controlnet"],
    "KSampler": ["ksampler", "sampler"],
    "VAE": ["vae", "latent", "decode", "encode"],
    "LoRA": ["lora"],
    "Checkpoint": ["checkpoint", "unet", "ckpt"],
    "IPAdapter": ["ipadapter", "clipvision"],
    "Upscale": ["upscale"],
    "CLIPTextEncode": ["cliptextencode", "clip"],
    "Resolution": ["latentimage", "empty"],
    "SaveImage": ["saveimage", "previewimage"],
}


# 症状 -> 可能成因主题。同一症状常有多个成因，必须跨主题召回，
# 否则「为什么脸崩」只会召回 KSampler，而漏掉 LoRA 权重过高、VAE 解码异常。
SYMPTOM_TOPICS = {
    "脸崩": ["KSampler", "LoRA", "VAE"],
    "脸部异常": ["KSampler", "LoRA", "VAE"],
    "不自然": ["ControlNet", "KSampler"],
    "僵硬": ["ControlNet", "KSampler"],
    "过曝": ["KSampler", "VAE"],
    "色偏": ["VAE", "Checkpoint"],
    "细节差": ["KSampler", "Upscale"],
}


def _first_symptom(lowered_question: str, topic: str) -> str:
    """
    找出该条目对应的症状词（用于生成可读的命中原因）
    """
    for symptom, candidates in SYMPTOM_TOPICS.items():
        if symptom.lower() in lowered_question and topic in candidates:
            return symptom
    return topic


class KnowledgeRanker:
    """
    检索结果排序器
    """

    # 症状 -> 可能成因主题表定义在模块级（见 SYMPTOM_TOPICS），
    # 排序与召回两处共用，避免两处各写一份导致不一致。
    def symptom_topics(self, lowered_question: str) -> List[str]:
        """
        从问题中提取症状对应的候选成因主题

        Args:
            lowered_question: 已转小写的问题文本

        Returns:
            候选主题列表
        """
        topics = []

        for symptom, candidates in SYMPTOM_TOPICS.items():
            if symptom.lower() in lowered_question:
                for topic in candidates:
                    if topic not in topics:
                        topics.append(topic)

        return topics

    @staticmethod
    def topics_for_item(item: Dict) -> List[str]:
        """
        推断条目所属主题

        Args:
            item: 知识条目

        Returns:
            主题列表
        """
        haystack = " ".join([
            str(item.get("node", "")),
            str(item.get("name", "")),
        ]).lower()

        topics = []
        for topic, hints in TOPIC_NODE_HINTS.items():
            if any(hint in haystack for hint in hints):
                topics.append(topic)

        return topics

    def rank(
        self,
        items: List[Dict],
        context: Dict = None,
        question: str = ""
    ) -> List[Dict]:
        """
        对候选知识排序

        Args:
            items: 候选知识条目
            context: 上下文，含 workflow_nodes / workflow_type / parameters
            question: 原始问题，用于字面命中加权

        Returns:
            排序后的知识列表（同分保持原顺序，稳定排序）
        """
        if not items:
            return []

        if context is None:
            context = {}

        workflow_nodes = context.get("workflow_nodes", []) or []
        # 节点名大小写不一致很常见（ControlNetApply vs controlnetapply），统一小写比较
        node_pool = {str(n).lower() for n in workflow_nodes}
        lowered_question = (question or "").lower()

        # 症状词（如"脸崩"）成因不止一个，先扩展候选主题再匹配，
        # 否则只召回 KSampler 而漏掉 LoRA 权重过高、VAE 解码异常等可能原因。
        symptom_topics = self.symptom_topics(lowered_question)

        scored = []

        for position, item in enumerate(items):
            score = 0.0
            reasons = []

            # 1. 节点是否在当前 workflow 中出现
            item_node = str(item.get("node", "")).lower()
            if item_node and item_node in node_pool:
                score += 10
                reasons.append("当前工作流包含该节点")

            # 2. 条目自身也可能是节点列表（pattern 类知识）
            for node in item.get("nodes", []) or []:
                if str(node).lower() in node_pool:
                    score += 10
                    reasons.append("当前工作流命中模式节点")
                    break

            # 3. 类型可信度加权
            item_type = item.get("type", "")
            if item_type in TRUSTED_TYPES:
                score += TRUSTED_TYPES[item_type]

            # 4. 字面命中
            item_name = str(item.get("name", "")).lower()
            if item_name and item_name in lowered_question:
                score += 2
                reasons.append("名称与问题字面匹配")

            # 5. learning_topics 交集
            topics = item.get("learning_topics", []) or []
            for topic in topics:
                if str(topic).lower() in lowered_question:
                    score += 1
                    break

            # 6. 症状候选成因：条目主题命中症状成因表则加权
            item_topics = item.get("topics", []) or self.topics_for_item(item)
            for topic in item_topics:
                if topic in symptom_topics:
                    score += 2
                    reasons.append(
                        f"可能是「{_first_symptom(lowered_question, topic)}」的成因"
                    )
                    break

            # 7. 风险条目降权
            if item.get("is_risk") or "风险" in item_name:
                score -= 5

            # 同分时按原始顺序稳定排列
            scored.append((score, position, item, reasons))

        scored.sort(key=lambda x: (-x[0], x[1]))

        # 附上打分理由，供 response_generator 说明「为什么这条排前面」
        ranked = []
        for score, _, item, reasons in scored:
            enriched = dict(item)
            enriched["score"] = score
            if reasons:
                enriched["match_reasons"] = reasons
            ranked.append(enriched)

        return ranked

    def top(self, items: List[Dict], context: Dict = None,
            question: str = "", limit: int = 3) -> List[Dict]:
        """
        排序并取前 N 条

        Args:
            items: 候选知识
            context: 上下文
            question: 原始问题
            limit: 保留条数

        Returns:
            排序后的前 N 条
        """
        return self.rank(items, context, question)[:limit]
