---
key: 图片生成/文生图/Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890.json
name: Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890.json
hash: 85940428fdf8632d
coverage: 0.818182
learned_at: 2026-10-15 22:26:25
nodes: [DualCLIPLoader, MarkdownNote, MarkdownNote, UNETLoader, VAEDecode, SaveImage, SaveImage, ImageStitch, CLIPTextEncode, Text Concatenate, ConditioningZeroOut, KSampler, VAELoader, LoadImage, MaskPreview, easy showAnything, Text Multiline, Note, LoraLoaderModelOnly, RepeatLatentBatch, InpaintModelConditioning, ImpactGaussianBlurMask]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 918845898843823, "steps": 20}
---

# 图片生成/文生图/Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-Krea-遮罩重绘-无AI味逼真质感_1951240129228709890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `DualCLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAELoader`
- `LoadImage`
- `MaskPreview`
- `easy showAnything`
- `Text Multiline`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `RepeatLatentBatch`
- `InpaintModelConditioning`
- `ImpactGaussianBlurMask`

## 关键参数

- `seed` = `918845898843823`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`VAEDecode`、`SaveImage`、`ImageStitch`、`CLIPTextEncode`、`Text Concatenate`、`ConditioningZeroOut`、`KSampler`、`VAELoader`、`LoadImage`、`MaskPreview`、`Text Multiline`、`LoraLoaderModelOnly`、`RepeatLatentBatch`、`InpaintModelConditioning`、`ImpactGaussianBlurMask`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader
