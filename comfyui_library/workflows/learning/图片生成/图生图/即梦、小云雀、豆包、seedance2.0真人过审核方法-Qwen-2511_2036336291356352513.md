---
key: 图片生成/图生图/即梦、小云雀、豆包、seedance2.0真人过审核方法-Qwen-2511_2036336291356352513.json
name: 即梦、小云雀、豆包、seedance2.0真人过审核方法-Qwen-2511_2036336291356352513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/即梦、小云雀、豆包、seedance2.0真人过审核方法-Qwen-2511_2036336291356352513.json
hash: d91b42b8d625ce71
coverage: 1
learned_at: 2026-10-23 12:33:24
nodes: [ConditioningZeroOut, KSampler, VAEDecode, ConditioningZeroOut, KSampler, EmptySD3LatentImage, VAEDecode, EmptySD3LatentImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, SaveImage, CustomAddLabel, CustomAddLabel, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "sa_solver", "scheduler": "simple", "seed": 42, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/即梦、小云雀、豆包、seedance2.0真人过审核方法-Qwen-2511_2036336291356352513.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/即梦、小云雀、豆包、seedance2.0真人过审核方法-Qwen-2511_2036336291356352513.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `ConditioningZeroOut`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `EmptySD3LatentImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `SaveImage`
- `CustomAddLabel`
- `CustomAddLabel`
- `SaveImage`

## 关键参数

- `seed` = `42`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（20/20）

**有卡**：`ConditioningZeroOut`、`KSampler`、`VAEDecode`、`EmptySD3LatentImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`SaveImage`、`CustomAddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
