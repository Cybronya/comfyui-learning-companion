---
key: 图片生成/图生图/【GUGU】FLUX2.0单图编辑_多图编辑_1993506477314949121.json
name: 【GUGU】FLUX2.0单图编辑_多图编辑_1993506477314949121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【GUGU】FLUX2.0单图编辑_多图编辑_1993506477314949121.json
hash: 7bff4fdbaacb89ee
coverage: 0.976744
learned_at: 2026-10-23 11:48:42
nodes: [BasicGuider, RandomNoise, KSamplerSelect, CLIPLoader, Flux2Scheduler, EmptyFlux2LatentImage, VAELoader, easy int, easy int, BasicGuider, RandomNoise, KSamplerSelect, CLIPLoader, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, FluxGuidance, VAELoader, easy int, easy int, ReferenceLatent, UNETLoader, ReferenceLatent, VAEEncode, ImageScaleToTotalPixels, LoadImage, SamplerCustomAdvanced, VAEDecode, UNETLoader, CLIPTextEncode, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, FluxGuidance, LoadImage, SaveImage, CLIPTextEncode, VAEEncode, LoadImage, ImageScaleToTotalPixels, VAEDecode, SaveImage, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/【GUGU】FLUX2.0单图编辑_多图编辑_1993506477314949121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【GUGU】FLUX2.0单图编辑_多图编辑_1993506477314949121.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `VAELoader`
- `easy int`
- `easy int`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `FluxGuidance`
- `VAELoader`
- `easy int`
- `easy int`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageScaleToTotalPixels`
- `LoadImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `FluxGuidance`
- `LoadImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LoadImage`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`

## 知识

覆盖率 **98%**（42/43）

**有卡**：`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`CLIPLoader`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`VAELoader`、`easy int`、`SamplerCustomAdvanced`、`FluxGuidance`、`ReferenceLatent`、`UNETLoader`、`VAEEncode`、`ImageScaleToTotalPixels`、`LoadImage`、`VAEDecode`、`CLIPTextEncode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
