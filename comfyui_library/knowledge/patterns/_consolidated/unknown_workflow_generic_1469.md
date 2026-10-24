---
name: unknown_workflow_generic_1469
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.535
common_nodes: [1hew_ImageGridSplit, EmptyImage, LoadImage, PreviewAny, PreviewImage, PrimitiveStringMultiline, RHLLMChatNode, RH_RhartImageG2OfficialImageToImage, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/NPC生成器，九宫格，支持纯文本或带参考图两种模式_2092490650733334529.json, 图片生成/文生图/敌人生成器，九宫格，支持纯文本或带参考图两种模式_2092507233866309633.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1469

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/NPC生成器，九宫格，支持纯文本或带参考图两种模式_2092490650733334529.json、图片生成/文生图/敌人生成器，九宫格，支持纯文本或带参考图两种模式_2092507233866309633.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `1hew_ImageGridSplit`
- `EmptyImage`
- `LoadImage`
- `PreviewAny`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RHLLMChatNode`
- `RH_RhartImageG2OfficialImageToImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `RH_RhartImageG2OfficialTextToImage` —— 1/2 个有
- `RH_RhartImageG2TextToImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
