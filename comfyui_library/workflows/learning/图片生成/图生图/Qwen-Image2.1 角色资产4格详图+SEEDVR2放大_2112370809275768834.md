---
key: 图片生成/图生图/Qwen-Image2.1 角色资产4格详图+SEEDVR2放大_2112370809275768834.json
name: Qwen-Image2.1 角色资产4格详图+SEEDVR2放大_2112370809275768834
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image2.1 角色资产4格详图+SEEDVR2放大_2112370809275768834.json
hash: e12455fb17429eef
coverage: 0.666667
learned_at: 2026-10-23 11:17:20
nodes: [SeedVR2LoadVAEModel, ImageScaleToTotalPixels, PrimitiveBoolean, ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, PrimitiveStringMultiline, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, QwenImage21Cache, KSampler, VAEDecode, Image Comparer (rgthree), PreviewImage, SeedVR2LoadDiTModel, SaveImage, LoadImage, Image Comparer (rgthree), SeedVR2VideoUpscaler, Fast Groups Bypasser (rgthree), MarkdownNote, 孤海注释]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 122571831596613, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen-Image2.1 角色资产4格详图+SEEDVR2放大_2112370809275768834.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image2.1 角色资产4格详图+SEEDVR2放大_2112370809275768834.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `PrimitiveBoolean`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `孤海注释`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `122571831596613`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（16/24）

**有卡**：`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`PrimitiveBoolean`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SaveImage`、`LoadImage`、`SeedVR2VideoUpscaler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
