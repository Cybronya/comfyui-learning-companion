---
key: 图片生成/图生图/SD1.5 ControlNet+智能锐化 1.0_2098206538765783041.json
name: SD1.5 ControlNet+智能锐化 1.0_2098206538765783041
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5 ControlNet+智能锐化 1.0_2098206538765783041.json
hash: de097ec74b25a6fb
coverage: 0.928571
learned_at: 2026-10-21 00:44:15
nodes: [VAEEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, PreviewImage, CLIPTextEncode, CLIPTextEncode, ControlNetLoader, CheckpointLoaderSimple, KSampler, ControlNetApplyAdvanced, VAEDecode, ImageSmartSharpen+, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 7, "checkpoint": "majicmixRealistic_v7.safetensors", "controlnet_strength": 1, "denoise": 0.10000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 239872360569482, "steps": 20}
---

# 图片生成/图生图/SD1.5 ControlNet+智能锐化 1.0_2098206538765783041.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5 ControlNet+智能锐化 1.0_2098206538765783041.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `VAEEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `ControlNetApplyAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageSmartSharpen+`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `majicmixRealistic_v7.safetensors`
- `seed` = `239872360569482`
- `steps` = `20`
- `cfg` = `7`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`
- `controlnet_strength` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`VAEEncode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`AIO_Preprocessor`、`CLIPTextEncode`、`ControlNetLoader`、`CheckpointLoaderSimple`、`KSampler`、`ControlNetApplyAdvanced`、`VAEDecode`、`ImageSmartSharpen+`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、VAEEncode
