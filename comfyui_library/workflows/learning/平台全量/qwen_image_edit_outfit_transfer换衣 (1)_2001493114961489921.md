---
key: 平台全量/qwen_image_edit_outfit_transfer换衣 (1)_2001493114961489921.json
name: qwen_image_edit_outfit_transfer换衣 (1)_2001493114961489921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen_image_edit_outfit_transfer换衣 (1)_2001493114961489921.json
hash: 49729bcd52c4798f
coverage: 0.589744
learned_at: 2026-11-14 01:16:38
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, GetNode, SetNode, CLIPLoader, SetNode, VAELoader, ConditioningZeroOut, EmptyLatentImage, ConditioningZeroOut, EmptyLatentImage, UNETLoader, SetNode, VAEDecode, TextEncodeQwenImageEditPlus, GetNode, SetNode, SetNode, GetImageSize, ImageScaleToTotalPixels, KSampler, VAEDecode, GetNode, LoadImage, SaveImage, SetNode, SaveImage, LoadImage, LoraLoaderModelOnly, LoadImage, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), TextEncodeQwenImageEditPlus, LoraLoaderModelOnly]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 174458152021336, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/qwen_image_edit_outfit_transfer换衣 (1)_2001493114961489921.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen_image_edit_outfit_transfer换衣 (1)_2001493114961489921.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `LoadImage`
- `SaveImage`
- `SetNode`
- `SaveImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `174458152021336`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **59%**（23/39）

**有卡**：`KSampler`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`EmptyLatentImage`、`UNETLoader`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`GetImageSize`、`ImageScaleToTotalPixels`、`LoadImage`、`SaveImage`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
