---
key: 图片生成/图生图/Flux.1-Krea-Dev图生图-无AI味超细节_1951506881573498882.json
name: Flux.1-Krea-Dev图生图-无AI味超细节_1951506881573498882
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev图生图-无AI味超细节_1951506881573498882.json
hash: 1de004c968a7ec93
coverage: 0.9
learned_at: 2026-10-23 10:58:42
nodes: [VAELoader, DualCLIPLoader, ImageStitch, VAEEncode, RH_Captioner, ImageScaleDownToSize, Text Multiline, VAEDecode, Text Concatenate, ConditioningZeroOut, CLIPTextEncode, easy showAnything, RepeatLatentBatch, UNETLoader, LoadImage, NunchakuFluxDiTLoader, SaveImage, SaveImage, KSampler, PrimitiveFloat]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.6000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 510844781850037, "steps": 20}
---

# 图片生成/图生图/Flux.1-Krea-Dev图生图-无AI味超细节_1951506881573498882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev图生图-无AI味超细节_1951506881573498882.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAELoader`
- `DualCLIPLoader`
- `ImageStitch`
- `VAEEncode` ★核心
- `RH_Captioner`
- `ImageScaleDownToSize`
- `Text Multiline`
- `VAEDecode` ★核心
- `Text Concatenate`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `RepeatLatentBatch`
- `UNETLoader` ★核心
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `PrimitiveFloat`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `510844781850037`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`VAELoader`、`DualCLIPLoader`、`ImageStitch`、`VAEEncode`、`RH_Captioner`、`ImageScaleDownToSize`、`Text Multiline`、`VAEDecode`、`Text Concatenate`、`ConditioningZeroOut`、`CLIPTextEncode`、`RepeatLatentBatch`、`UNETLoader`、`LoadImage`、`NunchakuFluxDiTLoader`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、RepeatLatentBatch
