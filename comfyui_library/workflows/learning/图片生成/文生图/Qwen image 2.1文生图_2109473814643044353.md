---
key: 图片生成/文生图/Qwen image 2.1文生图_2109473814643044353.json
name: Qwen image 2.1文生图_2109473814643044353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图_2109473814643044353.json
hash: 44c2b9e21fbc91c3
coverage: 0.909091
learned_at: 2026-10-21 02:54:20
nodes: [UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, Seed (rgthree), EmptyLatentImage, KSampler, SaveImage, PrimitiveStringMultiline, ResolutionSelector, VAEDecode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1052698597089605, "steps": 30, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1文生图_2109473814643044353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1文生图_2109473814643044353.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `Seed (rgthree)`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `VAEDecode` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1052698597089605`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`ResolutionSelector`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
