---
key: 图片生成/图生图/👾怪獸-FLUX.2多图编辑👾_1993639173827608577.json
name: 👾怪獸-FLUX.2多图编辑👾_1993639173827608577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/👾怪獸-FLUX.2多图编辑👾_1993639173827608577.json
hash: 12475a2370e2daf5
coverage: 0.941176
learned_at: 2026-10-23 13:39:24
nodes: [PreviewAny, RH_LLMAPI_NODE, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAEEncode, VAEEncode, UNETLoader, CLIPLoader, VAELoader, FluxGuidance, RandomNoise, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, VAEEncode, SamplerCustomAdvanced, ReferenceLatent, ReferenceLatent, ReferenceLatent, BasicGuider, VAEDecode, ImageScaleToTotalPixels, ImageConcanate, ImageConcanate, ImageConcanate, PrimitiveStringMultiline, SaveImage, SaveImage, LoadImage, LoadImage, LoadImage, CLIPTextEncode, Int, Int]
patterns: []
missing: []
---

# 图片生成/图生图/👾怪獸-FLUX.2多图编辑👾_1993639173827608577.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/👾怪獸-FLUX.2多图编辑👾_1993639173827608577.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `PreviewAny`
- `RH_LLMAPI_NODE`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `FluxGuidance`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ReferenceLatent`
- `BasicGuider`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `ImageConcanate`
- `ImageConcanate`
- `ImageConcanate`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `Int`
- `Int`

## 知识

覆盖率 **94%**（32/34）

**有卡**：`RH_LLMAPI_NODE`、`ImageScaleToTotalPixels`、`VAEEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`FluxGuidance`、`RandomNoise`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`ReferenceLatent`、`BasicGuider`、`VAEDecode`、`ImageConcanate`、`SaveImage`、`LoadImage`、`CLIPTextEncode`、`Int`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
