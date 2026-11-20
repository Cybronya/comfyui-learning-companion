---
key: 图片生成/文生图/强强联合！MJ风格工作流3.0版本！_2115671429000814593.json
name: 强强联合！MJ风格工作流3.0版本！_2115671429000814593
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/强强联合！MJ风格工作流3.0版本！_2115671429000814593.json
hash: 5cdb3653cb26157e
coverage: 0.5
learned_at: 2026-10-30 17:56:03
nodes: [CLIPLoader, ConditioningZeroOut, VAELoader, VAEDecode, SetNode, ConditioningKrea2Rebalance, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, GetNode, SetNode, SetNode, EmptyFlux2LatentImage, CLIPLoader, CLIPTextEncode, SetNode, SetNode, PrimitiveFloat, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, KSampler, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageSize, SeedVR2VideoUpscaler, ImageScaleBy, ImageResize+, ImageResize+, SeedVR2LoadVAEModel, SetNode, Any Switch (rgthree), ImageScaleBy, easy imageSize, GetNode, GetNode, Any Switch (rgthree), Image Comparer (rgthree), GetNode, GetNode, CLIPTextEncode, SetNode, SaveImage, UNETLoader, ModelSamplingAuraFlow, GetNode, KSampler, SetNode, UNETLoader, SetNode, SaveImage, SeedVR2LoadDiTModel, LoraLoaderModelOnly, SetNode, LoraLoaderModelOnly, ResolutionSelector, CLIPTextEncode, GetNode, GetNode, GetNode, CLIPTextEncode, VAEEncode, GetNode, KSampler, VAEDecode, GetNode, SetNode, SaveImage, PrimitiveInt, GetNode, GetNode, GetNode, Fast Groups Muter (rgthree), PrimitiveStringMultiline, EmptyLatentImage, SetNode, GetNode, Label (rgthree), Label (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 2.5, "denoise": 0.3600000000000001, "height": 1024, "sampler_name": "er_sde", "scheduler": "simple", "seed": 42, "steps": 25, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/强强联合！MJ风格工作流3.0版本！_2115671429000814593.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/强强联合！MJ风格工作流3.0版本！_2115671429000814593.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（96 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAELoader`
- `VAEDecode` ★核心
- `SetNode`
- `ConditioningKrea2Rebalance`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `EmptyFlux2LatentImage`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `KSampler` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageSize`
- `SeedVR2VideoUpscaler`
- `ImageScaleBy`
- `ImageResize+`
- `ImageResize+`
- `SeedVR2LoadVAEModel`
- `SetNode`
- `Any Switch (rgthree)`
- `ImageScaleBy`
- `easy imageSize`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `Image Comparer (rgthree)`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SaveImage`
- `UNETLoader` ★核心
- `ModelSamplingAuraFlow`
- `GetNode`
- `KSampler` ★核心
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `GetNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `SaveImage`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Muter (rgthree)`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `SetNode`
- `GetNode`
- `Label (rgthree)`
- `Label (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `42`
- `steps` = `25`
- `cfg` = `2.5`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `0.3600000000000001`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（48/96）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`VAELoader`、`VAEDecode`、`ConditioningKrea2Rebalance`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`EmptyFlux2LatentImage`、`KSampler`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`TTP_Tile_image_size`、`easy imageSize`、`SeedVR2VideoUpscaler`、`ImageScaleBy`、`ImageResize+`、`SeedVR2LoadVAEModel`、`SaveImage`、`UNETLoader`、`ModelSamplingAuraFlow`、`SeedVR2LoadDiTModel`、`ResolutionSelector`、`VAEEncode`、`EmptyLatentImage`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
