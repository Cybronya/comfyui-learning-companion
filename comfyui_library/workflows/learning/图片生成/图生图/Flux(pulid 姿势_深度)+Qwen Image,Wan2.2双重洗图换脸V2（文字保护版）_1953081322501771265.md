---
key: 图片生成/图生图/Flux(pulid 姿势_深度)+Qwen Image,Wan2.2双重洗图换脸V2（文字保护版）_1953081322501771265.json
name: Flux(pulid 姿势_深度)+Qwen Image,Wan2.2双重洗图换脸V2（文字保护版）_1953081322501771265
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux(pulid 姿势_深度)+Qwen Image,Wan2.2双重洗图换脸V2（文字保护版）_1953081322501771265.json
hash: 1bb91352c7a5736e
coverage: 0.871622
learned_at: 2026-10-23 10:58:12
nodes: [BasicScheduler, EmptySD3LatentImage, PrimitiveNode, DualCLIPLoader, VAELoader, CLIPTextEncode, KSamplerSelect, PrimitiveNode, ModelSamplingFlux, ControlNetApplyAdvanced, FluxGuidance, BasicGuider, ImageConcanate, JWImageResizeByLongerSide, ImageConcanate, JWImageResizeByLongerSide, LayerUtility: PurgeVRAM, SamplerCustomAdvanced, DownloadAndLoadDepthAnythingV2Model, SetUnionControlNetType, SetUnionControlNetType, SaveImage, OpenposePreprocessor, JWInteger, CLIPTextEncode, CR Prompt Text, Note, Note, SaveImage, Note, Note, ControlNetLoader, CLIPLoader, ModelSamplingAuraFlow, CLIPTextEncode, VAELoader, ModelSamplingSD3, CLIPLoader, InvertMask, PreviewImage, BBoxesToSAM2, easy showAnything, LayerMask: LoadSAM2Model, LayerUtility: PurgeVRAM, LayerMask: SAM2UltraV2, LayerUtility: PurgeVRAM, MaskToImage, PreviewImage, INPAINT_ExpandMask, CLIPTextEncode, CR Prompt Text, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, SeedVR2, CLIPTextEncode, LoraLoaderModelOnly, QwenVLDetection, CR Prompt Text, InpaintModelConditioning, UNETLoader, VAELoader, VAEEncode, RH_Captioner, VAEDecode, RH_Captioner, CM_NumberUnaryOperation, CM_NumberToInt, ImageScale, KSampler, CM_NumberToInt, LayerMask: MaskGrow, ApplyInstantID, InstantIDModelLoader, ControlNetLoader, SetLatentNoiseMask, VAEEncode, InstantIDFaceAnalysis, ControlNetApplyAdvanced, VAEDecode, ImageScaleBy, LayerMask: MaskGrow, CM_IntToFloat, LayerMask: PersonMaskUltra V2, ImageScaleBy, CR Upscale Image, CM_IntToNumber, PreviewImage, MaskPreview+, GetImageSize+, CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, PreviewImage, LayerUtility: LayerImageTransform, PreviewImage, easy imageColorMatch, PreviewImage, PreviewImage, PreviewImage, ImageScale, LayerUtility: CropBoxResolve, CM_IntToFloat, JWImageResizeByLongerSide, LayerUtility: CropByMask, LayerMask: PersonMaskUltra V2, CLIPTextEncode, FaceBoundingBox, PreviewImage, FaceAnalysisModels, JWImageResizeByLongerSide, LayerUtility: LayerImageTransform, SaveImage, SaveImage, LayerUtility: PurgeVRAM V2, ImageConcanate, VAEDecode, PDIMAGE_LongerSize, SeedVR2BlockSwap, ImageComposite+, Image Comparer (rgthree), CLIPTextEncode, RandomNoise, LayerUtility: PurgeVRAM, VAEDecode, UNETLoader, LayerUtility: PurgeVRAM, DepthAnything_V2, ImpactSwitch, KSampler, LayerUtility: PurgeVRAM, SaveImage, SaveImage, LoadImage, SaveImage, KSampler, PathchSageAttentionKJ, LoraLoaderModelOnly, DownloadAndLoadQwenModel, MaskPreview+, LoraLoaderModelOnly, LoadImage, NunchakuFluxDiTLoader, ImpactSwitch, NunchakuFluxPuLIDApplyV2, NunchakuPuLIDLoaderV2, RH_Captioner, NunchakuPulidApply, NunchakuPulidLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 0.1, "denoise": 0.10000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 965369974524576, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux(pulid 姿势_深度)+Qwen Image,Wan2.2双重洗图换脸V2（文字保护版）_1953081322501771265.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux(pulid 姿势_深度)+Qwen Image,Wan2.2双重洗图换脸V2（文字保护版）_1953081322501771265.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（148 个）：
- `BasicScheduler`
- `EmptySD3LatentImage`
- `PrimitiveNode`
- `DualCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `PrimitiveNode`
- `ModelSamplingFlux`
- `ControlNetApplyAdvanced` ★核心
- `FluxGuidance`
- `BasicGuider`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `LayerUtility: PurgeVRAM`
- `SamplerCustomAdvanced` ★核心
- `DownloadAndLoadDepthAnythingV2Model`
- `SetUnionControlNetType`
- `SetUnionControlNetType`
- `SaveImage`
- `OpenposePreprocessor`
- `JWInteger`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `Note`
- `Note`
- `SaveImage`
- `Note`
- `Note`
- `ControlNetLoader`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPLoader`
- `InvertMask`
- `PreviewImage`
- `BBoxesToSAM2`
- `easy showAnything`
- `LayerMask: LoadSAM2Model`
- `LayerUtility: PurgeVRAM`
- `LayerMask: SAM2UltraV2`
- `LayerUtility: PurgeVRAM`
- `MaskToImage`
- `PreviewImage`
- `INPAINT_ExpandMask`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `SeedVR2`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenVLDetection`
- `CR Prompt Text`
- `InpaintModelConditioning`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `RH_Captioner`
- `VAEDecode` ★核心
- `RH_Captioner`
- `CM_NumberUnaryOperation`
- `CM_NumberToInt`
- `ImageScale`
- `KSampler` ★核心
- `CM_NumberToInt`
- `LayerMask: MaskGrow`
- `ApplyInstantID`
- `InstantIDModelLoader`
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
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `PreviewImage`
- `LayerUtility: LayerImageTransform`
- `PreviewImage`
- `easy imageColorMatch`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `ImageScale`
- `LayerUtility: CropBoxResolve`
- `CM_IntToFloat`
- `JWImageResizeByLongerSide`
- `LayerUtility: CropByMask`
- `LayerMask: PersonMaskUltra V2`
- `CLIPTextEncode` ★核心
- `FaceBoundingBox`
- `PreviewImage`
- `FaceAnalysisModels`
- `JWImageResizeByLongerSide`
- `LayerUtility: LayerImageTransform`
- `SaveImage`
- `SaveImage`
- `LayerUtility: PurgeVRAM V2`
- `ImageConcanate`
- `VAEDecode` ★核心
- `PDIMAGE_LongerSize`
- `SeedVR2BlockSwap`
- `ImageComposite+`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `RandomNoise`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM`
- `DepthAnything_V2`
- `ImpactSwitch`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `KSampler` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `DownloadAndLoadQwenModel`
- `MaskPreview+`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `ImpactSwitch`
- `NunchakuFluxPuLIDApplyV2`
- `NunchakuPuLIDLoaderV2`
- `RH_Captioner`
- `NunchakuPulidApply`
- `NunchakuPulidLoader`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.1`
- `seed` = `965369974524576`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`

## 知识

覆盖率 **87%**（129/148）

**有卡**：`BasicScheduler`、`EmptySD3LatentImage`、`DualCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSamplerSelect`、`ModelSamplingFlux`、`ControlNetApplyAdvanced`、`FluxGuidance`、`BasicGuider`、`ImageConcanate`、`JWImageResizeByLongerSide`、`LayerUtility: PurgeVRAM`、`SamplerCustomAdvanced`、`DownloadAndLoadDepthAnythingV2Model`、`SetUnionControlNetType`、`SaveImage`、`OpenposePreprocessor`、`JWInteger`、`CR Prompt Text`、`ControlNetLoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`ModelSamplingSD3`、`InvertMask`、`BBoxesToSAM2`、`LayerMask: LoadSAM2Model`、`LayerMask: SAM2UltraV2`、`MaskToImage`、`INPAINT_ExpandMask`、`SeedVR2`、`LoraLoaderModelOnly`、`QwenVLDetection`、`InpaintModelConditioning`、`UNETLoader`、`VAEEncode`、`RH_Captioner`、`VAEDecode`、`CM_NumberUnaryOperation`、`CM_NumberToInt`、`ImageScale`、`KSampler`、`LayerMask: MaskGrow`、`ApplyInstantID`、`InstantIDModelLoader`、`SetLatentNoiseMask`、`InstantIDFaceAnalysis`、`ImageScaleBy`、`CM_IntToFloat`、`LayerMask: PersonMaskUltra V2`、`CR Upscale Image`、`CM_IntToNumber`、`MaskPreview+`、`GetImageSize+`、`CheckpointLoaderSimple`、`LayerUtility: LayerImageTransform`、`easy imageColorMatch`、`LayerUtility: CropBoxResolve`、`LayerUtility: CropByMask`、`FaceBoundingBox`、`FaceAnalysisModels`、`LayerUtility: PurgeVRAM V2`、`PDIMAGE_LongerSize`、`SeedVR2BlockSwap`、`ImageComposite+`、`RandomNoise`、`DepthAnything_V2`、`LoadImage`、`PathchSageAttentionKJ`、`DownloadAndLoadQwenModel`、`NunchakuFluxDiTLoader`、`NunchakuFluxPuLIDApplyV2`、`NunchakuPuLIDLoaderV2`、`NunchakuPulidApply`、`NunchakuPulidLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
