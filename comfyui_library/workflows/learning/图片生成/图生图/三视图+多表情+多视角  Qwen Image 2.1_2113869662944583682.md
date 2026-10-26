---
key: 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113869662944583682.json
name: 三视图+多表情+多视角  Qwen Image 2.1_2113869662944583682
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113869662944583682.json
hash: 16f084d93141a998
coverage: 0.730769
learned_at: 2026-10-26 22:04:42
nodes: [VAEDecode, VAEDecode, UNETLoader, JjkText, ImageStitch, ImageStitch, KSampler, VAEDecode, KSampler, KSampler, ComfySwitchNode, ComfySwitchNode, TextEncodeQwenImage21, SaveImage, JjkText, JjkText, QwenImage21Cache, ComfySwitchNode, TextEncodeQwenImage21, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, LoadImage, CLIPLoader, VAELoader, PrimitiveFloat]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 425663773366393, "steps": 25, "width": 1024}
---

# 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113869662944583682.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2113869662944583682.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `JjkText`
- `ImageStitch`
- `ImageStitch`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `SaveImage`
- `JjkText`
- `JjkText`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveFloat`

## 关键参数

- `seed` = `425663773366393`
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

**有卡**：`VAEDecode`、`UNETLoader`、`ImageStitch`、`KSampler`、`TextEncodeQwenImage21`、`SaveImage`、`QwenImage21Cache`、`EmptyLatentImage`、`ResolutionSelector`、`LoadImage`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
