---
key: 图片生成/图生图/【AI军火商】全网最强角色资产4格详图制作【Qwen-Image2.1】_2108004428056973313.json
name: 【AI军火商】全网最强角色资产4格详图制作【Qwen-Image2.1】_2108004428056973313
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【AI军火商】全网最强角色资产4格详图制作【Qwen-Image2.1】_2108004428056973313.json
hash: 115ed7c6626531b5
coverage: 0.727273
learned_at: 2026-10-21 00:46:36
nodes: [VAELoader, EmptyLatentImage, QwenImage21Cache, UNETLoader, CLIPLoader, KSampler, Image Comparer (rgthree), SeedVR2LoadDiTModel, SaveImage, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, ImageScaleToTotalPixels, TextEncodeQwenImage21, Image Comparer (rgthree), PrimitiveBoolean, ComfySwitchNode, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, ResolutionSelector, VAEDecode, PreviewImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 734399256477075, "steps": 40, "width": 1024}
---

# 图片生成/图生图/【AI军火商】全网最强角色资产4格详图制作【Qwen-Image2.1】_2108004428056973313.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【AI军火商】全网最强角色资产4格详图制作【Qwen-Image2.1】_2108004428056973313.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
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
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `734399256477075`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（16/22）

**有卡**：`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`KSampler`、`SeedVR2LoadDiTModel`、`SaveImage`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`TextEncodeQwenImage21`、`PrimitiveBoolean`、`ResolutionSelector`、`VAEDecode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
