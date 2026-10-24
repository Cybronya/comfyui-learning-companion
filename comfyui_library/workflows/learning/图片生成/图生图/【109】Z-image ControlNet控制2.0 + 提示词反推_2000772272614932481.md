---
key: 图片生成/图生图/【109】Z-image ControlNet控制2.0 + 提示词反推_2000772272614932481.json
name: 【109】Z-image ControlNet控制2.0 + 提示词反推_2000772272614932481
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【109】Z-image ControlNet控制2.0 + 提示词反推_2000772272614932481.json
hash: 317f35a29632d84c
coverage: 0.406977
learned_at: 2026-10-23 11:48:05
nodes: [SetNode, SetNode, SetNode, UNETLoader, SetNode, CLIPLoader, VAELoader, SetNode, SetNode, GetNode, EmptyLatentImage, GetNode, LayerUtility: ImageReelComposit, easy int, easy int, Note, SetNode, GetNode, GetNode, SetNode, SetNode, Note, GetNode, Note, Text Concatenate, easy showAnything, Note, easy seed, easy imagePixelPerfect, easy showAnything, CR Prompt Text, Text Concatenate, CR Prompt Text, Note, LayerUtility: ImageScaleByAspectRatio V2, SetNode, GetNode, GetNode, GetNode, CLIPTextEncode, ConditioningZeroOut, GetNode, GetNode, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, SetNode, VAEDecode, SaveImage, GetNode, GetNode, LayerUtility: ImageReel, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, easy showAnything, PreviewImage, PreviewImage, PreviewImage, Image Comparer (rgthree), Image Comparer (rgthree), KSampler, LatentUpscaleBy, Note, SetNode, Image Comparer (rgthree), GetNode, VAEDecode, CannyEdgePreprocessor, AIO_Preprocessor, SetNode, easy anythingIndexSwitch, Qwen3_VQA, ModelPatchLoader, AIO_Preprocessor, LoadImage, QwenImageDiffsynthControlnet, easy anythingIndexSwitch, GetNode, KSampler, GetNode, SaveImage, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.7000000000000002, "height": 512, "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 8925, "steps": 10, "width": 512}
---

# 图片生成/图生图/【109】Z-image ControlNet控制2.0 + 提示词反推_2000772272614932481.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【109】Z-image ControlNet控制2.0 + 提示词反推_2000772272614932481.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（86 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `EmptyLatentImage` ★核心
- `GetNode`
- `LayerUtility: ImageReelComposit`
- `easy int`
- `easy int`
- `Note`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `Note`
- `GetNode`
- `Note`
- `Text Concatenate`
- `easy showAnything`
- `Note`
- `easy seed`
- `easy imagePixelPerfect`
- `easy showAnything`
- `CR Prompt Text`
- `Text Concatenate`
- `CR Prompt Text`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `VAEDecode` ★核心
- `SaveImage`
- `GetNode`
- `GetNode`
- `LayerUtility: ImageReel`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `LatentUpscaleBy`
- `Note`
- `SetNode`
- `Image Comparer (rgthree)`
- `GetNode`
- `VAEDecode` ★核心
- `CannyEdgePreprocessor`
- `AIO_Preprocessor`
- `SetNode`
- `easy anythingIndexSwitch`
- `Qwen3_VQA`
- `ModelPatchLoader`
- `AIO_Preprocessor`
- `LoadImage`
- `QwenImageDiffsynthControlnet`
- `easy anythingIndexSwitch`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `SaveImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `8925`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `0.7000000000000002`

## 知识

覆盖率 **41%**（35/86）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`LayerUtility: ImageReelComposit`、`easy int`、`Text Concatenate`、`easy seed`、`easy imagePixelPerfect`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`ConditioningZeroOut`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageReel`、`KSampler`、`LatentUpscaleBy`、`CannyEdgePreprocessor`、`AIO_Preprocessor`、`easy anythingIndexSwitch`、`Qwen3_VQA`、`ModelPatchLoader`、`LoadImage`、`QwenImageDiffsynthControlnet`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
