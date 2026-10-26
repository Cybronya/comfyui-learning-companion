---
key: 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113899265037787137.json
name: 三视图+多表情+多视角  Qwen Image 2.1_2113899265037787137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113899265037787137.json
hash: 949b54c67028b366
coverage: 0.730769
learned_at: 2026-10-26 22:04:43
nodes: [VAEDecode, VAEDecode, UNETLoader, CLIPLoader, VAELoader, ImageStitch, KSampler, KSampler, SaveImage, LoadImage, ResolutionSelector, EmptyLatentImage, PrimitiveFloat, QwenImage21Cache, JjkText, JjkText, JjkText, TextEncodeQwenImage21, TextEncodeQwenImage21, TextEncodeQwenImage21, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, KSampler, VAEDecode, ImageStitch]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 147801817033447, "steps": 25, "width": 1024}
---

# 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113899265037787137.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113899265037787137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageStitch`
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `PrimitiveFloat`
- `QwenImage21Cache`
- `JjkText`
- `JjkText`
- `JjkText`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageStitch`

## 关键参数

- `seed` = `147801817033447`
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

**有卡**：`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageStitch`、`KSampler`、`SaveImage`、`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
