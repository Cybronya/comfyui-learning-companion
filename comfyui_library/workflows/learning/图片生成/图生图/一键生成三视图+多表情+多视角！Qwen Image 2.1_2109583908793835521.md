---
key: 图片生成/图生图/一键生成三视图+多表情+多视角！Qwen Image 2.1_2109583908793835521.json
name: 一键生成三视图+多表情+多视角！Qwen Image 2.1_2109583908793835521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键生成三视图+多表情+多视角！Qwen Image 2.1_2109583908793835521.json
hash: 4d5b2d36148d30bd
coverage: 0.730769
learned_at: 2026-10-23 11:57:38
nodes: [UNETLoader, CLIPLoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, VAEDecode, KSampler, ComfySwitchNode, TextEncodeQwenImage21, TextEncodeQwenImage21, KSampler, ComfySwitchNode, VAEDecode, ImageStitch, PrimitiveFloat, ImageStitch, ResolutionSelector, VAELoader, JjkText, JjkText, JjkText, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 822480229295600, "steps": 25, "width": 1024}
---

# 图片生成/图生图/一键生成三视图+多表情+多视角！Qwen Image 2.1_2109583908793835521.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键生成三视图+多表情+多视角！Qwen Image 2.1_2109583908793835521.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `ImageStitch`
- `PrimitiveFloat`
- `ImageStitch`
- `ResolutionSelector`
- `VAELoader`
- `JjkText`
- `JjkText`
- `JjkText`
- `SaveImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `822480229295600`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ImageStitch`、`ResolutionSelector`、`VAELoader`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
