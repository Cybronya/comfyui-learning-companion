---
key: 图片生成/图生图/FLUX.1图生图工作流_2088546573432217602.json
name: FLUX.1图生图工作流_2088546573432217602
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1图生图工作流_2088546573432217602.json
hash: 64b90ae13ae108a8
coverage: 1
learned_at: 2026-10-23 10:54:03
nodes: [DualCLIPLoader, VAELoader, VAEDecode, FluxGuidance, EmptySD3LatentImage, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, ImageScale, VAEEncode, CLIPTextEncode, KSampler, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.5000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 802936198406199, "steps": 30}
---

# 图片生成/图生图/FLUX.1图生图工作流_2088546573432217602.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1图生图工作流_2088546573432217602.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `FluxGuidance`
- `EmptySD3LatentImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageScale`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `802936198406199`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`FluxGuidance`、`EmptySD3LatentImage`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`ImageScale`、`VAEEncode`、`KSampler`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance
