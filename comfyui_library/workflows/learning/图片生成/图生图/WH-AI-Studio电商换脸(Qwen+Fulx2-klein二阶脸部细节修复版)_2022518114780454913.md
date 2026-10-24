---
key: 图片生成/图生图/WH-AI-Studio电商换脸(Qwen+Fulx2-klein二阶脸部细节修复版)_2022518114780454913.json
name: WH-AI-Studio电商换脸(Qwen+Fulx2-klein二阶脸部细节修复版)_2022518114780454913
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WH-AI-Studio电商换脸(Qwen+Fulx2-klein二阶脸部细节修复版)_2022518114780454913.json
hash: 840f15b76ecb4a49
coverage: 0.890909
learned_at: 2026-10-23 11:27:41
nodes: [EmptyLatentImage, ImpactSwitch, CLIPLoader, ConditioningZeroOut, FluxKontextImageScale, easy imageConcat, FluxKontextImageScale, VAELoader, UNETLoader, LoraLoaderModelOnly, PreviewImage, Load RetinaFace, MaskColorize, LayerMask: PersonMaskUltra V2, CLIPLoader, VAELoader, easy imageConcat, VAEDecode, UNETLoader, CLIPTextEncode, ConditioningZeroOut, ReferenceLatent, VAEEncode, VAEEncode, ReferenceLatent, ReferenceLatent, ImageConcanate, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, SaveImage, SaveImage, JWFloat, RandomNoise, ReferenceLatent, Flux2Scheduler, ImageConcanate, PreviewImage, GetImage, SaveImage, PreviewImage, Crop Face, ImageScaleToTotalPixels, ImageScaleToTotalPixels, easy cleanGpuUsed, VAEDecode, ImpactSwitch, TextEncodeQwenImageEditPlusAdvance_lrzjason, MarkdownNote, CR Text, LoadImage, LoadImage, CR Text, KSampler, LoadImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1.5, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 155720747961293, "steps": 8, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/WH-AI-Studio电商换脸(Qwen+Fulx2-klein二阶脸部细节修复版)_2022518114780454913.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WH-AI-Studio电商换脸(Qwen+Fulx2-klein二阶脸部细节修复版)_2022518114780454913.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `EmptyLatentImage` ★核心
- `ImpactSwitch`
- `CLIPLoader`
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `easy imageConcat`
- `FluxKontextImageScale`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `Load RetinaFace`
- `MaskColorize`
- `LayerMask: PersonMaskUltra V2`
- `CLIPLoader`
- `VAELoader`
- `easy imageConcat`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ImageConcanate`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `SaveImage`
- `JWFloat`
- `RandomNoise`
- `ReferenceLatent`
- `Flux2Scheduler`
- `ImageConcanate`
- `PreviewImage`
- `GetImage`
- `SaveImage`
- `PreviewImage`
- `Crop Face`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ImpactSwitch`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `MarkdownNote`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `KSampler` ★核心
- `LoadImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `155720747961293`
- `steps` = `8`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（49/55）

**有卡**：`EmptyLatentImage`、`CLIPLoader`、`ConditioningZeroOut`、`FluxKontextImageScale`、`easy imageConcat`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`Load RetinaFace`、`MaskColorize`、`LayerMask: PersonMaskUltra V2`、`VAEDecode`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`ImageConcanate`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`SaveImage`、`JWFloat`、`RandomNoise`、`Flux2Scheduler`、`GetImage`、`Crop Face`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`CR Text`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
