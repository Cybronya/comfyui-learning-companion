---
key: 图片生成/图生图/Flux-kontext-dev+nunchaku 图像编辑极速版_1939984148310454273.json
name: Flux-kontext-dev+nunchaku 图像编辑极速版_1939984148310454273
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux-kontext-dev+nunchaku 图像编辑极速版_1939984148310454273.json
hash: fce59764cf6760e0
coverage: 0.821429
learned_at: 2026-10-23 10:58:35
nodes: [NunchakuFluxDiTLoader, ReferenceLatent, FluxGuidance, ConditioningZeroOut, VAEDecode, SaveImage, KSampler, Image Comparer (rgthree), PreviewImage, ImageUpscaleWithModel, VAEEncode, Fast Bypasser (rgthree), Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), MarkdownNote, easy int, LoadImageOutput, LayerUtility: ImageScaleByAspectRatio V2, GoogleTranslateTextNode, CLIPTextEncode, ImageStitch, LoadImage, DualCLIPLoader, VAELoader, NunchakuFluxLoraLoader, UpscaleModelLoader, CR Prompt Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 807461519172526, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux-kontext-dev+nunchaku 图像编辑极速版_1939984148310454273.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux-kontext-dev+nunchaku 图像编辑极速版_1939984148310454273.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `NunchakuFluxDiTLoader`
- `ReferenceLatent`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `ImageUpscaleWithModel`
- `VAEEncode` ★核心
- `Fast Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `easy int`
- `LoadImageOutput`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GoogleTranslateTextNode`
- `CLIPTextEncode` ★核心
- `ImageStitch`
- `LoadImage`
- `DualCLIPLoader`
- `VAELoader`
- `NunchakuFluxLoraLoader` ★核心
- `UpscaleModelLoader`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `807461519172526`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（23/28）

**有卡**：`NunchakuFluxDiTLoader`、`ReferenceLatent`、`FluxGuidance`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`KSampler`、`ImageUpscaleWithModel`、`VAEEncode`、`Fast Bypasser (rgthree)`、`easy int`、`LoadImageOutput`、`LayerUtility: ImageScaleByAspectRatio V2`、`GoogleTranslateTextNode`、`CLIPTextEncode`、`ImageStitch`、`LoadImage`、`DualCLIPLoader`、`VAELoader`、`NunchakuFluxLoraLoader`、`UpscaleModelLoader`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
