---
key: 图片生成/文生图/Z-Image-Base-Text to Image_2016308651929116673.json
name: Z-Image-Base-Text to Image_2016308651929116673
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Base-Text to Image_2016308651929116673.json
hash: c0e3c5a815d13a1a
coverage: 0.846154
learned_at: 2026-10-19 22:15:25
nodes: [VAEDecode, ModelSamplingAuraFlow, SaveImage, Note, SDXL Resolutions (JPS), CLIPTextEncode, CLIPTextEncode, VAELoader, UNETLoader, CLIPLoader, EmptySD3LatentImage, MarkdownNote, KSampler]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 148943568176252, "steps": 50}
---

# 图片生成/文生图/Z-Image-Base-Text to Image_2016308651929116673.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Base-Text to Image_2016308651929116673.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Note`
- `SDXL Resolutions (JPS)`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `EmptySD3LatentImage`
- `MarkdownNote`
- `KSampler` ★核心

## 关键参数

- `seed` = `148943568176252`
- `steps` = `50`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`VAEDecode`、`ModelSamplingAuraFlow`、`SaveImage`、`SDXL Resolutions (JPS)`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`EmptySD3LatentImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、SDXL Resolutions (JPS)、EmptySD3LatentImage
