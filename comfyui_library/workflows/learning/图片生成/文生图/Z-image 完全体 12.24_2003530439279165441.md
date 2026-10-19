---
key: 图片生成/文生图/Z-image 完全体 12.24_2003530439279165441.json
name: Z-image 完全体 12.24_2003530439279165441
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image 完全体 12.24_2003530439279165441.json
hash: 6c4ce9aae1bbc7b9
coverage: 0.857143
learned_at: 2026-10-19 21:47:06
nodes: [VAEDecode, VAEDecode, ZImageFunControlnet, CLIPTextEncode, AIO_Preprocessor, LoadImage, EmptyLatentImage, KSampler, TilePreprocessor, AILab_MaskEnhancer, CLIPTextEncode, ZImageFunControlnet, KSampler, PreviewImage, PreviewImage, LoadImage, LoadImage, ModelPatchLoader, VAEEncode, VAEDecode, UpscaleModelLoader, KSamplerAdvanced, ZImageFunControlnet, ModelPatchLoader, Fast Groups Bypasser (rgthree), Anything Everywhere3, Anything Everywhere, UnetLoaderGGUF, CLIPLoader, VAELoader, CLIPTextEncode, ImageUpscaleWithModel, KSamplerAdvanced, SaveImage, EmptyLatentImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 2, "cfg": 9, "denoise": "FlowMatchEulerDiscreteScheduler", "height": 1720, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "fixed", "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-image 完全体 12.24_2003530439279165441.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image 完全体 12.24_2003530439279165441.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ZImageFunControlnet`
- `CLIPTextEncode` ★核心
- `AIO_Preprocessor`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `TilePreprocessor`
- `AILab_MaskEnhancer`
- `CLIPTextEncode` ★核心
- `ZImageFunControlnet`
- `KSampler` ★核心
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `ModelPatchLoader`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `KSamplerAdvanced` ★核心
- `ZImageFunControlnet`
- `ModelPatchLoader`
- `Fast Groups Bypasser (rgthree)`
- `Anything Everywhere3`
- `Anything Everywhere`
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1280`
- `height` = `1720`
- `batch_size` = `2`
- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `9`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `FlowMatchEulerDiscreteScheduler`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`VAEDecode`、`ZImageFunControlnet`、`CLIPTextEncode`、`AIO_Preprocessor`、`LoadImage`、`EmptyLatentImage`、`KSampler`、`TilePreprocessor`、`AILab_MaskEnhancer`、`ModelPatchLoader`、`VAEEncode`、`UpscaleModelLoader`、`KSamplerAdvanced`、`UnetLoaderGGUF`、`CLIPLoader`、`VAELoader`、`ImageUpscaleWithModel`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage、ZImageFunControlnet

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
