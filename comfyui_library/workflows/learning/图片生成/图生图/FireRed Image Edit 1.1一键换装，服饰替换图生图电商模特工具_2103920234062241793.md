---
key: 图片生成/图生图/FireRed Image Edit 1.1一键换装，服饰替换图生图电商模特工具_2103920234062241793.json
name: FireRed Image Edit 1.1一键换装，服饰替换图生图电商模特工具_2103920234062241793
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.1一键换装，服饰替换图生图电商模特工具_2103920234062241793.json
hash: 12fb1e71d23be9d4
coverage: 0.9
learned_at: 2026-10-21 00:39:18
nodes: [VAEEncode, ConditioningZeroOut, LayerUtility: PurgeVRAM, ReferenceLatent, ReferenceLatent, GetImageSize, EmptyFlux2LatentImage, VAEDecode, ImageScaleBy, ImageScaleBy, CLIPTextEncode, VAELoader, llama_cpp_parameters, EmptySD3LatentImage, EmptySD3LatentImage, KSampler, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, ImageConcanate, VAEEncode, VAEEncode, CLIPLoader, PathchSageAttentionKJ, ImageScaleToTotalPixels, easy imageSize, Reroute, LayerUtility: PurgeVRAM, ImageScaleToTotalPixels, LayerUtility: ImageReel, ImageConcatMulti, ImageScaleToTotalPixels, CR Text Concatenate, ConditioningZeroOut, ModelSamplingAuraFlow, CLIPLoader, VAELoader, LayerUtility: ImageReel, LayerUtility: ImageReel, VAEDecode, VAEDecode, easy imageColorMatch, CR Text, CR Text, CR Text Concatenate, CR Text, PrimitiveBoolean, easy ifElse, TextEncodeQwenImageEditPlus, CR Text, easy promptReplace, ShowText|pysssss, CR Text, LayerUtility: PurgeVRAM, ShowText|pysssss, LoadImage, LoadImage, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CFGNorm, KSampler, KSampler, llama_cpp_model_loader, llama_cpp_instruct_adv, PreviewImage, Image Comparer (rgthree), KOOK_SaveJPGImage, LayerColor: ColorAdapter, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed Image Edit 1.1一键换装，服饰替换图生图电商模特工具_2103920234062241793.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.1一键换装，服饰替换图生图电商模特工具_2103920234062241793.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（100 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（90/100）

**有卡**：`VAEEncode`、`ConditioningZeroOut`、`LayerUtility: PurgeVRAM`、`ReferenceLatent`、`GetImageSize`、`EmptyFlux2LatentImage`、`VAEDecode`、`ImageScaleBy`、`CLIPTextEncode`、`VAELoader`、`llama_cpp_parameters`、`EmptySD3LatentImage`、`KSampler`、`LayerUtility: ImageReelComposit`、`ImageConcanate`、`CLIPLoader`、`PathchSageAttentionKJ`、`ImageScaleToTotalPixels`、`easy imageSize`、`LayerUtility: ImageReel`、`ImageConcatMulti`、`CR Text Concatenate`、`ModelSamplingAuraFlow`、`easy imageColorMatch`、`CR Text`、`PrimitiveBoolean`、`TextEncodeQwenImageEditPlus`、`easy promptReplace`、`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`CFGNorm`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`KOOK_SaveJPGImage`、`LayerColor: ColorAdapter`、`SaveImage`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
