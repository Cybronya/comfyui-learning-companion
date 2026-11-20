---
name: image_to_image_inpaint_upscale_lora_11
type: Image To Image
frequency: 2
level: weak
coverage: 0.8515
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, Image Blank, ImageConcanate, ImageCrop+, ImageListToImageBatch, ImageScaleToTotalPixels, ImageToMask, ImageUpscaleWithModel, ImpactInt, InpaintModelConditioning, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, MaskToImage, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, StyleModelApply, StyleModelLoader, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, easy imageBatchToImageList, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/产品换背景_1896223790777434114.json, 平台全量/Flux 万物迁移_1912340382087114753.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_11

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/产品换背景_1896223790777434114.json、平台全量/Flux 万物迁移_1912340382087114753.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `Image Blank`
- `ImageConcanate`
- `ImageCrop+`
- `ImageListToImageBatch`
- `ImageScaleToTotalPixels`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `ImpactInt`
- `InpaintModelConditioning`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `MaskToImage`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `StyleModelApply`
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
- `easy imageBatchToImageList`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `EG_SJPJ_Node` —— 1/2 个有
- `FloatSlider` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `ImageResizeKJ` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `Joy_caption_two` —— 1/2 个有
- `Joy_caption_two_load` —— 1/2 个有
- `LayerFilter: HDREffects` —— 1/2 个有
- `LayerMask: BiRefNetUltraV2` —— 1/2 个有
- `LayerMask: LoadBiRefNetModel` —— 1/2 个有
- `LayerUtility: ExtendCanvas` —— 1/2 个有
- `LayerUtility: ImageBlend` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `Note Plus (mtb)` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `SetLatentNoiseMask` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
