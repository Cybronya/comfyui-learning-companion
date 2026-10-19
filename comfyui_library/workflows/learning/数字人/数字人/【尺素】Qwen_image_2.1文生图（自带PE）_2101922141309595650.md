---
key: 数字人/数字人/【尺素】Qwen_image_2.1文生图（自带PE）_2101922141309595650.json
name: 【尺素】Qwen_image_2.1文生图（自带PE）_2101922141309595650
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/【尺素】Qwen_image_2.1文生图（自带PE）_2101922141309595650.json
hash: 538d63955fe15f56
coverage: 0.4
learned_at: 2026-10-19 00:19:16
nodes: [ResolutionSelector, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, TextGenerateLTX2Prompt, easy showAnything, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CR Text, GetNode, GetNode, SaveImage, CLIPLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 25, "width": 1024}
---

# 数字人/数字人/【尺素】Qwen_image_2.1文生图（自带PE）_2101922141309595650.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/【尺素】Qwen_image_2.1文生图（自带PE）_2101922141309595650.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（30 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Text`
- `GetNode`
- `GetNode`
- `SaveImage`
- `CLIPLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `666`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **40%**（12/30）

**有卡**：`ResolutionSelector`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`TextGenerateLTX2Prompt`、`CR Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
