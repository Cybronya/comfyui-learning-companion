---
key: 图片生成/图生图/qwen2.1-image-图片编辑_2114193382485618689.json
name: qwen2.1-image-图片编辑_2114193382485618689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1-image-图片编辑_2114193382485618689.json
hash: 31be36071c958243
coverage: 0.666667
learned_at: 2026-10-26 22:04:18
nodes: [JsonExtractString, PreviewAny, PreviewAny, VAEDecode, SaveImage, Note, PreviewAny, BatchImagesNode, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, CLIPLoader, TextGenerate, PrimitiveStringMultiline, VAELoader, CLIPLoader, UNETLoader, PrimitiveStringMultiline, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 260923, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen2.1-image-图片编辑_2114193382485618689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1-image-图片编辑_2114193382485618689.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `JsonExtractString`
- `PreviewAny`
- `PreviewAny`
- `VAEDecode` ★核心
- `SaveImage`
- `Note`
- `PreviewAny`
- `BatchImagesNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `CLIPLoader`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `260923`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **67%**（14/21）

**有卡**：`JsonExtractString`、`VAEDecode`、`SaveImage`、`BatchImagesNode`、`ResolutionSelector`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`LoadImage`、`CLIPLoader`、`TextGenerate`、`VAELoader`、`UNETLoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
