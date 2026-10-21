---
name: unknown_workflow_upscale_vae_2
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.629667
common_nodes: [GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: [GetImageSize+, ImageResize+]
members: [图片生成/图生图/2001611198548307969.json, 图片生成/文生图/SeedVR2+TTP放大+0损耗压缩_2001561615235444738.json, 图片生成/文生图/百万像素超绝放大_2005617652724891650.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/2001611198548307969.json、图片生成/文生图/SeedVR2+TTP放大+0损耗压缩_2001561615235444738.json、图片生成/文生图/百万像素超绝放大_2005617652724891650.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `KOOK_ImageCompression` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：GetImageSize+、ImageResize+
