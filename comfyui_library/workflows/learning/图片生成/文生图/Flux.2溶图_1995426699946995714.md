---
key: 图片生成/文生图/Flux.2溶图_1995426699946995714.json
name: Flux.2溶图_1995426699946995714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.2溶图_1995426699946995714.json
hash: ca9aaa413f6ef13c
coverage: 0.903226
learned_at: 2026-10-19 21:32:33
nodes: [LoadImage, InspyrenetRembg, InspyrenetRembg, InspyrenetRembg, PreviewImage, KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, Flux2Scheduler, EmptyFlux2LatentImage, Note, RandomNoise, CLIPTextEncode, SamplerCustomAdvanced, ModelPatchTorchSettings, PathchSageAttentionKJ, CLIPLoader, CompositorConfig3, LoadImage, LoadImage, VAEDecode, SaveImage, Compositor3, ImageResizeKJv2, UNETLoader, LoadImage, Image Comparer (rgthree), VAELoader, RH_Translator]
patterns: []
missing: []
---

# 图片生成/文生图/Flux.2溶图_1995426699946995714.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.2溶图_1995426699946995714.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `LoadImage`
- `InspyrenetRembg`
- `InspyrenetRembg`
- `InspyrenetRembg`
- `PreviewImage`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `CompositorConfig3`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `Compositor3`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `LoadImage`
- `Image Comparer (rgthree)`
- `VAELoader`
- `RH_Translator`

## 知识

覆盖率 **90%**（28/31）

**有卡**：`LoadImage`、`InspyrenetRembg`、`KSamplerSelect`、`BasicGuider`、`ReferenceLatent`、`VAEEncode`、`FluxGuidance`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`RandomNoise`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CLIPLoader`、`CompositorConfig3`、`VAEDecode`、`SaveImage`、`Compositor3`、`ImageResizeKJv2`、`UNETLoader`、`VAELoader`、`RH_Translator`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
