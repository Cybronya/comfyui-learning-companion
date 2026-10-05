"""
归纳引擎（统一入口）

    学习记录（workflows/learning/*.md）
        ↓  ExperienceLoader
    ExperienceRow 列表
        ↓  PatternMiner        按 workflow_type 分组 + Jaccard 聚类
    WorkflowPattern 列表
        ↓  ParameterStatistics 逐模式统计（不跨模式混合）
    WorkflowPattern（含参数统计）
        ↓  KnowledgeBuilder    聚合常见问题 + 生成建议 + 跨模式对比
    ConsolidatedKnowledge
        ↓  KnowledgeStore      写 Markdown + index.md

关于与 knowledge_evolution 的关系（两者并存，不是重复）：
    knowledge_evolution      从 learning_loop 的「参数改动记录」归纳，
                            回答「改这个参数会怎样」
    knowledge_consolidation  从「完整 workflow」归纳，
                            回答「这类 workflow 长什么样、常用什么参数、
                            容易踩什么坑」
    两者数据源不同、产出也不同，未来可互相引用
"""

from datetime import datetime
from typing import List, Dict, Optional

from .models import ConsolidatedKnowledge, WorkflowPattern
from .experience_loader import ExperienceLoader, ExperienceRow
from .pattern_miner import PatternMiner
from .parameter_statistics import ParameterStatistics
from .knowledge_builder import KnowledgeBuilder
from .knowledge_store import KnowledgeStore


class ConsolidationEngine:
    """
    知识归纳引擎
    """

    def __init__(
        self,
        loader=None,
        miner=None,
        statistic=None,
        builder=None,
        store=None,
        similarity: float = 0.6,
        min_frequency: int = 2,
        database=None
    ) -> None:
        """
        初始化引擎

        Args:
            loader: ExperienceLoader
            miner: PatternMiner
            statistic: ParameterStatistics
            builder: KnowledgeBuilder
            store: KnowledgeStore
            similarity: 聚类相似度阈值
            min_frequency: 模式最小成员数
            database: WorkflowDatabase。传入则归纳出的模式写回
                     patterns（供 pattern_index 与 workflow.patterns 查询）
        """
        self.loader = loader or ExperienceLoader()
        self.miner = miner or PatternMiner(
            similarity=similarity, min_frequency=min_frequency
        )
        self.statistic = statistic or ParameterStatistics()
        self.builder = builder or KnowledgeBuilder()
        self.store = store or KnowledgeStore()
        self.database = database

    def consolidate(
        self,
        experiences: List[ExperienceRow] = None,
        store_path: str = None,
        save: bool = True
    ) -> ConsolidatedKnowledge:
        """
        执行一次归纳

        Args:
            experiences: 待归纳的记录；None 时从学习记录目录读取。
                         兼容设计稿里的「传经验文件路径」用法。
            store_path: 输出目录；None 时用默认
            save: 是否写入 Markdown

        Returns:
            ConsolidatedKnowledge
        """
        # 兼容：传入字符串路径时按「从学习记录读取」处理
        if isinstance(experiences, str):
            experiences = None

        rows = (
            experiences if experiences is not None
            else self.loader.load()
        )

        knowledge = ConsolidatedKnowledge(
            source_count=len(rows),
            generated_at=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        )

        if not rows:
            print(
                "没有可归纳的学习记录 —— 先运行 "
                "workflow_learning 的 learn_folder()"
            )
            return knowledge

        # ① 聚类
        patterns = self.miner.mine(rows)
        clustered = sum(p.frequency for p in patterns)
        knowledge.ungrouped = len(rows) - clustered

        # ② 按模式分组，供参数统计与问题聚合使用
        rows_by_key = {r.key: r for r in rows}
        grouped: Dict[str, List[ExperienceRow]] = {}

        for pattern in patterns:
            members = [
                rows_by_key[k] for k in pattern.members
                if k in rows_by_key
            ]
            grouped[pattern.name] = members

        # ③ 组装知识（内含逐模式参数统计、常见问题聚合、建议）
        built = self.builder.build(patterns, grouped)
        knowledge.patterns = built.patterns

        # ③' 模式写回数据库（不传 database 时跳过）
        if self.database is not None:
            self._deposit_patterns(built.patterns)

        # ④ 全局观察 + 跨模式对比
        knowledge.global_observations.extend(
            self.miner.global_observations(rows)
        )
        self.builder.cross_pattern_notes(knowledge, grouped)

        # ⑤ 落盘
        if save:
            store = (
                KnowledgeStore(store_path)
                if store_path else self.store
            )
            store.save(knowledge)

        return knowledge

    def _deposit_patterns(self, patterns) -> None:
        """
        归纳出的模式写回 WorkflowDatabase.patterns

        闭环的最后一环：学习 → 库 → 归纳 → 写回库。
        PatternRepository.add 会同步回填 workflow.patterns，
        IndexManager 的 pattern_index 也随之一致。幂等：同名覆盖。
        """
        try:
            for pattern in patterns:
                description = (
                    f"{pattern.workflow_type or '未分类'} · "
                    f"{pattern.frequency} 个样本 · {pattern.level}"
                )
                if pattern.recommendations:
                    description += (
                        "；" + pattern.recommendations[0]
                    )
                self.database.patterns.add(
                    pattern.name,
                    pattern.members,
                    description=description,
                )
            print(
                f"已把 {len(patterns)} 个模式写回数据库"
                "（comfyui_library.database）"
            )
        except Exception as e:
            # 写回失败不影响归纳产出本身
            print(f"模式写回数据库失败: {e}")

    # ---------- 报告 ----------

    def render_report(self, knowledge: ConsolidatedKnowledge) -> str:
        """
        渲染控制台摘要
        """
        if not knowledge.patterns:
            return (
                f"没有形成模式（样本 {knowledge.source_count} 个，"
                f"可能都不足最小成员数）"
            )

        lines = [
            f"归纳自 {knowledge.source_count} 个 workflow，"
            f"形成 {len(knowledge.patterns)} 个模式：",
        ]

        for pattern in knowledge.patterns:
            lines.append("")
            lines.append(
                f"【{pattern.name}】{pattern.workflow_type} "
                f"· {pattern.frequency} 个样本"
            )
            if pattern.common_nodes:
                lines.append(
                    "  共有节点：" + "、".join(pattern.common_nodes[:8])
                )
            for rec in pattern.recommendations[:3]:
                lines.append(f"  - {rec}")

        if knowledge.global_observations:
            lines.append("")
            lines.append("全局观察：")
            lines.extend(
                f"  - {obs}" for obs in knowledge.global_observations
            )

        return "\n".join(lines)
