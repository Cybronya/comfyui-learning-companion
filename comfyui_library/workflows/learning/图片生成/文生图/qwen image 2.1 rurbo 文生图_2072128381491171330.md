---
key: 图片生成/文生图/qwen image 2.1 rurbo 文生图_2072128381491171330.json
name: qwen image 2.1 rurbo 文生图_2072128381491171330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen image 2.1 rurbo 文生图_2072128381491171330.json
hash: 96503b084d4db093
coverage: 0.8125
learned_at: 2026-10-21 02:57:27
nodes: [VAEDecode, VAELoader, CLIPLoader, CLIPLoader, SaveImage, TextEncodeQwenImage21, easy showAnything, KSamplerSelect, TextGenerateLTX2Prompt, EmptyLatentImage, PrimitiveStringMultiline, SamplerCustom, ManualSigmas, PrimitiveStringMultiline, ResolutionSelector, UNETLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/qwen image 2.1 rurbo 文生图_2072128381491171330.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen image 2.1 rurbo 文生图_2072128381491171330.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPLoader`
- `SaveImage`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `KSamplerSelect` ★核心
- `TextGenerateLTX2Prompt`
- `EmptyLatentImage` ★核心
- `PrimitiveStringMultiline`
- `SamplerCustom` ★核心
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`VAEDecode`、`VAELoader`、`CLIPLoader`、`SaveImage`、`TextEncodeQwenImage21`、`KSamplerSelect`、`TextGenerateLTX2Prompt`、`EmptyLatentImage`、`SamplerCustom`、`ManualSigmas`、`ResolutionSelector`、`UNETLoader`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader、KSamplerSelect
