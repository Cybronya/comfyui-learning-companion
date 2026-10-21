---
key: 图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步无PE_2102016238707892225.json
name: Qwen Image 2.1 文生图 _ 纯净官流40步无PE_2102016238707892225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步无PE_2102016238707892225.json
hash: e11a09546c381c59
coverage: 0.782609
learned_at: 2026-10-20 01:50:53
nodes: [PixaromaRunTimer, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, EmptyLatentImage, KSampler, PixaromaSeed, LoadImage, LoadImage, Note, LoadImage, LoadImage, Note, LoadImage, LoadImage, LoadImage, Note, Note, PrimitiveStringMultiline, VAEDecode, SaveImage, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 681804419564456, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步无PE_2102016238707892225.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 文生图 _ 纯净官流40步无PE_2102016238707892225.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `PixaromaRunTimer`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `PixaromaSeed`
- `LoadImage`
- `LoadImage`
- `Note`
- `LoadImage`
- `LoadImage`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `Note`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `SaveImage`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `681804419564456`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`PixaromaRunTimer`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`PixaromaSeed`、`LoadImage`、`VAEDecode`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
