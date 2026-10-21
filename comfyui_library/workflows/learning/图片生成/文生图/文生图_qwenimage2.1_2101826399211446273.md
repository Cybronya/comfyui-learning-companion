---
key: 图片生成/文生图/文生图_qwenimage2.1_2101826399211446273.json
name: 文生图_qwenimage2.1_2101826399211446273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图_qwenimage2.1_2101826399211446273.json
hash: a3b95e6aa6e9a4f3
coverage: 0.923077
learned_at: 2026-10-20 01:52:49
nodes: [CLIPLoader, VAELoader, UNETLoader, easy showAnything, TextEncodeQwenImage21, EmptyLatentImage, KSampler, VAEDecode, SaveImageAdvanced, SaveImage, ResolutionSelector, TextGenerateLTX2Prompt, CLIPLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 888, "steps": 50, "width": 1024}
---

# 图片生成/文生图/文生图_qwenimage2.1_2101826399211446273.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图_qwenimage2.1_2101826399211446273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `easy showAnything`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `888`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`SaveImage`、`ResolutionSelector`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
