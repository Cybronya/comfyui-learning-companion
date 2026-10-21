---
key: 图片生成/文生图/Qwen image 2.1 文生图（提示词增强）_2101808005967867905.json
name: Qwen image 2.1 文生图（提示词增强）_2101808005967867905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图（提示词增强）_2101808005967867905.json
hash: 9f943cca5461d312
coverage: 0.916667
learned_at: 2026-10-20 01:51:11
nodes: [UNETLoader, CLIPLoader, VAELoader, CLIPLoader, TextEncodeQwenImage21, EmptyLatentImage, KSampler, VAEDecode, SaveImage, easy showAnything, TextGenerateLTX2Prompt, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图（提示词增强）_2101808005967867905.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图（提示词增强）_2101808005967867905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `easy showAnything`
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

覆盖率 **92%**（11/12）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`TextGenerateLTX2Prompt`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
