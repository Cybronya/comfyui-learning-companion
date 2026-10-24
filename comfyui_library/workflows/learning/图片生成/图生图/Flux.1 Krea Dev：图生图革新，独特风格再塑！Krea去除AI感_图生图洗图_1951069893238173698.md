---
key: 图片生成/图生图/Flux.1 Krea Dev：图生图革新，独特风格再塑！Krea去除AI感_图生图洗图_1951069893238173698.json
name: Flux.1 Krea Dev：图生图革新，独特风格再塑！Krea去除AI感_图生图洗图_1951069893238173698
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.1 Krea Dev：图生图革新，独特风格再塑！Krea去除AI感_图生图洗图_1951069893238173698.json
hash: 18bbd5e45f84c32e
coverage: 0.947368
learned_at: 2026-10-23 10:58:40
nodes: [UNETLoader, ConditioningZeroOut, SaveImage, VAELoader, VAEEncode, VAEDecode, SaveImage, easy imageConcat, ImageScaleDownToSize, LoadImage, Florence2ModelLoader, DualCLIPLoader, Florence2Run, Text Multiline, Text Concatenate, RH_Translator, easy showAnything, CLIPTextEncode, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.9000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 1112605903191943, "steps": 20}
---

# 图片生成/图生图/Flux.1 Krea Dev：图生图革新，独特风格再塑！Krea去除AI感_图生图洗图_1951069893238173698.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.1 Krea Dev：图生图革新，独特风格再塑！Krea去除AI感_图生图洗图_1951069893238173698.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `VAELoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `easy imageConcat`
- `ImageScaleDownToSize`
- `LoadImage`
- `Florence2ModelLoader`
- `DualCLIPLoader`
- `Florence2Run`
- `Text Multiline`
- `Text Concatenate`
- `RH_Translator`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1112605903191943`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.9000000000000001`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`UNETLoader`、`ConditioningZeroOut`、`SaveImage`、`VAELoader`、`VAEEncode`、`VAEDecode`、`easy imageConcat`、`ImageScaleDownToSize`、`LoadImage`、`Florence2ModelLoader`、`DualCLIPLoader`、`Florence2Run`、`Text Multiline`、`Text Concatenate`、`RH_Translator`、`CLIPTextEncode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader、VAEEncode
