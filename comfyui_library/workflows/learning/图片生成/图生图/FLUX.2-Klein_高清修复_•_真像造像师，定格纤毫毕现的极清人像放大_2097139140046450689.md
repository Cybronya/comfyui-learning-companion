---
key: 图片生成/图生图/FLUX.2-Klein_高清修复_•_真像造像师，定格纤毫毕现的极清人像放大_2097139140046450689.json
name: FLUX.2-Klein_高清修复_•_真像造像师，定格纤毫毕现的极清人像放大_2097139140046450689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2-Klein_高清修复_•_真像造像师，定格纤毫毕现的极清人像放大_2097139140046450689.json
hash: 7ca4ceb0d9b07bcd
coverage: 0.769231
learned_at: 2026-10-21 00:39:07
nodes: [EmptyFlux2LatentImage, Flux2Scheduler, ReferenceLatent, VAEEncode, VAELoader, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, SamplerCustomAdvanced, PlaySound|pysssss, Image Comparer (rgthree), RandomNoise, LoadImage, SaveImage, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, CFGGuider, CLIPTextEncode, CLIPTextEncode, CLIPLoader, ReferenceLatent, ImpactSwitch, UNETLoader, LoraLoaderModelOnly, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2-Klein_高清修复_•_真像造像师，定格纤毫毕现的极清人像放大_2097139140046450689.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2-Klein_高清修复_•_真像造像师，定格纤毫毕现的极清人像放大_2097139140046450689.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
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
- `LoadImage`
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
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`EmptyFlux2LatentImage`、`Flux2Scheduler`、`ReferenceLatent`、`VAEEncode`、`VAELoader`、`KSamplerSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`SamplerCustomAdvanced`、`PlaySound|pysssss`、`RandomNoise`、`LoadImage`、`SaveImage`、`CFGGuider`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、CFGGuider
