---
name: unknown_workflow_generic_1291
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.976
common_nodes: [CR Text, DapaoImageLayoutNode, DapaoRandomPromptLineExtractNode, DapaoSafeSaveImage, ImageListToBatch+, ImageStitch, ImpactInt, LoadImage, RH_Nano_Banana2_Gemini31Flash, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/ye服装换装【0.1】_2045009545092665345.json, 图片生成/图生图/超微距服装带细节换装【API调用每次1毛】_2011332640250531841.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1291

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/ye服装换装【0.1】_2045009545092665345.json、图片生成/图生图/超微距服装带细节换装【API调用每次1毛】_2011332640250531841.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `DapaoImageLayoutNode`
- `DapaoRandomPromptLineExtractNode`
- `DapaoSafeSaveImage`
- `ImageListToBatch+`
- `ImageStitch`
- `ImpactInt`
- `LoadImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Note Plus (mtb)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
