---
key: 图片生成/文生图/Qwen image 2.1 文生图_2101882676365062146.json
name: Qwen image 2.1 文生图_2101882676365062146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2101882676365062146.json
hash: d6faecd2f1233db5
coverage: 0.923077
learned_at: 2026-10-20 01:51:09
nodes: [TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, KSampler, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, easy showAnything, SaveImageAdvanced, ResolutionSelector, TextGenerateLTX2Prompt, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 666, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图_2101882676365062146.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图_2101882676365062146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `easy showAnything`
- `SaveImageAdvanced`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `SaveImage`

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

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImageAdvanced`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
