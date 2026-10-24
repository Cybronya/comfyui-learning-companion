---
key: 图片生成/图生图/Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_2011984571679645698.json
name: Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_2011984571679645698
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_2011984571679645698.json
hash: bc9edf2362df5638
coverage: 0.95122
learned_at: 2026-10-23 11:28:18
nodes: [Primitive integer [Crystools], GetImageSizeAndCount, ImageScaleDownToSize, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, LoraLoaderModelOnly, UNETLoader, easy anythingIndexSwitch, PreviewImage, Primitive integer [Crystools], Primitive integer [Crystools], LoraLoaderModelOnly, ModelSamplingSD3, CLIPTextEncode, CLIPTextEncode, VAELoader, ModelSamplingSD3, CLIPLoader, Text Concatenate, VAEDecode, VAEDecode, Text Multiline, VAEDecode, KSamplerAdvanced, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, DuckHideNode, SaveImage, VAEEncode, easy anythingIndexSwitch, DuckHideNode, easy showAnything, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, UNETLoader, Text Multiline, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 12, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "enable", "steps": "randomize"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_2011984571679645698.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2单帧图像生成洗图（一高噪二低噪）+SeedVR2 Video Upscaler_2011984571679645698.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `Primitive integer [Crystools]`
- `GetImageSizeAndCount`
- `ImageScaleDownToSize`
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `easy anythingIndexSwitch`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ModelSamplingSD3`
- `CLIPLoader`
- `Text Concatenate`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Text Multiline`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `DuckHideNode`
- `SaveImage`
- `VAEEncode` ★核心
- `easy anythingIndexSwitch`
- `DuckHideNode`
- `easy showAnything`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `Text Multiline`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **95%**（39/41）

**有卡**：`Primitive integer [Crystools]`、`GetImageSizeAndCount`、`ImageScaleDownToSize`、`EmptyHunyuanLatentVideo`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`UNETLoader`、`easy anythingIndexSwitch`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`Text Concatenate`、`VAEDecode`、`Text Multiline`、`KSamplerAdvanced`、`KSampler`、`DuckHideNode`、`SaveImage`、`VAEEncode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
