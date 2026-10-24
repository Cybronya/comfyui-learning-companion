---
key: 图片生成/图生图/FLUX.2-Klein：高清修复 • 真像造像师，高清极清人像放大_2079820337243582466.json
name: FLUX.2-Klein：高清修复 • 真像造像师，高清极清人像放大_2079820337243582466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2-Klein：高清修复 • 真像造像师，高清极清人像放大_2079820337243582466.json
hash: 1100f5d95c7bce19
coverage: 0.777778
learned_at: 2026-10-23 10:54:13
nodes: [EmptyFlux2LatentImage, Flux2Scheduler, ReferenceLatent, VAEEncode, VAELoader, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, SamplerCustomAdvanced, PlaySound|pysssss, Image Comparer (rgthree), RandomNoise, SaveImage, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, CFGGuider, CLIPTextEncode, CLIPTextEncode, CLIPLoader, ReferenceLatent, ImpactSwitch, UNETLoader, PrimitiveStringMultiline, LoraLoaderModelOnly, LoadImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2-Klein：高清修复 • 真像造像师，高清极清人像放大_2079820337243582466.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2-Klein：高清修复 • 真像造像师，高清极清人像放大_2079820337243582466.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `PlaySound|pysssss`
- `Image Comparer (rgthree)`
- `RandomNoise`
- `SaveImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ReferenceLatent`
- `ImpactSwitch`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **78%**（21/27）

**有卡**：`EmptyFlux2LatentImage`、`Flux2Scheduler`、`ReferenceLatent`、`VAEEncode`、`VAELoader`、`KSamplerSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`SamplerCustomAdvanced`、`PlaySound|pysssss`、`RandomNoise`、`SaveImage`、`CFGGuider`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider
