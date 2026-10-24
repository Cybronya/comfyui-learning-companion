---
key: 图片生成/图生图/FLUX.2 设计师专属商品设计全流程工作流_2045722294399537153.json
name: FLUX.2 设计师专属商品设计全流程工作流_2045722294399537153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2 设计师专属商品设计全流程工作流_2045722294399537153.json
hash: 5bc3a1a43205089d
coverage: 0.425532
learned_at: 2026-10-23 10:54:09
nodes: [CFGGuider, ReferenceLatent, VAEEncode, Flux2Scheduler, CLIPLoader, VAELoader, ReferenceLatent, Image Comparer (rgthree), Note, RandomNoise, EmptyFlux2LatentImage, PlaySound|pysssss, Note, Note, Image Comparer (rgthree), Image Comparer (rgthree), Note, Image Comparer (rgthree), Note, Image Comparer (rgthree), VAEDecode, ConditioningZeroOut, Note, Image Comparer (rgthree), SamplerCustomAdvanced, Image Comparer (rgthree), Note, Image Comparer (rgthree), KSamplerSelect, Image Comparer (rgthree), Note, Note, Image Comparer (rgthree), Image Comparer (rgthree), Note, Image Comparer (rgthree), Note, Note, Note, CLIPTextEncode, Image Comparer (rgthree), Image Comparer (rgthree), easy seed, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.2 设计师专属商品设计全流程工作流_2045722294399537153.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2 设计师专属商品设计全流程工作流_2045722294399537153.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `CFGGuider`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `Flux2Scheduler`
- `CLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `Image Comparer (rgthree)`
- `Note`
- `RandomNoise`
- `EmptyFlux2LatentImage`
- `PlaySound|pysssss`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Note`
- `Image Comparer (rgthree)`
- `Note`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `Note`
- `Image Comparer (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `Image Comparer (rgthree)`
- `Note`
- `Image Comparer (rgthree)`
- `KSamplerSelect` ★核心
- `Image Comparer (rgthree)`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Note`
- `Image Comparer (rgthree)`
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `easy seed`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader` ★核心

## 知识

覆盖率 **43%**（20/47）

**有卡**：`CFGGuider`、`ReferenceLatent`、`VAEEncode`、`Flux2Scheduler`、`CLIPLoader`、`VAELoader`、`RandomNoise`、`EmptyFlux2LatentImage`、`PlaySound|pysssss`、`VAEDecode`、`ConditioningZeroOut`、`SamplerCustomAdvanced`、`KSamplerSelect`、`CLIPTextEncode`、`easy seed`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`SaveImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
