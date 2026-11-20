---
name: text_to_image_inpaint_upscale_lora
type: Text To Image
frequency: 7
level: weak
coverage: 0.492429
common_nodes: [AIO_Preprocessor, Bookmark (rgthree), CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, GetImageSize, GetNode, Image Blank, Image Comparer (rgthree), ImageCompositeMasked, ImagePadForOutpaint, ImageScale, ImageScaleToTotalPixels, ImageStitch, ImageUpscaleWithModel, InpaintCropImproved, InpaintStitchImproved, JoinImageWithAlpha, JoinStringMulti, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelPassThrough, ModelPatchTorchSettings, ModelSamplingAuraFlow, PathchSageAttentionKJ, PlaySound|pysssss, PreviewImage, QwenMultiangleCameraNode, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy getNode, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide, easy prompt, easy promptConcat, easy promptLine, easy setNode, easy showAnything, easy stylesSelector, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_unload_model]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1 Edit全能合集文生图图生图处理工具_2102473513021034497.json, 图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2104662789758472194.json, 图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2105072387074125826.json, 图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2105400130022232066.json, 图片生成/文生图/Qwen2.1 Edit All In One 大合集｜文生图图生图高清放大一站搞定_2103658316122640386.json, 图片生成/文生图/Qwen2.1 Edit All In One合集，文生图图生图高清放大全覆盖_2103892863389093890.json, 平台全量/❷「合集」Qwen Edit All In One V2「6.7」_2007013698077986818.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_upscale_lora

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1 Edit全能合集文生图图生图处理工具_2102473513021034497.json、图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2104662789758472194.json、图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2105072387074125826.json、图片生成/图生图/Qwen2.1 Edit All In One 全能图像编辑工作流_2105400130022232066.json、图片生成/文生图/Qwen2.1 Edit All In One 大合集｜文生图图生图高清放大一站搞定_2103658316122640386.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：49%

## 共有节点

全部 7 个 workflow 都包含：
- `AIO_Preprocessor`
- `Bookmark (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelPassThrough`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `PlaySound|pysssss`
- `PreviewImage`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy getNode`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy imageSizeBySide`
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

**可变部分**（部分 workflow 才有）：
- `ColorMatchV2` —— 6/7 个有
- `ComfySwitchNode` —— 6/7 个有
- `JjkText` —— 6/7 个有
- `LayerUtility: TextBox` —— 6/7 个有
- `LensBlur` —— 6/7 个有
- `Light-Tool: RGBA2RGB` —— 6/7 个有
- `QwenImage21Cache` —— 6/7 个有
- `ResizeImageMaskNode` —— 6/7 个有
- `ResolutionSelector` —— 6/7 个有
- `SeedVR2Conditioning` —— 6/7 个有
- `SeedVR2PostProcessing` —— 6/7 个有
- `SeedVR2Preprocess` —— 6/7 个有
- `TextEncodeQwenImage21` —— 6/7 个有
- `ToBinaryMask` —— 6/7 个有
- `VAEDecodeTiled` —— 6/7 个有
- `VAEEncodeTiled` —— 6/7 个有
- `VOSR2ModelLoader` —— 6/7 个有
- `VOSR2Upscale` —— 6/7 个有
- `easy int` —— 6/7 个有
- `solarL_SaveImagesToZip` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `CheckpointLoaderSimple` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `ImageColorMatch+` —— 1/7 个有
- `ReferenceLatent` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `VAEEncode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 69% |
| 采样算法 | er_sde | - | 7 | 86% |
| 调度器 | beta | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 1280 | 7 | 0% |
| 高度 | 80 | 80 - 720 | 7 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本
- 采样算法 最常用 er_sde，7 个样本，一致性 86%
- 调度器 最常用 beta，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1280，7 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 720，7 个样本，取值分散，一致性仅 0%
- 高发问题（22/7 个样本）：Steps较低可能导致细节不足
