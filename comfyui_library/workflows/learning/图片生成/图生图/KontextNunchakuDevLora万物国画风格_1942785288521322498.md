---
key: 图片生成/图生图/KontextNunchakuDevLora万物国画风格_1942785288521322498.json
name: KontextNunchakuDevLora万物国画风格_1942785288521322498
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora万物国画风格_1942785288521322498.json
hash: 80bbfcea457c150d
coverage: 1
learned_at: 2026-10-23 11:06:33
nodes: [DualCLIPLoader, VAEDecode, SaveImage, FluxGuidance, ReferenceLatent, CLIPTextEncode, ConditioningZeroOut, FluxKontextImageScale, VAELoader, NunchakuFluxDiTLoader, VAEEncode, ModelSamplingFlux, KSampler, LoadImage, LoraLoaderModelOnly, RH_Translator]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 257266426545889, "steps": 20}
---

# 图片生成/图生图/KontextNunchakuDevLora万物国画风格_1942785288521322498.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora万物国画风格_1942785288521322498.json`

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
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `257266426545889`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`DualCLIPLoader`、`VAEDecode`、`SaveImage`、`FluxGuidance`、`ReferenceLatent`、`CLIPTextEncode`、`ConditioningZeroOut`、`FluxKontextImageScale`、`VAELoader`、`NunchakuFluxDiTLoader`、`VAEEncode`、`ModelSamplingFlux`、`KSampler`、`LoadImage`、`LoraLoaderModelOnly`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
