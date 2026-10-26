---
key: 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2114585973400100865.json
name: 三视图+多表情+多视角  Qwen Image 2.1_2114585973400100865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2114585973400100865.json
hash: a78089441f8f6b9f
coverage: 0.703704
learned_at: 2026-10-26 22:04:44
nodes: [VAEDecode, VAEDecode, UNETLoader, CLIPLoader, JjkText, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, ImageStitch, ImageStitch, KSampler, VAEDecode, KSampler, KSampler, TextEncodeQwenImage21, ComfySwitchNode, TextEncodeQwenImage21, JjkText, JjkText, SaveImage, EmptyLatentImage, ResolutionSelector, PrimitiveFloat, LoadImage, PreviewImage, ComfySwitchNode, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "beta", "seed": 133294341975269, "steps": 25, "width": 1024}
---

# 图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2114585973400100865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/三视图+多表情+多视角  Qwen Image 2.1_2114585973400100865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `JjkText`
- `VAELoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `ImageStitch`
- `ImageStitch`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `JjkText`
- `JjkText`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `PrimitiveFloat`
- `LoadImage`
- `PreviewImage`
- `ComfySwitchNode`
- `ComfySwitchNode`

## 关键参数

- `seed` = `133294341975269`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **70%**（19/27）

**有卡**：`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ImageStitch`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`ResolutionSelector`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
