---
key: 图片生成/图生图/Flux2.Klein_KV 4steps_2046833812876824578.json
name: Flux2.Klein_KV 4steps_2046833812876824578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2.Klein_KV 4steps_2046833812876824578.json
hash: 4cdf7d1ca0e18e60
coverage: 1
learned_at: 2026-10-23 11:00:52
nodes: [KSamplerSelect, SamplerCustomAdvanced, RandomNoise, VAELoader, CLIPLoader, CLIPTextEncode, VAEDecode, VAEEncode, ReferenceLatent, ReferenceLatent, GetImageSize, EmptyFlux2LatentImage, SaveImage, ImageScaleToTotalPixels, CLIPTextEncode, LoadImage, UNETLoader, CFGGuider, Flux2Scheduler]
patterns: []
missing: []
---

# 图片生成/图生图/Flux2.Klein_KV 4steps_2046833812876824578.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2.Klein_KV 4steps_2046833812876824578.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `SaveImage`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `UNETLoader` ★核心
- `CFGGuider`
- `Flux2Scheduler`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`KSamplerSelect`、`SamplerCustomAdvanced`、`RandomNoise`、`VAELoader`、`CLIPLoader`、`CLIPTextEncode`、`VAEDecode`、`VAEEncode`、`ReferenceLatent`、`GetImageSize`、`EmptyFlux2LatentImage`、`SaveImage`、`ImageScaleToTotalPixels`、`LoadImage`、`UNETLoader`、`CFGGuider`、`Flux2Scheduler`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
