---
key: 图片生成/图生图/Qwen-Image2.1 全能图片编辑(官方提示词强化)_2112460333402124289.json
name: Qwen-Image2.1 全能图片编辑(官方提示词强化)_2112460333402124289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image2.1 全能图片编辑(官方提示词强化)_2112460333402124289.json
hash: 3333df3d13566de2
coverage: 0.725
learned_at: 2026-10-23 11:17:20
nodes: [PrimitiveStringMultiline, ResolutionSelector, PrimitiveBoolean, PrimitiveStringMultiline, StringFormat, KSampler, VAEDecode, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), ComfySwitchNode, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, TextGenerate, BatchImagesNode, CLIPLoader, PrimitiveStringMultiline, RegexExtract, ShowAnything|Mie, ShowAnything|Mie, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, QwenImage21Cache, SaveImage, Image Comparer (rgthree), SeedVR2VideoUpscaler, SaveImage, Note, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1064020466210292, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen-Image2.1 全能图片编辑(官方提示词强化)_2112460333402124289.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image2.1 全能图片编辑(官方提示词强化)_2112460333402124289.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `StringFormat`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `BatchImagesNode`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `RegexExtract`
- `ShowAnything|Mie`
- `ShowAnything|Mie`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `QwenImage21Cache`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Note`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `1064020466210292`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（29/40）

**有卡**：`ResolutionSelector`、`PrimitiveBoolean`、`StringFormat`、`KSampler`、`VAEDecode`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`LoadImage`、`TextGenerate`、`BatchImagesNode`、`CLIPLoader`、`RegexExtract`、`ShowAnything|Mie`、`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`SaveImage`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
