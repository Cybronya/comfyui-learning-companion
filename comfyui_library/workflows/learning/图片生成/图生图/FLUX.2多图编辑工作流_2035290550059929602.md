---
key: 图片生成/图生图/FLUX.2多图编辑工作流_2035290550059929602.json
name: FLUX.2多图编辑工作流_2035290550059929602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2多图编辑工作流_2035290550059929602.json
hash: dfbae382a09e5cf7
coverage: 0.923077
learned_at: 2026-10-23 10:54:16
nodes: [KSamplerSelect, RandomNoise, CFGGuider, Flux2Scheduler, Int, Int, SaveImage, CR Text, ImageScale, CLIPTextEncode, CLIPTextEncode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, LoadImage, LoadImage, LoadImage, CLIPLoader, VAELoader, PreviewImage, Image Comparer (rgthree), UNETLoader, SamplerCustomAdvanced, VAEDecode, ConditioningAddImageReferenceDual, EmptyFlux2LatentImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2多图编辑工作流_2035290550059929602.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2多图编辑工作流_2035290550059929602.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `Flux2Scheduler`
- `Int`
- `Int`
- `SaveImage`
- `CR Text`
- `ImageScale`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ConditioningAddImageReferenceDual`
- `EmptyFlux2LatentImage`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`Flux2Scheduler`、`Int`、`SaveImage`、`CR Text`、`ImageScale`、`CLIPTextEncode`、`ImageScaleToTotalPixels`、`LoadImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`SamplerCustomAdvanced`、`VAEDecode`、`ConditioningAddImageReferenceDual`、`EmptyFlux2LatentImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
