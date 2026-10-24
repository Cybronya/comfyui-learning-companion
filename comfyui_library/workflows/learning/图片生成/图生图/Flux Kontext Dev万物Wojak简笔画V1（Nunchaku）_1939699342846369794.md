---
key: 图片生成/图生图/Flux Kontext Dev万物Wojak简笔画V1（Nunchaku）_1939699342846369794.json
name: Flux Kontext Dev万物Wojak简笔画V1（Nunchaku）_1939699342846369794
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物Wojak简笔画V1（Nunchaku）_1939699342846369794.json
hash: 3758337490bc0ea3
coverage: 0.913043
learned_at: 2026-10-23 10:56:39
nodes: [VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, NunchakuFluxDiTLoader, EmptySD3LatentImage, KSampler, VAEDecode, SaveImage, ImageConcanate, LoadImage, DualCLIPLoader, NunchakuFluxLoraLoader, CR Prompt Text, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 648778107668343, "steps": 20}
---

# 图片生成/图生图/Flux Kontext Dev万物Wojak简笔画V1（Nunchaku）_1939699342846369794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物Wojak简笔画V1（Nunchaku）_1939699342846369794.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
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
- `GoogleTranslateTextNode`
- `NunchakuFluxDiTLoader`
- `EmptySD3LatentImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcanate`
- `LoadImage`
- `DualCLIPLoader`
- `NunchakuFluxLoraLoader` ★核心
- `CR Prompt Text`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `648778107668343`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`NunchakuFluxDiTLoader`、`EmptySD3LatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`ImageConcanate`、`LoadImage`、`DualCLIPLoader`、`NunchakuFluxLoraLoader`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance
