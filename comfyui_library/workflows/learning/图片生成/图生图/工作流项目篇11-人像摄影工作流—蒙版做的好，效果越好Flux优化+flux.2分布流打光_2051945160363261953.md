---
key: 图片生成/图生图/工作流项目篇11-人像摄影工作流—蒙版做的好，效果越好Flux优化+flux.2分布流打光_2051945160363261953.json
name: 工作流项目篇11-人像摄影工作流—蒙版做的好，效果越好Flux优化+flux.2分布流打光_2051945160363261953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/工作流项目篇11-人像摄影工作流—蒙版做的好，效果越好Flux优化+flux.2分布流打光_2051945160363261953.json
hash: 3249c1e27b09859b
coverage: 0.694737
learned_at: 2026-10-23 12:50:36
nodes: [Note, Reroute, easy cleanGpuUsed, ImageUpscaleWithModel, Reroute, Reroute, ImageScale, PreviewImage, Reroute, Reroute, Reroute, Reroute, Note, Reroute, Reroute, EmptyLatentImage, ImageScale, MaskToSEGS, ConditioningZeroOut, Reroute, Reroute, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, CLIPTextEncodeFlux, Reroute, VAELoader, UNETLoader, Reroute, Reroute, ImageToMask, LayerUtility: ExtendCanvas, Reroute, easy cleanGpuUsed, Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), UpscaleModelLoader, ImageScaleBy, easy imageSize, easy imageScaleDownToSize, Reroute, easy imageSize, PreviewImage, easy imageSize, MaskToImage, PreviewMask_, MaskToImage, easy imageSize, PreviewImage, Note, TextInput_, Reroute, ImpactDilateMask, BrushNet, BrushNetLoader, LoadImage, easy cleanGpuUsed, LayerMask: MaskGrow, easy imageSize, LoadImage, LayerMask: SegmentAnythingUltra V2, CannyEdgePreprocessor, PreviewImage, Efficient Loader, TextInput_, IPAdapterAdvanced, IPAdapterUnifiedLoader, KSampler (Efficient), DetailerForEachDebug, VAEDecode, CLIPLoader, LayerUtility: PurgeVRAM, UNETLoader, KSamplerSelect, ConditioningZeroOut, CLIPTextEncode, SamplerCustomAdvanced, CFGGuider, VAELoader, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, ReferenceLatent, GetImageSize, EmptyFlux2LatentImage, SaveImage, RandomNoise, Flux2Scheduler, LoadImage, LayerUtility: ImageBlend, SaveImage, PreviewImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 5, "controlnet_strength": 0.3, "denoise": 0.8000000000000002, "height": 512, "sampler_name": "euler", "scheduler": "karras", "seed": -1, "steps": 28, "width": 512}
---

# 图片生成/图生图/工作流项目篇11-人像摄影工作流—蒙版做的好，效果越好Flux优化+flux.2分布流打光_2051945160363261953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/工作流项目篇11-人像摄影工作流—蒙版做的好，效果越好Flux优化+flux.2分布流打光_2051945160363261953.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（95 个）：
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
- `ControlNetLoader`
- `DualCLIPLoader`
- `CLIPTextEncodeFlux` ★核心
- `Reroute`
- `VAELoader`
- `UNETLoader` ★核心
- `Reroute`
- `Reroute`
- `ImageToMask`
- `LayerUtility: ExtendCanvas`
- `Reroute`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `UpscaleModelLoader`
- `ImageScaleBy`
- `easy imageSize`
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
- `Note`
- `TextInput_`
- `Reroute`
- `ImpactDilateMask`
- `BrushNet`
- `BrushNetLoader`
- `LoadImage`
- `easy cleanGpuUsed`
- `LayerMask: MaskGrow`
- `easy imageSize`
- `LoadImage`
- `LayerMask: SegmentAnythingUltra V2`
- `CannyEdgePreprocessor`
- `PreviewImage`
- `Efficient Loader`
- `TextInput_`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `KSampler (Efficient)` ★核心
- `DetailerForEachDebug`
- `VAEDecode` ★核心
- `CLIPLoader`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `RandomNoise`
- `Flux2Scheduler`
- `LoadImage`
- `LayerUtility: ImageBlend`
- `SaveImage`
- `PreviewImage`
- `CR Text`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `controlnet_strength` = `0.3`
- `seed` = `-1`
- `steps` = `28`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `karras`
- `denoise` = `0.8000000000000002`

## 知识

覆盖率 **69%**（66/95）

**有卡**：`easy cleanGpuUsed`、`ImageUpscaleWithModel`、`ImageScale`、`EmptyLatentImage`、`MaskToSEGS`、`ConditioningZeroOut`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`DualCLIPLoader`、`CLIPTextEncodeFlux`、`VAELoader`、`UNETLoader`、`ImageToMask`、`LayerUtility: ExtendCanvas`、`UpscaleModelLoader`、`ImageScaleBy`、`easy imageSize`、`easy imageScaleDownToSize`、`MaskToImage`、`PreviewMask_`、`TextInput_`、`ImpactDilateMask`、`BrushNet`、`BrushNetLoader`、`LoadImage`、`LayerMask: MaskGrow`、`LayerMask: SegmentAnythingUltra V2`、`CannyEdgePreprocessor`、`Efficient Loader`、`IPAdapterAdvanced`、`IPAdapterUnifiedLoader`、`KSampler (Efficient)`、`DetailerForEachDebug`、`VAEDecode`、`CLIPLoader`、`LayerUtility: PurgeVRAM`、`KSamplerSelect`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`CFGGuider`、`ImageScaleToTotalPixels`、`VAEEncode`、`ReferenceLatent`、`GetImageSize`、`EmptyFlux2LatentImage`、`SaveImage`、`RandomNoise`、`Flux2Scheduler`、`LayerUtility: ImageBlend`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
