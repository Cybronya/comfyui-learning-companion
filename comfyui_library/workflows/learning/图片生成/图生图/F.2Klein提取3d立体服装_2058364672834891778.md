---
key: 图片生成/图生图/F.2Klein提取3d立体服装_2058364672834891778.json
name: F.2Klein提取3d立体服装_2058364672834891778
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein提取3d立体服装_2058364672834891778.json
hash: 6889edb0cf5e2ef0
coverage: 1
learned_at: 2026-10-21 00:38:57
nodes: [VAELoader, CLIPLoader, ConditioningZeroOut, VAEDecode, CFGNorm, VAEEncode, Flux2KleinEditTextEncode_EditUtils, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, CR Text, LoraLoaderModelOnly, KSampler, SaveImage, LoadImage, ModelSamplingAuraFlow, Int, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 816791003825682, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2Klein提取3d立体服装_2058364672834891778.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein提取3d立体服装_2058364672834891778.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAELoader`
- `CLIPLoader`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `CFGNorm`
- `VAEEncode` ★核心
- `Flux2KleinEditTextEncode_EditUtils`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `SaveImage`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `Int`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `816791003825682`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`VAELoader`、`CLIPLoader`、`ConditioningZeroOut`、`VAEDecode`、`CFGNorm`、`VAEEncode`、`Flux2KleinEditTextEncode_EditUtils`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`LoraLoaderModelOnly`、`KSampler`、`SaveImage`、`LoadImage`、`ModelSamplingAuraFlow`、`Int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
