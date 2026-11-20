---
name: image_to_image_controlnet_inpaint_upscale_6
type: Image To Image
frequency: 2
level: weak
coverage: 0.8525
common_nodes: [AIO_Preprocessor, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DetailDaemonSamplerNode, Florence2ModelLoader, Florence2Run, GetImageSize+, Image Comparer (rgthree), ImageLoader, ImageResize+, ImageResizeKJv2, ImageScaleBy, ImageScaleToTotalPixels, ImageUpscaleWithModel, InpaintModelConditioning, KSampler, LatentUpscaleBy, LayerMask: MaskGrow, LayerUtility: CropByMask V2, LayerUtility: ImageScaleRestore, LayerUtility: PurgeVRAM V2, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, RandomNoise, SDPoseOODLoader, SDPoseOODProcessor, SamplerCustomAdvanced, SamplerEulerAncestral, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ShowText|pysssss, SplitSigmas, String Literal, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncode, VAELoader, YOLOModelLoader, ZImageFunControlnet, easy cleanGpuUsed, easy ifElse, easy imageBatchToImageList, easy imageListToImageBatch, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-Controlnet-2.1-8步局部重绘+lora修脸贴回+放大_2003151044785897473.json, 图片生成/文生图/Z-Image-Controlnet-2.1-8步文生图+lora修脸贴回+放大_2003343268333092866.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_inpaint_upscale_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image-Controlnet-2.1-8步局部重绘+lora修脸贴回+放大_2003151044785897473.json、图片生成/文生图/Z-Image-Controlnet-2.1-8步文生图+lora修脸贴回+放大_2003343268333092866.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DetailDaemonSamplerNode`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageLoader`
- `ImageResize+`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `KSampler`
- `LatentUpscaleBy`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleRestore`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RandomNoise`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SamplerCustomAdvanced`
- `SamplerEulerAncestral`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ShowText|pysssss`
- `SplitSigmas`
- `String Literal`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncode`
- `VAELoader`
- `YOLOModelLoader`
- `ZImageFunControlnet`
- `easy cleanGpuUsed`
- `easy ifElse`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `SetLatentNoiseMask` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.25 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
