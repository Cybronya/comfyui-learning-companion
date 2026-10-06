---
key: 图片生成/图生图/换脸+Face+Swap++Qwen-Image-2.1模特换头+换脸+klein_2107279318769561602.json
name: 换脸+Face+Swap++Qwen-Image-2.1模特换头+换脸+klein_2107279318769561602
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/换脸+Face+Swap++Qwen-Image-2.1模特换头+换脸+klein_2107279318769561602.json
hash: 7ac8ecbf2daea792
coverage: 0.853659
learned_at: 2026-10-06 22:33:30
nodes: [ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextEncodeQwenImage21, UNETLoader, BatchImagesNode, CLIPLoader, CLIPLoader, VAELoader, EmptyLatentImage, SaveImage, CLIPTextEncode, ReferenceLatent, ReferenceLatent, CLIPLoader, VAELoader, VAEEncode, KSampler, VAEDecode, EmptyFlux2LatentImage, UNETLoader, ReferenceLatent, ReferenceLatent, ImageResizeKJv2, ImageResizeKJv2, VAEEncode, LoraLoaderModelOnly, Note, LoadImage, CLIPTextEncode, SaveImage, Image Comparer (rgthree), LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), TextGenerateLTX2Prompt, JjkText, ResolutionSelector, LoadImage, LoadImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 412808031081800, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/换脸+Face+Swap++Qwen-Image-2.1模特换头+换脸+klein_2107279318769561602.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/换脸+Face+Swap++Qwen-Image-2.1模特换头+换脸+klein_2107279318769561602.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `SaveImage`
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
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `TextGenerateLTX2Prompt`
- `JjkText`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `412808031081800`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`UNETLoader`、`BatchImagesNode`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`SaveImage`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`EmptyFlux2LatentImage`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`LoadImage`、`TextGenerateLTX2Prompt`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
