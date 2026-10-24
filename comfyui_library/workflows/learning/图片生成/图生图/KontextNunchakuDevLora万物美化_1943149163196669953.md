---
key: 图片生成/图生图/KontextNunchakuDevLora万物美化_1943149163196669953.json
name: KontextNunchakuDevLora万物美化_1943149163196669953
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora万物美化_1943149163196669953.json
hash: 3820832b4058a13b
coverage: 1
learned_at: 2026-10-23 11:06:34
nodes: [DualCLIPLoader, VAEDecode, SaveImage, FluxGuidance, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, FluxKontextImageScale, VAELoader, NunchakuFluxDiTLoader, VAEEncode, ModelSamplingFlux, KSampler, LoraLoaderModelOnly, RH_Translator, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1063965716067634, "steps": 20}
---

# 图片生成/图生图/KontextNunchakuDevLora万物美化_1943149163196669953.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora万物美化_1943149163196669953.json`

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
- `FluxKontextImageScale`
- `VAELoader`
- `NunchakuFluxDiTLoader`
- `VAEEncode` ★核心
- `ModelSamplingFlux`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1063965716067634`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`FluxKontextImageScale`、`VAELoader`、`NunchakuFluxDiTLoader`、`VAEEncode`、`ModelSamplingFlux`、`KSampler`、`LoraLoaderModelOnly`、`RH_Translator`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
