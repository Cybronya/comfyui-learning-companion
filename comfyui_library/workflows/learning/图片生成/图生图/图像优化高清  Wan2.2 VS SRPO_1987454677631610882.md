---
key: 图片生成/图生图/图像优化高清  Wan2.2 VS SRPO_1987454677631610882.json
name: 图像优化高清  Wan2.2 VS SRPO_1987454677631610882
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像优化高清  Wan2.2 VS SRPO_1987454677631610882.json
hash: 455896b5aa3d9d0e
coverage: 0.891892
learned_at: 2026-10-23 12:38:04
nodes: [ConditioningZeroOut, UNETLoader, VAELoader, DualCLIPLoader, FluxGuidance, CLIPTextEncode, VAEEncode, CLIPLoader, UNETLoader, CLIPTextEncode, LoraLoader, Text Concatenate, PathchSageAttentionKJ, ModelSamplingSD3, VAEEncode, LoraLoaderModelOnly, LoraLoader, LoraLoader, VAELoader, KSampler, Text Multiline, ImageScaleToMegapixels, Image Comparer (rgthree), VAEDecode, PreviewImage, Float, PreviewImage, CLIPTextEncode, SaveImage, VAEDecode, Image Comparer (rgthree), LoadImage, SaveImage, KSampler, ImageScaleBy, ImageUpscaleWithModel, UpscaleModelLoader]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.3500000000000001, "lora_name": "WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v3_by-AI_Characters.safetensors", "sampler_name": "er_sde", "scheduler": "sgm_uniform", "seed": 7, "steps": 8, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/图像优化高清  Wan2.2 VS SRPO_1987454677631610882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像优化高清  Wan2.2 VS SRPO_1987454677631610882.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `Text Concatenate`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `VAELoader`
- `KSampler` ★核心
- `Text Multiline`
- `ImageScaleToMegapixels`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `PreviewImage`
- `Float`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `KSampler` ★核心
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `WAN2.2-LowNoise_SmartphoneSnapshotPhotoReality_v3_by-AI_Characters.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`
- `seed` = `7`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `sgm_uniform`
- `denoise` = `0.3500000000000001`

## 知识

覆盖率 **89%**（33/37）

**有卡**：`ConditioningZeroOut`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`FluxGuidance`、`CLIPTextEncode`、`VAEEncode`、`CLIPLoader`、`LoraLoader`、`Text Concatenate`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`KSampler`、`Text Multiline`、`ImageScaleToMegapixels`、`VAEDecode`、`Float`、`SaveImage`、`LoadImage`、`ImageScaleBy`、`ImageUpscaleWithModel`、`UpscaleModelLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
