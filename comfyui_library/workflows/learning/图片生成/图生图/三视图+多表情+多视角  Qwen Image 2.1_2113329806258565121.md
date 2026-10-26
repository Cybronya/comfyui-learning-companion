---
key: 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113329806258565121.json
name: 三视图+多表情+多视角  Qwen Image 2.1_2113329806258565121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113329806258565121.json
hash: 20e5e1f66aee3eec
coverage: 0.730769
learned_at: 2026-10-26 22:04:38
nodes: [VAEDecode, VAEDecode, UNETLoader, CLIPLoader, JjkText, ResolutionSelector, PrimitiveFloat, EmptyLatentImage, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, ImageStitch, ImageStitch, KSampler, VAEDecode, KSampler, KSampler, ComfySwitchNode, TextEncodeQwenImage21, ComfySwitchNode, ComfySwitchNode, TextEncodeQwenImage21, JjkText, JjkText, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 171885814020674, "steps": 25, "width": 1024}
---

# 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113329806258565121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113329806258565121.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `JjkText`
- `ResolutionSelector`
- `PrimitiveFloat`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `ImageStitch`
- `ImageStitch`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `JjkText`
- `JjkText`
- `LoadImage`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `171885814020674`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`VAEDecode`、`UNETLoader`、`CLIPLoader`、`ResolutionSelector`、`EmptyLatentImage`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ImageStitch`、`KSampler`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
