---
key: 图片生成/文生图/flux2-Timestep Distillation（步级蒸馏）_2061782953197391873.json
name: flux2-Timestep Distillation（步级蒸馏）_2061782953197391873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux2-Timestep Distillation（步级蒸馏）_2061782953197391873.json
hash: b12f4525c603eba3
coverage: 0.923077
learned_at: 2026-10-19 23:03:14
nodes: [BasicGuider, VAEEncode, LoadImage, ReferenceLatent, KSamplerSelect, VAELoader, EmptyFlux2LatentImage, SamplerCustomAdvanced, ImageScaleToTotalPixels, Note, MarkdownNote, CLIPLoader, RandomNoise, Flux2Scheduler, LoraLoaderModelOnly, UNETLoader, VAEEncode, ReferenceLatent, GetImageSize, SaveImage, ImageScaleToTotalPixels, VAEDecode, CLIPTextEncode, FluxGuidance, LoraLoaderModelOnly, LoadImage]
patterns: []
missing: []
---

# 图片生成/文生图/flux2-Timestep Distillation（步级蒸馏）_2061782953197391873.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux2-Timestep Distillation（步级蒸馏）_2061782953197391873.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `BasicGuider`
- `VAEEncode` ★核心
- `LoadImage`
- `ReferenceLatent`
- `KSamplerSelect` ★核心
- `VAELoader`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `Note`
- `MarkdownNote`
- `CLIPLoader`
- `RandomNoise`
- `Flux2Scheduler`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `GetImageSize`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`BasicGuider`、`VAEEncode`、`LoadImage`、`ReferenceLatent`、`KSamplerSelect`、`VAELoader`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`CLIPLoader`、`RandomNoise`、`Flux2Scheduler`、`LoraLoaderModelOnly`、`UNETLoader`、`GetImageSize`、`SaveImage`、`VAEDecode`、`CLIPTextEncode`、`FluxGuidance`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance
