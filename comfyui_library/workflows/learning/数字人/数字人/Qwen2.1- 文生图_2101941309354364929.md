---
key: 数字人/数字人/Qwen2.1- 文生图_2101941309354364929.json
name: Qwen2.1- 文生图_2101941309354364929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Qwen2.1- 文生图_2101941309354364929.json
hash: da8869aeb9351980
coverage: 0.8
learned_at: 2026-10-19 00:19:13
nodes: [UNETLoader, CLIPLoader, VAELoader, easy showAnything, EmptyLatentImage, TextGenerateLTX2Prompt, TextEncodeQwenImage21, CLIPLoader, VAEDecode, PreviewImage, SaveImage, ResolutionSelector, KSampler, JjkText, FastGroupsBypassSwitch]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 50, "width": 1024}
---

# 数字人/数字人/Qwen2.1- 文生图_2101941309354364929.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Qwen2.1- 文生图_2101941309354364929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `ResolutionSelector`
- `KSampler` ★核心
- `JjkText`
- `FastGroupsBypassSwitch`

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

覆盖率 **80%**（12/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImage`、`ResolutionSelector`、`KSampler`、`FastGroupsBypassSwitch`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
