---
key: 图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2112774389644222465.json
name: 【Qwen Image 2.1】图像生成大合集_2112774389644222465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2112774389644222465.json
hash: 72d1a179daa29fcc
coverage: 0.71875
learned_at: 2026-10-23 11:48:50
nodes: [LayerUtility: ImageReelComposit, VAEDecode, easy setNode, VAEDecode, Image Comparer (rgthree), PreviewImage, LayerUtility: ImageReel, EmptyLatentImage, TextEncodeQwenImage21, ComfySwitchNode, PreviewImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy setNode, VAEDecode, SaveImage, SaveImage, easy setNode, Seed (rgthree), KSampler, ResolutionSelector, UNETLoader, QwenImage21Cache, VAELoader, Anything Everywhere3, SetNode, SetNode, GetNode, LoadImage, KSampler, TextGenerateLTX2Prompt, EmptyLatentImage, ShowText|pysssss, GetNode, CR Prompt Text, ResolutionSelector, BatchImagesNode, Image Comparer (rgthree), Note, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, GetNode, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), PreviewAny, TextGenerateLTX2Prompt, LoadImage, KSampler, CR Prompt Text, CLIPLoader, CLIPLoader, CLIPLoader, Fast Groups Bypasser (rgthree), TextEncodeQwenImage21, easy showAnything, TextGenerateLTX2Prompt, SaveImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 619497571996618, "steps": 40, "width": 1024}
---

# 图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2112774389644222465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【Qwen Image 2.1】图像生成大合集_2112774389644222465.json`

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
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `easy setNode`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `easy setNode`
- `Seed (rgthree)`
- `KSampler` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Anything Everywhere3`
- `SetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `EmptyLatentImage` ★核心
- `ShowText|pysssss`
- `GetNode`
- `CR Prompt Text`
- `ResolutionSelector`
- `BatchImagesNode`
- `Image Comparer (rgthree)`
- `Note`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PreviewAny`
- `TextGenerateLTX2Prompt`
- `LoadImage`
- `KSampler` ★核心
- `CR Prompt Text`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `TextGenerateLTX2Prompt`
- `SaveImage`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `619497571996618`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（46/64）

**有卡**：`LayerUtility: ImageReelComposit`、`VAEDecode`、`easy setNode`、`LayerUtility: ImageReel`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`SaveImage`、`Seed (rgthree)`、`KSampler`、`ResolutionSelector`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`LoadImage`、`TextGenerateLTX2Prompt`、`CR Prompt Text`、`BatchImagesNode`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
