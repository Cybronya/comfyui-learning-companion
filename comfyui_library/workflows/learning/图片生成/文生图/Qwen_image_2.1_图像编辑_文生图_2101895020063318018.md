---
key: 图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json
name: Qwen_image_2.1_图像编辑_文生图_2101895020063318018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json
hash: 0f9cd03045845739
coverage: 0.609375
learned_at: 2026-10-07 02:29:27
nodes: [EmptyLatentImage, PrimitiveBoolean, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, BatchImagesNode, ImageScaleToTotalPixels, EmptyLatentImage, ResolutionSelector, ResolutionSelector, GetNode, VAEDecode, GetNode, GetNode, ComfySwitchNode, GetNode, Seed (rgthree), GetNode, GetNode, GetNode, SetNode, SetNode, VAELoader, QwenImage21Cache, SetNode, SetNode, PrimitiveStringMultiline, CLIPLoader, SetNode, CLIPLoader, CLIPLoader, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, PrimitiveStringMultiline, VAEDecode, Image Comparer (rgthree), SaveImage, KSampler, TextEncodeQwenImage21, TextEncodeQwenImage21, SaveImage, Seed (rgthree), KSampler, UNETLoader, easy showAnything, easy showAnything, PrimitiveStringMultiline, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, GetNode, PrimitiveStringMultiline]
patterns: []
missing: [Seed (rgthree), Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 577567495159582, "steps": 40, "width": 1024}
discoveries: [次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `EmptyLatentImage` ★核心
- `PrimitiveBoolean`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `ResolutionSelector`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `Seed (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `QwenImage21Cache`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `SetNode`
- `CLIPLoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `SaveImage`
- `Seed (rgthree)`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `easy showAnything`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `577567495159582`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **61%**（39/64）

**有卡**：`EmptyLatentImage`、`PrimitiveBoolean`、`LoadImage`、`ImageScaleToTotalPixels`、`BatchImagesNode`、`ResolutionSelector`、`VAEDecode`、`VAELoader`、`QwenImage21Cache`、`CLIPLoader`、`LoraLoaderModelOnly`、`SaveImage`、`KSampler`、`TextEncodeQwenImage21`、`UNETLoader`、`TextGenerateLTX2Prompt`

**缺卡**（2）：`Seed (rgthree)`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
