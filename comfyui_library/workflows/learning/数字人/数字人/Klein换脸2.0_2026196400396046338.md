---
key: 数字人/数字人/Klein换脸2.0_2026196400396046338.json
name: Klein换脸2.0_2026196400396046338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Klein换脸2.0_2026196400396046338.json
hash: 1106233a7ecfc47c
coverage: 0.96
learned_at: 2026-10-26 01:55:38
nodes: [CFGGuider, RandomNoise, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, CLIPLoader, ReferenceLatent, ConditioningZeroOut, VAEEncode, GetImageSize, VAEEncode, ReferenceLatent, VAEDecode, FluxKontextImageScale, VAELoader, UNETLoader, CLIPTextEncode, AutoCropFaces, ImageResizeKJv2, LoraLoaderModelOnly, SaveImage, LoadImage, PreviewImage, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/Klein换脸2.0_2026196400396046338.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Klein换脸2.0_2026196400396046338.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `GetImageSize`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `AutoCropFaces`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `LoadImage`
- `PreviewImage`
- `LoadImage`

## 知识

覆盖率 **96%**（24/25）

**有卡**：`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`CLIPLoader`、`ReferenceLatent`、`ConditioningZeroOut`、`VAEEncode`、`GetImageSize`、`VAEDecode`、`FluxKontextImageScale`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`AutoCropFaces`、`ImageResizeKJv2`、`LoraLoaderModelOnly`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
