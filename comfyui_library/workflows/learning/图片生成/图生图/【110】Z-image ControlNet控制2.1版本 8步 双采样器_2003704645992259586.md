---
key: 图片生成/图生图/【110】Z-image ControlNet控制2.1版本 8步 双采样器_2003704645992259586.json
name: 【110】Z-image ControlNet控制2.1版本 8步 双采样器_2003704645992259586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【110】Z-image ControlNet控制2.1版本 8步 双采样器_2003704645992259586.json
hash: 6add4633018a054a
coverage: 0.418919
learned_at: 2026-10-23 11:48:05
nodes: [SetNode, UNETLoader, SetNode, SetNode, SetNode, LayerUtility: ImageReelComposit, SetNode, Note, GetNode, Note, easy showAnything, Note, easy imagePixelPerfect, easy showAnything, CR Prompt Text, CR Prompt Text, GetNode, GetNode, PreviewImage, PreviewImage, PreviewImage, Image Comparer (rgthree), GetNode, SetNode, VAELoader, Text Concatenate, Text Concatenate, Note, ImpactSwitch, GetNode, GetNode, CLIPLoader, Qwen3_VQA, GetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM V2, EmptyLatentImage, SetNode, SetNode, GetImageSize, SetNode, Note, SaveImage, GetNode, GetNode, VAEDecode, SetNode, ModelPatchLoader, LoadImage, CLIPTextEncode, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, AIO_Preprocessor, ZImageFunControlnet, SetNode, GetNode, easy showAnything, HEDPreprocessor, GetNode, KSamplerAdvanced, KSamplerAdvanced, Note, SaveImage, LayerUtility: ImageReel, GetNode, easy seed, GetNode, GetNode, easy int, Note, CR Image Input Switch (4 way)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 512, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 512}
---

# 图片生成/图生图/【110】Z-image ControlNet控制2.1版本 8步 双采样器_2003704645992259586.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【110】Z-image ControlNet控制2.1版本 8步 双采样器_2003704645992259586.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageReelComposit`
- `SetNode`
- `Note`
- `GetNode`
- `Note`
- `easy showAnything`
- `Note`
- `easy imagePixelPerfect`
- `easy showAnything`
- `CR Prompt Text`
- `CR Prompt Text`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `GetNode`
- `SetNode`
- `VAELoader`
- `Text Concatenate`
- `Text Concatenate`
- `Note`
- `ImpactSwitch`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `Qwen3_VQA`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `EmptyLatentImage` ★核心
- `SetNode`
- `SetNode`
- `GetImageSize`
- `SetNode`
- `Note`
- `SaveImage`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `ModelPatchLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `ZImageFunControlnet`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `HEDPreprocessor`
- `GetNode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `Note`
- `SaveImage`
- `LayerUtility: ImageReel`
- `GetNode`
- `easy seed`
- `GetNode`
- `GetNode`
- `easy int`
- `Note`
- `CR Image Input Switch (4 way)`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **42%**（31/74）

**有卡**：`UNETLoader`、`LayerUtility: ImageReelComposit`、`easy imagePixelPerfect`、`CR Prompt Text`、`VAELoader`、`Text Concatenate`、`CLIPLoader`、`Qwen3_VQA`、`LayerUtility: PurgeVRAM V2`、`EmptyLatentImage`、`GetImageSize`、`SaveImage`、`VAEDecode`、`ModelPatchLoader`、`LoadImage`、`CLIPTextEncode`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`AIO_Preprocessor`、`ZImageFunControlnet`、`HEDPreprocessor`、`KSamplerAdvanced`、`LayerUtility: ImageReel`、`easy seed`、`easy int`、`CR Image Input Switch (4 way)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、UNETLoader
