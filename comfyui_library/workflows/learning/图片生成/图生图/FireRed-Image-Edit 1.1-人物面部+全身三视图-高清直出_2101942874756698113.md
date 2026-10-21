---
key: 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2101942874756698113.json
name: FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2101942874756698113
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2101942874756698113.json
hash: 0cb30147735d3cec
coverage: 0.75
learned_at: 2026-10-21 00:39:20
nodes: [PrimitiveNode, TextEncodeQwenImageEditPlus, CLIPTextEncode, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, KSampler, SaveImage, EmptyLatentImage, LoadImage, VAEDecode, RunningHub Deepcleaner, JjkText, SeedVR2, MarkdownNote, CustomAddLabel, SaveImage, MarkdownNote, 孤海注释]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 308871400890289, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2101942874756698113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-人物面部+全身三视图-高清直出_2101942874756698113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（20 个）：
- `PrimitiveNode`
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `RunningHub Deepcleaner`
- `JjkText`
- `SeedVR2`
- `MarkdownNote`
- `CustomAddLabel`
- `SaveImage`
- `MarkdownNote`
- `孤海注释`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `308871400890289`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **75%**（15/20）

**有卡**：`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`LoadImage`、`VAEDecode`、`RunningHub Deepcleaner`、`SeedVR2`、`CustomAddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
