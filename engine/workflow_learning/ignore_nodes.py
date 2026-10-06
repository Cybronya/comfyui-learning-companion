# -*- coding: utf-8 -*-
"""
布线/装饰节点忽略清单。

这类节点只承担「注释、转接、取值、预览」职能，不含生成知识：
给它们建知识卡只会稀释知识库，并让缺口检测 / 建卡优先级
被 `Note`、`Reroute` 这类节点永久霸榜。

来源：2026-10-06 对 comfyui_library/workflows/ 404 个真实
workflow 的节点频次统计，人工归类为无生成语义的布线与 UI 节点。

使用方：
- workflow_learner：缺口检测时跳过布线节点（不再计入缺卡与发现）
- learning_store：node_frequency() 可排除布线节点后再排建卡优先级
"""

# 纯布线：值原样进出，不产生任何变换
PLUMBING_NODES = frozenset({
    "Note",
    "MarkdownNote",
    "Reroute",
    "Reroute (rgthree)",
    "GetNode",
    "SetNode",
    "Any Switch (rgthree)",
    "ComfySwitchNode",
    "easy ifElse",
    "easy showAnything",
    "ImpactSwitch",
    "Anything Everywhere",
    "Anything Everywhere3",
    "Anything Everywhere4",
})

# 纯注释 / 帮助文本（中文社区常见注释节点）
COMMENT_NODES = frozenset({
    "孤海注释",
    "Show Text|pysssss",
    "ShowText|pysssss",
    "JjkText",
})

# 纯预览 / 调试输出（不参与生成链路）
PREVIEW_NODES = frozenset({
    "PreviewImage",
    "Preview Any",
    "Image Comparer (rgthree)",
    "Image Comparer (rgthree) 🖼️",
})

# 输入占位（LoadImage 之外的上传占位类，语义固定到不值一张卡）
PLACEHOLDER_NODES = frozenset({
    "PrimitiveNode",
    "PrimitiveString",
    "PrimitiveStringMultiline",
    "PrimitiveInt",
    "PrimitiveFloat",
})

IGNORED_NODES = (
    PLUMBING_NODES | COMMENT_NODES | PREVIEW_NODES | PLACEHOLDER_NODES
)


def is_ignored(node_type: str) -> bool:
    """该节点类型是否为布线/注释/预览类（不建卡、不计缺口）"""
    return node_type in IGNORED_NODES


def filter_ignored(node_types):
    """过滤掉布线类节点，返回剩余列表（保持原顺序）"""
    return [n for n in node_types if not is_ignored(n)]
