---
name: unknown_workflow_generic_499
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.818
common_nodes: [LoadImage, ProcessString, RH_LLMAPI_Pro_Node, SaveImage, Text, easy promptConcat, easy promptLine, easy showAnything]
problems: []
missing: [easy promptConcat, easy promptLine]
members: [图片生成/反推提示词/全自动电商出详情只提示_2106391913095061506.json, 图片生成/图生图/2102301912535232513.json, 数字人/数字人/电商详情页生成直出10张_2102684851412492289.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_499

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/全自动电商出详情只提示_2106391913095061506.json、图片生成/图生图/2102301912535232513.json、数字人/数字人/电商详情页生成直出10张_2102684851412492289.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `ProcessString`
- `RH_LLMAPI_Pro_Node`
- `SaveImage`
- `Text`
- `easy promptConcat`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RH_Nano_Banana2_Image2Image` —— 2/3 个有
- `ShowText` —— 2/3 个有
- `PreviewAny` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `SimplePromptBatcher` —— 1/3 个有
- `easy saveText` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：easy promptConcat、easy promptLine
