---
key: 平台全量/人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1957322367137673218.json
name: 人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1957322367137673218
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1957322367137673218.json
hash: 8db353eca344d8be
coverage: 0.669811
learned_at: 2026-11-14 01:36:15
nodes: [Note, Reroute, easy cleanGpuUsed, ImageUpscaleWithModel, Reroute, Reroute, ImageScale, PreviewImage, Reroute, Reroute, Reroute, Reroute, LayerUtility: ImageBlend, Note, Reroute, Reroute, EmptyLatentImage, ImageScale, MaskToSEGS, ConditioningZeroOut, Reroute, Reroute, ControlNetApplyAdvanced, CannyEdgePreprocessor, ControlNetLoader, DualCLIPLoader, CLIPTextEncodeFlux, Reroute, VAELoader, UNETLoader, Reroute, VAEEncode, IPAdapterAdvanced, ICLightConditioning, Reroute, ImageToMask, VAEDecode, LayerUtility: ExtendCanvas, Reroute, Reroute, EmptyLatentImage, easy imageSize, CLIPVisionLoader, DetailTransfer, easy cleanGpuUsed, LayerUtility: ImageBlend, SaveImage, Image Comparer (rgthree), easy cleanGpuUsed, Image Comparer (rgthree), Reroute, Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), UpscaleModelLoader, ImageScaleBy, easy imageSize, IPAdapterAdvanced, easy imageScaleDownToSize, Reroute, easy imageSize, PreviewImage, easy imageSize, MaskToImage, PreviewMask_, MaskToImage, easy imageSize, PreviewImage, CLIPTextEncode, CLIPTextEncode, Reroute, Note, PreviewImage, TextInput_, Reroute, InvertMask, KSampler, GrowMask, ImpactDilateMask, BrushNet, BrushNetLoader, CheckpointLoaderSimple, VAELoader, LoadAndApplyICLightUnet, IPAdapterUnifiedLoader, PreviewImage, IPAdapterUnifiedLoader, Efficient Loader, KSampler (Efficient), LayerMask: SegmentAnythingUltra V2, LoadImage, easy cleanGpuUsed, LayerMask: MaskGrow, easy imageSize, LoadImage, TextInput_, DetailerForEachDebug, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, Reroute, LoraLoaderModelOnly, Image Comparer (rgthree), QwenImageIntegratedKSampler, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "majicmixRealistic_v7.safetensors", "controlnet_strength": 0.3, "denoise": 999, "height": 512, "sampler_name": 0, "scheduler": 0, "seed": "使用自然光对图像重新照明", "steps": "图生图 image-to-image", "width": 512}
---

# 平台全量/人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1957322367137673218.json

> 来源文件 `comfyui_library/workflows/平台全量/人像摄影工作流（SDXL+Brushnet+Ipadapter+Flux优化+Iclight打光)_1957322367137673218.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（106 个）：
- `Note`
- `Reroute`
- `easy cleanGpuUsed`
- `ImageUpscaleWithModel`
- `Reroute`
- `Reroute`
- `ImageScale`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageBlend`
- `Note`
- `Reroute`
- `Reroute`
- `EmptyLatentImage` ★核心
- `ImageScale`
- `MaskToSEGS`
- `ConditioningZeroOut`
- `Reroute`
- `Reroute`
- `ControlNetApplyAdvanced` ★核心
- `CannyEdgePreprocessor`
- `ControlNetLoader`
- `DualCLIPLoader`
- `CLIPTextEncodeFlux` ★核心
- `Reroute`
- `VAELoader`
- `UNETLoader` ★核心
- `Reroute`
- `VAEEncode` ★核心
- `IPAdapterAdvanced`
- `ICLightConditioning`
- `Reroute`
- `ImageToMask`
- `VAEDecode` ★核心
- `LayerUtility: ExtendCanvas`
- `Reroute`
- `Reroute`
- `EmptyLatentImage` ★核心
- `easy imageSize`
- `CLIPVisionLoader`
- `DetailTransfer`
- `easy cleanGpuUsed`
- `LayerUtility: ImageBlend`
- `SaveImage`
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `Reroute`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `easy imageSize`
- `IPAdapterAdvanced`
- `easy imageScaleDownToSize`
- `Reroute`
- `easy imageSize`
- `PreviewImage`
- `easy imageSize`
- `MaskToImage`
- `PreviewMask_`
- `MaskToImage`
- `easy imageSize`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `Note`
- `PreviewImage`
- `TextInput_`
- `Reroute`
- `InvertMask`
- `KSampler` ★核心
- `GrowMask`
- `ImpactDilateMask`
- `BrushNet`
- `BrushNetLoader`
- `CheckpointLoaderSimple` ★核心
- `VAELoader`
- `LoadAndApplyICLightUnet`
- `IPAdapterUnifiedLoader`
- `PreviewImage`
- `IPAdapterUnifiedLoader`
- `Efficient Loader`
- `KSampler (Efficient)` ★核心
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `easy cleanGpuUsed`
- `LayerMask: MaskGrow`
- `easy imageSize`
- `LoadImage`
- `TextInput_`
- `DetailerForEachDebug`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `QwenImageIntegratedKSampler` ★核心
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `controlnet_strength` = `0.3`
- `seed` = `使用自然光对图像重新照明`
- `steps` = `图生图 image-to-image`
- `cfg` = `1`
- `sampler_name` = `0`
- `scheduler` = `0`
- `denoise` = `999`
- `checkpoint` = `majicmixRealistic_v7.safetensors`

## 知识

覆盖率 **67%**（71/106）

**有卡**：`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`ImageScale`、`LayerUtility: ImageBlend`、`EmptyLatentImage`、`MaskToSEGS`、`ConditioningZeroOut`、`ControlNetApplyAdvanced`、`CannyEdgePreprocessor`、`ControlNetLoader`、`DualCLIPLoader`、`CLIPTextEncodeFlux`、`VAELoader`、`UNETLoader`、`VAEEncode`、`IPAdapterAdvanced`、`ICLightConditioning`、`ImageToMask`、`VAEDecode`、`LayerUtility: ExtendCanvas`、`easy imageSize`、`CLIPVisionLoader`、`DetailTransfer`、`SaveImage`、`UpscaleModelLoader`、`ImageScaleBy`、`easy imageScaleDownToSize`、`MaskToImage`、`PreviewMask_`、`CLIPTextEncode`、`TextInput_`、`InvertMask`、`KSampler`、`GrowMask`、`ImpactDilateMask`、`BrushNet`、`BrushNetLoader`、`CheckpointLoaderSimple`、`LoadAndApplyICLightUnet`、`IPAdapterUnifiedLoader`、`Efficient Loader`、`KSampler (Efficient)`、`LayerMask: SegmentAnythingUltra V2`、`LoadImage`、`LayerMask: MaskGrow`、`DetailerForEachDebug`、`CLIPLoader`、`LoraLoaderModelOnly`、`QwenImageIntegratedKSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode
