"""
知识存储

归纳结果落盘。

格式沿用 `workflow_learning` 那套约定：**Markdown + frontmatter**。
理由与学习记录一致 ——

    1. Agent 直接可读可 grep：
       `grep -rl "ControlNet 权重" comfyui_library/knowledge/patterns/`
    2. git diff 可读，不会整块变更
    3. 与知识卡（comfyui_library/knowledge/**/*.md）格式统一

一个模式一个文件：

    comfyui_library/knowledge/patterns/_consolidated/<pattern>.md

frontmatter 放机器查的字段（frequency / common_nodes / parameter_stats），
正文放人读的部分（典型参数 / 常见问题 / 建议）。
"""

from pathlib import Path
from typing import List, Dict, Any, Optional

from ..workflow_learning.markdown_format import (
    build_frontmatter,
    split_frontmatter,
    parse_frontmatter,
)
from ..workflow_learning.paths import relative_to_project
from .models import (
    ConsolidatedKnowledge,
    WorkflowPattern,
    ParameterStat,
    LEVEL_STRONG,
    LEVEL_MODERATE,
    LEVEL_WEAK,
)


# 归纳产物的存放位置：与手写 Pattern 卡同目录，但用 _ 前缀子目录区分
# （_ 前缀是仓库里约定的「非人工维护产物」标记）
DEFAULT_FOLDER = "comfyui_library/knowledge/patterns/_consolidated"

LEVEL_LABEL = {
    LEVEL_STRONG: "强结论",
    LEVEL_MODERATE: "中等可信",
    LEVEL_WEAK: "弱结论（样本不足）",
}


