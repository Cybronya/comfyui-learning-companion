---
key: 图片生成/图生图/Qwen Image 2.1 PE 图像编辑_2102228368161853441.json
name: Qwen Image 2.1 PE 图像编辑_2102228368161853441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE 图像编辑_2102228368161853441.json
hash: aa948498befb77b4
coverage: 0.846154
learned_at: 2026-10-15 22:25:11
nodes: [Note, UNETLoader, CLIPLoader, VAELoader, VAEDecode, QwenImage21Cache, Note, SaveImage, easy cleanGpuUsed, KSampler, LoadImage, easy showAnything, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, QwenPERewriteT8, CR Prompt Text, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 PE 图像编辑_2102228368161853441.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE 图像编辑_2102228368161853441.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `Note`
- `SaveImage`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `LoadImage`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `QwenPERewriteT8`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`SaveImage`、`easy cleanGpuUsed`、`KSampler`、`LoadImage`、`EmptyLatentImage`、`ResolutionSelector`、`QwenPERewriteT8`、`CR Prompt Text`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
