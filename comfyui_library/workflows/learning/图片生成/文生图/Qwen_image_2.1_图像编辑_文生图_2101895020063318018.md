---
key: 图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json
name: Qwen_image_2.1_图像编辑_文生图_2101895020063318018
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json
hash: 0f9cd03045845739
coverage: 0.609375
learned_at: 2026-10-10 20:59:09
nodes: [EmptyLatentImage, PrimitiveBoolean, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, BatchImagesNode, ImageScaleToTotalPixels, EmptyLatentImage, ResolutionSelector, ResolutionSelector, GetNode, VAEDecode, GetNode, GetNode, ComfySwitchNode, GetNode, Seed (rgthree), GetNode, GetNode, GetNode, SetNode, SetNode, VAELoader, QwenImage21Cache, SetNode, SetNode, PrimitiveStringMultiline, CLIPLoader, SetNode, CLIPLoader, CLIPLoader, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, PrimitiveStringMultiline, VAEDecode, Image Comparer (rgthree), SaveImage, KSampler, TextEncodeQwenImage21, TextEncodeQwenImage21, SaveImage, Seed (rgthree), KSampler, UNETLoader, easy showAnything, easy showAnything, PrimitiveStringMultiline, TextGenerateLTX2Prompt, TextGenerateLTX2Prompt, GetNode, PrimitiveStringMultiline]
patterns: []
missing: [Seed (rgthree), Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 577567495159582, "steps": 40, "width": 1024}
discoveries: [次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_image_2.1_图像编辑_文生图_2101895020063318018.json`

## 结构

**节点**（64 个）：
- `EmptyLatentImage`
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
- `EmptyLatentImage`
- `ResolutionSelector`
- `ResolutionSelector`
- `GetNode`
- `VAEDecode`
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
- `LoraLoaderModelOnly`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VAEDecode`
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `SaveImage`
- `Seed (rgthree)`
- `KSampler`
- `UNETLoader`
- `easy showAnything`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`
- `TextGenerateLTX2Prompt`
- `GetNode`
- `PrimitiveStringMultiline`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `577567495159582`
- `steps` = `40`
- `width` = `1024`

## 知识

覆盖率 **61%**（39/64）

**有卡**：`EmptyLatentImage`、`PrimitiveBoolean`、`LoadImage`、`ImageScaleToTotalPixels`、`BatchImagesNode`、`ResolutionSelector`、`GetNode`、`VAEDecode`、`ComfySwitchNode`、`Seed (rgthree)`、`SetNode`、`VAELoader`、`QwenImage21Cache`、`PrimitiveStringMultiline`、`CLIPLoader`

**缺卡**（2）：`Seed (rgthree)`、`Seed (rgthree)`

## 学习发现

- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
