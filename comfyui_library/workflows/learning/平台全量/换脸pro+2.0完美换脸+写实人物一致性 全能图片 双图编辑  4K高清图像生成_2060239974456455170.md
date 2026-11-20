---
key: 平台全量/换脸pro+2.0完美换脸+写实人物一致性 全能图片 双图编辑  4K高清图像生成_2060239974456455170.json
name: 换脸pro+2.0完美换脸+写实人物一致性 全能图片 双图编辑  4K高清图像生成_2060239974456455170
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/换脸pro+2.0完美换脸+写实人物一致性 全能图片 双图编辑  4K高清图像生成_2060239974456455170.json
hash: b762443645d6e519
coverage: 0.90625
learned_at: 2026-11-14 02:08:16
nodes: [SaveImage, ImageConcatMulti, RH_Nano_Banana2_Image2Image, CR Text, ImageConcatMulti, SaveImage, LoadImage, LoadImage, CR Text, CLIPTextEncode, ReferenceLatent, ReferenceLatent, CLIPLoader, VAELoader, VAEEncode, KSampler, VAEDecode, EmptyFlux2LatentImage, UNETLoader, ReferenceLatent, ReferenceLatent, ImageResizeKJv2, ImageResizeKJv2, VAEEncode, LoadImage, LoraLoaderModelOnly, Note, LoadImage, CLIPTextEncode, SaveImage, Image Comparer (rgthree), Fast Groups Bypasser (rgthree)]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 649272925413366, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/换脸pro+2.0完美换脸+写实人物一致性 全能图片 双图编辑  4K高清图像生成_2060239974456455170.json

> 来源文件 `comfyui_library/workflows/平台全量/换脸pro+2.0完美换脸+写实人物一致性 全能图片 双图编辑  4K高清图像生成_2060239974456455170.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `SaveImage`
- `ImageConcatMulti`
- `RH_Nano_Banana2_Image2Image`
- `CR Text`
- `ImageConcatMulti`
- `SaveImage`
- `LoadImage`
- `LoadImage`
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
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `649272925413366`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（29/32）

**有卡**：`SaveImage`、`ImageConcatMulti`、`RH_Nano_Banana2_Image2Image`、`CR Text`、`LoadImage`、`CLIPTextEncode`、`ReferenceLatent`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`KSampler`、`VAEDecode`、`EmptyFlux2LatentImage`、`UNETLoader`、`ImageResizeKJv2`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
