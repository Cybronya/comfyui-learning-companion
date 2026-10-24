---
key: 图片生成/图生图/FireRed-Image-Edit 1.1-户外全景图-高清直出_2045819047106846721.json
name: FireRed-Image-Edit 1.1-户外全景图-高清直出_2045819047106846721
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-户外全景图-高清直出_2045819047106846721.json
hash: 5be762a45c2eee2a
coverage: 0.882353
learned_at: 2026-10-23 10:55:37
nodes: [PrimitiveNode, TextEncodeQwenImageEditPlus, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSampler, SaveImage, CustomAddLabel, SaveImage, EmptyLatentImage, LoadImage, JjkText, SeedVR2, VAEDecode, RunningHub Deepcleaner]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 250590263149287, "steps": 8, "width": 2048}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1-户外全景图-高清直出_2045819047106846721.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-户外全景图-高清直出_2045819047106846721.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `PrimitiveNode`
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `SaveImage`
- `CustomAddLabel`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `JjkText`
- `SeedVR2`
- `VAEDecode` ★核心
- `RunningHub Deepcleaner`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `250590263149287`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `2048`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`KSampler`、`SaveImage`、`CustomAddLabel`、`EmptyLatentImage`、`LoadImage`、`SeedVR2`、`VAEDecode`、`RunningHub Deepcleaner`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
