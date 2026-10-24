---
key: 图片生成/图生图/FireRed-Image-Edit 1.1-面部三视图-高清直出_2045087093600292865.json
name: FireRed-Image-Edit 1.1-面部三视图-高清直出_2045087093600292865
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-面部三视图-高清直出_2045087093600292865.json
hash: 724646ca37119961
coverage: 0.882353
learned_at: 2026-10-23 10:55:37
nodes: [VAEDecode, PrimitiveNode, TextEncodeQwenImageEditPlus, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSampler, SaveImage, SaveImage, EmptyLatentImage, LoadImage, CustomAddLabel, easy cleanGpuUsed, SeedVR2, JjkText]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 447259658214550, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1-面部三视图-高清直出_2045087093600292865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-面部三视图-高清直出_2045087093600292865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `VAEDecode` ★核心
- `PrimitiveNode`
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `SaveImage`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `CustomAddLabel`
- `easy cleanGpuUsed`
- `SeedVR2`
- `JjkText`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `447259658214550`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`VAEDecode`、`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`LoadImage`、`CustomAddLabel`、`easy cleanGpuUsed`、`SeedVR2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
