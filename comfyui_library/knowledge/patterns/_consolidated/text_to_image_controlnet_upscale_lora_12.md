---
name: text_to_image_controlnet_upscale_lora_12
type: Text To Image
frequency: 2
level: weak
coverage: 0.849
common_nodes: [AddLabel, AddMask, ApplyFBCacheOnModel, ApplyInstantID, ApplyPulidFlux, Blend, CLIPTextEncode, CM_IntToFloat, CM_IntToNumber, CM_NumberToInt, CM_NumberUnaryOperation, CR Prompt Text, CR Upscale Image, CheckpointLoaderSimple, ColorMatch, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, FaceAnalysisModels, FaceBoundingBox, FluxGuidance, FluxKontextImageScale, GetImageSize+, GetImageSizeAndCount, GoogleTranslateTextNode, Image Comparer (rgthree), Image Padding, ImageAndMaskPreview, ImageComposite+, ImageConcanate, ImageResizeAdvanced, ImageScale, ImageScaleBy, ImageStitch, ImpactSwitch, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, KSampler, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: CropByMask V2, LayerUtility: ImageBlend V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: LayerImageTransform, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM V2, LoadImage, LoadRembgByBiRefNetModel, LoraLoaderModelOnly, MagCache, MaskPreview+, PMRF, PathchSageAttentionKJ, PreviewImage, PrimitiveInt, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Captioner, RMBG, ReferenceLatent, RembgByBiRefNet, SaveImage, SetLatentNoiseMask, Text Concatenate (JPS), TextInput_, UnetLoaderGGUF, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy imageColorMatch, easy showAnything, preview_mask]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX Kontext 万物融合-产品+背景合并图_1944337602067746817.json, 图片生成/图生图/Flux Kontext Dev超级换装融合稳定加速版v1_1941793532090990593.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_12

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/FLUX Kontext 万物融合-产品+背景合并图_1944337602067746817.json、图片生成/图生图/Flux Kontext Dev超级换装融合稳定加速版v1_1941793532090990593.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `AddMask`
- `ApplyFBCacheOnModel`
- `ApplyInstantID`
- `ApplyPulidFlux`
- `Blend`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CM_IntToNumber`
- `CM_NumberToInt`
- `CM_NumberUnaryOperation`
- `CR Prompt Text`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize+`
- `GetImageSizeAndCount`
- `GoogleTranslateTextNode`
- `Image Comparer (rgthree)`
- `Image Padding`
- `ImageAndMaskPreview`
- `ImageComposite+`
- `ImageConcanate`
- `ImageResizeAdvanced`
- `ImageScale`
- `ImageScaleBy`
- `ImageStitch`
- `ImpactSwitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `JWImageResizeByLongerSide`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlend V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: LayerImageTransform`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadRembgByBiRefNetModel`
- `LoraLoaderModelOnly`
- `MagCache`
- `MaskPreview+`
- `PMRF`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `PrimitiveInt`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Captioner`
- `RMBG`
- `ReferenceLatent`
- `RembgByBiRefNet`
- `SaveImage`
- `SetLatentNoiseMask`
- `Text Concatenate (JPS)`
- `TextInput_`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageColorMatch`
- `easy showAnything`
- `preview_mask`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
