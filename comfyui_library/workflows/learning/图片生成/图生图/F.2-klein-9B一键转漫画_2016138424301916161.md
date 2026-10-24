---
key: 图片生成/图生图/F.2-klein-9B一键转漫画_2016138424301916161.json
name: F.2-klein-9B一键转漫画_2016138424301916161
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2-klein-9B一键转漫画_2016138424301916161.json
hash: 3cbbba52ed615ab5
coverage: 1
learned_at: 2026-10-23 10:52:40
nodes: [RandomNoise, KSamplerSelect, EmptyFlux2LatentImage, SamplerCustomAdvanced, CLIPLoader, UNETLoader, Flux2Scheduler, VAEDecode, SaveImage, CLIPTextEncode, ImageScaleToTotalPixels, VAELoader, ReferenceLatent, CFGGuider, VAEEncode, ReferenceLatent, LoadImage, CLIPTextEncode, LoraLoaderModelOnly, GetImageSize]
patterns: []
missing: []
---

# 图片生成/图生图/F.2-klein-9B一键转漫画_2016138424301916161.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2-klein-9B一键转漫画_2016138424301916161.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `RandomNoise`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAELoader`
- `ReferenceLatent`
- `CFGGuider`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `GetImageSize`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`RandomNoise`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`CLIPLoader`、`UNETLoader`、`Flux2Scheduler`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`ImageScaleToTotalPixels`、`VAELoader`、`ReferenceLatent`、`CFGGuider`、`VAEEncode`、`LoadImage`、`LoraLoaderModelOnly`、`GetImageSize`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider
