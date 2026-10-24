---
key: 图片生成/图生图/KontextDev转绘Aaron Douglas风格_1940612072243884034.json
name: KontextDev转绘Aaron Douglas风格_1940612072243884034
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextDev转绘Aaron Douglas风格_1940612072243884034.json
hash: fa07d365035225e9
coverage: 1
learned_at: 2026-10-23 11:06:26
nodes: [DualCLIPLoader, VAEDecode, SaveImage, VAEEncode, FluxGuidance, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, KSampler, FluxKontextImageScale, VAELoader, ModelSamplingFlux, NunchakuFluxDiTLoader, RH_Translator, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 809024342215474, "steps": 20}
---

# 图片生成/图生图/KontextDev转绘Aaron Douglas风格_1940612072243884034.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextDev转绘Aaron Douglas风格_1940612072243884034.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（15 个）：
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `FluxGuidance`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `FluxKontextImageScale`
- `VAELoader`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `RH_Translator`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `809024342215474`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`VAEEncode`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`KSampler`、`FluxKontextImageScale`、`VAELoader`、`ModelSamplingFlux`、`NunchakuFluxDiTLoader`、`RH_Translator`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent
