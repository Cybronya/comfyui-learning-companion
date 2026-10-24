---
key: 图片生成/图生图/Flux1-Kontext双图编辑+Nunchaku+Turbo8步加速+10秒出图_1948150218222108674.json
name: Flux1-Kontext双图编辑+Nunchaku+Turbo8步加速+10秒出图_1948150218222108674
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux1-Kontext双图编辑+Nunchaku+Turbo8步加速+10秒出图_1948150218222108674.json
hash: 8404f96417fc8f9c
coverage: 0.95
learned_at: 2026-10-23 10:58:57
nodes: [FluxGuidance, ReferenceLatent, FluxKontextImageScale, ConditioningZeroOut, VAEEncode, CLIPTextEncode, VAEDecode, RH_Translator, DualCLIPLoader, VAELoader, ShowText|pysssss, NunchakuFluxDiTLoader, ImageStitch, KSampler, NunchakuFluxLoraLoader, Text Multiline, LoadImage, LoadImage, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1076200740816239, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux1-Kontext双图编辑+Nunchaku+Turbo8步加速+10秒出图_1948150218222108674.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux1-Kontext双图编辑+Nunchaku+Turbo8步加速+10秒出图_1948150218222108674.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `FluxGuidance`
- `ReferenceLatent`
- `FluxKontextImageScale`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `RH_Translator`
- `DualCLIPLoader`
- `VAELoader`
- `ShowText|pysssss`
- `NunchakuFluxDiTLoader`
- `ImageStitch`
- `KSampler` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `Text Multiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1076200740816239`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`FluxGuidance`、`ReferenceLatent`、`FluxKontextImageScale`、`ConditioningZeroOut`、`VAEEncode`、`CLIPTextEncode`、`VAEDecode`、`RH_Translator`、`DualCLIPLoader`、`VAELoader`、`NunchakuFluxDiTLoader`、`ImageStitch`、`KSampler`、`NunchakuFluxLoraLoader`、`Text Multiline`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
