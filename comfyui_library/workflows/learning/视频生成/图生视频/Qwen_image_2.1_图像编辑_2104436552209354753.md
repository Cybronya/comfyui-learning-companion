---
key: 视频生成/图生视频/Qwen_image_2.1_图像编辑_2104436552209354753.json
name: Qwen_image_2.1_图像编辑_2104436552209354753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen_image_2.1_图像编辑_2104436552209354753.json
hash: e3e6dbd907a8f01c
coverage: 0.65625
learned_at: 2026-10-17 22:18:57
nodes: [EmptyLatentImage, PrimitiveBoolean, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, BatchImagesNode, ImageScaleToTotalPixels, EmptyLatentImage, ResolutionSelector, ResolutionSelector, GetNode, VAEDecode, SaveImage, GetNode, GetNode, ComfySwitchNode, GetNode, Seed (rgthree), GetNode, GetNode, GetNode, Seed (rgthree), easy showAnything, KSampler, KSampler, SetNode, SetNode, VAELoader, QwenImage21Cache, SetNode, SetNode, TextGenerateLTX2Prompt, PrimitiveStringMultiline, UNETLoader, CLIPLoader, SetNode, GetNode, easy showAnything, CLIPLoader, CLIPLoader, LoraLoaderModelOnly, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), TextGenerateLTX2Prompt, LoadImage, PrimitiveStringMultiline, TextEncodeQwenImage21, TextEncodeQwenImage21, VAEDecode, Image Comparer (rgthree), SaveImage, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1023151102027374, "steps": 50, "width": 1024}
---

# 视频生成/图生视频/Qwen_image_2.1_图像编辑_2104436552209354753.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen_image_2.1_图像编辑_2104436552209354753.json`

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
- `SaveImage`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `Seed (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `Seed (rgthree)`
- `easy showAnything`
- `KSampler` ★核心
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `VAELoader`
- `QwenImage21Cache`
- `SetNode`
- `SetNode`
- `TextGenerateLTX2Prompt`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `CLIPLoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1023151102027374`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **66%**（42/64）

**有卡**：`EmptyLatentImage`、`PrimitiveBoolean`、`LoadImage`、`ImageScaleToTotalPixels`、`BatchImagesNode`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`Seed (rgthree)`、`KSampler`、`VAELoader`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
