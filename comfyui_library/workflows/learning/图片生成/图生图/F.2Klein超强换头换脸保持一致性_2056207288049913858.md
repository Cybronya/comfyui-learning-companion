---
key: 图片生成/图生图/F.2Klein超强换头换脸保持一致性_2056207288049913858.json
name: F.2Klein超强换头换脸保持一致性_2056207288049913858
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein超强换头换脸保持一致性_2056207288049913858.json
hash: 468dd258b175e020
coverage: 0.863636
learned_at: 2026-10-23 10:52:49
nodes: [LayerUtility: ImageScaleByAspectRatio V2, SolidMask, easy ifElse, easy isMaskEmpty, LoadRembgByBiRefNetModel, RembgByBiRefNet, LoraLoaderModelOnly, Flux2KleinEditTextEncode_EditUtils, CLIPLoader, VAELoader, UNETLoader, ConditioningZeroOut, KSampler, VAEDecode, Image Comparer (rgthree), EmptyFlux2LatentImage, PreviewImage, SaveImage, ImpactInt, CR Prompt Text, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1045800799876347, "steps": 5}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2Klein超强换头换脸保持一致性_2056207288049913858.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein超强换头换脸保持一致性_2056207288049913858.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SolidMask`
- `easy ifElse`
- `easy isMaskEmpty`
- `LoadRembgByBiRefNetModel`
- `RembgByBiRefNet`
- `LoraLoaderModelOnly` ★核心
- `Flux2KleinEditTextEncode_EditUtils`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `EmptyFlux2LatentImage`
- `PreviewImage`
- `SaveImage`
- `ImpactInt`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `1045800799876347`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`SolidMask`、`easy isMaskEmpty`、`LoadRembgByBiRefNetModel`、`RembgByBiRefNet`、`LoraLoaderModelOnly`、`Flux2KleinEditTextEncode_EditUtils`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`EmptyFlux2LatentImage`、`SaveImage`、`ImpactInt`、`CR Prompt Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
