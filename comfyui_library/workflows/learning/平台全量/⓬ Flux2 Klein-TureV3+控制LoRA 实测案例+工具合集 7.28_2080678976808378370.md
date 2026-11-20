---
key: 平台全量/⓬ Flux2 Klein-TureV3+控制LoRA 实测案例+工具合集 7.28_2080678976808378370.json
name: ⓬ Flux2 Klein-TureV3+控制LoRA 实测案例+工具合集 7.28_2080678976808378370
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/⓬ Flux2 Klein-TureV3+控制LoRA 实测案例+工具合集 7.28_2080678976808378370.json
hash: 95abff437c943f8d
coverage: 0.627907
learned_at: 2026-11-14 01:20:50
nodes: [EmptyLatentImage, GetNode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SeedVR2LoadVAEModel, GetNode, GetNode, SetNode, SetNode, VAELoader, SetNode, SetNode, ImageScaleToTotalPixels, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, CLIPTextEncode, ConditioningZeroOut, SetNode, GetNode, SetNode, GetNode, GetNode, VAEEncode, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, SetNode, PreviewImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ImageConcatMulti, ImageConcatMulti, GetNode, ImagePass, GetNode, SetNode, PlaySound|pysssss, VAEDecode, SetNode, PlaySound|pysssss, LoadImage, ImageConcatMulti, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImagePass, LensBlur, SetNode, ImagePass, GetNode, Fast Groups Bypasser (rgthree), PreviewImage, LayerMask: LoadSegformerModel, ImageFlip+, LayerMask: SegformerFashionSetting, LayerMask: SegformerUltraV3, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CropFace, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, GetNode, SomethingToString, GetNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, ProcessString, CLIPTextEncode, llama_cpp_instruct_adv, Fast Groups Bypasser (rgthree), CR Simple Text Watermark, LoadImage, CFGGuider, RandomNoise, SamplerCustomAdvanced, LCSColorAnchor, LCSLoadData, GetNode, GetNode, GetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LCSSharpnessCalibrate, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, JoinStringMulti, llama_cpp_model_loader, llama_cpp_parameters, GetImageSize, LCSToneAdjust, CR Image Grid Panel, ReferenceLatent, VAEEncode, ReferenceLatent, GetNode, GetNode, GetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ModelPassThrough, SetNode, LoaderGGUF, SetNode, ReferenceLatent, MarkdownNote, DWPreprocessor, OpenposePreprocessor, AIO_Preprocessor, easy cleanGpuUsed, SetNode, SetNode, ModelPassThrough, easy promptLine, DSINE-NormalMapPreprocessor, LayerUtility: SaveImagePlus, PreviewImage, PreviewImage, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, CannyEdgePreprocessor, AnyLineArtPreprocessor_aux, DepthAnythingV2Preprocessor, GetNode, SetNode, easy int, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, PreviewImage, TextInput_, LoraLoaderModelOnly, LoraLoaderModelOnly, TextInput_, UNETLoader, ImpactStringSelector, TextInput_, GetNode, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, LCSSharpnessIntervene, LoadImage, LoadImage, easy showAnything, SeedVR2VideoUpscaler, LoraLoaderModelOnly, KSamplerSelect, ImageConcatMulti, LoraLoaderModelOnly, SetNode, easy int, easy int, EmptyFlux2LatentImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, Note, Seed (rgthree), Image Comparer (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: SaveImagePlus, MarkdownNote, Note, Note, Note, Note, Note, Note, Note, TextInput_, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Note, ImpactStringSelector, ImpactStringSelector, LoadImage, SeedVR2LoadDiTModel, Note, LoadImage, LoadImage, MarkdownNote, MarkdownNote, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 512, "width": 512}
---

# 平台全量/⓬ Flux2 Klein-TureV3+控制LoRA 实测案例+工具合集 7.28_2080678976808378370.json

> 来源文件 `comfyui_library/workflows/平台全量/⓬ Flux2 Klein-TureV3+控制LoRA 实测案例+工具合集 7.28_2080678976808378370.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（258 个）：
- `EmptyLatentImage` ★核心
- `GetNode`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadVAEModel`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `ImageScaleToTotalPixels`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `SetNode`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `ImagePass`
- `GetNode`
- `SetNode`
- `PlaySound|pysssss`
- `VAEDecode` ★核心
- `SetNode`
- `PlaySound|pysssss`
- `LoadImage`
- `ImageConcatMulti`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImagePass`
- `LensBlur`
- `SetNode`
- `ImagePass`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `LayerMask: LoadSegformerModel`
- `ImageFlip+`
- `LayerMask: SegformerFashionSetting`
- `LayerMask: SegformerUltraV3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CropFace`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `GetNode`
- `SomethingToString`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `ProcessString`
- `CLIPTextEncode` ★核心
- `llama_cpp_instruct_adv`
- `Fast Groups Bypasser (rgthree)`
- `CR Simple Text Watermark`
- `LoadImage`
- `CFGGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LCSColorAnchor`
- `LCSLoadData`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LCSSharpnessCalibrate`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `JoinStringMulti`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `GetImageSize`
- `LCSToneAdjust`
- `CR Image Grid Panel`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPassThrough`
- `SetNode`
- `LoaderGGUF`
- `SetNode`
- `ReferenceLatent`
- `MarkdownNote`
- `DWPreprocessor`
- `OpenposePreprocessor`
- `AIO_Preprocessor`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `ModelPassThrough`
- `easy promptLine`
- `DSINE-NormalMapPreprocessor`
- `LayerUtility: SaveImagePlus`
- `PreviewImage`
- `PreviewImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `CannyEdgePreprocessor`
- `AnyLineArtPreprocessor_aux`
- `DepthAnythingV2Preprocessor`
- `GetNode`
- `SetNode`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `PreviewImage`
- `TextInput_`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TextInput_`
- `UNETLoader` ★核心
- `ImpactStringSelector`
- `TextInput_`
- `GetNode`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `LCSSharpnessIntervene`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `SeedVR2VideoUpscaler`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `ImageConcatMulti`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `easy int`
- `easy int`
- `EmptyFlux2LatentImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `Note`
- `Seed (rgthree)`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: SaveImagePlus`
- `MarkdownNote`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `TextInput_`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `ImpactStringSelector`
- `ImpactStringSelector`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `Note`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **63%**（162/258）

**有卡**：`EmptyLatentImage`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`VAELoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`VAEEncode`、`ReferenceLatent`、`LoadImage`、`ImageConcatMulti`、`ImagePass`、`PlaySound|pysssss`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LensBlur`、`LayerMask: LoadSegformerModel`、`ImageFlip+`、`LayerMask: SegformerFashionSetting`、`LayerMask: SegformerUltraV3`、`CropFace`、`SomethingToString`、`ProcessString`、`llama_cpp_instruct_adv`、`CR Simple Text Watermark`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`LCSColorAnchor`、`LCSLoadData`、`LCSSharpnessCalibrate`、`JoinStringMulti`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`GetImageSize`、`LCSToneAdjust`、`CR Image Grid Panel`、`ModelPassThrough`、`LoaderGGUF`、`DWPreprocessor`、`OpenposePreprocessor`、`AIO_Preprocessor`、`easy cleanGpuUsed`、`easy promptLine`、`DSINE-NormalMapPreprocessor`、`LayerUtility: SaveImagePlus`、`CannyEdgePreprocessor`、`AnyLineArtPreprocessor_aux`、`DepthAnythingV2Preprocessor`、`easy int`、`CLIPLoader`、`TextInput_`、`LoraLoaderModelOnly`、`UNETLoader`、`ImpactStringSelector`、`BasicScheduler`、`LCSSharpnessIntervene`、`SeedVR2VideoUpscaler`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`Seed (rgthree)`、`SeedVR2LoadDiTModel`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
