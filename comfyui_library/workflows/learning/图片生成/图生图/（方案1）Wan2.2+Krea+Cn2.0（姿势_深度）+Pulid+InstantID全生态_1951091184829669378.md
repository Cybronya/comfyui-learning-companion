---
key: 图片生成/图生图/（方案1）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态_1951091184829669378.json
name: （方案1）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态_1951091184829669378
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（方案1）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态_1951091184829669378.json
hash: 67e5e248a8229785
coverage: 0.866667
learned_at: 2026-10-23 13:37:43
nodes: [PulidFluxOptions, PulidFluxInsightFaceLoader, RandomNoise, PulidFluxEvaClipLoader, KSamplerSelect, Note, PreviewImage, Note, PreviewImage, PulidFluxFaceDetector, PreviewImage, DualCLIPLoader, SaveImage, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, LoraLoaderModelOnly, Bjornulf_TextToStringAndSeed, CLIPTextEncode, UNETLoader, CR Prompt Text, KSampler, ControlNetLoader, SetUnionControlNetType, SetUnionControlNetType, ImpactSwitch, ApplyPulidFlux, SamplerCustomAdvanced, BasicScheduler, PulidFluxModelLoader, UNETLoader, BasicGuider, FluxGuidance, CLIPTextEncode, ConditioningZeroOut, VAELoader, ControlNetApplyAdvanced, DownloadAndLoadDepthAnythingV2Model, JWInteger, LoadImage, PDIMAGE_LongerSize, EmptySD3LatentImage, LayerUtility: PurgeVRAM, VAEDecode, VAEDecode, LayerUtility: PurgeVRAM, KSampler, LayerUtility: PurgeVRAM, CM_NumberUnaryOperation, CM_NumberToInt, ImageScale, CM_NumberToInt, LayerMask: MaskGrow, ControlNetLoader, SetLatentNoiseMask, VAEEncode, InstantIDFaceAnalysis, ControlNetApplyAdvanced, VAEDecode, ImageScaleBy, LayerMask: MaskGrow, CM_IntToFloat, LayerMask: PersonMaskUltra V2, ImageScaleBy, CR Upscale Image, CM_IntToNumber, PreviewImage, MaskPreview+, GetImageSize+, CLIPTextEncode, easy imageColorMatch, PreviewImage, PreviewImage, Image Comparer (rgthree), ImageScale, LayerUtility: CropBoxResolve, CM_IntToFloat, LayerUtility: CropByMask, LayerMask: PersonMaskUltra V2, CLIPTextEncode, PreviewImage, JWImageResizeByLongerSide, LayerUtility: LayerImageTransform, SaveImage, SaveImage, ImageConcanate, ImageComposite+, ImageConcanate, CheckpointLoaderSimple, ApplyInstantID, ApplyFBCacheOnModel, FaceAnalysisModels, FaceBoundingBox, PrimitiveNode, JWImageResizeByLongerSide, LayerUtility: LayerImageTransform, PreviewImage, SaveImage, SaveImage, VAEDecode, PMRF, PreviewImage, PreviewImage, KSampler, InstantIDModelLoader, ControlNetLoader, LoadImage, SaveImage, SaveImage, ImpactSwitch, DepthAnything_V2, OpenposePreprocessor]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 0.1, "denoise": 0.5, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 253074653426537, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/（方案1）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态_1951091184829669378.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（方案1）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态_1951091184829669378.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（120 个）：
- `PulidFluxOptions`
- `PulidFluxInsightFaceLoader`
- `RandomNoise`
- `PulidFluxEvaClipLoader`
- `KSamplerSelect` ★核心
- `Note`
- `PreviewImage`
- `Note`
- `PreviewImage`
- `PulidFluxFaceDetector`
- `PreviewImage`
- `DualCLIPLoader`
- `SaveImage`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Bjornulf_TextToStringAndSeed`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CR Prompt Text`
- `KSampler` ★核心
- `ControlNetLoader`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `ImpactSwitch`
- `ApplyPulidFlux`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `PulidFluxModelLoader`
- `UNETLoader` ★核心
- `BasicGuider`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `ControlNetApplyAdvanced` ★核心
- `DownloadAndLoadDepthAnythingV2Model`
- `JWInteger`
- `LoadImage`
- `PDIMAGE_LongerSize`
- `EmptySD3LatentImage`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `CM_NumberUnaryOperation`
- `CM_NumberToInt`
- `ImageScale`
- `CM_NumberToInt`
- `LayerMask: MaskGrow`
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
- `GetImageSize+`
- `CLIPTextEncode` ★核心
- `easy imageColorMatch`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageScale`
- `LayerUtility: CropBoxResolve`
- `CM_IntToFloat`
- `LayerUtility: CropByMask`
- `LayerMask: PersonMaskUltra V2`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `JWImageResizeByLongerSide`
- `LayerUtility: LayerImageTransform`
- `SaveImage`
- `SaveImage`
- `ImageConcanate`
- `ImageComposite+`
- `ImageConcanate`
- `CheckpointLoaderSimple` ★核心
- `ApplyInstantID`
- `ApplyFBCacheOnModel`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `PrimitiveNode`
- `JWImageResizeByLongerSide`
- `LayerUtility: LayerImageTransform`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `PMRF`
- `PreviewImage`
- `PreviewImage`
- `KSampler` ★核心
- `InstantIDModelLoader`
- `ControlNetLoader`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `ImpactSwitch`
- `DepthAnything_V2`
- `OpenposePreprocessor`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `253074653426537`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.5`
- `controlnet_strength` = `0.1`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`

## 知识

覆盖率 **87%**（104/120）

**有卡**：`PulidFluxOptions`、`PulidFluxInsightFaceLoader`、`RandomNoise`、`PulidFluxEvaClipLoader`、`KSamplerSelect`、`PulidFluxFaceDetector`、`DualCLIPLoader`、`SaveImage`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`Bjornulf_TextToStringAndSeed`、`CR Prompt Text`、`KSampler`、`ControlNetLoader`、`SetUnionControlNetType`、`ApplyPulidFlux`、`SamplerCustomAdvanced`、`BasicScheduler`、`PulidFluxModelLoader`、`BasicGuider`、`FluxGuidance`、`ConditioningZeroOut`、`ControlNetApplyAdvanced`、`DownloadAndLoadDepthAnythingV2Model`、`JWInteger`、`LoadImage`、`PDIMAGE_LongerSize`、`EmptySD3LatentImage`、`LayerUtility: PurgeVRAM`、`VAEDecode`、`CM_NumberUnaryOperation`、`CM_NumberToInt`、`ImageScale`、`LayerMask: MaskGrow`、`SetLatentNoiseMask`、`VAEEncode`、`InstantIDFaceAnalysis`、`ImageScaleBy`、`CM_IntToFloat`、`LayerMask: PersonMaskUltra V2`、`CR Upscale Image`、`CM_IntToNumber`、`MaskPreview+`、`GetImageSize+`、`easy imageColorMatch`、`LayerUtility: CropBoxResolve`、`LayerUtility: CropByMask`、`JWImageResizeByLongerSide`、`LayerUtility: LayerImageTransform`、`ImageConcanate`、`ImageComposite+`、`CheckpointLoaderSimple`、`ApplyInstantID`、`ApplyFBCacheOnModel`、`FaceAnalysisModels`、`FaceBoundingBox`、`PMRF`、`InstantIDModelLoader`、`DepthAnything_V2`、`OpenposePreprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
