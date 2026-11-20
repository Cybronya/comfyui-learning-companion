---
key: 平台全量/flux.2图像编辑_1995497834998857729.json
name: flux.2图像编辑_1995497834998857729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux.2图像编辑_1995497834998857729.json
hash: 631dac90117f6b71
coverage: 0.84
learned_at: 2026-11-14 01:11:00
nodes: [Flux2Scheduler, BasicGuider, VAEEncode, LoadImage, ReferenceLatent, KSamplerSelect, VAELoader, EmptyFlux2LatentImage, ImageScaleToTotalPixels, VAEDecode, Note, RandomNoise, CLIPLoader, UNETLoader, FluxGuidance, MarkdownNote, PrimitiveNode, LoadImage, ImageScaleToTotalPixels, ReferenceLatent, VAEEncode, SamplerCustomAdvanced, PrimitiveNode, CLIPTextEncode, SaveImage]
patterns: []
missing: []
---

# 平台全量/flux.2图像编辑_1995497834998857729.json

> 来源文件 `comfyui_library/workflows/平台全量/flux.2图像编辑_1995497834998857729.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `Flux2Scheduler`
- `BasicGuider`
- `VAEEncode` ★核心
- `LoadImage`
- `ReferenceLatent`
- `KSamplerSelect` ★核心
- `VAELoader`
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `Note`
- `RandomNoise`
- `CLIPLoader`
- `UNETLoader` ★核心
- `FluxGuidance`
- `MarkdownNote`
- `PrimitiveNode`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `SaveImage`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`Flux2Scheduler`、`BasicGuider`、`VAEEncode`、`LoadImage`、`ReferenceLatent`、`KSamplerSelect`、`VAELoader`、`EmptyFlux2LatentImage`、`ImageScaleToTotalPixels`、`VAEDecode`、`RandomNoise`、`CLIPLoader`、`UNETLoader`、`FluxGuidance`、`SamplerCustomAdvanced`、`CLIPTextEncode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect
