---
key: 图片生成/图生图/人物迁移 qwen-image-edit 2511+seedvr2.5，全能图片V1pro平替_2005065754267578370.json
name: 人物迁移 qwen-image-edit 2511+seedvr2.5，全能图片V1pro平替_2005065754267578370
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物迁移 qwen-image-edit 2511+seedvr2.5，全能图片V1pro平替_2005065754267578370.json
hash: 2ddd3c667a1bdbc1
coverage: 0.914286
learned_at: 2026-10-23 12:11:27
nodes: [VAELoader, ModelSamplingAuraFlow, CFGNorm, CLIPLoader, ConditioningZeroOut, VAEEncode, KSampler, LoadSAM3Model, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, SAM3Segmentation, BlockifyMask, LayerUtility: ImageBlend, DrawMaskOnImage, ImageResizeKJ, PreviewImage, PathchSageAttentionKJ, LoraLoaderModelOnly, RH_Translator, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SaveImage, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, SDPoseOODProcessor, TextEncodeQwenImageEditPlus, LoadImage, LoadImage, SDPoseOODLoader, PreviewImage, Int, UNETLoader, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 6681, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/人物迁移 qwen-image-edit 2511+seedvr2.5，全能图片V1pro平替_2005065754267578370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物迁移 qwen-image-edit 2511+seedvr2.5，全能图片V1pro平替_2005065754267578370.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `LoadSAM3Model`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `SAM3Segmentation`
- `BlockifyMask`
- `LayerUtility: ImageBlend`
- `DrawMaskOnImage`
- `ImageResizeKJ`
- `PreviewImage`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SDPoseOODProcessor`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `LoadImage`
- `SDPoseOODLoader`
- `PreviewImage`
- `Int`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `6681`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`CLIPLoader`、`ConditioningZeroOut`、`VAEEncode`、`KSampler`、`LoadSAM3Model`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`SAM3Segmentation`、`BlockifyMask`、`LayerUtility: ImageBlend`、`DrawMaskOnImage`、`ImageResizeKJ`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`RH_Translator`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`SDPoseOODProcessor`、`TextEncodeQwenImageEditPlus`、`LoadImage`、`SDPoseOODLoader`、`Int`、`UNETLoader`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
