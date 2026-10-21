---
key: 图片生成/图生图/Character Head and Face Swaps人物换头换脸_2100035107896774657.json
name: Character Head and Face Swaps人物换头换脸_2100035107896774657
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Character Head and Face Swaps人物换头换脸_2100035107896774657.json
hash: 723f24a047bf90ee
coverage: 0.860465
learned_at: 2026-10-21 00:38:52
nodes: [LoadImage, LoadImage, SaveImage, RH_SeedreamV5ProImageToImage, Fast Groups Bypasser (rgthree), SaveImage, ImageConcatMulti, RH_Nano_Banana2_Image2Image, CR Text, ImageConcatMulti, SaveImage, CR Text, CLIPTextEncode, ReferenceLatent, ReferenceLatent, CLIPLoader, VAELoader, VAEEncode, KSampler, VAEDecode, EmptyFlux2LatentImage, UNETLoader, ReferenceLatent, ReferenceLatent, ImageResizeKJv2, ImageResizeKJv2, VAEEncode, LoraLoaderModelOnly, Note, CLIPTextEncode, SaveImage, Image Comparer (rgthree), CR Prompt Text, SaveImage, ImageConcatMulti, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1100494507112574, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Character Head and Face Swaps人物换头换脸_2100035107896774657.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Character Head and Face Swaps人物换头换脸_2100035107896774657.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `RH_SeedreamV5ProImageToImage`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `ImageConcatMulti`
- `RH_Nano_Banana2_Image2Image`
- `CR Text`
- `ImageConcatMulti`
- `SaveImage`
- `CR Text`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `UNETLoader` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `CR Prompt Text`
- `SaveImage`
- `ImageConcatMulti`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1100494507112574`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（37/43）

**有卡**：`LoadImage`、`SaveImage`、`RH_SeedreamV5ProImageToImage`、`ImageConcatMulti`、`RH_Nano_Banana2_Image2Image`、`CR Text`、`CLIPTextEncode`、`ReferenceLatent`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`KSampler`、`VAEDecode`、`EmptyFlux2LatentImage`、`UNETLoader`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
