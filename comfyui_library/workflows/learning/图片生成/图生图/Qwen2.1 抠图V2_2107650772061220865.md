---
key: 图片生成/图生图/Qwen2.1 抠图V2_2107650772061220865.json
name: Qwen2.1 抠图V2_2107650772061220865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1 抠图V2_2107650772061220865.json
hash: 7aec384e5f940623
coverage: 0.8
learned_at: 2026-10-21 00:43:36
nodes: [CLIPLoader, VAELoader, MarkdownNote, Note, QwenImage21Cache, EmptyLatentImage, VAEDecode, ComfySwitchNode, ResolutionSelector, UNETLoader, SaveImage, TextEncodeQwenImage21, KSampler, LoadImage, Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 493702176519858, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwen2.1 抠图V2_2107650772061220865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1 抠图V2_2107650772061220865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `Note`
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `LoadImage`
- `Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `493702176519858`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`EmptyLatentImage`、`VAEDecode`、`ResolutionSelector`、`UNETLoader`、`SaveImage`、`TextEncodeQwenImage21`、`KSampler`、`LoadImage`、`Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
