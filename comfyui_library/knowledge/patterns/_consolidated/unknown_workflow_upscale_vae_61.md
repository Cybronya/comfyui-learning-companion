---
name: unknown_workflow_upscale_vae_61
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.931
common_nodes: [GetImageSize, ImageResize+, ImageScale, ImageScaleBy, ImageScaleToTotalPixels, ImageTile+, ImageUntile+, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/TTP分块高清放大_2100404605812301825.json, 图片生成/图生图/TTP分块高清放大_2100492925233885186.json, 平台全量/TTP分块放大_2043988372481384449.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_61

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/TTP分块高清放大_2100404605812301825.json、图片生成/图生图/TTP分块高清放大_2100492925233885186.json、平台全量/TTP分块放大_2043988372481384449.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSize`
- `ImageResize+`
- `ImageScale`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageTile+`
- `ImageUntile+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy cleanGpuUsed`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
