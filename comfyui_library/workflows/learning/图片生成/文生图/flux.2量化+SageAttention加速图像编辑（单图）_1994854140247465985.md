---
key: 图片生成/文生图/flux.2量化+SageAttention加速图像编辑（单图）_1994854140247465985.json
name: flux.2量化+SageAttention加速图像编辑（单图）_1994854140247465985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux.2量化+SageAttention加速图像编辑（单图）_1994854140247465985.json
hash: ba62d6bd8832f498
coverage: 0.862069
learned_at: 2026-10-19 21:33:11
nodes: [KSamplerSelect, BasicGuider, ReferenceLatent, VAEEncode, FluxGuidance, Flux2Scheduler, EmptyFlux2LatentImage, Note, RandomNoise, VAELoader, UnetLoaderGGUF, ModelPatchTorchSettings, CLIPTextEncode, CLIPLoader, LoadImage, LoadImage, PreviewAny, SamplerCustomAdvanced, VAEDecode, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, PathchSageAttentionKJ, RH_Translator, ImageScaleToTotalPixels, PrimitiveNode, PrimitiveNode, SaveImage, easy promptLine]
patterns: []
missing: []
---

# 图片生成/文生图/flux.2量化+SageAttention加速图像编辑（单图）_1994854140247465985.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux.2量化+SageAttention加速图像编辑（单图）_1994854140247465985.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `FluxGuidance`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `Note`
- `RandomNoise`
- `VAELoader`
- `UnetLoaderGGUF` ★核心
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `PreviewAny`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `PathchSageAttentionKJ`
- `RH_Translator`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`
- `PrimitiveNode`
- `SaveImage`
- `easy promptLine`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`KSamplerSelect`、`BasicGuider`、`ReferenceLatent`、`VAEEncode`、`FluxGuidance`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`RandomNoise`、`VAELoader`、`UnetLoaderGGUF`、`ModelPatchTorchSettings`、`CLIPTextEncode`、`CLIPLoader`、`LoadImage`、`SamplerCustomAdvanced`、`VAEDecode`、`ImageScaleToTotalPixels`、`PathchSageAttentionKJ`、`RH_Translator`、`SaveImage`、`easy promptLine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
