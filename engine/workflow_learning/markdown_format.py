"""
学习记录 ↔ Markdown

一个 workflow 一个 Markdown 文件，frontmatter 存元数据、正文存学到的内容。

    ---
    key: sd1.5/basic.json
    name: basic
    type: Text To Image
    status: completed
    hash: a95cceecfb5d5225
    coverage: 1.0
    learned_at: 2026-10-06T01:12:39
    nodes: [CheckpointLoaderSimple, CLIPTextEncode, KSampler]
    missing: []
    ---

    # sd1.5/basic

    > 来源 comfyui_library/workflows/sd1.5/basic.json

    ## 生成流程
    ...

frontmatter 只用标准库解析，支持两种写法（本项目实际用到的）：
    key: value
    key: [a, b, c]              ← 列表用行内形式，避免引入块状列表解析

不引入 PyYAML —— 项目约定只用标准库，且这里的字段集是封闭的，
不需要完整的 YAML 语法。
"""

import json
import re
from typing import List, Dict, Any

from .learning_record import LearningRecord


# frontmatter 分隔符
DELIMITER = "---"

# 行内列表：[a, b, "c d"]
_INLINE_LIST = re.compile(r"^\[(.*)\]$")


class FrontmatterError(Exception):
    """
    frontmatter 格式错误
    """


def split_frontmatter(text: str):
    """
    拆出 frontmatter 与正文

    Args:
        text: 完整 Markdown 文本

    Returns:
        (frontmatter 文本, 正文)；无 frontmatter 时返回 ("", 原文)
    """
    stripped = text.lstrip("\ufeff")

    if not stripped.startswith(DELIMITER):
        return "", text

    lines = stripped.split("\n")
    if lines[0].strip() != DELIMITER:
        return "", text

    for i in range(1, len(lines)):
        if lines[i].strip() == DELIMITER:
            return (
                "\n".join(lines[1:i]),
                "\n".join(lines[i + 1:]),
            )

    # 没有闭合分隔符：视为无 frontmatter，而不是静默吞掉内容
    return "", text


def _split_inline_list(inner: str) -> List[str]:
    """
    拆行内列表，正确处理带引号的元素

    诊断结论这类自由文本里可能含半角逗号（如「CFG 值较高，建议 7-10, 或更低」），
    直接按逗号切会把一个元素劈成两个。含逗号的元素在序列化时会被加引号，
    这里按引号边界切。

    Args:
        inner: 方括号内的内容

    Returns:
        元素列表
    """
    items: List[str] = []
    current: List[str] = []
    quote = None
    i = 0
    length = len(inner)

    while i < length:
        ch = inner[i]

        if quote:
            if ch == "\\" and i + 1 < length:
                # 转义序列：下一个字符按字面处理，跳过反斜杠本身
                current.append(inner[i + 1])
                i += 2
                continue
            if ch == quote:
                quote = None
            else:
                current.append(ch)
        else:
            if ch in ("'", '"'):
                quote = ch
            elif ch == ",":
                items.append("".join(current).strip())
                current = []
            else:
                current.append(ch)

        i += 1

    tail = "".join(current).strip()
    if tail:
        items.append(tail)

    return [item for item in items if item]


