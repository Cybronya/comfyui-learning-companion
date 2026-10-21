---
key: 图片生成/文生图/Qwen Image 2.1 全能工作流合集_2101841162679177218.json
name: Qwen Image 2.1 全能工作流合集_2101841162679177218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 全能工作流合集_2101841162679177218.json
hash: ef85fd069b8c0e04
coverage: 0.746479
learned_at: 2026-10-20 01:50:51
nodes: [LayerUtility: ImageReelComposit, VAEDecode, easy getNode, SaveImage, LayerUtility: ImageReel, EmptyLatentImage, TextEncodeQwenImage21, PreviewImage, Seed (rgthree), ComfySwitchNode, LayerUtility: ImageReel, EmptyLatentImage, LayerUtility: ImageReelComposit, ResolutionSelector, easy setNode, VAEDecode, ShowText|pysssss, easy getNode, easy getNode, easy setNode, QwenImage21Cache, CLIPLoader, VAELoader, Anything Everywhere3, CR Prompt Text, TextEncodeQwenImage21, VAEDecode, ResolutionSelector, Seed (rgthree), SaveImage, KSampler, EmptyLatentImage, Seed (rgthree), RHLLMChatNode, ResizeLongestToNode, PreviewImage, Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Label (rgthree), SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, Any Switch (rgthree), SeedVR2LoadDiTModel, ShowText|pysssss, RHLLMChatNode, easy setNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, CR Prompt Text, LoadImage, LoadImage, TextEncodeQwenImage21, ComfySwitchNode, ResolutionSelector, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, KSampler, SaveImage, Fast Groups Bypasser (rgthree), Label (rgthree), SaveImage, UNETLoader, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 283080278110399, "steps": 25, "width": 1024}
---

# 图片生成/文生图/Qwen Image 2.1 全能工作流合集_2101841162679177218.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 全能工作流合集_2101841162679177218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `easy getNode`
- `SaveImage`
- `LayerUtility: ImageReel`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `PreviewImage`
- `Seed (rgthree)`
- `ComfySwitchNode`
- `LayerUtility: ImageReel`
- `EmptyLatentImage` ★核心
- `LayerUtility: ImageReelComposit`
- `ResolutionSelector`
- `easy setNode`
- `VAEDecode` ★核心
- `ShowText|pysssss`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `CR Prompt Text`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `Seed (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `RHLLMChatNode`
- `ResizeLongestToNode`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `Any Switch (rgthree)`
- `SeedVR2LoadDiTModel`
- `ShowText|pysssss`
- `RHLLMChatNode`
- `easy setNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ResolutionSelector`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`
- `SaveImage`
- `UNETLoader` ★核心
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `283080278110399`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（53/71）

**有卡**：`LayerUtility: ImageReelComposit`、`VAEDecode`、`easy getNode`、`SaveImage`、`LayerUtility: ImageReel`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`ResolutionSelector`、`easy setNode`、`QwenImage21Cache`、`CLIPLoader`、`VAELoader`、`CR Prompt Text`、`KSampler`、`RHLLMChatNode`、`ResizeLongestToNode`、`Label (rgthree)`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`LoadImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
