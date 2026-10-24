---
name: unknown_workflow_generic_1390
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.666
common_nodes: [Bjornulf_ShowInt, GetNode, LoadImage, PreviewImage, RHBatchImages:, RHExtractImage, RHUploadZip, SaveImage, SetNode, Text, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/批量上传局部重绘v2_2062012357316005890.json, 图片生成/图生图/批量上传局部重绘全能图片G2_2062779401909133313.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1390

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/批量上传局部重绘v2_2062012357316005890.json、图片生成/图生图/批量上传局部重绘全能图片G2_2062779401909133313.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `GetNode`
- `LoadImage`
- `PreviewImage`
- `RHBatchImages:`
- `RHExtractImage`
- `RHUploadZip`
- `SaveImage`
- `SetNode`
- `Text`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageListToImageBatch` —— 1/2 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/2 个有
- `RH_RhartImageG2ImageToImage` —— 1/2 个有
- `RH_RhartImageG2ImageToImage_Batch` —— 1/2 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
