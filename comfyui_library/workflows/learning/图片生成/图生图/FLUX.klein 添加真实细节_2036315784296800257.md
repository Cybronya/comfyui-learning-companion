---
key: 图片生成/图生图/FLUX.klein 添加真实细节_2036315784296800257.json
name: FLUX.klein 添加真实细节_2036315784296800257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.klein 添加真实细节_2036315784296800257.json
hash: 6c6cb3a92195caac
coverage: 0.95
learned_at: 2026-10-23 10:54:17
nodes: [SamplerCustomAdvanced, EmptyFlux2LatentImage, Flux2Scheduler, CFGGuider, KSamplerSelect, RandomNoise, GetImageSize, ImageScaleToTotalPixels, CLIPLoader, CLIPTextEncode, VAEEncode, ReferenceLatent, ConditioningZeroOut, VAEDecode, VAELoader, LoraLoaderModelOnly, UNETLoader, LoadImage, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.klein 添加真实细节_2036315784296800257.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.klein 添加真实细节_2036315784296800257.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`GetImageSize`、`ImageScaleToTotalPixels`、`CLIPLoader`、`CLIPTextEncode`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`VAEDecode`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage
