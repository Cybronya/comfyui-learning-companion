---
name: unknown_workflow_generic_1645
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7225
common_nodes: [Image Comparer (rgthree), ImageResize+, LoadRembgByBiRefNetModel, MaskToImage, RembgByBiRefNet, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/【批量抠图】Birefnet II轻量级抠图_1965861255657492481.json, 平台全量/快速抠图-Birefnet_2039664641562910721.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1645

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【批量抠图】Birefnet II轻量级抠图_1965861255657492481.json、平台全量/快速抠图-Birefnet_2039664641562910721.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：72%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageResize+`
- `LoadRembgByBiRefNetModel`
- `MaskToImage`
- `RembgByBiRefNet`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RHBatchImages:` —— 1/2 个有
- `RHUploadZip` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
