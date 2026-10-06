---
key: 图片生成/文生图/qwen image 2.1文生图_2094967170106216450.json
name: qwen image 2.1文生图_2094967170106216450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image 2.1文生图_2094967170106216450.json
hash: 938339cc5b0c7b9a
coverage: 0.785714
learned_at: 2026-10-06 22:57:30
nodes: [VAEDecode, VAELoader, EmptyLatentImage, UNETLoader, ResolutionSelector, CLIPLoader, CLIPLoader, SaveImage, TextEncodeQwenImage21, PrimitiveStringMultiline, PrimitiveStringMultiline, TextGenerateLTX2Prompt, KSampler, easy showAnything]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 7, "steps": 40, "width": 1024}
---

# 图片生成/文生图/qwen image 2.1文生图_2094967170106216450.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image 2.1文生图_2094967170106216450.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `ResolutionSelector`
- `CLIPLoader`
- `CLIPLoader`
- `SaveImage`
- `TextEncodeQwenImage21`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `easy showAnything`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `7`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（11/14）

**有卡**：`VAEDecode`、`VAELoader`、`EmptyLatentImage`、`UNETLoader`、`ResolutionSelector`、`CLIPLoader`、`SaveImage`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
