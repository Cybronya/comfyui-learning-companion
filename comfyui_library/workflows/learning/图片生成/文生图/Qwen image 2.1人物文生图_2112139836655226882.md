---
key: 图片生成/文生图/Qwen image 2.1人物文生图_2112139836655226882.json
name: Qwen image 2.1人物文生图_2112139836655226882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1人物文生图_2112139836655226882.json
hash: f48d3e3158fe589c
coverage: 0.676471
learned_at: 2026-10-21 02:54:19
nodes: [LayerUtility: ImageReelComposit, VAEDecode, VAEDecode, Image Comparer (rgthree), PreviewImage, LayerUtility: ImageReel, EmptyLatentImage, ComfySwitchNode, VAEDecode, easy setNode, Seed (rgthree), KSampler, VAELoader, SetNode, SetNode, GetNode, CR Prompt Text, Image Comparer (rgthree), Note, TextEncodeQwenImage21, LoadImage, LoadImage, EmptyLatentImage, ComfySwitchNode, Fast Groups Bypasser (rgthree), LoadImage, CLIPLoader, CLIPLoader, CLIPLoader, UNETLoader, QwenImage21Cache, Anything Everywhere3, KSampler, GetNode, LoadImage, ResolutionSelector, TextGenerateLTX2Prompt, TextEncodeQwenImage21, ShowText|pysssss, EmptyLatentImage, LoadImage, GetNode, ResolutionSelector, BatchImagesNode, PreviewAny, SaveImage, SaveImage, SaveImage, LoadImage, CR Prompt Text, LoadImage, KSampler, LayerUtility: ImageReel, easy setNode, PreviewImage, LayerUtility: ImageReelComposit, TextGenerateLTX2Prompt, Fast Groups Bypasser (rgthree), ResolutionSelector, JjkText, JjkText, JjkText, TextEncodeQwenImage21, easy showAnything, CR Prompt Text, TextGenerateLTX2Prompt, easy setNode, JjkText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1123515860212464, "steps": 40, "width": 1024}
---

# 图片生成/文生图/Qwen image 2.1人物文生图_2112139836655226882.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1人物文生图_2112139836655226882.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `easy setNode`
- `Seed (rgthree)`
- `KSampler` ★核心
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `CR Prompt Text`
- `Image Comparer (rgthree)`
- `Note`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CLIPLoader`
- `CLIPLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `Anything Everywhere3`
- `KSampler` ★核心
- `GetNode`
- `LoadImage`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `TextEncodeQwenImage21`
- `ShowText|pysssss`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `GetNode`
- `ResolutionSelector`
- `BatchImagesNode`
- `PreviewAny`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`
- `KSampler` ★核心
- `LayerUtility: ImageReel`
- `easy setNode`
- `PreviewImage`
- `LayerUtility: ImageReelComposit`
- `TextGenerateLTX2Prompt`
- `Fast Groups Bypasser (rgthree)`
- `ResolutionSelector`
- `JjkText`
- `JjkText`
- `JjkText`
- `TextEncodeQwenImage21`
- `easy showAnything`
- `CR Prompt Text`
- `TextGenerateLTX2Prompt`
- `easy setNode`
- `JjkText`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1123515860212464`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **68%**（46/68）

**有卡**：`LayerUtility: ImageReelComposit`、`VAEDecode`、`LayerUtility: ImageReel`、`EmptyLatentImage`、`easy setNode`、`Seed (rgthree)`、`KSampler`、`VAELoader`、`CR Prompt Text`、`TextEncodeQwenImage21`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`BatchImagesNode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
