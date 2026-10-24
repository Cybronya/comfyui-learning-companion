---
name: unknown_workflow_upscale_vae_45
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.931
common_nodes: [GetImageSize, ImageResize+, ImageScale, ImageScaleBy, ImageScaleToTotalPixels, ImageTile+, ImageUntile+, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/TTP分块高清放大_2100404605812301825.json, 图片生成/图生图/TTP分块高清放大_2100492925233885186.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_45

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/TTP分块高清放大_2100404605812301825.json、图片生成/图生图/TTP分块高清放大_2100492925233885186.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
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

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
