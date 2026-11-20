---
key: 平台全量/TTP+SeedVR2人像专用高清修复放大 SeedVR2.5.1 z-image turb_2025049406134816769.json
name: TTP+SeedVR2人像专用高清修复放大 SeedVR2.5.1 z-image turb_2025049406134816769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/TTP+SeedVR2人像专用高清修复放大 SeedVR2.5.1 z-image turb_2025049406134816769.json
hash: a84b95c6b6bc42a2
coverage: 0.8
learned_at: 2026-11-14 01:01:21
nodes: [SeedVR2LoadVAEModel, VAELoader, CLIPLoader, SamplerCustom, easy showAnything, CLIPTextEncode, CLIPTextEncode, SamplerEulerAncestral, BasicScheduler, SeedVR2LoadDiTModel, SamplerCustom, VAEDecode, easy showAnything, SamplerEulerAncestral, MaskPreview, ShowText, Florence2Run, Florence2ModelLoader, Reroute, CLIPTextEncode, easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, VAEEncode, PreviewImage, LayerUtility: ImageMaskScaleAs, SamplerCustom, KSamplerSelect, BasicScheduler, DetailDaemonSamplerNode, VAEDecode, Seed (rgthree), FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, easy cleanGpuUsed, VAEDecode, ReferenceLatent, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, VAEEncode, easy imageSizeBySide, easy cleanGpuUsed, easy cleanGpuUsed, easy imageListToImageBatch, easy cleanGpuUsed, SaveImage, AILab_QwenVL, easy imageBatchToImageList, easy showAnything, PreviewImage, easy cleanGpuUsed, Reroute, ImageColorMatch+, GetNode, ImageScaleToTotalPixels, SeedVR2VideoUpscaler, ImageScaleToTotalPixelsX, easy imageSize, TTP_Image_Tile_Batch, BasicScheduler, PreviewImage, TTP_Image_Assy, InpaintCropImproved, SAM3Segment, InpaintCropImproved, PreviewImage, CheckpointLoaderSimple, SeedVR2VideoUpscaler, UNETLoader, Image Comparer (rgthree), InpaintStitchImproved, SetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, SaveImage, Image Comparer (rgthree), LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "Qwen-Rapid-AIO-NSFW-v18.1.safetensors"}
---

# 平台全量/TTP+SeedVR2人像专用高清修复放大 SeedVR2.5.1 z-image turb_2025049406134816769.json

> 来源文件 `comfyui_library/workflows/平台全量/TTP+SeedVR2人像专用高清修复放大 SeedVR2.5.1 z-image turb_2025049406134816769.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（80 个）：
- `SeedVR2LoadVAEModel`
- `VAELoader`
- `CLIPLoader`
- `SamplerCustom` ★核心
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SamplerEulerAncestral` ★核心
- `BasicScheduler`
- `SeedVR2LoadDiTModel`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `easy showAnything`
- `SamplerEulerAncestral` ★核心
- `MaskPreview`
- `ShowText`
- `Florence2Run`
- `Florence2ModelLoader`
- `Reroute`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `PreviewImage`
- `LayerUtility: ImageMaskScaleAs`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `DetailDaemonSamplerNode` ★核心
- `VAEDecode` ★核心
- `Seed (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `easy imageSizeBySide`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy imageListToImageBatch`
- `easy cleanGpuUsed`
- `SaveImage`
- `AILab_QwenVL`
- `easy imageBatchToImageList`
- `easy showAnything`
- `PreviewImage`
- `easy cleanGpuUsed`
- `Reroute`
- `ImageColorMatch+`
- `GetNode`
- `ImageScaleToTotalPixels`
- `SeedVR2VideoUpscaler`
- `ImageScaleToTotalPixelsX`
- `easy imageSize`
- `TTP_Image_Tile_Batch`
- `BasicScheduler`
- `PreviewImage`
- `TTP_Image_Assy`
- `InpaintCropImproved`
- `SAM3Segment`
- `InpaintCropImproved`
- `PreviewImage`
- `CheckpointLoaderSimple` ★核心
- `SeedVR2VideoUpscaler`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `InpaintStitchImproved`
- `SetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `GetNode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`

## 关键参数

- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v18.1.safetensors`

## 知识

覆盖率 **80%**（64/80）

**有卡**：`SeedVR2LoadVAEModel`、`VAELoader`、`CLIPLoader`、`SamplerCustom`、`CLIPTextEncode`、`SamplerEulerAncestral`、`BasicScheduler`、`SeedVR2LoadDiTModel`、`VAEDecode`、`MaskPreview`、`ShowText`、`Florence2Run`、`Florence2ModelLoader`、`easy cleanGpuUsed`、`VAEEncode`、`LayerUtility: ImageMaskScaleAs`、`KSamplerSelect`、`DetailDaemonSamplerNode`、`Seed (rgthree)`、`FluxKontextMultiReferenceLatentMethod`、`ReferenceLatent`、`TextEncodeQwenImageEditPlus`、`easy imageSizeBySide`、`easy imageListToImageBatch`、`SaveImage`、`AILab_QwenVL`、`easy imageBatchToImageList`、`ImageColorMatch+`、`ImageScaleToTotalPixels`、`SeedVR2VideoUpscaler`、`ImageScaleToTotalPixelsX`、`easy imageSize`、`TTP_Image_Tile_Batch`、`TTP_Image_Assy`、`InpaintCropImproved`、`SAM3Segment`、`CheckpointLoaderSimple`、`UNETLoader`、`InpaintStitchImproved`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、DetailDaemonSamplerNode
