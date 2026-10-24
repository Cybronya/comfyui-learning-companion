---
key: 图片生成/图生图/Flux Kontext Dev Nunchaku 加速_1939859280994734082.json
name: Flux Kontext Dev Nunchaku 加速_1939859280994734082
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev Nunchaku 加速_1939859280994734082.json
hash: aa0af155061ba8b9
coverage: 0.85
learned_at: 2026-10-23 10:56:26
nodes: [VAELoader, ConditioningZeroOut, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, DualCLIPLoader, ImageStitch, NunchakuFluxDiTLoader, CLIPTextEncode, GoogleTranslateTextNode, VAEEncode, KSampler, VAEDecode, Note, LoadImage, LoadImageOutput, SaveImage, CR Prompt Text, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 157739065932023, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev Nunchaku 加速_1939859280994734082.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev Nunchaku 加速_1939859280994734082.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `FluxKontextImageScale`
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `DualCLIPLoader`
- `ImageStitch`
- `NunchakuFluxDiTLoader`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Note`
- `LoadImage`
- `LoadImageOutput`
- `SaveImage`
- `CR Prompt Text`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `157739065932023`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`DualCLIPLoader`、`ImageStitch`、`NunchakuFluxDiTLoader`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`VAEEncode`、`KSampler`、`VAEDecode`、`LoadImage`、`LoadImageOutput`、`SaveImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
