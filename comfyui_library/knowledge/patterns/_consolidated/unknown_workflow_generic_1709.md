---
name: unknown_workflow_generic_1709
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.883
common_nodes: [ColorMatch, Get Image Size, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, LoadImage, SaveImage, SeedVR2, TTP_Image_Assy, TTP_Image_Tile_Batch]
problems: []
missing: []
members: [图片生成/图生图/图像分块极速放大 SeedVR2 【快速、好用】_1977525512761417729.json, 图片生成/图生图/图像超清4k放大_1991039297094656002.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1709

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图像分块极速放大 SeedVR2 【快速、好用】_1977525512761417729.json、图片生成/图生图/图像超清4k放大_1991039297094656002.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 2 个 workflow 都包含：
- `ColorMatch`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`

**可变部分**（部分 workflow 才有）：
- `ImpactMinMax` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `SeedVR2BlockSwap` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy int` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
