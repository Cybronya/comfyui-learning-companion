---
key: 图片生成/文生图/【开源】Qwen image 2.1 文生图_2102002816368857089.json
name: 【开源】Qwen image 2.1 文生图_2102002816368857089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【开源】Qwen image 2.1 文生图_2102002816368857089.json
hash: 3f6c6c9c0ab137f5
coverage: 1
learned_at: 2026-10-20 01:52:07
nodes: [KSampler, VAEDecode, VAELoader, CLIPLoader, UNETLoader, TextEncodeQwenImage21, SaveImageAdvanced, EmptyLatentImage, easy promptList, ResolutionSelector, Text, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 295557363567090, "steps": 25, "width": 1024}
---

# 图片生成/文生图/【开源】Qwen image 2.1 文生图_2102002816368857089.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【开源】Qwen image 2.1 文生图_2102002816368857089.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `EmptyLatentImage` ★核心
- `easy promptList`
- `ResolutionSelector`
- `Text`
- `SaveImage`

## 关键参数

- `seed` = `295557363567090`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`KSampler`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`EmptyLatentImage`、`easy promptList`、`ResolutionSelector`、`Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
