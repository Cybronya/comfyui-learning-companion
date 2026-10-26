---
key: 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113529216594698242.json
name: 三视图+多表情+多视角  Qwen Image 2.1_2113529216594698242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113529216594698242.json
hash: 572939b801ba505a
coverage: 0.730769
learned_at: 2026-10-26 22:04:40
nodes: [UNETLoader, CLIPLoader, JjkText, VAELoader, TextEncodeQwenImage21, TextEncodeQwenImage21, JjkText, PrimitiveFloat, LoadImage, ResolutionSelector, QwenImage21Cache, EmptyLatentImage, JjkText, ComfySwitchNode, TextEncodeQwenImage21, ComfySwitchNode, KSampler, ComfySwitchNode, KSampler, KSampler, VAEDecode, VAEDecode, VAEDecode, ImageStitch, ImageStitch, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 1109489996050760, "steps": 25, "width": 1024}
---

# 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113529216594698242.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113529216594698242.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `JjkText`
- `VAELoader`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `JjkText`
- `PrimitiveFloat`
- `LoadImage`
- `ResolutionSelector`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `JjkText`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `KSampler` ★核心
- `ComfySwitchNode`
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageStitch`
- `ImageStitch`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1109489996050760`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`、`ResolutionSelector`、`QwenImage21Cache`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`ImageStitch`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
