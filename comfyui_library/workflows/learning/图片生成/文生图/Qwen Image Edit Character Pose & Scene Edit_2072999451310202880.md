---
key: 图片生成/文生图/Qwen Image Edit Character Pose & Scene Edit_2072999451310202880.json
name: Qwen Image Edit Character Pose & Scene Edit_2072999451310202880
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image Edit Character Pose & Scene Edit_2072999451310202880.json
hash: 723f8c3f219e77a4
coverage: 0.821429
learned_at: 2026-10-20 00:01:35
nodes: [ModelSamplingAuraFlow, CFGNorm, Mask To Image (mtb), CLIPLoader, TextEncodeQwenImageEditPlus, Image Rembg (Remove Background), VAELoader, MaskPreview+, ControlNetLoader, UpscaleModelLoader, UpscaleModelLoader, MaskPreview+, PreviewImage, LoraLoaderModelOnly, UNETLoader, ControlNetApplyAdvanced, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, VAELoader, TextEncodeQwenImageEditPlus, ReferenceLatent, UNETLoader, PreviewImage, MaskPreview+, SetLatentNoiseMask, PreviewImage, ReferenceLatent, PreviewImage, GetImageSize+, MaskToImage, PreviewImage, InstantIDFaceAnalysis, MaskPreview, MaskPreview, SolidMask, DWPreprocessor, KSampler, MaskToImage, PreviewImage, SetLatentNoiseMask, LoraLoaderModelOnly, KSampler, Image Comparer (rgthree), LayerUtility: RestoreCropBox, LoraLoaderModelOnly, PreviewImage, InspyrenetRembgLoader, ImageUpscaleWithModel, InspyrenetRembgProcess, ImageUpscaleWithModel, LayerMask: MaskGrow, TextEncodeQwenImageEditPlus, VAEEncode, Fast Groups Bypasser (rgthree), ImageResizeKJv2, LayerMask: MaskGrow, LayerUtility: RestoreCropBox, LayerUtility: RestoreCropBox, ImageCompositeMasked, VAEDecode, PreviewImage, MaskFromFaceModel, LayerUtility: CropByMask V2, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, ColorMatchImage, PreviewImage, PreviewImage, ACE_ImageFaceCrop, VAEDecode, ACE_ImageFaceCrop, PreviewImage, LayerUtility: ImageBlendAdvance, TTP_Expand_And_Mask, LayerUtility: CropByMask V2, PreviewImage, VAEEncode, LoraLoaderModelOnly, PreviewImage, LoadImage, LoadImage, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 0.5000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 189083695861360, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image Edit Character Pose & Scene Edit_2072999451310202880.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image Edit Character Pose & Scene Edit_2072999451310202880.json`

## 结构

**生成流程**：Model → Encode → Control → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `Mask To Image (mtb)`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `Image Rembg (Remove Background)`
- `VAELoader`
- `MaskPreview+`
- `ControlNetLoader`
- `UpscaleModelLoader`
- `UpscaleModelLoader`
- `MaskPreview+`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `PreviewImage`
- `MaskPreview+`
- `SetLatentNoiseMask`
- `PreviewImage`
- `ReferenceLatent`
- `PreviewImage`
- `GetImageSize+`
- `MaskToImage`
- `PreviewImage`
- `InstantIDFaceAnalysis`
- `MaskPreview`
- `MaskPreview`
- `SolidMask`
- `DWPreprocessor`
- `KSampler` ★核心
- `MaskToImage`
- `PreviewImage`
- `SetLatentNoiseMask`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `LayerUtility: RestoreCropBox`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `InspyrenetRembgLoader`
- `ImageUpscaleWithModel`
- `InspyrenetRembgProcess`
- `ImageUpscaleWithModel`
- `LayerMask: MaskGrow`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `LayerMask: MaskGrow`
- `LayerUtility: RestoreCropBox`
- `LayerUtility: RestoreCropBox`
- `ImageCompositeMasked`
- `VAEDecode` ★核心
- `PreviewImage`
- `MaskFromFaceModel`
- `LayerUtility: CropByMask V2`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `ColorMatchImage`
- `PreviewImage`
- `PreviewImage`
- `ACE_ImageFaceCrop`
- `VAEDecode` ★核心
- `ACE_ImageFaceCrop`
- `PreviewImage`
- `LayerUtility: ImageBlendAdvance`
- `TTP_Expand_And_Mask`
- `LayerUtility: CropByMask V2`
- `PreviewImage`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.5000000000000001`
- `seed` = `189083695861360`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（69/84）

**有卡**：`ModelSamplingAuraFlow`、`CFGNorm`、`Mask To Image (mtb)`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`、`Image Rembg (Remove Background)`、`VAELoader`、`MaskPreview+`、`ControlNetLoader`、`UpscaleModelLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`ControlNetApplyAdvanced`、`ReferenceLatent`、`SetLatentNoiseMask`、`GetImageSize+`、`MaskToImage`、`InstantIDFaceAnalysis`、`MaskPreview`、`SolidMask`、`DWPreprocessor`、`KSampler`、`LayerUtility: RestoreCropBox`、`InspyrenetRembgLoader`、`ImageUpscaleWithModel`、`InspyrenetRembgProcess`、`LayerMask: MaskGrow`、`VAEEncode`、`ImageResizeKJv2`、`ImageCompositeMasked`、`VAEDecode`、`MaskFromFaceModel`、`LayerUtility: CropByMask V2`、`ColorMatchImage`、`ACE_ImageFaceCrop`、`LayerUtility: ImageBlendAdvance`、`TTP_Expand_And_Mask`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、ControlNetApplyAdvanced

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
