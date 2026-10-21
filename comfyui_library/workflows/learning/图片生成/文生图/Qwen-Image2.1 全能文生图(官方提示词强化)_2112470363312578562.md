---
key: 图片生成/文生图/Qwen-Image2.1 全能文生图(官方提示词强化)_2112470363312578562.json
name: Qwen-Image2.1 全能文生图(官方提示词强化)_2112470363312578562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image2.1 全能文生图(官方提示词强化)_2112470363312578562.json
hash: a6b684492fb6b656
coverage: 0.689655
learned_at: 2026-10-21 02:54:35
nodes: [PrimitiveStringMultiline, ResolutionSelector, KSampler, VAEDecode, Fast Groups Bypasser (rgthree), ImageScaleToTotalPixels, SeedVR2LoadDiTModel, ShowAnything|Mie, SaveImage, VAELoader, CLIPLoader, UNETLoader, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), MarkdownNote, 孤海注释, PrimitiveStringMultiline, CLIPLoader, TextGenerate, PrimitiveStringMultiline, StringFormat, RegexExtract, EmptyLatentImage, Fast Groups Bypasser (rgthree), ComfySwitchNode, TextEncodeQwenImage21, ShowAnything|Mie]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 299053072677727, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen-Image2.1 全能文生图(官方提示词强化)_2112470363312578562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image2.1 全能文生图(官方提示词强化)_2112470363312578562.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadDiTModel`
- `ShowAnything|Mie`
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `MarkdownNote`
- `孤海注释`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `StringFormat`
- `RegexExtract`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ShowAnything|Mie`

## 关键参数

- `seed` = `299053072677727`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（20/29）

**有卡**：`ResolutionSelector`、`KSampler`、`VAEDecode`、`ImageScaleToTotalPixels`、`SeedVR2LoadDiTModel`、`ShowAnything|Mie`、`SaveImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`TextGenerate`、`StringFormat`、`RegexExtract`、`EmptyLatentImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
