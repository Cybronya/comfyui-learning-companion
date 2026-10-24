---
key: 图片生成/图生图/最新Flux 2.0多图编辑工作流（支持直接输入中文提示词）_1993527135818235906.json
name: 最新Flux 2.0多图编辑工作流（支持直接输入中文提示词）_1993527135818235906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最新Flux 2.0多图编辑工作流（支持直接输入中文提示词）_1993527135818235906.json
hash: 03d8ba7e7ff18b14
coverage: 0.9375
learned_at: 2026-10-23 13:06:49
nodes: [PrimitiveNode, VAEEncode, PrimitiveNode, SamplerCustomAdvanced, ImageConcanate, VAEEncode, VAEEncode, BasicGuider, EmptyFlux2LatentImage, ReferenceLatent, VAEDecode, CLIPTextEncode, ImageConcanate, SaveImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, LoadImage, LoadImage, easy promptList, Flux2Scheduler, KSamplerSelect, RandomNoise, FluxGuidance, ReferenceLatent, ReferenceLatent, UNETLoader, VAELoader, CLIPLoader, ImageConcanate, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/最新Flux 2.0多图编辑工作流（支持直接输入中文提示词）_1993527135818235906.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最新Flux 2.0多图编辑工作流（支持直接输入中文提示词）_1993527135818235906.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `PrimitiveNode`
- `VAEEncode` ★核心
- `PrimitiveNode`
- `SamplerCustomAdvanced` ★核心
- `ImageConcanate`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `BasicGuider`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ImageConcanate`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy promptList`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `FluxGuidance`
- `ReferenceLatent`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `ImageConcanate`
- `SaveImage`

## 知识

覆盖率 **94%**（30/32）

**有卡**：`VAEEncode`、`SamplerCustomAdvanced`、`ImageConcanate`、`BasicGuider`、`EmptyFlux2LatentImage`、`ReferenceLatent`、`VAEDecode`、`CLIPTextEncode`、`SaveImage`、`ImageScaleToTotalPixels`、`LoadImage`、`easy promptList`、`Flux2Scheduler`、`KSamplerSelect`、`RandomNoise`、`FluxGuidance`、`UNETLoader`、`VAELoader`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
