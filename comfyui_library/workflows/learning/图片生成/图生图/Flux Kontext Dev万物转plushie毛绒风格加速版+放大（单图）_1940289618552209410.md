---
key: 图片生成/图生图/Flux Kontext Dev万物转plushie毛绒风格加速版+放大（单图）_1940289618552209410.json
name: Flux Kontext Dev万物转plushie毛绒风格加速版+放大（单图）_1940289618552209410
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物转plushie毛绒风格加速版+放大（单图）_1940289618552209410.json
hash: a5478dc8dd69dd4e
coverage: 1
learned_at: 2026-10-23 10:56:50
nodes: [ImageStitch, FluxGuidance, ReferenceLatent, ConditioningZeroOut, VAEEncode, VAEDecode, SaveImage, FluxKontextImageScale, CLIPTextEncode, RH_Translator, DualCLIPLoader, VAELoader, NunchakuFluxLoraLoader, KSampler, UNETLoader, LoadImage, SaveImage, NunchakuFluxDiTLoader, LoadImage, Text Multiline, ImageConcatMulti, PMRF, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 399987337272441, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux Kontext Dev万物转plushie毛绒风格加速版+放大（单图）_1940289618552209410.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev万物转plushie毛绒风格加速版+放大（单图）_1940289618552209410.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `ImageStitch`
- `FluxGuidance`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `FluxKontextImageScale`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `DualCLIPLoader`
- `VAELoader`
- `NunchakuFluxLoraLoader` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `NunchakuFluxDiTLoader`
- `LoadImage`
- `Text Multiline`
- `ImageConcatMulti`
- `PMRF`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `399987337272441`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（23/23）

**有卡**：`ImageStitch`、`FluxGuidance`、`ReferenceLatent`、`ConditioningZeroOut`、`VAEEncode`、`VAEDecode`、`SaveImage`、`FluxKontextImageScale`、`CLIPTextEncode`、`RH_Translator`、`DualCLIPLoader`、`VAELoader`、`NunchakuFluxLoraLoader`、`KSampler`、`UNETLoader`、`LoadImage`、`NunchakuFluxDiTLoader`、`Text Multiline`、`ImageConcatMulti`、`PMRF`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
