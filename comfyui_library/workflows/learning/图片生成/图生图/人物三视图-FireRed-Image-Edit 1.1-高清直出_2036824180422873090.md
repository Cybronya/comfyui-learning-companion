---
key: 图片生成/图生图/人物三视图-FireRed-Image-Edit 1.1-高清直出_2036824180422873090.json
name: 人物三视图-FireRed-Image-Edit 1.1-高清直出_2036824180422873090
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物三视图-FireRed-Image-Edit 1.1-高清直出_2036824180422873090.json
hash: d7f4e8ef25aeceaa
coverage: 0.894737
learned_at: 2026-10-23 12:09:26
nodes: [KSampler, CustomAddLabel, SaveImage, VAEDecode, easy cleanGpuUsed, UNETLoader, LoraLoaderModelOnly, PrimitiveNode, TextEncodeQwenImageEditPlus, EmptyLatentImage, CLIPLoader, VAELoader, Int, Int, CLIPTextEncode, SaveImage, JjkText, LoadImage, SeedVR2]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 502267236134544, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/人物三视图-FireRed-Image-Edit 1.1-高清直出_2036824180422873090.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物三视图-FireRed-Image-Edit 1.1-高清直出_2036824180422873090.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（19 个）：
- `KSampler` ★核心
- `CustomAddLabel`
- `SaveImage`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveNode`
- `TextEncodeQwenImageEditPlus`
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `VAELoader`
- `Int`
- `Int`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `JjkText`
- `LoadImage`
- `SeedVR2`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `502267236134544`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`KSampler`、`CustomAddLabel`、`SaveImage`、`VAEDecode`、`easy cleanGpuUsed`、`UNETLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImageEditPlus`、`EmptyLatentImage`、`CLIPLoader`、`VAELoader`、`Int`、`CLIPTextEncode`、`LoadImage`、`SeedVR2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
