"""
模式挖掘器

把「节点清单各不相同」的一堆 workflow 聚成若干模式。

设计稿的做法是 `key = "_".join(sorted(nodes))` —— 要求节点集合**完全相等**
才归为同一模式。真实场景下这几乎不成立：

    workflow A: [Checkpoint, CLIP, KSampler, VAEDecode, SaveImage]
    workflow B: [Checkpoint, CLIP, KSampler, VAEDecode, SaveImage, Upscale]
    workflow C: [Checkpoint, CLIP, KSampler, VAEDecode, SaveImage, LoraLoader]

B 和 C 只是多了各自的特色节点，核心结构一样，但精确匹配下三个都是独立模式、
frequency 恒为 1，等于没归纳。

这里改成两步聚类：

    1. 先按 workflow_type 分组
       SD1.5 与 Wan 的 steps 差一个数量级，混在一起统计参数毫无意义。

    2. 组内按节点共现关系聚类
       逐个 workflow 找「已有模式里最像的那个」（Jaccard 相似度），
       达到阈值就加入，否则自立门户。
       Jaccard 对「多一个特色节点」这种差异不敏感 —— 这正是要的性质。

模式名也据此生成：以共有节点里的功能节点命名
（如 ControlNetApply + KSampler → `controlnet_sampler`），
而不是把全部节点用下划线拼起来（那是标识不是名字）。
"""

from collections import Counter
from typing import List, Dict, Any, Tuple

from .models import WorkflowPattern
from .experience_loader import ExperienceRow


# 功能节点关键词 → 命名用短名。
#
# 顺序即优先级：一个模式取最先命中的几个作为名字。
# 所以**专用词必须排在通用词前面** —— 否则 WanVideoSampler 会因为命中
# "sampler" 而被命名成 sampler，丢掉「视频」这个更有辨识度的信息。
FEATURE_HINTS = (
    # 专用管线（先判，它们最能说明"这类流程在干什么"）
    ("controlnet", "controlnet"),
    ("ipadapter", "ipadapter"),
    ("wanvideo", "video"),
    ("videocombine", "video"),
    ("img2img", "img2img"),
    ("inpaint", "inpaint"),
    ("upscale", "upscale"),
    ("latentupscale", "latent_upscale"),
    ("facedetailer", "face_detailer"),
    ("lora", "lora"),
    # 通用构件（放后面，仅在没有专用管线可判时使用）
    ("ksampler", "sampler"),
    ("sampler", "sampler"),
    ("cliptextencode", "clip"),
    ("checkpointloader", "checkpoint"),
    ("unetloader", "unet"),
    ("vae", "vae"),
)

# 参与相似度计算时忽略的节点：
# 它们不影响「工作流属于哪一类」，计入会把差异放大
IGNORED_NODES = {
    "Note",             # ComfyUI 便签，纯注释
    "PrimitiveNode",    # 类型转换占位
    "Reroute",          # 连线整理
    "MarkdownNote",
}


def jaccard(a: set, b: set) -> float:
    """
    Jaccard 相似度 = |交集| / |并集|

    取值 0-1。1 表示完全相同。

    Args:
        a: 集合 A
        b: 集合 B

    Returns:
        相似度
    """
    if not a and not b:
        return 1.0

    union = a | b
    if not union:
        return 0.0

    return len(a & b) / len(union)


