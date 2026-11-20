---
key: 图片生成/图生图/katongchongwufenjing_2115985614167429122.json
name: katongchongwufenjing_2115985614167429122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/katongchongwufenjing_2115985614167429122.json
hash: a413fc19e7a85f1c
coverage: 0.92
learned_at: 2026-10-30 23:24:47
nodes: [UNETLoader, CLIPLoader, JWStringConcat, Qwen3_VQA, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, CLIPTextEncode, CLIPTextEncode, VAEEncode, EmptyFlux2LatentImage, GetImageSize, ReferenceLatent, ReferenceLatent, Flux2Scheduler, KSamplerSelect, CFGGuider, easy promptLine, Text Multiline, SaveImage, RandomNoise, VAEDecode, SamplerCustomAdvanced, LoadImage, JjkText]
patterns: []
missing: []
---

# 图片生成/图生图/katongchongwufenjing_2115985614167429122.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/katongchongwufenjing_2115985614167429122.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `JWStringConcat`
- `Qwen3_VQA`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `ReferenceLatent`
- `ReferenceLatent`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `easy promptLine`
- `Text Multiline`
- `SaveImage`
- `RandomNoise`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `JjkText`

## 知识

覆盖率 **92%**（23/25）

**有卡**：`UNETLoader`、`CLIPLoader`、`JWStringConcat`、`Qwen3_VQA`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`EmptyFlux2LatentImage`、`GetImageSize`、`ReferenceLatent`、`Flux2Scheduler`、`KSamplerSelect`、`CFGGuider`、`easy promptLine`、`Text Multiline`、`SaveImage`、`RandomNoise`、`VAEDecode`、`SamplerCustomAdvanced`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect
