---
key: 图片生成/图生图/Background Replacement +Lighting_2049509168872165378.json
name: Background Replacement +Lighting_2049509168872165378
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Background Replacement +Lighting_2049509168872165378.json
hash: 77b6277b49b07126
coverage: 0.77381
learned_at: 2026-10-23 10:51:29
nodes: [SeedVR2LoadVAEModel, TTP_Image_Tile_Batch, ImageScaleBy, GetImageSize+, SeedVR2LoadDiTModel, GetImageSize+, TTP_Tile_image_size, ImageResize+, ImageScaleBy, SeedVR2VideoUpscaler, RMBG, RMBG, LayerUtility: ColorImage, ImageCompositeMasked, DepthAnything_V2, PreviewImage, DepthAnythingV2Preprocessor, PreviewImage, Zoe-DepthMapPreprocessor, PreviewImage, CannyEdgePreprocessor, PreviewImage, ImpactSwitch, DownloadAndLoadDepthAnythingV2Model, GetImageSizeAndCount, EmptyLatentImage, ClipLoaderGGUF, CLIPLoader, Reroute, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, GetNode, SaveImage, ImageResize+, GrowMaskWithBlur, LoraLoaderModelOnly, Convert Masks to Images, VAEDecode, CLIPTextEncode, ConditioningZeroOut, VAELoader, ImageCompositeMasked, ModelPatchLoader, KSampler, PainterFluxImageEdit, LayerMask: MaskStroke, Image Comparer (rgthree), VAEEncode, ReferenceLatent, VAEDecode, VAELoader, CLIPLoader, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, SetNode, Image Comparer (rgthree), SetNode, GetNode, PreviewImage, Text Multiline, ZImageFunControlnet, GetImageSize, PreviewImage, MaraScottIsEmptyOrNone_v1, easy ifElse, ShowText|pysssss, ImageConcatMulti, TTP_Image_Assy, Fast Groups Bypasser (rgthree), Note, LayerUtility: ImageScaleByAspectRatio V2, easy imageConcat, AILab_QwenVL, ttN concat, easy cleanGpuUsed, LoadImage, LoadImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 767446040326647, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Background Replacement +Lighting_2049509168872165378.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Background Replacement +Lighting_2049509168872165378.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `SeedVR2LoadVAEModel`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `GetImageSize+`
- `SeedVR2LoadDiTModel`
- `GetImageSize+`
- `TTP_Tile_image_size`
- `ImageResize+`
- `ImageScaleBy`
- `SeedVR2VideoUpscaler`
- `RMBG`
- `RMBG`
- `LayerUtility: ColorImage`
- `ImageCompositeMasked`
- `DepthAnything_V2`
- `PreviewImage`
- `DepthAnythingV2Preprocessor`
- `PreviewImage`
- `Zoe-DepthMapPreprocessor`
- `PreviewImage`
- `CannyEdgePreprocessor`
- `PreviewImage`
- `ImpactSwitch`
- `DownloadAndLoadDepthAnythingV2Model`
- `GetImageSizeAndCount`
- `EmptyLatentImage` ★核心
- `ClipLoaderGGUF`
- `CLIPLoader`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `GetNode`
- `SaveImage`
- `ImageResize+`
- `GrowMaskWithBlur`
- `LoraLoaderModelOnly` ★核心
- `Convert Masks to Images`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `ImageCompositeMasked`
- `ModelPatchLoader`
- `KSampler` ★核心
- `PainterFluxImageEdit`
- `LayerMask: MaskStroke`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `SetNode`
- `Image Comparer (rgthree)`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `Text Multiline`
- `ZImageFunControlnet`
- `GetImageSize`
- `PreviewImage`
- `MaraScottIsEmptyOrNone_v1`
- `easy ifElse`
- `ShowText|pysssss`
- `ImageConcatMulti`
- `TTP_Image_Assy`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageConcat`
- `AILab_QwenVL`
- `ttN concat`
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `767446040326647`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（65/84）

**有卡**：`SeedVR2LoadVAEModel`、`TTP_Image_Tile_Batch`、`ImageScaleBy`、`GetImageSize+`、`SeedVR2LoadDiTModel`、`TTP_Tile_image_size`、`ImageResize+`、`SeedVR2VideoUpscaler`、`RMBG`、`LayerUtility: ColorImage`、`ImageCompositeMasked`、`DepthAnything_V2`、`DepthAnythingV2Preprocessor`、`Zoe-DepthMapPreprocessor`、`CannyEdgePreprocessor`、`DownloadAndLoadDepthAnythingV2Model`、`GetImageSizeAndCount`、`EmptyLatentImage`、`ClipLoaderGGUF`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`、`GrowMaskWithBlur`、`Convert Masks to Images`、`VAEDecode`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAELoader`、`ModelPatchLoader`、`PainterFluxImageEdit`、`LayerMask: MaskStroke`、`VAEEncode`、`ReferenceLatent`、`Text Multiline`、`ZImageFunControlnet`、`GetImageSize`、`MaraScottIsEmptyOrNone_v1`、`ImageConcatMulti`、`TTP_Image_Assy`、`easy imageConcat`、`AILab_QwenVL`、`ttN concat`、`easy cleanGpuUsed`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
