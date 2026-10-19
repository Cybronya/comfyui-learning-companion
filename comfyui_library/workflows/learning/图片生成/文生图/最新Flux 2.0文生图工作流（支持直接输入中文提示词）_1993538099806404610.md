---
key: 图片生成/文生图/最新Flux 2.0文生图工作流（支持直接输入中文提示词）_1993538099806404610.json
name: 最新Flux 2.0文生图工作流（支持直接输入中文提示词）_1993538099806404610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/最新Flux 2.0文生图工作流（支持直接输入中文提示词）_1993538099806404610.json
hash: 77ee2585085bdb7c
coverage: 1
learned_at: 2026-10-19 21:33:37
nodes: [VAEEncode, SamplerCustomAdvanced, ImageConcanate, VAEEncode, VAEEncode, EmptyFlux2LatentImage, ReferenceLatent, VAEDecode, CLIPTextEncode, ImageConcanate, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, LoadImage, LoadImage, Flux2Scheduler, KSamplerSelect, RandomNoise, ReferenceLatent, ReferenceLatent, UNETLoader, VAELoader, ImageConcanate, ImageScaleToTotalPixels, SaveImage, BasicGuider, CLIPLoader, FluxGuidance, easy promptList, CR Text, easy int, easy int]
patterns: []
missing: []
---

# 图片生成/文生图/最新Flux 2.0文生图工作流（支持直接输入中文提示词）_1993538099806404610.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/最新Flux 2.0文生图工作流（支持直接输入中文提示词）_1993538099806404610.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `VAEEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ImageConcanate`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `ReferenceLatent`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `VAELoader`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `BasicGuider`
- `CLIPLoader`
- `FluxGuidance`
- `easy promptList`
- `CR Text`
- `easy int`
- `easy int`

## 知识

覆盖率 **100%**（32/32）

**有卡**：`VAEEncode`、`SamplerCustomAdvanced`、`ImageConcanate`、`EmptyFlux2LatentImage`、`ReferenceLatent`、`VAEDecode`、`CLIPTextEncode`、`ImageScaleToTotalPixels`、`LoadImage`、`Flux2Scheduler`、`KSamplerSelect`、`RandomNoise`、`UNETLoader`、`VAELoader`、`SaveImage`、`BasicGuider`、`CLIPLoader`、`FluxGuidance`、`easy promptList`、`CR Text`、`easy int`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
