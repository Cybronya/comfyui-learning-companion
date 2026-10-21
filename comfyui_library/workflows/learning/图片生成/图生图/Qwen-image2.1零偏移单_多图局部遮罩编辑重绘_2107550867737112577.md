---
key: 图片生成/图生图/Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107550867737112577.json
name: Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107550867737112577
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107550867737112577.json
hash: 2e6ea4d26e29436a
coverage: 0.857143
learned_at: 2026-10-21 00:43:31
nodes: [CLIPLoader, VAELoader, VAEDecode, GetImageSize, VAEEncode, SetLatentNoiseMask, ResizeImageMaskNode, LoadImage, QwenImage21Cache, Image Comparer (rgthree), Note, SaveImage, UNETLoader, KSampler, PrimitiveStringMultiline, LoadImage, RHHiddenNodes, TextEncodeQwenImage21, VAEDecode, WujiUpscaler2, WujiCleaner]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 507830684350889, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107550867737112577.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1零偏移单_多图局部遮罩编辑重绘_2107550867737112577.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `GetImageSize`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `ResizeImageMaskNode`
- `LoadImage`
- `QwenImage21Cache`
- `Image Comparer (rgthree)`
- `Note`
- `SaveImage`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `RHHiddenNodes`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `WujiUpscaler2`
- `WujiCleaner`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `507830684350889`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`GetImageSize`、`VAEEncode`、`SetLatentNoiseMask`、`ResizeImageMaskNode`、`LoadImage`、`QwenImage21Cache`、`SaveImage`、`UNETLoader`、`KSampler`、`RHHiddenNodes`、`TextEncodeQwenImage21`、`WujiUpscaler2`、`WujiCleaner`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
