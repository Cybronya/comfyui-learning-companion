---
key: 平台全量/Qwen Image 2.1 人物换背景_2106931711295713281.json
name: Qwen Image 2.1 人物换背景_2106931711295713281
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image 2.1 人物换背景_2106931711295713281.json
hash: 18b3790a24b4d4a1
coverage: 0.6875
learned_at: 2026-11-14 00:49:54
nodes: [TextEncodeQwenImage21, ComfySwitchNode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, easy setNode, VAEDecode, TextGenerateLTX2Prompt, TextEncodeQwenImage21, GetNode, EmptyLatentImage, ComfySwitchNode, KSampler, LoadImage, ShowText|pysssss, EmptyLatentImage, SetNode, UNETLoader, QwenImage21Cache, CLIPLoader, CLIPLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, PreviewImage, Image Comparer (rgthree), KSampler, VAEDecode, easy setNode, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, PreviewImage, Image Comparer (rgthree), BatchImagesNode, SaveImage, PreviewAny, ResolutionSelector, CR Prompt Text, GetNode, TextGenerateLTX2Prompt, CR Prompt Text, Anything Everywhere3, SetNode, Note, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), ResolutionSelector]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1032049235759282, "steps": 40, "width": 1024}
---

# 平台全量/Qwen Image 2.1 人物换背景_2106931711295713281.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image 2.1 人物换背景_2106931711295713281.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `easy setNode`
- `VAEDecode` ★核心
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `GetNode`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `KSampler` ★核心
- `LoadImage`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `SetNode`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy setNode`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `BatchImagesNode`
- `SaveImage`
- `PreviewAny`
- `ResolutionSelector`
- `CR Prompt Text`
- `GetNode`
- `TextGenerateLTX2Prompt`
- `CR Prompt Text`
- `Anything Everywhere3`
- `SetNode`
- `Note`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1032049235759282`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **69%**（33/48）

**有卡**：`TextEncodeQwenImage21`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`easy setNode`、`VAEDecode`、`TextGenerateLTX2Prompt`、`EmptyLatentImage`、`KSampler`、`LoadImage`、`UNETLoader`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`SaveImage`、`BatchImagesNode`、`ResolutionSelector`、`CR Prompt Text`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
