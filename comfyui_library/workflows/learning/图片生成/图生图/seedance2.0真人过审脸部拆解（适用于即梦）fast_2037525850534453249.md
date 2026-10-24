---
key: 图片生成/图生图/seedance2.0真人过审脸部拆解（适用于即梦）fast_2037525850534453249.json
name: seedance2.0真人过审脸部拆解（适用于即梦）fast_2037525850534453249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/seedance2.0真人过审脸部拆解（适用于即梦）fast_2037525850534453249.json
hash: 75e9c5dba507a6d2
coverage: 1
learned_at: 2026-10-23 11:45:14
nodes: [ConditioningZeroOut, KSampler, VAEDecode, ConditioningZeroOut, EmptySD3LatentImage, VAEDecode, EmptySD3LatentImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, CustomAddLabel, CustomAddLabel, KSampler, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "simple", "seed": 42, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/seedance2.0真人过审脸部拆解（适用于即梦）fast_2037525850534453249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/seedance2.0真人过审脸部拆解（适用于即梦）fast_2037525850534453249.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `CustomAddLabel`
- `CustomAddLabel`
- `KSampler` ★核心
- `LoadImage`

## 关键参数

- `seed` = `42`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`EmptySD3LatentImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`、`CustomAddLabel`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
