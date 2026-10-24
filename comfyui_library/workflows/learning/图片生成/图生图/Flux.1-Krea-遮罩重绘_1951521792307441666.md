---
key: 图片生成/图生图/Flux.1-Krea-遮罩重绘_1951521792307441666.json
name: Flux.1-Krea-遮罩重绘_1951521792307441666
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-遮罩重绘_1951521792307441666.json
hash: e8cfdc09d73d2611
coverage: 0.9
learned_at: 2026-10-23 10:58:43
nodes: [SaveImage, SaveImage, VAEDecode, KSampler, CLIPTextEncode, RepeatLatentBatch, DualCLIPLoader, UNETLoader, VAELoader, Note, ImpactGaussianBlurMask, Text Concatenate, LoraLoaderModelOnly, MaskPreview, InpaintModelConditioning, ConditioningZeroOut, LoadImage, easy showAnything, RH_Translator, ImageStitch]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 587799825032737, "steps": 20}
---

# 图片生成/图生图/Flux.1-Krea-遮罩重绘_1951521792307441666.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-遮罩重绘_1951521792307441666.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `RepeatLatentBatch`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `Note`
- `ImpactGaussianBlurMask`
- `Text Concatenate`
- `LoraLoaderModelOnly` ★核心
- `MaskPreview`
- `InpaintModelConditioning`
- `ConditioningZeroOut`
- `LoadImage`
- `easy showAnything`
- `RH_Translator`
- `ImageStitch`

## 关键参数

- `seed` = `587799825032737`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`SaveImage`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`RepeatLatentBatch`、`DualCLIPLoader`、`UNETLoader`、`VAELoader`、`ImpactGaussianBlurMask`、`Text Concatenate`、`LoraLoaderModelOnly`、`MaskPreview`、`InpaintModelConditioning`、`ConditioningZeroOut`、`LoadImage`、`RH_Translator`、`ImageStitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader
