---
key: 图片生成/文生图/【AI小兵哥】Flux.2-多图编辑工作流_1994221492407828481.json
name: 【AI小兵哥】Flux.2-多图编辑工作流_1994221492407828481
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【AI小兵哥】Flux.2-多图编辑工作流_1994221492407828481.json
hash: 59895b8cfb9b638b
coverage: 0.96875
learned_at: 2026-10-19 21:33:19
nodes: [ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, LoadImage, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, LoadImage, ImageScaleToTotalPixels, VAEEncode, ReferenceLatent, CLIPLoader, BasicGuider, VAELoader, SamplerCustomAdvanced, Flux2Scheduler, KSamplerSelect, FluxGuidance, CLIPTextEncode, easy int, easy int, LoadImage, VAEDecode, EmptyFlux2LatentImage, RandomNoise, ModelPatchTorchSettings, ApplySageAttention, EasyCache, UNETLoader, UnetLoaderGGUF, SaveImage, PreviewImage]
patterns: []
missing: []
---

# 图片生成/文生图/【AI小兵哥】Flux.2-多图编辑工作流_1994221492407828481.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【AI小兵哥】Flux.2-多图编辑工作流_1994221492407828481.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `CLIPLoader`
- `BasicGuider`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `easy int`
- `easy int`
- `LoadImage`
- `VAEDecode` ★核心
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `ModelPatchTorchSettings`
- `ApplySageAttention`
- `EasyCache`
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `SaveImage`
- `PreviewImage`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`ImageScaleToTotalPixels`、`VAEEncode`、`ReferenceLatent`、`LoadImage`、`CLIPLoader`、`BasicGuider`、`VAELoader`、`SamplerCustomAdvanced`、`Flux2Scheduler`、`KSamplerSelect`、`FluxGuidance`、`CLIPTextEncode`、`easy int`、`VAEDecode`、`EmptyFlux2LatentImage`、`RandomNoise`、`ModelPatchTorchSettings`、`ApplySageAttention`、`EasyCache`、`UNETLoader`、`UnetLoaderGGUF`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、FluxGuidance、KSamplerSelect
