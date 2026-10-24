---
key: 图片生成/图生图/flux2.0图生图_1994969105419657218.json
name: flux2.0图生图_1994969105419657218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux2.0图生图_1994969105419657218.json
hash: 83466d7d1c2a35d7
coverage: 1
learned_at: 2026-10-23 11:36:30
nodes: [RandomNoise, BasicGuider, VAEDecode, UNETLoader, CLIPLoader, FluxGuidance, VAELoader, KSamplerSelect, Flux2Scheduler, SamplerCustomAdvanced, EmptyFlux2LatentImage, ReferenceLatent, VAEEncode, ReferenceLatent, VAEEncode, 孤海图像缩放按像素, 孤海图像缩放按像素, SaveImage, Width/Height Literal (Image Saver), Width/Height Literal, LoadImage, LoadImage, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/flux2.0图生图_1994969105419657218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux2.0图生图_1994969105419657218.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `RandomNoise`
- `BasicGuider`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `FluxGuidance`
- `VAELoader`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `孤海图像缩放按像素`
- `孤海图像缩放按像素`
- `SaveImage`
- `Width/Height Literal (Image Saver)`
- `Width/Height Literal`
- `LoadImage`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **100%**（23/23）

**有卡**：`RandomNoise`、`BasicGuider`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`FluxGuidance`、`VAELoader`、`KSamplerSelect`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`ReferenceLatent`、`VAEEncode`、`孤海图像缩放按像素`、`SaveImage`、`Width/Height Literal (Image Saver)`、`Width/Height Literal`、`LoadImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
