---
name: unknown_workflow_upscale_vae_47
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.868
common_nodes: [GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, JoinImageWithAlpha, KOOK_ImageCompression, KOOK_SaveJPGImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy cleanGpuUsed, easy clearCacheAll, easy int, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/图像批量放大-ZIP格式-SeedVR2.5（有用）_2011684011390799874.json, 平台全量/图像批量放大-ZIP格式-SeedVR2.5_2003401578579202050.json, 平台全量/图像批量放大ZIP上传下载-SeedVR2.5_2016381202407628801.json, 平台全量/超清放大-最高可放大至1亿像素-SeedVR2.5.15_1985578252192436226.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_47

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图像批量放大-ZIP格式-SeedVR2.5（有用）_2011684011390799874.json、平台全量/图像批量放大-ZIP格式-SeedVR2.5_2003401578579202050.json、平台全量/图像批量放大ZIP上传下载-SeedVR2.5_2016381202407628801.json、平台全量/超清放大-最高可放大至1亿像素-SeedVR2.5.15_1985578252192436226.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `JoinImageWithAlpha`
- `KOOK_ImageCompression`
- `KOOK_SaveJPGImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 3/4 个有
- `HAIGC_SaveImagesToZip` —— 3/4 个有
- `ImageListToBatch_` —— 3/4 个有
- `RHUploadZip_V2` —— 3/4 个有
- `easy imageSize` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `Int` —— 1/4 个有
- `TextBox` —— 1/4 个有
- `easy mathInt` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
