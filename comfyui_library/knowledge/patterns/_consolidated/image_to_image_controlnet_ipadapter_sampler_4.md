---
name: image_to_image_controlnet_ipadapter_sampler_4
type: Image To Image
frequency: 4
level: strong
coverage: 0.62
common_nodes: [AIO_Preprocessor, Anything Everywhere3, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplySD3, ControlNetLoader, DetailTransfer, Fast Bypasser (rgthree), FreeU_V2, GetNode, ICLightConditioning, IPAdapterAdvanced, IPAdapterUnifiedLoader, Image Comparer (rgthree), ImageApplyLUT+, ImageCASharpening+, ImageResize+, ImpactSwitch, KSampler, LayerColor: AutoAdjustV2, LayerFilter: GaussianBlur, LayerUtility: ColorPicker, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LightSource, LoadAndApplyICLightUnet, LoadImage, LoadImageMask, MaskToImage, PreviewBridge, PreviewImage, Prompts Everywhere, SaveImage, SetNode, VAEDecode, VAEEncode, easy imageSize, easy imageSizeBySide, easy negative, easy positive, easy showAnything, easy stylesSelector]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI一键打光_1922262219151622145.json, 图片生成/图生图/ic-light重打光，超强光影融合插件，保持物体细节不变，生成真实光影_1891043714717065217.json, 图片生成/图生图/环境人物智能一键打光_1913284902190575618.json, 图片生成/图生图/自动匹配环境光 智能打光relight_1922217827632349185.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_ipadapter_sampler_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI一键打光_1922262219151622145.json、图片生成/图生图/ic-light重打光，超强光影融合插件，保持物体细节不变，生成真实光影_1891043714717065217.json、图片生成/图生图/环境人物智能一键打光_1913284902190575618.json、图片生成/图生图/自动匹配环境光 智能打光relight_1922217827632349185.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：62%

## 共有节点

全部 4 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `DetailTransfer`
- `Fast Bypasser (rgthree)`
- `FreeU_V2`
- `GetNode`
- `ICLightConditioning`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `Image Comparer (rgthree)`
- `ImageApplyLUT+`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactSwitch`
- `KSampler`
- `LayerColor: AutoAdjustV2`
- `LayerFilter: GaussianBlur`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LightSource`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `LoadImageMask`
- `MaskToImage`
- `PreviewBridge`
- `PreviewImage`
- `Prompts Everywhere`
- `SaveImage`
- `SetNode`
- `VAEDecode`
- `VAEEncode`
- `easy imageSize`
- `easy imageSizeBySide`
- `easy negative`
- `easy positive`
- `easy showAnything`
- `easy stylesSelector`

**可变部分**（部分 workflow 才有）：
- `CR Upscale Image` —— 3/4 个有
- `ConditioningSetAreaStrength` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `DualCLIPLoader` —— 3/4 个有
- `ImageTile+` —— 3/4 个有
- `ImageUntile+` —— 3/4 个有
- `Images to Linear` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `VAEDecodeTiled` —— 3/4 个有
- `VAEEncodeTiled` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `easy imageBatchToImageList` —— 3/4 个有
- `easy imageListToImageBatch` —— 3/4 个有
- `easy imageRemBg` —— 3/4 个有
- `KSampler (Efficient)` —— 1/4 个有
- `easy seed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | 0.5 - 0.5 | 4 | 100% |
| 采样步数 | 30 | 30 - 30 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 4 | 42% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | karras | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.5，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 30 - 30，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，4 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 karras，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
