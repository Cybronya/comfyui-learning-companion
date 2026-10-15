---
key: 图片生成/文生图/Qwen Image edit 2509 + Nunchaku + SRPO 高清去AI感工作流  课程对应流程_1971577017105838081.json
name: Qwen Image edit 2509 + Nunchaku + SRPO 高清去AI感工作流  课程对应流程_1971577017105838081
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image edit 2509 + Nunchaku + SRPO 高清去AI感工作流  课程对应流程_1971577017105838081.json
hash: 694e2cb18138903c
coverage: 0.666667
learned_at: 2026-10-15 22:27:04
nodes: [Image Comparer (rgthree), PreviewImage, FluxGuidance, ModelSamplingFlux, Seed (rgthree), Image Comparer (rgthree), Note, VAELoader, Note, easy cleanGpuUsed, ConditioningZeroOut, MarkdownNote, LoadImage, ImageScaleToTotalPixels, DualCLIPLoader, CR SDXL Aspect Ratio, VAEEncode, GetNode, Reroute, Upscale Model Loader, LoraLoaderModelOnly, CFGNorm, SetNode, UnetLoaderGGUF, SimpleMath+, SimpleMath+, CLIPTextEncode, PreviewImage, VAEEncode, EmptySD3LatentImage, MarkdownNote, TextEncodeQwenImageEditPlus, Note, ModelSamplingAuraFlow, UnetLoaderGGUF, LoraLoaderModelOnly, MarkdownNote, TextEncodeQwenImageEditPlus, CLIPLoader, VAELoader, Note, LoadImage, UNETLoader, LoraLoaderModelOnly, CR Text, NunchakuQwenImageDiTLoader, MarkdownNote, KSampler, UltimateSDUpscale, Note, ImageScaleBy, KSampler, Note, LoadImage, VAEDecode, VAEDecode, PreviewImage, SaveImage, PreviewImage, Note]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.10000000000000002, "sampler_name": "euler", "scheduler": "beta", "seed": 966283409977494, "steps": 30}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image edit 2509 + Nunchaku + SRPO 高清去AI感工作流  课程对应流程_1971577017105838081.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image edit 2509 + Nunchaku + SRPO 高清去AI感工作流  课程对应流程_1971577017105838081.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
- `Image Comparer (rgthree)`
- `PreviewImage`
- `FluxGuidance`
- `ModelSamplingFlux`
- `Seed (rgthree)`
- `Image Comparer (rgthree)`
- `Note`
- `VAELoader`
- `Note`
- `easy cleanGpuUsed`
- `ConditioningZeroOut`
- `MarkdownNote`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `DualCLIPLoader`
- `CR SDXL Aspect Ratio`
- `VAEEncode` ★核心
- `GetNode`
- `Reroute`
- `Upscale Model Loader`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `SetNode`
- `UnetLoaderGGUF` ★核心
- `SimpleMath+`
- `SimpleMath+`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `MarkdownNote`
- `TextEncodeQwenImageEditPlus`
- `Note`
- `ModelSamplingAuraFlow`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `TextEncodeQwenImageEditPlus`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CR Text`
- `NunchakuQwenImageDiTLoader`
- `MarkdownNote`
- `KSampler` ★核心
- `UltimateSDUpscale`
- `Note`
- `ImageScaleBy`
- `KSampler` ★核心
- `Note`
- `LoadImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `PreviewImage`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `966283409977494`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **67%**（40/60）

**有卡**：`FluxGuidance`、`ModelSamplingFlux`、`Seed (rgthree)`、`VAELoader`、`easy cleanGpuUsed`、`ConditioningZeroOut`、`LoadImage`、`ImageScaleToTotalPixels`、`DualCLIPLoader`、`CR SDXL Aspect Ratio`、`VAEEncode`、`Upscale Model Loader`、`LoraLoaderModelOnly`、`CFGNorm`、`UnetLoaderGGUF`、`SimpleMath+`、`CLIPTextEncode`、`EmptySD3LatentImage`、`TextEncodeQwenImageEditPlus`、`ModelSamplingAuraFlow`、`CLIPLoader`、`UNETLoader`、`CR Text`、`NunchakuQwenImageDiTLoader`、`KSampler`、`UltimateSDUpscale`、`ImageScaleBy`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
