---
name: image_to_image_inpaint_upscale_lora_4
type: Image To Image
frequency: 3
level: strong
coverage: 0.870667
common_nodes: [Anything Everywhere3, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CLIPVisionLoader, CR Latent Batch Size, ConditioningZeroOut, DisableNoise, DualCLIPLoader, Fast Groups Bypasser (rgthree), Florence2ModelLoader, Florence2Run, FluxGuidance, GetImageSize+, Image Comparer (rgthree), ImageConcatMulti, ImageScale, ImageScaleToTotalPixels, ImageToMask, ImageUpscaleWithModel, ImpactInt, InpaintModelConditioning, KSampler, KSamplerSelect, LayerUtility: CropByMask, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LongCLIPTextEncodeFlux, LoraLoaderModelOnly, MaskPreview+, MaskToImage, ModelSamplingFlux, PreviewImage, RandomNoise, ReduxAdvanced, SamplerCustomAdvanced, SaveImage, SolidMask, SplitSigmasDenoise, StyleModelLoader, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageBatchToImageList, easy imageConcat]
problems: []
missing: []
members: [图片生成/图生图/AIYO-高还原度图片仿写_1905278147149877250.json, 图片生成/图生图/抖音小红书美女涨粉工作流_1903670134605783041.json, 图片生成/图生图/超真实批量仿写_抖音小红书美女_1908924211169996801.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/AIYO-高还原度图片仿写_1905278147149877250.json、图片生成/图生图/抖音小红书美女涨粉工作流_1903670134605783041.json、图片生成/图生图/超真实批量仿写_抖音小红书美女_1908924211169996801.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `CR Latent Batch Size`
- `ConditioningZeroOut`
- `DisableNoise`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `InpaintModelConditioning`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LongCLIPTextEncodeFlux`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `MaskToImage`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `ReduxAdvanced`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SolidMask`
- `SplitSigmasDenoise`
- `StyleModelLoader`
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
- `easy imageBatchToImageList`
- `easy imageConcat`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | deis | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 deis，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
