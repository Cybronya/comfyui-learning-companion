---
key: 数字人/数字人/digital_combination.json_2061356509828829186.json
name: digital_combination.json_2061356509828829186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/digital_combination.json_2061356509828829186.json
hash: 647cc1e3eeac478e
coverage: 1
learned_at: 2026-10-26 01:58:30
nodes: [CFGNorm, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEdit, LoraLoaderModelOnly, ModelSamplingAuraFlow, Int, Int, Int, EmptySD3LatentImage, UNETLoader, CLIPLoader, VAELoader, KSampler, VAEDecode, LoadImage, LoadImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 550085123848181, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/digital_combination.json_2061356509828829186.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/digital_combination.json_2061356509828829186.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CFGNorm`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEdit`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `Int`
- `Int`
- `Int`
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`

## 关键参数

- `seed` = `550085123848181`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`CFGNorm`、`TextEncodeQwenImageEditPlus`、`TextEncodeQwenImageEdit`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`Int`、`EmptySD3LatentImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`VAEDecode`、`LoadImage`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
