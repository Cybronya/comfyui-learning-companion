---
key: 图片生成/图生图/GTPimage2.0：纯净细节，无痕优化_2069655726187958273.json
name: GTPimage2.0：纯净细节，无痕优化_2069655726187958273
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/GTPimage2.0：纯净细节，无痕优化_2069655726187958273.json
hash: 7cdbd79cb84a6d05
coverage: 0.87931
learned_at: 2026-10-23 11:02:43
nodes: [NunchakuFluxDiTLoader, NunchakuTextEncoderLoader, VAELoader, FluxForwardODESampler, BasicScheduler, FluxDeGuidance, DisableNoise, VAEEncode, FluxDeGuidance, InFluxModelSamplingPred, BasicGuider, SamplerCustomAdvanced, DisableNoise, OutFluxModelSamplingPred, BasicScheduler, FluxReverseODESampler, BasicGuider, SamplerCustomAdvanced, FlipSigmas, ImageResize+, PreviewImage, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, PreviewImage, easy imageColorMatch, VAEDecode, LoadImage, Note, SaveImage, PreviewImage, easy int, UNETLoader, CLIPTextEncode, CLIPLoader, VAELoader, CLIPTextEncode, VAEEncode, Latent Noise Injection, VAEDecode, KSampler, easy cleanGpuUsed, CLIPTextEncode, CLIPLoader, VAELoader, UNETLoader_Any, KSampler, VAEEncode, ReferenceLatent, ConditioningZeroOut, VAEDecode, easy imageColorMatch, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, Image Comparer (rgthree), PrimitiveFloat, PrimitiveFloat]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 477270951588149, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/GTPimage2.0：纯净细节，无痕优化_2069655726187958273.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/GTPimage2.0：纯净细节，无痕优化_2069655726187958273.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `NunchakuFluxDiTLoader`
- `NunchakuTextEncoderLoader`
- `VAELoader`
- `FluxForwardODESampler` ★核心
- `BasicScheduler`
- `FluxDeGuidance`
- `DisableNoise`
- `VAEEncode` ★核心
- `FluxDeGuidance`
- `InFluxModelSamplingPred`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `DisableNoise`
- `OutFluxModelSamplingPred`
- `BasicScheduler`
- `FluxReverseODESampler` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `FlipSigmas`
- `ImageResize+`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `easy imageColorMatch`
- `VAEDecode` ★核心
- `LoadImage`
- `Note`
- `SaveImage`
- `PreviewImage`
- `easy int`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `Latent Noise Injection`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader_Any` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `easy imageColorMatch`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `Image Comparer (rgthree)`
- `PrimitiveFloat`
- `PrimitiveFloat`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `477270951588149`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **88%**（51/58）

**有卡**：`NunchakuFluxDiTLoader`、`NunchakuTextEncoderLoader`、`VAELoader`、`FluxForwardODESampler`、`BasicScheduler`、`FluxDeGuidance`、`DisableNoise`、`VAEEncode`、`InFluxModelSamplingPred`、`BasicGuider`、`SamplerCustomAdvanced`、`OutFluxModelSamplingPred`、`FluxReverseODESampler`、`FlipSigmas`、`ImageResize+`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`easy imageColorMatch`、`VAEDecode`、`LoadImage`、`SaveImage`、`easy int`、`UNETLoader`、`CLIPLoader`、`Latent Noise Injection`、`KSampler`、`easy cleanGpuUsed`、`UNETLoader_Any`、`ReferenceLatent`、`ConditioningZeroOut`、`ModelSamplingAuraFlow`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
