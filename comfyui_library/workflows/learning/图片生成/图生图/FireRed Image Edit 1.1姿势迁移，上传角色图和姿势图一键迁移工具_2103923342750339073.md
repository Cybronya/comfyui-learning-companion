---
key: 图片生成/图生图/FireRed Image Edit 1.1姿势迁移，上传角色图和姿势图一键迁移工具_2103923342750339073.json
name: FireRed Image Edit 1.1姿势迁移，上传角色图和姿势图一键迁移工具_2103923342750339073
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.1姿势迁移，上传角色图和姿势图一键迁移工具_2103923342750339073.json
hash: 6209f00a56b863ff
coverage: 0.863636
learned_at: 2026-10-21 00:39:19
nodes: [ImageConcanate, ConditioningZeroOut, VAEDecode, VAEEncode, KSampler, UnetLoaderGGUF, LayerUtility: PurgeVRAM, ImageScaleToTotalPixels, ModelSamplingAuraFlow, CFGNorm, PathchSageAttentionKJ, ConditioningZeroOut, EmptySD3LatentImage, easy imageSize, LoadImage, ShowText|pysssss, LayerUtility: PurgeVRAM, ImageScaleToTotalPixels, ImageScaleToTotalPixels, CLIPLoader, VAELoader, VAELoader, CLIPLoader, CR Text, CR Text, SDPoseOODLoader, LoadImage, CLIPTextEncode, UNETLoader, UNETLoader, VAEDecode, LayerUtility: PurgeVRAM, SaveImage, PreviewImage, Image Comparer (rgthree), ImageConcanate, SaveImageJPG_GH, PreviewImage, VAEDecode, LayerColor: ColorAdapter, KSampler, LoraLoaderModelOnly, workflow>123, LoraLoaderModelOnly, KSampler, SDPoseOODProcessor, PreviewImage, easy ifElse, PrimitiveBoolean, TextEncodeQwenImageEditPlus, ShowText|pysssss, Qwen3_VQA, SomethingToString, PrimitiveBoolean, easy ifElse, CR Text Concatenate, CR Text Concatenate, CR Text, CR Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed Image Edit 1.1姿势迁移，上传角色图和姿势图一键迁移工具_2103923342750339073.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed Image Edit 1.1姿势迁移，上传角色图和姿势图一键迁移工具_2103923342750339073.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `ImageConcanate`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `KSampler` ★核心
- `UnetLoaderGGUF` ★核心
- `LayerUtility: PurgeVRAM`
- `ImageScaleToTotalPixels`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PathchSageAttentionKJ`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `easy imageSize`
- `LoadImage`
- `ShowText|pysssss`
- `LayerUtility: PurgeVRAM`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `CR Text`
- `CR Text`
- `SDPoseOODLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `SaveImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `SaveImageJPG_GH`
- `PreviewImage`
- `VAEDecode` ★核心
- `LayerColor: ColorAdapter`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `workflow>123`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SDPoseOODProcessor`
- `PreviewImage`
- `easy ifElse`
- `PrimitiveBoolean`
- `TextEncodeQwenImageEditPlus`
- `ShowText|pysssss`
- `Qwen3_VQA`
- `SomethingToString`
- `PrimitiveBoolean`
- `easy ifElse`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text`
- `CR Text`
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

覆盖率 **86%**（76/88）

**有卡**：`ImageConcanate`、`ConditioningZeroOut`、`VAEDecode`、`VAEEncode`、`KSampler`、`UnetLoaderGGUF`、`LayerUtility: PurgeVRAM`、`ImageScaleToTotalPixels`、`ModelSamplingAuraFlow`、`CFGNorm`、`PathchSageAttentionKJ`、`EmptySD3LatentImage`、`easy imageSize`、`LoadImage`、`CLIPLoader`、`VAELoader`、`CR Text`、`SDPoseOODLoader`、`CLIPTextEncode`、`UNETLoader`、`SaveImage`、`SaveImageJPG_GH`、`LayerColor: ColorAdapter`、`LoraLoaderModelOnly`、`workflow>123`、`SDPoseOODProcessor`、`PrimitiveBoolean`、`TextEncodeQwenImageEditPlus`、`Qwen3_VQA`、`SomethingToString`、`CR Text Concatenate`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

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
