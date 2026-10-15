---
key: 图片生成/文生图/（最强人像文生图）Wan2.2+Krea+Cn2.0+Pulid+InstantID_1951546750295330818.json
name: （最强人像文生图）Wan2.2+Krea+Cn2.0+Pulid+InstantID_1951546750295330818
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（最强人像文生图）Wan2.2+Krea+Cn2.0+Pulid+InstantID_1951546750295330818.json
hash: 3d7ac1e940008c5b
coverage: 0.815126
learned_at: 2026-10-15 22:29:10
nodes: [ControlNetLoader, InstantIDFaceAnalysis, ControlNetApplyAdvanced, CLIPTextEncode, LayerUtility: LayerImageTransform, CheckpointLoaderSimple, ApplyInstantID, ApplyFBCacheOnModel, KSampler, InstantIDModelLoader, ApplyPulidFlux, UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, DownloadAndLoadDepthAnythingV2Model, SetUnionControlNetType, DepthAnything_V2, ImpactSwitch, VAELoader, UNETLoader, PulidFluxModelLoader, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxOptions, PulidFluxFaceDetector, PreviewImage, PreviewImage, MaskPreview+, PreviewImage, CM_IntToNumber, VAEEncode, LayerMask: PersonMaskUltra V2, LayerMask: MaskGrow, SetLatentNoiseMask, LayerUtility: CropBoxResolve, GetImageSize+, CM_NumberUnaryOperation, CM_NumberToInt, PreviewImage, CM_IntToFloat, PreviewImage, PathchSageAttentionKJ, LayerUtility: PurgeVRAM, PrimitiveNode, FaceBoundingBox, FaceAnalysisModels, PreviewImage, JWInteger, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPTextEncode, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, DualCLIPLoader, PreviewImage, ImageScale, SetNode, PreviewImage, CLIPTextEncode, LayerUtility: CropByMask, CM_NumberToInt, CM_IntToFloat, ImageScaleBy, CR Upscale Image, ControlNetLoader, ImpactSwitch, LayerMask: PersonMaskUltra V2, PreviewImage, ControlNetLoader, BasicGuider, KSampler, DWPreprocessor, LayerMask: MaskGrow, ConditioningZeroOut, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, LoraLoaderModelOnly, BasicScheduler, KSamplerSelect, FluxGuidance, ImageConcanate, SetUnionControlNetType, CR Prompt Text, ControlNetApplyAdvanced, Bjornulf_TextToStringAndSeed, VAELoader, VAEEncode, SaveImage, JWImageResizeByLongerSide, SaveImage, Image Comparer (rgthree), ImageScale, PreviewImage, VAEDecode, LayerUtility: LayerImageTransform, ImageScaleBy, PreviewImage, easy imageColorMatch, PreviewImage, ImageComposite+, SaveImage, PDIMAGE_LongerSize, VAEDecode, Image Comparer (rgthree), VAEDecode, SaveImage, KSampler, Image Comparer (rgthree), PreviewImage, LoadImage, LoadImage, EmptySD3LatentImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 2.0000000000000004, "denoise": 0.05000000000000001, "sampler_name": "heun", "scheduler": "beta", "seed": 497163970725457, "steps": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/（最强人像文生图）Wan2.2+Krea+Cn2.0+Pulid+InstantID_1951546750295330818.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（最强人像文生图）Wan2.2+Krea+Cn2.0+Pulid+InstantID_1951546750295330818.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（119 个）：
- `ControlNetLoader`
- `InstantIDFaceAnalysis`
- `ControlNetApplyAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: LayerImageTransform`
- `CheckpointLoaderSimple` ★核心
- `ApplyInstantID`
- `ApplyFBCacheOnModel`
- `KSampler` ★核心
- `InstantIDModelLoader`
- `ApplyPulidFlux`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `DownloadAndLoadDepthAnythingV2Model`
- `SetUnionControlNetType`
- `DepthAnything_V2`
- `ImpactSwitch`
- `VAELoader`
- `UNETLoader` ★核心
- `PulidFluxModelLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxOptions`
- `PulidFluxFaceDetector`
- `PreviewImage`
- `PreviewImage`
- `MaskPreview+`
- `PreviewImage`
- `CM_IntToNumber`
- `VAEEncode` ★核心
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: MaskGrow`
- `SetLatentNoiseMask`
- `LayerUtility: CropBoxResolve`
- `GetImageSize+`
- `CM_NumberUnaryOperation`
- `CM_NumberToInt`
- `PreviewImage`
- `CM_IntToFloat`
- `PreviewImage`
- `PathchSageAttentionKJ`
- `LayerUtility: PurgeVRAM`
- `PrimitiveNode`
- `FaceBoundingBox`
- `FaceAnalysisModels`
- `PreviewImage`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `PreviewImage`
- `ImageScale`
- `SetNode`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: CropByMask`
- `CM_NumberToInt`
- `CM_IntToFloat`
- `ImageScaleBy`
- `CR Upscale Image`
- `ControlNetLoader`
- `ImpactSwitch`
- `LayerMask: PersonMaskUltra V2`
- `PreviewImage`
- `ControlNetLoader`
- `BasicGuider`
- `KSampler` ★核心
- `DWPreprocessor`
- `LayerMask: MaskGrow`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `FluxGuidance`
- `ImageConcanate`
- `SetUnionControlNetType`
- `CR Prompt Text`
- `ControlNetApplyAdvanced` ★核心
- `Bjornulf_TextToStringAndSeed`
- `VAELoader`
- `VAEEncode` ★核心
- `SaveImage`
- `JWImageResizeByLongerSide`
- `SaveImage`
- `Image Comparer (rgthree)`
- `ImageScale`
- `PreviewImage`
- `VAEDecode` ★核心
- `LayerUtility: LayerImageTransform`
- `ImageScaleBy`
- `PreviewImage`
- `easy imageColorMatch`
- `PreviewImage`
- `ImageComposite+`
- `SaveImage`
- `PDIMAGE_LongerSize`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `EmptySD3LatentImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `2.0000000000000004`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`
- `seed` = `497163970725457`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.05000000000000001`

## 知识

覆盖率 **82%**（97/119）

**有卡**：`ControlNetLoader`、`InstantIDFaceAnalysis`、`ControlNetApplyAdvanced`、`CLIPTextEncode`、`LayerUtility: LayerImageTransform`、`CheckpointLoaderSimple`、`ApplyInstantID`、`ApplyFBCacheOnModel`、`KSampler`、`InstantIDModelLoader`、`ApplyPulidFlux`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`DownloadAndLoadDepthAnythingV2Model`、`SetUnionControlNetType`、`DepthAnything_V2`、`VAELoader`、`PulidFluxModelLoader`、`PulidFluxEvaClipLoader`、`PulidFluxInsightFaceLoader`、`PulidFluxOptions`、`PulidFluxFaceDetector`、`MaskPreview+`、`CM_IntToNumber`、`VAEEncode`、`LayerMask: PersonMaskUltra V2`、`LayerMask: MaskGrow`、`SetLatentNoiseMask`、`LayerUtility: CropBoxResolve`、`GetImageSize+`、`CM_NumberUnaryOperation`、`CM_NumberToInt`、`CM_IntToFloat`、`LayerUtility: PurgeVRAM`、`FaceBoundingBox`、`FaceAnalysisModels`、`JWInteger`、`CLIPLoader`、`DualCLIPLoader`、`ImageScale`、`LayerUtility: CropByMask`、`ImageScaleBy`、`CR Upscale Image`、`BasicGuider`、`DWPreprocessor`、`ConditioningZeroOut`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicScheduler`、`KSamplerSelect`、`FluxGuidance`、`ImageConcanate`、`CR Prompt Text`、`Bjornulf_TextToStringAndSeed`、`SaveImage`、`JWImageResizeByLongerSide`、`VAEDecode`、`easy imageColorMatch`、`ImageComposite+`、`PDIMAGE_LongerSize`、`LoadImage`、`EmptySD3LatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
