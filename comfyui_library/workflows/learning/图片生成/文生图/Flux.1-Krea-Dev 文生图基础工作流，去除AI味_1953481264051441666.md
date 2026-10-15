---
key: 图片生成/文生图/Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666.json
name: Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666.json
hash: a8b3d237a3f61558
coverage: 0.733333
learned_at: 2026-10-10 20:58:36
nodes: [MarkdownNote, MarkdownNote, EmptyLatentImage, VAELoader, DualCLIPLoader, UNETLoader, ConditioningZeroOut, easy showAnything, CLIPTextEncode, RH_Translator, KSampler, LoraLoaderModelOnly, VAEDecode, SaveImage, Text Multiline]
patterns: [text_to_image]
missing: [Text Multiline]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 1047313144882271, "steps": 30, "width": 1024}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666.json`

## 结构

**节点**（15 个）：
- `MarkdownNote`
- `MarkdownNote`
- `EmptyLatentImage`
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader`
- `ConditioningZeroOut`
- `easy showAnything`
- `CLIPTextEncode`
- `RH_Translator`
- `KSampler`
- `LoraLoaderModelOnly`
- `VAEDecode`
- `SaveImage`
- `Text Multiline`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1536`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1047313144882271`
- `steps` = `30`
- `width` = `1024`

## 知识

覆盖率 **73%**（11/15）

**有卡**：`MarkdownNote`、`EmptyLatentImage`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`ConditioningZeroOut`、`easy showAnything`、`CLIPTextEncode`、`RH_Translator`、`KSampler`

**缺卡**（1）：`Text Multiline`

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
