---
key: 图片生成/文生图/FLUX.2 Turbo_2006076343817084929.json
name: FLUX.2 Turbo_2006076343817084929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2 Turbo_2006076343817084929.json
hash: 610b5b600cf6a074
coverage: 0.916667
learned_at: 2026-10-19 22:00:30
nodes: [BasicGuider, VAEEncode, LoadImage, VAEEncode, ReferenceLatent, FluxGuidance, KSamplerSelect, ReferenceLatent, PrimitiveNode, PrimitiveNode, VAELoader, EmptyFlux2LatentImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, VAEDecode, ImageScaleToTotalPixels, CLIPTextEncode, LoadImage, SaveImage, UNETLoader, CLIPLoader, RandomNoise, Flux2Scheduler, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2 Turbo_2006076343817084929.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2 Turbo_2006076343817084929.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `BasicGuider`
- `VAEEncode` ★核心
- `LoadImage`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAELoader`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `Flux2Scheduler`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **92%**（22/24）

**有卡**：`BasicGuider`、`VAEEncode`、`LoadImage`、`ReferenceLatent`、`FluxGuidance`、`KSamplerSelect`、`VAELoader`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`VAEDecode`、`CLIPTextEncode`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`Flux2Scheduler`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance
