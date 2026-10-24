---
key: 图片生成/图生图/一键换装,服装迁移，电商换装，小红书风格FireRed-image-edit-1.1_2066680972007006209.json
name: 一键换装,服装迁移，电商换装，小红书风格FireRed-image-edit-1.1_2066680972007006209
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键换装,服装迁移，电商换装，小红书风格FireRed-image-edit-1.1_2066680972007006209.json
hash: b18acea265f6b8c3
coverage: 0.92
learned_at: 2026-10-23 11:56:42
nodes: [VAEEncode, ConditioningZeroOut, LayerUtility: PurgeVRAM, ReferenceLatent, ReferenceLatent, GetImageSize, EmptyFlux2LatentImage, CLIPTextEncode, VAELoader, llama_cpp_parameters, EmptySD3LatentImage, EmptySD3LatentImage, KSampler, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, ImageConcanate, VAEEncode, VAEEncode, CLIPLoader, PathchSageAttentionKJ, ImageScaleToTotalPixels, easy imageSize, Reroute, ImageScaleToTotalPixels, LayerUtility: ImageReel, ImageConcatMulti, ImageScaleToTotalPixels, CR Text Concatenate, ConditioningZeroOut, ModelSamplingAuraFlow, CLIPLoader, VAELoader, LayerUtility: ImageReel, CR Text, CR Text, CR Text Concatenate, PrimitiveBoolean, easy ifElse, TextEncodeQwenImageEditPlus, CR Text, ShowText|pysssss, LayerUtility: PurgeVRAM, ShowText|pysssss, UNETLoader, LoraLoaderModelOnly, CFGNorm, KSampler, llama_cpp_model_loader, llama_cpp_instruct_adv, LoraLoaderModelOnly, KSampler, ImageScaleBy, easy imageColorMatch, VAEDecode, CR Text, easy promptReplace, VAEDecode, ImageScaleBy, UNETLoader, LoraLoaderModelOnly, LayerUtility: PurgeVRAM, VAEDecode, LayerUtility: ImageReel, Image Comparer (rgthree), KOOK_SaveJPGImage, LoadImage, LoadImage, Image Comparer (rgthree), SaveImage, SaveImageAndMetadata_, LayerColor: ColorAdapter, SaveImageAndMetadata_, SaveImage, CR Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.6000000000000001, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 1010827569638829, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/一键换装,服装迁移，电商换装，小红书风格FireRed-image-edit-1.1_2066680972007006209.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键换装,服装迁移，电商换装，小红书风格FireRed-image-edit-1.1_2066680972007006209.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `LayerUtility: PurgeVRAM`
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `EmptyFlux2LatentImage`
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
- `CR Text`
- `CR Text`
- `CR Text Concatenate`
- `PrimitiveBoolean`
- `easy ifElse`
- `TextEncodeQwenImageEditPlus`
- `CR Text`
- `ShowText|pysssss`
- `LayerUtility: PurgeVRAM`
- `ShowText|pysssss`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `KSampler` ★核心
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `ImageScaleBy`
- `easy imageColorMatch`
- `VAEDecode` ★核心
- `CR Text`
- `easy promptReplace`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: PurgeVRAM`
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `Image Comparer (rgthree)`
- `KOOK_SaveJPGImage`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImageAndMetadata_`
- `LayerColor: ColorAdapter`
- `SaveImageAndMetadata_`
- `SaveImage`
- `CR Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1010827569638829`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **92%**（69/75）

**有卡**：`VAEEncode`、`ConditioningZeroOut`、`LayerUtility: PurgeVRAM`、`ReferenceLatent`、`GetImageSize`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`VAELoader`、`llama_cpp_parameters`、`EmptySD3LatentImage`、`KSampler`、`LayerUtility: ImageReelComposit`、`ImageConcanate`、`CLIPLoader`、`PathchSageAttentionKJ`、`ImageScaleToTotalPixels`、`easy imageSize`、`LayerUtility: ImageReel`、`ImageConcatMulti`、`CR Text Concatenate`、`ModelSamplingAuraFlow`、`CR Text`、`PrimitiveBoolean`、`TextEncodeQwenImageEditPlus`、`UNETLoader`、`LoraLoaderModelOnly`、`CFGNorm`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`ImageScaleBy`、`easy imageColorMatch`、`VAEDecode`、`easy promptReplace`、`KOOK_SaveJPGImage`、`LoadImage`、`SaveImage`、`SaveImageAndMetadata_`、`LayerColor: ColorAdapter`

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
