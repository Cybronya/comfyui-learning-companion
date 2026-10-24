---
key: 图片生成/图生图/Flux.1-Krea-Dev图生图-NUCHAKU版本_1951478524945313793.json
name: Flux.1-Krea-Dev图生图-NUCHAKU版本_1951478524945313793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev图生图-NUCHAKU版本_1951478524945313793.json
hash: 300c76ca6b7f479b
coverage: 0.947368
learned_at: 2026-10-23 10:58:41
nodes: [NunchakuFluxDiTLoader, ImageStitch, CLIPTextEncode, VAELoader, ConditioningZeroOut, VAEDecode, LoadImage, InpaintModelConditioning, Text Multiline, ImageScaleDownToSize, RH_Captioner, RepeatLatentBatch, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, Text Concatenate, DualCLIPLoader, SaveImage, SaveImage, KSampler]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 0.8000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 639644880926412, "steps": 20}
---

# 图片生成/图生图/Flux.1-Krea-Dev图生图-NUCHAKU版本_1951478524945313793.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev图生图-NUCHAKU版本_1951478524945313793.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `NunchakuFluxDiTLoader`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `LoadImage`
- `InpaintModelConditioning`
- `Text Multiline`
- `ImageScaleDownToSize`
- `RH_Captioner`
- `RepeatLatentBatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `Text Concatenate`
- `DualCLIPLoader`
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心

## 关键参数

- `seed` = `639644880926412`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.8000000000000002`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`NunchakuFluxDiTLoader`、`ImageStitch`、`CLIPTextEncode`、`VAELoader`、`ConditioningZeroOut`、`VAEDecode`、`LoadImage`、`InpaintModelConditioning`、`Text Multiline`、`ImageScaleDownToSize`、`RH_Captioner`、`RepeatLatentBatch`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text Concatenate`、`DualCLIPLoader`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、RepeatLatentBatch、DualCLIPLoader
