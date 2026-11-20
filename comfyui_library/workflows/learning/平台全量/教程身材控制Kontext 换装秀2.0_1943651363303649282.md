---
key: 平台全量/教程身材控制Kontext 换装秀2.0_1943651363303649282.json
name: 教程身材控制Kontext 换装秀2.0_1943651363303649282
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/教程身材控制Kontext 换装秀2.0_1943651363303649282.json
hash: 65368bf3469dac39
coverage: 0.868852
learned_at: 2026-11-14 02:10:33
nodes: [FluxKontextImageScale, VAELoader, VAEEncode, UNETLoader, DualCLIPLoader, ReferenceLatent, PulidFluxEvaClipLoader, PulidFluxModelLoader, LayerUtility: ImageScaleByAspectRatio V2, PulidFluxInsightFaceLoader, ImageConcanate, JWImageResizeByLongerSide, DownloadAndLoadFlorence2Model, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, Reroute, Florence2Run, Note, LayerUtility: JoyCaptionBeta1, EmptyLatentImage, GetImageSize+, PreviewImage, ImageAndMaskPreview, SaveImage, LayerMask: PersonMaskUltra V2, LayerMask: LoadBenModel, AddLabel, AddLabel, easy imageSizeByLongerSide, FluxGuidance, ApplyPulidFlux, LayerMask: BenUltra, ImageStitch, ConditioningZeroOut, easy showAnything, KSampler, VAEDecode, TextInput_, Text Concatenate (JPS), AddMask, ImageRemoveAlpha+, PreviewImage, LayerUtility: CropByMask V2, ImageAndMaskPreview, JWImageResizeByLongerSide, AddLabel, PreviewImage, CLIPTextEncode, LayerUtility: ImageMaskScaleAsV2, Crop Image Square (JPS), SubtractMask, PreviewImage, LayerMask: PersonMaskUltra V2, PreviewImage, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, Image Padding, ImageConcanate, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 889311692085251, "steps": 12, "width": 1536}
---

# 平台全量/教程身材控制Kontext 换装秀2.0_1943651363303649282.json

> 来源文件 `comfyui_library/workflows/平台全量/教程身材控制Kontext 换装秀2.0_1943651363303649282.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（61 个）：
- `FluxKontextImageScale`
- `VAELoader`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `ReferenceLatent`
- `PulidFluxEvaClipLoader`
- `PulidFluxModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PulidFluxInsightFaceLoader`
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
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: LoadBenModel`
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
- `TextInput_`
- `Text Concatenate (JPS)`
- `AddMask`
- `ImageRemoveAlpha+`
- `PreviewImage`
- `LayerUtility: CropByMask V2`
- `ImageAndMaskPreview`
- `JWImageResizeByLongerSide`
- `AddLabel`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageMaskScaleAsV2`
- `Crop Image Square (JPS)`
- `SubtractMask`
- `PreviewImage`
- `LayerMask: PersonMaskUltra V2`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Padding`
- `ImageConcanate`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1536`
- `height` = `1152`
- `batch_size` = `1`
- `seed` = `889311692085251`
- `steps` = `12`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（53/61）

**有卡**：`FluxKontextImageScale`、`VAELoader`、`VAEEncode`、`UNETLoader`、`DualCLIPLoader`、`ReferenceLatent`、`PulidFluxEvaClipLoader`、`PulidFluxModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`PulidFluxInsightFaceLoader`、`ImageConcanate`、`JWImageResizeByLongerSide`、`DownloadAndLoadFlorence2Model`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`Florence2Run`、`LayerUtility: JoyCaptionBeta1`、`EmptyLatentImage`、`GetImageSize+`、`ImageAndMaskPreview`、`SaveImage`、`LayerMask: PersonMaskUltra V2`、`LayerMask: LoadBenModel`、`AddLabel`、`easy imageSizeByLongerSide`、`FluxGuidance`、`ApplyPulidFlux`、`LayerMask: BenUltra`、`ImageStitch`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`TextInput_`、`Text Concatenate (JPS)`、`AddMask`、`ImageRemoveAlpha+`、`LayerUtility: CropByMask V2`、`CLIPTextEncode`、`LayerUtility: ImageMaskScaleAsV2`、`Crop Image Square (JPS)`、`SubtractMask`、`LoadImage`、`LoraLoaderModelOnly`、`Image Padding`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
