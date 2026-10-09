---
key: 图片生成/图生图/Qwen+image+2.1图片编辑-mums_2102062409107202049.json
name: Qwen+image+2.1图片编辑-mums_2102062409107202049.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen+image+2.1图片编辑-mums_2102062409107202049.json
hash: ed743611d92fae81
coverage: 0.888889
learned_at: 2026-10-09 22:19:27
nodes: [UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, KSampler, LoadImage, LoadImage, LoadImage, LoadImage, Text, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, PrimitiveBoolean, VAEDecode, SaveImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 64167014340095, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen+image+2.1图片编辑-mums_2102062409107202049.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2102062409107202049.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`

## 关键参数

- `seed` = `64167014340095`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`LoadImage`、`Text`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`PrimitiveBoolean`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
