---
key: 图片生成/图生图/Flux Kontext万物迁移Put it here加速版v1_1946742400083746817.json
name: Flux Kontext万物迁移Put it here加速版v1_1946742400083746817
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext万物迁移Put it here加速版v1_1946742400083746817.json
hash: 01b2f1cd71272328
coverage: 0.903226
learned_at: 2026-10-23 10:57:44
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, VAEDecode, UnetLoaderGGUF, FluxKontextImageScale, SaveImage, ImageConcanate, SaveImage, KSampler, FastCanvasTool, LoadImage, LoadImage, PreviewImage, RMBG, ImageCropper, TTP_Expand_And_Mask, PDIMAGE_LongerSize, LoraLoaderModelOnly, CR Prompt Text, FastCanvas, TeaCache]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 764521395251108, "steps": 20}
---

# 图片生成/图生图/Flux Kontext万物迁移Put it here加速版v1_1946742400083746817.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext万物迁移Put it here加速版v1_1946742400083746817.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
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
- `SaveImage`
- `ImageConcanate`
- `SaveImage`
- `KSampler` ★核心
- `FastCanvasTool`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `RMBG`
- `ImageCropper`
- `TTP_Expand_And_Mask`
- `PDIMAGE_LongerSize`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `FastCanvas`
- `TeaCache`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `764521395251108`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`VAEDecode`、`UnetLoaderGGUF`、`FluxKontextImageScale`、`SaveImage`、`ImageConcanate`、`KSampler`、`FastCanvasTool`、`LoadImage`、`RMBG`、`ImageCropper`、`TTP_Expand_And_Mask`、`PDIMAGE_LongerSize`、`LoraLoaderModelOnly`、`CR Prompt Text`、`FastCanvas`、`TeaCache`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
