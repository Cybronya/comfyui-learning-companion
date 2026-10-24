---
key: 图片生成/图生图/千府AI-Flux.2_Klein高清洗图工作流_2032316645363949570.json
name: 千府AI-Flux.2_Klein高清洗图工作流_2032316645363949570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千府AI-Flux.2_Klein高清洗图工作流_2032316645363949570.json
hash: c6f006bc1e0f1785
coverage: 0.913043
learned_at: 2026-10-23 12:28:34
nodes: [Anything Everywhere, CLIPTextEncode, VAELoader, SaveImage, CFGGuider, RandomNoise, VAEDecode, KSamplerSelect, CLIPLoader, UNETLoader, SamplerCustomAdvanced, CLIPTextEncode, Text Multiline, LoadImage, Image Comparer (rgthree), ModelPatchTorchSettings, GetImageSize, VAEEncode, ReferenceLatent, ReferenceLatent, EmptyFlux2LatentImage, Flux2Scheduler, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 图片生成/图生图/千府AI-Flux.2_Klein高清洗图工作流_2032316645363949570.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千府AI-Flux.2_Klein高清洗图工作流_2032316645363949570.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SaveImage`
- `CFGGuider`
- `RandomNoise`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `LoadImage`
- `Image Comparer (rgthree)`
- `ModelPatchTorchSettings`
- `GetImageSize`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **91%**（21/23）

**有卡**：`CLIPTextEncode`、`VAELoader`、`SaveImage`、`CFGGuider`、`RandomNoise`、`VAEDecode`、`KSamplerSelect`、`CLIPLoader`、`UNETLoader`、`SamplerCustomAdvanced`、`Text Multiline`、`LoadImage`、`ModelPatchTorchSettings`、`GetImageSize`、`VAEEncode`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider
