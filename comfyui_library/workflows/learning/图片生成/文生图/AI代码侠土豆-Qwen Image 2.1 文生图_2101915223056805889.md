---
key: 图片生成/文生图/AI代码侠土豆-Qwen Image 2.1 文生图_2101915223056805889.json
name: AI代码侠土豆-Qwen Image 2.1 文生图_2101915223056805889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/AI代码侠土豆-Qwen Image 2.1 文生图_2101915223056805889.json
hash: 4c2ed5302aabceb0
coverage: 0.482759
learned_at: 2026-10-20 01:50:19
nodes: [SetNode, CLIPLoader, SetNode, VAELoader, SetNode, GetNode, GetNode, TextEncodeQwenImage21, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Label (rgthree), Label (rgthree), EmptyLatentImage, SetNode, SetNode, SaveImage, VAEDecode, easy cleanGpuUsed, UNETLoader, Label (rgthree), KSampler, ResolutionSelector, Text Multiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 494473095646804, "steps": 40, "width": 1024}
---

# 图片生成/文生图/AI代码侠土豆-Qwen Image 2.1 文生图_2101915223056805889.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/AI代码侠土豆-Qwen Image 2.1 文生图_2101915223056805889.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（29 个）：
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImage21`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `EmptyLatentImage` ★核心
- `SetNode`
- `SetNode`
- `SaveImage`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `Label (rgthree)`
- `KSampler` ★核心
- `ResolutionSelector`
- `Text Multiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `494473095646804`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **48%**（14/29）

**有卡**：`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`Label (rgthree)`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`KSampler`、`ResolutionSelector`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