class KnowledgeStore:
    """
    归纳知识存储
    """

    def __init__(self, path: str = None) -> None:
        """
        初始化存储

        Args:
            path: 输出目录；None 时用默认
                  comfyui_library/knowledge/patterns/_consolidated/
        """
        self.folder = Path(path) if path else Path(DEFAULT_FOLDER)
        self.index_path = self.folder / "index.md"

    # ---------- 写 ----------

    def save(self, knowledge: ConsolidatedKnowledge) -> str:
        """
        保存归纳结果（全量覆盖）

        归纳是全量重算的，覆盖比追加准确 ——
        否则同一个模式在多次归纳后会堆出多条重复记录。

        Args:
            knowledge: 归纳结果

        Returns:
            索引文件路径；失败返回空串
        """
        try:
            self.folder.mkdir(parents=True, exist_ok=True)

            self._clear_records()

            for pattern in knowledge.patterns:
                self._write_pattern(pattern)

            self.index_path.write_text(
                self._render_index(knowledge), encoding="utf-8"
            )

            return str(self.index_path)
        except Exception as e:
            print(f"保存归纳知识失败: {e}")
            return ""

    def _clear_records(self) -> None:
        """
        清掉旧记录（保留 README）
        """
        for path in self.folder.glob("*.md"):
            if path.name in ("index.md", "README.md"):
                continue
            try:
                path.unlink()
            except OSError:
                pass

    def _write_pattern(self, pattern: WorkflowPattern) -> Path:
        """
        写一个模式的记录
        """
        path = self.folder / f"{pattern.name}.md"
        path.write_text(self.render_pattern(pattern), encoding="utf-8")
        return path

    # ---------- 渲染 ----------

    def render_pattern(self, pattern: WorkflowPattern) -> str:
        """
        渲染单个模式为 Markdown
        """
        front = build_frontmatter({
            "name": pattern.name,
            "type": pattern.workflow_type,
            "frequency": pattern.frequency,
            "level": pattern.level,
            "coverage": pattern.coverage,
            "common_nodes": pattern.common_nodes,
            # parameter_stats 不进 frontmatter：它是嵌套 dict，
            # 行内列表格式表达不了，塞进去会被 str() 成 Python 字面量。
            # 统计值只存在正文的「典型参数」表里，需要时从正文解析回来。
            "problems": [
                p["problem"] for p in pattern.common_problems
            ],
            "missing": pattern.missing_nodes,
            "members": pattern.members,
            "source": "knowledge_consolidation",
        })

        body = self._render_body(pattern)

        return front + "\n" + body

    def _render_body(self, pattern: WorkflowPattern) -> str:
        """
        正文（人读部分）
        """
        sections = []

        header = [
            f"# {pattern.name}",
            "",
            f"> 由 `engine/knowledge_consolidation` 从 "
            f"{pattern.frequency} 个 workflow 归纳得出"
            f"（{'、'.join(pattern.members[:5])}"
            + ("…" if len(pattern.members) > 5 else "")
            + "）",
            "",
            f"- **类型**：{pattern.workflow_type or '未分类'}",
            f"- **样本数**：{pattern.frequency}",
            f"- **可信度**：{LEVEL_LABEL.get(pattern.level, pattern.level)}",
            f"- **平均知识覆盖**：{pattern.coverage:.0%}",
        ]
        sections.append("\n".join(header))

        # ---- 共有节点 ----
        nodes = ["## 共有节点", ""]
        if pattern.common_nodes:
            nodes.append(
                f"全部 {pattern.frequency} 个 workflow 都包含："
            )
            for node in pattern.common_nodes:
                nodes.append(f"- `{node}`")
        else:
            nodes.append("无（成员之间没有完全共有的节点）")

        if pattern.variable_nodes:
            nodes.append("")
            nodes.append("**可变部分**（部分 workflow 才有）：")
            for node, count in sorted(
                pattern.variable_nodes.items(),
                key=lambda kv: (-kv[1], kv[0]),
            ):
                nodes.append(
                    f"- `{node}` —— {count}/{pattern.frequency} 个有"
                )
        sections.append("\n".join(nodes))

        # ---- 典型参数 ----
        params = ["## 典型参数", ""]
        if pattern.parameter_stats:
            params.append("| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |")
            params.append("|---|---|---|---|---|")
            for name, stat in pattern.parameter_stats.items():
                params.append(
                    f"| {self._label(name)} "
                    f"| {self._center(stat)} "
                    f"| {self._range(stat)} "
                    f"| {stat.count} "
                    f"| {stat.consistency:.0%} |"
                )
        else:
            params.append("无可统计的参数。")
        sections.append("\n".join(params))

        # ---- 常见问题 ----
        problems = ["## 常见问题", ""]
        if pattern.common_problems:
            problems.append("| 问题 | 出现次数 | 严重度 | 示例 |")
            problems.append("|---|---|---|---|")
            for item in pattern.common_problems:
                sample = (item["samples"][0] if item["samples"] else "")
                if len(sample) > 60:
                    sample = sample[:60] + "…"
                problems.append(
                    f"| {item['problem']} "
                    f"| {item['count']}/{pattern.frequency} "
                    f"| {item['severity']} "
                    f"| {sample} |"
                )
        else:
            problems.append("参数体检未发现问题。")
        sections.append("\n".join(problems))

        # ---- 建议 ----
        if pattern.recommendations:
            recs = ["## 建议与风险", ""]
            recs.extend(f"- {r}" for r in pattern.recommendations)
            sections.append("\n".join(recs))

        return "\n\n".join(sections).rstrip() + "\n"

    def _render_index(self, knowledge: ConsolidatedKnowledge) -> str:
        """
        渲染汇总索引
        """
        lines = [
            "# 归纳出的 Workflow 模式",
            "",
            "> 本目录由 `engine/knowledge_consolidation` 自动生成，勿手改。",
            "> 每个模式一个 Markdown 文件，frontmatter 存统计字段，"
            "正文存结论。",
            "",
            "| 模式 | 类型 | 样本 | 可信度 | 覆盖 |",
            "|---|---|---|---|---|",
        ]

        for pattern in knowledge.patterns:
            lines.append(
                f"| [`{pattern.name}`]({pattern.name}.md) "
                f"| {pattern.workflow_type or '未分类'} "
                f"| {pattern.frequency} "
                f"| {LEVEL_LABEL.get(pattern.level, pattern.level)} "
                f"| {pattern.coverage:.0%} |"
            )

        if knowledge.global_observations:
            lines.extend(["", "## 全局观察", ""])
            lines.extend(
                f"- {item}" for item in knowledge.global_observations
            )

        lines.extend([
            "",
            "---",
            "",
            f"归纳自 {knowledge.source_count} 个 workflow，"
            f"形成 {len(knowledge.patterns)} 个模式"
            + (
                f"，{knowledge.ungrouped} 个样本量不足未成模式"
                if knowledge.ungrouped else ""
            ),
            f"，生成时间 {knowledge.generated_at}",
            "",
        ])

        return "\n".join(lines)

    # ---------- 读 ----------

    def load_all(self) -> List[WorkflowPattern]:
        """
        读回全部模式（供检索层使用）
        """
        if not self.folder.exists():
            return []

        patterns = []

        for path in sorted(self.folder.glob("*.md")):
            if path.name in ("index.md", "README.md"):
                continue

            try:
                patterns.append(self.load(path))
            except Exception:
                continue

        return patterns

    def load(self, path: Path) -> WorkflowPattern:
        """
        读一个模式文件
        """
        front, _body = split_frontmatter(
            path.read_text(encoding="utf-8-sig")
        )
        data = parse_frontmatter(front)

        stats = self._stats_from_body(
            path.read_text(encoding="utf-8-sig")
        )

        return WorkflowPattern(
            name=data.get("name", path.stem),
            workflow_type=data.get("type", ""),
            frequency=int(data.get("frequency", 0) or 0),
            common_nodes=_as_list(data.get("common_nodes")),
            all_nodes=_as_list(data.get("common_nodes")),
            variable_nodes={},
            parameter_stats=stats,
            missing_nodes=_as_list(data.get("missing")),
            members=_as_list(data.get("members")),
            level=data.get("level", LEVEL_WEAK),
            coverage=float(data.get("coverage", 0) or 0),
        )

    @staticmethod
    def _stats_from_body(text: str) -> Dict[str, ParameterStat]:
        """
        从正文的参数表格重建统计

        嵌套结构在 frontmatter 的行内列表格式里表达不了
        （值本身是 dict），所以参数表只存在于正文，
        需要时从这里解析回来。
        """
        stats: Dict[str, ParameterStat] = {}

        for line in text.split("\n"):
            if not line.startswith("| ") or "---" in line:
                continue

            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 4:
                continue

            label = cells[0].strip("`")
            center = cells[1].strip("`")
            range_text = cells[2]
            count_text = cells[3]

            if not count_text.isdigit():
                continue

            name = KnowledgeStore._name_from_label(label)

            numeric = _to_number(center) or _to_number(
                range_text.split(" - ")[0]
            )

            stats[name] = ParameterStat(
                count=int(count_text),
                median=numeric,
                mean=numeric,
                most_common=(
                    None if numeric is not None else center
                ),
                values=[],
            )

        return stats

    @staticmethod
    def _name_from_label(label: str) -> str:
        """
        中文标签转回参数名
        """
        mapping = {
            "Prompt 约束强度(CFG)": "cfg",
            "采样步数": "steps",
            "重绘幅度": "denoise",
            "采样算法": "sampler_name",
            "调度器": "scheduler",
            "宽度": "width",
            "高度": "height",
            "ControlNet 权重": "controlnet_strength",
            "LoRA 模型强度": "strength_model",
            "LoRA 文本强度": "strength_clip",
        }
        return mapping.get(label, label)

    @staticmethod
    def _label(name: str) -> str:
        return KnowledgeBuilder_label(name)

    @staticmethod
    def _center(stat: ParameterStat) -> str:
        if stat.is_numeric:
            return f"{stat.median:g}"
        return str(stat.most_common or "-")

    @staticmethod
    def _range(stat: ParameterStat) -> str:
        if stat.is_numeric:
            return stat.typical_range or "-"
        return "-"

    def folder_relative(self) -> str:
        """
        输出目录（相对仓库根）
        """
        return relative_to_project(self.folder)


def KnowledgeBuilder_label(name: str) -> str:
    """
    参数名转中文（与 KnowledgeBuilder._param_label 保持一致）
    """
    return {
        "cfg": "Prompt 约束强度(CFG)",
        "steps": "采样步数",
        "denoise": "重绘幅度",
        "sampler_name": "采样算法",
        "scheduler": "调度器",
        "width": "宽度",
        "height": "高度",
        "controlnet_strength": "ControlNet 权重",
        "strength_model": "LoRA 模型强度",
        "strength_clip": "LoRA 文本强度",
    }.get(name, name)


def _to_number(text: str):
    """
    尝试把文本转成数字
    """
    text = str(text).strip().strip("`")
    try:
        value = float(text)
    except ValueError:
        return None
    return int(value) if value.is_integer() else value


def _as_list(value: Any) -> List[str]:
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [str(v) for v in value]
    text = str(value).strip()
    if not text:
        return []
    return [item.strip() for item in text.split(",") if item.strip()]
