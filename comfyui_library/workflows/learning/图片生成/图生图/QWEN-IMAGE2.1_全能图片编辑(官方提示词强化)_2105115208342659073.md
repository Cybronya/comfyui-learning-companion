---
key: 图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105115208342659073.json
name: QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105115208342659073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105115208342659073.json
hash: 9225b1288cb247c5
coverage: 0.74359
learned_at: 2026-10-21 00:41:55
nodes: [VAELoader, EmptyLatentImage, QwenImage21Cache, UNETLoader, CLIPLoader, KSampler, Image Comparer (rgthree), SeedVR2LoadDiTModel, SaveImage, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, ImageScaleToTotalPixels, PrimitiveStringMultiline, PrimitiveStringMultiline, StringFormat, TextEncodeQwenImage21, SaveImage, CLIPLoader, PrimitiveStringMultiline, BatchImagesNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Image Comparer (rgthree), TextGenerate, Fast Groups Bypasser (rgthree), ShowAnything|Mie, ResolutionSelector, PrimitiveBoolean, ShowAnything|Mie, LoadImage, ComfySwitchNode, RegexExtract, PrimitiveStringMultiline, ComfySwitchNode, VAEDecode, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 308913588198609, "steps": 40, "width": 1024}
---

# 图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105115208342659073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QWEN-IMAGE2.1_全能图片编辑(官方提示词强化)_2105115208342659073.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `VAELoader`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `StringFormat`
- `TextEncodeQwenImage21`
- `SaveImage`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `BatchImagesNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `TextGenerate`
- `Fast Groups Bypasser (rgthree)`
- `ShowAnything|Mie`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `ShowAnything|Mie`
- `LoadImage`
- `ComfySwitchNode`
- `RegexExtract`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `308913588198609`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（29/39）

**有卡**：`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`KSampler`、`SeedVR2LoadDiTModel`、`SaveImage`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`StringFormat`、`TextEncodeQwenImage21`、`BatchImagesNode`、`LoadImage`、`TextGenerate`、`ShowAnything|Mie`、`ResolutionSelector`、`PrimitiveBoolean`、`RegexExtract`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