def parse_frontmatter(front: str) -> Dict[str, Any]:
    """
    解析 frontmatter

    Args:
        front: frontmatter 文本（不含 --- 分隔符）

    Returns:
        {键: 值}；列表值返回 list，其余返回 str
    """
    result: Dict[str, Any] = {}

    for line in front.split("\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        if ":" not in line:
            continue

        key, _, raw = line.partition(":")
        key = key.strip()
        raw = raw.strip()

        match = _INLINE_LIST.match(raw)
        if match:
            result[key] = _split_inline_list(match.group(1))
        elif raw.startswith("{") and raw.endswith("}"):
            # 行内 JSON：dict 值（如 parameters）。JSON 自带定界，
            # 逗号 / 引号 / 冒号都不会像行内列表那样切错
            try:
                result[key] = json.loads(raw)
            except ValueError:
                result[key] = raw
        elif raw == "":
            result[key] = ""
        else:
            result[key] = raw.strip("'\"")

    return result


def _quote_item(value: Any) -> str:
    """
    序列化列表元素

    含逗号或引号的文本必须加引号保护，否则读回时会被切错。
    引号选文本里没出现的那种；两种都出现时用反斜杠转义外层引号。
    """
    text = str(value)

    if "," not in text and '"' not in text and "'" not in text:
        return text

    if '"' not in text:
        return f'"{text}"'

    if "'" not in text:
        return f"'{text}'"

    escaped = text.replace("'", "\\'")
    return f'"{escaped}"'

def build_frontmatter(data: Dict[str, Any]) -> str:
    """
    序列化 frontmatter

    Args:
        data: {键: 值}

    Returns:
        含分隔符的 frontmatter 文本
    """
    lines = [DELIMITER]

    for key, value in data.items():
        if value is None:
            continue

        if isinstance(value, (list, tuple)):
            # 含逗号或引号的元素加引号，否则读回时会被切错
            rendered = [_quote_item(item) for item in value]
            lines.append(f"{key}: [{', '.join(rendered)}]")
        elif isinstance(value, dict):
            # 行内 JSON，sort_keys 保稳定（git diff 干净）
            lines.append(
                f"{key}: "
                + json.dumps(value, ensure_ascii=False, sort_keys=True)
            )
        elif isinstance(value, bool):
            lines.append(f"{key}: {str(value).lower()}")
        elif isinstance(value, float):
            # 1.0 写成 1.0，0.778 不写成 0.7780000001
            lines.append(f"{key}: {value:g}")
        else:
            lines.append(f"{key}: {value}")

    lines.append(DELIMITER)
    lines.append("")

    return "\n".join(lines)


def to_markdown(record: LearningRecord) -> str:
    """
    学习记录 → Markdown

    frontmatter 放机器查询需要的字段，正文放人读的内容。

    Args:
        record: 学习记录

    Returns:
        完整 Markdown 文本
    """
    front = build_frontmatter({
        "key": record.key,
        "name": record.workflow_name,
        "type": record.workflow_type,
        "status": record.status,
        "source": record.source_kind,
        "file": record.file_path,
        "hash": record.content_hash,
        "official": True if record.official else None,
        "coverage": record.coverage,
        "learned_at": record.learned_at,
        "nodes": record.nodes,
        "patterns": record.patterns,
        "missing": record.missing_nodes,
        # 参数体检结论进 frontmatter：knowledge_consolidation 要靠它
        # 归纳「这一类 workflow 的常见问题」，只放正文的话机器读不到
        "problems": record.diagnostic_issues or None,
        # 参数与发现进 frontmatter：经 Markdown 往返后不再丢
        # （否则存量迁移到数据库的记录没有参数，归纳无从统计）
        "parameters": record.parameters or None,
        "discoveries": record.discoveries or None,
        "error": record.error or None,
    })

    body = render_body(record)

    return front + "\n" + body


def render_body(record: LearningRecord) -> str:
    """
    渲染正文（人读部分）
    """
    sections = []

    # ---- 标题与来源 ----
    header = [f"# {record.key}", ""]
    if record.file_path:
        header.append(f"> 来源文件 `{record.file_path}`")
    if record.status != "completed":
        header.append("")
        header.append(
            f"**状态：{record.status}**"
            + (f" —— {record.error}" if record.error else "")
        )
    sections.append("\n".join(header))

    # ---- 结构 ----
    if record.nodes:
        structure = ["## 结构", ""]

        if record.pipeline:
            structure.append(
                "**生成流程**：" + " → ".join(record.pipeline)
            )
            structure.append("")

        core = set(record.important_nodes)
        structure.append(f"**节点**（{len(record.nodes)} 个）：")
        for node in record.nodes:
            mark = " ★核心" if node in core else ""
            structure.append(f"- `{node}`{mark}")

        if record.patterns:
            structure.append("")
            structure.append("**识别到的模式**：" + "、".join(
                record.patterns
            ))

        sections.append("\n".join(structure))

    # ---- 参数 ----
    if record.parameters:
        params = ["## 关键参数", ""]
        for name, value in record.parameters.items():
            params.append(f"- `{name}` = `{value}`")
        sections.append("\n".join(params))

    # ---- 知识覆盖 ----
    if record.nodes:
        knowledge = ["## 知识", ""]
        knowledge.append(
            f"覆盖率 **{record.coverage:.0%}**"
            f"（{len(record.covered_nodes)}/{len(record.nodes)}）"
        )

        if record.covered_nodes:
            knowledge.append("")
            knowledge.append("**有卡**：" + "、".join(
                f"`{n}`" for n in dict.fromkeys(record.covered_nodes)
            ))

        if record.missing_nodes:
            knowledge.append("")
            knowledge.append(
                f"**缺卡**（{len(record.missing_nodes)}）："
                + "、".join(
                    f"`{n}`" for n in record.missing_nodes
                )
            )

        if record.knowledge_refs:
            knowledge.append("")
            knowledge.append("**用到的条目**：" + "、".join(
                record.knowledge_refs[:8]
            ))

        sections.append("\n".join(knowledge))

    # ---- 体检 ----
    if record.diagnostic_issues:
        diag = [
            "## 参数体检",
            "",
            f"发现 {len(record.diagnostic_issues)} 个问题：",
        ]
        for item in record.diagnostic_issues:
            diag.append(f"- {item}")
        sections.append("\n".join(diag))

    # ---- 发现 ----
    if record.discoveries:
        findings = ["## 学习发现", ""]
        for item in record.discoveries:
            findings.append(f"- {item}")
        sections.append("\n".join(findings))

    return "\n\n".join(sections).rstrip() + "\n"


def from_markdown(text: str) -> LearningRecord:
    """
    Markdown → 学习记录

    Args:
        text: 完整 Markdown 文本

    Returns:
        LearningRecord
    """
    front, _body = split_frontmatter(text)
    data = parse_frontmatter(front) if front else {}

    record = LearningRecord(
        workflow_name=data.get("name", ""),
        file_path=data.get("file", ""),
        key=data.get("key", ""),
        status=data.get("status", "completed"),
        source_kind=data.get("source", "json"),
        content_hash=data.get("hash", ""),
        official=bool(data.get("official", False)),
        workflow_type=data.get("type", ""),
        nodes=_as_list(data.get("nodes")),
        patterns=_as_list(data.get("patterns")),
        missing_nodes=_as_list(data.get("missing")),
        diagnostic_issues=_as_list(data.get("problems")),
        parameters=(
            data["parameters"]
            if isinstance(data.get("parameters"), dict) else {}
        ),
        discoveries=_as_list(data.get("discoveries")),
        error=data.get("error", ""),
        learned_at=data.get("learned_at", ""),
    )

    # 覆盖率反推 covered_nodes，保证 from_dict 往返后仍能算对
    coverage = data.get("coverage", "")
    if coverage not in ("", None):
        try:
            ratio = float(coverage)
        except ValueError:
            ratio = 0.0
        if record.nodes and not record.covered_nodes:
            covered_count = round(ratio * len(record.nodes))
            record.covered_nodes = record.nodes[:covered_count]

    return record


def _as_list(value: Any) -> List[str]:
    """
    frontmatter 值转字符串列表
    """
    if value is None:
        return []
    if isinstance(value, (list, tuple)):
        return [str(v) for v in value]
    text = str(value).strip()
    if not text:
        return []
    return [item.strip() for item in text.split(",") if item.strip()]
