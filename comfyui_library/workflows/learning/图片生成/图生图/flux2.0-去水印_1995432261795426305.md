---
key: 图片生成/图生图/flux2.0-去水印_1995432261795426305.json
name: flux2.0-去水印_1995432261795426305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux2.0-去水印_1995432261795426305.json
hash: 1eff1d2a6006814c
coverage: 0.869565
learned_at: 2026-10-23 11:36:30
nodes: [Flux2Scheduler, FluxGuidance, KSamplerSelect, PrimitiveNode, PrimitiveNode, BasicGuider, ReferenceLatent, VAEEncode, VAELoader, SamplerCustomAdvanced, VAEDecode, RandomNoise, ImageScaleToTotalPixels, CLIPLoader, load_GGUF, EmptyFlux2LatentImage, UnetLoaderGGUF, SaveImage, LoadImage, UNETLoader, CLIPTextEncode, CR Text, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/flux2.0-去水印_1995432261795426305.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux2.0-去水印_1995432261795426305.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `Flux2Scheduler`
- `FluxGuidance`
- `KSamplerSelect` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `BasicGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `load_GGUF`
- `EmptyFlux2LatentImage`
- `UnetLoaderGGUF` ★核心
- `SaveImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CR Text`
- `PreviewImage`

## 知识

覆盖率 **87%**（20/23）

**有卡**：`Flux2Scheduler`、`FluxGuidance`、`KSamplerSelect`、`BasicGuider`、`ReferenceLatent`、`VAEEncode`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecode`、`RandomNoise`、`ImageScaleToTotalPixels`、`CLIPLoader`、`load_GGUF`、`EmptyFlux2LatentImage`、`UnetLoaderGGUF`、`SaveImage`、`LoadImage`、`UNETLoader`、`CLIPTextEncode`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
