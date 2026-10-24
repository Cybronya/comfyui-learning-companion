---
key: 图片生成/图生图/Flux Kontext Dev万物移除新remove加速版V3_1941717646519988225.json
name: Flux Kontext Dev万物移除新remove加速版V3_1941717646519988225
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物移除新remove加速版V3_1941717646519988225.json
hash: 4ab445902f8b2937
coverage: 0.913043
learned_at: 2026-10-23 10:56:48
nodes: [VAELoader, ConditioningZeroOut, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, VAEDecode, SaveImage, SaveImage, MagCache, UnetLoaderGGUF, KSampler, LoraLoaderModelOnly, LoadImage, CR Prompt Text, ImageConcanate, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 654083301602961, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev万物移除新remove加速版V3_1941717646519988225.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物移除新remove加速版V3_1941717646519988225.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `MagCache`
- `UnetLoaderGGUF` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CR Prompt Text`
- `ImageConcanate`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `654083301602961`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`MagCache`、`UnetLoaderGGUF`、`KSampler`、`LoraLoaderModelOnly`、`LoadImage`、`CR Prompt Text`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
