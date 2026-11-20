---
key: 图片生成/图生图/AI Video Studio PR插件 Qwen2.1图像生成_2115403115095748609.json
name: AI Video Studio PR插件 Qwen2.1图像生成_2115403115095748609
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AI Video Studio PR插件 Qwen2.1图像生成_2115403115095748609.json
hash: 7c35ccf612a687ce
coverage: 0.69697
learned_at: 2026-10-30 17:49:20
nodes: [LayerUtility: ImageReelComposit, VAEDecode, easy setNode, VAEDecode, Image Comparer (rgthree), PreviewImage, LayerUtility: ImageReel, TextEncodeQwenImage21, EmptyLatentImage, ComfySwitchNode, VAEDecode, easy setNode, Seed (rgthree), KSampler, CR Prompt Text, ResolutionSelector, TextGenerateLTX2Prompt, easy showAnything, VAELoader, SetNode, SetNode, GetNode, CR Prompt Text, Image Comparer (rgthree), Note, TextEncodeQwenImage21, LoadImage, LoadImage, EmptyLatentImage, ComfySwitchNode, Fast Groups Bypasser (rgthree), LoadImage, CLIPLoader, CLIPLoader, CLIPLoader, UNETLoader, QwenImage21Cache, Anything Everywhere3, KSampler, GetNode, LoadImage, ResolutionSelector, TextGenerateLTX2Prompt, TextEncodeQwenImage21, ShowText|pysssss, EmptyLatentImage, Fast Groups Bypasser (rgthree), LoadImage, GetNode, ResolutionSelector, BatchImagesNode, PreviewAny, SaveImage, SaveImage, SaveImage, LoadImage, CR Prompt Text, LoadImage, KSampler, LayerUtility: ImageReel, easy setNode, PreviewImage, LayerUtility: ImageReelComposit, TextGenerateLTX2Prompt, ComfySwitchNode, ComfySwitchNode]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 294529428471217, "steps": 40, "width": 1024}
---

# 图片生成/图生图/AI Video Studio PR插件 Qwen2.1图像生成_2115403115095748609.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AI Video Studio PR插件 Qwen2.1图像生成_2115403115095748609.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `LayerUtility: ImageReelComposit`
- `VAEDecode` ★核心
- `easy setNode`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `LayerUtility: ImageReel`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `easy setNode`
- `Seed (rgthree)`
- `KSampler` ★核心
- `CR Prompt Text`
- `ResolutionSelector`
- `TextGenerateLTX2Prompt`
- `easy showAnything`
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
- `Fast Groups Bypasser (rgthree)`
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
- `ComfySwitchNode`
- `ComfySwitchNode`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `294529428471217`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **70%**（46/66）

**有卡**：`LayerUtility: ImageReelComposit`、`VAEDecode`、`easy setNode`、`LayerUtility: ImageReel`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`Seed (rgthree)`、`KSampler`、`CR Prompt Text`、`ResolutionSelector`、`TextGenerateLTX2Prompt`、`VAELoader`、`LoadImage`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`BatchImagesNode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
