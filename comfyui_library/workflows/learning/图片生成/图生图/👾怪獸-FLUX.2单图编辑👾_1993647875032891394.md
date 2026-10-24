---
key: 图片生成/图生图/👾怪獸-FLUX.2单图编辑👾_1993647875032891394.json
name: 👾怪獸-FLUX.2单图编辑👾_1993647875032891394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/👾怪獸-FLUX.2单图编辑👾_1993647875032891394.json
hash: f66ff189e18fa2ef
coverage: 1
learned_at: 2026-10-23 13:39:24
nodes: [CLIPLoader, VAELoader, ImageScaleToTotalPixels, UNETLoader, VAEDecode, EmptyFlux2LatentImage, CLIPTextEncode, FluxGuidance, ReferenceLatent, VAEEncode, RandomNoise, BasicGuider, KSamplerSelect, SamplerCustomAdvanced, Flux2Scheduler, Int, Int, SaveImage, LoadImage, CR Prompt Text]
patterns: []
missing: []
---

# 图片生成/图生图/👾怪獸-FLUX.2单图编辑👾_1993647875032891394.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/👾怪獸-FLUX.2单图编辑👾_1993647875032891394.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `Int`
- `Int`
- `SaveImage`
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`UNETLoader`、`VAEDecode`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`FluxGuidance`、`ReferenceLatent`、`VAEEncode`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`Int`、`SaveImage`、`LoadImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
