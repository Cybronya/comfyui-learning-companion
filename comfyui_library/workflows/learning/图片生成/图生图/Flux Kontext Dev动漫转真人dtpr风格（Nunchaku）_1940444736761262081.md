---
key: 图片生成/图生图/Flux Kontext Dev动漫转真人dtpr风格（Nunchaku）_1940444736761262081.json
name: Flux Kontext Dev动漫转真人dtpr风格（Nunchaku）_1940444736761262081
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev动漫转真人dtpr风格（Nunchaku）_1940444736761262081.json
hash: 64d5e7e73e50c35c
coverage: 0.875
learned_at: 2026-10-23 10:56:59
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, NunchakuFluxDiTLoader, EmptySD3LatentImage, KSampler, VAEDecode, SaveImage, ImageConcanate, LoadImage, FluxGuidance, NunchakuFluxLoraLoader, SaveImage, Note, CR Prompt Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 421903868938228, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev动漫转真人dtpr风格（Nunchaku）_1940444736761262081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev动漫转真人dtpr风格（Nunchaku）_1940444736761262081.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `PreviewImage`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `MarkdownNote`
- `ReferenceLatent`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcanate`
- `LoadImage`
- `FluxGuidance`
- `NunchakuFluxLoraLoader` ★核心
- `SaveImage`
- `Note`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `421903868938228`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`ImageConcanate`、`LoadImage`、`FluxGuidance`、`NunchakuFluxLoraLoader`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