class PatternMiner:
    """
    workflow 模式挖掘器
    """

    def __init__(
        self,
        similarity: float = 0.6,
        min_frequency: int = 2
    ) -> None:
        """
        初始化挖掘器

        Args:
            similarity: 归入已有模式的最低 Jaccard 相似度。
                         0.6 的含义：两个 workflow 六成节点重合即视为同类
            min_frequency: 模式最小成员数。低于此值视为个案不产出知识
        """
        self.similarity = similarity
        self.min_frequency = min_frequency

    def mine(
        self,
        experiences: List[ExperienceRow]
    ) -> List[WorkflowPattern]:
        """
        挖掘模式

        Args:
            experiences: 待归纳的 workflow 记录

        Returns:
            WorkflowPattern 列表（按成员数降序）
        """
        rows = [e for e in experiences if getattr(e, "nodes", None)]

        if not rows:
            return []

        # 按 workflow_type 分组：不同类型的参数不可混合统计
        by_type: Dict[str, List[ExperienceRow]] = {}
        for row in rows:
            by_type.setdefault(
                row.workflow_type or "未分类", []
            ).append(row)

        patterns: List[WorkflowPattern] = []

        for workflow_type, group in by_type.items():
            patterns.extend(self._mine_group(workflow_type, group))

        patterns.sort(key=lambda p: (-p.frequency, p.name))
        return patterns

    # ---------- 组内聚类 ----------

    def _mine_group(
        self,
        workflow_type: str,
        group: List[ExperienceRow]
    ) -> List[WorkflowPattern]:
        """
        单个类型内聚类
        """
        clusters: List[Dict] = []

        for row in group:
            node_set = set(self._significant_nodes(row.nodes))

            if not node_set:
                continue

            best = None
            best_score = 0.0

            for cluster in clusters:
                score = jaccard(node_set, cluster["node_set"])
                if score > best_score:
                    best_score = score
                    best = cluster

            if best is not None and best_score >= self.similarity:
                best["members"].append(row)
                best["node_set"] = best["node_set"] | node_set
            else:
                clusters.append({
                    "members": [row],
                    "node_set": set(node_set),
                })

        patterns = []
        for cluster in clusters:
            pattern = self._build_pattern(workflow_type, cluster)
            if pattern.frequency >= self.min_frequency:
                patterns.append(pattern)

        return patterns

    def _build_pattern(
        self,
        workflow_type: str,
        cluster: Dict
    ) -> WorkflowPattern:
        """
        把一个聚类整理成 WorkflowPattern

        参数统计留空，由 ParameterStatistics 按模式分组后填 ——
        这里不做统计是为了职责单一，也避免全量数据先混后分。
        """
        members: List[ExperienceRow] = cluster["members"]

        # 共有节点：出现在**全部**成员里
        node_sets = [
            set(self._significant_nodes(m.nodes)) for m in members
        ]
        common = set.intersection(*node_sets) if node_sets else set()
        union = set.union(*node_sets) if node_sets else set()

        # 出现但不齐全的节点 = 该模式的「可变部分」
        variable = {
            node: sum(1 for s in node_sets if node in s)
            for node in sorted(union - common)
        }

        # 缺卡节点取并集去重
        missing: List[str] = []
        for member in members:
            for node in member.missing_nodes:
                if node not in missing:
                    missing.append(node)

        coverages = [m.coverage for m in members if m.coverage]

        return WorkflowPattern(
            name=self._pattern_name(workflow_type, common, union),
            workflow_type=workflow_type,
            frequency=len(members),
            common_nodes=sorted(common),
            all_nodes=sorted(union),
            variable_nodes=variable,
            missing_nodes=missing,
            members=[m.key for m in members],
            coverage=(
                sum(coverages) / len(coverages) if coverages else 0.0
            ),
        )

    # ---------- 命名 ----------

    def _pattern_name(
        self,
        workflow_type: str,
        common: set,
        union: set
    ) -> str:
        """
        生成可读的模式名

        以共有节点里的功能特征命名。若共有节点没有特征词
        （如只剩 VAEDecode / SaveImage 这类管线节点），
        退回到 workflow_type + 成员数。
        """
        # 特征词可能在共有节点里，也可能只在并集里（有一个成员缺）
        # 优先用共有的，避免名不副实
        hints = []
        for keyword, short in FEATURE_HINTS:
            if any(keyword in n.lower() for n in common):
                hints.append(short)

        if not hints:
            for keyword, short in FEATURE_HINTS:
                if any(keyword in n.lower() for n in union):
                    hints.append(short)

        # 去重保序，最多取 3 个
        unique = list(dict.fromkeys(hints))[:3]

        if unique:
            suffix = "_".join(unique)
            type_part = self._type_slug(workflow_type)
            return f"{type_part}_{suffix}" if type_part else suffix

        type_part = self._type_slug(workflow_type) or "pattern"
        return f"{type_part}_generic"

    @staticmethod
    def _type_slug(workflow_type: str) -> str:
        """
        workflow_type 转 slug

        "Text To Image" → "text_to_image"；"SDXL Portrait" → "sdxl_portrait"
        """
        if not workflow_type or workflow_type.lower() == "未分类":
            return ""

        cleaned = "".join(
            ch.lower() if ch.isalnum() else "_"
            for ch in workflow_type
        )
        return "_".join(part for part in cleaned.split("_") if part)

    @staticmethod
    def _significant_nodes(nodes: List[str]) -> List[str]:
        """
        滤掉不影响分类的节点

        Note / MarkdownNote 这类注释节点如果计入会稀释相似度：
        两个结构完全相同的 workflow，只因一个有便签就被拆成两个模式。
        """
        return [
            n for n in nodes
            if n and n not in IGNORED_NODES
        ]

    # ---------- 全局观察 ----------

    def global_observations(
        self,
        experiences: List[ExperienceRow]
    ) -> List[str]:
        """
        全局层面的观察

        比模式更粗的结论：哪些节点几乎每个 workflow 都有
        （说明是该领域的必备链路），哪些很少出现（说明是少数派用法）。
        """
        rows = [e for e in experiences if getattr(e, "nodes", None)]

        if len(rows) < 2:
            return []

        counter: Counter = Counter()
        for row in rows:
            for node in set(self._significant_nodes(row.nodes)):
                counter[node] += 1

        total = len(rows)
        observations = []

        # 必备节点：出现在 80% 以上
        essential = [
            node for node, count in counter.items()
            if count / total >= 0.8
        ]
        if essential:
            observations.append(
                f"必备节点（出现在 ≥80% 的 workflow，{total} 个样本）："
                + "、".join(sorted(essential))
            )

        # 少数派：出现过但不足 20%
        rare = [
            node for node, count in counter.items()
            if count / total < 0.2
        ]
        if rare:
            observations.append(
                f"少数派节点（出现率 <20%）：" + "、".join(sorted(rare))
            )

        # 类型分布
        types = Counter(r.workflow_type or "未分类" for r in rows)
        if len(types) > 1:
            observations.append(
                "workflow 类型分布："
                + "、".join(
                    f"{t} {c} 个" for t, c in types.most_common()
                )
            )

        return observations
