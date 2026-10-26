---
name: unknown_workflow_generic_1526
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8035
common_nodes: [CR Text, CR Text Replace, GetTextFromJson, LoadImage, LoadJsonFromText, RH_LLMAPI_Pro_Node, RH_Nano_Banana2_Gemini31Flash, SaveImage, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/批量服装电商多角度自动生成多个环境背景真实_2065057600143716353.json, 图片生成/图生图/电商服装一键生成多背景Ai自动出背景图_2065054479896109057.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1526

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/批量服装电商多角度自动生成多个环境背景真实_2065057600143716353.json、图片生成/图生图/电商服装一键生成多背景Ai自动出背景图_2065054479896109057.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `CR Text Replace`
- `GetTextFromJson`
- `LoadImage`
- `LoadJsonFromText`
- `RH_LLMAPI_Pro_Node`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `Int` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `Text Multiline` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
