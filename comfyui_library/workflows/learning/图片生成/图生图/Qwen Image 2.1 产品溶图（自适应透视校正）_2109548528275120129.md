---
key: 图片生成/图生图/Qwen Image 2.1 产品溶图（自适应透视校正）_2109548528275120129.json
name: Qwen Image 2.1 产品溶图（自适应透视校正）_2109548528275120129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 产品溶图（自适应透视校正）_2109548528275120129.json
hash: 247d98c97dcd1ab3
coverage: 0.7
learned_at: 2026-10-23 11:12:41
nodes: [ComfySwitchNode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy setNode, VAEDecode, TextGenerateLTX2Prompt, TextEncodeQwenImage21, EmptyLatentImage, ComfySwitchNode, SetNode, QwenImage21Cache, CLIPLoader, CLIPLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, PreviewImage, Image Comparer (rgthree), VAEDecode, easy setNode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, PreviewImage, Image Comparer (rgthree), SaveImage, PreviewAny, ResolutionSelector, GetNode, TextGenerateLTX2Prompt, Anything Everywhere3, SetNode, Note, Fast Groups Bypasser (rgthree), ResolutionSelector, EmptyLatentImage, TextEncodeQwenImage21, LoadImage, CR Prompt Text, UNETLoader, ShowText|pysssss, KSampler, LoadImage, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, GetNode, BatchImagesNode, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 164816017827009, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1 产品溶图（自适应透视校正）_2109548528275120129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 产品溶图（自适应透视校正）_2109548528275120129.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `ComfySwitchNode`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `easy setNode`
- `VAEDecode` ★核心
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `SetNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `easy setNode`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewAny`
- `ResolutionSelector`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `Anything Everywhere3`
- `SetNode`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `ShowText|pysssss`
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `GetNode`
- `BatchImagesNode`
- `CR Prompt Text`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `164816017827009`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（35/50）

**有卡**：`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy setNode`、`VAEDecode`、`TextGenerateLTX2Prompt`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`SaveImage`、`ResolutionSelector`、`LoadImage`、`CR Prompt Text`、`UNETLoader`、`KSampler`、`BatchImagesNode`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
