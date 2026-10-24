---
key: 图片生成/图生图/试衣换装flux-klein-9b-virtual-tryon_2026568259612446721.json
name: 试衣换装flux-klein-9b-virtual-tryon_2026568259612446721
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/试衣换装flux-klein-9b-virtual-tryon_2026568259612446721.json
hash: 412a8afa21c9ae57
coverage: 0.9
learned_at: 2026-10-23 13:27:48
nodes: [CLIPTextEncode, ReferenceLatent, VAEEncode, VAEEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, CLIPLoader, KSampler, CLIPTextEncode, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent, VAEEncode, CLIPLoader, KSampler, EmptyFlux2LatentImage, CLIPTextEncode, CLIPTextEncode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, Note, VAEDecode, ImageResizeKJv2, EmptyFlux2LatentImage, VAEEncode, Image Comparer (rgthree), SaveImage, Note, UNETLoader, LoraLoaderModelOnly, LoadImage, LoadImage, VAELoader, VAELoader, UNETLoader, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), VAEDecode, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 600450557956235, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/试衣换装flux-klein-9b-virtual-tryon_2026568259612446721.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/试衣换装flux-klein-9b-virtual-tryon_2026568259612446721.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CLIPLoader`
- `KSampler` ★核心
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Note`
- `VAEDecode` ★核心
- `ImageResizeKJv2`
- `EmptyFlux2LatentImage`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `Note`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `600450557956235`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（45/50）

**有卡**：`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`CLIPLoader`、`KSampler`、`EmptyFlux2LatentImage`、`ImageResizeKJv2`、`VAEDecode`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
