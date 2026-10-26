---
name: unknown_workflow_upscale_sampler_clip_28
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7172
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/4Kttpflux 放大工作流 api 版本_1984539387545468930.json, 图片生成/图生图/F1一键精修+放大，金属，户外带通用_1993247312828891137.json, 图片生成/图生图/FLUX-测图+TTP放大_1959876674903027714.json, 图片生成/图生图/FLUX高清修复去油腻工作流_1942936253006569474.json, 图片生成/图生图/Flux 4k高清修复_1932001102521106433.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_28

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/4Kttpflux 放大工作流 api 版本_1984539387545468930.json、图片生成/图生图/F1一键精修+放大，金属，户外带通用_1993247312828891137.json、图片生成/图生图/FLUX-测图+TTP放大_1959876674903027714.json、图片生成/图生图/FLUX高清修复去油腻工作流_1942936253006569474.json、图片生成/图生图/Flux 4k高清修复_1932001102521106433.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 4/5 个有
- `LoraLoader` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `easy imageBatchToImageList` —— 4/5 个有
- `VAEDecode` —— 3/5 个有
- `Florence2Run` —— 2/5 个有
- `ImageListToImageBatch` —— 2/5 个有
- `Seed Everywhere` —— 2/5 个有
- `ShowText|pysssss` —— 2/5 个有
- `easy imageListToImageBatch` —— 2/5 个有
- `DisableNoise` —— 1/5 个有
- `DownloadAndLoadFlorence2Model` —— 1/5 个有
- `Florence2ModelLoader` —— 1/5 个有
- `ImageListToBatch+` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `ImpactImageBatchToImageList` —— 1/5 个有
- `InjectLatentNoise+` —— 1/5 个有
- `JjkText` —— 1/5 个有
- `KepStringLiteral` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LayerUtility: JoyCaption2` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `SplitSigmasDenoise` —— 1/5 个有
- `TeaCache` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.9 | 0.5 - 1 | 4 | 75% |
| LoRA 文本强度 | 0.9 | 0.5 - 1 | 4 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.9，观测区间 0.5 - 1，4 个样本
- LoRA 文本强度 中位数 0.9，观测区间 0.5 - 1，4 个样本
