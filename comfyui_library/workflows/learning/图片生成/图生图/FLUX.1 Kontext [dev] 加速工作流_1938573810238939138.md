---
key: 图片生成/图生图/FLUX.1 Kontext [dev] 加速工作流_1938573810238939138.json
name: FLUX.1 Kontext [dev] 加速工作流_1938573810238939138
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1 Kontext [dev] 加速工作流_1938573810238939138.json
hash: 924344f892340ca7
coverage: 0.846154
learned_at: 2026-10-23 10:53:58
nodes: [VAELoader, DualCLIPLoader, ConditioningZeroOut, VAEDecode, FluxGuidance, ReferenceLatent, easy cleanGpuUsed, PreviewImage, SaveImage, easy cleanGpuUsed, MarkdownNote, VAEEncode, EmptySD3LatentImage, GetImageSize, ImageScaleToTotalPixels, FluxKontextImageScale, KSampler, ImageStitch, LoraLoaderModelOnly, UnetLoaderGGUF, UNETLoader, MarkdownNote, Note, LoadImage, LoadImage, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 678598894545183, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.1 Kontext [dev] 加速工作流_1938573810238939138.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1 Kontext [dev] 加速工作流_1938573810238939138.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAELoader`
- `DualCLIPLoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `FluxGuidance`
- `ReferenceLatent`
- `easy cleanGpuUsed`
- `PreviewImage`
- `SaveImage`
- `easy cleanGpuUsed`
- `MarkdownNote`
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `FluxKontextImageScale`
- `KSampler` ★核心
- `ImageStitch`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `MarkdownNote`
- `Note`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `678598894545183`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（22/26）

**有卡**：`VAELoader`、`DualCLIPLoader`、`ConditioningZeroOut`、`VAEDecode`、`FluxGuidance`、`ReferenceLatent`、`easy cleanGpuUsed`、`SaveImage`、`VAEEncode`、`EmptySD3LatentImage`、`GetImageSize`、`ImageScaleToTotalPixels`、`FluxKontextImageScale`、`KSampler`、`ImageStitch`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`UNETLoader`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
