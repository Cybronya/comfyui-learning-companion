---
name: unknown_workflow_generic_1409
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.413
common_nodes: [GetNode, LoadImage, RH_Nano_Banana2_Image2Image, SaveImage, SetNode, Text]
problems: []
missing: []
members: [图片生成/图生图/服装搭配2_2071162422261538818.json, 图片生成/文生图/一致性生图工作流（老程）_2019663643889111042.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1409

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/服装搭配2_2071162422261538818.json、图片生成/文生图/一致性生图工作流（老程）_2019663643889111042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：41%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `LoadImage`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `SetNode`
- `Text`

**可变部分**（部分 workflow 才有）：
- `MultiTextConcatenate` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `StringMergeNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
