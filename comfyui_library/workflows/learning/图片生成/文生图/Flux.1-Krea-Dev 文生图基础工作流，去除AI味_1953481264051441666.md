---
key: 图片生成/文生图/Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666.json
name: Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666.json
hash: a8b3d237a3f61558
coverage: 0.8
learned_at: 2026-10-15 22:26:25
nodes: [MarkdownNote, MarkdownNote, EmptyLatentImage, VAELoader, DualCLIPLoader, UNETLoader, ConditioningZeroOut, easy showAnything, CLIPTextEncode, RH_Translator, KSampler, LoraLoaderModelOnly, VAEDecode, SaveImage, Text Multiline]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 1047313144882271, "steps": 30, "width": 1024}
---

# 图片生成/文生图/Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-Dev 文生图基础工作流，去除AI味_1953481264051441666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `MarkdownNote`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Text Multiline`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `1047313144882271`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`EmptyLatentImage`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`ConditioningZeroOut`、`CLIPTextEncode`、`RH_Translator`、`KSampler`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、UNETLoader
