---
name: unknown_workflow_upscale_lora_sampler_124
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.978
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImageListToImageBatch, ImageUpscaleWithModel, ImpactMinMax, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, SDVN Load Image Url, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageSize, easy int]
problems: []
missing: []
members: [图片生成/图生图/高清和修复二合一的效果_2100418665740066817.json, 平台全量/高清放大_2043859255450669057.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_124

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/高清和修复二合一的效果_2100418665740066817.json、平台全量/高清放大_2043859255450669057.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageListToImageBatch`
- `ImageUpscaleWithModel`
- `ImpactMinMax`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SDVN Load Image Url`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageBatchToImageList`
- `easy imageSize`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `DF_Float` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageScaleBy` —— 1/2 个有
- `PDImageResizeV2` —— 1/2 个有
- `RH_DLSS5Enhance` —— 1/2 个有
- `ResizeImagesByLongerEdge` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
