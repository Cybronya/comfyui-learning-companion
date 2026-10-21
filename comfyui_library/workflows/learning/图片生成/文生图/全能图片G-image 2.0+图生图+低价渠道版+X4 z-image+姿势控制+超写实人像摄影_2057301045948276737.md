---
key: 图片生成/文生图/全能图片G-image 2.0+图生图+低价渠道版+X4 z-image+姿势控制+超写实人像摄影_2057301045948276737.json
name: 全能图片G-image 2.0+图生图+低价渠道版+X4 z-image+姿势控制+超写实人像摄影_2057301045948276737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/全能图片G-image 2.0+图生图+低价渠道版+X4 z-image+姿势控制+超写实人像摄影_2057301045948276737.json
hash: e8a98f54c1b896b2
coverage: 0.841463
learned_at: 2026-10-21 02:59:01
nodes: [SaveImage, RH_RhartImageG2ImageToImage, SaveImage, RH_RhartImageG2ImageToImage, SaveImage, RH_RhartImageG2ImageToImage, SaveImage, RH_RhartImageG2ImageToImage, AspectRatioSelect, LoadImage, ConditioningZeroOut, easy showAnything, VAEDecode, ImageBatchMulti, CLIPTextEncode, VAELoader, InpaintCropImproved, SeedVR2LoadVAEModel, easy imageSizeBySide, LayerUtility: ImageScaleByAspectRatio V2, ImageUntile+, SamplerCustom, easy imageSize, ImageScaleToTotalPixels, CLIPLoader, PreviewImage, easy showAnything, VAEDecode, PreviewBridge, SamplerCustom, VAEDecode, easy showAnything, PreviewImage, SamplerCustom, DWPreprocessor, ImageTile+, SeedVR2VideoUpscaler, DetailDaemonSamplerNode, SplitSigmas, LayerMask: PersonMaskUltra V2, ImageBatchToList+, MaskPreview, SamplerCustom, SeedVR2VideoUpscaler, VAEEncode, VAEEncode, VAEDecode, SamplerCustom, VAEDecode, InpaintStitchImproved, EmptyLatentImage, SplitSigmas, easy cleanGpuUsed, PreviewImage, BasicScheduler, UNETLoader, PreviewBridge, PreviewImage, PreviewBridge, PreviewBridge, PreviewBridge, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ModelPatchLoader, ZImageFunControlnet, LoadImage, PrimitiveNode, Seed (rgthree), SaveImage, PreviewImage, PreviewBridge, Fast Groups Bypasser (rgthree), SeedVR2LoadDiTModel, Any Switch (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, easy positive, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 512, "width": 512}
---

# 图片生成/文生图/全能图片G-image 2.0+图生图+低价渠道版+X4 z-image+姿势控制+超写实人像摄影_2057301045948276737.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/全能图片G-image 2.0+图生图+低价渠道版+X4 z-image+姿势控制+超写实人像摄影_2057301045948276737.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `SaveImage`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `RH_RhartImageG2ImageToImage`
- `AspectRatioSelect`
- `LoadImage`
- `ConditioningZeroOut`
- `easy showAnything`
- `VAEDecode` ★核心
- `ImageBatchMulti`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `InpaintCropImproved`
- `SeedVR2LoadVAEModel`
- `easy imageSizeBySide`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageUntile+`
- `SamplerCustom` ★核心
- `easy imageSize`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `PreviewImage`
- `easy showAnything`
- `VAEDecode` ★核心
- `PreviewBridge`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `easy showAnything`
- `PreviewImage`
- `SamplerCustom` ★核心
- `DWPreprocessor`
- `ImageTile+`
- `SeedVR2VideoUpscaler`
- `DetailDaemonSamplerNode` ★核心
- `SplitSigmas`
- `LayerMask: PersonMaskUltra V2`
- `ImageBatchToList+`
- `MaskPreview`
- `SamplerCustom` ★核心
- `SeedVR2VideoUpscaler`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `InpaintStitchImproved`
- `EmptyLatentImage` ★核心
- `SplitSigmas`
- `easy cleanGpuUsed`
- `PreviewImage`
- `BasicScheduler`
- `UNETLoader` ★核心
- `PreviewBridge`
- `PreviewImage`
- `PreviewBridge`
- `PreviewBridge`
- `PreviewBridge`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelPatchLoader`
- `ZImageFunControlnet`
- `LoadImage`
- `PrimitiveNode`
- `Seed (rgthree)`
- `SaveImage`
- `PreviewImage`
- `PreviewBridge`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2LoadDiTModel`
- `Any Switch (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy positive`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`

## 知识

覆盖率 **84%**（69/82）

**有卡**：`SaveImage`、`RH_RhartImageG2ImageToImage`、`AspectRatioSelect`、`LoadImage`、`ConditioningZeroOut`、`VAEDecode`、`ImageBatchMulti`、`CLIPTextEncode`、`VAELoader`、`InpaintCropImproved`、`SeedVR2LoadVAEModel`、`easy imageSizeBySide`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageUntile+`、`SamplerCustom`、`easy imageSize`、`ImageScaleToTotalPixels`、`CLIPLoader`、`PreviewBridge`、`DWPreprocessor`、`ImageTile+`、`SeedVR2VideoUpscaler`、`DetailDaemonSamplerNode`、`SplitSigmas`、`LayerMask: PersonMaskUltra V2`、`ImageBatchToList+`、`MaskPreview`、`VAEEncode`、`InpaintStitchImproved`、`EmptyLatentImage`、`easy cleanGpuUsed`、`BasicScheduler`、`UNETLoader`、`KSamplerSelect`、`ModelPatchLoader`、`ZImageFunControlnet`、`Seed (rgthree)`、`SeedVR2LoadDiTModel`、`easy positive`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、UNETLoader
