---
name: unknown_workflow_upscale_vae_29
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8902
common_nodes: [ImageResize+, ImageScaleBy, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/无损放大工作流_2046887976344494082.json, 图片生成/图生图/高清放大 SeedVR2.5 + TTP分块放大_2071767145079468033.json, 图片生成/图生图/高清放大SeedVR2.5 + TTP 分块放大1.0_2061629043874820098.json, 图片生成/图生图/（漫剧人物）放大细节修复（极速版）_2045585679790379010.json, 图片生成/图生图/🍭老许Gary：SeedVR2.5图像放大修复_2018018624648253441.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_29

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/无损放大工作流_2046887976344494082.json、图片生成/图生图/高清放大 SeedVR2.5 + TTP分块放大_2071767145079468033.json、图片生成/图生图/高清放大SeedVR2.5 + TTP 分块放大1.0_2061629043874820098.json、图片生成/图生图/（漫剧人物）放大细节修复（极速版）_2045585679790379010.json、图片生成/图生图/🍭老许Gary：SeedVR2.5图像放大修复_2018018624648253441.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResize+`
- `ImageScaleBy`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `ConstrainImage|pysssss` —— 3/5 个有
- `Get Image Size` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `GetImageSize+` —— 2/5 个有
- `INTConstant` —— 2/5 个有
- `ImageScaleToTotalPixels` —— 2/5 个有
- `CR Simple Image Compare` —— 1/5 个有
- `KOOK_SaveJPGImage` —— 1/5 个有
- `PreviewImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
