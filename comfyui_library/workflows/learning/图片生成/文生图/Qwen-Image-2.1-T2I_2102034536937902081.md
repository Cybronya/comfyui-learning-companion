---
key: 图片生成/文生图/Qwen-Image-2.1-T2I_2102034536937902081.json
name: Qwen-Image-2.1-T2I_2102034536937902081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-T2I_2102034536937902081.json
hash: 7330715b63ece39b
coverage: 0.869565
learned_at: 2026-10-20 01:51:16
nodes: [CLIPLoader, TextGenerate, PrimitiveStringMultiline, easy showAnything, EmptyLatentImage, TextEncodeQwenImage21, KSampler, Seed (rgthree), VAEDecode, SaveImage, Fast Groups Bypasser (rgthree), easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, easy promptList, VAELoader, UNETLoader, CLIPLoader, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen-Image-2.1-T2I_2102034536937902081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1-T2I_2102034536937902081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `Seed (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `easy promptList`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `0`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`CLIPLoader`、`TextGenerate`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`KSampler`、`Seed (rgthree)`、`VAEDecode`、`SaveImage`、`easy promptList`、`VAELoader`、`UNETLoader`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
