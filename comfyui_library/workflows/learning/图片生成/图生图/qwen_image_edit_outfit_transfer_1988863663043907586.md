---
key: 图片生成/图生图/qwen_image_edit_outfit_transfer_1988863663043907586.json
name: qwen_image_edit_outfit_transfer_1988863663043907586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_edit_outfit_transfer_1988863663043907586.json
hash: 4c50f4b2182bdb9d
coverage: 0.621622
learned_at: 2026-10-23 11:44:05
nodes: [GetNode, GetNode, KSampler, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSampler, GetNode, SaveImage, VAEDecode, SetNode, VAEDecode, UNETLoader, LoraLoaderModelOnly, SetNode, CLIPLoader, SetNode, VAELoader, SetNode, LoraLoaderModelOnly, LoadImage, TextEncodeQwenImageEditPlus, ConditioningZeroOut, EmptyLatentImage, LoraLoaderModelOnly, ConditioningZeroOut, ImageScaleToTotalPixels, GetImageSize, EmptyLatentImage, TextEncodeQwenImageEditPlus, LoadImage, SaveImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 756469783557218, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen_image_edit_outfit_transfer_1988863663043907586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_edit_outfit_transfer_1988863663043907586.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `SaveImage`
- `VAEDecode` ★核心
- `SetNode`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `756469783557218`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **62%**（23/37）

**有卡**：`KSampler`、`SaveImage`、`VAEDecode`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`LoadImage`、`TextEncodeQwenImageEditPlus`、`ConditioningZeroOut`、`EmptyLatentImage`、`ImageScaleToTotalPixels`、`GetImageSize`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
