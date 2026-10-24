---
key: 图片生成/图生图/Kontext-模特换装_2.0_1950950998808395778.json
name: Kontext-模特换装_2.0_1950950998808395778
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext-模特换装_2.0_1950950998808395778.json
hash: 3fd47d517e07b565
coverage: 0.93617
learned_at: 2026-10-23 11:06:23
nodes: [VAELoader, LoraLoaderModelOnly, CLIPTextEncode, ConditioningZeroOut, ReferenceLatent, CLIPTextEncode, LayerMask: LoadBenModel, TextInput_, VAEEncode, VAEEncode, KSampler, UNETLoader, DualCLIPLoader, Anything Everywhere, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, Text Concatenate (JPS), ApplyPulidFlux, PulidFluxModelLoader, PulidFluxInsightFaceLoader, PulidFluxEvaClipLoader, VAEDecode, LayerMask: BenUltra, FluxKontextImageScale, LayerUtility: CropByMask V2, ImageStitch, ConditioningZeroOut, GetImageSize+, EmptyLatentImage, KSampler, VAEDecode, FluxGuidance, ReferenceLatent, ImageScaleToTotalPixels, UpscaleModelLoader, ImageUpscaleWithModel, LayerUtility: JoyCaptionBeta1, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Int, LoadImage, LoadImage, SaveImage, easy hiresFix, PrimitiveNode, Image Comparer (rgthree)]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 493831901610657, "steps": 25, "width": 1536}
---

# 图片生成/图生图/Kontext-模特换装_2.0_1950950998808395778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext-模特换装_2.0_1950950998808395778.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `LayerMask: LoadBenModel`
- `TextInput_`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `Anything Everywhere`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `Text Concatenate (JPS)`
- `ApplyPulidFlux`
- `PulidFluxModelLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxEvaClipLoader`
- `VAEDecode` ★核心
- `LayerMask: BenUltra`
- `FluxKontextImageScale`
- `LayerUtility: CropByMask V2`
- `ImageStitch`
- `ConditioningZeroOut`
- `GetImageSize+`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `FluxGuidance`
- `ReferenceLatent`
- `ImageScaleToTotalPixels`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `LayerUtility: JoyCaptionBeta1`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `easy hiresFix`
- `PrimitiveNode`
- `Image Comparer (rgthree)`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `493831901610657`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1536`
- `height` = `1152`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（44/47）

**有卡**：`VAELoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`LayerMask: LoadBenModel`、`TextInput_`、`VAEEncode`、`KSampler`、`UNETLoader`、`DualCLIPLoader`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`Text Concatenate (JPS)`、`ApplyPulidFlux`、`PulidFluxModelLoader`、`PulidFluxInsightFaceLoader`、`PulidFluxEvaClipLoader`、`VAEDecode`、`LayerMask: BenUltra`、`FluxKontextImageScale`、`LayerUtility: CropByMask V2`、`ImageStitch`、`GetImageSize+`、`EmptyLatentImage`、`FluxGuidance`、`ImageScaleToTotalPixels`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`LoadImage`、`SaveImage`、`easy hiresFix`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
