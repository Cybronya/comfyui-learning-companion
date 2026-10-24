---
key: 图片生成/图生图/Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000525304743460865.json
name: Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000525304743460865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000525304743460865.json
hash: 7cf43c5bdcbdc273
coverage: 0.833333
learned_at: 2026-10-23 11:31:31
nodes: [VAELoader, EmptySD3LatentImage, Note, CLIPTextEncode, GetImageSize, CLIPLoader, ModelSamplingAuraFlow, VAEDecode, Canny, AIO_Preprocessor, QwenImageDiffsynthControlnet, PreviewImage, AIO_Preprocessor, UNETLoader, ImageConcatMulti, easy showAnything, SeedVR2, LayerUtility: PurgeVRAM, SaveImage, ImageCASharpening+, Image Comparer (rgthree), SaveImage, LoadImage, ImageScaleToMaxDimension, ConditioningZeroOut, SaveImage, KSampler, ImageResize+, PreviewImage, TTP_Image_Tile_Batch, ImageResize+, ImageCASharpening+, Get Image Size, ImpactMinMax, SaveImage, LayerUtility: PurgeVRAM, VAEDecode, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, TTP_Image_Assy, Image Comparer (rgthree), Qwen3_VQA, CR Prompt Text, Note, Note, easy showAnything, CR Prompt Text, Text Concatenate, Text Concatenate, easy anythingIndexSwitch, ModelPatchLoader, SaveImage, easy anythingIndexSwitch]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.6500000000000001, "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 445144804643622, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000525304743460865.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image完美版自动提示词多条件Union Controlnet 2.0控制V1_2000525304743460865.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `VAELoader`
- `EmptySD3LatentImage`
- `Note`
- `CLIPTextEncode` ★核心
- `GetImageSize`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `VAEDecode` ★核心
- `Canny`
- `AIO_Preprocessor`
- `QwenImageDiffsynthControlnet`
- `PreviewImage`
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `ImageConcatMulti`
- `easy showAnything`
- `SeedVR2`
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `ImageCASharpening+`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `ImageScaleToMaxDimension`
- `ConditioningZeroOut`
- `SaveImage`
- `KSampler` ★核心
- `ImageResize+`
- `PreviewImage`
- `TTP_Image_Tile_Batch`
- `ImageResize+`
- `ImageCASharpening+`
- `Get Image Size`
- `ImpactMinMax`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `Qwen3_VQA`
- `CR Prompt Text`
- `Note`
- `Note`
- `easy showAnything`
- `CR Prompt Text`
- `Text Concatenate`
- `Text Concatenate`
- `easy anythingIndexSwitch`
- `ModelPatchLoader`
- `SaveImage`
- `easy anythingIndexSwitch`

## 关键参数

- `seed` = `445144804643622`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `0.6500000000000001`

## 知识

覆盖率 **83%**（45/54）

**有卡**：`VAELoader`、`EmptySD3LatentImage`、`CLIPTextEncode`、`GetImageSize`、`CLIPLoader`、`ModelSamplingAuraFlow`、`VAEDecode`、`Canny`、`AIO_Preprocessor`、`QwenImageDiffsynthControlnet`、`UNETLoader`、`ImageConcatMulti`、`SeedVR2`、`LayerUtility: PurgeVRAM`、`SaveImage`、`ImageCASharpening+`、`LoadImage`、`ImageScaleToMaxDimension`、`ConditioningZeroOut`、`KSampler`、`ImageResize+`、`TTP_Image_Tile_Batch`、`Get Image Size`、`ImpactMinMax`、`LoraLoaderModelOnly`、`TTP_Image_Assy`、`Qwen3_VQA`、`CR Prompt Text`、`Text Concatenate`、`easy anythingIndexSwitch`、`ModelPatchLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
