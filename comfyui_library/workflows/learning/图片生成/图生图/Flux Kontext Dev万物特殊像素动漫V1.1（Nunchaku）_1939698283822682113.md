---
key: 图片生成/图生图/Flux Kontext Dev万物特殊像素动漫V1.1（Nunchaku）_1939698283822682113.json
name: Flux Kontext Dev万物特殊像素动漫V1.1（Nunchaku）_1939698283822682113
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物特殊像素动漫V1.1（Nunchaku）_1939698283822682113.json
hash: 9b8d2597fd2ebe43
coverage: 0.875
learned_at: 2026-10-23 10:56:46
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, DualCLIPLoader, NunchakuFluxDiTLoader, EmptySD3LatentImage, KSampler, VAEDecode, SaveImage, ImageConcanate, SaveImage, GoogleTranslateTextNode, easy showAnything, NunchakuFluxLoraLoader, CR Prompt Text, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 442103818495666, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev万物特殊像素动漫V1.1（Nunchaku）_1939698283822682113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物特殊像素动漫V1.1（Nunchaku）_1939698283822682113.json`

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
- `FluxGuidance`
- `ReferenceLatent`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcanate`
- `SaveImage`
- `GoogleTranslateTextNode`
- `easy showAnything`
- `NunchakuFluxLoraLoader` ★核心
- `CR Prompt Text`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `442103818495666`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`ImageConcanate`、`GoogleTranslateTextNode`、`NunchakuFluxLoraLoader`、`CR Prompt Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
