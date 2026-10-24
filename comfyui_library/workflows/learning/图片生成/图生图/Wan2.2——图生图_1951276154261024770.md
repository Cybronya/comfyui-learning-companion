---
key: 图片生成/图生图/Wan2.2——图生图_1951276154261024770.json
name: Wan2.2——图生图_1951276154261024770
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2——图生图_1951276154261024770.json
hash: 0a5c84a30dc1fbba
coverage: 0.9375
learned_at: 2026-10-23 11:28:11
nodes: [CLIPTextEncode, ModelSamplingSD3, PreviewImage, UNETLoader, UNETLoader, CLIPLoader, VAEDecode, SaveImage, ModelSamplingSD3, LoadImage, CLIPTextEncode, ImageResizeKJv2, VAELoader, VAEEncode, KSampler, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3.5, "denoise": 0.3500000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 751444142837848, "steps": 10}
---

# 图片生成/图生图/Wan2.2——图生图_1951276154261024770.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2——图生图_1951276154261024770.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `PreviewImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `ModelSamplingSD3`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `VAELoader`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `751444142837848`
- `steps` = `10`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.3500000000000001`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`CLIPTextEncode`、`ModelSamplingSD3`、`UNETLoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`LoadImage`、`ImageResizeKJv2`、`VAELoader`、`VAEEncode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
