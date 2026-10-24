---
key: 图片生成/图生图/Flux Kontext Dev手部修复（Nunchaku）_1941544818873102338.json
name: Flux Kontext Dev手部修复（Nunchaku）_1941544818873102338
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev手部修复（Nunchaku）_1941544818873102338.json
hash: 6e197df40ab4a2c1
coverage: 0.875
learned_at: 2026-10-23 10:57:10
nodes: [VAELoader, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, DualCLIPLoader, NunchakuFluxDiTLoader, EmptySD3LatentImage, VAEDecode, KSampler, SaveImage, ImageConcanate, ConditioningZeroOut, Note, GoogleTranslateTextNode, SaveImage, NunchakuFluxLoraLoader, LoadImage, CR Prompt Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 152469559375050, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev手部修复（Nunchaku）_1941544818873102338.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev手部修复（Nunchaku）_1941544818873102338.json`

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
- `DualCLIPLoader`
- `NunchakuFluxDiTLoader`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `ImageConcanate`
- `ConditioningZeroOut`
- `Note`
- `GoogleTranslateTextNode`
- `SaveImage`
- `NunchakuFluxLoraLoader` ★核心
- `LoadImage`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `152469559375050`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`VAELoader`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`DualCLIPLoader`、`NunchakuFluxDiTLoader`、`EmptySD3LatentImage`、`VAEDecode`、`KSampler`、`SaveImage`、`ImageConcanate`、`ConditioningZeroOut`、`GoogleTranslateTextNode`、`NunchakuFluxLoraLoader`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
