---
key: 图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101831592514772993.json
name: 【Qwen Image 2.1】全功能集合工作流_2101831592514772993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101831592514772993.json
hash: 9c049496c66933f1
coverage: 0.75
learned_at: 2026-10-20 01:52:05
nodes: [LayerUtility: ImageReelComposit, VAEDecode, easy setNode, easy getNode, Image Comparer (rgthree), SeedVR2LoadVAEModel, VAEDecode, SeedVR2LoadDiTModel, Seed (rgthree), Image Comparer (rgthree), Fast Groups Bypasser (rgthree), Any Switch (rgthree), SaveImage, SeedVR2VideoUpscaler, LoraLoaderModelOnly, PreviewImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LayerUtility: ImageReel, TextEncodeQwenImage21, EmptyLatentImage, TextEncodeQwenImage21, KSampler, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, Image Comparer (rgthree), PreviewImage, KSampler, Seed (rgthree), ComfySwitchNode, LoadImage, LayerUtility: ImageReel, EmptyLatentImage, LayerUtility: ImageReelComposit, ResolutionSelector, easy setNode, VAEDecode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Label (rgthree), Label (rgthree), ShowText|pysssss, ShowText|pysssss, SaveImage, SaveImage, LoadImage, KSampler, ResolutionSelector, UNETLoader, VAELoader, easy getNode, easy getNode, easy setNode, Anything Everywhere3, QwenImage21Cache, CLIPLoader, ResizeLongestToNode, RHLLMChatNode, Seed (rgthree), Fast Groups Bypasser (rgthree), CR Prompt Text, TextEncodeQwenImage21, SaveImage, CR Prompt Text, RHLLMChatNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 240737692808322, "steps": 25, "width": 1024}
---

# 图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101831592514772993.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【Qwen Image 2.1】全功能集合工作流_2101831592514772993.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（72 个）：
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `easy setNode`
- `easy getNode`
- `Image Comparer (rgthree)`
- `SeedVR2LoadVAEModel`
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `Seed (rgthree)`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageReel`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `KSampler` ★核心
- `Seed (rgthree)`
- `ComfySwitchNode`
- `LoadImage`
- `LayerUtility: ImageReel`
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageReelComposit`
- `ResolutionSelector`
- `easy setNode`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `KSampler` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `VAELoader`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `Anything Everywhere3`
- `QwenImage21Cache`
- `CLIPLoader`
- `ResizeLongestToNode`
- `RHLLMChatNode`
- `Seed (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `SaveImage`
- `CR Prompt Text`
- `RHLLMChatNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `240737692808322`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（54/72）

**有卡**：`LayerUtility: ImageReelComposit`、`VAEDecode`、`easy setNode`、`easy getNode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`Seed (rgthree)`、`SaveImage`、`SeedVR2VideoUpscaler`、`LoraLoaderModelOnly`、`LayerUtility: ImageReel`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`ResolutionSelector`、`LoadImage`、`Label (rgthree)`、`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`CLIPLoader`、`ResizeLongestToNode`、`RHLLMChatNode`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
