---
key: 图片生成/图生图/小红书 FireRed-V1.1虚拟换装_2041129593666539522.json
name: 小红书 FireRed-V1.1虚拟换装_2041129593666539522
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/小红书 FireRed-V1.1虚拟换装_2041129593666539522.json
hash: 61d487f080bea404
coverage: 0.886364
learned_at: 2026-10-23 12:49:01
nodes: [SeedVR2LoadVAEModel, easy imageSizeBySide, LoraLoaderModelOnly, SaveImage, SeedVR2VideoUpscaler, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, CLIPLoader, VAELoader, VAEDecode, Image Comparer (rgthree), ConditioningZeroOut, UNETLoader, VAELoader, TTResolutionSelector, ConditioningZeroOut, EmptyLatentImage, KSampler, VAEDecode, SaveImage, KSampler, LoraLoaderModelOnly, SeedVR2LoadDiTModel, Image Comparer (rgthree), Fast Groups Bypasser (rgthree), Text, Note, Note, LoadImage, LoadImage, LoadImage, UNETLoader, UNETLoader, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, ImageResize+, ImageResize+, LoadImage, Text]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "beta", "seed": 639098830096611, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/小红书 FireRed-V1.1虚拟换装_2041129593666539522.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/小红书 FireRed-V1.1虚拟换装_2041129593666539522.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `SeedVR2LoadVAEModel`
- `easy imageSizeBySide`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `VAELoader`
- `TTResolutionSelector`
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `SeedVR2LoadDiTModel`
- `Image Comparer (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Text`
- `Note`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ImageResize+`
- `ImageResize+`
- `LoadImage`
- `Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `639098830096611`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（39/44）

**有卡**：`SeedVR2LoadVAEModel`、`easy imageSizeBySide`、`LoraLoaderModelOnly`、`SaveImage`、`SeedVR2VideoUpscaler`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`ConditioningZeroOut`、`UNETLoader`、`TTResolutionSelector`、`EmptyLatentImage`、`KSampler`、`SeedVR2LoadDiTModel`、`Text`、`LoadImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`ImageResize+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
