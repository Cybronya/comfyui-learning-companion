---
name: unknown_workflow_upscale_vae_88
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.921
common_nodes: [Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [平台全量/TTP图片超高清放大工作流_2068243799708618753.json, 平台全量/seedvr2分块高清放大_2049405124145057793.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_88

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/TTP图片超高清放大工作流_2068243799708618753.json、平台全量/seedvr2分块高清放大_2049405124145057793.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
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
- `GetImageSize+` —— 1/2 个有
- `ImageListToImageBatch` —— 1/2 个有
- `ImpactImageBatchToImageList` —— 1/2 个有
- `ImpactMinMax` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
