---
key: 图片生成/图生图/FLUX.2 双图融合_1993494554741587970.json
name: FLUX.2 双图融合_1993494554741587970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 双图融合_1993494554741587970.json
hash: 32942c3144bc0309
coverage: 0.913043
learned_at: 2026-10-23 10:54:08
nodes: [SamplerCustomAdvanced, ImageScaleToTotalPixels, FluxGuidance, ImageScaleToTotalPixels, VAEEncode, VAEEncode, ReferenceLatent, ReferenceLatent, EmptyFlux2LatentImage, RandomNoise, KSamplerSelect, Flux2Scheduler, BasicGuider, VAEDecode, UNETLoader, CLIPLoader, VAELoader, LoadImage, LoadImage, SaveImage, CLIPTextEncode, PrimitiveNode, PrimitiveNode]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 双图融合_1993494554741587970.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 双图融合_1993494554741587970.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `SamplerCustomAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `BasicGuider`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `PrimitiveNode`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`SamplerCustomAdvanced`、`ImageScaleToTotalPixels`、`FluxGuidance`、`VAEEncode`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`RandomNoise`、`KSamplerSelect`、`Flux2Scheduler`、`BasicGuider`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`SaveImage`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
