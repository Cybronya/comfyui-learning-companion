---
key: 图片生成/图生图/Flux.1 Krea Dev图生图【逼真质感 无AI味】_1951177506269409281.json
name: Flux.1 Krea Dev图生图【逼真质感 无AI味】_1951177506269409281
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1 Krea Dev图生图【逼真质感 无AI味】_1951177506269409281.json
hash: 3f6eb183cafa4c66
coverage: 0.894737
learned_at: 2026-10-23 10:58:40
nodes: [ConditioningZeroOut, VAEEncode, CLIPTextEncode, KSampler, DualCLIPLoader, UNETLoader, ImageScaleDownToSize, VAELoader, VAEDecode, RH_Translator, RH_Captioner, Text Concatenate, SaveImage, LoadImage, ImageStitch, PreviewImage, Text Multiline, RepeatLatentBatch, easy showAnything]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 274959697364794, "steps": 20}
---

# 图片生成/图生图/Flux.1 Krea Dev图生图【逼真质感 无AI味】_1951177506269409281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1 Krea Dev图生图【逼真质感 无AI味】_1951177506269409281.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `ImageScaleDownToSize`
- `VAELoader`
- `VAEDecode` ★核心
- `RH_Translator`
- `RH_Captioner`
- `Text Concatenate`
- `SaveImage`
- `LoadImage`
- `ImageStitch`
- `PreviewImage`
- `Text Multiline`
- `RepeatLatentBatch`
- `easy showAnything`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `274959697364794`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`ConditioningZeroOut`、`VAEEncode`、`CLIPTextEncode`、`KSampler`、`DualCLIPLoader`、`UNETLoader`、`ImageScaleDownToSize`、`VAELoader`、`VAEDecode`、`RH_Translator`、`RH_Captioner`、`Text Concatenate`、`SaveImage`、`LoadImage`、`ImageStitch`、`Text Multiline`、`RepeatLatentBatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、RepeatLatentBatch
