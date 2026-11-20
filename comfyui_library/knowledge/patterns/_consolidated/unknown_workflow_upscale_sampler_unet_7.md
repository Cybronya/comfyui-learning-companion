---
name: unknown_workflow_upscale_sampler_unet_7
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.5315
common_nodes: [Any Switch (rgthree), ApplyPulidFlux, BasicGuider, BasicScheduler, Color Correct (mtb), DepthAnythingPreprocessor, DisableNoise, EmptyLatentImage, GetNode, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, InjectLatentNoise+, Int, KSamplerSelect, LatentInterpolate, LayerFilter: FilmV2, LoadImage, ModelSamplingFlux, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RandomNoise, SamplerCustomAdvanced, Seed Everywhere, SetNode, SplitSigmasDenoise, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/🐧_🎄_🎅_1935163741250232322.json, 平台全量/【企鹅AI】FluxGirl-Ultra-V3_1855924838077435906.json, 平台全量/超级有爱的🎄Fluxgirl V3 🎄圣诞皮肤_1863567167391248385.json, 平台全量/麦橘超然MajicFlux工作流-功能随意组合_1905452716926373890.json, 平台全量/🍊_Magic_Flus_🐧134_1876243170588872706.json, 平台全量/🐧_🎄_🎅-🎅_1869590413081219073.json, 平台全量/🐧_🎄_🎅_1867949611200446465.json, 平台全量/🐧_🎄_🎅（无人）_1869197660803469314.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_7

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/🐧_🎄_🎅_1935163741250232322.json、平台全量/【企鹅AI】FluxGirl-Ultra-V3_1855924838077435906.json、平台全量/超级有爱的🎄Fluxgirl V3 🎄圣诞皮肤_1863567167391248385.json、平台全量/麦橘超然MajicFlux工作流-功能随意组合_1905452716926373890.json、平台全量/🍊_Magic_Flus_🐧134_1876243170588872706.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 8 个 workflow 都包含：
- `Any Switch (rgthree)`
- `ApplyPulidFlux`
- `BasicGuider`
- `BasicScheduler`
- `Color Correct (mtb)`
- `DepthAnythingPreprocessor`
- `DisableNoise`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `InjectLatentNoise+`
- `Int`
- `KSamplerSelect`
- `LatentInterpolate`
- `LayerFilter: FilmV2`
- `LoadImage`
- `ModelSamplingFlux`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Seed Everywhere`
- `SetNode`
- `SplitSigmasDenoise`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `easy clearCacheAll` —— 7/8 个有
- `ConditioningZeroOut` —— 6/8 个有
- `FaceDetailer` —— 6/8 个有
- `SAMLoader` —— 6/8 个有
- `SaveImageAndMetadata_` —— 6/8 个有
- `UltralyticsDetectorProvider` —— 6/8 个有
- `easy bookmark` —— 5/8 个有
- `CLIPTextEncode` —— 4/8 个有
- `DualCLIPLoader` —— 4/8 个有
- `FluxGuidance` —— 4/8 个有
- `RHHiddenNodes` —— 4/8 个有
- `easy imageConcat` —— 4/8 个有
- `ImageResizeKJ` —— 3/8 个有
- `PreviewImage` —— 3/8 个有
- `String` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `RH_Captioner` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `CR Simple Image Compare` —— 1/8 个有
- `DetailDaemonSamplerNode` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `Florence2ModelLoader` —— 1/8 个有
- `Florence2Run` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `Joy_caption` —— 1/8 个有
- `Joy_caption_load` —— 1/8 个有
- `LayerUtility: ImageBlendAdvance` —— 1/8 个有
- `StringFunction|pysssss` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 8 | 100% |
| 高度 | 512 | 512 - 512 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，8 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，8 个样本，取值集中（一致性 100%）
