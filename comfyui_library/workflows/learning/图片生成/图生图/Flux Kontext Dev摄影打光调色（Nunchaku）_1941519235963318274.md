---
key: 图片生成/图生图/Flux Kontext Dev摄影打光调色（Nunchaku）_1941519235963318274.json
name: Flux Kontext Dev摄影打光调色（Nunchaku）_1941519235963318274
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev摄影打光调色（Nunchaku）_1941519235963318274.json
hash: 4ba78b947b747ceb
coverage: 0.875
learned_at: 2026-10-23 10:57:11
nodes: [VAELoader, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, NunchakuFluxDiTLoader, EmptySD3LatentImage, VAEDecode, SaveImage, KSampler, SaveImage, ImageConcanate, ConditioningZeroOut, NunchakuFluxLoraLoader, CR Prompt Text, LoadImage, Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1113953482073894, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev摄影打光调色（Nunchaku）_1941519235963318274.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev摄影打光调色（Nunchaku）_1941519235963318274.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `VAELoader`
- `PreviewImage`
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
- `NunchakuFluxDiTLoader`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `SaveImage`
- `ImageConcanate`
- `ConditioningZeroOut`
- `NunchakuFluxLoraLoader` ★核心
- `CR Prompt Text`
- `LoadImage`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1113953482073894`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`VAELoader`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`EmptySD3LatentImage`、`VAEDecode`、`SaveImage`、`KSampler`、`ImageConcanate`、`ConditioningZeroOut`、`NunchakuFluxLoraLoader`、`CR Prompt Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
