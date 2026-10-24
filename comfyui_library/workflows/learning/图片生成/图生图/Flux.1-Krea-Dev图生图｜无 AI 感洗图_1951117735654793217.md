---
key: 图片生成/图生图/Flux.1-Krea-Dev图生图｜无 AI 感洗图_1951117735654793217.json
name: Flux.1-Krea-Dev图生图｜无 AI 感洗图_1951117735654793217
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev图生图｜无 AI 感洗图_1951117735654793217.json
hash: 13d3252da6a59631
coverage: 0.944444
learned_at: 2026-10-23 10:58:43
nodes: [VAELoader, DualCLIPLoader, UNETLoader, KSampler, RepeatLatentBatch, VAEEncode, VAEDecode, SaveImage, SaveImage, ImageStitch, ConditioningZeroOut, CLIPTextEncode, Text Concatenate, ImageScaleDownToSize, RH_Captioner, easy showAnything, LoadImage, Text Multiline]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 65767973718899, "steps": 20}
---

# 图片生成/图生图/Flux.1-Krea-Dev图生图｜无 AI 感洗图_1951117735654793217.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1-Krea-Dev图生图｜无 AI 感洗图_1951117735654793217.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `RepeatLatentBatch`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `ImageStitch`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `Text Concatenate`
- `ImageScaleDownToSize`
- `RH_Captioner`
- `easy showAnything`
- `LoadImage`
- `Text Multiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `65767973718899`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（17/18）

**有卡**：`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`KSampler`、`RepeatLatentBatch`、`VAEEncode`、`VAEDecode`、`SaveImage`、`ImageStitch`、`ConditioningZeroOut`、`CLIPTextEncode`、`Text Concatenate`、`ImageScaleDownToSize`、`RH_Captioner`、`LoadImage`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、RepeatLatentBatch
