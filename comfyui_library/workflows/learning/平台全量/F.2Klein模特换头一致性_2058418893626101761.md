---
key: 平台全量/F.2Klein模特换头一致性_2058418893626101761.json
name: F.2Klein模特换头一致性_2058418893626101761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/F.2Klein模特换头一致性_2058418893626101761.json
hash: 9c8c949abee3117c
coverage: 0.875
learned_at: 2026-11-14 00:24:09
nodes: [ConditioningZeroOut, EmptyFlux2LatentImage, UNETLoader, CLIPLoader, VAELoader, easy imageConcat, easy imageConcat, Flux2KleinEditTextEncode_EditUtils, LoraLoaderModelOnly, VAEDecode, SaveImage, LoadImage, SaveImage, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, RMBG, PreviewImage, ClothesSegment, Int, PreviewImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 221838742448930, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/F.2Klein模特换头一致性_2058418893626101761.json

> 来源文件 `comfyui_library/workflows/平台全量/F.2Klein模特换头一致性_2058418893626101761.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy imageConcat`
- `easy imageConcat`
- `Flux2KleinEditTextEncode_EditUtils`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `RMBG`
- `PreviewImage`
- `ClothesSegment`
- `Int`
- `PreviewImage`

## 关键参数

- `seed` = `221838742448930`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`ConditioningZeroOut`、`EmptyFlux2LatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`easy imageConcat`、`Flux2KleinEditTextEncode_EditUtils`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`LoadImage`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`RMBG`、`ClothesSegment`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
