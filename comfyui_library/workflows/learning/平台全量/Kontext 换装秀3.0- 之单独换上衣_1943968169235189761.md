---
key: 平台全量/Kontext 换装秀3.0- 之单独换上衣_1943968169235189761.json
name: Kontext 换装秀3.0- 之单独换上衣_1943968169235189761
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext 换装秀3.0- 之单独换上衣_1943968169235189761.json
hash: e59a36796972e6e8
coverage: 0.90566
learned_at: 2026-11-14 00:34:39
nodes: [FluxKontextImageScale, FluxGuidance, ImageStitch, GetImageSize+, VAEEncode, Text Concatenate (JPS), PulidFluxEvaClipLoader, PulidFluxModelLoader, ApplyPulidFlux, PulidFluxInsightFaceLoader, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, Reroute, ReferenceLatent, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, ConditioningZeroOut, VAEEncode, VAEDecode, CLIPTextEncode, ImageAndMaskPreview, PreviewImage, PreviewImage, AddMask, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, EmptyLatentImage, KSampler, TextInput_, PreviewImage, PreviewImage, VAEDecode, LayerUtility: ImageReel, LayerUtility: JoyCaptionBeta1, KSampler, UNETLoader, DualCLIPLoader, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, AddMask, LayerMask: PersonMaskUltra V2, ImageAndMaskPreview, LayerMask: LoadBenModel, LayerMask: BenUltra, LayerUtility: CropByMask V2, LayerUtility: ImageReelComposit, SaveImage, SaveImage, ClothesSegment]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 597020376105838, "steps": 12, "width": 1536}
---

# 平台全量/Kontext 换装秀3.0- 之单独换上衣_1943968169235189761.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext 换装秀3.0- 之单独换上衣_1943968169235189761.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `FluxKontextImageScale`
- `FluxGuidance`
- `ImageStitch`
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
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ImageAndMaskPreview`
- `PreviewImage`
- `PreviewImage`
- `AddMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextInput_`
- `PreviewImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `LayerUtility: JoyCaptionBeta1`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `AddMask`
- `LayerMask: PersonMaskUltra V2`
- `ImageAndMaskPreview`
- `LayerMask: LoadBenModel`
- `LayerMask: BenUltra`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `SaveImage`
- `ClothesSegment`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1536`
- `height` = `1152`
- `batch_size` = `1`
- `seed` = `597020376105838`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（48/53）

**有卡**：`FluxKontextImageScale`、`FluxGuidance`、`ImageStitch`、`GetImageSize+`、`VAEEncode`、`Text Concatenate (JPS)`、`PulidFluxEvaClipLoader`、`PulidFluxModelLoader`、`ApplyPulidFlux`、`PulidFluxInsightFaceLoader`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEDecode`、`ImageAndMaskPreview`、`AddMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`TextInput_`、`LayerUtility: ImageReel`、`LayerUtility: JoyCaptionBeta1`、`UNETLoader`、`DualCLIPLoader`、`LoadImage`、`LoraLoaderModelOnly`、`LayerMask: PersonMaskUltra V2`、`LayerMask: LoadBenModel`、`LayerMask: BenUltra`、`LayerUtility: CropByMask V2`、`LayerUtility: ImageReelComposit`、`SaveImage`、`ClothesSegment`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
