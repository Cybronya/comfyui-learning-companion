---
name: unknown_workflow_generic_1609
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.931
common_nodes: [AutoImageResize, CR Value, Cut By Mask, DF_Integer, Get Image Size, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImageScale, ImpactMinMax, InvertMask (segment anything), LoadImage, MaskToImage, SaveImage, SeedVR2, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, easy anythingIndexSwitch]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2.5图片快速高清放大_2011478686431715329.json, 图片生成/图生图/SeedVR2.5图片高清放大_2038075237920673794.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1609

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SeedVR2.5图片快速高清放大_2011478686431715329.json、图片生成/图生图/SeedVR2.5图片高清放大_2038075237920673794.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `AutoImageResize`
- `CR Value`
- `Cut By Mask`
- `DF_Integer`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageScale`
- `ImpactMinMax`
- `InvertMask (segment anything)`
- `LoadImage`
- `MaskToImage`
- `SaveImage`
- `SeedVR2`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `easy anythingIndexSwitch`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
