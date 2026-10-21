---
key: 图片生成/文生图/单图编辑 ( Krea 2 Identity Edit v1.2 ）_2079889925343891458.json
name: 单图编辑 ( Krea 2 Identity Edit v1.2 ）_2079889925343891458
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/单图编辑 ( Krea 2 Identity Edit v1.2 ）_2079889925343891458.json
hash: 038585b742ab0efc
coverage: 0.64
learned_at: 2026-10-20 00:40:21
nodes: [KSampler, VAEDecode, VAEEncode, Krea2EditModelPatch, EmptySD3LatentImage, ResolutionSelector, Krea2EditGroundedEncode, LoadImage, VAEEncode, Note, Note, Note, Note, Note, Note, Note, CLIPLoader, UNETLoader, VAELoader, LoadImage, Note, SaveImage, LoraLoaderModelOnly, Krea2EditGroundedEncode, JjkText]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 292920134750707, "steps": 10}
---

# 图片生成/文生图/单图编辑 ( Krea 2 Identity Edit v1.2 ）_2079889925343891458.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/单图编辑 ( Krea 2 Identity Edit v1.2 ）_2079889925343891458.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `Krea2EditModelPatch`
- `EmptySD3LatentImage`
- `ResolutionSelector`
- `Krea2EditGroundedEncode`
- `LoadImage`
- `VAEEncode` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoadImage`
- `Note`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `Krea2EditGroundedEncode`
- `JjkText`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `292920134750707`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **64%**（16/25）

**有卡**：`KSampler`、`VAEDecode`、`VAEEncode`、`Krea2EditModelPatch`、`EmptySD3LatentImage`、`ResolutionSelector`、`Krea2EditGroundedEncode`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader
