---
key: 图片生成/文生图/Qwen image 2.1 文生图提示词增强_2101911095622594562.json
name: Qwen image 2.1 文生图提示词增强_2101911095622594562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图提示词增强_2101911095622594562.json
hash: 883681d5944cb03f
coverage: 0.857143
learned_at: 2026-10-20 01:51:11
nodes: [TextEncodeQwenImage21, EmptyLatentImage, VAEDecode, UNETLoader, CLIPLoader, VAELoader, easy showAnything, SaveImageAdvanced, KSampler, ResolutionSelector, CLIPLoader, PrimitiveStringMultiline, TextGenerateLTX2Prompt, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 114257646250050, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图提示词增强_2101911095622594562.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图提示词增强_2101911095622594562.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy showAnything`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `ResolutionSelector`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `114257646250050`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`TextEncodeQwenImage21`、`EmptyLatentImage`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImageAdvanced`、`KSampler`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
