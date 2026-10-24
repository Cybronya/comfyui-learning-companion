---
name: unknown_workflow_upscale_vae_16
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.825143
common_nodes: [GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/4K高清放大_2055902054677262338.json, 图片生成/图生图/6k图像保留质感究极放大seedVR2+ttp一分钟出图_2080927672020062209.json, 图片生成/图生图/6k图像保留质感究极放大seedVR2+ttp一分钟出图_2096056787190505474.json, 图片生成/图生图/6k图像保留质感究极放大seedVR2+ttp一分钟出图_2096164231119986689.json, 图片生成/图生图/6k图像保留质感究极放大（seedVR2+ttp）一分钟出图_2048119652559097858.json, 图片生成/图生图/G-image-2 + 放大_2048576303057604609.json, 图片生成/图生图/SeedVR2 （TTP分块）4K图片高清放大_2063228339137110017.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_16

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/4K高清放大_2055902054677262338.json、图片生成/图生图/6k图像保留质感究极放大seedVR2+ttp一分钟出图_2080927672020062209.json、图片生成/图生图/6k图像保留质感究极放大seedVR2+ttp一分钟出图_2096056787190505474.json、图片生成/图生图/6k图像保留质感究极放大seedVR2+ttp一分钟出图_2096164231119986689.json、图片生成/图生图/6k图像保留质感究极放大（seedVR2+ttp）一分钟出图_2048119652559097858.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`

**可变部分**（部分 workflow 才有）：
- `Float` —— 4/7 个有
- `Int` —— 4/7 个有
- `KOOK_ImageCompression` —— 4/7 个有
- `ImageCASharpening+` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `easy int` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `RH_RhartImageG2ImageToImage` —— 1/7 个有
- `RH_RhartImageG2OfficialImageToImage` —— 1/7 个有
- `RH_RhartImageG2TextToImage` —— 1/7 个有
- `图像缩放V2_孤海` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
