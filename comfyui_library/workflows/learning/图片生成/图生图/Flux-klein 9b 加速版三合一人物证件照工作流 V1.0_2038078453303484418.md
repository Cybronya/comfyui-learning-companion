---
key: 图片生成/图生图/Flux-klein 9b 加速版三合一人物证件照工作流 V1.0_2038078453303484418.json
name: Flux-klein 9b 加速版三合一人物证件照工作流 V1.0_2038078453303484418
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux-klein 9b 加速版三合一人物证件照工作流 V1.0_2038078453303484418.json
hash: 3dfdb4ab9a5cbf22
coverage: 0.793103
learned_at: 2026-10-23 10:58:32
nodes: [ReferenceLatent, ReferenceLatent, VAEEncode, ReferenceLatent, ReferenceLatent, KSampler, LoraLoaderModelOnly, VAELoader, CLIPLoader, VAELoader, VAEEncode, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, PrimitiveNode, VAEDecode, easy cleanGpuUsed, ConditioningZeroOut, ImageScaleToTotalPixels, VAEEncode, Int, Fast Groups Bypasser (rgthree), ConditioningZeroOut, easy cleanGpuUsed, VAEDecode, CLIPTextEncode, Int, SaveImage, SaveImage, Image Comparer (rgthree), EmptyFlux2LatentImage, KSampler, LoraLoaderModelOnly, LoadImage, UNETLoader, CLIPLoader, MarkdownNote, MarkdownNote, UNETLoader, LoadImage, LoadImage, Note, Fast Groups Bypasser (rgthree), Note, LoadImage, LoadImage, LoadImage, Note, easy imageInsetCrop, SaveImage, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, Fast Groups Bypasser (rgthree), MarkdownNote, MuyeTextEditOutput, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 806802412789593, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux-klein 9b 加速版三合一人物证件照工作流 V1.0_2038078453303484418.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux-klein 9b 加速版三合一人物证件照工作流 V1.0_2038078453303484418.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ConditioningZeroOut`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `Int`
- `Fast Groups Bypasser (rgthree)`
- `ConditioningZeroOut`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `easy imageInsetCrop`
- `SaveImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `MuyeTextEditOutput`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `806802412789593`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **79%**（46/58）

**有卡**：`ReferenceLatent`、`VAEEncode`、`KSampler`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`VAEDecode`、`easy cleanGpuUsed`、`ConditioningZeroOut`、`ImageScaleToTotalPixels`、`Int`、`SaveImage`、`EmptyFlux2LatentImage`、`LoadImage`、`UNETLoader`、`easy imageInsetCrop`、`MuyeTextEditOutput`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
