---
key: 图片生成/文生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json
name: 人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json
hash: 5eb70399870cc15b
coverage: 0.621622
learned_at: 2026-10-06 21:51:24
nodes: [ComfySwitchNode, VAEDecode, KSampler, QwenImage21Cache, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ResolutionSelector, JjkText, LoadImage, CLIPTextEncode, ReferenceLatent, ReferenceLatent, CLIPLoader, VAELoader, VAEEncode, KSampler, VAEDecode, EmptyFlux2LatentImage, UNETLoader, ReferenceLatent, ReferenceLatent, ImageResizeKJv2, ImageResizeKJv2, VAEEncode, LoraLoaderModelOnly, LoadImage, CLIPTextEncode, SaveImage, Image Comparer (rgthree), LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, SaveImage]
patterns: [text_to_image, image_to_image]
missing: [Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), EmptyFlux2LatentImage, ImageResizeKJv2, ImageResizeKJv2, ReferenceLatent, ReferenceLatent, ReferenceLatent, ReferenceLatent]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 229768560102089, "steps": 4, "width": 1024}
discoveries: [次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `EmptyFlux2LatentImage` 仅有 VAE/Checkpoint 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `ReferenceLatent` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `ReferenceLatent` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `ReferenceLatent` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `ReferenceLatent` 仅有 VAE 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/人像换脸丨Qwen-Image2.1＋Flux2-Klein丨换头与换脸_2100134870709260289.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（37 个）：
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `JjkText`
- `LoadImage`
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
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `229768560102089`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **62%**（23/37）

**有卡**：`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`LoadImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`SaveImage`

**缺卡**（9）：`Fast Groups Bypasser (rgthree)`、`Fast Groups Bypasser (rgthree)`、`EmptyFlux2LatentImage`、`ImageResizeKJv2`、`ImageResizeKJv2`、`ReferenceLatent`、`ReferenceLatent`、`ReferenceLatent`、`ReferenceLatent`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `EmptyFlux2LatentImage` 仅有 VAE/Checkpoint 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ImageResizeKJv2` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `ReferenceLatent` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `ReferenceLatent` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `ReferenceLatent` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `ReferenceLatent` 仅有 VAE 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
