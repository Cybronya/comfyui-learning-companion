---
name: unknown_workflow_upscale_lora_sampler_45
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.618833
common_nodes: [BasicGuider, BasicScheduler, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GetNode, ImageScaleToTotalPixels, ImageUpscaleWithModel, ImpactImageBatchToImageList, Int, KSamplerSelect, LoraLoaderModelOnly, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed Everywhere, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/gongzuoliuziyong1_1937562107925958657.json, 平台全量/gongzuoliuziyong2_1945022215995969538.json, 平台全量/【企鹅AI】Flux girl 网红生成器 PRO-V3_1854098231419342849.json, 平台全量/【企鹅AI】Flux girl 网红生成器 V2_1846476978701660162.json, 平台全量/【企鹅AI】FluxGirl穿搭小游戏V2_1852303664731119618.json, 平台全量/【企鹅AI】FluxGirl穿搭小游戏_1851605882294648833.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_45

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/gongzuoliuziyong1_1937562107925958657.json、平台全量/gongzuoliuziyong2_1945022215995969538.json、平台全量/【企鹅AI】Flux girl 网红生成器 PRO-V3_1854098231419342849.json、平台全量/【企鹅AI】Flux girl 网红生成器 V2_1846476978701660162.json、平台全量/【企鹅AI】FluxGirl穿搭小游戏V2_1852303664731119618.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GetNode`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ImpactImageBatchToImageList`
- `Int`
- `KSamplerSelect`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed Everywhere`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingPreprocessor` —— 5/6 个有
- `DisableNoise` —— 5/6 个有
- `LayerFilter: FilmV2` —— 5/6 个有
- `ModelSamplingFlux` —— 5/6 个有
- `SplitSigmasDenoise` —— 5/6 个有
- `CLIPTextEncode` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `LayerUtility: ImageBlendAdvance` —— 3/6 个有
- `SaveImageAndMetadata_` —— 3/6 个有
- `String` —— 3/6 个有
- `StringFunction|pysssss` —— 3/6 个有
- `CR Text Input Switch (4 way)` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `RHHiddenNodes` —— 2/6 个有
- `Random Number` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `CR Simple Image Compare` —— 1/6 个有
- `ImageResizeKJ` —— 1/6 个有
- `Joy_caption` —— 1/6 个有
- `Joy_caption_load` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 6 | 100% |
| 高度 | 512 | 512 - 512 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，6 个样本，取值集中（一致性 100%）
