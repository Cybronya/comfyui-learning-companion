---
key: 图片生成/图生图/FLUX.2-klein 图像编辑- 图像编辑-快速出图图像生成zip输出_2022641416794542081.json
name: FLUX.2-klein 图像编辑- 图像编辑-快速出图图像生成zip输出_2022641416794542081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2-klein 图像编辑- 图像编辑-快速出图图像生成zip输出_2022641416794542081.json
hash: c9572cda94a7ac9a
coverage: 1
learned_at: 2026-10-23 10:54:13
nodes: [ConditioningZeroOut, CLIPLoader, UNETLoader, VAELoader, Int, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, KSampler, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, CompressImages, CR Text, CR Text, LoadImage, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.2-klein 图像编辑- 图像编辑-快速出图图像生成zip输出_2022641416794542081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2-klein 图像编辑- 图像编辑-快速出图图像生成zip输出_2022641416794542081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（15 个）：
- `ConditioningZeroOut`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode` ★核心
- `CompressImages`
- `CR Text`
- `CR Text`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `42`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`ConditioningZeroOut`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyFlux2LatentImage`、`KSampler`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`VAEDecode`、`CompressImages`、`CR Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPLoader、ConditioningZeroOut、LoadImage、EmptyFlux2LatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
