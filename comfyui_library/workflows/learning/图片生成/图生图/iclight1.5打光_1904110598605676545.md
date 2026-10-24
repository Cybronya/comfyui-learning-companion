---
key: 图片生成/图生图/iclight1.5打光_1904110598605676545.json
name: iclight1.5打光_1904110598605676545
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/iclight1.5打光_1904110598605676545.json
hash: 6fdc05d2cf8553b9
coverage: 0.8125
learned_at: 2026-10-23 11:37:38
nodes: [VAEEncode, CLIPTextEncode, Image Comparer (rgthree), SaveImage, VAEDecode, MaskToImage, LoadAndApplyICLightUnet, CheckpointLoaderSimple, VAEEncode, MaskBlur+, LoadImage, PreviewImage, Note, ICLightConditioning, CLIPTextEncode, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 8, "checkpoint": "majicmixRealistic_v7.safetensors", "denoise": 0.9400000000000002, "sampler_name": "euler", "scheduler": "normal", "seed": 415359855648681, "steps": 20}
---

# 图片生成/图生图/iclight1.5打光_1904110598605676545.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/iclight1.5打光_1904110598605676545.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAEDecode` ★核心
- `MaskToImage`
- `LoadAndApplyICLightUnet`
- `CheckpointLoaderSimple` ★核心
- `VAEEncode` ★核心
- `MaskBlur+`
- `LoadImage`
- `PreviewImage`
- `Note`
- `ICLightConditioning`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `majicmixRealistic_v7.safetensors`
- `seed` = `415359855648681`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.9400000000000002`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`VAEEncode`、`CLIPTextEncode`、`SaveImage`、`VAEDecode`、`MaskToImage`、`LoadAndApplyICLightUnet`、`CheckpointLoaderSimple`、`MaskBlur+`、`LoadImage`、`ICLightConditioning`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEEncode、ICLightConditioning、SaveImage
