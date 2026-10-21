---
key: 图片生成/图生图/Qwen Image 2.1 PE 多图像编辑 最多9图_2102740160445247490.json
name: Qwen Image 2.1 PE 多图像编辑 最多9图_2102740160445247490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE 多图像编辑 最多9图_2102740160445247490.json
hash: 5cf60391950a8525
coverage: 0.846154
learned_at: 2026-10-21 00:42:06
nodes: [Note, UNETLoader, CLIPLoader, VAELoader, VAEDecode, QwenImage21Cache, Note, SaveImage, easy cleanGpuUsed, KSampler, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, QwenPERewriteT8, easy showAnything, TextEncodeQwenImage21, EmptyLatentImage, ResolutionSelector, ComfySwitchNode, LoadImage, LoadImage, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 PE 多图像编辑 最多9图_2102740160445247490.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 PE 多图像编辑 最多9图_2102740160445247490.json`

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
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenPERewriteT8`
- `easy showAnything`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`

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

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`SaveImage`、`easy cleanGpuUsed`、`KSampler`、`LoadImage`、`QwenPERewriteT8`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ResolutionSelector`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
