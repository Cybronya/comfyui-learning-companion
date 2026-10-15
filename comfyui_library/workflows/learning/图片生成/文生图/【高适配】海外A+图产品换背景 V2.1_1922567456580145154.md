---
key: 图片生成/文生图/【高适配】海外A+图产品换背景 V2.1_1922567456580145154.json
name: 【高适配】海外A+图产品换背景 V2.1_1922567456580145154
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【高适配】海外A+图产品换背景 V2.1_1922567456580145154.json
hash: 97e9312313700f6d
coverage: 0.849315
learned_at: 2026-10-15 22:28:06
nodes: [LayerUtility: ImageRemoveAlpha, LayerUtility: ImageRemoveAlpha, Label (rgthree), Label (rgthree), ReroutePrimitive|pysssss, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Florence2ModelLoader, BrushNet, easy cleanGpuUsed, GetImageSize+, ReroutePrimitive|pysssss, VAEDecode, Image Comparer (rgthree), easy cleanGpuUsed, easy clearCacheAll, ControlNetLoader, UltimateSDUpscale, ControlNetApplySD3, AIO_Preprocessor, LoadImage, ShowText|pysssss, Fast Groups Bypasser (rgthree), ControlNetApplyAdvanced, ControlNetLoader, PreviewImage, ControlNetApplyAdvanced, AIO_Preprocessor, ControlNetLoader, GrowMask, CLIPTextEncodeFlux, VAEDecode, PreviewImage, Florence2Run, ReroutePrimitive|pysssss, ReroutePrimitive|pysssss, LamaRemover, Text Concatenate, Image Comparer (rgthree), CR Color Panel, LayerStyle: ColorOverlay V2, PreviewImage, LayerStyle: ColorOverlay V2, KSampler, UpscaleModelLoader, LoraLoaderModelOnly, LayerMask: SegmentAnythingUltra V2, PreviewImage, VAEEncode, KSampler, LoadImage, IPAdapterUnifiedLoader, IPAdapterAdvanced, easy showAnything, MaskPreview+, Image Comparer (rgthree), CLIPTextEncodeFlux, GoogleTranslateTextNode, MaskPreview+, PreviewBridge, LayerUtility: ImageBlendAdvance V3, InvertMask, AddMask, easy stylesSelector, LoadImage, Efficient Loader, BrushNetLoader, UNETLoader, DualCLIPLoader, VAELoader, LoraLoaderModelOnly, LayerStyle: ColorOverlay V2, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 1, "denoise": 0.30000000000000004, "sampler_name": "euler", "scheduler": "normal", "seed": 619405342319396, "steps": 20}
---

# 图片生成/文生图/【高适配】海外A+图产品换背景 V2.1_1922567456580145154.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【高适配】海外A+图产品换背景 V2.1_1922567456580145154.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（73 个）：
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageRemoveAlpha`
- `Label (rgthree)`
- `Label (rgthree)`
- `ReroutePrimitive|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `Florence2ModelLoader`
- `BrushNet`
- `easy cleanGpuUsed`
- `GetImageSize+`
- `ReroutePrimitive|pysssss`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `ControlNetLoader`
- `UltimateSDUpscale`
- `ControlNetApplySD3` ★核心
- `AIO_Preprocessor`
- `LoadImage`
- `ShowText|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `PreviewImage`
- `ControlNetApplyAdvanced` ★核心
- `AIO_Preprocessor`
- `ControlNetLoader`
- `GrowMask`
- `CLIPTextEncodeFlux` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `Florence2Run`
- `ReroutePrimitive|pysssss`
- `ReroutePrimitive|pysssss`
- `LamaRemover`
- `Text Concatenate`
- `Image Comparer (rgthree)`
- `CR Color Panel`
- `LayerStyle: ColorOverlay V2`
- `PreviewImage`
- `LayerStyle: ColorOverlay V2`
- `KSampler` ★核心
- `UpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LayerMask: SegmentAnythingUltra V2`
- `PreviewImage`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `IPAdapterUnifiedLoader`
- `IPAdapterAdvanced`
- `easy showAnything`
- `MaskPreview+`
- `Image Comparer (rgthree)`
- `CLIPTextEncodeFlux` ★核心
- `GoogleTranslateTextNode`
- `MaskPreview+`
- `PreviewBridge`
- `LayerUtility: ImageBlendAdvance V3`
- `InvertMask`
- `AddMask`
- `easy stylesSelector`
- `LoadImage`
- `Efficient Loader`
- `BrushNetLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LayerStyle: ColorOverlay V2`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1`
- `seed` = `619405342319396`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **85%**（62/73）

**有卡**：`LayerUtility: ImageRemoveAlpha`、`Label (rgthree)`、`ReroutePrimitive|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`Florence2ModelLoader`、`BrushNet`、`easy cleanGpuUsed`、`GetImageSize+`、`VAEDecode`、`easy clearCacheAll`、`ControlNetLoader`、`UltimateSDUpscale`、`ControlNetApplySD3`、`AIO_Preprocessor`、`LoadImage`、`ControlNetApplyAdvanced`、`GrowMask`、`CLIPTextEncodeFlux`、`Florence2Run`、`LamaRemover`、`Text Concatenate`、`CR Color Panel`、`LayerStyle: ColorOverlay V2`、`KSampler`、`UpscaleModelLoader`、`LoraLoaderModelOnly`、`LayerMask: SegmentAnythingUltra V2`、`VAEEncode`、`IPAdapterUnifiedLoader`、`IPAdapterAdvanced`、`MaskPreview+`、`GoogleTranslateTextNode`、`PreviewBridge`、`LayerUtility: ImageBlendAdvance V3`、`InvertMask`、`AddMask`、`easy stylesSelector`、`Efficient Loader`、`BrushNetLoader`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
