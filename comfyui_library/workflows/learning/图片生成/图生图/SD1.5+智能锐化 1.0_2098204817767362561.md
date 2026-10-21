---
key: 图片生成/图生图/SD1.5+智能锐化 1.0_2098204817767362561.json
name: SD1.5+智能锐化 1.0_2098204817767362561
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5+智能锐化 1.0_2098204817767362561.json
hash: 54d85828ac783b38
coverage: 1
learned_at: 2026-10-21 00:44:15
nodes: [VAEEncode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPTextEncode, KSampler, CheckpointLoaderSimple, VAEDecode, SaveImage, ImageSmartSharpen+]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 7, "checkpoint": "majicmixRealistic_v7.safetensors", "denoise": 0.10000000000000002, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 667727110413874, "steps": 20}
---

# 图片生成/图生图/SD1.5+智能锐化 1.0_2098204817767362561.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5+智能锐化 1.0_2098204817767362561.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `VAEEncode` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageSmartSharpen+`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `667727110413874`
- `steps` = `20`
- `cfg` = `7`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`
- `checkpoint` = `majicmixRealistic_v7.safetensors`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`VAEEncode`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`KSampler`、`CheckpointLoaderSimple`、`VAEDecode`、`SaveImage`、`ImageSmartSharpen+`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEEncode、SaveImage、ImageSmartSharpen+
