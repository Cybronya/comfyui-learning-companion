---
key: 图片生成/文生图/QWEN-IMAGE2.1 全能文生图(官方提示词强化)_2101915002625150978.json
name: QWEN-IMAGE2.1 全能文生图(官方提示词强化)_2101915002625150978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QWEN-IMAGE2.1 全能文生图(官方提示词强化)_2101915002625150978.json
hash: 2bfcb647dc784695
coverage: 0.740741
learned_at: 2026-10-20 01:50:48
nodes: [VAELoader, UNETLoader, CLIPLoader, CLIPLoader, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, ImageScaleToTotalPixels, KSampler, SaveImage, PrimitiveStringMultiline, PrimitiveStringMultiline, EmptyLatentImage, ResolutionSelector, StringFormat, Image Comparer (rgthree), SaveImage, ShowAnything|Mie, VAEDecode, ShowAnything|Mie, TextGenerate, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), RegexExtract, PrimitiveStringMultiline, TextEncodeQwenImage21, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 268442069734997, "steps": 40, "width": 1024}
---

# 图片生成/文生图/QWEN-IMAGE2.1 全能文生图(官方提示词强化)_2101915002625150978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QWEN-IMAGE2.1 全能文生图(官方提示词强化)_2101915002625150978.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `StringFormat`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ShowAnything|Mie`
- `VAEDecode` ★核心
- `ShowAnything|Mie`
- `TextGenerate`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `RegexExtract`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`

## 关键参数

- `seed` = `268442069734997`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **74%**（20/27）

**有卡**：`VAELoader`、`UNETLoader`、`CLIPLoader`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`ResolutionSelector`、`StringFormat`、`ShowAnything|Mie`、`VAEDecode`、`TextGenerate`、`RegexExtract`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
