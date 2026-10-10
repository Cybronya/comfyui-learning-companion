---
key: 图片生成/图生图/Flux2 Klein9b 多图融合编辑1.1_2031915076499808257.json
name: Flux2 Klein9b 多图融合编辑1.1_2031915076499808257
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux2 Klein9b 多图融合编辑1.1_2031915076499808257.json
hash: ca843ca9c0f8ea20
coverage: 0.583333
learned_at: 2026-10-10 20:48:02
nodes: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, VAEDecode, ConditioningZeroOut, VAEEncode, CLIPTextEncode, VAEEncode, ReferenceLatent, ReferenceLatent, ComfySwitchNode, ReferenceLatent, VAEEncode, ComfySwitchNode, easy isNone, easy showAnything, Image Comparer (rgthree), easy isNone, easy showAnything, ReferenceLatent, ComfySwitchNode, ComfySwitchNode, LayerUtility: ImageScaleByAspectRatio V2, easy isNone, easy showAnything, VAEEncode, easy isNone, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, Note, CLIPLoader, VAELoader, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, LoadImage, easy int, UNETLoader, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, KSampler, PDRatioSelector, ratio_selector, Int, SaveImage]
patterns: [image_to_image]
missing: [LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, easy int, easy isNone, easy isNone, easy isNone, easy isNone]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 819771896006679, "steps": 4}
discoveries: [次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识, 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识, 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识, 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux2 Klein9b 多图融合编辑1.1_2031915076499808257.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux2 Klein9b 多图融合编辑1.1_2031915076499808257.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（48 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `ComfySwitchNode`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ComfySwitchNode`
- `easy isNone`
- `easy showAnything`
- `Image Comparer (rgthree)`
- `easy isNone`
- `easy showAnything`
- `ReferenceLatent`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy isNone`
- `easy showAnything`
- `VAEEncode` ★核心
- `easy isNone`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `easy int`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `PDRatioSelector`
- `ratio_selector`
- `Int`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `819771896006679`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **58%**（28/48）

**有卡**：`LoraLoaderModelOnly`、`VAEDecode`、`ConditioningZeroOut`、`VAEEncode`、`CLIPTextEncode`、`ReferenceLatent`、`EmptyFlux2LatentImage`、`CLIPLoader`、`VAELoader`、`LoadImage`、`UNETLoader`、`KSampler`、`PDRatioSelector`、`ratio_selector`、`Int`、`SaveImage`

**缺卡**（9）：`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`easy isNone`、`easy isNone`、`easy isNone`、`easy isNone`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识
- 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识
- 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识
- 次要节点 `easy isNone` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
