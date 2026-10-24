---
name: unknown_workflow_upscale_vae_44
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7645
common_nodes: [Fast Groups Bypasser (rgthree), IfInnerExecute, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleComparison+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2+TTP无损高清放大8k（RH批量版）_2050833550534029314.json, 图片生成/图生图/SeedVR2+TTP无损高清放大_2045402007468511234.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_44

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SeedVR2+TTP无损高清放大8k（RH批量版）_2050833550534029314.json、图片生成/图生图/SeedVR2+TTP无损高清放大_2045402007468511234.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `IfInnerExecute`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleComparison+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_ShowText` —— 1/2 个有
- `HAIGC_LoadImagesFromZip` —— 1/2 个有
- `ImageListToImageBatch` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `SelectImageList` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy imageCount` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
