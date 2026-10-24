---
key: 图片生成/图生图/Flux Kontext万物Logo融合Place It加速版v1_1946420363637219330.json
name: Flux Kontext万物Logo融合Place It加速版v1_1946420363637219330
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext万物Logo融合Place It加速版v1_1946420363637219330.json
hash: 557a00a99f747ee0
coverage: 0.9
learned_at: 2026-10-23 10:57:40
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, VAEDecode, UnetLoaderGGUF, FluxKontextImageScale, PDIMAGE_LongerSize, SaveImage, ImageConcanate, TeaCache, SaveImage, LoraLoaderModelOnly, FastCanvasTool, PreviewImage, RMBG, LoadImage, LoadImage, CR Prompt Text, TTP_Expand_And_Mask, FastCanvas, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 20396176493490, "steps": 21}
---

# 图片生成/图生图/Flux Kontext万物Logo融合Place It加速版v1_1946420363637219330.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext万物Logo融合Place It加速版v1_1946420363637219330.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `PreviewImage`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `UnetLoaderGGUF` ★核心
- `FluxKontextImageScale`
- `PDIMAGE_LongerSize`
- `SaveImage`
- `ImageConcanate`
- `TeaCache`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `FastCanvasTool`
- `PreviewImage`
- `RMBG`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `TTP_Expand_And_Mask`
- `FastCanvas`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `20396176493490`
- `steps` = `21`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（27/30）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`VAEDecode`、`UnetLoaderGGUF`、`FluxKontextImageScale`、`PDIMAGE_LongerSize`、`SaveImage`、`ImageConcanate`、`TeaCache`、`LoraLoaderModelOnly`、`FastCanvasTool`、`RMBG`、`LoadImage`、`CR Prompt Text`、`TTP_Expand_And_Mask`、`FastCanvas`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
