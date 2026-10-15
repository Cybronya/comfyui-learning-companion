---
key: 图片生成/文生图/Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890.json
name: Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890.json
hash: 85940428fdf8632d
coverage: 0.727273
learned_at: 2026-10-10 20:58:36
nodes: [DualCLIPLoader, MarkdownNote, MarkdownNote, UNETLoader, VAEDecode, SaveImage, SaveImage, ImageStitch, CLIPTextEncode, Text Concatenate, ConditioningZeroOut, KSampler, VAELoader, LoadImage, MaskPreview, easy showAnything, Text Multiline, Note, LoraLoaderModelOnly, RepeatLatentBatch, InpaintModelConditioning, ImpactGaussianBlurMask]
patterns: []
missing: [Text Concatenate, Text Multiline]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 918845898843823, "steps": 20}
discoveries: [次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890.json`

## 结构

**节点**（22 个）：
- `DualCLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader`
- `VAEDecode`
- `SaveImage`
- `SaveImage`
- `ImageStitch`
- `CLIPTextEncode`
- `Text Concatenate`
- `ConditioningZeroOut`
- `KSampler`
- `VAELoader`
- `LoadImage`
- `MaskPreview`
- `easy showAnything`
- `Text Multiline`
- `Note`
- `LoraLoaderModelOnly`
- `RepeatLatentBatch`
- `InpaintModelConditioning`
- `ImpactGaussianBlurMask`

## 关键参数

- `cfg` = `1`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `918845898843823`
- `steps` = `20`

## 知识

覆盖率 **73%**（16/22）

**有卡**：`DualCLIPLoader`、`MarkdownNote`、`UNETLoader`、`VAEDecode`、`SaveImage`、`ImageStitch`、`CLIPTextEncode`、`Text Concatenate`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`LoadImage`、`MaskPreview`、`easy showAnything`

**缺卡**（2）：`Text Concatenate`、`Text Multiline`

## 学习发现

- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
