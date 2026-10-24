---
key: 图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2109826006751203329.json
name: 印花提取-商业级_Flux.1_Kontext_2109826006751203329
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2109826006751203329.json
hash: f2a4c5e2f2fb37c1
coverage: 1
learned_at: 2026-10-23 12:32:56
nodes: [FluxKontextImageScale, UNETLoader, DualCLIPLoader, VAELoader, LoraLoaderModelOnly, CLIPTextEncode, VAEEncode, FluxGuidance, ConditioningZeroOut, VAEDecode, SaveImage, ReferenceLatent, KSampler, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 301728396447421, "steps": 20}
---

# 图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2109826006751203329.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2109826006751203329.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `FluxKontextImageScale`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `ReferenceLatent`
- `KSampler` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `301728396447421`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`FluxKontextImageScale`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEEncode`、`FluxGuidance`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`ReferenceLatent`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
