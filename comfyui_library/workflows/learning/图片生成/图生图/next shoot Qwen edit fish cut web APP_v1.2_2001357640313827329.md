---
key: 图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.2_2001357640313827329.json
name: next shoot Qwen edit fish cut web APP_v1.2_2001357640313827329
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.2_2001357640313827329.json
hash: cb0921b7fb930808
coverage: 1
learned_at: 2026-10-23 11:41:08
nodes: [CFGNorm, ModelSamplingAuraFlow, VAELoader, ImageScaleToTotalPixels, VAEDecode, TextEncodeQwenImageEditPlus, SaveImage, CR Text Concatenate, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPLoader, TextEncodeQwenImageEditPlus, UNETLoader, CR Text, EmptyLatentImage, CR Text, CR Text, KSampler, LoadImage, 孤海图像缩放按像素]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 768, "sampler_name": "euler", "scheduler": "simple", "seed": 884020837952328, "steps": 8, "width": 1344}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.2_2001357640313827329.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/next shoot Qwen edit fish cut web APP_v1.2_2001357640313827329.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `SaveImage`
- `CR Text Concatenate`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `CR Text`
- `EmptyLatentImage` ★核心
- `CR Text`
- `CR Text`
- `KSampler` ★核心
- `LoadImage`
- `孤海图像缩放按像素`

## 关键参数

- `width` = `1344`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `884020837952328`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CFGNorm`、`ModelSamplingAuraFlow`、`VAELoader`、`ImageScaleToTotalPixels`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`SaveImage`、`CR Text Concatenate`、`LoraLoaderModelOnly`、`CLIPLoader`、`UNETLoader`、`CR Text`、`EmptyLatentImage`、`KSampler`、`LoadImage`、`孤海图像缩放按像素`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
