---
name: unknown_workflow_inpaint_upscale_sampler_9
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.460667
common_nodes: [AIO_Preprocessor, Bookmark (rgthree), CFGNorm, CLIPLoader, ColorMatchV2, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, GetImageSize, GetNode, Image Blank, Image Comparer (rgthree), ImageCompositeMasked, ImagePadForOutpaint, ImageScale, ImageScaleToTotalPixels, ImageStitch, ImageUpscaleWithModel, InpaintCropImproved, InpaintStitchImproved, JoinImageWithAlpha, JoinStringMulti, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextBox, LensBlur, Light-Tool: RGBA2RGB, LoadImage, MaskPreview+, ModelPassThrough, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, PlaySound|pysssss, PreviewImage, QwenImage21Cache, QwenMultiangleCameraNode, ResizeImageMaskNode, ResolutionSelector, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2PostProcessing, SeedVR2Preprocess, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, ToBinaryMask, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy getNode, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide, easy int, easy prompt, easy promptConcat, easy promptLine, easy setNode, easy showAnything, easy stylesSelector, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_unload_model]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1 Edit All In One_2104333758026571778.json, 图片生成/图生图/全功能合集Qwen2.1+Edit+All+In+One_2108376316243439617.json, 图片生成/文生图/「合集」Qwen2.1 Edit All In One_2101986321656016898.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen2.1 Edit All In One_2104333758026571778.json、图片生成/图生图/全功能合集Qwen2.1+Edit+All+In+One_2108376316243439617.json、图片生成/文生图/「合集」Qwen2.1 Edit All In One_2101986321656016898.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Bookmark (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `ColorMatchV2`
- `ComfySwitchNode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextImageScale`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSize`
- `GetNode`
- `Image Blank`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImagePadForOutpaint`
- `ImageScale`
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `ImageUpscaleWithModel`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `JoinImageWithAlpha`
- `JoinStringMulti`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextBox`
- `LensBlur`
- `Light-Tool: RGBA2RGB`
- `LoadImage`
- `MaskPreview+`
- `ModelPassThrough`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PreviewImage`
- `QwenImage21Cache`
- `QwenMultiangleCameraNode`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2Conditioning`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2PostProcessing`
- `SeedVR2Preprocess`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `TextEncodeQwenImage21`
- `ToBinaryMask`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy getNode`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy imageSizeBySide`
- `easy int`
- `easy prompt`
- `easy promptConcat`
- `easy promptLine`
- `easy setNode`
- `easy showAnything`
- `easy stylesSelector`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_unload_model`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
