---
key: 图片生成/图生图/一键换装-FireRed-image-edit-1.1_2105579383493849089.json
name: 一键换装-FireRed-image-edit-1.1_2105579383493849089
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键换装-FireRed-image-edit-1.1_2105579383493849089.json
hash: 83650225be8679d3
coverage: 0.915493
learned_at: 2026-10-21 00:46:54
nodes: [VAEEncode, ConditioningZeroOut, LayerUtility: PurgeVRAM, ReferenceLatent, ReferenceLatent, GetImageSize, EmptyFlux2LatentImage, VAEDecode, ImageScaleBy, ImageScaleBy, CLIPTextEncode, VAELoader, llama_cpp_parameters, EmptySD3LatentImage, EmptySD3LatentImage, KSampler, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, ImageConcanate, VAEEncode, VAEEncode, CLIPLoader, PathchSageAttentionKJ, ImageScaleToTotalPixels, easy imageSize, Reroute, LayerUtility: PurgeVRAM, ImageScaleToTotalPixels, LayerUtility: ImageReel, ImageConcatMulti, ImageScaleToTotalPixels, CR Text Concatenate, ConditioningZeroOut, ModelSamplingAuraFlow, CLIPLoader, VAELoader, LayerUtility: ImageReel, LayerUtility: ImageReel, VAEDecode, VAEDecode, easy imageColorMatch, CR Text, CR Text, CR Text Concatenate, CR Text, PrimitiveBoolean, easy ifElse, TextEncodeQwenImageEditPlus, CR Text, easy promptReplace, ShowText|pysssss, CR Text, LayerUtility: PurgeVRAM, ShowText|pysssss, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CFGNorm, KSampler, KSampler, llama_cpp_model_loader, llama_cpp_instruct_adv, PreviewImage, Image Comparer (rgthree), KOOK_SaveJPGImage, LayerColor: ColorAdapter, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.6000000000000001, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 949758735698657, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/一键换装-FireRed-image-edit-1.1_2105579383493849089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键换装-FireRed-image-edit-1.1_2105579383493849089.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM`
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `ImageScaleBy`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `llama_cpp_parameters`
- `EmptySD3LatentImage`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReelComposit`
- `ImageConcanate`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `ImageScaleToTotalPixels`
- `easy imageSize`
- `Reroute`
- `LayerUtility: PurgeVRAM`
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageReel`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `ModelSamplingAuraFlow`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReel`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `easy imageColorMatch`
- `CR Text`
- `CR Text`
- `CR Text Concatenate`
- `CR Text`
- `PrimitiveBoolean`
- `easy ifElse`
- `TextEncodeQwenImageEditPlus`
- `CR Text`
- `easy promptReplace`
- `ShowText|pysssss`
- `CR Text`
- `LayerUtility: PurgeVRAM`
- `ShowText|pysssss`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `KSampler` ★核心
- `KSampler` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `KOOK_SaveJPGImage`
- `LayerColor: ColorAdapter`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `949758735698657`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **92%**（65/71）

**有卡**：`VAEEncode`、`ConditioningZeroOut`、`LayerUtility: PurgeVRAM`、`ReferenceLatent`、`GetImageSize`、`EmptyFlux2LatentImage`、`VAEDecode`、`ImageScaleBy`、`CLIPTextEncode`、`VAELoader`、`llama_cpp_parameters`、`EmptySD3LatentImage`、`KSampler`、`LayerUtility: ImageReelComposit`、`ImageConcanate`、`CLIPLoader`、`PathchSageAttentionKJ`、`ImageScaleToTotalPixels`、`easy imageSize`、`LayerUtility: ImageReel`、`ImageConcatMulti`、`CR Text Concatenate`、`ModelSamplingAuraFlow`、`easy imageColorMatch`、`CR Text`、`PrimitiveBoolean`、`TextEncodeQwenImageEditPlus`、`easy promptReplace`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CFGNorm`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`KOOK_SaveJPGImage`、`LayerColor: ColorAdapter`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
