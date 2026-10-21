---
key: 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2102180872337321986.json
name: 开源最强图片模型 Qwen-image2.1  文生图带优化_2102180872337321986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2102180872337321986.json
hash: 9f81ab31d2dd22c5
coverage: 0.809524
learned_at: 2026-10-20 01:52:28
nodes: [UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, easy showAnything, CR Prompt List, String Literal, Seed (rgthree), MarkdownNote, Note Plus (mtb), 孤海注释, ImpactInt, ImpactInt, TextGenerateLTX2Prompt, CLIPLoader, SaveImage, CR Text, easy showAnything]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 496085427137285, "steps": 50, "width": 1024}
---

# 图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2102180872337321986.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/开源最强图片模型 Qwen-image2.1  文生图带优化_2102180872337321986.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `easy showAnything`
- `CR Prompt List`
- `String Literal`
- `Seed (rgthree)`
- `MarkdownNote`
- `Note Plus (mtb)`
- `孤海注释`
- `ImpactInt`
- `ImpactInt`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `SaveImage`
- `CR Text`
- `easy showAnything`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `496085427137285`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`CR Prompt List`、`String Literal`、`Seed (rgthree)`、`Note Plus (mtb)`、`ImpactInt`、`TextGenerateLTX2Prompt`、`SaveImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、UNETLoader、Seed (rgthree)
