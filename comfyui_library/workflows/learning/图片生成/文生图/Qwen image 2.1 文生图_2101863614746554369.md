---
key: 图片生成/文生图/Qwen image 2.1 文生图_2101863614746554369.json
name: Qwen image 2.1 文生图_2101863614746554369
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2101863614746554369.json
hash: 2e407935713950e0
coverage: 0.923077
learned_at: 2026-10-20 01:51:08
nodes: [EmptyLatentImage, CLIPLoader, VAELoader, CLIPLoader, UNETLoader, TextEncodeQwenImage21, SaveImageAdvanced, KSampler, SaveImage, easy showAnything, VAEDecode, TextGenerateLTX2Prompt, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图_2101863614746554369.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2101863614746554369.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `SaveImage`
- `easy showAnything`
- `VAEDecode` ★核心
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`

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

**有卡**：`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`TextEncodeQwenImage21`、`SaveImageAdvanced`、`KSampler`、`SaveImage`、`VAEDecode`、`TextGenerateLTX2Prompt`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
