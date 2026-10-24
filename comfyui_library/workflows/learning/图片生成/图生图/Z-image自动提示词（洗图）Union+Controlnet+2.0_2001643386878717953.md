---
key: 图片生成/图生图/Z-image自动提示词（洗图）Union+Controlnet+2.0_2001643386878717953.json
name: Z-image自动提示词（洗图）Union+Controlnet+2.0_2001643386878717953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image自动提示词（洗图）Union+Controlnet+2.0_2001643386878717953.json
hash: 30b7a1dde0083c03
coverage: 0.807692
learned_at: 2026-10-23 11:31:57
nodes: [KSampler, easy showAnything, CLIPTextEncode, AIO_Preprocessor, Canny, AIO_Preprocessor, GetImageSize, EmptySD3LatentImage, Text Concatenate, KSampler, ImageResize+, ImageCASharpening+, Get Image Size, ImpactMinMax, TTP_Image_Tile_Batch, PreviewImage, easy showAnything, SeedVR2, LayerUtility: PurgeVRAM, TTP_Image_Assy, ImageCASharpening+, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ModelSamplingAuraFlow, ConditioningZeroOut, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, ImageResize+, SaveImage, Image Comparer (rgthree), VAEDecode, SaveImage, LoraLoaderModelOnly, CR Prompt Text, LoadImage, MarkdownNote, easy anythingIndexSwitch, QwenImageDiffsynthControlnet, ModelPatchLoader, easy int, MarkdownNote, VAELoader, Qwen3_VQA, CLIPLoader, PreviewImage, SaveImage, MarkdownNote, VAEDecode, PreviewImage, ImageConcatMulti, ImageConcatMulti]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.6500000000000001, "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 519019905993125, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-image自动提示词（洗图）Union+Controlnet+2.0_2001643386878717953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image自动提示词（洗图）Union+Controlnet+2.0_2001643386878717953.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `KSampler` ★核心
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `Canny`
- `AIO_Preprocessor`
- `GetImageSize`
- `EmptySD3LatentImage`
- `Text Concatenate`
- `KSampler` ★核心
- `ImageResize+`
- `ImageCASharpening+`
- `Get Image Size`
- `ImpactMinMax`
- `TTP_Image_Tile_Batch`
- `PreviewImage`
- `easy showAnything`
- `SeedVR2`
- `LayerUtility: PurgeVRAM`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `ImageResize+`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `LoadImage`
- `MarkdownNote`
- `easy anythingIndexSwitch`
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `easy int`
- `MarkdownNote`
- `VAELoader`
- `Qwen3_VQA`
- `CLIPLoader`
- `PreviewImage`
- `SaveImage`
- `MarkdownNote`
- `VAEDecode` ★核心
- `PreviewImage`
- `ImageConcatMulti`
- `ImageConcatMulti`

## 关键参数

- `seed` = `519019905993125`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `0.6500000000000001`

## 知识

覆盖率 **81%**（42/52）

**有卡**：`KSampler`、`CLIPTextEncode`、`AIO_Preprocessor`、`Canny`、`GetImageSize`、`EmptySD3LatentImage`、`Text Concatenate`、`ImageResize+`、`ImageCASharpening+`、`Get Image Size`、`ImpactMinMax`、`TTP_Image_Tile_Batch`、`SeedVR2`、`LayerUtility: PurgeVRAM`、`TTP_Image_Assy`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`SaveImage`、`VAEDecode`、`CR Prompt Text`、`LoadImage`、`easy anythingIndexSwitch`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`easy int`、`VAELoader`、`Qwen3_VQA`、`CLIPLoader`、`ImageConcatMulti`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
