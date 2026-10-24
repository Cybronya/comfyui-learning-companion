---
key: 图片生成/图生图/老高自动提示词（洗图背景）Union+Controlnet+2.0_2015688100151824386.json
name: 老高自动提示词（洗图背景）Union+Controlnet+2.0_2015688100151824386
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/老高自动提示词（洗图背景）Union+Controlnet+2.0_2015688100151824386.json
hash: e4c3aaec518ff9ee
coverage: 0.814815
learned_at: 2026-10-23 13:23:27
nodes: [KSampler, easy showAnything, CLIPTextEncode, AIO_Preprocessor, Canny, AIO_Preprocessor, GetImageSize, ImageResize+, ImageCASharpening+, Get Image Size, ImpactMinMax, TTP_Image_Tile_Batch, PreviewImage, easy showAnything, SeedVR2, LayerUtility: PurgeVRAM, TTP_Image_Assy, ImageCASharpening+, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ConditioningZeroOut, LayerUtility: PurgeVRAM, ImageResize+, SaveImage, Image Comparer (rgthree), VAEDecode, SaveImage, LoraLoaderModelOnly, MarkdownNote, easy anythingIndexSwitch, MarkdownNote, VAELoader, Qwen3_VQA, PreviewImage, SaveImage, MarkdownNote, PreviewImage, ImageConcatMulti, ImageConcatMulti, easy int, LoadImage, KSampler, VAEDecode, CLIPLoader, EmptySD3LatentImage, ModelSamplingAuraFlow, ModelPatchLoader, QwenImageDiffsynthControlnet, LoraLoaderModelOnly, Text Concatenate, CR Prompt Text, UNETLoader, LoraLoaderModelOnly, CR Prompt Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.6500000000000001, "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 1121020078992875, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/老高自动提示词（洗图背景）Union+Controlnet+2.0_2015688100151824386.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/老高自动提示词（洗图背景）Union+Controlnet+2.0_2015688100151824386.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `KSampler` ★核心
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `Canny`
- `AIO_Preprocessor`
- `GetImageSize`
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM`
- `ImageResize+`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `easy anythingIndexSwitch`
- `MarkdownNote`
- `VAELoader`
- `Qwen3_VQA`
- `PreviewImage`
- `SaveImage`
- `MarkdownNote`
- `PreviewImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `easy int`
- `LoadImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `LoraLoaderModelOnly` ★核心
- `Text Concatenate`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`

## 关键参数

- `seed` = `1121020078992875`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `0.6500000000000001`

## 知识

覆盖率 **81%**（44/54）

**有卡**：`KSampler`、`CLIPTextEncode`、`AIO_Preprocessor`、`Canny`、`GetImageSize`、`ImageResize+`、`ImageCASharpening+`、`Get Image Size`、`ImpactMinMax`、`TTP_Image_Tile_Batch`、`SeedVR2`、`LayerUtility: PurgeVRAM`、`TTP_Image_Assy`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`SaveImage`、`VAEDecode`、`LoraLoaderModelOnly`、`easy anythingIndexSwitch`、`VAELoader`、`Qwen3_VQA`、`ImageConcatMulti`、`easy int`、`LoadImage`、`CLIPLoader`、`EmptySD3LatentImage`、`ModelSamplingAuraFlow`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`Text Concatenate`、`CR Prompt Text`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
