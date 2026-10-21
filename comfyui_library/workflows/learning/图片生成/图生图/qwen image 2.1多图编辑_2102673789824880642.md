---
key: 图片生成/图生图/qwen image 2.1多图编辑_2102673789824880642.json
name: qwen image 2.1多图编辑_2102673789824880642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image 2.1多图编辑_2102673789824880642.json
hash: 87956f0d663952ae
coverage: 0.826087
learned_at: 2026-10-21 00:46:01
nodes: [CLIPLoader, CLIPLoader, MarkdownNote, VAELoader, TextGenerateLTX2Prompt, ResolutionSelector, BatchImagesNode, TextEncodeQwenImage21, UNETLoader, KSampler, LoadImage, VAEDecode, SaveImage, PreviewImage, ImpactConditionalBranch, EmptyLatentImage, QwenImage21Cache, easy showAnything, ImageConcatMulti, ImageConcatMulti, LoadImage, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1034844694223447, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen image 2.1多图编辑_2102673789824880642.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image 2.1多图编辑_2102673789824880642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `CLIPLoader`
- `CLIPLoader`
- `MarkdownNote`
- `VAELoader`
- `TextGenerateLTX2Prompt`
- `ResolutionSelector`
- `BatchImagesNode`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `ImpactConditionalBranch`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `easy showAnything`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `1034844694223447`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`CLIPLoader`、`VAELoader`、`TextGenerateLTX2Prompt`、`ResolutionSelector`、`BatchImagesNode`、`TextEncodeQwenImage21`、`UNETLoader`、`KSampler`、`LoadImage`、`VAEDecode`、`SaveImage`、`ImpactConditionalBranch`、`EmptyLatentImage`、`QwenImage21Cache`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
