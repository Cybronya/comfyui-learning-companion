---
key: 图片生成/图生图/SAM3 + Qwen_Edit + Z-Image Turbo 换装工作流_1995890984967946241.json
name: SAM3 + Qwen_Edit + Z-Image Turbo 换装工作流_1995890984967946241
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SAM3 + Qwen_Edit + Z-Image Turbo 换装工作流_1995890984967946241.json
hash: bc05078d1ce85738
coverage: 0.557143
learned_at: 2026-10-23 11:23:28
nodes: [PrimitiveInt, SetNode, SetNode, PrimitiveInt, CLIPLoader, VAELoader, ModelSamplingAuraFlow, CFGNorm, SetNode, SetNode, SetNode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, GetNode, GetNode, GetNode, GetNode, VAEDecode, PreviewImage, GetNode, GetNode, GetNode, SaveImageExtended, ModelSamplingAuraFlow, easy clearCacheAll, easy cleanGpuUsed, CLIPTextEncode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, PreviewImage, Image Comparer (rgthree), UpscaleModelLoader, SetNode, CLIPLoader, VAELoader, SetNode, SetNode, SetNode, Fast Groups Bypasser (rgthree), SetLatentNoiseMask, VAEEncode, MaskToImage, PreviewImage, MaskToImage, PreviewImage, GrowMaskWithBlur, Mask Rect Area (Advanced), GetImageSize, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoadImage, LoadImage, ImageScaleToTotalPixels, SetNode, ImageScaleToTotalPixels, SetNode, MaskBoundingBox+, PreviewImage, SAM3Segmentation, EmptySD3LatentImage, LoadSAM3Model, UltimateSDUpscale, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 885603708971368, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/SAM3 + Qwen_Edit + Z-Image Turbo 换装工作流_1995890984967946241.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SAM3 + Qwen_Edit + Z-Image Turbo 换装工作流_1995890984967946241.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（70 个）：
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `SetNode`
- `SetNode`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `SaveImageExtended`
- `ModelSamplingAuraFlow`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `UpscaleModelLoader`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `SetLatentNoiseMask`
- `VAEEncode` ★核心
- `MaskToImage`
- `PreviewImage`
- `MaskToImage`
- `PreviewImage`
- `GrowMaskWithBlur`
- `Mask Rect Area (Advanced)`
- `GetImageSize`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `SetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `MaskBoundingBox+`
- `PreviewImage`
- `SAM3Segmentation`
- `EmptySD3LatentImage`
- `LoadSAM3Model`
- `UltimateSDUpscale`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `885603708971368`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **56%**（39/70）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`TextEncodeQwenImageEditPlus`、`KSampler`、`VAEDecode`、`SaveImageExtended`、`easy clearCacheAll`、`easy cleanGpuUsed`、`CLIPTextEncode`、`GetImageSizeAndCount`、`UpscaleModelLoader`、`SetLatentNoiseMask`、`VAEEncode`、`MaskToImage`、`GrowMaskWithBlur`、`Mask Rect Area (Advanced)`、`GetImageSize`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`ImageScaleToTotalPixels`、`MaskBoundingBox+`、`SAM3Segmentation`、`EmptySD3LatentImage`、`LoadSAM3Model`、`UltimateSDUpscale`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
