---
key: 图片生成/图生图/史上最强换脸工作流 黑兽Klein 9B BFS换脸V1 林耀3.26_2037080557837881346.json
name: 史上最强换脸工作流 黑兽Klein 9B BFS换脸V1 林耀3.26_2037080557837881346
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/史上最强换脸工作流 黑兽Klein 9B BFS换脸V1 林耀3.26_2037080557837881346.json
hash: 4167e985078cd12a
coverage: 1
learned_at: 2026-10-23 12:36:17
nodes: [ReferenceLatent, ReferenceLatent, VAELoader, KSampler, EmptyFlux2LatentImage, GetImageSize, CLIPLoader, UNETLoader, LayerUtility: PurgeVRAM V2, VAEDecode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEEncode, VAEEncode, ReferenceLatent, ReferenceLatent, ConditioningZeroOut, SaveImage, easy imageConcat, ImageConcatMulti, SaveImage, CR Prompt Text, CLIPTextEncode, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 43, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/史上最强换脸工作流 黑兽Klein 9B BFS换脸V1 林耀3.26_2037080557837881346.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/史上最强换脸工作流 黑兽Klein 9B BFS换脸V1 林耀3.26_2037080557837881346.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `KSampler` ★核心
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `SaveImage`
- `easy imageConcat`
- `ImageConcatMulti`
- `SaveImage`
- `CR Prompt Text`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `43`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（25/25）

**有卡**：`ReferenceLatent`、`VAELoader`、`KSampler`、`EmptyFlux2LatentImage`、`GetImageSize`、`CLIPLoader`、`UNETLoader`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`ImageScaleToTotalPixels`、`VAEEncode`、`ConditioningZeroOut`、`SaveImage`、`easy imageConcat`、`ImageConcatMulti`、`CR Prompt Text`、`CLIPTextEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
