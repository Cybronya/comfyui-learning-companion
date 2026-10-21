---
key: 图片生成/文生图/qwen image 2.1 文_图省图_2108227375078141954.json
name: qwen image 2.1 文_图省图_2108227375078141954
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image 2.1 文_图省图_2108227375078141954.json
hash: 435038bea4f0d407
coverage: 1
learned_at: 2026-10-21 02:57:29
nodes: [JjkShowText, CLIPLoader, VAELoader, QwenImage21Cache, QwenImagePromptOptimizer, TextEncodeQwenImage21GH, VAEDecode, UNETLoader, LoadImage, SaveImage, EmptyLatentImage, KSampler, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 133908397344935, "steps": 50, "width": 1024}
---

# 图片生成/文生图/qwen image 2.1 文_图省图_2108227375078141954.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image 2.1 文_图省图_2108227375078141954.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `JjkShowText`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `QwenImagePromptOptimizer`
- `TextEncodeQwenImage21GH`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `133908397344935`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`JjkShowText`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`QwenImagePromptOptimizer`、`TextEncodeQwenImage21GH`、`VAEDecode`、`UNETLoader`、`LoadImage`、`SaveImage`、`EmptyLatentImage`、`KSampler`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、QwenImage21Cache
