---
key: （方案2）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态V2_1951200400257036289.json
name: （方案2）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态V2_1951200400257036289
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/（方案2）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态V2_1951200400257036289.json
hash: b34649c9ff2065c8
coverage: 0.725664
learned_at: 2026-10-10 21:00:00
nodes: [KSamplerSelect, Note, DualCLIPLoader, PathchSageAttentionKJ, ModelSamplingSD3, CLIPTextEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, KSampler, ControlNetLoader, SetUnionControlNetType, SetUnionControlNetType, SamplerCustomAdvanced, BasicScheduler, BasicGuider, CLIPTextEncode, ConditioningZeroOut, ControlNetApplyAdvanced, DownloadAndLoadDepthAnythingV2Model, JWInteger, LoadImage, EmptySD3LatentImage, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, CM_NumberUnaryOperation, CM_NumberToInt, ImageScale, CM_NumberToInt, LayerMask: MaskGrow, ControlNetLoader, SetLatentNoiseMask, VAEEncode, InstantIDFaceAnalysis, ControlNetApplyAdvanced, VAEDecode, ImageScaleBy, LayerMask: MaskGrow, CM_IntToFloat, LayerMask: PersonMaskUltra V2, ImageScaleBy, CR Upscale Image, CM_IntToNumber, PreviewImage, MaskPreview+, GetImageSize+, CLIPTextEncode, easy imageColorMatch, PreviewImage, PreviewImage, Image Comparer (rgthree), ImageScale, LayerUtility: CropBoxResolve, CM_IntToFloat, LayerUtility: CropByMask, LayerMask: PersonMaskUltra V2, CLIPTextEncode, PreviewImage, LayerUtility: LayerImageTransform, SaveImage, CheckpointLoaderSimple, ApplyInstantID, ApplyFBCacheOnModel, FaceAnalysisModels, FaceBoundingBox, PrimitiveNode, JWImageResizeByLongerSide, LayerUtility: LayerImageTransform, PreviewImage, PreviewImage, PreviewImage, KSampler, InstantIDModelLoader, ControlNetLoader, ImpactSwitch, DepthAnything_V2, OpenposePreprocessor, SaveImage, SeedVR2, ImageComposite+, ControlNetLoader, PDIMAGE_LongerSize, LayerUtility: PurgeVRAM, VAEDecode, Note, FluxGuidance, VAELoader, SaveImage, KSampler, SaveImage, SaveImage, VAEDecode, CR Prompt Text, CLIPTextEncode, RH_Captioner, VAEDecode, Bjornulf_TextToStringAndSeed, RandomNoise, ImageConcanate, SaveImage, NunchakuFluxDiTLoader, LoadImage, NunchakuFluxPuLIDApplyV2, NunchakuPuLIDLoaderV2, ImpactSwitch]
patterns: [image_to_image]
missing: [ImageComposite+, LayerMask: MaskGrow, LayerMask: MaskGrow, LayerMask: PersonMaskUltra V2, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask, LayerUtility: LayerImageTransform, LayerUtility: LayerImageTransform, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, easy imageColorMatch, CR Prompt Text, CR Upscale Image, GetImageSize+, MaskPreview+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 0.1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 497163970725457, "steps": 10}
discoveries: [次要节点 `ImageComposite+` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropBoxResolve` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropByMask` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LayerImageTransform` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: LayerImageTransform` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Upscale Image` 仅有 Upscale 的通用知识，没有该节点自己的说明, 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# （方案2）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态V2_1951200400257036289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/（方案2）Wan2.2+Krea+Cn2.0（姿势_深度）+Pulid+InstantID全生态V2_1951200400257036289.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（113 个）：
- `KSamplerSelect` ★核心
- `Note`
- `DualCLIPLoader`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `ControlNetLoader`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `BasicGuider`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced` ★核心
- `DownloadAndLoadDepthAnythingV2Model`
- `JWInteger`
- `LoadImage`
- `EmptySD3LatentImage`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
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
- `LayerUtility: LayerImageTransform`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `ApplyInstantID`
- `ApplyFBCacheOnModel`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `PrimitiveNode`
- `JWImageResizeByLongerSide`
- `LayerUtility: LayerImageTransform`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `KSampler` ★核心
- `InstantIDModelLoader`
- `ControlNetLoader`
- `ImpactSwitch`
- `DepthAnything_V2`
- `OpenposePreprocessor`
- `SaveImage`
- `SeedVR2`
- `ImageComposite+`
- `ControlNetLoader`
- `PDIMAGE_LongerSize`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `Note`
- `FluxGuidance`
- `VAELoader`
- `SaveImage`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `RH_Captioner`
- `VAEDecode` ★核心
- `Bjornulf_TextToStringAndSeed`
- `RandomNoise`
- `ImageConcanate`
- `SaveImage`
- `NunchakuFluxDiTLoader`
- `LoadImage`
- `NunchakuFluxPuLIDApplyV2`
- `NunchakuPuLIDLoaderV2`
- `ImpactSwitch`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `497163970725457`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.1`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`

## 知识

覆盖率 **73%**（82/113）

**有卡**：`KSamplerSelect`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`KSampler`、`ControlNetLoader`、`SetUnionControlNetType`、`SamplerCustomAdvanced`、`BasicScheduler`、`BasicGuider`、`ConditioningZeroOut`、`ControlNetApplyAdvanced`、`DownloadAndLoadDepthAnythingV2Model`、`JWInteger`、`LoadImage`、`EmptySD3LatentImage`、`CM_NumberUnaryOperation`、`CM_NumberToInt`、`ImageScale`、`SetLatentNoiseMask`、`VAEEncode`、`InstantIDFaceAnalysis`、`VAEDecode`、`ImageScaleBy`、`CM_IntToFloat`、`CM_IntToNumber`、`SaveImage`、`CheckpointLoaderSimple`、`ApplyInstantID`、`ApplyFBCacheOnModel`、`FaceAnalysisModels`、`FaceBoundingBox`、`JWImageResizeByLongerSide`、`InstantIDModelLoader`、`DepthAnything_V2`、`OpenposePreprocessor`、`SeedVR2`、`PDIMAGE_LongerSize`、`FluxGuidance`、`RH_Captioner`、`Bjornulf_TextToStringAndSeed`、`RandomNoise`、`ImageConcanate`、`NunchakuFluxDiTLoader`、`NunchakuFluxPuLIDApplyV2`、`NunchakuPuLIDLoaderV2`

**缺卡**（18）：`ImageComposite+`、`LayerMask: MaskGrow`、`LayerMask: MaskGrow`、`LayerMask: PersonMaskUltra V2`、`LayerMask: PersonMaskUltra V2`、`LayerUtility: CropBoxResolve`、`LayerUtility: CropByMask`、`LayerUtility: LayerImageTransform`、`LayerUtility: LayerImageTransform`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`LayerUtility: PurgeVRAM`、`easy imageColorMatch`、`CR Prompt Text`、`CR Upscale Image`、`GetImageSize+`、`MaskPreview+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `ImageComposite+` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: MaskGrow` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: PersonMaskUltra V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropBoxResolve` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropByMask` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LayerImageTransform` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: LayerImageTransform` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageColorMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Upscale Image` 仅有 Upscale 的通用知识，没有该节点自己的说明
- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `MaskPreview+` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
