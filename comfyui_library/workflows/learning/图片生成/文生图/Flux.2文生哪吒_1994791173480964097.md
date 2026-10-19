---
key: 图片生成/文生图/Flux.2文生哪吒_1994791173480964097.json
name: Flux.2文生哪吒_1994791173480964097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2文生哪吒_1994791173480964097.json
hash: 9b6e3fa0a2f5d16c
coverage: 0.88
learned_at: 2026-10-19 21:32:33
nodes: [ImageScaleToTotalPixels, VAEEncode, VAEEncode, ImageScaleToTotalPixels, EmptyFlux2LatentImage, ReferenceLatent, ReferenceLatent, FluxGuidance, PreviewImage, LoadImage, LoadImage, SamplerCustomAdvanced, RandomNoise, BasicGuider, KSamplerSelect, Flux2Scheduler, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, PrimitiveNode, PrimitiveNode, VAEDecode, SaveImage, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2文生哪吒_1994791173480964097.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2文生哪吒_1994791173480964097.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `FluxGuidance`
- `PreviewImage`
- `LoadImage`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **88%**（22/25）

**有卡**：`ImageScaleToTotalPixels`、`VAEEncode`、`EmptyFlux2LatentImage`、`ReferenceLatent`、`FluxGuidance`、`LoadImage`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`Flux2Scheduler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance
