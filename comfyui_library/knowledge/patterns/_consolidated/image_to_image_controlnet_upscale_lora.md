---
name: image_to_image_controlnet_upscale_lora
type: Image To Image
frequency: 2
level: weak
coverage: 0.7035
common_nodes: [ApplyFBCacheOnModel, ApplyInstantID, BasicGuider, BasicScheduler, Bjornulf_TextToStringAndSeed, CLIPLoader, CLIPTextEncode, CM_IntToFloat, CM_IntToNumber, CM_NumberToInt, CM_NumberUnaryOperation, CR Prompt Text, CR Upscale Image, CheckpointLoaderSimple, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, DualCLIPLoader, EmptySD3LatentImage, FaceAnalysisModels, FaceBoundingBox, FluxGuidance, GetImageSize+, Image Comparer (rgthree), ImageComposite+, ImageConcanate, ImageScale, ImageScaleBy, ImpactSwitch, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, JWInteger, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingSD3, PDIMAGE_LongerSize, PathchSageAttentionKJ, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, SetUnionControlNetType, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: [ImageComposite+, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LayerUtility: PurgeVRAM, easy imageColorMatch, CR Prompt Text, CR Upscale Image, GetImageSize+, MaskPreview+]
members: [图片生成/文生图/1951200400257036289.json, 图片生成/文生图/1951546750295330818.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1951200400257036289.json、图片生成/文生图/1951546750295330818.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFBCacheOnModel`
- `ApplyInstantID`
- `BasicGuider`
- `BasicScheduler`
- `Bjornulf_TextToStringAndSeed`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CM_IntToNumber`
- `CM_NumberToInt`
- `CM_NumberUnaryOperation`
- `CR Prompt Text`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `FluxGuidance`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageComposite+`
- `ImageConcanate`
- `ImageScale`
- `ImageScaleBy`
- `ImpactSwitch`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `JWImageResizeByLongerSide`
- `JWInteger`
- `KSampler`
- `KSamplerSelect`
- `LayerMask: MaskGrow`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask`
- `LayerUtility: LayerImageTransform`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskPreview+`
- `ModelSamplingSD3`
- `PDIMAGE_LongerSize`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetLatentNoiseMask`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `ApplyPulidFlux` —— 1/2 个有
- `DWPreprocessor` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxPuLIDApplyV2` —— 1/2 个有
- `NunchakuPuLIDLoaderV2` —— 1/2 个有
- `OpenposePreprocessor` —— 1/2 个有
- `PulidFluxEvaClipLoader` —— 1/2 个有
- `PulidFluxFaceDetector` —— 1/2 个有
- `PulidFluxInsightFaceLoader` —— 1/2 个有
- `PulidFluxModelLoader` —— 1/2 个有
- `PulidFluxOptions` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `SeedVR2` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5.5 | - | 2 | 18% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 50% |
| 重绘幅度 | 0.525 | - | 2 | 10% |
| ControlNet 权重 | 1.05 | - | 2 | 10% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 50%
- 重绘幅度 中位数 0.525，样本不足，未给区间，2 个样本，取值分散，一致性仅 10%
- ControlNet 权重 中位数 1.05，样本不足，未给区间，2 个样本，取值分散，一致性仅 10%
- 风险：重绘幅度 观测到 0.05，低于常用下限 0.1（）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：ImageComposite+、LayerMask: MaskGrow、LayerMask: PersonMaskUltra V2、LayerUtility: CropBoxResolve、LayerUtility: CropByMask
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
