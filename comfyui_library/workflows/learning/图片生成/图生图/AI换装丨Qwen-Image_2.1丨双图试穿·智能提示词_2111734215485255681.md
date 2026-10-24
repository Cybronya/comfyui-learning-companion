---
key: 图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2111734215485255681.json
name: AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2111734215485255681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2111734215485255681.json
hash: 754aeaeeca787640
coverage: 0.789474
learned_at: 2026-10-23 10:50:35
nodes: [CLIPLoader, CLIPLoader, BatchImagesNode, VAELoader, EmptyLatentImage, ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextGenerate, TextEncodeQwenImage21, UNETLoader, JjkText, ResolutionSelector, PrimitiveStringMultiline, ComfySwitchNode, LoadImage, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 34296019101237, "steps": 50, "width": 1088}
---

# 图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2111734215485255681.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AI换装丨Qwen-Image_2.1丨双图试穿·智能提示词_2111734215485255681.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `CLIPLoader`
- `BatchImagesNode`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextGenerate`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `JjkText`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `SaveImage`

## 关键参数

- `width` = `1088`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `34296019101237`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（15/19）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextGenerate`、`TextEncodeQwenImage21`、`UNETLoader`、`ResolutionSelector`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
