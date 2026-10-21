---
key: 图片生成/文生图/【SevnFading】Qwen-Image-2.1 多合一工作流 （进阶版）_2101856561537830914.json
name: 【SevnFading】Qwen-Image-2.1 多合一工作流 （进阶版）_2101856561537830914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【SevnFading】Qwen-Image-2.1 多合一工作流 （进阶版）_2101856561537830914.json
hash: c173ad9db1c3b37b
coverage: 0.543071
learned_at: 2026-10-20 01:52:06
nodes: [VAELoader, QwenImage21Cache, KSampler, ResolutionSelector, PrimitiveInt, GetImageSize, EmptyLatentImage, VAELoader, KSampler, GetNode, PreviewImage, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, PreviewImage, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LoadImage, LoadImage, LoadImage, PreviewImage, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, GetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, LoadImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, MarkdownNote, PrimitiveInt, CLIPLoader, StringConcatenate, ModelAttentionBackend, TextEncodeQwenImage21, Label (rgthree), SaveImage, RegexReplace, TextGenerate, ModelAttentionBackend, MarkdownNote, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, BatchImagesNode, SeedVR2LoadVAEModel, SetNode, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, GetNode, SaveImage, VAEDecode, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Image Comparer (rgthree), VAEDecode, INTConstant, SaveImage, Label (rgthree), Label (rgthree), PrimitiveStringMultiline, QwenImage21Cache, SaveImage, GetNode, Fast Groups Bypasser (rgthree), ResolutionSelector, Fast Groups Bypasser (rgthree), TextGenerate, UNETLoader, CLIPLoader, easy showAnything, EmptyLatentImage, INTConstant, Image Comparer (rgthree), Image Comparer (rgthree), PrimitiveStringMultiline, VOSR2ModelLoader, LoadImage, INTConstant, LoadImage, VOSR2Upscale, SaveImage, CLIPLoader, CLIPLoader, StringConcatenate, RegexReplace, Label (rgthree), TextEncodeQwenImage21, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VAELoader, QwenImage21Cache, KSampler, UNETLoader, MarkdownNote, PrimitiveInt, CLIPLoader, ModelAttentionBackend, TextEncodeQwenImage21, Label (rgthree), SaveImage, RegexReplace, VAEDecode, ResolutionSelector, EmptyLatentImage, Label (rgthree), Label (rgthree), ResolutionSelector, PrimitiveInt, GetImageSize, EmptyLatentImage, VAELoader, KSampler, GetNode, PreviewImage, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, PreviewImage, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, LoadImage, LoadImage, LoadImage, PreviewImage, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, GetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, LoadImage, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, ModelAttentionBackend, MarkdownNote, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, VAEDecode, QwenImage21Cache, GetNode, Fast Groups Bypasser (rgthree), UNETLoader, CLIPLoader, LoadImage, Label (rgthree), TextEncodeQwenImage21, PrimitiveStringMultiline, PrimitiveStringMultiline, Label (rgthree), Label (rgthree), SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 513817922471387, "steps": 40, "width": 1024}
---

# 图片生成/文生图/【SevnFading】Qwen-Image-2.1 多合一工作流 （进阶版）_2101856561537830914.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【SevnFading】Qwen-Image-2.1 多合一工作流 （进阶版）_2101856561537830914.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（267 个）：
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `ResolutionSelector`
- `PrimitiveInt`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `KSampler` ★核心
- `GetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `LoadImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MarkdownNote`
- `PrimitiveInt`
- `CLIPLoader`
- `StringConcatenate`
- `ModelAttentionBackend`
- `TextEncodeQwenImage21`
- `Label (rgthree)`
- `SaveImage`
- `RegexReplace`
- `TextGenerate`
- `ModelAttentionBackend`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BatchImagesNode`
- `SeedVR2LoadVAEModel`
- `SetNode`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `GetNode`
- `SaveImage`
- `VAEDecode` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `INTConstant`
- `SaveImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `PrimitiveStringMultiline`
- `QwenImage21Cache`
- `SaveImage`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `Fast Groups Bypasser (rgthree)`
- `TextGenerate`
- `UNETLoader` ★核心
- `CLIPLoader`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `INTConstant`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `PrimitiveStringMultiline`
- `VOSR2ModelLoader`
- `LoadImage`
- `INTConstant`
- `LoadImage`
- `VOSR2Upscale`
- `SaveImage`
- `CLIPLoader`
- `CLIPLoader`
- `StringConcatenate`
- `RegexReplace`
- `Label (rgthree)`
- `TextEncodeQwenImage21`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `PrimitiveInt`
- `CLIPLoader`
- `ModelAttentionBackend`
- `TextEncodeQwenImage21`
- `Label (rgthree)`
- `SaveImage`
- `RegexReplace`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `Label (rgthree)`
- `Label (rgthree)`
- `ResolutionSelector`
- `PrimitiveInt`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `KSampler` ★核心
- `GetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `LoadImage`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `LoadImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ModelAttentionBackend`
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `Label (rgthree)`
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Label (rgthree)`
- `Label (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `513817922471387`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **54%**（145/267）

**有卡**：`VAELoader`、`QwenImage21Cache`、`KSampler`、`ResolutionSelector`、`GetImageSize`、`EmptyLatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`StringConcatenate`、`ModelAttentionBackend`、`TextEncodeQwenImage21`、`Label (rgthree)`、`SaveImage`、`RegexReplace`、`TextGenerate`、`BatchImagesNode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`VAEDecode`、`INTConstant`、`VOSR2ModelLoader`、`VOSR2Upscale`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
