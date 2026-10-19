---
name: text_to_image_controlnet_inpaint_lora_5
type: Text To Image
frequency: 2
level: weak
coverage: 0.775
common_nodes: [AIO_Preprocessor, Anything Everywhere, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoader, Crop (mtb), DepthAnythingV2Preprocessor, DifferentialDiffusion, DualCLIPLoader, EmptyLatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageSize+, GoogleTranslateTextNode, Image Comparer (rgthree), Image Filter Adjustments, ImageConcanate, ImageScale, ImageToMask, ImpactGaussianBlurMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LaMaInpaint, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LineArtPreprocessor, LoadImage, Lora Loader Stack (rgthree), MaskToImage, OpenposePreprocessor, PreviewImage, RH_LLMAPI_NODE, ReduxAdvanced, SaveImage, SetLatentNoiseMask, StyleModelLoader, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageSize, easy showAnything, ttN concat]
problems: [Steps较低可能导致细节不足]
missing: [Crop (mtb), Image Filter Adjustments, LayerUtility: CropByMask V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, Text Multiline, ttN concat, GetImageSize+, Lora Loader Stack (rgthree), easy imageSize]
members: [图片生成/文生图/1984171131043250177.json, 图片生成/文生图/RH10.27-郑义工作流_1984171131043250177.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_inpaint_lora_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1984171131043250177.json、图片生成/文生图/RH10.27-郑义工作流_1984171131043250177.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
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
- `LineArtPreprocessor`
- `LoadImage`
- `Lora Loader Stack (rgthree)`
- `MaskToImage`
- `OpenposePreprocessor`
- `PreviewImage`
- `RH_LLMAPI_NODE`
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
- `easy showAnything`
- `ttN concat`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.4 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 0.77 | - | 2 | 100% |
| 宽度 | 1080 | - | 2 | 100% |
| 高度 | 1920 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 0.77，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Crop (mtb)、Image Filter Adjustments、LayerUtility: CropByMask V2、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: RestoreCropBox
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
