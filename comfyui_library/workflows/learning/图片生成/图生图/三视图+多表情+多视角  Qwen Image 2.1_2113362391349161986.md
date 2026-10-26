---
key: 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113362391349161986.json
name: 三视图+多表情+多视角  Qwen Image 2.1_2113362391349161986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113362391349161986.json
hash: abc6ad4623a078dd
coverage: 0.730769
learned_at: 2026-10-26 22:04:40
nodes: [VAEDecode, VAEDecode, UNETLoader, CLIPLoader, JjkText, VAELoader, TextEncodeQwenImage21, ImageStitch, ImageStitch, KSampler, VAEDecode, KSampler, KSampler, ComfySwitchNode, TextEncodeQwenImage21, ComfySwitchNode, JjkText, SaveImage, TextEncodeQwenImage21, ComfySwitchNode, JjkText, QwenImage21Cache, PrimitiveFloat, ResolutionSelector, EmptyLatentImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 407052298946369, "steps": 25, "width": 1024}
---

# 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113362391349161986.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113362391349161986.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `JjkText`
- `VAELoader`
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
- `JjkText`
- `SaveImage`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `JjkText`
- `QwenImage21Cache`
- `PrimitiveFloat`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `LoadImage`

## 关键参数

- `seed` = `407052298946369`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`ImageStitch`、`KSampler`、`SaveImage`、`QwenImage21Cache`、`ResolutionSelector`、`EmptyLatentImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
