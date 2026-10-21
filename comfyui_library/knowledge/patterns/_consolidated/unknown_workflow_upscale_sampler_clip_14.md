---
name: unknown_workflow_upscale_sampler_clip_14
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.649
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, GrowMask, Image Comparer (rgthree), ImageUpscaleWithModel, InvertMask, JoinImageWithAlpha, KSamplerSelect, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LoadImage, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, Upscale Model Loader, VAEDecode, VAEEncode, VAELoader, YUAN_TXTConvertAny, easy cleanGpuUsed]
problems: []
missing: [CR Text, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, SimpleMath+, easy cleanGpuUsed, GetImageSize+, ImageResize+, Upscale Model Loader, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy imageScaleDownToSize]
members: [图片生成/图生图/2064532810496565250.json, 图片生成/图生图/2095771710493650945.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/2064532810496565250.json、图片生成/图生图/2095771710493650945.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：65%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `InvertMask`
- `JoinImageWithAlpha`
- `KSamplerSelect`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `Upscale Model Loader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `YUAN_TXTConvertAny`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImpactInt` —— 1/2 个有
- `ImpactMinMax` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `TTP_Image_Assy` —— 1/2 个有
- `TTP_Image_Tile_Batch` —— 1/2 个有
- `UltimateSDUpscaleCustomSample` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy imageScaleDownToSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、LayerMask: BiRefNetUltraV2、LayerMask: LoadBiRefNetModelV2、SimpleMath+、easy cleanGpuUsed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
