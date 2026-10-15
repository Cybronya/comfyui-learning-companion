---
key: 图片生成/图生图/Qwen Image 2.1全功能集合文生图图生图处理工作流_2102094333674614786.json
name: Qwen Image 2.1全功能集合文生图图生图处理工作流_2102094333674614786
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1全功能集合文生图图生图处理工作流_2102094333674614786.json
hash: a40ffa74271aaf79
coverage: 0.777778
learned_at: 2026-10-15 22:25:12
nodes: [LayerUtility: ImageReelComposit, VAEDecode, easy setNode, easy getNode, Image Comparer (rgthree), SeedVR2LoadVAEModel, VAEDecode, SeedVR2LoadDiTModel, Seed (rgthree), Image Comparer (rgthree), Fast Groups Bypasser (rgthree), Any Switch (rgthree), SaveImage, SeedVR2VideoUpscaler, LoraLoaderModelOnly, PreviewImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LayerUtility: ImageReel, TextEncodeQwenImage21, EmptyLatentImage, TextEncodeQwenImage21, KSampler, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, Image Comparer (rgthree), PreviewImage, KSampler, Seed (rgthree), ComfySwitchNode, LoadImage, LayerUtility: ImageReel, EmptyLatentImage, LayerUtility: ImageReelComposit, ResolutionSelector, easy setNode, VAEDecode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ShowText|pysssss, ShowText|pysssss, SaveImage, SaveImage, CR Prompt Text, LoadImage, KSampler, ResolutionSelector, UNETLoader, VAELoader, RHLLMChatNode, easy getNode, easy getNode, easy setNode, Anything Everywhere3, QwenImage21Cache, CLIPLoader, ResizeLongestToNode, RHLLMChatNode, Seed (rgthree), Fast Groups Bypasser (rgthree), CR Prompt Text, TextEncodeQwenImage21, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1全功能集合文生图图生图处理工作流_2102094333674614786.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1全功能集合文生图图生图处理工作流_2102094333674614786.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
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
- `ShowText|pysssss`
- `ShowText|pysssss`
- `SaveImage`
- `SaveImage`
- `CR Prompt Text`
- `LoadImage`
- `KSampler` ★核心
- `ResolutionSelector`
- `UNETLoader` ★核心
- `VAELoader`
- `RHLLMChatNode`
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

覆盖率 **78%**（77/99）

**有卡**：`LayerUtility: ImageReelComposit`、`VAEDecode`、`easy setNode`、`easy getNode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`Seed (rgthree)`、`SaveImage`、`SeedVR2VideoUpscaler`、`LoraLoaderModelOnly`、`LayerUtility: ImageReel`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`KSampler`、`ResolutionSelector`、`LoadImage`、`CR Prompt Text`、`UNETLoader`、`VAELoader`、`RHLLMChatNode`、`QwenImage21Cache`、`CLIPLoader`、`ResizeLongestToNode`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
