---
key: 平台全量/Kontext 换装秀3.0 --之单独换裤子_1943971398694080513.json
name: Kontext 换装秀3.0 --之单独换裤子_1943971398694080513
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext 换装秀3.0 --之单独换裤子_1943971398694080513.json
hash: ecad2b10c4adc77d
coverage: 0.909091
learned_at: 2026-11-14 00:34:38
nodes: [FluxKontextImageScale, FluxGuidance, GetImageSize+, VAEEncode, Text Concatenate (JPS), PulidFluxEvaClipLoader, PulidFluxModelLoader, ApplyPulidFlux, PulidFluxInsightFaceLoader, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, Reroute, LayerMask: PersonMaskUltra V2, ImageAndMaskPreview, SaveImage, ReferenceLatent, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, ConditioningZeroOut, VAEEncode, KSampler, VAEDecode, CLIPTextEncode, ImageAndMaskPreview, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, EmptyLatentImage, easy anythingIndexSwitch, KSampler, UNETLoader, DualCLIPLoader, VAEDecode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, PreviewImage, PreviewImage, PreviewImage, ImageStitch, LayerUtility: JoyCaptionBeta1, TextInput_, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, AddMask, LayerMask: LoadBenModel, LayerMask: BenUltra, LayerUtility: CropByMask V2, AddMask, SubtractMask, PreviewImage, ClothesSegment]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 391512330559626, "steps": 12, "width": 1536}
---

# 平台全量/Kontext 换装秀3.0 --之单独换裤子_1943971398694080513.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext 换装秀3.0 --之单独换裤子_1943971398694080513.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `FluxKontextImageScale`
- `FluxGuidance`
- `GetImageSize+`
- `VAEEncode` ★核心
- `Text Concatenate (JPS)`
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `ApplyPulidFlux`
- `PulidFluxInsightFaceLoader`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `Reroute`
- `LayerMask: PersonMaskUltra V2`
- `ImageAndMaskPreview`
- `SaveImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ImageAndMaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `easy anythingIndexSwitch`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `ImageStitch`
- `LayerUtility: JoyCaptionBeta1`
- `TextInput_`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `AddMask`
- `LayerMask: LoadBenModel`
- `LayerMask: BenUltra`
- `LayerUtility: CropByMask V2`
- `AddMask`
- `SubtractMask`
- `PreviewImage`
- `ClothesSegment`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `391512330559626`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1536`
- `height` = `1152`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（50/55）

**有卡**：`FluxKontextImageScale`、`FluxGuidance`、`GetImageSize+`、`VAEEncode`、`Text Concatenate (JPS)`、`PulidFluxEvaClipLoader`、`PulidFluxModelLoader`、`ApplyPulidFlux`、`PulidFluxInsightFaceLoader`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerMask: PersonMaskUltra V2`、`ImageAndMaskPreview`、`SaveImage`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`EmptyLatentImage`、`easy anythingIndexSwitch`、`UNETLoader`、`DualCLIPLoader`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`ImageStitch`、`LayerUtility: JoyCaptionBeta1`、`TextInput_`、`LoadImage`、`LoraLoaderModelOnly`、`AddMask`、`LayerMask: LoadBenModel`、`LayerMask: BenUltra`、`LayerUtility: CropByMask V2`、`SubtractMask`、`ClothesSegment`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
