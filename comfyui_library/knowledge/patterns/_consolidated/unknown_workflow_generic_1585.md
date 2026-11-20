---
name: unknown_workflow_generic_1585
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.872
common_nodes: [CR Prompt Text, Int, LoadImage, PreviewImage, RH_LLMAPI_Pro_Node, SaveImage, Switch, Text, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/🦖25宫格分镜_2027984658763354114.json, 图片生成/文生图/🦖9宫格分镜_2042530499960250369.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1585

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/🦖25宫格分镜_2027984658763354114.json、图片生成/文生图/🦖9宫格分镜_2042530499960250369.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `Int`
- `LoadImage`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `Switch`
- `Text`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `RH_DolaSeedream50ProImageToImage` —— 1/2 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/2 个有
- `StringConcatenate` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `TwoWaySwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
