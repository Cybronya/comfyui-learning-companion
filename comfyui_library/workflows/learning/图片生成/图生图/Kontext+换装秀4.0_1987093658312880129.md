---
key: 图片生成/图生图/Kontext+换装秀4.0_1987093658312880129.json
name: Kontext+换装秀4.0_1987093658312880129
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext+换装秀4.0_1987093658312880129.json
hash: 45accca46be52e4d
coverage: 0.897959
learned_at: 2026-10-23 11:06:10
nodes: [FluxGuidance, VAEEncode, PulidFluxEvaClipLoader, PulidFluxModelLoader, PulidFluxInsightFaceLoader, ReferenceLatent, ConditioningZeroOut, VAEEncode, VAELoader, ImageStitch, LayerUtility: ImageReel, CLIPTextEncode, ReferenceLatent, ConditioningZeroOut, LayerUtility: ImageReelComposit, FluxKontextImageScale, ApplyPulidFlux, LayerUtility: JoyCaptionBeta1, VAEDecode, PreviewImage, PreviewImage, GetImageSize+, EmptyLatentImage, Reroute, PreviewImage, UNETLoader, DualCLIPLoader, LoraLoaderModelOnly, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, easy showAnything, TextInput_, Text Concatenate (JPS), KSampler, KSampler, CLIPTextEncode, LayerMask: BenUltra, LayerMask: LoadBenModel, LayerUtility: CropByMask V2, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, LoadImage, ImageStitch, Note Plus (mtb)]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 532442943628335, "steps": 25, "width": 1536}
---

# 图片生成/图生图/Kontext+换装秀4.0_1987093658312880129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext+换装秀4.0_1987093658312880129.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `FluxGuidance`
- `VAEEncode` ★核心
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `PulidFluxInsightFaceLoader`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAELoader`
- `ImageStitch`
- `LayerUtility: ImageReel`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `LayerUtility: ImageReelComposit`
- `FluxKontextImageScale`
- `ApplyPulidFlux`
- `LayerUtility: JoyCaptionBeta1`
- `VAEDecode` ★核心
- `PreviewImage`
- `PreviewImage`
- `GetImageSize+`
- `EmptyLatentImage` ★核心
- `Reroute`
- `PreviewImage`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `easy showAnything`
- `TextInput_`
- `Text Concatenate (JPS)`
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `LayerMask: BenUltra`
- `LayerMask: LoadBenModel`
- `LayerUtility: CropByMask V2`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `LoadImage`
- `ImageStitch`
- `Note Plus (mtb)`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1536`
- `height` = `1152`
- `batch_size` = `1`
- `seed` = `532442943628335`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（44/49）

**有卡**：`FluxGuidance`、`VAEEncode`、`PulidFluxEvaClipLoader`、`PulidFluxModelLoader`、`PulidFluxInsightFaceLoader`、`ReferenceLatent`、`ConditioningZeroOut`、`VAELoader`、`ImageStitch`、`LayerUtility: ImageReel`、`CLIPTextEncode`、`LayerUtility: ImageReelComposit`、`FluxKontextImageScale`、`ApplyPulidFlux`、`LayerUtility: JoyCaptionBeta1`、`VAEDecode`、`GetImageSize+`、`EmptyLatentImage`、`UNETLoader`、`DualCLIPLoader`、`LoraLoaderModelOnly`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`TextInput_`、`Text Concatenate (JPS)`、`KSampler`、`LayerMask: BenUltra`、`LayerMask: LoadBenModel`、`LayerUtility: CropByMask V2`、`LoadImage`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Note Plus (mtb)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
