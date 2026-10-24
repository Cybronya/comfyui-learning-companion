---
key: 图片生成/图生图/Flux Kontext Dev 10倍三重加速（Nunchaku）_1939491330919735298.json
name: Flux Kontext Dev 10倍三重加速（Nunchaku）_1939491330919735298
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev 10倍三重加速（Nunchaku）_1939491330919735298.json
hash: 3bbc2e370c33a0de
coverage: 0.863636
learned_at: 2026-10-23 10:56:24
nodes: [VAELoader, ConditioningZeroOut, LoadImageOutput, VAEDecode, VAEEncode, FluxKontextImageScale, MarkdownNote, FluxGuidance, ReferenceLatent, MarkdownNote, CLIPTextEncode, GoogleTranslateTextNode, EmptySD3LatentImage, ImageStitch, PreviewImage, SaveImage, KSampler, NunchakuFluxDiTLoader, DualCLIPLoader, NunchakuFluxLoraLoader, LoadImage, CR Prompt Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 447991987695537, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux Kontext Dev 10倍三重加速（Nunchaku）_1939491330919735298.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Dev 10倍三重加速（Nunchaku）_1939491330919735298.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `LoadImageOutput`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `EmptySD3LatentImage`
- `ImageStitch`
- `PreviewImage`
- `SaveImage`
- `KSampler` ★核心
- `NunchakuFluxDiTLoader`
- `DualCLIPLoader`
- `NunchakuFluxLoraLoader` ★核心
- `LoadImage`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `447991987695537`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEDecode`、`VAEEncode`、`FluxKontextImageScale`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`EmptySD3LatentImage`、`ImageStitch`、`SaveImage`、`KSampler`、`NunchakuFluxDiTLoader`、`DualCLIPLoader`、`NunchakuFluxLoraLoader`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、SaveImage、LoadImage、FluxGuidance

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
