---
key: 平台全量/【阡陌】Nunchaku Kontext+8步Turbo lora极速秒出图_1964546880803885058.json
name: 【阡陌】Nunchaku Kontext+8步Turbo lora极速秒出图_1964546880803885058
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/【阡陌】Nunchaku Kontext+8步Turbo lora极速秒出图_1964546880803885058.json
hash: 42adc8b303971a4b
coverage: 0.95
learned_at: 2026-11-14 01:25:57
nodes: [SaveImage, VAEDecode, Note, KSampler, NunchakuFluxDiTLoader, NunchakuTextEncoderLoaderV2, VAELoader, ImageConcanate, ImageConcanate, LoadImage, LoadImage, LoadImage, CLIPTextEncode, NunchakuFluxLoraLoader, ConditioningZeroOut, ReferenceLatent, FluxGuidance, LoadImage, VAEEncode, FluxKontextImageScale]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 913298408408255, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/【阡陌】Nunchaku Kontext+8步Turbo lora极速秒出图_1964546880803885058.json

> 来源文件 `comfyui_library/workflows/平台全量/【阡陌】Nunchaku Kontext+8步Turbo lora极速秒出图_1964546880803885058.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `Note`
- `KSampler` ★核心
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoaderV2`
- `VAELoader`
- `ImageConcanate`
- `ImageConcanate`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `NunchakuFluxLoraLoader` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `FluxGuidance`
- `LoadImage`
- `VAEEncode` ★核心
- `FluxKontextImageScale`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `913298408408255`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`SaveImage`、`VAEDecode`、`KSampler`、`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoaderV2`、`VAELoader`、`ImageConcanate`、`LoadImage`、`CLIPTextEncode`、`NunchakuFluxLoraLoader`、`ConditioningZeroOut`、`ReferenceLatent`、`FluxGuidance`、`VAEEncode`、`FluxKontextImageScale`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、NunchakuTextEncoderLoaderV2

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
