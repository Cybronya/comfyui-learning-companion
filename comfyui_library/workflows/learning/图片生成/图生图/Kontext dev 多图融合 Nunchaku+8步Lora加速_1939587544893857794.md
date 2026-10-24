---
key: 图片生成/图生图/Kontext dev 多图融合 Nunchaku+8步Lora加速_1939587544893857794.json
name: Kontext dev 多图融合 Nunchaku+8步Lora加速_1939587544893857794
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Kontext dev 多图融合 Nunchaku+8步Lora加速_1939587544893857794.json
hash: baa5a83fb30e3b6f
coverage: 1
learned_at: 2026-10-23 11:05:45
nodes: [FluxGuidance, ReferenceLatent, VAEEncode, FluxKontextImageScale, ImageStitch, VAELoader, DualCLIPLoader, KSampler, ConditioningZeroOut, Int, Int, VAEDecode, CLIPTextEncode, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, RH_LLMAPI_NODE, LoadImage, EmptySD3LatentImage, Text Multiline, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 34236826400939, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Kontext dev 多图融合 Nunchaku+8步Lora加速_1939587544893857794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Kontext dev 多图融合 Nunchaku+8步Lora加速_1939587544893857794.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `FluxGuidance`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `ImageStitch`
- `VAELoader`
- `DualCLIPLoader`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `Int`
- `Int`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `RH_LLMAPI_NODE`
- `LoadImage`
- `EmptySD3LatentImage`
- `Text Multiline`
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `34236826400939`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`FluxGuidance`、`ReferenceLatent`、`VAEEncode`、`FluxKontextImageScale`、`ImageStitch`、`VAELoader`、`DualCLIPLoader`、`KSampler`、`ConditioningZeroOut`、`Int`、`VAEDecode`、`CLIPTextEncode`、`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`、`RH_LLMAPI_NODE`、`LoadImage`、`EmptySD3LatentImage`、`Text Multiline`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
