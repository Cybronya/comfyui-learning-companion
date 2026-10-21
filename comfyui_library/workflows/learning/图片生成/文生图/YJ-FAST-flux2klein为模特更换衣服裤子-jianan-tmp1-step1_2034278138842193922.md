---
key: 图片生成/文生图/YJ-FAST-flux2klein为模特更换衣服裤子-jianan-tmp1-step1_2034278138842193922.json
name: YJ-FAST-flux2klein为模特更换衣服裤子-jianan-tmp1-step1_2034278138842193922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/YJ-FAST-flux2klein为模特更换衣服裤子-jianan-tmp1-step1_2034278138842193922.json
hash: 9dbb471fc8a8c233
coverage: 0.931034
learned_at: 2026-10-21 02:55:28
nodes: [CLIPLoader, KSamplerSelect, SamplerCustomAdvanced, VAEEncode, ConditioningZeroOut, CLIPTextEncode, Reroute, ReferenceLatent, ReferenceLatent, VAELoader, ReferenceLatent, VAEEncode, EmptyFlux2LatentImage, CR Text, LoadImage, LoadImage, LoadImage, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, Flux2Scheduler, VAEDecode, SaveImage, RandomNoise, CFGGuider, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, VAEEncode, CR Text]
patterns: []
missing: []
---

# 图片生成/文生图/YJ-FAST-flux2klein为模特更换衣服裤子-jianan-tmp1-step1_2034278138842193922.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/YJ-FAST-flux2klein为模特更换衣服裤子-jianan-tmp1-step1_2034278138842193922.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `Reroute`
- `ReferenceLatent`
- `ReferenceLatent`
- `VAELoader`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Flux2Scheduler`
- `VAEDecode` ★核心
- `SaveImage`
- `RandomNoise`
- `CFGGuider`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEEncode` ★核心
- `CR Text`

## 知识

覆盖率 **93%**（27/29）

**有卡**：`CLIPLoader`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEEncode`、`ConditioningZeroOut`、`CLIPTextEncode`、`ReferenceLatent`、`VAELoader`、`EmptyFlux2LatentImage`、`CR Text`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`Flux2Scheduler`、`VAEDecode`、`SaveImage`、`RandomNoise`、`CFGGuider`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、CFGGuider
