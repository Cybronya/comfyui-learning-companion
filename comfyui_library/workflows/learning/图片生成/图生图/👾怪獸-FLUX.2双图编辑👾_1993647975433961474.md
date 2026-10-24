---
key: 图片生成/图生图/👾怪獸-FLUX.2双图编辑👾_1993647975433961474.json
name: 👾怪獸-FLUX.2双图编辑👾_1993647975433961474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/👾怪獸-FLUX.2双图编辑👾_1993647975433961474.json
hash: b82205a7a56e75ed
coverage: 0.916667
learned_at: 2026-10-23 13:39:24
nodes: [CLIPLoader, UNETLoader, VAELoader, ImageScaleToTotalPixels, ImageScaleToTotalPixels, KSamplerSelect, EmptyFlux2LatentImage, Flux2Scheduler, BasicGuider, SamplerCustomAdvanced, VAEDecode, SaveImage, CLIPTextEncode, VAEEncode, FluxGuidance, VAEEncode, ReferenceLatent, ReferenceLatent, RandomNoise, PrimitiveInt, PrimitiveInt, LoadImage, LoadImage, CR Prompt Text]
patterns: []
missing: []
---

# 图片生成/图生图/👾怪獸-FLUX.2双图编辑👾_1993647975433961474.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/👾怪獸-FLUX.2双图编辑👾_1993647975433961474.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `FluxGuidance`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`KSamplerSelect`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`VAEEncode`、`FluxGuidance`、`ReferenceLatent`、`RandomNoise`、`LoadImage`、`CR Prompt Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
