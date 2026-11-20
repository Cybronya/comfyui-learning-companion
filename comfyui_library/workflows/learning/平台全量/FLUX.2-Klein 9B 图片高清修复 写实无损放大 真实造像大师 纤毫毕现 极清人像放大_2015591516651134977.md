---
key: 平台全量/FLUX.2-Klein 9B 图片高清修复 写实无损放大 真实造像大师 纤毫毕现 极清人像放大_2015591516651134977.json
name: FLUX.2-Klein 9B 图片高清修复 写实无损放大 真实造像大师 纤毫毕现 极清人像放大_2015591516651134977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.2-Klein 9B 图片高清修复 写实无损放大 真实造像大师 纤毫毕现 极清人像放大_2015591516651134977.json
hash: 4a031dcb5d4bc5f4
coverage: 0.76
learned_at: 2026-11-14 00:25:10
nodes: [EmptyFlux2LatentImage, Flux2Scheduler, ReferenceLatent, VAEEncode, UNETLoader, VAELoader, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, PlaySound|pysssss, RandomNoise, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, CFGGuider, CLIPTextEncode, CLIPTextEncode, CLIPLoader, ReferenceLatent, PrimitiveStringMultiline, SamplerCustomAdvanced, ImpactSwitch, Image Comparer (rgthree), LoadImage, SaveImage]
patterns: []
missing: []
---

# 平台全量/FLUX.2-Klein 9B 图片高清修复 写实无损放大 真实造像大师 纤毫毕现 极清人像放大_2015591516651134977.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.2-Klein 9B 图片高清修复 写实无损放大 真实造像大师 纤毫毕现 极清人像放大_2015591516651134977.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `PlaySound|pysssss`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ReferenceLatent`
- `PrimitiveStringMultiline`
- `SamplerCustomAdvanced` ★核心
- `ImpactSwitch`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`

## 知识

覆盖率 **76%**（19/25）

**有卡**：`EmptyFlux2LatentImage`、`Flux2Scheduler`、`ReferenceLatent`、`VAEEncode`、`UNETLoader`、`VAELoader`、`KSamplerSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`PlaySound|pysssss`、`RandomNoise`、`CFGGuider`、`CLIPTextEncode`、`CLIPLoader`、`SamplerCustomAdvanced`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect
