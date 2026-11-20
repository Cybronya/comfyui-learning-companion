---
name: text_to_image_inpaint_upscale_lora
type: Text To Image
frequency: 6
level: strong
coverage: 0.501333
common_nodes: [AIO_Preprocessor, Bookmark (rgthree), CFGNorm, CLIPLoader, CLIPTextEncode, ColorMatchV2, ComfySwitchNode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, GetImageSize, GetNode, Image Blank, Image Comparer (rgthree), ImageCompositeMasked, ImagePadForOutpaint, ImageScale, ImageScaleToTotalPixels, ImageStitch, ImageUpscaleWithModel, InpaintCropImproved, InpaintStitchImproved, JjkText, JoinImageWithAlpha, JoinStringMulti, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextBox, LensBlur, Light-Tool: RGBA2RGB, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelPassThrough, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, PlaySound|pysssss, PreviewImage, QwenImage21Cache, QwenMultiangleCameraNode, ResizeImageMaskNode, ResolutionSelector, SaveImage, Seed (rgthree), SeedVR2Conditioning, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2PostProcessing, SeedVR2Preprocess, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, TextEncodeQwenImage21, ToBinaryMask, UNETLoader, UpscaleModelLoader, VAEDecode, VAEDecodeTiled, VAEEncodeTiled, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy getNode, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide, easy int, easy prompt, easy promptConcat, easy promptLine, easy setNode, easy showAnything, easy stylesSelector, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_unload_model, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 Edit全能合集文生图图生图处理工具_2102473513021034497.json, 图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2104662789758472194.json, 图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2105072387074125826.json, 图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2105400130022232066.json, 图片生成/文生图/Qwen2.1 Edit All In One 大合集｜文生图图生图高清放大一站搞定_2103658316122640386.json, 图片生成/文生图/Qwen2.1 Edit All In One合集，文生图图生图高清放大全覆盖_2103892863389093890.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_upscale_lora

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 Edit全能合集文生图图生图处理工具_2102473513021034497.json、图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2104662789758472194.json、图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2105072387074125826.json、图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2105400130022232066.json、图片生成/文生图/Qwen2.1 Edit All In One 大合集｜文生图图生图高清放大一站搞定_2103658316122640386.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：50%

## 共有节点

全部 6 个 workflow 都包含：
- `AIO_Preprocessor`
- `Bookmark (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `JjkText`
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
- `LoraLoaderModelOnly`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（15/6 个样本）：Steps较低可能导致细节不足
