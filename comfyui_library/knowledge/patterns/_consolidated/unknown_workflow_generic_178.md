---
name: unknown_workflow_generic_178
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.823
common_nodes: [Get Image Size, ImageCASharpening+, ImageResize+, ImpactMinMax, LoadImage, SeedVR2, TTP_Image_Assy, TTP_Image_Tile_Batch]
problems: []
missing: []
members: [图片生成/图生图/SeedVR无损4k放大（极速）_2006705954708000770.json, 图片生成/图生图/SeedVR无损4k放大（极速）_2011349356733014017.json, 图片生成/图生图/SeedVR无损4k放大（极速）_2021427542640566274.json, 图片生成/图生图/万物图片高清放大（分块）seedVR2_1956177364311048194.json, 图片生成/图生图/万物高清_2086061742978846722.json, 图片生成/图生图/万物高清放大_1985667227728916481.json, 图片生成/图生图/人像、文字、万物皆可高清放大8K（不变形）_2112521603924971521.json, 图片生成/图生图/人像高清放大修复不改变原细节 产品高清修复 人物高清修复 产品高清放大4K 8k_2007832429540675585.json, 图片生成/图生图/图片4K高清放大修复不改变原细节（分块）seedVR2_2032131005594738690.json, 图片生成/图生图/图片清晰放大优化精修模糊变清晰seedVR2 万物高清放大（分块）_2074670337190621185.json, 图片生成/图生图/多分镜&二次放大-Rubby_2007714930438443010.json, 图片生成/图生图/多分镜&二次放大-rubby_2008814429311340545.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_178

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/SeedVR无损4k放大（极速）_2006705954708000770.json、图片生成/图生图/SeedVR无损4k放大（极速）_2011349356733014017.json、图片生成/图生图/SeedVR无损4k放大（极速）_2021427542640566274.json、图片生成/图生图/万物图片高清放大（分块）seedVR2_1956177364311048194.json、图片生成/图生图/万物高清_2086061742978846722.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 12 个 workflow 都包含：
- `Get Image Size`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `LoadImage`
- `SeedVR2`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 10/12 个有
- `SaveImage` —— 10/12 个有
- `DF_Integer` —— 9/12 个有
- `SimpleMath+` —— 9/12 个有
- `easy cleanGpuUsed` —— 9/12 个有
- `PreviewImage` —— 7/12 个有
- `SetNode` —— 4/12 个有
- `GetNode` —— 3/12 个有
- `LayerUtility: PurgeVRAM V2` —— 3/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `KOOK_SaveJPGImage` —— 2/12 个有
- `RH_Nano_Banana2_Image2Image` —— 2/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `TT_img_enc` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
