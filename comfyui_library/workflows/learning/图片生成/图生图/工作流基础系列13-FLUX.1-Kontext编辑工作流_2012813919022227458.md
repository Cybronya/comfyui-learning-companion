---
key: 图片生成/图生图/工作流基础系列13-FLUX.1-Kontext编辑工作流_2012813919022227458.json
name: 工作流基础系列13-FLUX.1-Kontext编辑工作流_2012813919022227458
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/工作流基础系列13-FLUX.1-Kontext编辑工作流_2012813919022227458.json
hash: f658d9fb94a5e943
coverage: 0.794118
learned_at: 2026-10-23 12:50:26
nodes: [MarkdownNote, LoadImage, FluxKontextImageScale, PreviewImage, FluxGuidance, LayerUtility: GetImageSize, VAEEncode, MarkdownNote, easy promptList, Note, VAEEncode, ReferenceLatent, LoraLoaderModelOnly, easy promptList, ImageScaleToTotalPixels, ImageStitch, PreviewImage, UNETLoader, VAELoader, DualCLIPLoader, CLIPTextEncode, ConditioningZeroOut, Seed (rgthree), KSampler, EmptySD3LatentImage, FluxKontextImageScale, PreviewImage, LoadImage, LoadImage, LoadImage, ImageScaleToTotalPixels, Image Comparer (rgthree), VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 667894466279507, "steps": 20}
---

# 图片生成/图生图/工作流基础系列13-FLUX.1-Kontext编辑工作流_2012813919022227458.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/工作流基础系列13-FLUX.1-Kontext编辑工作流_2012813919022227458.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `MarkdownNote`
- `LoadImage`
- `FluxKontextImageScale`
- `PreviewImage`
- `FluxGuidance`
- `LayerUtility: GetImageSize`
- `VAEEncode` ★核心
- `MarkdownNote`
- `easy promptList`
- `Note`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LoraLoaderModelOnly` ★核心
- `easy promptList`
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `PreviewImage`
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `Seed (rgthree)`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `FluxKontextImageScale`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `667894466279507`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（27/34）

**有卡**：`LoadImage`、`FluxKontextImageScale`、`FluxGuidance`、`LayerUtility: GetImageSize`、`VAEEncode`、`easy promptList`、`ReferenceLatent`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`ImageStitch`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`Seed (rgthree)`、`KSampler`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
