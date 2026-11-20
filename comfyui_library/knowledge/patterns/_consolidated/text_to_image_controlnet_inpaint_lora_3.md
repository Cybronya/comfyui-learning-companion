---
name: text_to_image_controlnet_inpaint_lora_3
type: Text To Image
frequency: 4
level: strong
coverage: 0.868
common_nodes: [AIO_Preprocessor, Anything Everywhere, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, Crop (mtb), DepthAnythingV2Preprocessor, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize+, GoogleTranslateTextNode, Image Comparer (rgthree), Image Filter Adjustments, ImageConcanate, ImageScale, ImageToMask, ImpactGaussianBlurMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LaMaInpaint, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoadImage, Lora Loader Stack (rgthree), MaskToImage, OpenposePreprocessor, PreviewImage, ReduxAdvanced, SaveImage, SetLatentNoiseMask, StyleModelLoader, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, ttN concat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【NEW】分镜转绘-260507_2052263172022784002.json, 图片生成/图生图/【NEW】分镜转绘-260507_2052304096614461441.json, 图片生成/文生图/RH10.27-郑义工作流_1984171131043250177.json, 平台全量/RH10.20-一丹工作流_1980570098073255938.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/【NEW】分镜转绘-260507_2052263172022784002.json、图片生成/图生图/【NEW】分镜转绘-260507_2052304096614461441.json、图片生成/文生图/RH10.27-郑义工作流_1984171131043250177.json、平台全量/RH10.20-一丹工作流_1980570098073255938.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
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
- `ChatGLM4TranslateTextNode` —— 3/4 个有
- `Image Crop Location` —— 3/4 个有
- `Image Paste Crop` —— 3/4 个有
- `ImageScaleToTotalPixels` —— 3/4 个有
- `Mask Crop Region` —— 3/4 个有
- `easy float` —— 3/4 个有
- `BasicGuider` —— 2/4 个有
- `BasicScheduler` —— 2/4 个有
- `CannyEdgePreprocessor` —— 2/4 个有
- `ControlNetInpaintingAliMamaApply` —— 2/4 个有
- `ExpressionEditor` —— 2/4 个有
- `GrowMaskWithBlur` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `KSamplerSelect` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `LineArtPreprocessor` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `RH_LLMAPI_Pro_Node` —— 2/4 个有
- `RandomNoise` —— 2/4 个有
- `SamplerCustomAdvanced` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `VAEEncodeForInpaint` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `ttN pipeKSampler` —— 2/4 个有
- `ttN pipeLoader` —— 2/4 个有
- `ttN text` —— 2/4 个有
- `FluxKontextNode` —— 1/4 个有
- `LoadImageAdvanced` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 0.885 | 0.75 - 1 | 4 | 86% |
| ControlNet 权重 | 0.35 | 0.3 - 0.4 | 4 | 86% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1180 | 1080 - 1280 | 4 | 92% |
| 高度 | 1344 | 768 - 1920 | 4 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 0.885，观测区间 0.75 - 1，4 个样本，取值集中（一致性 86%）
- ControlNet 权重 中位数 0.35，观测区间 0.3 - 0.4，4 个样本，取值集中（一致性 86%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1180，观测区间 1080 - 1280，4 个样本，取值集中（一致性 92%）
- 高度 中位数 1344，观测区间 768 - 1920，4 个样本
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
