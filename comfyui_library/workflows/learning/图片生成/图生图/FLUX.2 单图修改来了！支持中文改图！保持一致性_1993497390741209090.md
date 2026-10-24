---
key: 图片生成/图生图/FLUX.2 单图修改来了！支持中文改图！保持一致性_1993497390741209090.json
name: FLUX.2 单图修改来了！支持中文改图！保持一致性_1993497390741209090
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 单图修改来了！支持中文改图！保持一致性_1993497390741209090.json
hash: f026df325e1ab616
coverage: 0.84
learned_at: 2026-10-23 10:54:08
nodes: [Flux2Scheduler, BasicGuider, VAEEncode, FluxGuidance, KSamplerSelect, ReferenceLatent, PrimitiveNode, PrimitiveNode, VAELoader, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, ImageScaleToTotalPixels, Note, UNETLoader, RandomNoise, SaveImage, CLIPLoader, MarkdownNote, LoadImage, CLIPTextEncode, LoadImage, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 单图修改来了！支持中文改图！保持一致性_1993497390741209090.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 单图修改来了！支持中文改图！保持一致性_1993497390741209090.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `Flux2Scheduler`
- `BasicGuider`
- `VAEEncode` ★核心
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAELoader`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `Note`
- `UNETLoader` ★核心
- `RandomNoise`
- `SaveImage`
- `CLIPLoader`
- `MarkdownNote`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`Flux2Scheduler`、`BasicGuider`、`VAEEncode`、`FluxGuidance`、`KSamplerSelect`、`ReferenceLatent`、`VAELoader`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`VAEDecode`、`ImageScaleToTotalPixels`、`UNETLoader`、`RandomNoise`、`SaveImage`、`CLIPLoader`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
