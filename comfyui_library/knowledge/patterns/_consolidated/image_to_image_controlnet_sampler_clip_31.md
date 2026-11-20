---
name: image_to_image_controlnet_sampler_clip_31
type: Image To Image
frequency: 2
level: weak
coverage: 0.737
common_nodes: [BatchAverageImage, CLIPTextEncode, CheckpointLoaderSimple, ColorMatchImage, ControlNetApply, ControlNetLoader, DepthAnythingPreprocessor, FrequencyCombination, FrequencySeparation, FrequencySeparationHSV, GrowMaskWithBlur, ICLightConditioning, Image Blending Mode, Image Comparer (rgthree), ImageBatch, ImageBatchMulti, Int, JWImageResize, KSampler, LoadAndApplyICLightUnet, LoadImage, LoadImageMask, MaskToImage, PreviewBridge, PreviewImage, RemapImageRange, RemapMaskRange, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [平台全量/Relight Better than Magnific - Relighting v5 (bett_1840083322272972801.json, 平台全量/【大师流】IC light 保持颜色 重绘_1819014022011224066.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_31

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Relight Better than Magnific - Relighting v5 (bett_1840083322272972801.json、平台全量/【大师流】IC light 保持颜色 重绘_1819014022011224066.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：74%

## 共有节点

全部 2 个 workflow 都包含：
- `BatchAverageImage`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatchImage`
- `ControlNetApply`
- `ControlNetLoader`
- `DepthAnythingPreprocessor`
- `FrequencyCombination`
- `FrequencySeparation`
- `FrequencySeparationHSV`
- `GrowMaskWithBlur`
- `ICLightConditioning`
- `Image Blending Mode`
- `Image Comparer (rgthree)`
- `ImageBatch`
- `ImageBatchMulti`
- `Int`
- `JWImageResize`
- `KSampler`
- `LoadAndApplyICLightUnet`
- `LoadImage`
- `LoadImageMask`
- `MaskToImage`
- `PreviewBridge`
- `PreviewImage`
- `RemapImageRange`
- `RemapMaskRange`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `Blur` —— 1/2 个有
- `Cfg Literal` —— 1/2 个有
- `ConditioningConcat` —— 1/2 个有
- `FaceAnalysisModels` —— 1/2 个有
- `FaceSegmentation` —— 1/2 个有
- `Float` —— 1/2 个有
- `GroundingDinoModelLoader (segment anything)` —— 1/2 个有
- `GroundingDinoSAMSegment (segment anything)` —— 1/2 个有
- `IPAdapterAdvanced` —— 1/2 个有
- `IPAdapterFaceID` —— 1/2 个有
- `IPAdapterUnifiedLoader` —— 1/2 个有
- `IPAdapterUnifiedLoaderFaceID` —— 1/2 个有
- `Image Blend by Mask` —— 1/2 个有
- `Image Size to Number` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `ImageScaleToMegapixels` —— 1/2 个有
- `MaskFromRGBCMYBW+` —— 1/2 个有
- `Number to Int` —— 1/2 个有
- `SAMModelLoader (segment anything)` —— 1/2 个有
- `Switch any [Crystools]` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 5.25 | - | 2 | 48% |
| 采样算法 | dpmpp_2m_sde | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.575 | - | 2 | 26% |
| ControlNet 权重 | 0.775 | - | 2 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 5.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 dpmpp_2m_sde，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.575，样本不足，未给区间，2 个样本，取值分散，一致性仅 26%
- ControlNet 权重 中位数 0.775，样本不足，未给区间，2 个样本，取值集中（一致性 90%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
