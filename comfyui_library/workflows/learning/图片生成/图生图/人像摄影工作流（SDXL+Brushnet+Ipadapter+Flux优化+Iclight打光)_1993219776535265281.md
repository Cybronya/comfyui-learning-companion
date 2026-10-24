---
key: 图片生成/图生图/人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1993219776535265281.json
name: 人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1993219776535265281
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1993219776535265281.json
hash: ebdb02c3dfbcdd43
coverage: 0.691489
learned_at: 2026-10-23 12:08:30
nodes: [Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, LayerUtility: ExtendCanvas, Color (hexadecimal), MaskToImage, easy cleanGpuUsed, ImageScale, easy imageSize, Reroute, easy imageScaleDownToSize, easy imageSize, LoadImage, LayerMask: SegmentAnythingUltra V2, LoadImage, IPAdapterAdvanced, IPAdapterUnifiedLoader, TextInput_, TextInput_, Reroute, Reroute, BrushNetLoader, easy cleanGpuUsed, Reroute, Reroute, Reroute, Efficient Loader, ControlNetApplyAdvanced, Reroute, BrushNet, ControlNetLoader, easy imageSize, Reroute, Reroute, EmptyLatentImage, easy cleanGpuUsed, PreviewImage, Reroute, KSampler (Efficient), LayerUtility: ImageBlend, ImageScale, Image Comparer (rgthree), Image Comparer (rgthree), ImageScaleBy, Reroute, easy imageSize, easy imageSize, Reroute, PreviewImage, LayerMask: MaskGrow, ImageToMask, MaskToImage, PreviewImage, PreviewMask_, CLIPTextEncode, LoadAndApplyICLightUnet, Reroute, UNETLoader, KSampler, IPAdapterUnifiedLoader, CheckpointLoaderSimple, VAELoader, InvertMask, GrowMask, ICLightConditioning, VAEEncode, Reroute, CLIPTextEncode, easy imageSize, EmptyLatentImage, DetailTransfer, LayerUtility: ImageBlend, VAEDecode, Image Comparer (rgthree), IPAdapterAdvanced, easy cleanGpuUsed, CLIPVisionLoader, SaveImage, DetailerForEachDebug, Image Comparer (rgthree), ConditioningZeroOut, CLIPTextEncodeFlux, VAELoader, MaskToSEGS, DualCLIPLoader, ImpactDilateMask, CannyEdgePreprocessor, Image Comparer (rgthree), UpscaleModelLoader, ImageUpscaleWithModel]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "checkpoint": "majicmixRealistic_v7.safetensors", "controlnet_strength": 0.3, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 11, "steps": 25, "width": 512}
---

# 图片生成/图生图/人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1993219776535265281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1993219776535265281.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（94 个）：
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: ExtendCanvas`
- `Color (hexadecimal)`
- `MaskToImage`
- `easy cleanGpuUsed`
- `ImageScale`
- `easy imageSize`
- `Reroute`
- `easy imageScaleDownToSize`
- `easy imageSize`
- `LoadImage`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `TextInput_`
- `TextInput_`
- `Reroute`
- `Reroute`
- `BrushNetLoader`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `Efficient Loader`
- `ControlNetApplyAdvanced` ★核心
- `Reroute`
- `BrushNet`
- `ControlNetLoader`
- `easy imageSize`
- `Reroute`
- `Reroute`
- `EmptyLatentImage` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `Reroute`
- `KSampler (Efficient)` ★核心
- `LayerUtility: ImageBlend`
- `ImageScale`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `Reroute`
- `easy imageSize`
- `easy imageSize`
- `Reroute`
- `PreviewImage`
- `LayerMask: MaskGrow`
- `ImageToMask`
- `MaskToImage`
- `PreviewImage`
- `PreviewMask_`
- `CLIPTextEncode` ★核心
- `LoadAndApplyICLightUnet`
- `Reroute`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `IPAdapterUnifiedLoader`
- `CheckpointLoaderSimple` ★核心
- `VAELoader`
- `InvertMask`
- `GrowMask`
- `ICLightConditioning`
- `VAEEncode` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `EmptyLatentImage` ★核心
- `DetailTransfer`
- `LayerUtility: ImageBlend`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `IPAdapterAdvanced`
- `easy cleanGpuUsed`
- `CLIPVisionLoader`
- `SaveImage`
- `DetailerForEachDebug`
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `CLIPTextEncodeFlux` ★核心
- `VAELoader`
- `MaskToSEGS`
- `DualCLIPLoader`
- `ImpactDilateMask`
- `CannyEdgePreprocessor`
- `Image Comparer (rgthree)`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `controlnet_strength` = `0.3`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `11`
- `steps` = `25`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `majicmixRealistic_v7.safetensors`

## 知识

覆盖率 **69%**（65/94）

**有卡**：`LayerUtility: ExtendCanvas`、`Color (hexadecimal)`、`MaskToImage`、`easy cleanGpuUsed`、`ImageScale`、`easy imageSize`、`easy imageScaleDownToSize`、`LoadImage`、`LayerMask: SegmentAnythingUltra V2`、`IPAdapterAdvanced`、`IPAdapterUnifiedLoader`、`TextInput_`、`BrushNetLoader`、`Efficient Loader`、`ControlNetApplyAdvanced`、`BrushNet`、`ControlNetLoader`、`EmptyLatentImage`、`KSampler (Efficient)`、`LayerUtility: ImageBlend`、`ImageScaleBy`、`LayerMask: MaskGrow`、`ImageToMask`、`PreviewMask_`、`CLIPTextEncode`、`LoadAndApplyICLightUnet`、`UNETLoader`、`KSampler`、`CheckpointLoaderSimple`、`VAELoader`、`InvertMask`、`GrowMask`、`ICLightConditioning`、`VAEEncode`、`DetailTransfer`、`VAEDecode`、`CLIPVisionLoader`、`SaveImage`、`DetailerForEachDebug`、`ConditioningZeroOut`、`CLIPTextEncodeFlux`、`MaskToSEGS`、`DualCLIPLoader`、`ImpactDilateMask`、`CannyEdgePreprocessor`、`UpscaleModelLoader`、`ImageUpscaleWithModel`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
