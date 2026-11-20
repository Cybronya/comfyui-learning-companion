---
name: unknown_workflow_sampler_clip_unet_446
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.890333
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, FluxGuidance, GetImageSize+, INTConstant, Image Comparer (rgthree), KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: NumberCalculatorV2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageColorMatch, easy imageListToImageBatch, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Y-T2I+I2I+Upscale_flux2_1993686487835279361.json, 平台全量/FLUX2 一致性高清放大（需要Plus 运行）_1993426045776969730.json, "平台全量/Flux2-高清放大,太逆天了！_1993557551012839425.json"]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_446

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Y-T2I+I2I+Upscale_flux2_1993686487835279361.json、平台全量/FLUX2 一致性高清放大（需要Plus 运行）_1993426045776969730.json、平台全量/Flux2-高清放大,太逆天了！_1993557551012839425.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxGuidance`
- `GetImageSize+`
- `INTConstant`
- `Image Comparer (rgthree)`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: NumberCalculatorV2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageColorMatch`
- `easy imageListToImageBatch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `SDXL Resolutions (JPS)` —— 1/3 个有
- `SeedVR2` —— 1/3 个有
- `SeedVR2BlockSwap` —— 1/3 个有
- `SeedVR2ExtraArgs` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
