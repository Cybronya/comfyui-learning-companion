---
key: 图片生成/图生图/Z-Image姿势控制2.0+高清放大2K_2000726955454590978.json
name: Z-Image姿势控制2.0+高清放大2K_2000726955454590978
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image姿势控制2.0+高清放大2K_2000726955454590978.json
hash: 587a03c0588fe555
coverage: 0.875
learned_at: 2026-10-23 11:29:50
nodes: [CLIPLoader, ConditioningZeroOut, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, VAELoader, VAEDecode, PreviewImage, AIO_Preprocessor, LoadImage, EmptyLatentImage, CLIPTextEncode, Text, UNETLoader, LoraLoaderModelOnly, SeedVR2BlockSwap, SeedVR2ExtraArgs, VAEDecode, PreviewImage, SeedVR2, SaveImage, ModelPatchLoader, QwenImageDiffsynthControlnet, KSampler, KSampler]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.7000000000000002, "height": 1920, "sampler_name": "euler", "scheduler": "ddim_uniform", "seed": 969989929262987, "steps": 7, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Z-Image姿势控制2.0+高清放大2K_2000726955454590978.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image姿势控制2.0+高清放大2K_2000726955454590978.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `ConditioningZeroOut`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `VAELoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `AIO_Preprocessor`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `Text`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `VAEDecode` ★核心
- `PreviewImage`
- `SeedVR2`
- `SaveImage`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `KSampler` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `969989929262987`
- `steps` = `7`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `ddim_uniform`
- `denoise` = `0.7000000000000002`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`CLIPLoader`、`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`VAEDecode`、`AIO_Preprocessor`、`LoadImage`、`EmptyLatentImage`、`CLIPTextEncode`、`Text`、`UNETLoader`、`LoraLoaderModelOnly`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`SeedVR2`、`SaveImage`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
