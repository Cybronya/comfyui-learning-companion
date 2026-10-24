---
name: unknown_workflow_upscale_vae_28
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8466
common_nodes: [GetImageSize+, ImageResize+, ImageScaleBy, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/巨星放大_2111002690523324418.json, 图片生成/图生图/快速图像0变现一亿像素超清细节放大_1992873146072231938.json, 图片生成/图生图/无损转高清_2085970588300046337.json, 图片生成/图生图/百万像素超绝放大_2011688385735299074.json, 图片生成/图生图/高清放大图片恢复材质细节（适合物体）_2015293769049972738.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_28

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/巨星放大_2111002690523324418.json、图片生成/图生图/快速图像0变现一亿像素超清细节放大_1992873146072231938.json、图片生成/图生图/无损转高清_2085970588300046337.json、图片生成/图生图/百万像素超绝放大_2011688385735299074.json、图片生成/图生图/高清放大图片恢复材质细节（适合物体）_2015293769049972738.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `GetImageSize+`
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
- `GetNode` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `Image H264 Compression (mtb)` —— 1/5 个有
- `ImageCASharpening+` —— 1/5 个有
- `MemoryCleaner` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
