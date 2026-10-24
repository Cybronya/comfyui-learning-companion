---
key: 图片生成/图生图/Flux Kontext Dev鱿鱼游戏123木头人加速版v1.5_1943615112152576001.json
name: Flux Kontext Dev鱿鱼游戏123木头人加速版v1.5_1943615112152576001
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev鱿鱼游戏123木头人加速版v1.5_1943615112152576001.json
hash: d62e052614234ca6
coverage: 0.916667
learned_at: 2026-10-23 10:57:21
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, DualCLIPLoader, VAEDecode, MagCache, UnetLoaderGGUF, FluxKontextImageScale, KSampler, PDIMAGE_LongerSize, SaveImage, SaveImage, ImageConcanate, LoraLoaderModelOnly, GoogleTranslateTextNode, LoadImage, CR Prompt Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 335237233178702, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev鱿鱼游戏123木头人加速版v1.5_1943615112152576001.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev鱿鱼游戏123木头人加速版v1.5_1943615112152576001.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
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
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `MagCache`
- `UnetLoaderGGUF` ★核心
- `FluxKontextImageScale`
- `KSampler` ★核心
- `PDIMAGE_LongerSize`
- `SaveImage`
- `SaveImage`
- `ImageConcanate`
- `LoraLoaderModelOnly` ★核心
- `GoogleTranslateTextNode`
- `LoadImage`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `335237233178702`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`DualCLIPLoader`、`VAEDecode`、`MagCache`、`UnetLoaderGGUF`、`FluxKontextImageScale`、`KSampler`、`PDIMAGE_LongerSize`、`SaveImage`、`ImageConcanate`、`LoraLoaderModelOnly`、`GoogleTranslateTextNode`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage
