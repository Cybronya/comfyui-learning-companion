---
key: 图片生成/图生图/F.2Klein提取3d立体服装_2056216125565874178.json
name: F.2Klein提取3d立体服装_2056216125565874178
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein提取3d立体服装_2056216125565874178.json
hash: dc7c6e21414c6a3c
coverage: 1
learned_at: 2026-10-23 10:52:47
nodes: [VAELoader, CLIPLoader, ConditioningZeroOut, VAEDecode, CFGNorm, VAEEncode, Flux2KleinEditTextEncode_EditUtils, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, CR Text, LoraLoaderModelOnly, KSampler, SaveImage, LoadImage, ModelSamplingAuraFlow, Int, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1102637447523096, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2Klein提取3d立体服装_2056216125565874178.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein提取3d立体服装_2056216125565874178.json`

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

- `seed` = `1102637447523096`
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
