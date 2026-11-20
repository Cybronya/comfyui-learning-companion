---
key: 平台全量/节点系列14-抠图系列01-LayerMask_ BiRefNet Ultra V2(Advance)_2037375823220576257.json
name: 节点系列14-抠图系列01-LayerMask_ BiRefNet Ultra V2(Advance)_2037375823220576257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/节点系列14-抠图系列01-LayerMask_ BiRefNet Ultra V2(Advance)_2037375823220576257.json
hash: fccfa9317204ba98
coverage: 0.68
learned_at: 2026-11-14 02:32:19
nodes: [CFGGuider, RandomNoise, CLIPTextEncode, CLIPLoader, Seed (rgthree), ConditioningZeroOut, ReferenceLatent, ReferenceLatent, VAELoader, VAEEncode, EmptyFlux2LatentImage, PreviewImage, Text, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, GetNode, KSamplerSelect, Flux2Scheduler, SaveImage, SetNode, Note, Note, Note, Image Comparer (rgthree), SamplerCustomAdvanced, VAEDecode, Note, Reroute, Image Comparer (rgthree), LayerMask: LoadBiRefNetModelV2, Note, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Image Comparer (rgthree), UNETLoader, Image Comparer (rgthree), GetNode, Note, DrawMaskOnImage, SaveImage, Image Comparer (rgthree), LayerMask: BiRefNetUltraV2, LayerMask: BiRefNetUltraV2, LayerMask: BiRefNetUltraV2, LayerMask: BiRefNetUltraV2, LoadImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/节点系列14-抠图系列01-LayerMask_ BiRefNet Ultra V2(Advance)_2037375823220576257.json

> 来源文件 `comfyui_library/workflows/平台全量/节点系列14-抠图系列01-LayerMask_ BiRefNet Ultra V2(Advance)_2037375823220576257.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `CFGGuider`
- `RandomNoise`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `Seed (rgthree)`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `PreviewImage`
- `Text`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `KSamplerSelect` ★核心
- `Flux2Scheduler`
- `SaveImage`
- `SetNode`
- `Note`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `Note`
- `Reroute`
- `Image Comparer (rgthree)`
- `LayerMask: LoadBiRefNetModelV2`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `GetNode`
- `Note`
- `DrawMaskOnImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: BiRefNetUltraV2`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **68%**（34/50）

**有卡**：`CFGGuider`、`RandomNoise`、`CLIPTextEncode`、`CLIPLoader`、`Seed (rgthree)`、`ConditioningZeroOut`、`ReferenceLatent`、`VAELoader`、`VAEEncode`、`EmptyFlux2LatentImage`、`Text`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerSelect`、`Flux2Scheduler`、`SaveImage`、`SamplerCustomAdvanced`、`VAEDecode`、`LayerMask: LoadBiRefNetModelV2`、`UNETLoader`、`DrawMaskOnImage`、`LayerMask: BiRefNetUltraV2`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、CFGGuider
