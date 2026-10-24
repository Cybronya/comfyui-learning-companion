---
key: 图片生成/图生图/flux2.0-去水印_1995756422661025793.json
name: flux2.0-去水印_1995756422661025793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux2.0-去水印_1995756422661025793.json
hash: fd65f629d7c1f36b
coverage: 0.95
learned_at: 2026-10-23 11:36:30
nodes: [CLIPTextEncode, VAEEncode, CR Text, Flux2Scheduler, SamplerCustomAdvanced, PreviewImage, ReferenceLatent, BasicGuider, VAEDecode, RandomNoise, KSamplerSelect, CLIPLoader, UNETLoader, load_GGUF, FluxGuidance, UnetLoaderGGUF, VAELoader, ImageScaleToTotalPixels, LoadImage, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/flux2.0-去水印_1995756422661025793.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux2.0-去水印_1995756422661025793.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CR Text`
- `Flux2Scheduler`
- `SamplerCustomAdvanced` ★核心
- `PreviewImage`
- `ReferenceLatent`
- `BasicGuider`
- `VAEDecode` ★核心
- `RandomNoise`
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `load_GGUF`
- `FluxGuidance`
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`CLIPTextEncode`、`VAEEncode`、`CR Text`、`Flux2Scheduler`、`SamplerCustomAdvanced`、`ReferenceLatent`、`BasicGuider`、`VAEDecode`、`RandomNoise`、`KSamplerSelect`、`CLIPLoader`、`UNETLoader`、`load_GGUF`、`FluxGuidance`、`UnetLoaderGGUF`、`VAELoader`、`ImageScaleToTotalPixels`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
