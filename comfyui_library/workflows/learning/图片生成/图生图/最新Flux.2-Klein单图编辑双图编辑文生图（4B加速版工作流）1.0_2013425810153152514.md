---
key: 图片生成/图生图/最新Flux.2-Klein单图编辑双图编辑文生图（4B加速版工作流）1.0_2013425810153152514.json
name: 最新Flux.2-Klein单图编辑双图编辑文生图（4B加速版工作流）1.0_2013425810153152514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/最新Flux.2-Klein单图编辑双图编辑文生图（4B加速版工作流）1.0_2013425810153152514.json
hash: bdf696099b9a5013
coverage: 1
learned_at: 2026-10-23 13:06:50
nodes: [VAELoader, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, RandomNoise, KSamplerSelect, Flux2Scheduler, EmptyFlux2LatentImage, CFGGuider, VAEDecode, SamplerCustomAdvanced, GetImageSize+, ReferenceLatent, CLIPTextEncode, SaveImage, LoadImage, CLIPLoader, UNETLoader, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/最新Flux.2-Klein单图编辑双图编辑文生图（4B加速版工作流）1.0_2013425810153152514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/最新Flux.2-Klein单图编辑双图编辑文生图（4B加速版工作流）1.0_2013425810153152514.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `CFGGuider`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetImageSize+`
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **100%**（20/20）

**有卡**：`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`VAEEncode`、`ReferenceLatent`、`RandomNoise`、`KSamplerSelect`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`CFGGuider`、`VAEDecode`、`SamplerCustomAdvanced`、`GetImageSize+`、`CLIPTextEncode`、`SaveImage`、`LoadImage`、`CLIPLoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
