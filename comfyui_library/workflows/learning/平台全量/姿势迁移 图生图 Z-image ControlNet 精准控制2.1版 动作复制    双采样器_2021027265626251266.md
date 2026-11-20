---
key: 平台全量/姿势迁移 图生图 Z-image ControlNet 精准控制2.1版 动作复制    双采样器_2021027265626251266.json
name: 姿势迁移 图生图 Z-image ControlNet 精准控制2.1版 动作复制    双采样器_2021027265626251266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/姿势迁移 图生图 Z-image ControlNet 精准控制2.1版 动作复制    双采样器_2021027265626251266.json
hash: 3d85e73efa953c2d
coverage: 0.43662
learned_at: 2026-11-14 01:59:07
nodes: [UNETLoader, SetNode, SetNode, SetNode, LayerUtility: ImageReelComposit, easy showAnything, easy imagePixelPerfect, CR Prompt Text, CR Prompt Text, GetNode, GetNode, PreviewImage, PreviewImage, PreviewImage, Image Comparer (rgthree), GetNode, SetNode, VAELoader, Text Concatenate, Text Concatenate, Note, ImpactSwitch, GetNode, GetNode, CLIPLoader, GetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM V2, EmptyLatentImage, SetNode, Note, GetNode, GetNode, VAEDecode, SetNode, ModelPatchLoader, CLIPTextEncode, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, AIO_Preprocessor, AIO_Preprocessor, ZImageFunControlnet, SetNode, GetNode, easy showAnything, HEDPreprocessor, GetNode, KSamplerAdvanced, KSamplerAdvanced, Note, GetNode, GetNode, GetNode, easy int, Note, CR Image Input Switch (4 way), SaveImage, SetNode, SetNode, SetNode, easy seed, SetNode, GetImageSize, LayerUtility: ImageReel, SaveImage, Qwen3_VQA, easy showAnything, GetNode, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 512, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 512}
---

# 平台全量/姿势迁移 图生图 Z-image ControlNet 精准控制2.1版 动作复制    双采样器_2021027265626251266.json

> 来源文件 `comfyui_library/workflows/平台全量/姿势迁移 图生图 Z-image ControlNet 精准控制2.1版 动作复制    双采样器_2021027265626251266.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageReelComposit`
- `easy showAnything`
- `easy imagePixelPerfect`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `EmptyLatentImage` ★核心
- `SetNode`
- `Note`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `ModelPatchLoader`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `easy int`
- `Note`
- `CR Image Input Switch (4 way)`
- `SaveImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy seed`
- `SetNode`
- `GetImageSize`
- `LayerUtility: ImageReel`
- `SaveImage`
- `Qwen3_VQA`
- `easy showAnything`
- `GetNode`
- `LoadImage`

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

覆盖率 **44%**（31/71）

**有卡**：`UNETLoader`、`LayerUtility: ImageReelComposit`、`easy imagePixelPerfect`、`CR Prompt Text`、`VAELoader`、`Text Concatenate`、`CLIPLoader`、`LayerUtility: PurgeVRAM V2`、`EmptyLatentImage`、`VAEDecode`、`ModelPatchLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`AIO_Preprocessor`、`ZImageFunControlnet`、`HEDPreprocessor`、`KSamplerAdvanced`、`easy int`、`CR Image Input Switch (4 way)`、`SaveImage`、`easy seed`、`GetImageSize`、`LayerUtility: ImageReel`、`Qwen3_VQA`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage、UNETLoader
