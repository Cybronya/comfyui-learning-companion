---
key: 图片生成/文生图/qwen-image2.1文生图_2115022402173358081.json
name: qwen-image2.1文生图_2115022402173358081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image2.1文生图_2115022402173358081.json
hash: a381c32dc00028c1
coverage: 0.8
learned_at: 2026-10-30 17:55:45
nodes: [ResolutionSelector, UNETLoader, TextEncodeQwenImage21, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, SaveImage, TextInputNode, CLIPLoader, PrimitiveStringMultiline, TextGenerate, PreviewAny, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 447606998181262, "steps": 30, "width": 1024}
---

# 图片生成/文生图/qwen-image2.1文生图_2115022402173358081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image2.1文生图_2115022402173358081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（15 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `TextInputNode`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `TextGenerate`
- `PreviewAny`
- `ComfySwitchNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `447606998181262`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`ResolutionSelector`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`TextInputNode`、`TextGenerate`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、UNETLoader
