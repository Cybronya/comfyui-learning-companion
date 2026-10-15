---
key: 图片生成/文生图/Qwen Image 2.1 PE 文生图 多宫格图_2102745138786299906.json
name: Qwen Image 2.1 PE 文生图 多宫格图_2102745138786299906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE 文生图 多宫格图_2102745138786299906.json
hash: 8cece434055eb2d5
coverage: 0.8125
learned_at: 2026-10-15 22:26:56
nodes: [Note, UNETLoader, CLIPLoader, VAELoader, VAEDecode, QwenImage21Cache, KSampler, easy showAnything, TextEncodeQwenImage21, EmptyLatentImage, ComfySwitchNode, QwenPERewriteT8, easy cleanGpuUsed, SaveImage, CR Prompt Text, ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 PE 文生图 多宫格图_2102745138786299906.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 PE 文生图 多宫格图_2102745138786299906.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `Note`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `easy showAnything`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenPERewriteT8`
- `easy cleanGpuUsed`
- `SaveImage`
- `CR Prompt Text`
- `ResolutionSelector`

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

覆盖率 **81%**（13/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`QwenImage21Cache`、`KSampler`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`QwenPERewriteT8`、`easy cleanGpuUsed`、`SaveImage`、`CR Prompt Text`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache
