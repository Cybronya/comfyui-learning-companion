---
key: 图片生成/文生图/Qwen image 2.1 文生图_2102294732612395009.json
name: Qwen image 2.1 文生图_2102294732612395009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2102294732612395009.json
hash: bcdb5620115f9b2e
coverage: 0.866667
learned_at: 2026-10-20 01:51:10
nodes: [TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, UNETLoader, CLIPLoader, VAELoader, ResolutionSelector, KSampler, CLIPLoader, TextGenerateLTX2Prompt, SaveImageAdvanced, SaveImage, Text, easy showAnything, ImpactSwitch]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 45, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图_2102294732612395009.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2102294732612395009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `KSampler` ★核心
- `CLIPLoader`
- `TextGenerateLTX2Prompt`
- `SaveImageAdvanced`
- `SaveImage`
- `Text`
- `easy showAnything`
- `ImpactSwitch`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `666`
- `steps` = `45`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（13/15）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`KSampler`、`TextGenerateLTX2Prompt`、`SaveImageAdvanced`、`SaveImage`、`Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
