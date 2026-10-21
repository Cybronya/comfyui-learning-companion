---
key: 图片生成/文生图/Z-Image Turbo VS De-Turbo VS Re-Turbo对比_2073390583678332930.json
name: Z-Image Turbo VS De-Turbo VS Re-Turbo对比_2073390583678332930
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image Turbo VS De-Turbo VS Re-Turbo对比_2073390583678332930.json
hash: 19a1284be2b7a6f1
coverage: 1
learned_at: 2026-10-20 00:01:45
nodes: [ConditioningZeroOut, CLIPTextEncode, LayerUtility: PurgeVRAM, KSampler, ConditioningZeroOut, CLIPTextEncode, LayerUtility: PurgeVRAM, KSampler, ConditioningZeroOut, CLIPTextEncode, LayerUtility: PurgeVRAM, KSampler, CLIPLoader, EmptyLatentImage, VAELoader, SaveImage, VAEDecode, VAEDecode, VAEDecode, ImageConcatMulti, UNETLoader, SaveImage, easy promptLine, SaveImage, SaveImage, UNETLoader, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 243292566267486, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image Turbo VS De-Turbo VS Re-Turbo对比_2073390583678332930.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image Turbo VS De-Turbo VS Re-Turbo对比_2073390583678332930.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `UNETLoader` ★核心
- `SaveImage`
- `easy promptLine`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `243292566267486`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`LayerUtility: PurgeVRAM`、`KSampler`、`CLIPLoader`、`EmptyLatentImage`、`VAELoader`、`SaveImage`、`VAEDecode`、`ImageConcatMulti`、`UNETLoader`、`easy promptLine`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
