---
key: 图片生成/图生图/Flux Kontext Dev人物动作修改双重ID一致性V1（Nunchaku）_1939935086693552129.json
name: Flux Kontext Dev人物动作修改双重ID一致性V1（Nunchaku）_1939935086693552129
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev人物动作修改双重ID一致性V1（Nunchaku）_1939935086693552129.json
hash: 379bf7e47b7096a7
coverage: 0.879518
learned_at: 2026-10-23 10:56:57
nodes: [VAELoader, ConditioningZeroOut, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, NunchakuFluxDiTLoader, CR Prompt Text, KSampler, PreviewImage, MagCache, UnetLoaderGGUF, LoraLoaderModelOnly, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader, EmptySD3LatentImage, CM_NumberUnaryOperation, CM_NumberToInt, ImageScale, KSampler, CM_NumberToInt, LayerMask: MaskGrow, InstantIDModelLoader, ControlNetLoader, SetLatentNoiseMask, VAEEncode, InstantIDFaceAnalysis, ControlNetApplyAdvanced, VAEDecode, ImageScaleBy, LayerMask: MaskGrow, CM_IntToFloat, LayerMask: PersonMaskUltra V2, ImageScaleBy, CR Upscale Image, CM_IntToNumber, PreviewImage, MaskPreview+, GetImageSize+, CLIPTextEncode, ControlNetLoader, PreviewImage, LayerUtility: LayerImageTransform, PreviewImage, easy imageColorMatch, PreviewImage, PreviewImage, PreviewImage, Image Comparer (rgthree), ImageScale, LayerUtility: CropBoxResolve, CM_IntToFloat, LayerUtility: CropByMask, LayerMask: PersonMaskUltra V2, CLIPTextEncode, FaceBoundingBox, PreviewImage, FaceAnalysisModels, JWImageResizeByLongerSide, PMRF, LayerUtility: LayerImageTransform, SaveImage, SaveImage, JWImageResizeByLongerSide, SaveImage, VAEDecode, ImageConcanate, ImageConcanate, SaveImage, ImageComposite+, LoadImage, ImageConcanate, SaveImage, SaveImage, CheckpointLoaderSimple, ApplyInstantID, ApplyFBCacheOnModel]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 0.1, "denoise": 0.5, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 704098276559230, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux Kontext Dev人物动作修改双重ID一致性V1（Nunchaku）_1939935086693552129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev人物动作修改双重ID一致性V1（Nunchaku）_1939935086693552129.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（83 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `CR Prompt Text`
- `KSampler` ★核心
- `PreviewImage`
- `MagCache`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `EmptySD3LatentImage`
- `CM_NumberUnaryOperation`
- `CM_NumberToInt`
- `ImageScale`
- `KSampler` ★核心
- `CM_NumberToInt`
- `LayerMask: MaskGrow`
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
- `ControlNetLoader`
- `PreviewImage`
- `LayerUtility: LayerImageTransform`
- `PreviewImage`
- `easy imageColorMatch`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageScale`
- `LayerUtility: CropBoxResolve`
- `CM_IntToFloat`
- `LayerUtility: CropByMask`
- `LayerMask: PersonMaskUltra V2`
- `CLIPTextEncode` ★核心
- `FaceBoundingBox`
- `PreviewImage`
- `FaceAnalysisModels`
- `JWImageResizeByLongerSide`
- `PMRF`
- `LayerUtility: LayerImageTransform`
- `SaveImage`
- `SaveImage`
- `JWImageResizeByLongerSide`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `SaveImage`
- `ImageComposite+`
- `LoadImage`
- `ImageConcanate`
- `SaveImage`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `ApplyInstantID`
- `ApplyFBCacheOnModel`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `704098276559230`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.5`
- `controlnet_strength` = `0.1`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`

## 知识

覆盖率 **88%**（73/83）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`CR Prompt Text`、`KSampler`、`MagCache`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`NunchakuFluxLoraLoader`、`EmptySD3LatentImage`、`CM_NumberUnaryOperation`、`CM_NumberToInt`、`ImageScale`、`LayerMask: MaskGrow`、`InstantIDModelLoader`、`ControlNetLoader`、`SetLatentNoiseMask`、`InstantIDFaceAnalysis`、`ControlNetApplyAdvanced`、`VAEDecode`、`ImageScaleBy`、`CM_IntToFloat`、`LayerMask: PersonMaskUltra V2`、`CR Upscale Image`、`CM_IntToNumber`、`MaskPreview+`、`GetImageSize+`、`LayerUtility: LayerImageTransform`、`easy imageColorMatch`、`LayerUtility: CropBoxResolve`、`LayerUtility: CropByMask`、`FaceBoundingBox`、`FaceAnalysisModels`、`JWImageResizeByLongerSide`、`PMRF`、`SaveImage`、`ImageConcanate`、`ImageComposite+`、`LoadImage`、`CheckpointLoaderSimple`、`ApplyInstantID`、`ApplyFBCacheOnModel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
