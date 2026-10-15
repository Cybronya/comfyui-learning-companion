---
key: 图片生成/文生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json
name: 人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json
hash: 5eb70399870cc15b
coverage: 0.864865
learned_at: 2026-10-10 20:59:35
nodes: [ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ResolutionSelector, JjkText, LoadImage, CLIPTextEncode, ReferenceLatent, ReferenceLatent, CLIPLoader, VAELoader, VAEEncode, KSampler, VAEDecode, EmptyFlux2LatentImage, UNETLoader, ReferenceLatent, ReferenceLatent, ImageResizeKJv2, ImageResizeKJv2, VAEEncode, LoraLoaderModelOnly, LoadImage, CLIPTextEncode, SaveImage, Image Comparer (rgthree), LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 229768560102089, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json`

## 结构

**节点**（37 个）：
- `ComfySwitchNode`
- `VAEDecode`
- `KSampler`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `ResolutionSelector`
- `JjkText`
- `LoadImage`
- `CLIPTextEncode`
- `ReferenceLatent`
- `ReferenceLatent`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode`
- `KSampler`
- `VAEDecode`
- `EmptyFlux2LatentImage`
- `UNETLoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VAEEncode`
- `LoraLoaderModelOnly`
- `LoadImage`
- `CLIPTextEncode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `229768560102089`
- `steps` = `4`
- `width` = `1024`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`ComfySwitchNode`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`JjkText`、`LoadImage`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`EmptyFlux2LatentImage`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`SaveImage`、`Image Comparer (rgthree)`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
