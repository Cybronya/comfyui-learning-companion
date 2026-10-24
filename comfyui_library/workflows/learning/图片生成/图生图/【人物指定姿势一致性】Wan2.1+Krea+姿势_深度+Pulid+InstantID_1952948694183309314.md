---
key: 图片生成/图生图/【人物指定姿势一致性】Wan2.1+Krea+姿势_深度+Pulid+InstantID_1952948694183309314.json
name: 【人物指定姿势一致性】Wan2.1+Krea+姿势_深度+Pulid+InstantID_1952948694183309314
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【人物指定姿势一致性】Wan2.1+Krea+姿势_深度+Pulid+InstantID_1952948694183309314.json
hash: 51e4af4d9d34341a
coverage: 0.850877
learned_at: 2026-10-23 11:49:28
nodes: [KSamplerSelect, Note, PulidFluxFaceDetector, BasicScheduler, BasicGuider, ImageScaleBy, PrimitiveNode, FluxGuidance, LayerUtility: PurgeVRAM, UNETLoader, VAELoader, PulidFluxModelLoader, RandomNoise, PulidFluxInsightFaceLoader, PulidFluxEvaClipLoader, DualCLIPLoader, EmptySD3LatentImage, OpenposePreprocessor, DownloadAndLoadDepthAnythingV2Model, ControlNetLoader, SetUnionControlNetType, SetUnionControlNetType, FaceAnalysisModels, FaceBoundingBox, ImageScale, PreviewImage, CheckpointLoaderSimple, CLIPTextEncode, CLIPTextEncode, InstantIDModelLoader, InstantIDFaceAnalysis, ControlNetLoader, ControlNetLoader, ApplyInstantID, ControlNetApplyAdvanced, KSampler, VAEDecode, VAEEncode, SetLatentNoiseMask, LayerUtility: CropByMask, ApplyFBCacheOnModel, CR Upscale Image, CM_IntToFloat, ImageScaleBy, LayerUtility: LayerImageTransform, LayerMask: PersonMaskUltra V2, LayerMask: MaskGrow, PreviewImage, PreviewImage, LayerUtility: LayerImageTransform, easy imageColorMatch, ImageScale, GetImageSize+, CM_NumberUnaryOperation, CM_NumberToInt, CM_IntToFloat, LayerUtility: CropBoxResolve, LayerMask: MaskGrow, ControlNetApplyAdvanced, SaveImage, Image Comparer (rgthree), PreviewImage, MaskPreview+, PreviewImage, CM_NumberToInt, CM_IntToNumber, PreviewImage, PreviewImage, CLIPLoader, VAELoader, TrimVideoLatent, VAEDecode, MathExpression|pysssss, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, WanVaceToVideo, DepthAnything_V2, ImageComposite+, PulidFluxOptions, CR Prompt Text, ApplyPulidFlux, SamplerCustomAdvanced, ConditioningZeroOut, CLIPTextEncode, ImpactSwitch, LayerMask: PersonMaskUltra V2, CR Prompt Text, GetImageRangeFromBatch, CLIPTextEncode, VAEDecode, PreviewImage, UNETLoader, JWInteger, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, KSampler, PreviewImage, PDIMAGE_LongerSize, Text Concatenate, ImpactSwitch, RepeatImageBatch, ImpactSwitch, PreviewImage, ImageConcanate, LoadImage, PMRF, PreviewImage, ImageConcanate, LoadImage, RH_LLMAPI_NODE, RH_LLMAPI_NODE, JWInteger, JWImageResizeByLongerSide]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 0.6000000000000001, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 12055502359716, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【人物指定姿势一致性】Wan2.1+Krea+姿势_深度+Pulid+InstantID_1952948694183309314.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【人物指定姿势一致性】Wan2.1+Krea+姿势_深度+Pulid+InstantID_1952948694183309314.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（114 个）：
- `KSamplerSelect` ★核心
- `Note`
- `PulidFluxFaceDetector`
- `BasicScheduler`
- `BasicGuider`
- `ImageScaleBy`
- `PrimitiveNode`
- `FluxGuidance`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `VAELoader`
- `PulidFluxModelLoader`
- `RandomNoise`
- `PulidFluxInsightFaceLoader`
- `PulidFluxEvaClipLoader`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `OpenposePreprocessor`
- `DownloadAndLoadDepthAnythingV2Model`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `ImageScale`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `InstantIDModelLoader`
- `InstantIDFaceAnalysis`
- `ControlNetLoader`
- `ControlNetLoader`
- `ApplyInstantID`
- `ControlNetApplyAdvanced` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `LayerUtility: CropByMask`
- `ApplyFBCacheOnModel`
- `CR Upscale Image`
- `CM_IntToFloat`
- `ImageScaleBy`
- `LayerUtility: LayerImageTransform`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: MaskGrow`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: LayerImageTransform`
- `easy imageColorMatch`
- `ImageScale`
- `GetImageSize+`
- `CM_NumberUnaryOperation`
- `CM_NumberToInt`
- `CM_IntToFloat`
- `LayerUtility: CropBoxResolve`
- `LayerMask: MaskGrow`
- `ControlNetApplyAdvanced` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `MaskPreview+`
- `PreviewImage`
- `CM_NumberToInt`
- `CM_IntToNumber`
- `PreviewImage`
- `PreviewImage`
- `CLIPLoader`
- `VAELoader`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `MathExpression|pysssss`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `WanVaceToVideo`
- `DepthAnything_V2`
- `ImageComposite+`
- `PulidFluxOptions`
- `CR Prompt Text`
- `ApplyPulidFlux`
- `SamplerCustomAdvanced` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ImpactSwitch`
- `LayerMask: PersonMaskUltra V2`
- `CR Prompt Text`
- `GetImageRangeFromBatch`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `JWInteger`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `PreviewImage`
- `PDIMAGE_LongerSize`
- `Text Concatenate`
- `ImpactSwitch`
- `RepeatImageBatch`
- `ImpactSwitch`
- `PreviewImage`
- `ImageConcanate`
- `LoadImage`
- `PMRF`
- `PreviewImage`
- `ImageConcanate`
- `LoadImage`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_NODE`
- `JWInteger`
- `JWImageResizeByLongerSide`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`
- `controlnet_strength` = `0.6000000000000001`
- `seed` = `12055502359716`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（97/114）

**有卡**：`KSamplerSelect`、`PulidFluxFaceDetector`、`BasicScheduler`、`BasicGuider`、`ImageScaleBy`、`FluxGuidance`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`VAELoader`、`PulidFluxModelLoader`、`RandomNoise`、`PulidFluxInsightFaceLoader`、`PulidFluxEvaClipLoader`、`DualCLIPLoader`、`EmptySD3LatentImage`、`OpenposePreprocessor`、`DownloadAndLoadDepthAnythingV2Model`、`ControlNetLoader`、`SetUnionControlNetType`、`FaceAnalysisModels`、`FaceBoundingBox`、`ImageScale`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`InstantIDModelLoader`、`InstantIDFaceAnalysis`、`ApplyInstantID`、`ControlNetApplyAdvanced`、`KSampler`、`VAEDecode`、`VAEEncode`、`SetLatentNoiseMask`、`LayerUtility: CropByMask`、`ApplyFBCacheOnModel`、`CR Upscale Image`、`CM_IntToFloat`、`LayerUtility: LayerImageTransform`、`LayerMask: PersonMaskUltra V2`、`LayerMask: MaskGrow`、`easy imageColorMatch`、`GetImageSize+`、`CM_NumberUnaryOperation`、`CM_NumberToInt`、`LayerUtility: CropBoxResolve`、`SaveImage`、`MaskPreview+`、`CM_IntToNumber`、`CLIPLoader`、`TrimVideoLatent`、`MathExpression|pysssss`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`WanVaceToVideo`、`DepthAnything_V2`、`ImageComposite+`、`PulidFluxOptions`、`CR Prompt Text`、`ApplyPulidFlux`、`SamplerCustomAdvanced`、`ConditioningZeroOut`、`GetImageRangeFromBatch`、`JWInteger`、`LayerUtility: ImageScaleByAspectRatio V2`、`PDIMAGE_LongerSize`、`Text Concatenate`、`RepeatImageBatch`、`ImageConcanate`、`LoadImage`、`PMRF`、`RH_LLMAPI_NODE`、`JWImageResizeByLongerSide`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
