---
key: 图片生成/图生图/KontextNunchakuDevLora火焰特效_1943526598106619905.json
name: KontextNunchakuDevLora火焰特效_1943526598106619905
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora火焰特效_1943526598106619905.json
hash: 7d66d64e8ffc87cf
coverage: 1
learned_at: 2026-10-23 11:06:39
nodes: [SaveImage, DualCLIPLoader, VAEDecode, KSampler, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, ReferenceLatent, VAELoader, FluxKontextImageScale, VAEEncode, EmptySD3LatentImage, NunchakuFluxDiTLoader, ModelSamplingFlux, LoadImage, LoadImage, SDXLPromptStyler, ImageStitch, LoraLoaderModelOnly, RH_Translator]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 962825567377544, "steps": 20}
---

# 图片生成/图生图/KontextNunchakuDevLora火焰特效_1943526598106619905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/KontextNunchakuDevLora火焰特效_1943526598106619905.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `SaveImage`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAELoader`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `EmptySD3LatentImage`
- `NunchakuFluxDiTLoader`
- `ModelSamplingFlux`
- `LoadImage`
- `LoadImage`
- `SDXLPromptStyler`
- `ImageStitch`
- `LoraLoaderModelOnly` ★核心
- `RH_Translator`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `962825567377544`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`SaveImage`、`DualCLIPLoader`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`FluxGuidance`、`ConditioningZeroOut`、`ReferenceLatent`、`VAELoader`、`FluxKontextImageScale`、`VAEEncode`、`EmptySD3LatentImage`、`NunchakuFluxDiTLoader`、`ModelSamplingFlux`、`LoadImage`、`SDXLPromptStyler`、`ImageStitch`、`LoraLoaderModelOnly`、`RH_Translator`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
