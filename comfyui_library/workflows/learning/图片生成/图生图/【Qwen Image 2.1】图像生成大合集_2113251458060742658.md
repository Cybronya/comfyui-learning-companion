---
key: 图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2113251458060742658.json
name: 【Qwen Image 2.1】图像生成大合集_2113251458060742658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2113251458060742658.json
hash: 9dbd7d493020103c
coverage: 0.71875
learned_at: 2026-10-26 22:04:28
nodes: [LayerUtility: ImageReelComposit, VAEDecode, easy setNode, VAEDecode, Image Comparer (rgthree), PreviewImage, LayerUtility: ImageReel, TextEncodeQwenImage21, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, PreviewImage, LayerUtility: ImageReelComposit, easy setNode, VAEDecode, SaveImage, SaveImage, easy setNode, Seed (rgthree), KSampler, SaveImage, CR Prompt Text, ResolutionSelector, TextGenerateLTX2Prompt, easy showAnything, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, SetNode, SetNode, GetNode, KSampler, TextGenerateLTX2Prompt, EmptyLatentImage, ShowText|pysssss, GetNode, BatchImagesNode, Image Comparer (rgthree), TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, GetNode, EmptyLatentImage, ComfySwitchNode, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), PreviewAny, TextGenerateLTX2Prompt, KSampler, CLIPLoader, CLIPLoader, CLIPLoader, CR Prompt Text, Note, LayerUtility: ImageReel, ResolutionSelector, LoadImage, Fast Groups Bypasser (rgthree), ResolutionSelector, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 648621762169953, "steps": 40, "width": 1024}
---

# 图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2113251458060742658.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2113251458060742658.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `easy setNode`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `PreviewImage`
- `LayerUtility: ImageReelComposit`
- `easy setNode`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `easy setNode`
- `Seed (rgthree)`
- `KSampler` ★核心
- `SaveImage`
- `CR Prompt Text`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `SetNode`
- `SetNode`
- `GetNode`
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `EmptyLatentImage` ★核心
- `ShowText|pysssss`
- `GetNode`
- `BatchImagesNode`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PreviewAny`
- `TextGenerateLTX2Prompt`
- `KSampler` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `CR Prompt Text`
- `Note`
- `LayerUtility: ImageReel`
- `ResolutionSelector`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `648621762169953`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（46/64）

**有卡**：`LayerUtility: ImageReelComposit`、`VAEDecode`、`easy setNode`、`LayerUtility: ImageReel`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`SaveImage`、`Seed (rgthree)`、`KSampler`、`CR Prompt Text`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`BatchImagesNode`、`LoadImage`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
