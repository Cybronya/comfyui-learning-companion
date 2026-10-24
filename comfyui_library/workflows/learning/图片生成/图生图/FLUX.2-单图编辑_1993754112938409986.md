---
key: 图片生成/图生图/FLUX.2-单图编辑_1993754112938409986.json
name: FLUX.2-单图编辑_1993754112938409986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2-单图编辑_1993754112938409986.json
hash: 719e0cae90b2e729
coverage: 0.92
learned_at: 2026-10-23 10:54:14
nodes: [VAELoader, SamplerCustomAdvanced, LoadImage, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, RandomNoise, BasicGuider, KSamplerSelect, ReferenceLatent, VAEEncode, MarkdownNote, FluxGuidance, VAEDecode, PreviewImage, SaveImage, CLIPLoader, UNETLoader, LoadImage, ImageScaleToTotalPixels, LoadImage, Flux2Scheduler, EmptyFlux2LatentImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2-单图编辑_1993754112938409986.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2-单图编辑_1993754112938409986.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `MarkdownNote`
- `FluxGuidance`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **92%**（23/25）

**有卡**：`VAELoader`、`SamplerCustomAdvanced`、`LoadImage`、`ImageScaleToTotalPixels`、`VAEEncode`、`ReferenceLatent`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`FluxGuidance`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`UNETLoader`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
