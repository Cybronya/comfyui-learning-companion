---
key: 图片生成/图生图/FireRed-edit1.1-单图编辑_2029538924632219649.json
name: FireRed-edit1.1-单图编辑_2029538924632219649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-edit1.1-单图编辑_2029538924632219649.json
hash: 05bc77e93f143f7d
coverage: 0.923077
learned_at: 2026-10-23 10:55:53
nodes: [EmptyLatentImage, VAELoader, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, Image Comparer (rgthree), LoadImage, UNETLoader, CLIPLoader, TextEncodeQwenImageEditPlus, LoraLoaderModelOnly, KSampler, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 1082970284490595, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-edit1.1-单图编辑_2029538924632219649.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-edit1.1-单图编辑_2029538924632219649.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `EmptyLatentImage` ★核心
- `VAELoader`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `1082970284490595`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`EmptyLatentImage`、`VAELoader`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`TextEncodeQwenImageEditPlus`、`LoraLoaderModelOnly`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
