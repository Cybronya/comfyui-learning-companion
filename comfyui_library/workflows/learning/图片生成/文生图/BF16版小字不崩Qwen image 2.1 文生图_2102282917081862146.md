---
key: 图片生成/文生图/BF16版小字不崩Qwen image 2.1 文生图_2102282917081862146.json
name: BF16版小字不崩Qwen image 2.1 文生图_2102282917081862146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/BF16版小字不崩Qwen image 2.1 文生图_2102282917081862146.json
hash: e72bed834fef02c5
coverage: 1
learned_at: 2026-10-20 01:50:23
nodes: [VAEDecode, EmptyLatentImage, KSampler, TextEncodeQwenImage21, VAELoader, ResolutionSelector, CR Prompt Text, SaveImage, SaveImageAdvanced, CLIPLoader, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 448707222953503, "steps": 50, "width": 1024}
---

# 图片生成/文生图/BF16版小字不崩Qwen image 2.1 文生图_2102282917081862146.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/BF16版小字不崩Qwen image 2.1 文生图_2102282917081862146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `VAELoader`
- `ResolutionSelector`
- `CR Prompt Text`
- `SaveImage`
- `SaveImageAdvanced`
- `CLIPLoader`
- `UNETLoader` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `448707222953503`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAEDecode`、`EmptyLatentImage`、`KSampler`、`TextEncodeQwenImage21`、`VAELoader`、`ResolutionSelector`、`CR Prompt Text`、`SaveImage`、`SaveImageAdvanced`、`CLIPLoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
