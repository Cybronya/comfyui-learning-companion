---
key: 图片生成/图生图/分镜流qwen-image-2.1_2103091290836652033.json
name: 分镜流qwen-image-2.1_2103091290836652033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/分镜流qwen-image-2.1_2103091290836652033.json
hash: 0180671bc8f9857d
coverage: 0.477612
learned_at: 2026-10-21 00:49:45
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), SetNode, Label (rgthree), PrimitiveInt, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Note, Label (rgthree), PrimitiveStringMultiline, Note, Note, Note, SetNode, PrimitiveFloat, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ResolutionSelector, SetNode, SetNode, SetNode, Label (rgthree), SetNode, SetNode, GetNode, GetNode, PrimitiveInt, Label (rgthree), UNETLoader, CLIPLoader, VAELoader, LoadImage, LoadImage, LoadImage, LoadImage, BatchImagesNode, SetNode, LoadImage, SetNode, LoadImage, KSampler, VAEDecode, GetNode, GetNode, GetNode, GetNode, EmptyLatentImage, TextEncodeQwenImage21, GetNode, CLIPLoader, SplitImageWithAlpha, TextGenerate, SaveImage, Text Multiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 967310508490443, "steps": 25, "width": 1024}
---

# 图片生成/图生图/分镜流qwen-image-2.1_2103091290836652033.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/分镜流qwen-image-2.1_2103091290836652033.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `Label (rgthree)`
- `PrimitiveInt`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`
- `Label (rgthree)`
- `PrimitiveStringMultiline`
- `Note`
- `Note`
- `Note`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `BatchImagesNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `GetNode`
- `CLIPLoader`
- `SplitImageWithAlpha`
- `TextGenerate`
- `SaveImage`
- `Text Multiline`

## 关键参数

- `seed` = `967310508490443`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **48%**（32/67）

**有卡**：`Label (rgthree)`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`BatchImagesNode`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`SplitImageWithAlpha`、`TextGenerate`、`SaveImage`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
