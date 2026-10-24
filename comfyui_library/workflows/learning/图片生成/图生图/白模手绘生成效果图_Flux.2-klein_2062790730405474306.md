---
key: 图片生成/图生图/白模手绘生成效果图_Flux.2-klein_2062790730405474306.json
name: 白模手绘生成效果图_Flux.2-klein_2062790730405474306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/白模手绘生成效果图_Flux.2-klein_2062790730405474306.json
hash: a126cebb9efac778
coverage: 0.863636
learned_at: 2026-10-23 13:18:09
nodes: [CFGGuider, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, PlaySound|pysssss, CLIPTextEncode, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, VAEEncode, EmptyFlux2LatentImage, Flux2Scheduler, VAEDecode, SaveImage, Image Comparer (rgthree), CLIPLoader, VAELoader, Note, PrimitiveStringMultiline, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader]
patterns: []
missing: []
---

# 图片生成/图生图/白模手绘生成效果图_Flux.2-klein_2062790730405474306.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/白模手绘生成效果图_Flux.2-klein_2062790730405474306.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CFGGuider`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `PlaySound|pysssss`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `Note`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心

## 知识

覆盖率 **86%**（19/22）

**有卡**：`CFGGuider`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`PlaySound|pysssss`、`CLIPTextEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`VAEEncode`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`VAELoader`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
