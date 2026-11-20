---
name: unknown_workflow_upscale_vae_54
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8935
common_nodes: [GetImageSize+, ImageResize+, ImageScaleBy, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/放大_2107022066804420610.json, 图片生成/文生图/百万像素超绝放大_2005617652724891650.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_54

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/放大_2107022066804420610.json、图片生成/文生图/百万像素超绝放大_2005617652724891650.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `SaveImageJPG_GH` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
