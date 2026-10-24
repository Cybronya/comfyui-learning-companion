---
key: 图片生成/图生图/四阶段混元world-Kontext人物+场景-Wan修改动作-InstantID修复ID V2_1949407703245434882.json
name: 四阶段混元world-Kontext人物+场景-Wan修改动作-InstantID修复ID V2_1949407703245434882
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/四阶段混元world-Kontext人物+场景-Wan修改动作-InstantID修复ID V2_1949407703245434882.json
hash: ce362cb6c90602e6
coverage: 0.897436
learned_at: 2026-10-23 12:37:35
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, VAEDecode, FluxKontextImageScale, SaveImage, KSampler, FastCanvasTool, PreviewImage, RMBG, ImageCropper, TTP_Expand_And_Mask, LoraLoaderModelOnly, TeaCache, LoadImage, CR Prompt Text, FastCanvas, UnetLoaderGGUF, ImageConcanate, SaveImage, CLIPLoader, VAELoader, CLIPTextEncode, ModelSamplingSD3, PathchSageAttentionKJ, TrimVideoLatent, WanVaceToVideo, VAEDecode, VHS_VideoCombine, UNETLoader, SaveImage, ImageConcanate, ImageConcanate, CLIPTextEncode, LayerUtility: PurgeVRAM, PDIMAGE_LongerSize, MathExpression|pysssss, PreviewImage, KSampler, JWInteger, DWPreprocessor, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RepeatImageBatch, CM_NumberUnaryOperation, CM_NumberToInt, ImageScale, KSampler, CM_NumberToInt, LayerMask: MaskGrow, InstantIDModelLoader, ControlNetLoader, SetLatentNoiseMask, VAEEncode, InstantIDFaceAnalysis, ControlNetApplyAdvanced, VAEDecode, ImageScaleBy, LayerMask: MaskGrow, CM_IntToFloat, LayerMask: PersonMaskUltra V2, ImageScaleBy, CR Upscale Image, CM_IntToNumber, PreviewImage, MaskPreview+, GetImageSize+, CLIPTextEncode, ControlNetLoader, PreviewImage, LayerUtility: LayerImageTransform, PreviewImage, easy imageColorMatch, PreviewImage, PreviewImage, PreviewImage, Image Comparer (rgthree), ImageScale, LayerUtility: CropBoxResolve, CM_IntToFloat, LayerUtility: CropByMask, LayerMask: PersonMaskUltra V2, CLIPTextEncode, PreviewImage, FaceAnalysisModels, PMRF, LayerUtility: LayerImageTransform, ApplyFBCacheOnModel, FaceBoundingBox, JWImageResizeByLongerSide, ApplyInstantID, CheckpointLoaderSimple, ImageComposite+, PDIMAGE_LongerSize, PDIMAGE_LongerSize, GetImageRangeFromBatch, UNETLoader, LoraLoaderModelOnly, SaveImage, SaveImage, SaveImage, LoadImage, SaveImage, PDIMAGE_LongerSize, ImageConcanate, PDIMAGE_LongerSize, CR Prompt Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "juggernautXL_v9Rdphoto2Lightning.safetensors", "controlnet_strength": 0.1, "denoise": 0.5, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 1082905511505657, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/四阶段混元world-Kontext人物+场景-Wan修改动作-InstantID修复ID V2_1949407703245434882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/四阶段混元world-Kontext人物+场景-Wan修改动作-InstantID修复ID V2_1949407703245434882.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（117 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `PreviewImage`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `SaveImage`
- `KSampler` ★核心
- `FastCanvasTool`
- `PreviewImage`
- `RMBG`
- `ImageCropper`
- `TTP_Expand_And_Mask`
- `LoraLoaderModelOnly` ★核心
- `TeaCache`
- `LoadImage`
- `CR Prompt Text`
- `FastCanvas`
- `UnetLoaderGGUF` ★核心
- `ImageConcanate`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `TrimVideoLatent`
- `WanVaceToVideo`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `SaveImage`
- `ImageConcanate`
- `ImageConcanate`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `PDIMAGE_LongerSize`
- `MathExpression|pysssss`
- `PreviewImage`
- `KSampler` ★核心
- `JWInteger`
- `DWPreprocessor`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RepeatImageBatch`
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
- `PreviewImage`
- `FaceAnalysisModels`
- `PMRF`
- `LayerUtility: LayerImageTransform`
- `ApplyFBCacheOnModel`
- `FaceBoundingBox`
- `JWImageResizeByLongerSide`
- `ApplyInstantID`
- `CheckpointLoaderSimple` ★核心
- `ImageComposite+`
- `PDIMAGE_LongerSize`
- `PDIMAGE_LongerSize`
- `GetImageRangeFromBatch`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `PDIMAGE_LongerSize`
- `ImageConcanate`
- `PDIMAGE_LongerSize`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1082905511505657`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.5`
- `controlnet_strength` = `0.1`
- `checkpoint` = `juggernautXL_v9Rdphoto2Lightning.safetensors`

## 知识

覆盖率 **90%**（105/117）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`VAEDecode`、`FluxKontextImageScale`、`SaveImage`、`KSampler`、`FastCanvasTool`、`RMBG`、`ImageCropper`、`TTP_Expand_And_Mask`、`LoraLoaderModelOnly`、`TeaCache`、`LoadImage`、`CR Prompt Text`、`FastCanvas`、`UnetLoaderGGUF`、`ImageConcanate`、`CLIPLoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`TrimVideoLatent`、`WanVaceToVideo`、`VHS_VideoCombine`、`UNETLoader`、`LayerUtility: PurgeVRAM`、`PDIMAGE_LongerSize`、`MathExpression|pysssss`、`JWInteger`、`DWPreprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`RepeatImageBatch`、`CM_NumberUnaryOperation`、`CM_NumberToInt`、`ImageScale`、`LayerMask: MaskGrow`、`InstantIDModelLoader`、`ControlNetLoader`、`SetLatentNoiseMask`、`InstantIDFaceAnalysis`、`ControlNetApplyAdvanced`、`ImageScaleBy`、`CM_IntToFloat`、`LayerMask: PersonMaskUltra V2`、`CR Upscale Image`、`CM_IntToNumber`、`MaskPreview+`、`GetImageSize+`、`LayerUtility: LayerImageTransform`、`easy imageColorMatch`、`LayerUtility: CropBoxResolve`、`LayerUtility: CropByMask`、`FaceAnalysisModels`、`PMRF`、`ApplyFBCacheOnModel`、`FaceBoundingBox`、`JWImageResizeByLongerSide`、`ApplyInstantID`、`CheckpointLoaderSimple`、`ImageComposite+`、`GetImageRangeFromBatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
