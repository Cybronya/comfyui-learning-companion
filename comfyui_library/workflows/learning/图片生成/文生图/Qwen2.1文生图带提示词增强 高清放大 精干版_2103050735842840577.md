---
key: 图片生成/文生图/Qwen2.1文生图带提示词增强 高清放大 精干版_2103050735842840577.json
name: Qwen2.1文生图带提示词增强 高清放大 精干版_2103050735842840577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图带提示词增强 高清放大 精干版_2103050735842840577.json
hash: 6b01f80598fffa86
coverage: 0.782609
learned_at: 2026-10-07 02:28:14
nodes: [TextGenerate, CLIPLoader, StringConstantMultiline, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, UNETLoader, ConditioningZeroOut, LoraLoaderModelOnly, CLIPLoader, VAELoader, ResolutionSelector, KSampler, ImageScaleBy, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, easy clearCacheAll, PreviewImage, SaveImage, Fast Groups Bypasser (rgthree), Label (rgthree), Label (rgthree)]
patterns: []
missing: [Label (rgthree), Label (rgthree), easy clearCacheAll]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 325829040963076, "steps": 40, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen2.1文生图带提示词增强 高清放大 精干版_2103050735842840577.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图带提示词增强 高清放大 精干版_2103050735842840577.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `TextGenerate`
- `CLIPLoader`
- `StringConstantMultiline`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `KSampler` ★核心
- `ImageScaleBy`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `easy clearCacheAll`
- `PreviewImage`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`

## 关键参数

- `seed` = `325829040963076`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`TextGenerate`、`CLIPLoader`、`StringConstantMultiline`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`UNETLoader`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`VAELoader`、`ResolutionSelector`、`KSampler`、`ImageScaleBy`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`SaveImage`

**缺卡**（3）：`Label (rgthree)`、`Label (rgthree)`、`easy clearCacheAll`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
