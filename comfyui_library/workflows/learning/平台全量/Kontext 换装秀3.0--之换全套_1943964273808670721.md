---
key: 平台全量/Kontext 换装秀3.0--之换全套_1943964273808670721.json
name: Kontext 换装秀3.0--之换全套_1943964273808670721
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext 换装秀3.0--之换全套_1943964273808670721.json
hash: c7b3ce760129b9ff
coverage: 0.9
learned_at: 2026-11-14 00:34:39
nodes: [FluxGuidance, VAEEncode, PulidFluxEvaClipLoader, PulidFluxModelLoader, PulidFluxInsightFaceLoader, ReferenceLatent, ConditioningZeroOut, VAEEncode, KSampler, VAELoader, VAEDecode, KSampler, ImageStitch, LayerUtility: ImageReel, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, Text Concatenate (JPS), CLIPTextEncode, LayerMask: PersonMaskUltra V2, LayerMask: LoadBenModel, ReferenceLatent, ConditioningZeroOut, LayerUtility: ImageReelComposit, SaveImage, SaveImage, FluxKontextImageScale, ApplyPulidFlux, LayerUtility: JoyCaptionBeta1, easy showAnything, LayerMask: BenUltra, ImageAndMaskPreview, AddMask, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, PreviewImage, GetImageSize+, EmptyLatentImage, TextInput_, LayerUtility: CropByMask V2, Reroute, PreviewImage, CLIPTextEncode, UNETLoader, DualCLIPLoader, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 397358885044630, "steps": 12, "width": 1536}
---

# 平台全量/Kontext 换装秀3.0--之换全套_1943964273808670721.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext 换装秀3.0--之换全套_1943964273808670721.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `FluxGuidance`
- `VAEEncode` ★核心
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `PulidFluxInsightFaceLoader`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ImageStitch`
- `LayerUtility: ImageReel`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `Text Concatenate (JPS)`
- `CLIPTextEncode` ★核心
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: LoadBenModel`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `SaveImage`
- `FluxKontextImageScale`
- `ApplyPulidFlux`
- `LayerUtility: JoyCaptionBeta1`
- `easy showAnything`
- `LayerMask: BenUltra`
- `ImageAndMaskPreview`
- `AddMask`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `PreviewImage`
- `GetImageSize+`
- `EmptyLatentImage` ★核心
- `TextInput_`
- `LayerUtility: CropByMask V2`
- `Reroute`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `397358885044630`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1536`
- `height` = `1152`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（45/50）

**有卡**：`FluxGuidance`、`VAEEncode`、`PulidFluxEvaClipLoader`、`PulidFluxModelLoader`、`PulidFluxInsightFaceLoader`、`ReferenceLatent`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`VAEDecode`、`ImageStitch`、`LayerUtility: ImageReel`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`Text Concatenate (JPS)`、`CLIPTextEncode`、`LayerMask: PersonMaskUltra V2`、`LayerMask: LoadBenModel`、`LayerUtility: ImageReelComposit`、`SaveImage`、`FluxKontextImageScale`、`ApplyPulidFlux`、`LayerUtility: JoyCaptionBeta1`、`LayerMask: BenUltra`、`ImageAndMaskPreview`、`AddMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize+`、`EmptyLatentImage`、`TextInput_`、`LayerUtility: CropByMask V2`、`UNETLoader`、`DualCLIPLoader`、`LoadImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
