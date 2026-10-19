---
key: 图片生成/文生图/FLUX.2多图参考编辑_1994778617873883137.json
name: FLUX.2多图参考编辑_1994778617873883137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FLUX.2多图参考编辑_1994778617873883137.json
hash: 3bf3b36510f67e22
coverage: 0.925926
learned_at: 2026-10-19 21:32:28
nodes: [KSamplerSelect, Flux2Scheduler, ImageScaleToTotalPixels, SamplerCustomAdvanced, VAEDecode, UNETLoader, RandomNoise, SaveImage, CLIPLoader, VAELoader, CLIPTextEncode, EmptyFlux2LatentImage, ImageScaleToTotalPixels, VAEEncode, VAEEncode, BasicGuider, FluxGuidance, ReferenceLatent, ImageConcanate, CR Text, ImageConcanate, ReferenceLatent, PrimitiveNode, PrimitiveNode, LoadImage, LoadImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/文生图/FLUX.2多图参考编辑_1994778617873883137.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FLUX.2多图参考编辑_1994778617873883137.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `RandomNoise`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `VAEEncode` ★核心
- `BasicGuider`
- `FluxGuidance`
- `ReferenceLatent`
- `ImageConcanate`
- `CR Text`
- `ImageConcanate`
- `ReferenceLatent`
- `PrimitiveNode`
- `PrimitiveNode`
- `LoadImage`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **93%**（25/27）

**有卡**：`KSamplerSelect`、`Flux2Scheduler`、`ImageScaleToTotalPixels`、`SamplerCustomAdvanced`、`VAEDecode`、`UNETLoader`、`RandomNoise`、`SaveImage`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`EmptyFlux2LatentImage`、`VAEEncode`、`BasicGuider`、`FluxGuidance`、`ReferenceLatent`、`ImageConcanate`、`CR Text`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
