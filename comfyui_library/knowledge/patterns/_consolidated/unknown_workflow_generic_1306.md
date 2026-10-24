---
name: unknown_workflow_generic_1306
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.811
common_nodes: [CR Text, HAIGC_CombineUnits, HAIGC_Layer, HAIGC_SavePSD, LoadImage, PromptBatchQueue, RH_LLMAPI_Pro_Node, RH_Nano_Banana2_Gemini31Flash, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/一键产品生成详情主图_2046506767437275138.json, 图片生成/图生图/一键生成产品详情页_2030177329959407617.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1306

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键产品生成详情主图_2046506767437275138.json、图片生成/图生图/一键生成产品详情页_2030177329959407617.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `HAIGC_CombineUnits`
- `HAIGC_Layer`
- `HAIGC_SavePSD`
- `LoadImage`
- `PromptBatchQueue`
- `RH_LLMAPI_Pro_Node`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 1/2 个有
- `CR Text Replace` —— 1/2 个有
- `Int` —— 1/2 个有
- `IntToString` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
