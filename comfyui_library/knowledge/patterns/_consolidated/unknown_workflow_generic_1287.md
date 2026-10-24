---
name: unknown_workflow_generic_1287
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.859
common_nodes: [DF_Integer, Get Image Size, Image Comparer (rgthree), ImageCASharpening+, ImageFromBatch, ImageResize+, ImpactMinMax, LoadImage, SaveImage, SeedVR2, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, easy batchAnything, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy imageCount, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/seedVR2 终极强化版高清工作流_1964342535374163970.json, 图片生成/图生图/一致性+全能图片V1 老照片修复_1976496032466997249.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1287

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/seedVR2 终极强化版高清工作流_1964342535374163970.json、图片生成/图生图/一致性+全能图片V1 老照片修复_1976496032466997249.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `DF_Integer`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageFromBatch`
- `ImageResize+`
- `ImpactMinMax`
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `easy batchAnything`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy imageCount`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveFloat` —— 1/2 个有
- `RH_Nano_Banana_Image2Image` —— 1/2 个有
- `Textbox` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
