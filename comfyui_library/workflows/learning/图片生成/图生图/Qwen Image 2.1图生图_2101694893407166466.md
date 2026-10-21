---
key: 图片生成/图生图/Qwen Image 2.1图生图_2101694893407166466.json
name: Qwen Image 2.1图生图_2101694893407166466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图生图_2101694893407166466.json
hash: 11678b8c2365730f
coverage: 0.666667
learned_at: 2026-10-21 00:42:32
nodes: [UNETLoader, VAELoader, EmptyLatentImage, KSampler, VAEDecode, SaveImage, ImageScaleBy, VAEEncodeTiled, KSampler, VAEDecodeTiled, SaveImage, Note, Note, Note, Note, Note, Note, Note, CLIPLoader, TextEncodeQwenImage21, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.18, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 20260921, "steps": 14, "width": 2048}
---

# 图片生成/图生图/Qwen Image 2.1图生图_2101694893407166466.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图生图_2101694893407166466.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageScaleBy`
- `VAEEncodeTiled` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `LoadImage`

## 关键参数

- `width` = `2048`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `20260921`
- `steps` = `14`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.18`

## 知识

覆盖率 **67%**（14/21）

**有卡**：`UNETLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`ImageScaleBy`、`VAEEncodeTiled`、`VAEDecodeTiled`、`CLIPLoader`、`TextEncodeQwenImage21`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
