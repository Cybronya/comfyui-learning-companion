---
key: 图片生成/图生图/Qwen image 2.1-图生图-角色四视图-V1_2101831881938522113.json
name: Qwen image 2.1-图生图-角色四视图-V1_2101831881938522113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1-图生图-角色四视图-V1_2101831881938522113.json
hash: de706d839da3dff1
coverage: 0.78125
learned_at: 2026-10-21 00:42:56
nodes: [CLIPLoader, TextGenerateLTX2Prompt, QwenImage21Cache, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, ResolutionSelector, ComfySwitchNode, KSampler, EmptyLatentImage, UNETLoader, CLIPLoader, VAELoader, easy showAnything, BatchImagesNode, LoadImage, PrimitiveStringMultiline, MarkdownNote, VAEDecode, SaveImage, StringConcatenate, PrimitiveStringMultiline, ComfySwitchNode, PrimitiveStringMultiline, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 433423567691388, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1-图生图-角色四视图-V1_2101831881938522113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1-图生图-角色四视图-V1_2101831881938522113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `ComfySwitchNode`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `BatchImagesNode`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `VAEDecode` ★核心
- `SaveImage`
- `StringConcatenate`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`

## 关键参数

- `seed` = `433423567691388`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（25/32）

**有卡**：`CLIPLoader`、`TextGenerateLTX2Prompt`、`QwenImage21Cache`、`LoadImage`、`TextEncodeQwenImage21`、`ResolutionSelector`、`KSampler`、`EmptyLatentImage`、`UNETLoader`、`VAELoader`、`BatchImagesNode`、`VAEDecode`、`SaveImage`、`StringConcatenate`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
