---
name: text_to_image_controlnet_inpaint_lora_4
type: Text To Image
frequency: 3
level: strong
coverage: 0.866667
common_nodes: [AIO_Preprocessor, Anything Everywhere, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, Crop (mtb), DepthAnythingV2Preprocessor, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize+, GoogleTranslateTextNode, Image Comparer (rgthree), Image Filter Adjustments, ImageConcanate, ImageScale, ImageToMask, ImpactGaussianBlurMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LaMaInpaint, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoadImage, Lora Loader Stack (rgthree), MaskToImage, OpenposePreprocessor, PreviewImage, ReduxAdvanced, SaveImage, SetLatentNoiseMask, StyleModelLoader, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, ttN concat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【NEW】分镜转绘-260507_2052263172022784002.json, 图片生成/图生图/【NEW】分镜转绘-260507_2052304096614461441.json, 图片生成/文生图/RH10.27-郑义工作流_1984171131043250177.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【NEW】分镜转绘-260507_2052263172022784002.json、图片生成/图生图/【NEW】分镜转绘-260507_2052304096614461441.json、图片生成/文生图/RH10.27-郑义工作流_1984171131043250177.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `Crop (mtb)`
- `DepthAnythingV2Preprocessor`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageSize+`
- `GoogleTranslateTextNode`
- `Image Comparer (rgthree)`
- `Image Filter Adjustments`
- `ImageConcanate`
- `ImageScale`
- `ImageToMask`
- `ImpactGaussianBlurMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LaMaInpaint`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `MaskToImage`
- `OpenposePreprocessor`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `StyleModelLoader`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`
- `ttN concat`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 2/3 个有
- `BasicScheduler` —— 2/3 个有
- `CannyEdgePreprocessor` —— 2/3 个有
- `ChatGLM4TranslateTextNode` —— 2/3 个有
- `ControlNetInpaintingAliMamaApply` —— 2/3 个有
- `ExpressionEditor` —— 2/3 个有
- `GrowMaskWithBlur` —— 2/3 个有
- `Image Crop Location` —— 2/3 个有
- `Image Paste Crop` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `KSamplerSelect` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `Mask Crop Region` —— 2/3 个有
- `RH_LLMAPI_Pro_Node` —— 2/3 个有
- `RandomNoise` —— 2/3 个有
- `SamplerCustomAdvanced` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `VAEEncodeForInpaint` —— 2/3 个有
- `easy float` —— 2/3 个有
- `ttN pipeKSampler` —— 2/3 个有
- `ttN pipeLoader` —— 2/3 个有
- `ttN text` —— 2/3 个有
- `FluxKontextNode` —— 1/3 个有
- `LineArtPreprocessor` —— 1/3 个有
- `LoadImageAdvanced` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 0.77 - 1 | 3 | 88% |
| ControlNet 权重 | 0.3 | 0.3 - 0.4 | 3 | 86% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1280 | 1080 - 1280 | 3 | 92% |
| 高度 | 768 | 768 - 1920 | 3 | 53% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.77 - 1，3 个样本，取值集中（一致性 88%）
- ControlNet 权重 中位数 0.3，观测区间 0.3 - 0.4，3 个样本，取值集中（一致性 86%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 1080 - 1280，3 个样本，取值集中（一致性 92%）
- 高度 中位数 768，观测区间 768 - 1920，3 个样本
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
