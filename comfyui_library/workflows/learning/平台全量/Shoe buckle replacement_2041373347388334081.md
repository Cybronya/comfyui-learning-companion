---
key: 平台全量/Shoe buckle replacement_2041373347388334081.json
name: Shoe buckle replacement_2041373347388334081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Shoe buckle replacement_2041373347388334081.json
hash: dfdd39c89810344a
coverage: 0.923077
learned_at: 2026-11-14 01:00:40
nodes: [Flux2Scheduler, CFGGuider, SamplerCustomAdvanced, ConditioningZeroOut, EmptyFlux2LatentImage, RandomNoise, ReferenceLatent, VAEEncode, ReferenceLatent, ReferenceLatent, VAEEncode, ReferenceLatent, KSamplerSelect, MarkdownNote, CLIPTextEncode, ColorMatch, VAEDecode, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, SaveImage, GetImageSize, PreviewImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/Shoe buckle replacement_2041373347388334081.json

> 来源文件 `comfyui_library/workflows/平台全量/Shoe buckle replacement_2041373347388334081.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `Flux2Scheduler`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `ColorMatch`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `GetImageSize`
- `PreviewImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`Flux2Scheduler`、`CFGGuider`、`SamplerCustomAdvanced`、`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`RandomNoise`、`ReferenceLatent`、`VAEEncode`、`KSamplerSelect`、`CLIPTextEncode`、`ColorMatch`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`SaveImage`、`GetImageSize`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
