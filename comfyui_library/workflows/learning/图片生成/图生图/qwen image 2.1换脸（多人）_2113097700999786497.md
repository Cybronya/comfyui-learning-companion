---
key: 图片生成/图生图/qwen image 2.1换脸（多人）_2113097700999786497.json
name: qwen image 2.1换脸（多人）_2113097700999786497
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image 2.1换脸（多人）_2113097700999786497.json
hash: e57085bebabdd5b3
coverage: 0.535714
learned_at: 2026-10-26 22:04:15
nodes: [TextGenerateLTX2Prompt, CLIPLoader, QwenImage21Cache, PrimitiveStringMultiline, GetNode, LayerUtility: ImageBlend, PreviewImage, 取色器_孤海, LayerMask: MaskGrow, LayerUtility: ColorImage, UNETLoader, KSampler, BatchImagesNode, SaveImage, TextEncodeQwenImage21, VAELoader, CLIPLoader, PrimitiveStringMultiline, ColorMatch, SetNode, VAEDecode, easy showAnything, SetNode, Image Comparer (rgthree), SaveImage, LoadImage, MaskPreview+, ImpactInt, LoadImage, PreviewImage, MaskPreview+, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, LayerUtility: CropByMask V2, GetNode, Image Comparer (rgthree), PreviewImage, SetNode, SetNode, LayerUtility: CropBoxResolve, easy showAnything, GetNode, PreviewImage, ImageCompositeMasked, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, LayerMask: MaskGrow]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 94, "steps": 40}
---

# 图片生成/图生图/qwen image 2.1换脸（多人）_2113097700999786497.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image 2.1换脸（多人）_2113097700999786497.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `QwenImage21Cache`
- `PrimitiveStringMultiline`
- `GetNode`
- `LayerUtility: ImageBlend`
- `PreviewImage`
- `取色器_孤海`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `BatchImagesNode`
- `SaveImage`
- `TextEncodeQwenImage21`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ColorMatch`
- `SetNode`
- `VAEDecode` ★核心
- `easy showAnything`
- `SetNode`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `MaskPreview+`
- `ImpactInt`
- `LoadImage`
- `PreviewImage`
- `MaskPreview+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LayerUtility: CropByMask V2`
- `GetNode`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `LayerUtility: CropBoxResolve`
- `easy showAnything`
- `GetNode`
- `PreviewImage`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerMask: MaskGrow`

## 关键参数

- `seed` = `94`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **54%**（30/56）

**有卡**：`TextGenerateLTX2Prompt`、`CLIPLoader`、`QwenImage21Cache`、`LayerUtility: ImageBlend`、`取色器_孤海`、`LayerMask: MaskGrow`、`LayerUtility: ColorImage`、`UNETLoader`、`KSampler`、`BatchImagesNode`、`SaveImage`、`TextEncodeQwenImage21`、`VAELoader`、`ColorMatch`、`VAEDecode`、`LoadImage`、`MaskPreview+`、`ImpactInt`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`LayerUtility: CropByMask V2`、`LayerUtility: CropBoxResolve`、`ImageCompositeMasked`、`ImageResizeKJv2`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
