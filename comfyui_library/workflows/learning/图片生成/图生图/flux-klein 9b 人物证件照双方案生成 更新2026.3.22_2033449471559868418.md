---
key: 图片生成/图生图/flux-klein 9b 人物证件照双方案生成 更新2026.3.22_2033449471559868418.json
name: flux-klein 9b 人物证件照双方案生成 更新2026.3.22_2033449471559868418
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux-klein 9b 人物证件照双方案生成 更新2026.3.22_2033449471559868418.json
hash: dda1018fa0660812
coverage: 0.793103
learned_at: 2026-10-23 11:35:41
nodes: [ReferenceLatent, ReferenceLatent, VAEEncode, ReferenceLatent, ReferenceLatent, KSampler, LoraLoaderModelOnly, VAELoader, CLIPLoader, VAELoader, VAEEncode, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, PrimitiveNode, Note, VAEDecode, easy cleanGpuUsed, ConditioningZeroOut, ImageScaleToTotalPixels, VAEEncode, Int, Fast Groups Bypasser (rgthree), ConditioningZeroOut, easy cleanGpuUsed, VAEDecode, CLIPTextEncode, Int, SaveImage, SaveImage, Image Comparer (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), EmptyFlux2LatentImage, KSampler, UNETLoader, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, UNETLoader, MuyeTextEditOutput, LoadImage, SaveImage, easy imageInsetCrop, CLIPLoader, LoadImage, LoadImage, Note, Note, MarkdownNote, MarkdownNote, MarkdownNote, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 433482042046057, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/flux-klein 9b 人物证件照双方案生成 更新2026.3.22_2033449471559868418.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux-klein 9b 人物证件照双方案生成 更新2026.3.22_2033449471559868418.json`

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
- `Note`
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
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `MuyeTextEditOutput`
- `LoadImage`
- `SaveImage`
- `easy imageInsetCrop`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `Note`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `433482042046057`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **79%**（46/58）

**有卡**：`ReferenceLatent`、`VAEEncode`、`KSampler`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`VAEDecode`、`easy cleanGpuUsed`、`ConditioningZeroOut`、`ImageScaleToTotalPixels`、`Int`、`SaveImage`、`LoadImage`、`EmptyFlux2LatentImage`、`UNETLoader`、`MuyeTextEditOutput`、`easy imageInsetCrop`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
