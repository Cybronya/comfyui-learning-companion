---
key: 图片生成/文生图/lty_古风动漫V1.0_1992764574332153857.json
name: lty_古风动漫V1.0_1992764574332153857
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/lty_古风动漫V1.0_1992764574332153857.json
hash: 2b886552f2707d27
coverage: 0.941176
learned_at: 2026-10-19 20:34:27
nodes: [SeedVR2BlockSwap, ImageScaleToTotalPixels, SeedVR2ExtraArgs, SeedVR2, SaveImage, Image Comparer (rgthree), VAEDecode, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, UNETLoader, CLIPTextEncode, CLIPLoader, KSampler, EmptyLatentImage, ConditioningZeroOut]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 383941557453118, "steps": 8, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/lty_古风动漫V1.0_1992764574332153857.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/lty_古风动漫V1.0_1992764574332153857.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `SeedVR2BlockSwap`
- `ImageScaleToTotalPixels`
- `SeedVR2ExtraArgs`
- `SeedVR2`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `383941557453118`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`SeedVR2BlockSwap`、`ImageScaleToTotalPixels`、`SeedVR2ExtraArgs`、`SeedVR2`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`KSampler`、`EmptyLatentImage`、`ConditioningZeroOut`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
