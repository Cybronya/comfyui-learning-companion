---
key: 图片生成/图生图/KontextNunchakuDev转绘Abbott Fuller Graves风格_1940994557704355841.json
name: KontextNunchakuDev转绘Abbott Fuller Graves风格_1940994557704355841
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextNunchakuDev转绘Abbott Fuller Graves风格_1940994557704355841.json
hash: 5a94977d14638c89
coverage: 0.9375
learned_at: 2026-10-23 11:06:46
nodes: [DualCLIPLoader, VAEDecode, SaveImage, FluxGuidance, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, KSampler, FluxKontextImageScale, VAELoader, ModelSamplingFlux, NunchakuFluxDiTLoader, ShowText|pysssss, VAEEncode, LoadImage, RH_Translator]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 292994210104030, "steps": 20}
---

# 图片生成/图生图/KontextNunchakuDev转绘Abbott Fuller Graves风格_1940994557704355841.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextNunchakuDev转绘Abbott Fuller Graves风格_1940994557704355841.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `FluxGuidance`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `FluxKontextImageScale`
- `VAELoader`
- `ModelSamplingFlux`
- `NunchakuFluxDiTLoader`
- `ShowText|pysssss`
- `VAEEncode` ★核心
- `LoadImage`
- `RH_Translator`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `292994210104030`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`KSampler`、`FluxKontextImageScale`、`VAELoader`、`ModelSamplingFlux`、`NunchakuFluxDiTLoader`、`VAEEncode`、`LoadImage`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance、ReferenceLatent
