---
name: unknown_workflow_generic_692
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.4035
common_nodes: [Comfly_LLm_API, GetNode, PreviewAny, SetNode, Text, easy saveText]
problems: []
missing: []
members: [图片生成/反推提示词/单图图像反推工作流-动作版_2004081105131192322.json, 图片生成/反推提示词/双图像视频工作流_2005132533216014337.json, 图片生成/反推提示词/图像打标工作流_2006244436107337730.json, 图片生成/反推提示词/视频反推工作流_2002649345990246402.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_692

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/单图图像反推工作流-动作版_2004081105131192322.json、图片生成/反推提示词/双图像视频工作流_2005132533216014337.json、图片生成/反推提示词/图像打标工作流_2006244436107337730.json、图片生成/反推提示词/视频反推工作流_2002649345990246402.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：40%

## 共有节点

全部 4 个 workflow 都包含：
- `Comfly_LLm_API`
- `GetNode`
- `PreviewAny`
- `SetNode`
- `Text`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `MultiLinePromptIndex` —— 3/4 个有
- `RH_LLMAPI_Pro_Node` —— 3/4 个有
- `Text Concatenate` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `MultiLinePromptMG` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
