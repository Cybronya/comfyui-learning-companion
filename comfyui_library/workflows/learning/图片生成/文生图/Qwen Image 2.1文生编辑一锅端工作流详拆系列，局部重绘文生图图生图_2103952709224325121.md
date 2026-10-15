---
key: 图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列，局部重绘文生图图生图_2103952709224325121.json
name: Qwen Image 2.1文生编辑一锅端工作流详拆系列，局部重绘文生图图生图_2103952709224325121
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列，局部重绘文生图图生图_2103952709224325121.json
hash: a2204de4953b1d8d
coverage: 0.762295
learned_at: 2026-10-15 22:27:02
nodes: [Seed (rgthree), ShowText|pysssss, ResolutionSelector, EmptyLatentImage, SaveImage, VAEDecode, easy setNode, TextEncodeQwenImage21, easy getNode, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveBoolean, Seed (rgthree), LayerUtility: ImageReel, LayerUtility: ImageReelComposit, ShowText|pysssss, SaveImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), ResizeLongestToNode, Fast Groups Bypasser (rgthree), LoadImage, RHLLMChatNode, ResolutionSelector, EmptyLatentImage, Fast Groups Bypasser (rgthree), easy getNode, easy getNode, SaveImage, Fast Bypasser (rgthree), Any Switch (rgthree), CLIPLoader, VAELoader, KSampler, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), KSampler, VAEDecode, TextEncodeQwenImage21, VAEDecode, TextEncodeQwenImage21, LayerUtility: ImageReelComposit, QwenImage21Cache, Fast Groups Bypasser (rgthree), PreviewImage, LayerUtility: ImageReel, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), EmptyLatentImage, ComfySwitchNode, Seed (rgthree), ComfySwitchNode, PreviewImage, easy setNode, PreviewImage, Image Comparer (rgthree), PrimitiveBoolean, Image Comparer (rgthree), ResolutionSelector, CR Prompt Text, KSampler, easy setNode, VOSR2ModelLoader, easy float, easy setNode, ImageScaleBy, VOSR2Upscale, SaveImage, PreviewImage, easy getNode, easy getNode, easy getNode, Any Switch (rgthree), easy int, SplitImageWithAlpha, RHLLMChatNode, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), LoraLoaderModelOnly, UNETLoader, CR Prompt Text, Anything Everywhere3, Fast Groups Bypasser (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列，局部重绘文生图图生图_2103952709224325121.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生编辑一锅端工作流详拆系列，局部重绘文生图图生图_2103952709224325121.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（122 个）：
- `Seed (rgthree)`
- `ShowText|pysssss`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `easy setNode`
- `TextEncodeQwenImage21`
- `easy getNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveBoolean`
- `Seed (rgthree)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `ShowText|pysssss`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ResizeLongestToNode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `RHLLMChatNode`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `easy getNode`
- `easy getNode`
- `SaveImage`
- `Fast Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `LayerUtility: ImageReelComposit`
- `QwenImage21Cache`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `Seed (rgthree)`
- `ComfySwitchNode`
- `PreviewImage`
- `easy setNode`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `PrimitiveBoolean`
- `Image Comparer (rgthree)`
- `ResolutionSelector`
- `CR Prompt Text`
- `KSampler` ★核心
- `easy setNode`
- `VOSR2ModelLoader`
- `easy float`
- `easy setNode`
- `ImageScaleBy`
- `VOSR2Upscale`
- `SaveImage`
- `PreviewImage`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `Any Switch (rgthree)`
- `easy int`
- `SplitImageWithAlpha`
- `RHLLMChatNode`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CR Prompt Text`
- `Anything Everywhere3`
- `Fast Groups Bypasser (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `CR Prompt Text`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **76%**（93/122）

**有卡**：`Seed (rgthree)`、`ResolutionSelector`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`easy setNode`、`TextEncodeQwenImage21`、`easy getNode`、`LoadImage`、`PrimitiveBoolean`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`ResizeLongestToNode`、`RHLLMChatNode`、`Fast Bypasser (rgthree)`、`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`SeedVR2VideoUpscaler`、`CR Prompt Text`、`VOSR2ModelLoader`、`easy float`、`ImageScaleBy`、`VOSR2Upscale`、`easy int`、`SplitImageWithAlpha`、`LoraLoaderModelOnly`、`UNETLoader`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
