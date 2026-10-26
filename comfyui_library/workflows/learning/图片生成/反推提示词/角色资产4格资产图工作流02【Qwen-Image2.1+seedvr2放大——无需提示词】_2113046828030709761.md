---
key: 图片生成/反推提示词/角色资产4格资产图工作流02【Qwen-Image2.1+seedvr2放大——无需提示词】_2113046828030709761.json
name: 角色资产4格资产图工作流02【Qwen-Image2.1+seedvr2放大——无需提示词】_2113046828030709761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/角色资产4格资产图工作流02【Qwen-Image2.1+seedvr2放大——无需提示词】_2113046828030709761.json
hash: 09d39a9fbf6deeea
coverage: 0.761905
learned_at: 2026-10-26 22:01:13
nodes: [VAELoader, EmptyLatentImage, QwenImage21Cache, UNETLoader, CLIPLoader, KSampler, Image Comparer (rgthree), SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, ImageScaleToTotalPixels, TextEncodeQwenImage21, PrimitiveBoolean, ComfySwitchNode, ResolutionSelector, VAEDecode, PreviewImage, PrimitiveStringMultiline, Image Comparer (rgthree), SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 363165996954163, "steps": 40, "width": 1024}
---

# 图片生成/反推提示词/角色资产4格资产图工作流02【Qwen-Image2.1+seedvr2放大——无需提示词】_2113046828030709761.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/角色资产4格资产图工作流02【Qwen-Image2.1+seedvr2放大——无需提示词】_2113046828030709761.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `VAELoader`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImage21`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `PreviewImage`
- `PrimitiveStringMultiline`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `363165996954163`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`KSampler`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`TextEncodeQwenImage21`、`PrimitiveBoolean`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
