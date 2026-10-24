---
key: 图片生成/图生图/FireRed_Edit_1.1_plus_ultra_v9 图像编辑工作流_2044052989601648641.json
name: FireRed_Edit_1.1_plus_ultra_v9 图像编辑工作流_2044052989601648641
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed_Edit_1.1_plus_ultra_v9 图像编辑工作流_2044052989601648641.json
hash: 9cc1d72790210c6c
coverage: 0.759259
learned_at: 2026-10-23 10:55:56
nodes: [SeedVR2LoadVAEModel, easy cleanGpuUsed, easy clearCacheAll, easy cleanGpuUsed, easy clearCacheAll, SeedVR2VideoUpscaler, PreviewImage, Image Comparer (rgthree), SeedVR2LoadDiTModel, INTConstant, INTConstant, PreviewImage, ImageScaleToTotalPixels, Fast Groups Bypasser (rgthree), AIO_Preprocessor, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), MaskToImage, GetImageSize, ImageBlend, PrimitiveInt, ImpactSwitch, ImageScaleToTotalPixels, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SaveImage, SaveImage, MaskToImage, PrimitiveInt, GetImageSize, ImageBlend, CLIPTextEncode, CFGNorm, ImageUpscaleWithModel, EmptyLatentImage, ImpactSwitch, ImpactSwitch, KSampler, SaveImage, ImagePadForOutpaint, ModelSamplingAuraFlow, UNETLoader, LoraLoader, LoraLoader, TextEncodeQwenImageEditPlus, LoraLoader, UpscaleModelLoader, VAEDecode, VAELoader, UnetLoaderGGUF, CLIPLoader]
patterns: [text_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "lora_name": "FireRed-Image-Edit-1.0-Lightning-8steps-v1.1.safetensors", "sampler_name": "euler", "scheduler": "simple", "seed": 81613721704032, "steps": 6, "strength_clip": 1, "strength_model": 1, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed_Edit_1.1_plus_ultra_v9 图像编辑工作流_2044052989601648641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed_Edit_1.1_plus_ultra_v9 图像编辑工作流_2044052989601648641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `SeedVR2LoadVAEModel`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SeedVR2LoadDiTModel`
- `INTConstant`
- `INTConstant`
- `PreviewImage`
- `ImageScaleToTotalPixels`
- `Fast Groups Bypasser (rgthree)`
- `AIO_Preprocessor`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `MaskToImage`
- `GetImageSize`
- `ImageBlend`
- `PrimitiveInt`
- `ImpactSwitch`
- `ImageScaleToTotalPixels`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SaveImage`
- `SaveImage`
- `MaskToImage`
- `PrimitiveInt`
- `GetImageSize`
- `ImageBlend`
- `CLIPTextEncode` ★核心
- `CFGNorm`
- `ImageUpscaleWithModel`
- `EmptyLatentImage` ★核心
- `ImpactSwitch`
- `ImpactSwitch`
- `KSampler` ★核心
- `SaveImage`
- `ImagePadForOutpaint`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `LoraLoader` ★核心
- `UpscaleModelLoader`
- `VAEDecode` ★核心
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`

**识别到的模式**：text_to_image、lora

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `81613721704032`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `FireRed-Image-Edit-1.0-Lightning-8steps-v1.1.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **76%**（41/54）

**有卡**：`SeedVR2LoadVAEModel`、`easy cleanGpuUsed`、`easy clearCacheAll`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`INTConstant`、`ImageScaleToTotalPixels`、`AIO_Preprocessor`、`LoadImage`、`MaskToImage`、`GetImageSize`、`ImageBlend`、`SaveImage`、`CLIPTextEncode`、`CFGNorm`、`ImageUpscaleWithModel`、`EmptyLatentImage`、`KSampler`、`ImagePadForOutpaint`、`ModelSamplingAuraFlow`、`UNETLoader`、`LoraLoader`、`TextEncodeQwenImageEditPlus`、`UpscaleModelLoader`、`VAEDecode`、`VAELoader`、`UnetLoaderGGUF`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
