---
key: 图片生成/文生图/Qwen image 2.1 文生图_2104471028356435969.json
name: Qwen image 2.1 文生图_2104471028356435969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2104471028356435969.json
hash: c5d9b09dec068c99
coverage: 0.923077
learned_at: 2026-10-07 02:16:05
nodes: [ResolutionSelector, TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, KSampler, UNETLoader, CLIPLoader, VAELoader, easy showAnything, CLIPLoader, SaveImage, SaveImageAdvanced, TextGenerateLTX2Prompt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图_2104471028356435969.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2104471028356435969.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `CLIPLoader`
- `SaveImage`
- `SaveImageAdvanced`
- `TextGenerateLTX2Prompt`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `666`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`ResolutionSelector`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`SaveImageAdvanced`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
