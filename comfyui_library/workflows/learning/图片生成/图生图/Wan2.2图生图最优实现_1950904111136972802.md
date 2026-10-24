---
key: 图片生成/图生图/Wan2.2图生图最优实现_1950904111136972802.json
name: Wan2.2图生图最优实现_1950904111136972802
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2图生图最优实现_1950904111136972802.json
hash: 9f7700fd94cda49d
coverage: 0.947368
learned_at: 2026-10-23 11:28:21
nodes: [SaveImage, easy seed, String Literal, VAEDecode, UNETLoader, CLIPLoader, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, VAELoader, VAEEncode, VAEDecode, ImageResizeKJv2, KSampler, KSampler, PreviewImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3.5, "denoise": 0.4000000000000001, "sampler_name": "euler", "scheduler": "simple", "seed": 764940855534971, "steps": 20}
---

# 图片生成/图生图/Wan2.2图生图最优实现_1950904111136972802.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2图生图最优实现_1950904111136972802.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `SaveImage`
- `easy seed`
- `String Literal`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `KSampler` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `764940855534971`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4000000000000001`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`SaveImage`、`easy seed`、`String Literal`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`VAEEncode`、`ImageResizeKJv2`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、easy seed
