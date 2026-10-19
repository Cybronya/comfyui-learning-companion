---
key: 图片生成/文生图/Z-Image-Turbo-Controlnet2 + Inpaint_2002209734201622530.json
name: Z-Image-Turbo-Controlnet2 + Inpaint_2002209734201622530
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image-Turbo-Controlnet2 + Inpaint_2002209734201622530.json
hash: 1f1d3b1e18191c65
coverage: 0.771429
learned_at: 2026-10-19 21:47:01
nodes: [ModelSamplingAuraFlow, EmptySD3LatentImage, UNETLoader, VAELoader, ModelPatchLoader, ConditioningZeroOut, GetImageSize, ZImageFunControlnet, DifferentialDiffusion, KSampler, KSampler, VAEDecode, PreviewImage, ImageScaleBy, VAEEncode, Reroute, Image Comparer (rgthree), UpscaleModelLoader, UltimateSDUpscale, PreviewImage, GetImageSizeAndCount, Image Comparer (rgthree), SeedVR2VideoUpscaler, PreviewImage, SeedVR2LoadVAEModel, Image Comparer (rgthree), CLIPLoader, LoadImage, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, SeedVR2LoadDiTModel, PreviewImage, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.5, "sampler_name": "res_2s", "scheduler": "beta57", "seed": 239843452509997, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Z-Image-Turbo-Controlnet2 + Inpaint_2002209734201622530.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image-Turbo-Controlnet2 + Inpaint_2002209734201622530.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `ModelSamplingAuraFlow`
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `VAELoader`
- `ModelPatchLoader`
- `ConditioningZeroOut`
- `GetImageSize`
- `ZImageFunControlnet`
- `DifferentialDiffusion`
- `KSampler` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `ImageScaleBy`
- `VAEEncode` ★核心
- `Reroute`
- `Image Comparer (rgthree)`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `PreviewImage`
- `GetImageSizeAndCount`
- `Image Comparer (rgthree)`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SeedVR2LoadDiTModel`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `239843452509997`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `res_2s`
- `scheduler` = `beta57`
- `denoise` = `0.5`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`ModelSamplingAuraFlow`、`EmptySD3LatentImage`、`UNETLoader`、`VAELoader`、`ModelPatchLoader`、`ConditioningZeroOut`、`GetImageSize`、`ZImageFunControlnet`、`DifferentialDiffusion`、`KSampler`、`VAEDecode`、`ImageScaleBy`、`VAEEncode`、`UpscaleModelLoader`、`UltimateSDUpscale`、`GetImageSizeAndCount`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`CLIPLoader`、`LoadImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`SeedVR2LoadDiTModel`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
