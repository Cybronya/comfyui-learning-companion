---
key: 图片生成/图生图/Flux2.DEV-三角色一场景图编辑_2018937350511923202.json
name: Flux2.DEV-三角色一场景图编辑_2018937350511923202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2.DEV-三角色一场景图编辑_2018937350511923202.json
hash: b7836d267711b6e9
coverage: 0.921053
learned_at: 2026-10-23 11:00:52
nodes: [KSamplerSelect, SamplerCustomAdvanced, ImageConcanate, ImageConcanate, UNETLoader, VAELoader, Flux2Scheduler, CLIPLoader, ImageConcanate, VAEDecode, BasicGuider, FluxGuidance, SaveImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ReferenceLatent, VAEEncode, VAEEncode, ReferenceLatent, VAEEncode, ReferenceLatent, VAEEncode, ReferenceLatent, easy promptList, SaveImage, EmptyFlux2LatentImage, CLIPTextEncode, PrimitiveNode, PrimitiveNode, RandomNoise, LoadImage, LoadImage, LoadImage, LoadImage, Note, ImageConcanate]
patterns: []
missing: []
---

# 图片生成/图生图/Flux2.DEV-三角色一场景图编辑_2018937350511923202.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2.DEV-三角色一场景图编辑_2018937350511923202.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `UNETLoader` ★核心
- `VAELoader`
- `Flux2Scheduler`
- `CLIPLoader`
- `ImageConcanate`
- `VAEDecode` ★核心
- `BasicGuider`
- `FluxGuidance`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `easy promptList`
- `SaveImage`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `RandomNoise`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Note`
- `ImageConcanate`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`ImageConcanate`、`UNETLoader`、`VAELoader`、`Flux2Scheduler`、`CLIPLoader`、`VAEDecode`、`BasicGuider`、`FluxGuidance`、`SaveImage`、`ImageScaleToTotalPixels`、`ReferenceLatent`、`VAEEncode`、`easy promptList`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`RandomNoise`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
