---
key: 图片生成/图生图/A3、万物迁移F.1版本 - 和风_1990399537883865089.json
name: A3、万物迁移F.1版本 - 和风_1990399537883865089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/A3、万物迁移F.1版本 - 和风_1990399537883865089.json
hash: fc03caabbd38aff7
coverage: 0.947368
learned_at: 2026-10-23 10:50:09
nodes: [EmptyImage, easy imageSize, ImageToMask, ImageScaleToTotalPixels, ImageScaleToTotalPixels, easy imageConcat, easy imageConcat, easy imageSize, easy imageSize, VAEDecode, easy imageSize, ImageCrop, ImageScale, JWFloat, DifferentialDiffusion, LoraLoaderModelOnly, UnetLoaderGGUF, MaskToImage, MarkdownNote, LoadImage, SaveImage, LoadImage, MarkdownNote, ACE_TextTranslate, DualCLIPLoaderGGUF, FluxGuidance, CLIPTextEncode, CLIPVisionLoader, StyleModelLoader, LoraLoaderModelOnly, ReduxAdvanced, InpaintModelConditioning, KSampler, LayerUtility: CropByMask V2, LayerUtility: NumberCalculator, LayerUtility: RestoreCropBox, VAELoader, ConditioningZeroOut]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "sgm_uniform", "seed": 734107396715566, "steps": 9}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/A3、万物迁移F.1版本 - 和风_1990399537883865089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/A3、万物迁移F.1版本 - 和风_1990399537883865089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `EmptyImage`
- `easy imageSize`
- `ImageToMask`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `easy imageConcat`
- `easy imageConcat`
- `easy imageSize`
- `easy imageSize`
- `VAEDecode` ★核心
- `easy imageSize`
- `ImageCrop`
- `ImageScale`
- `JWFloat`
- `DifferentialDiffusion`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `MaskToImage`
- `MarkdownNote`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `MarkdownNote`
- `ACE_TextTranslate`
- `DualCLIPLoaderGGUF`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPVisionLoader`
- `StyleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `ReduxAdvanced`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `LayerUtility: CropByMask V2`
- `LayerUtility: NumberCalculator`
- `LayerUtility: RestoreCropBox`
- `VAELoader`
- `ConditioningZeroOut`

## 关键参数

- `seed` = `734107396715566`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **95%**（36/38）

**有卡**：`EmptyImage`、`easy imageSize`、`ImageToMask`、`ImageScaleToTotalPixels`、`easy imageConcat`、`VAEDecode`、`ImageCrop`、`ImageScale`、`JWFloat`、`DifferentialDiffusion`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`MaskToImage`、`LoadImage`、`SaveImage`、`ACE_TextTranslate`、`DualCLIPLoaderGGUF`、`FluxGuidance`、`CLIPTextEncode`、`CLIPVisionLoader`、`StyleModelLoader`、`ReduxAdvanced`、`InpaintModelConditioning`、`KSampler`、`LayerUtility: CropByMask V2`、`LayerUtility: NumberCalculator`、`LayerUtility: RestoreCropBox`、`VAELoader`、`ConditioningZeroOut`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
