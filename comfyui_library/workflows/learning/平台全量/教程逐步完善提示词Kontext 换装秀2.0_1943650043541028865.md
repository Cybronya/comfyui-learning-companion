---
key: 平台全量/教程逐步完善提示词Kontext 换装秀2.0_1943650043541028865.json
name: 教程逐步完善提示词Kontext 换装秀2.0_1943650043541028865
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/教程逐步完善提示词Kontext 换装秀2.0_1943650043541028865.json
hash: 7a2113b9382bc759
coverage: 0.852459
learned_at: 2026-11-14 02:10:33
nodes: [FluxKontextImageScale, VAELoader, VAEEncode, UNETLoader, DualCLIPLoader, PulidFluxEvaClipLoader, PulidFluxModelLoader, LayerUtility: ImageScaleByAspectRatio V2, PulidFluxInsightFaceLoader, ImageConcanate, ImageConcanate, JWImageResizeByLongerSide, DownloadAndLoadFlorence2Model, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, Reroute, Florence2Run, Note, LayerUtility: JoyCaptionBeta1, EmptyLatentImage, GetImageSize+, PreviewImage, ImageAndMaskPreview, SaveImage, LayerMask: LoadBenModel, AddLabel, AddLabel, AddLabel, easy imageSizeByLongerSide, FluxGuidance, ApplyPulidFlux, LayerMask: BenUltra, ImageStitch, ConditioningZeroOut, easy showAnything, KSampler, VAEDecode, Crop Image Square (JPS), TextInput_, Text Concatenate (JPS), ImageRemoveAlpha+, PreviewImage, LayerUtility: CropByMask V2, ImageAndMaskPreview, JWImageResizeByLongerSide, Image Padding, PreviewImage, ReferenceLatent, LayerMask: PersonMaskUltra V2, Note, CLIPTextEncode, AddMask, SubtractMask, PreviewImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, PreviewImage, LoadImage, LayerMask: PersonMaskUltra V2, LayerUtility: ImageMaskScaleAsV2]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 967175738833783, "steps": 12, "width": 1536}
---

# 平台全量/教程逐步完善提示词Kontext 换装秀2.0_1943650043541028865.json

> 来源文件 `comfyui_library/workflows/平台全量/教程逐步完善提示词Kontext 换装秀2.0_1943650043541028865.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `FluxKontextImageScale`
- `VAELoader`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PulidFluxInsightFaceLoader`
- `ImageConcanate`
- `ImageConcanate`
- `JWImageResizeByLongerSide`
- `DownloadAndLoadFlorence2Model`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `Reroute`
- `Florence2Run`
- `Note`
- `LayerUtility: JoyCaptionBeta1`
- `EmptyLatentImage` ★核心
- `GetImageSize+`
- `PreviewImage`
- `ImageAndMaskPreview`
- `SaveImage`
- `LayerMask: LoadBenModel`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `easy imageSizeByLongerSide`
- `FluxGuidance`
- `ApplyPulidFlux`
- `LayerMask: BenUltra`
- `ImageStitch`
- `ConditioningZeroOut`
- `easy showAnything`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Crop Image Square (JPS)`
- `TextInput_`
- `Text Concatenate (JPS)`
- `ImageRemoveAlpha+`
- `PreviewImage`
- `LayerUtility: CropByMask V2`
- `ImageAndMaskPreview`
- `JWImageResizeByLongerSide`
- `Image Padding`
- `PreviewImage`
- `ReferenceLatent`
- `LayerMask: PersonMaskUltra V2`
- `Note`
- `CLIPTextEncode` ★核心
- `AddMask`
- `SubtractMask`
- `PreviewImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `LoadImage`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageMaskScaleAsV2`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1536`
- `height` = `1152`
- `batch_size` = `1`
- `seed` = `967175738833783`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（52/61）

**有卡**：`FluxKontextImageScale`、`VAELoader`、`VAEEncode`、`UNETLoader`、`DualCLIPLoader`、`PulidFluxEvaClipLoader`、`PulidFluxModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`PulidFluxInsightFaceLoader`、`ImageConcanate`、`JWImageResizeByLongerSide`、`DownloadAndLoadFlorence2Model`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`Florence2Run`、`LayerUtility: JoyCaptionBeta1`、`EmptyLatentImage`、`GetImageSize+`、`ImageAndMaskPreview`、`SaveImage`、`LayerMask: LoadBenModel`、`AddLabel`、`easy imageSizeByLongerSide`、`FluxGuidance`、`ApplyPulidFlux`、`LayerMask: BenUltra`、`ImageStitch`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`Crop Image Square (JPS)`、`TextInput_`、`Text Concatenate (JPS)`、`ImageRemoveAlpha+`、`LayerUtility: CropByMask V2`、`Image Padding`、`ReferenceLatent`、`LayerMask: PersonMaskUltra V2`、`CLIPTextEncode`、`AddMask`、`SubtractMask`、`LoadImage`、`LoraLoaderModelOnly`、`LayerUtility: ImageMaskScaleAsV2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
