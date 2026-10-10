---
key: 图片生成/图生图/Qwen-Image 2.1：生图、改图、拼图，一个模型全搞定_2102215048675545090.json
name: Qwen-Image 2.1：生图、改图、拼图，一个模型全搞定_2102215048675545090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1：生图、改图、拼图，一个模型全搞定_2102215048675545090.json
hash: b398936d5c0a4da2
coverage: 0.287671
learned_at: 2026-10-10 20:48:09
nodes: [SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, PrimitiveStringMultiline, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, GetNode, LoadImage, SetNode, SetNode, GetNode, SetNode, GetNode, LoadImage, SetNode, LoadImage, GetNode, LoadImage, SetNode, SetNode, LoadImage, SetNode, LoadImage, GetNode, GetNode, GetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, PrimitiveStringMultiline, ResolutionSelector, EmptyLatentImage, SetNode, UNETLoader, SetNode, QwenImage21Cache, CLIPLoader, TextEncodeQwenImage21, ComfySwitchNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, VAEDecode, KSampler, SetNode, VAELoader, SaveImage, SetNode, GetNode, SaveImageAdvanced, SetNode, LoadImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 167111110634031, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen-Image 2.1：生图、改图、拼图，一个模型全搞定_2102215048675545090.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image 2.1：生图、改图、拼图，一个模型全搞定_2102215048675545090.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（73 个）：
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `GetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SetNode`
- `VAELoader`
- `SaveImage`
- `SetNode`
- `GetNode`
- `SaveImageAdvanced`
- `SetNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `167111110634031`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **29%**（21/73）

**有卡**：`LoadImage`、`ResolutionSelector`、`EmptyLatentImage`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`TextEncodeQwenImage21`、`VAEDecode`、`KSampler`、`VAELoader`、`SaveImage`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
