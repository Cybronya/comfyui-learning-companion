---
key: 平台全量/AI短剧漫剧专用 4格角色资产图工作流【Qwen-Image2.1+seedvr2放大】_2117447053709238273.json
name: AI短剧漫剧专用 4格角色资产图工作流【Qwen-Image2.1+seedvr2放大】_2117447053709238273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/AI短剧漫剧专用 4格角色资产图工作流【Qwen-Image2.1+seedvr2放大】_2117447053709238273.json
hash: 063b20e8f1d604d3
coverage: 0.708333
learned_at: 2026-11-14 00:16:52
nodes: [VAELoader, EmptyLatentImage, QwenImage21Cache, UNETLoader, CLIPLoader, KSampler, Image Comparer (rgthree), SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, ImageScaleToTotalPixels, TextEncodeQwenImage21, PrimitiveBoolean, ComfySwitchNode, ResolutionSelector, VAEDecode, PreviewImage, PrimitiveStringMultiline, Image Comparer (rgthree), SaveImage, LoadImage, 孤海注释, 孤海注释, 忽略多组孤海]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 222122961982142, "steps": 40, "width": 1024}
---

# 平台全量/AI短剧漫剧专用 4格角色资产图工作流【Qwen-Image2.1+seedvr2放大】_2117447053709238273.json

> 来源文件 `comfyui_library/workflows/平台全量/AI短剧漫剧专用 4格角色资产图工作流【Qwen-Image2.1+seedvr2放大】_2117447053709238273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
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
- `孤海注释`
- `孤海注释`
- `忽略多组孤海`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `222122961982142`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（17/24）

**有卡**：`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`UNETLoader`、`CLIPLoader`、`KSampler`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`ImageScaleToTotalPixels`、`TextEncodeQwenImage21`、`PrimitiveBoolean`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`LoadImage`、`忽略多组孤海`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
