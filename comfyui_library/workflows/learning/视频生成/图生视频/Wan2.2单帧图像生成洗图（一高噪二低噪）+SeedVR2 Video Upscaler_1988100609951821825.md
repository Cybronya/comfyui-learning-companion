---
key: 视频生成/图生视频/Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_1988100609951821825.json
name: Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_1988100609951821825.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1988100609951821825.json
hash: b671ecafec19dfdd
coverage: 0.897959
learned_at: 2026-10-15 22:33:01
nodes: [UNETLoader, KSamplerAdvanced, Primitive integer [Crystools], GetImageSizeAndCount, ImageScaleDownToSize, EmptyHunyuanLatentVideo, VAEEncode, easy anythingIndexSwitch, LoraLoaderModelOnly, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, easy anythingIndexSwitch, LoraLoaderModelOnly, PreviewImage, VAEDecode, Primitive integer [Crystools], Primitive integer [Crystools], Text Multiline, LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, VAELoader, LoraLoaderModelOnly, VAEDecode, KSamplerAdvanced, PathchSageAttentionKJ, ModelSamplingSD3, LoraLoaderModelOnly, CR Simple Image Compare, VAEDecode, ImageSharpen, KSampler, PreviewImage, EsesImageEffectBloom, SeedVR2ExtraArgs, SeedVR2BlockSwap, SaveImage, LoadImage, CLIPLoader, Text Concatenate, ImageScaleToTotalPixels, PreviewImage, SeedVR2GGUF, BetterFilmGrain, PreviewImage, AILab_QwenVL, easy showAnything]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1.02, "denoise": 0.10000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 114558263660987, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_1988100609951821825.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1988100609951821825.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `Primitive integer [Crystools]`
- `GetImageSizeAndCount`
- `ImageScaleDownToSize`
- `EmptyHunyuanLatentVideo`
- `VAEEncode` ★核心
- `easy anythingIndexSwitch`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `easy anythingIndexSwitch`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `CR Simple Image Compare`
- `VAEDecode` ★核心
- `ImageSharpen`
- `KSampler` ★核心
- `PreviewImage`
- `EsesImageEffectBloom`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `SaveImage`
- `LoadImage`
- `CLIPLoader`
- `Text Concatenate`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `SeedVR2GGUF`
- `BetterFilmGrain`
- `PreviewImage`
- `AILab_QwenVL`
- `easy showAnything`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `114558263660987`
- `steps` = `8`
- `cfg` = `1.02`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **90%**（44/49）

**有卡**：`UNETLoader`、`KSamplerAdvanced`、`Primitive integer [Crystools]`、`GetImageSizeAndCount`、`ImageScaleDownToSize`、`EmptyHunyuanLatentVideo`、`VAEEncode`、`easy anythingIndexSwitch`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`VAEDecode`、`Text Multiline`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`CR Simple Image Compare`、`ImageSharpen`、`KSampler`、`EsesImageEffectBloom`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`SaveImage`、`LoadImage`、`CLIPLoader`、`Text Concatenate`、`ImageScaleToTotalPixels`、`SeedVR2GGUF`、`BetterFilmGrain`、`AILab_QwenVL`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
