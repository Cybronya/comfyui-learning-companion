---
name: unknown_workflow_generic_981
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.895333
common_nodes: [DF_Integer, Get Image Size, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImpactMinMax, LoadImage, SaveImage, SeedVR2, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2+TTP 高清放大_1989281903083704321.json, 图片生成/图生图/SeedVR2.5图片快速高清放大_2011478686431715329.json, 图片生成/图生图/SeedVR2.5图片高清放大_2038075237920673794.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_981

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SeedVR2+TTP 高清放大_1989281903083704321.json、图片生成/图生图/SeedVR2.5图片快速高清放大_2011478686431715329.json、图片生成/图生图/SeedVR2.5图片高清放大_2038075237920673794.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `DF_Integer`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`

**可变部分**（部分 workflow 才有）：
- `AutoImageResize` —— 2/3 个有
- `CR Value` —— 2/3 个有
- `Cut By Mask` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `InvertMask (segment anything)` —— 2/3 个有
- `MaskToImage` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
