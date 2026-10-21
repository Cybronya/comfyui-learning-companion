---
key: 图片生成/文生图/Qwen image 2.1 文生图 影视美学_2101866960572211201.json
name: Qwen image 2.1 文生图 影视美学_2101866960572211201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图 影视美学_2101866960572211201.json
hash: 4a0de8c8b9166a7f
coverage: 0.928571
learned_at: 2026-10-20 01:51:06
nodes: [CLIPLoader, VAELoader, VAEDecode, EmptyLatentImage, TextEncodeQwenImage21, CLIPLoader, UNETLoader, TextGenerateLTX2Prompt, easy showAnything, MuyeTextEditOutput, ResolutionSelector, SaveImage, KSampler, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 803767325158883, "steps": 50, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1 文生图 影视美学_2101866960572211201.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 文生图 影视美学_2101866960572211201.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `MuyeTextEditOutput`
- `ResolutionSelector`
- `SaveImage`
- `KSampler` ★核心
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `803767325158883`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`UNETLoader`、`TextGenerateLTX2Prompt`、`MuyeTextEditOutput`、`ResolutionSelector`、`SaveImage`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、SaveImage
