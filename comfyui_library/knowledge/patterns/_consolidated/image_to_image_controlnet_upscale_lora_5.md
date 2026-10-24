---
name: image_to_image_controlnet_upscale_lora_5
type: Image To Image
frequency: 6
level: weak
coverage: 0.858833
common_nodes: [ApplyInstantID, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CM_IntToFloat, CM_IntToNumber, CM_NumberToInt, CM_NumberUnaryOperation, CR Upscale Image, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, DualCLIPLoader, EmptySD3LatentImage, FaceAnalysisModels, FaceBoundingBox, FluxGuidance, GetImageSize+, Image Comparer (rgthree), ImageComposite+, ImageScale, ImageScaleBy, ImpactSwitch, InstantIDFaceAnalysis, InstantIDModelLoader, JWImageResizeByLongerSide, JWInteger, KSampler, KSamplerSelect, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, MaskPreview+, ModelSamplingSD3, PDIMAGE_LongerSize, PathchSageAttentionKJ, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, SetLatentNoiseMask, SetUnionControlNetType, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["图片生成/图生图/Flux(pulid 姿势_深度)+Qwen Image,Wan2.2双重洗图换脸V2（文字保护版）_1953081322501771265.json", 图片生成/图生图/【人物指定姿势一致性】Wan2.1+Krea+姿势_深度+Pulid+InstantID_1952948694183309314.json, 图片生成/图生图/【电商】模特写真换脸 Krea+Wan2.2+CN+Pulid+Instantid_1953355535418576897.json, 图片生成/图生图/（方案1）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态_1951091184829669378.json, 图片生成/文生图/（方案2）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态V2_1951200400257036289.json, 图片生成/文生图/（最强人像文生图）Wan2.2+Krea+Cn2.0+Pulid+InstantID_1951546750295330818.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_lora_5

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux(pulid 姿势_深度)+Qwen Image,Wan2.2双重洗图换脸V2（文字保护版）_1953081322501771265.json、图片生成/图生图/【人物指定姿势一致性】Wan2.1+Krea+姿势_深度+Pulid+InstantID_1952948694183309314.json、图片生成/图生图/【电商】模特写真换脸 Krea+Wan2.2+CN+Pulid+Instantid_1953355535418576897.json、图片生成/图生图/（方案1）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态_1951091184829669378.json、图片生成/文生图/（方案2）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态V2_1951200400257036289.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `ApplyInstantID`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `CM_IntToNumber`
- `CM_NumberToInt`
- `CM_NumberUnaryOperation`
- `CR Upscale Image`
- `CheckpointLoaderSimple`
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
- `ApplyFBCacheOnModel` —— 5/6 个有
- `CR Prompt Text` —— 5/6 个有
- `ConditioningZeroOut` —— 5/6 个有
- `ImageConcanate` —— 5/6 个有
- `OpenposePreprocessor` —— 5/6 个有
- `ApplyPulidFlux` —— 4/6 个有
- `Bjornulf_TextToStringAndSeed` —— 4/6 个有
- `PulidFluxEvaClipLoader` —— 4/6 个有
- `PulidFluxFaceDetector` —— 4/6 个有
- `PulidFluxInsightFaceLoader` —— 4/6 个有
- `PulidFluxModelLoader` —— 4/6 个有
- `PulidFluxOptions` —— 4/6 个有
- `NunchakuFluxDiTLoader` —— 2/6 个有
- `NunchakuFluxPuLIDApplyV2` —— 2/6 个有
- `NunchakuPuLIDLoaderV2` —— 2/6 个有
- `PMRF` —— 2/6 个有
- `RH_Captioner` —— 2/6 个有
- `SeedVR2` —— 2/6 个有
- `BBoxesToSAM2` —— 1/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `DWPreprocessor` —— 1/6 个有
- `DownloadAndLoadQwenModel` —— 1/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `INPAINT_ExpandMask` —— 1/6 个有
- `InpaintModelConditioning` —— 1/6 个有
- `InvertMask` —— 1/6 个有
- `LayerMask: LoadSAM2Model` —— 1/6 个有
- `LayerMask: SAM2UltraV2` —— 1/6 个有
- `LayerUtility: ImageReel` —— 1/6 个有
- `LayerUtility: ImageReelComposit` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `MaskToImage` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `ModelSamplingAuraFlow` —— 1/6 个有
- `ModelSamplingFlux` —— 1/6 个有
- `NunchakuPulidApply` —— 1/6 个有
- `NunchakuPulidLoader` —— 1/6 个有
- `QwenVLDetection` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `RepeatImageBatch` —— 1/6 个有
- `SeedVR2BlockSwap` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `ShowText` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `TrimVideoLatent` —— 1/6 个有
- `WanVaceToVideo` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.35 | 0.1 - 2 | 6 | 0% |
| 采样步数 | 9 | 1 - 10 | 6 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 33% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 0.75 | 0.05 - 1 | 6 | 31% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- ControlNet 权重 中位数 0.35，观测区间 0.1 - 2，6 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 9，观测区间 1 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 33%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 0.75，观测区间 0.05 - 1，6 个样本，取值分散，一致性仅 31%
- 风险：重绘幅度 观测到 0.05，低于常用下限 0.1（）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
