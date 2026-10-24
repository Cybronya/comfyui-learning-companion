---
key: 图片生成/图生图/FLUX.2 klein base 版单图编辑_2012465215350251522.json
name: FLUX.2 klein base 版单图编辑_2012465215350251522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 klein base 版单图编辑_2012465215350251522.json
hash: 5ac264a895f1ddeb
coverage: 0.95
learned_at: 2026-10-23 10:54:07
nodes: [VAELoader, ReferenceLatent, VAEDecode, KSamplerSelect, ReferenceLatent, RandomNoise, SamplerCustomAdvanced, GetImageSize, EmptyFlux2LatentImage, CLIPTextEncode, CLIPLoader, CFGGuider, Flux2Scheduler, CLIPTextEncode, ImageScaleToTotalPixels, VAEEncode, SaveImage, UNETLoader, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 klein base 版单图编辑_2012465215350251522.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 klein base 版单图编辑_2012465215350251522.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `VAELoader`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `ReferenceLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CFGGuider`
- `Flux2Scheduler`
- `CLIPTextEncode` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`VAELoader`、`ReferenceLatent`、`VAEDecode`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`GetImageSize`、`EmptyFlux2LatentImage`、`CLIPTextEncode`、`CLIPLoader`、`CFGGuider`、`Flux2Scheduler`、`ImageScaleToTotalPixels`、`VAEEncode`、`SaveImage`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider、KSamplerSelect
