---
key: 图片生成/图生图/单图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1938402352451751937.json
name: 单图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1938402352451751937
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/单图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1938402352451751937.json
hash: d8d2a529acc049f2
coverage: 1
learned_at: 2026-10-23 12:32:16
nodes: [VAEEncode, ReferenceLatent, FluxGuidance, CLIPTextEncode, SaveImage, KSampler, VAELoader, RH_LLMAPI_NODE, FluxKontextImageScale, ConditioningZeroOut, GetImageSize+, EmptySD3LatentImage, VAEDecode, Text Multiline, DualCLIPLoader, LoadImage, NunchakuFluxLoraLoader, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, NunchakuFluxLoraLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 101643976348815, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/单图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1938402352451751937.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/单图极速出图Flux Kontext Dev+Nunchaku+8步Lora+LLM自动润词_1938402352451751937.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `VAELoader`
- `RH_LLMAPI_NODE`
- `FluxKontextImageScale`
- `ConditioningZeroOut`
- `GetImageSize+`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `Text Multiline`
- `DualCLIPLoader`
- `LoadImage`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader` ★核心
- `NunchakuFluxLoraLoader` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `101643976348815`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`VAEEncode`、`ReferenceLatent`、`FluxGuidance`、`CLIPTextEncode`、`SaveImage`、`KSampler`、`VAELoader`、`RH_LLMAPI_NODE`、`FluxKontextImageScale`、`ConditioningZeroOut`、`GetImageSize+`、`EmptySD3LatentImage`、`VAEDecode`、`Text Multiline`、`DualCLIPLoader`、`LoadImage`、`NunchakuFluxLoraLoader`、`NunchakuFluxDiTLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
