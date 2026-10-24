---
name: unknown_workflow_upscale_sampler_clip_10
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.689375
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, FluxGuidance, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageUpscaleWithModel, KSamplerSelect, LoadImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecodeTiled, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX-测图+TTP放大_1959876674903027714.json, 图片生成/图生图/FLUX高清修复去油腻工作流_1942936253006569474.json, 图片生成/图生图/Flux 4k高清修复_1932001102521106433.json, 图片生成/图生图/放大照片无损_1963489445680074754.json, 图片生成/图生图/放大照片无损_1975073868308197377.json, 图片生成/图生图/无损高清放大（新技术）_1963484675418443777.json, 图片生成/图生图/超级好用无损放大照片_1976081180497940482.json, 图片生成/图生图/高清放大（零变形）_1953056397183356930.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/FLUX-测图+TTP放大_1959876674903027714.json、图片生成/图生图/FLUX高清修复去油腻工作流_1942936253006569474.json、图片生成/图生图/Flux 4k高清修复_1932001102521106433.json、图片生成/图生图/放大照片无损_1963489445680074754.json、图片生成/图生图/放大照片无损_1975073868308197377.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `KSamplerSelect`
- `LoadImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Florence2Run` —— 7/8 个有
- `LoraLoader` —— 7/8 个有
- `ShowText|pysssss` —— 7/8 个有
- `easy imageBatchToImageList` —— 7/8 个有
- `easy imageListToImageBatch` —— 7/8 个有
- `Florence2ModelLoader` —— 6/8 个有
- `ImageListToImageBatch` —— 6/8 个有
- `ImageScaleBy` —— 6/8 个有
- `easy imageSize` —— 6/8 个有
- `ImageScale` —— 5/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/8 个有
- `SeedVR2` —— 5/8 个有
- `SeedVR2BlockSwap` —— 5/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `easy imageSizeBySide` —— 5/8 个有
- `VAEDecode` —— 3/8 个有
- `Seed Everywhere` —— 2/8 个有
- `DisableNoise` —— 1/8 个有
- `DownloadAndLoadFlorence2Model` —— 1/8 个有
- `ImpactImageBatchToImageList` —— 1/8 个有
- `InjectLatentNoise+` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `KepStringLiteral` —— 1/8 个有
- `LayerUtility: JoyCaption2` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `SplitSigmasDenoise` —— 1/8 个有
- `TeaCache` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.5 - 1 | 7 | 80% |
| LoRA 文本强度 | 1 | 0.5 - 1 | 7 | 80% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.5 - 1，7 个样本，取值集中（一致性 80%）
- LoRA 文本强度 中位数 1，观测区间 0.5 - 1，7 个样本，取值集中（一致性 80%）
