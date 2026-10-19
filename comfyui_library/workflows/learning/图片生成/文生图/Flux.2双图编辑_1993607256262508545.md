---
key: 图片生成/文生图/Flux.2双图编辑_1993607256262508545.json
name: Flux.2双图编辑_1993607256262508545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2双图编辑_1993607256262508545.json
hash: 65a6ec9f6dd1e1e5
coverage: 1
learned_at: 2026-10-19 21:32:32
nodes: [UNETLoader, CLIPLoader, VAELoader, ImpactInt, ImpactInt, BasicGuider, FluxGuidance, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, VAEDecode, ReferenceLatent, SaveImage, ImageScaleToTotalPixels, VAEEncode, ImageScaleToTotalPixels, ReferenceLatent, RH_Translator, VAEEncode, LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2双图编辑_1993607256262508545.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2双图编辑_1993607256262508545.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImpactInt`
- `ImpactInt`
- `BasicGuider`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ReferenceLatent`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `ReferenceLatent`
- `RH_Translator`
- `VAEEncode` ★核心
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **100%**（24/24）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImpactInt`、`BasicGuider`、`FluxGuidance`、`CLIPTextEncode`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`ReferenceLatent`、`SaveImage`、`ImageScaleToTotalPixels`、`VAEEncode`、`RH_Translator`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
