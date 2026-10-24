---
key: 图片生成/图生图/FireRed-Image-Edit 1.1-场景一致性_2045840113577500674.json
name: FireRed-Image-Edit 1.1-场景一致性_2045840113577500674
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-场景一致性_2045840113577500674.json
hash: d8b477dcce770a02
coverage: 0.806452
learned_at: 2026-10-23 10:55:36
nodes: [PrimitiveNode, TextEncodeQwenImageEditPlus, UNETLoader, CLIPLoader, VAELoader, KSampler, EmptyLatentImage, VAEDecode, CLIPTextEncode, PrimitiveNode, TextEncodeQwenImageEditPlus, CustomAddLabel, EmptyLatentImage, VAEDecode, SeedVR2, CLIPTextEncode, RunningHub Deepcleaner, DrawMaskOnImage, GetImageSize, PreviewImage, RunningHub Deepcleaner, ImageScaleToTotalPixels, LoraLoaderModelOnly, KSampler, JjkText, SaveImage, SaveImage, JjkText, ImagePadForOutpaint, LoadImage, MarkdownNote]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 132287402254739, "steps": 8, "width": 2048}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-Edit 1.1-场景一致性_2045840113577500674.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-Edit 1.1-场景一致性_2045840113577500674.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `PrimitiveNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `TextEncodeQwenImageEditPlus`
- `CustomAddLabel`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `SeedVR2`
- `CLIPTextEncode` ★核心
- `RunningHub Deepcleaner`
- `DrawMaskOnImage`
- `GetImageSize`
- `PreviewImage`
- `RunningHub Deepcleaner`
- `ImageScaleToTotalPixels`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `JjkText`
- `SaveImage`
- `SaveImage`
- `JjkText`
- `ImagePadForOutpaint`
- `LoadImage`
- `MarkdownNote`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `132287402254739`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `2048`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（25/31）

**有卡**：`TextEncodeQwenImageEditPlus`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`CLIPTextEncode`、`CustomAddLabel`、`SeedVR2`、`RunningHub Deepcleaner`、`DrawMaskOnImage`、`GetImageSize`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`SaveImage`、`ImagePadForOutpaint`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
