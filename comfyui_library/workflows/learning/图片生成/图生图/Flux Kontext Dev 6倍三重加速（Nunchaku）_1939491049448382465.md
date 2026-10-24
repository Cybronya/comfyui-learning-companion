---
key: 图片生成/图生图/Flux Kontext Dev 6倍三重加速（Nunchaku）_1939491049448382465.json
name: Flux Kontext Dev 6倍三重加速（Nunchaku）_1939491049448382465
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev 6倍三重加速（Nunchaku）_1939491049448382465.json
hash: 98ef6f9ad856a3c7
coverage: 0.9
learned_at: 2026-10-23 10:56:26
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEDecode, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, EmptySD3LatentImage, DualCLIPLoader, ImageStitch, NunchakuFluxDiTLoader, CLIPTextEncode, GoogleTranslateTextNode, SaveImage, CR Prompt Text, LoadImage, KSampler]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 302211313548189, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev 6倍三重加速（Nunchaku）_1939491049448382465.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev 6倍三重加速（Nunchaku）_1939491049448382465.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `PreviewImage`
- `LoadImageOutput`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `EmptySD3LatentImage`
- `DualCLIPLoader`
- `ImageStitch`
- `NunchakuFluxDiTLoader`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `SaveImage`
- `CR Prompt Text`
- `LoadImage`
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `302211313548189`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEDecode`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`EmptySD3LatentImage`、`DualCLIPLoader`、`ImageStitch`、`NunchakuFluxDiTLoader`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`SaveImage`、`CR Prompt Text`、`LoadImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
