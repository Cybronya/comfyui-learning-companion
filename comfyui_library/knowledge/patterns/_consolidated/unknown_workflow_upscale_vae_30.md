---
name: unknown_workflow_upscale_vae_30
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9506
common_nodes: [ImageResize+, ImageScaleBy, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/无损放大工作流_2046887976344494082.json, 图片生成/图生图/老孙AI TTP+seed VR2放大 亿级像素_2114580383802159106.json, 图片生成/图生图/零偏差高清放大_SeedVR2_jex_2040343386443489281.json, 图片生成/图生图/高清放大 SeedVR2.5 + TTP分块放大_2071767145079468033.json, 图片生成/图生图/高清放大SeedVR2.5 + TTP 分块放大1.0_2061629043874820098.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_30

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/无损放大工作流_2046887976344494082.json、图片生成/图生图/老孙AI TTP+seed VR2放大 亿级像素_2114580383802159106.json、图片生成/图生图/零偏差高清放大_SeedVR2_jex_2040343386443489281.json、图片生成/图生图/高清放大 SeedVR2.5 + TTP分块放大_2071767145079468033.json、图片生成/图生图/高清放大SeedVR2.5 + TTP 分块放大1.0_2061629043874820098.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResize+`
- `ImageScaleBy`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`

**可变部分**（部分 workflow 才有）：
- `Get Image Size` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `ConstrainImage|pysssss` —— 3/5 个有
- `GetImageSize+` —— 2/5 个有
- `KOOK_SaveJPGImage` —— 1/5 个有
- `MuyeLoadImage` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy imageScaleToNormPixels` —— 1/5 个有
- `数学运算_孤海` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
