---
key: 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清出图_2073975079939174402.json
name: FireRed-Image-Edit 1.1-人物面部+全身三视图-高清出图_2073975079939174402
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清出图_2073975079939174402.json
hash: 3f8ec82802051705
coverage: 0.8125
learned_at: 2026-10-23 10:55:32
nodes: [UNETLoader, TextEncodeQwenImageEditPlus, CLIPTextEncode, EmptyLatentImage, LoraLoaderModelOnly, CLIPLoader, PrimitiveNode, KSampler, VAEDecode, RunningHub Deepcleaner, LoadImage, JjkText, PreviewImage, SaveImage, VAELoader, SeedVR2]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 62681201569351, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清出图_2073975079939174402.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清出图_2073975079939174402.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `PrimitiveNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `RunningHub Deepcleaner`
- `LoadImage`
- `JjkText`
- `PreviewImage`
- `SaveImage`
- `VAELoader`
- `SeedVR2`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `62681201569351`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（13/16）

**有卡**：`UNETLoader`、`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`CLIPLoader`、`KSampler`、`VAEDecode`、`RunningHub Deepcleaner`、`LoadImage`、`SaveImage`、`VAELoader`、`SeedVR2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
