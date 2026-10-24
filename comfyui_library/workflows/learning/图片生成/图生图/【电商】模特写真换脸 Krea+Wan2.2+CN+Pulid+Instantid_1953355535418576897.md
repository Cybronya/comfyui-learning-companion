---
key: 图片生成/图生图/【电商】模特写真换脸 Krea+Wan2.2+CN+Pulid+Instantid_1953355535418576897.json
name: 【电商】模特写真换脸 Krea+Wan2.2+CN+Pulid+Instantid_1953355535418576897
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【电商】模特写真换脸 Krea+Wan2.2+CN+Pulid+Instantid_1953355535418576897.json
hash: 18c5cf3114e4a3c6
coverage: 0.863248
learned_at: 2026-10-23 11:51:02
nodes: [PulidFluxOptions, PulidFluxInsightFaceLoader, RandomNoise, PulidFluxEvaClipLoader, KSamplerSelect, PreviewImage, PreviewImage, PulidFluxFaceDetector, PreviewImage, DualCLIPLoader, LoraLoaderModelOnly, ImpactSwitch, BasicScheduler, PulidFluxModelLoader, BasicGuider, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, VAELoader, EmptySD3LatentImage, VAEDecode, CM_NumberUnaryOperation, CM_NumberToInt, CM_NumberToInt, ControlNetLoader, SetLatentNoiseMask, VAEEncode, InstantIDFaceAnalysis, ControlNetApplyAdvanced, VAEDecode, ImageScaleBy, LayerMask: MaskGrow, CM_IntToFloat, LayerMask: PersonMaskUltra V2, ImageScaleBy, CR Upscale Image, CM_IntToNumber, PreviewImage, MaskPreview+, CLIPTextEncode, easy imageColorMatch, PreviewImage, PreviewImage, CM_IntToFloat, LayerUtility: CropByMask, CLIPTextEncode, PreviewImage, LayerUtility: LayerImageTransform, CheckpointLoaderSimple, ApplyInstantID, ApplyFBCacheOnModel, FaceAnalysisModels, FaceBoundingBox, PrimitiveNode, JWImageResizeByLongerSide, LayerUtility: LayerImageTransform, KSampler, InstantIDModelLoader, ControlNetLoader, ShowText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, UNETLoader, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPTextEncode, VAELoader, VAEDecode, VAEDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPLoader, SaveImage, ModelSamplingSD3, ModelSamplingSD3, KSampler, KSampler, Bjornulf_TextToStringAndSeed, SamplerCustomAdvanced, PreviewImage, PreviewImage, GetImageSize+, ImageScale, LayerUtility: CropBoxResolve, LayerMask: MaskGrow, ImageScale, PreviewImage, LayerMask: PersonMaskUltra V2, LayerUtility: ImageReelComposit, LoadImage, ImageComposite+, LayerUtility: ImageReel, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, PDIMAGE_LongerSize, OpenposePreprocessor, SetUnionControlNetType, SetUnionControlNetType, ImpactSwitch, ControlNetLoader, JWInteger, ControlNetApplyAdvanced, LayerUtility: PurgeVRAM, ApplyPulidFlux, LoadImage, SaveImage, SaveImage, Image Comparer (rgthree), SaveImage, PreviewImage, CR Text Concatenate, RHHiddenNodes, RHHiddenNodes, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 0.6000000000000001, "denoise": 1, "sampler_name": "heun", "scheduler": "beta", "seed": 497163970725457, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/【电商】模特写真换脸 Krea+Wan2.2+CN+Pulid+Instantid_1953355535418576897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【电商】模特写真换脸 Krea+Wan2.2+CN+Pulid+Instantid_1953355535418576897.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（117 个）：
- `PulidFluxOptions`
- `PulidFluxInsightFaceLoader`
- `RandomNoise`
- `PulidFluxEvaClipLoader`
- `KSamplerSelect` ★核心
- `PreviewImage`
- `PreviewImage`
- `PulidFluxFaceDetector`
- `PreviewImage`
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `ImpactSwitch`
- `BasicScheduler`
- `PulidFluxModelLoader`
- `BasicGuider`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `CM_NumberUnaryOperation`
- `CM_NumberToInt`
- `CM_NumberToInt`
- `ControlNetLoader`
- `SetLatentNoiseMask`
- `VAEEncode` ★核心
- `InstantIDFaceAnalysis`
- `ControlNetApplyAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `LayerMask: MaskGrow`
- `CM_IntToFloat`
- `LayerMask: PersonMaskUltra V2`
- `ImageScaleBy`
- `CR Upscale Image`
- `CM_IntToNumber`
- `PreviewImage`
- `MaskPreview+`
- `CLIPTextEncode` ★核心
- `easy imageColorMatch`
- `PreviewImage`
- `PreviewImage`
- `CM_IntToFloat`
- `LayerUtility: CropByMask`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `LayerUtility: LayerImageTransform`
- `CheckpointLoaderSimple` ★核心
- `ApplyInstantID`
- `ApplyFBCacheOnModel`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `PrimitiveNode`
- `JWImageResizeByLongerSide`
- `LayerUtility: LayerImageTransform`
- `KSampler` ★核心
- `InstantIDModelLoader`
- `ControlNetLoader`
- `ShowText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `SaveImage`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `KSampler` ★核心
- `Bjornulf_TextToStringAndSeed`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `PreviewImage`
- `GetImageSize+`
- `ImageScale`
- `LayerUtility: CropBoxResolve`
- `LayerMask: MaskGrow`
- `ImageScale`
- `PreviewImage`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `ImageComposite+`
- `LayerUtility: ImageReel`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `PDIMAGE_LongerSize`
- `OpenposePreprocessor`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `ImpactSwitch`
- `ControlNetLoader`
- `JWInteger`
- `ControlNetApplyAdvanced` ★核心
- `LayerUtility: PurgeVRAM`
- `ApplyPulidFlux`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `CR Text Concatenate`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.6000000000000001`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`
- `seed` = `497163970725457`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **86%**（101/117）

**有卡**：`PulidFluxOptions`、`PulidFluxInsightFaceLoader`、`RandomNoise`、`PulidFluxEvaClipLoader`、`KSamplerSelect`、`PulidFluxFaceDetector`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`BasicScheduler`、`PulidFluxModelLoader`、`BasicGuider`、`FluxGuidance`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAELoader`、`EmptySD3LatentImage`、`VAEDecode`、`CM_NumberUnaryOperation`、`CM_NumberToInt`、`ControlNetLoader`、`SetLatentNoiseMask`、`VAEEncode`、`InstantIDFaceAnalysis`、`ControlNetApplyAdvanced`、`ImageScaleBy`、`LayerMask: MaskGrow`、`CM_IntToFloat`、`LayerMask: PersonMaskUltra V2`、`CR Upscale Image`、`CM_IntToNumber`、`MaskPreview+`、`easy imageColorMatch`、`LayerUtility: CropByMask`、`LayerUtility: LayerImageTransform`、`CheckpointLoaderSimple`、`ApplyInstantID`、`ApplyFBCacheOnModel`、`FaceAnalysisModels`、`FaceBoundingBox`、`JWImageResizeByLongerSide`、`KSampler`、`InstantIDModelLoader`、`ShowText`、`UNETLoader`、`PathchSageAttentionKJ`、`LayerUtility: PurgeVRAM`、`CLIPLoader`、`SaveImage`、`ModelSamplingSD3`、`Bjornulf_TextToStringAndSeed`、`SamplerCustomAdvanced`、`GetImageSize+`、`ImageScale`、`LayerUtility: CropBoxResolve`、`LayerUtility: ImageReelComposit`、`LoadImage`、`ImageComposite+`、`LayerUtility: ImageReel`、`DepthAnything_V2`、`DownloadAndLoadDepthAnythingV2Model`、`PDIMAGE_LongerSize`、`OpenposePreprocessor`、`SetUnionControlNetType`、`JWInteger`、`ApplyPulidFlux`、`CR Text Concatenate`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
