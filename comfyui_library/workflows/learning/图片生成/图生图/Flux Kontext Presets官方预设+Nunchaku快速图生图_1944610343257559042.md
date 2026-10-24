---
key: 图片生成/图生图/Flux Kontext Presets官方预设+Nunchaku快速图生图_1944610343257559042.json
name: Flux Kontext Presets官方预设+Nunchaku快速图生图_1944610343257559042
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux Kontext Presets官方预设+Nunchaku快速图生图_1944610343257559042.json
hash: b55808eb0060cc56
coverage: 1
learned_at: 2026-10-23 10:57:24
nodes: [Text Multiline, NunchakuFluxDiTLoader, DualCLIPLoader, VAELoader, FluxKontextImageScale, ReferenceLatent, FluxGuidance, ConditioningZeroOut, NunchakuFluxLoraLoader, CLIPTextEncode, RH_LLMAPI_NODE, KSampler, VAEDecode, LoadImage, VAEEncode, SaveImage, LoadKontextPresets]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 600727562580326, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux Kontext Presets官方预设+Nunchaku快速图生图_1944610343257559042.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux Kontext Presets官方预设+Nunchaku快速图生图_1944610343257559042.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（17 个）：
- `Text Multiline`
- `NunchakuFluxDiTLoader`
- `DualCLIPLoader`
- `VAELoader`
- `FluxKontextImageScale`
- `ReferenceLatent`
- `FluxGuidance`
- `ConditioningZeroOut`
- `NunchakuFluxLoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `RH_LLMAPI_NODE`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `SaveImage`
- `LoadKontextPresets`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `600727562580326`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`Text Multiline`、`NunchakuFluxDiTLoader`、`DualCLIPLoader`、`VAELoader`、`FluxKontextImageScale`、`ReferenceLatent`、`FluxGuidance`、`ConditioningZeroOut`、`NunchakuFluxLoraLoader`、`CLIPTextEncode`、`RH_LLMAPI_NODE`、`KSampler`、`VAEDecode`、`LoadImage`、`VAEEncode`、`SaveImage`、`LoadKontextPresets`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
